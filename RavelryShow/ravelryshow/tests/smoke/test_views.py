"""Smoke tests for views"""
import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_basic_view(self):
        from ravelryshow.views import all_projects_view
        request = testing.DummyRequest()
        info = all_projects_view(request)
        self.assertEqual(info['user']['name'], 'lavaturtle')
