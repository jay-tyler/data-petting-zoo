import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from re import match
from random import choice
from string import capwords, strip
from rules import name_rules, geofeat_rules

# Warn if a value is being assigned to a copy
pd.set_option('mode.chained_assignment', 'warn')

# Imports of needed data
try:
    gb = pd.read_pickle("data/pickles/gb.pk1")
except IOError:
    # TODO: In this case should do a bunch of stuff to get gb into namespace
    pass


def setgb(file_path):
    """Read the GB.txt file from geonames and return an appropriately
    filtered DataFrame"""
    gb = pd.read_table(file_path)
    column_names = ['geoid', 'name', 'asciiname', 'altname', 'lat', 'long',
        'feature_class', 'feature_code', 'country_code', 'cc2', 'adm1', 'adm2',
        'adm3', 'adm4', 'pop', 'elev', 'delev', 'timezone', 'moddate']
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


def setfam(dfin):
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


def getfamdf(df, namekey):
    """Get dataframe subset from df for rows belonging to the family
    which is a sub"""
    def _droidfind(listin):
        result = None
        try:
            result = namekey in listin
        except TypeError:
            pass
        return result if result is True else None
    mask = df['ls_namefam'].map(lambda x: _droidfind(x))
    return df[~mask.isnull()]


def setalt(df, column_names=None):
    """DataFrame should only be the dataframe that
    comes after setgb if columns is left undefined; column_names is a list of
    column names that the resulting dataframe should contain. This list should
    include 'parent.'"""

    df_alt = df.copy()
    df_alt.drop(['altname'], inplace=True, axis=1)
    df_alt.drop(['ls_altname'], inplace=True, axis=1)
    df_alt['parent'] = np.nan

    if column_names is None:
        column_names = ['geoid', 'name', 'parent', 'asciiname', 'lat', 'long',
                     'feature_class', 'feature_code', 'country_code', 'cc2',
                     'adm1', 'adm2', 'adm3', 'adm4', 'pop', 'elev', 'delev',
                     'timezone', 'moddate']
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


def random_query(df):
    """Return a sub-dataframe corresponding to a particular namefamily. 
    Also return a sample placename from that namefamily"""
    namekey = choice(name_rules.keys())
    subdf = getfamdf(df, namekey)
    placename = choice(subdf['name'])
    return subdf, placename


def placename_query(df, placestring):
    """Attempt to match placestring to a city with a family pattern; 
    return the matching sub-DataFrame and namekey if a match is made"""
    # First try to query assuming that the user formatted the placename
    # correctly
    place = capwords(placestring).strip()
    query = df['name'].str.contains(place)
    if not query.any():
        place = placestring.lower().strip()
        query = df['name'].str.contains(place)


    return df(query)
    ##TODOTODOTODO

if __name__ == "__main__":
    gbf = 'data/pristine/GB.txt'
    gb = setgb(gbf)
    gb2 = setfam(gb)

    print gb2['ls_namefam'].dropna()


# patlist = name_rules[namekey]
# invmask = gb['ls_altname'].map(lambda x:patinls(x, patlist)).isnull()
# return df[~invmask]
