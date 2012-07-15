"""Unit tests for transforms"""
from unittest import TestCase

from ravelryshow import transforms

class TransformTests(TestCase):
    def setUp(self):
        self._all_projects = [{'name': 'A Project',
                               'madeFor': 'Suzy'},
                              {'name': 'Eco Mittens',
                               'madeFor': 'The Lorax'},
                              {'name': 'Another Project',
                               'madeFor': 'Guy Forget'},
                              {'name': 'Funny Hat',
                               'madeFor': 'The Lorax'}]

    def test_all_projects(self):
        """All Projects transform just puts all projects in one group"""
        groups = transforms.all_projects_transform(self._all_projects)
        self.assertEquals(1, len(groups))
        self.assertEquals('All Projects', groups[0]['title'])
        self.assertEquals(self._all_projects, groups[0]['projects'])

    def test_by_recipient(self):
        """By Recipient transform groups projects and sorts correctly"""
        groups = transforms.by_recipient_transform(self._all_projects)
        self.assertEquals(3, len(groups))
        self.assertEquals(['Guy Forget', 'Suzy', 'The Lorax'], [pg['title'] for pg in groups])
        self.assertEquals(2, len(groups[2]))
