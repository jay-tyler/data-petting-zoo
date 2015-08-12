# coding: utf-8

get_ipython().magic(u'paste')
import pandas as pd; import numpy as np
from pandas import Series, DataFrame

gb = pd.read_pickle("pickles/gb.pk1")
alt.to_pickle("pickles/alt_gb.pk1")

ext = alt['name']
import pandas as pd; import numpy as np
from pandas import Series, DataFrame

gb = pd.read_pickle("data/pickles/gb.pk1")
alt.to_pickle("data/pickles/alt_gb.pk1")

ext = alt['name']
get_ipython().magic(u'rep 3')
import pandas as pd; import numpy as np
from pandas import Series, DataFrame

gb = pd.read_pickle("data/pickles/gb.pk1")
alt.to_pickle("data/pickles/alt_gb.pk1")
import pandas as pd; import numpy as np
from pandas import Series, DataFrame

gb = pd.read_pickle("data/pickles/gb.pk1")
gb.head()
get_ipython().magic(u'whos ')
gb.describe()
gb.size()
gb.size
gb.shape
checkdb = pd.read_table('data/pristine/GB.txt')
checkdb.shape()
checkdb.shape
del checkdb
db['name' == 'Edinburgh']
gb['name' == 'Edinburgh']
gb.columns
gb[gb.name == 'london']
gb[gb.name == 'London']
gb[gb.name == 'Edinburgh']
gb[gb.name == 'Edinburough']
gb[gb.adm1 == 'ADM1']
gb.adm1.unique()
gb[gb.adm1 == '05']
gb[gb.adm1 == '05']
gb[gb.adm1 == '03']
gb.adm1.unique()
gb[gb.adm1 == '01']
gb[gb.adm1 == '00']
gb[gb.adm1 == '00'].head()
gb[gb.adm1 == '00'].tail()
gb[gb.adm1 == '00']
gb[gb.adm1 == 'NIR']
gb[gb.adm1 == 'nan']
gb.adm1.unique()
gb[gb.adm1 == nan]
gb.adm1.isnull()
gb.adm1.isnull().any()
gb[gb.adm1.isnull()]
pd.options.display.max_rows = 250
get_ipython().magic(u'pinfo pd.options.display.max_colwidth')
pd.options.display.max_colwidth
pd.options.display.max_colwidth = 15
gb[gb.adm1.isnull()]
gb[gb.adm1.isnull()].iloc[:,5]
gb[gb.adm1.isnull()].iloc[:,2]
gb[gb.names == 'Oban']
gb[gb.name == 'Oban']
gb.iloc[46041,:]
gb.iloc[46041,:].name
gb.iloc[46041].name
gb.iloc[46041]
a = gb.iloc[46041].name
a
a = gb.iloc[46041]
a.name
a.columns.
a.columns
a
a['name']
a.name
get_ipython().magic(u'pinfo a.name')
gb[gb.adm1 == 'SCT']
gb[gb.adm1 == 'SCT'].names.head()
gb[gb.adm1 == 'SCT'].name.head()
gb
gb.columsn
gb.columns
remove_these_adm1 = ['05', '00', '01', '00', 'NIR']
for i in remove_these_adm1:
    gb = gb[gb.adm1 != i]
    
gb.shape()
gb.shape
gb.adm1.unique()
remove_these_adm1 = ['05', '00', '01', 'NIR', '03']
for i in remove_these_adm1:
    gb = gb[gb.adm1 != i]
    
gb.adm1.unique()
gb.to_pickle('data/pickles/gb.pk1')
get_ipython().magic(u'ls data/pickles/')
gb.to_csv('data/exports/gb.csv')
gb.adm2.unique()
gb.adm3.unique()
gb.adm3.unique().shape
gb.adm2['C6'].head()
gb[gb.adm2 == 'C6'].head()
gb[gb.adm3 == '00CAGA']
gb[gb.adm3 == '00CA008']
gb[gb.adm3 == '00CA008'].name
a = gb[gb.adm3 == '00CA008']
a.name
a['name']
b=a['name']
b
gb.columns
gb.adm4.unique()
gb.adm4.unique().shape()
gb.adm4.unique().shape
gb.adm3.unique().shape
gb.adm2.unique().shape
gb.adm3.head()
gb.adm3.tail()
gb.adm4.tail()
gb.adm1
gb.adm2
gb.shape
gb.columns
ext = gb['name']
ext.str.contains("(^aber)")
gb[ext.str.contains("(^aber)")]
gb[ext.str.contains("(aber)")]
gb[ext.str.contains("(aber)")].name.unique()
gb[gb.name == "Aberdeen"]
gb[ext.str.contains("(Aber)")].name.unique()
gb.feature_code.head()
gb[gb.name == "Aberdeen"].feature_code
