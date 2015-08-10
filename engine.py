import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import re
from rules import name_rules, geofeat_rules

# Warn if a value is being assigned to a copy
pd.set_option('mode.chained_assignment', 'warn')

# Imports of needed data
gb = pd.read_pickle("data/pickles/gb.pk1")


def setup_gb_dataframe_from_pristine(file_path):
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
    return gb


def setup_name_families():
    """In-place setup name families for df dataframe. 

    Note: this only acts on the 'name' field. Use another function to setup
    altname families

    Column changes: will add a ls_namefam column

    TODO: This is a one run deal. Fix.
    """
    global df
    l = df.shape







    df = df.copy()
    # df["ls_namefam"] = np.nan
    # Iterate over rows in dataframe
    for index, row in df.iterrows():
        # For each row, check each name_rule
        for namekey, ls_regex in name_rules.iteritems():
            result = patinstr(row.loc['name'], ls_regex)
            if result:
                cur = df.loc[index, 'ls_namefam']
                if not isinstance(cur, list):
                    print df.loc[index, 'name'], namekey
                    df.loc[index, 'name'] = list([namekey])
                else:
                    df.loc[index, 'name'].append(namekey)
    return df

    # list([name]) if not isinstance(cur, list) else cur.append(name)

    # gb['ls_altname'].map(lambda x:patinls(x, patlist))


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
