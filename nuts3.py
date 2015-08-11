import numpy as np
import pandas as pd
from pandas import DataFrame
import fiona
from shapely.geometry import Point, asShape
from shapely.prepared import prep
from shapely import speedups


def append_nuts3_region(dfin, shapefile):
    """ Take a pandas dataframe with lat and long columns and a shapefile.
    Convert coordinates to Shapely points to do a point-in-polygon check
    for each point. Append name of nuts3 region corresponding to point-in-polygon
    to the dataframe.
    This is extremely slow. Needs to be optimized with Shapely boundary box.
    """
    df = dfin.copy()
    df['nuts3'] = np.nan
    fc = fiona.open(shapefile)
    speedups.enable()
    for feature in fc:
        prepared_shape = prep(asShape(feature['geometry']))
        for index, row in df.iterrows():
            point = Point(row.loc['long'], row.loc['lat'])
            if prepared_shape.contains(point):
                df.loc[index, 'nuts3name'] = feature['properties']['NUTS315NM']
                df.loc[index, 'nuts3id'] = feature['properties']['NUTS315CD']
    return df


def append_2013_gva(dfin):
    df = dfin.copy()
    gva = pd.read_csv('../gvanuts32014.csv')
    gvasub = DataFrame(columns=['nuts3id', 'gva2013'])
    gvasub['nuts3id'], gvasub['gva2013'] = gva['nutsid'], gva['2013']
    df_gva = pd.merge(
        left=df,
        right=gvasub.dropna(),
        how='left',
        left_on='nuts3id',
        right_on='nuts3id')
    return df_gva
