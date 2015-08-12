# coding: utf-8

import pandas as pd
import numpy as np; from pandas import Series, DataFrame
gb = pd.read_pickle('data/pickles/gb.pk1')
gb.shape
def lsfinpat(listostr, listopat):
    """Search each string in slist for a substring instance defined by patlist; return
    re.match if found, None if not found"""
    found = None
    for string in listostr:
        if not found:
            for pat in listopat:
                found = re.match(pat, string)
                if found:
                    break
        else:
            break
    return found
gb['ls_altname'].apply(lsfinpat)
gb['ls_altname'].apply(?
get_ipython().set_next_input(u"gb['ls_altname'].apply");get_ipython().magic(u'pinfo apply')
get_ipython().set_next_input(u"gb['ls_altname'].map");get_ipython().magic(u'pinfo map')
gb['ls_altname'].map(listofmap(x, 'bob'))
gb['ls_altname'].map(lsfinpat(x, 'bob'))
gb['ls_altname'].map(lamda x:lsfinpat(x, 'bob'))
gb['ls_altname'].applymap(lamda x:lsfinpat(x, 'bob'))
gb['ls_altname'].applymap(lambda x:lsfinpat(x, 'bob'))
gb['ls_altname'].map(lambda x:lsfinpat(x, 'bob'))
import re
gb['ls_altname'].map(lambda x:lsfinpat(x, 'bob'))
gb['ls_altname'].map(lambda x:lsfinpat(x, 'London'))
gb['ls_altname'].map(lambda x:patinls(x, 'London'))
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
gb['ls_altname'].map(lambda x:patinls(x, 'London'))
a = gb['ls_altname'].map(lambda x:patinls(x, 'London'))
a.dropna()
a[0]
a.iloc[1]
a.iloc[2]
a.iloc[1,:]
a[a.index == 0]
a = a.dropna()
a.iloc[1]
a.iloc[1].string
a.iloc[1].match
b = a.iloc[1]
b.group
b.group()
gb['ls_altname'].map(lambda x:patinls(x, ['London'])

)
a = gb['ls_altname'].map(lambda x:patinls(x, ['London']))
a
a.dropna()
a = a.dropna()
a = gb['ls_altname'].map(lambda x:patinls(x, ['London']))
patlist = ['London']
a = gb['ls_altname'].map(lambda x:patinls(x, patlist))
a
a.dropna()
a.iloc[0]
a.iloc[1]
a
a = a.dropna()
a.iloc[1]
a.iloc[1].string
a.iloc[1].group()
get_ipython().system(u'touch engine.py')
a = 'why do pangolins dream of quiche'
b = 'why do pangolins dream of quiche'
a is b
import sys
a = sys.intern('why do pangolins dream of quiche')
a = intern('why do pangolins dream of quiche')
b = "'why do pangolins dream of quiche'
b = 'why do pangolins dream of quiche'
b
a is b
b = 'why do pangolins dream of quiche'
a is b
a = intern('why do pangolins dream of quiche')
a is b
b is a
c = 'why do pangolins dream of quiche'
a is c
a = intern('why do pangolins dream of quiche')
type(a)
intern(b)
a is b
intern(a)
a is b
id(a)
id(b)
s3a = "strin"
s3 = s3a + 'g'
s3 is "string"
intern(s3) is "string"
intern(a) is 'why do pangolins dream of quiche'
get_ipython().magic(u'pinfo intern')
a = intern('why do pangolins dream of quiche')
b = 'why do pangolins dream of quiche'
a is b
get_ipython().magic(u'timeit a == b')
get_ipython().magic(u'timeit a is b')
get_ipython().magic(u'timeit a == b')
get_ipython().magic(u'timeit a is b')
for i in gb.iterrows()
for i in gb.iterrows():
    print i
    
$load_ext
$load_ext autoreload
get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
import engine
import engine
import engine
gba = engine.setup_gb_dataframe_from_pristine()
gba = engine.setup_gb_dataframe_from_pristine('data/pickles/gb.pk1')
gba = engine.setup_gb_dataframe_from_pristine('data/pristine/GB.txt')
gba = pd.read_csv('data/pickles/gb.pk1')
gba = pd.read_csv('data/pristine/GB.txt')
gba = engine.setup_gb_dataframe_from_pristine('data/pristine/GB.txt')
gba.head()
gba.shape
del gba
def patinstr(string, patlist):
    """Search string for a substring instance defined by patlist; return
    re.match if found, None if not found"""
    found = None
    for pat in patlist:
        found = re.match(pat, string)
        if found:
            break

    return found
patinstr('Accorn', ("(Ac)", "(Acc)", "(ock$)"))
a = patinstr('Accorn', ("(Ac)", "(Acc)", "(ock$)"))
a.string
name_rules = {
    "aberP": ("(Aber)"),
    "acPaccPockS": ("(Ac)", "(Acc)", "(ock$)"),
    "afonSavonQ": ("(afon$)", "([aA]von)"),
    "arPardP": ("(Ar)", "(Ard)"),
    "byS": ("(by$)"),
    "ashP": ("(Ash)"),
    "astP": ("(Ast)"),
    "auchenPauchinPauchachP": ("(Auchen)", "(Auchin)", "(Auchach)"),
    "auchterP": ("(Auchter)"),
    "axPexePaxeAeskA": ("(Ax)", "(Exe)", "(Usk)", "(Esk)"),
    "aySeyS": ("(ay$)", "(ey$)"),
}
gba = engine.setup_gb_dataframe_from_pristine('data/pristine/GB.txt')
gba["ls_namefame"]
gba["ls_namefame"] = np.nan
gba["ls_namefame"]
gba['ls_namefam'] = list()
get_ipython().magic(u'pinfo gba.iterrows')
name = "bob"
cur = np.nan
list(name) if cur == np.nan else cur.append(name)
cur == np.nan
cur is np.nan
cur
False == False
np.nan == np.nan
np.isnan()
np.isnan(cur)
list(name) if np.isnan(cur) else cur.append(name)
list([name]) if np.isnan(cur) else cur.append(name)
cur = list([name]) if np.isnan(cur) else cur.append(name)
list([name]) if np.isnan(cur) else cur.append(name)
cur.append(name)
np.isnan(cur)
isinstance(cur, list)
list([name]) if not isinstance(cur, list) else cur.append(name)
cur
cur = np.nan
get_ipython().magic(u'rep 137')
list([name]) if not isinstance(cur, list) else cur.append(name)
gba
def setup_name_families(df, teardown=False):
    """Setup name families for df dataframe

    Note: this only acts on the 'name' field. Use another function to setup
    altname families

    Column changes: will add a ls_namefam column
    """
    df["ls_namefam"] = np.nan
    # Iterate over rows in dataframe
    for index, row in df.iterrows():
        # For each row, check each name_rule
        for namekey, ls_regex in name_rules.iteritems():
            result = patinstr(row.loc['name'], ls_regex)
            if result:
                cur = df.loc[index, 'ls_namefam']
                if not isinstance(cur, list):
                    df.loc[index, 'name'] = list([namekey])
                else:
                    df.loc[index, 'name'].append(namekey)

    # list([name]) if not isinstance(cur, list) else cur.append(name)

    # gb['ls_altname'].map(lambda x:patinls(x, patlist))
                    
