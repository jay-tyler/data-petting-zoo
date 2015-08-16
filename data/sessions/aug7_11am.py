# coding: utf-8

import pandas as pd; import numpy as np
from pandas import Series, DataFrame
get_ipython().magic(u'ls ')
gb = pd.load_pickle("pickles/gb.pk1")
gb = pd.read_pickle("pickles/gb.pk1")
gb.columns()
gb.columns
gb['pop'].max()
a = gb['pop'].max()
a
a.item
a.item()
a.view()
gb['pop'].transform(max)
get_ipython().magic(u'pinfo gb.idxmax')
gb['pop'].idxmax()
get_ipython().set_next_input(u"gb['pop'].idxmax");get_ipython().magic(u'pinfo idxmax')
get_ipython().magic(u'pinfo2 gb.idxmax')
gb['pop'].idxmax(axis=1)
gb.iloc[17150]
