"""Pyramid setup function, called when 'pserve' is run"""
from pyramid.config import Configurator


def main(global_config, **settings):
    """Set up the Pyramid app and define the views"""
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('by_for', '/byrecipient')
    config.add_route('duration', '/byduration')
    config.scan()
    return config.make_wsgi_app()
