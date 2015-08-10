import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import re
from rules import name_rules, geofeat_rules








gb = pd.read_pickle("data/pickles/gb.pk1")

def setup_gb_dataframe_from_pristine(file_path):
    gb = pd.read_csv(file_path)
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

def setup_families(teardown=False):
    """Setup name families for the dataframe"""
    
    # gb['ls_altname'].map(lambda x:patinls(x, patlist))

def patinls(slist, patlist):
    """Search each string in slist for a substring instance defined by patlist; return
    re.match if found, None if not found"""
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