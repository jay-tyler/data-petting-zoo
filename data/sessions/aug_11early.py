# coding: utf-8

import pandas as pd; import numpy as np; from pandas import Series, DataFrame
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd projects/')
get_ipython().magic(u'cd data-petting-zoo/')
get_ipython().magic(u'ls ')
from rules import name_rules, geofeat_rules
gbf = 'data/pristine/GB.txt'
gb = setgb(gbf)
other = setfam(gb)
from engine import setgb, setfam
colors = cycle(['orange', '#eeeeee', 'b', 'y', 'cyan', 'magenta', 'yellow', 'red', '#cccccc', 'green', 'pink'])
from itertools import cycle
colors = cycle(['orange', '#eeeeee', 'b', 'y', 'cyan', 'magenta', 'yellow', 'red', '#cccccc', 'green', 'pink'])
import matplotlib.pyplot as plt
for key in name_rules.keys():
    data = getfamdf(gb2, key)
    plt.scatter(data.long, data.lat, label=key, c=next(colors), s=80, alpha=0.4)
    plt.legend(loc='lower right')
    
from engine import getfamdf
get_ipython().magic(u'matplotlib ')
for key in name_rules.keys():
    data = getfamdf(gb2, key)
    plt.scatter(data.long, data.lat, label=key, c=next(colors), s=80, alpha=0.4)
    plt.legend(loc='lower right')
for key in name_rules.keys():
    data = getfamdf(other, key)
    plt.scatter(data.long, data.lat, label=key, c=next(colors), s=80, alpha=0.4)
    plt.legend(loc='lower right')
gb = setgb(gbf)
gb2 = setfam(gb)
for key in name_rules.keys():
    data = getfamdf(other, key)
    plt.scatter(data.long, data.lat, label=key, c=next(colors), s=80, alpha=0.4)
    plt.legend(loc='lower right')
for key in name_rules.keys():
    data = getfamdf(gb2, key)
    plt.scatter(data.long, data.lat, label=key, c=next(colors), s=80, alpha=0.4)
    plt.legend(loc='lower right')
for key in name_rules.keys():
    data = getfamdf(gb2, key)
    data.to_json('data/exports/{}'.format(key))
    
for key in name_rules.keys():
    data = getfamdf(gb2, key)
    data.to_json('data/exports/{}.json'.format(key))
get_ipython().system(u' git add .')
get_ipython().system(u'git commit -m "about to add to name rules"')
from rules import name_rules, geofeat_rules
colors = cycle(['orange', '#eeeeee', 'b', 'y', 'cyan', 'magenta', 'yellow', 'red', '#cccccc', 'green', 'pink', 'coral', 'lawngreen', 'maroon', 'darkslategray', 'burlywood', 'lightpink', 'tomato'])
colors = cycle(['orange', '#eeeeee', 'b', 'y', 'cyan', 'magenta', 'yellow', 'red', '#cccccc', 'green', 'pink', 'coral', 'lawngreen', 'maroon', 'darkslategray', 'burlywood', 'lightpink', 'tomato', 'yellowgreen', 'olive', 'goldenrod'])
