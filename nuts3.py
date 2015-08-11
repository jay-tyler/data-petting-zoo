import numpy as np
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
                df.loc[index, 'nuts3'] = feature['properties']['NUTS315NM']
    return df
