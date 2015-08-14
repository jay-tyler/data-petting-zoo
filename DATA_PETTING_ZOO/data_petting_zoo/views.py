from pyramid.view import view_config
import pandas as pd
from engine import query_name_or_fam, query_namefam_table, get_fam


gb = pd.read_pickle("../data/pickles/gb_final.pk1")
NAMEFAM = pd.read_table("../data/namefam.tab")


@view_config(route_name='search',
             xhr=True,
             renderer='json')
@view_config(route_name='home',
             renderer='templates/home.jinja2')
def home_view(request):

    if request.current_route_path() == '/':
        menu_items = []
        for r in range(len(NAMEFAM)):
            menu_items.append(
                [str(NAMEFAM['namekey'][r]),
                 str(NAMEFAM['human_namekey'][r])]
            )
        return {'menu_items': menu_items}

    try:
        name = request.matchdict['name']
    except KeyError:
        return {}

    if 'HTTP_X_REQUESTED_WITH' in request.environ:
        if query_name_or_fam(gb, name) is None:
            return {'error': 'Ba-a-a-a-a-a-a-a-a-ad query. Try again.'}
        else:
            fam_df, namekey, placename = query_name_or_fam(gb, name)
            if namekey is None:
                return {'fam_df': fam_df.fillna(0),
                        'name': placename,
                        'message': 'Does not belong to a known family of names.'}
            namefam_dict = query_namefam_table(namekey)

        return {'fam_df': fam_df.fillna(0),
                'namefam_dict': namefam_dict,
                'name': placename}


@view_config(route_name='dropdown',
             xhr=True,
             renderer='json')
def dropdown_view(request):
    try:
        namekey = request.matchdict['namekey']
    except KeyError:
        return {}

    if 'HTTP_X_REQUESTED_WITH' in request.environ:
        fam_df, namekey, placename = get_fam(gb, namekey)
        namefam_dict = query_namefam_table(namekey)
        return {'fam_df': fam_df.fillna(0),
                'namefam_dict': namefam_dict}


@view_config(route_name='about',
             renderer='templates/about.jinja2')
def about_view(request):
    return {}
