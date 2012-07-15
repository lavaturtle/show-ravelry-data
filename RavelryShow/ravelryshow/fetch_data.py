import json
import urllib


API_KEY = '41ea1a592266728c48ca047437822999e86834dc'
USERNAME = 'lavaturtle'


def fetch_project_data():
    """Fetch a dictionary of project data"""
    url_format = "http://api.ravelry.com/projects/{username}/progress.json?status=in-progress+hibernating+finished+frogged&notes=true&key={key}"
    url = url_format.format(username=USERNAME, key=API_KEY)
    reader = urllib.urlopen(url)
    data_json = reader.read()
    data_dict = json.loads(data_json)
    return data_dict
