"""Unit tests for transforms"""
from unittest import TestCase

from ravelryshow import transforms


class TransformTests(TestCase):
    def setUp(self):
        self._all_projects = [{'name': 'A Project',
                               'madeFor': 'Suzy',
                               'started': '2012-03-02',
                               'completed': '2012-03-07'},
                              {'name': 'Eco Mittens',
                               'madeFor': 'The Lorax',
                               'started': '2011-01-01',
                               'completed': '2011-03-01'},
                              {'name': 'Another Project',
                               'madeFor': 'Guy Forget',
                               'started': '2008-08-01',
                               'completed': None},
                              {'name': 'Funny Hat',
                               'madeFor': 'The Lorax',
                               'started': '2012-03-02',
                               'completed': '2012-03-02'}]

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
        self.assertEquals(['Guy Forget', 'Suzy', 'The Lorax'],
                          [pg['title'] for pg in groups])
        self.assertEquals(2, len(groups[2]))

    def test_by_duration(self):
        """By Duration transform groups projects correctly"""
        groups = transforms.duration_transform(self._all_projects)
        self.assertEquals(4, len(groups))
        self.assertEquals('Less than a day', groups[0]['title'])
        self.assertEquals('Funny Hat', groups[0]['projects'][0]['name'])
        self.assertEquals('Less than a week', groups[1]['title'])
        self.assertEquals('A Project', groups[1]['projects'][0]['name'])
        self.assertEquals('Less than a year', groups[2]['title'])
        self.assertEquals('Eco Mittens', groups[2]['projects'][0]['name'])
        self.assertEquals('More than a year', groups[3]['title'])
        self.assertEquals('Another Project', groups[3]['projects'][0]['name'])
