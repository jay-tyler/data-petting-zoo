from pyramid.view import view_config


@view_config(route_name='home',
             renderer='templates/home.jinja2')
def home_view(request):
    return {}


@view_config(route_name='about',
             renderer='templates/about.jinja2')
def about_view(request):
    return {}
