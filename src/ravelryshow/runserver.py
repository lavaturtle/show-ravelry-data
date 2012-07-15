from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from projects import print_projects


def show_projects(request):
    return Response(print_projects())


if __name__ == '__main__':
    config = Configurator()
    config.add_route('projects', '/projects')
    config.add_view(show_projects, route_name='projects')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
