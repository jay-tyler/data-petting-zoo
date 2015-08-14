from re import match
from random import sample
from string import capwords
import pandas as pd
import numpy as np
from pandas import DataFrame
import fiona
from shapely.geometry import Point, asShape
from shapely.prepared import prep
from shapely import speedups
from rules import name_rules, geofeat_rules, wiki_codes

DATA_ROOT = ""  # TODO: wire this up

# Warn if a value is being assigned to a copy
pd.set_option('mode.chained_assignment', 'warn')

# Imports of needed data
try:
    GB = pd.read_pickle("../../data/pickles/gb.pk1")
except IOError:
    # TODO: In this case should do a bunch of stuff to get gb into namespace
    pass

try:
    NAMEFAM = pd.read_table("../../data/namefam.tab")
except IOError:
    # TODO: In this case should do a bunch of stuff to get gb into namespace
    print 'oh no'


################################
# Setup Data Functions
################################
def set_gb(file_path):
    """Read the GB.txt file from geonames and return an appropriately
    filtered DataFrame"""
    gb = pd.read_csv(file_path)
    # Trim away an initial index column
    gb = gb.ix[:, 1:20]
    column_names = [
        'geoid', 'name', 'asciiname', 'altname', 'lat', 'long',
        'feature_class', 'feature_code', 'country_code', 'cc2', 'adm1', 'adm2',
        'adm3', 'adm4', 'pop', 'elev', 'delev', 'timezone', 'moddate'
    ]
    gb.columns = column_names
    # Removing rows that correspond to Cyprus, N. Ireland, cruft etc.
    remove_these_adm1 = ['05', '00', '01', 'NIR', '03']
    for i in remove_these_adm1:
        gb = gb[gb.adm1 != i]
    # Get rid of adm1 with null values
    gb = gb[~gb.adm1.isnull()]
    # Setting a list of alternate names from altname string field
    gb['ls_altname'] = gb['altname'].dropna().apply(lambda x: x.split(','))
    # Pick only feature codes that correspond to towns and cities, see
    # http://www.geonames.org/export/codes.html
    gb = gb[gb.feature_code.isin(geofeat_rules)]
    # Clean up index
    gb.index = range(len(gb))
    return gb


def set_fam(dfin):
    """In-place setup name families for df dataframe.

    Note: this only acts on the 'name' field. Use another function to setup
    altname families

    Column changes: will add a ls_namefam column

    TODO: This is a one run deal; not idempotent. Fix.
    """
    df = dfin.copy()
    df["ls_namefam"] = np.nan
    # Iterate over rows in dataframe
    for index, row in df.iterrows():
        # For each row, check each name_rule
        for namekey, ls_regex in name_rules.iteritems():
            result = patinstr(row.loc['name'], ls_regex)
            if result:
                cur = df.loc[index, 'ls_namefam']
                if not isinstance(cur, list):
                    df.loc[index, 'ls_namefam'] = list([namekey])
                else:
                    df.loc[index, 'ls_namefam'].append(namekey)
    return df


def set_alt(df, column_names=None):
    """DataFrame should only be the dataframe that
    comes after setgb if columns is left undefined; column_names is a list of
    column names that the resulting dataframe should contain. This list should
    include 'parent.'"""

    df_alt = df.copy()
    df_alt.drop(['altname'], inplace=True, axis=1)
    df_alt.drop(['ls_altname'], inplace=True, axis=1)
    df_alt['parent'] = np.nan

    if column_names is None:
        column_names = [
            'geoid', 'name', 'parent', 'asciiname', 'lat', 'long',
            'feature_class', 'feature_code', 'country_code', 'cc2',
            'adm1', 'adm2', 'adm3', 'adm4', 'pop', 'elev', 'delev',
            'timezone', 'moddate'
        ]
    df_alt = df_alt[column_names]

    i = len(df)
    for index, row in df.iterrows():
        parent_name = row['name']
        try:
            a_names = iter(row['ls_altname'])
        except TypeError:
            pass
        else:
            for a_name in a_names:
                row['name'] = a_name
                row['parent'] = parent_name
                df_alt.ix[i] = row[column_names]
                i += 1

    df_alt[~df_alt['name'].str.contains('/')]
    return df_alt


def set_namefam_table(file_path):
    """Read the namfam csv file and load to a table"""
    return pd.read_csv(file_path)


def append_nuts3_region(dfin, shapefile_path):
    """ Take a pandas dataframe with lat and long columns and a shapefile.
    Convert coordinates to Shapely points to do a point-in-polygon check
    for each point. Append name of nuts3 region corresponding to
    point-in-polygon to the dataframe.
    This is extremely slow. Needs to be optimized with Shapely boundary box.
    """
    df = dfin.copy()
    df['nuts3'] = np.nan
    fc = fiona.open(shapefile_path)
    speedups.enable()
    for feature in fc:
        prepared_shape = prep(asShape(feature['geometry']))
        for index, row in df.iterrows():
            point = Point(row.loc['long'], row.loc['lat'])
            if prepared_shape.contains(point):
                df.loc[index, 'nuts3name'] = feature['properties']['NUTS315NM']
                df.loc[index, 'nuts3id'] = feature['properties']['NUTS315CD']
    return df


