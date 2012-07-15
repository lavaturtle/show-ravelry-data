import json
import urllib


def fetch_project_data():
    """Fetch a dictionary of project data"""
    url = 'http://api.ravelry.com/projects/lavaturtle/progress.json?key=41ea1a592266728c48ca047437822999e86834dc&status=in-progress+hibernating+finished+frogged&notes=true'
    reader = urllib.urlopen(url)
    data_json = reader.read()
    data_dict = json.loads(data_json)
    return data_dict
