show-ravelry-data
=================

Pyramid-based web app that displays Ravelry project data organized in various ways.

By default, the app displays data for user lavaturtle.

To set up and run the server locally (assuming you have python and virtualenvwrapper):
* git clone git://github.com/lavaturtle/show-ravelry-data.git
* mkvirtualenv show-ravelry-data
* cd show-ravelry-data/RavelryShow
* python setup.py develop
* pserve production.ini

The app can then be viewed at http://localhost:6543/
