import json
from pyramid.view import view_config
import urllib

@view_config(route_name='home', renderer='templates/projects.pt')
def projects_view(request):
    data_dict = fetch_project_data()
    user = data_dict['user']
    projects = data_dict['projects']
    return {'user': user,
            'projects': projects}


def fetch_project_data():
    """Fetch a dictionary of project data"""
    url = 'http://api.ravelry.com/projects/lavaturtle/progress.json?key=41ea1a592266728c48ca047437822999e86834dc&status=in-progress+hibernating+finished+frogged&notes=true'
    reader = urllib.urlopen(url)
    data_json = reader.read()
    data_dict = json.loads(data_json)
    return data_dict