def append_2013_gva(dfin, csv_file_path):
    df = dfin.copy()
    gva = pd.read_csv(csv_file_path)
    gvasub = DataFrame(columns=['nuts3id', 'gva2013'])
    gvasub['nuts3id'], gvasub['gva2013'] = gva['nutsid'], gva['2013']
    df_gva = pd.merge(
        left=df,
        right=gvasub.dropna(),
        how='left',
        left_on='nuts3id',
        right_on='nuts3id')
    return df_gva


################################
# Helper Query Functions
################################
def patinls(slist, patlist):
    """Search each string in slist for a substring instance defined by patlist;
    return re.match if found, None if not found"""
    found = None
    try:
        strings = iter(slist)
    except TypeError:
        return
    for string in strings:
        if not found:
            for pat in patlist:
                found = match(pat, string)
                if found:
                    break
        else:
            break
    return found


def patinstr(string, patlist):
    """Search string for a substring instance defined by patlist; return
    re.match if found, None if not found"""
    found = None
    if not isinstance(string, str):
        return None
    for pat in patlist:
        found = match(pat, string)
        if found:
            break
    return found


################################
# DataFrame Query Functions
################################
def get_fam(df, namekey):
    """Return a (sub-dataframe, namekey, placename) corresponding to a
    particular namefamily. Will return None for placename from that
    namefamily"""
    def _droidfind(listin):
        result = None
        try:
            result = namekey in listin
        except TypeError:
            pass
        return result if result is True else None
    mask = df['ls_namefam'].map(lambda x: _droidfind(x))
    return df[~mask.isnull()], namekey, None


def query_random(df):
    """Return a (sub-dataframe, namekey, placename) corresponding to a
    particular namefamily. Also return a sample placename from that
    namefamily"""
    df = df.copy()
    namekeys = name_rules.keys()
    namekey = sample(namekeys, 1)[0]

    subdf = get_fam(df, namekey)
    placename = subdf['name'].sample().values[0]
    return subdf, namekey, placename


def query_name(df, placestring):
    """Return a sub-DataFrame containing boolean matches to place name.

    This is intended as a Helper function. Will attempt a more literal
    match, and if this fails, will try a loose match.
    """
    # First try to query assuming that the user formatted the placename
    # correctly, then try a looser search
    place = capwords(placestring).strip()
    query = df['name'].str.contains('.*' + place + '.*')
    if not query.any():
        place = placestring.lower().strip()
        query = df['name'].str.contains('.*' + place + '.*')
    return query


def query_placename(df, placestring):
    """Attempt to match placestring to a city with a family pattern;
    return the matching sub-DataFrame, namekey, and full placename if a match
    is made, else None

    If there are multiple associated name families, then one will be
    picked at random"""
    df = df.copy()
    query = query_name(df, placestring)
    # Return a dataframe row with the placename contained;
    # assure that this row actually has a namefam associated
    try:
        namefam_row = df[query & (~df['ls_namefam'].isnull())].sample()
    except ValueError:
        # In this case, there is no namefam_row match
        return None

    namekey = namefam_row['ls_namefam'].map(lambda x: sample(x, 1))
    # An ugly way to get the string out
    namekey = namekey.values[0][0]
    placename = namefam_row['name']
    return get_fam(df, namekey), namekey, placename.values[0]


def query_name_or_fam(df, placestring):
    """Attempt to match placestring to a city with a family pattern; else
    attempt to find a place of the same name. Return None otherwise.

    If namefamily is found: return the matching sub-DataFrame, namekey,
    and full placenameif a match

    If namefamily is not found, but placename is: return the singular placename
    row as a DataFrame, None for namekey, and full placename

    Otherwise return None."""
    df = df.copy()
    result = query_placename(df, placestring)
    if result is None:
        # Case of place with no namefam
        query = query_name(df, placestring)
        try:
            row = df[query].sample()
            result = row, None, row['name'].values[0]
        except ValueError:
            result = None
    return result


def query_pop_slice(df, popthresh):
    """Return a sub-DataFrame from DataFrame df that excludes all population
    values below the threshold"""

    return df[df['pop'] >= popthresh]


def query_namefam_table(namekey):
    """Return a dictionary containing strings of all of the elements of
    a namefam table in human readable string format"""
    row = NAMEFAM[NAMEFAM['namekey'] == namekey]
    if row.shape[0] == 0:
        # Case of asking for a namekey that doesn't exist
        return None
    toreturn = dict()

    # Turning wiki_code characters into a human readable string
    wiki_str = ""
    for code in row['wiki_codes'].values[0].split():
        frag = wiki_codes.get(code.rstrip(',').lstrip())
        frag = frag if frag is not None else ""
        wiki_str += "{}, ".format(frag)
    wiki_str = wiki_str.rstrip(", ")
    toreturn['wiki_codes'] = wiki_str
    for colname in ['namekey', 'humandef', 'lan_notes', 'human_namekey']:
        val = row[colname].values[0]
        if pd.isnull(val):
            val = None
        toreturn[colname] = val
    # toreturn['wiki_codes'] = wiki_str.rstrip(", ")
    # toreturn['namekey'] = row['namekey'].values[0]
    # toreturn['humandef'] = row['humandef'].values[0]
    # toreturn['lan_notes'] = row['lan_notes'].values[0]
    # toreturn['human_namekey'] = row['human_namekey'].values[0]
    return toreturn


if __name__ == "__main__":
    gbf = 'data/pristine/GB.txt'
    gb = set_gb(gbf)
    gb2 = set_fam(gb)

    print gb2['ls_namefam'].dropna()
