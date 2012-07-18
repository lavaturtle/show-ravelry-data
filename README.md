show-ravelry-data
=================

Pyramid-based web app that displays Ravelry project data organized in various ways.

By default, the app displays data for user lavaturtle.

# Running the server locally
You'll need to have python installed.

Here are two sets of instructions: one for using a virtual environment, and an alternative set of instructions, for not using a virtual environment.

## Using a virtual environment
* git clone git://github.com/lavaturtle/show-ravelry-data.git
* mkvirtualenv show-ravelry-data (or create a virtual environment using the command of your choice)
* cd show-ravelry-data/RavelryShow
* python setup.py develop
* pserve production.ini

## Not using a virtual environment
* git clone git://github.com/lavaturtle/show-ravelry-data.git
* cd show-ravelry-data/RavelryShow
* sudo python setup.py develop
* pserve production.ini

## Local URL
Once the server is running locally, the app can be viewed at http://localhost:6543/
