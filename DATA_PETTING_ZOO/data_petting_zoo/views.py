from pyramid.view import view_config
import pandas as pd
import json
from engine import query_placename

gb = pd.read_pickle("../data/pickles/gb13.pk1")


@view_config(route_name='search',
             xhr=True,
             renderer='json')
@view_config(route_name='place',
             renderer='templates/home.jinja2')
@view_config(route_name='home',
             renderer='templates/home.jinja2')
def home_view(request):
    try:
        name = request.matchdict['name']
    except KeyError:
        return {}

    if 'HTTP_X_REQUESTED_WITH' in request.environ:
        fam_df, namekey, placename = query_placename(gb, name)
        # if place doesn't have a family name - return place row, plot
        # point

        # if place is not in dataset - return random query

        # else, return all three as json obj

        return fam_df.to_json(orient="records")

    # else:
    #     place = gb.loc[gb['name'] == name]
    #     place_zip = dict(zip(place.columns.values, place.values[0]))
    #     place_json = json.dumps(place_zip)
    #     return {'place': place_json}


@view_config(route_name='about',
             renderer='templates/about.jinja2')
def about_view(request):
    return {}
