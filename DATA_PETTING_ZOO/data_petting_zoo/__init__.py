from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.renderers import JSON
from pandas import DataFrame

from .models import (
    DBSession,
    Base,
)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    json_renderer = JSON()

    def dataframe_adapter(df, request):
        return df.to_dict(orient="records")

    json_renderer.add_adapter(DataFrame, dataframe_adapter)
    config.add_renderer('json', json_renderer)

    config.include('pyramid_jinja2')
    config.include('pyramid_tm')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('place', '/place/{name}')
    config.add_route('search', '/search/{name}')
    config.add_route('dropdown', '/dropdown/{namekey}')

    config.scan()

    return config.make_wsgi_app()
