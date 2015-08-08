# coding: utf-8

import pandas as pd; import numpy as np
from pandas import Series, DataFrame
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd data')
get_ipython().magic(u'ls ')
gb = pd.*csv*
get_ipython().magic(u'psearch pd.*csv*')
gb = pd.read_csv("GB.txt")
file = open("GB.txt", "r")
a = file.readline()
a
file.close()
file = open("alternateNames/alternateNames.txt", "r")
a = file.readline()
a
file.close()
gb = pd.read_table("GB.txt")
gb
gb.columns
['geoid', 'name', 'asciiname', 'altname', 'lat', 'long', 'feature_class', 'feature_code', 'country_code', 'cc2', 'adm1', 'adm2', 'adm3', 'adm4', 'pop', 'elev', 'delev', 'timezone', 'moddate']
gb.columns = _
gb
gb.head()
gb.tail()
get_ipython().magic(u'ls ')
get_ipython().magic(u'mkdir pickles')
get_ipython().magic(u'mkdir pristine')
get_ipython().magic(u'ls ')
get_ipython().magic(u'mv alternateNames/ ./pristine/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'mv columns_GB.txt pristine/')
get_ipython().magic(u'mv GB.txt pristine/')
get_ipython().magic(u'ls ')
get_ipython().system(u'tree')
gb.to_pickle("gb.pk1")
gb
gb.columns
sub = gb['altname']
sub.dropna
sub.dropna(axis=1)
sub.dropna(axis=0)
sub.dropna(axis=0).split(',')
sub.dropna(axis=0).*
get_ipython().magic(u'pinfo sub.apply')
sub.apply(lamda x: x.split(','))
sub.apply(lambda x: x.split(','))
sub.dropna().apply(lambda x: x.split(','))
gb['ls_altname']=sub.apply(lambda x: x.split(','))
gb['ls_altname']=sub.dropna().apply(lambda x: x.split(','))
gb.head()
gb.tail()
gb.mask(gb.altname != NaN)
gb.mask(gb.altname != pd.NaN)
gb.mask(gb.altname != np.NaN)
gb[~gb.altname.isnull()]
alt = gb[~gb.altname.isnull()]
alt.altname
alt.ls_altname[4]
alt.ls_altname._ix[4,:]
alt.ls_altname._ix(4,:)
alt.ls_altname._ix(4)
get_ipython().magic(u'pinfo alt.ls_altname._ix')
alt.ls_altname.loc[4,:]
get_ipython().magic(u'pinfo alt.ls_altname.loc')
alt.ls_altname
alt.ls_altname['geoid' == 51513]
gb.iloc[1]
gb.iloc[2]
gb.iloc[1]
gb.iloc[4]
alt.iloc[5]
alt.iloc[5]['ls_altname']
a = alt.iloc[5]['ls_altname']
len(a)
type(a)
a[4]
a[3]
b = a[3]
alt
gb.to_pickle("pickles/gb.pk1")
alt.to_pickle("pickles/alt_gb.pk1")
test = pd.load("pickles/alt_gb.pk1")
test.head()
test.describe()
test
test.describe
test.describe()
ext = alt['name']
ext.str.extract([by^])
ext.str.extract('[by]^')
ext.str.extract('([by]^)')
ext2 = ext.str.extract('([by]^)')
ext2.dropna()
ext2.isnull()
ext2[~ext2.isnull()]
ext2 = ext.str.extract('(by)')
ext2
ext2.dropna()
ext
ext.str.contains('(by^)')
ext2 = ext.str.contains('(by^)')
ext2[True]
ext[ext2]
ext2 = ext.str.contains('(by)')
ext2
ext[ext2]
ext2 = ext.str.contains('(by\b)')
ext[ext2]
ext2 = ext.str.contains('(by)')
ext2 = ext.str.contains('(by$)')
ext[ext2]
gb[gb.name == ext[ext2]]
get_ipython().magic(u'pinfo gb.iloc')
get_ipython().magic(u'pinfo s.isin')
ext[ext2]
ext3 = ext[ext2]
ext3.isin(gb['names'])
ext3.isin(gb['name'])
gb[ext3.isin(gb['name'])]
gb * ext3.isin(gb['name'])
ext3.isin(gb['name'])
gb.loc[ext3.isin(gb['name']), :]
gb.loc[gb['name'].isin(ext3), :]
by_names = gb.loc[gb['name'].isin(ext3), :]
by_names['names'].unique()
by_names['name'].unique()
by_names
by_names['names']
by_names['name']
list(by_names['name'])
gb.iloc[720]
gb.iloc[722]
gb.iloc[723]
by_names.to_pickle("pickles/by_names.pk1")
by_names.plot()
by_names['pop'].plot()
a = by_names['pop'].plot()
get_ipython().magic(u'psearch a.*show*')
a.matshow()
get_ipython().magic(u'matplotlib')
by_names['pop'].plot()
gb['pop'].plot()
both = [_, __]
for series in both:
    series.plot()
    
for series in both:
    series.plot()
both[0]
[by_names['pop'], gb['pop']]
both = [by_names['pop'], gb['pop']]
for series in both:
    series.plot()
for series in both:
    series.scatter()
for series in both:
    series.point()
get_ipython().magic(u'pastebin 0-152')
get_ipython().magic(u'pinfo %history')
get_ipython().magic(u'pinfo save')
get_ipython().magic(u'ls ')
get_ipython().magic(u'mkdir sessions')
get_ipython().magic(u'save sessions/aug6.py 0-157')
