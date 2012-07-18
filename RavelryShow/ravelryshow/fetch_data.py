"""Function for fetching data from Ravelry

fetch_project_data: Fetch project data

"""
import json
import urllib


USERNAME = 'lavaturtle'
API_KEY = '41ea1a592266728c48ca047437822999e86834dc'

URL_FORMAT = "http://api.ravelry.com/projects/{username}/progress.json?status={statuses}&notes=true&key={key}"
STATUSES = ['in-progress', 'hibernating', 'finished', 'frogged']


def fetch_project_data():
    """Fetch a dictionary of project data from Ravelry

    @return dict with output of Ravelry project API

    Returned dict is expected to have keys 'user' and 'projects'

    """
    url = URL_FORMAT.format(username=USERNAME,
                            key=API_KEY,
                            statuses="+".join(STATUSES))
    reader = urllib.urlopen(url)
    data_json = reader.read()
    data_dict = json.loads(data_json)
    return data_dict
