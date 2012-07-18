import json
import urllib


API_KEY = '41ea1a592266728c48ca047437822999e86834dc'
USERNAME = 'lavaturtle'
STATUSES = ['in-progress', 'hibernating', 'finished', 'frogged']


def fetch_project_data():
    """Fetch a dictionary of project data from Ravelry"""
    url_format = "http://api.ravelry.com/projects/{username}/progress.json?status={statuses}&notes=true&key={key}"
    url = url_format.format(username=USERNAME,
                            key=API_KEY,
                            statuses="+".join(STATUSES))
    reader = urllib.urlopen(url)
    data_json = reader.read()
    data_dict = json.loads(data_json)
    return data_dict
