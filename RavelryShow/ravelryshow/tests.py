import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import projects_view
        request = testing.DummyRequest()
        info = projects_view(request)
        self.assertEqual(info['user']['name'], 'lavaturtle')
