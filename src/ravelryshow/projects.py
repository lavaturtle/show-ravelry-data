import json
from pyramid.response import Response
import urllib


def print_projects():
    data_dict = fetch_project_data()
    project_names = [project['name'] for project in data_dict['projects']]
    return ', '.join(project_names)


def fetch_project_data():
    """Fetch a dictionary of project data"""
    url = 'http://api.ravelry.com/projects/lavaturtle/progress.json?key=41ea1a592266728c48ca047437822999e86834dc&status=in-progress+hibernating+finished+frogged&notes=true'
    reader = urllib.urlopen(url)
    data_json = reader.read()
    data_dict = json.loads(data_json)
    return data_dict
