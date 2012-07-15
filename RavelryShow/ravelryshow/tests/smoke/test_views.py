"""Smoke tests for views"""
from pyramid import testing
import unittest

from ravelryshow import views

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_basic_view(self):
        """Smoke-test basic "All Projects" view"""
        request = testing.DummyRequest()
        info = views.all_projects_view(request)
        self.assertEqual(info['user']['name'], 'lavaturtle')

    def test_by_recipient_view(self):
        """Smoke-test "By Recipient" view"""
        request = testing.DummyRequest()
        info = views.by_recipient_view(request)
        self.assertEqual(info['user']['name'], 'lavaturtle')
