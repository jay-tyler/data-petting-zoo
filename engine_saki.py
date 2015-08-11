import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import re
from rules import name_rules, geofeat_rules

# Warn if a value is being assigned to a copy
pd.set_option('mode.chained_assignment', 'warn')

# Imports of needed data
gb = pd.read_pickle("data/pickles/gb.pk1")


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
    # Setting a list of alternate names from altname string field
    gb['ls_altname'] = gb['altname'].dropna().apply(lambda x: x.split(','))
    # Pick only feature codes that correspond to towns and cities, see
    # http://www.geonames.org/export/codes.html
    gb = gb[gb.feature_code.isin(geofeat_rules)]
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

    # list([name]) if not isinstance(cur, list) else cur.append(name)
    # gb['ls_altname'].map(lambda x:patinls(x, patlist))


def setupalt(df):
    df_alt = df.copy()
    df_alt.drop(['altname'], inplace=True, axis=1)
    df_alt.drop(['ls_altname'], inplace=True, axis=1)
    df_alt['parent'] = np.nan
    column_names = ['geoid', 'name', 'parent', 'asciiname', 'lat', 'long',
                     'feature_class', 'feature_code', 'country_code', 'cc2',
                     'adm1', 'adm2', 'adm3', 'adm4', 'pop', 'elev', 'delev',
                     'timezone', 'moddate']
    df_alt = df_alt[column_names]

    # for index, row in df.iterrows():
    #     parent_name = row['name']
    #     for a_name in row['ls_altname']:
    #         df_alt.ix['name', ] = a_name
    #         df_alt.ix['parent', ] = parent_name

    for index, row in df.iterrows():
        parent_name = row['name']
        for a_name in row['ls_altname']:
            row['name'] = a_name
            for i in range(len(df)):
                df_alt.ix[i, 'name'] = a_name

    return df_alt

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
                found = re.match(pat, string)
                if found:
                    break
        else:
            break
    return found


def patinstr(string, patlist):
    """Search string for a substring instance defined by patlist; return
    re.match if found, None if not found"""
    found = None
    for pat in patlist:
        found = re.match(pat, string)
        if found:
            break

    return found


if __name__ == "__main__":
    gbf = 'data/pristine/GB.txt'
    gb = setgb(gbf)
    other = setfam(gb)

    print other['ls_namefam'].dropna()

# def setup_df_alt(df):
#     df = df.copy()

#     for index, row in df.iterrows():
#         add'parent' = np.nan
#         df_alt.append(row[slice])
#         parent_name = row['name']
#         for aname in row['is_altname']:
#             row['name'] = aname
#             df_alt.append(row[slice])
#     return de_alt




