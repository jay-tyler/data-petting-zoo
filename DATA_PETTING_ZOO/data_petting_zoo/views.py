from pyramid.view import view_config
from engine import setgb, getfamdf
import pandas as pd
import json

gb = pd.read_pickle("../data/pickles/test_fam.pk1")


@view_config(route_name='place',
             renderer='templates/home.jinja2')
@view_config(route_name='home',
             renderer='templates/home.jinja2')
def home_view(request):
    try:
        name = request.matchdict['name']
    except KeyError:
        return {}
    # namekey = ''.join(gb.loc[gb['name'] == name]['ls_namefam'].values[0])
    # fam_df = getfamdf(gb, namekey)
    place = gb.loc[gb['name'] == name]
    place_zip = dict(zip(place.columns.values, place.values[0]))
    place_json = json.dumps(place_zip)

    return {'place': place_json}


@view_config(route_name='about',
             renderer='templates/about.jinja2')
def about_view(request):
    return {}
