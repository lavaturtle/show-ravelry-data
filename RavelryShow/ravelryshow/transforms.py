"""Functions providing different ways of organizing project data

Each function takes a list of "project" dictionaries and returns a list of
"project group" dictionaries.

A "project group" dictionary has format
{'title': sometitle,
 'projects': [project_dict]}

all_projects_transform: Puts all projects in one group
by_recipient_transform: Groups projects by the "made for" field
duration_transform: Groups projects by how long they took

"""
from collections import defaultdict
from datetime import datetime
import locale


def all_projects_transform(projects):
    """Most basic transform: all projects in one group

    @param projects: List of dictionaries, one per project
    @return list of project group dictionaries

    """
    return [{'title': 'All Projects',
             'projects': projects}]


def by_recipient_transform(projects):
    """Group projects by "made for" field

    @param projects: List of dictionaries, one per project
    @return list of project group dictionaries, sorted by recipient

    """
    projects_by_recipient = defaultdict(list)
    for project in projects:
        recipient = project['madeFor']
        projects_by_recipient[recipient].append(project)
    sorted_recipients = sorted(projects_by_recipient.keys(),
                               cmp=lambda x, y: locale.strcoll(x.lower(), y.lower()))
    project_groups = [{'title': recip,
                       'projects': projects_by_recipient[recip]}
                      for recip in sorted_recipients]
    return project_groups


DURATIONS_BY_CUTOFF = {1: 'Less than a day',
                7: 'Less than a week',
                30: 'Less than a month',
                366: 'Less than a year',
                1000000000: 'More than a year'}


DATE_FORMAT_ISO_8601 = '%Y-%m-%d'


def parse_date(date_str):
    """Parse a date in ISO 8601 format"""
    return datetime.strptime(date_str, DATE_FORMAT_ISO_8601)


def duration_transform(projects):
    """Group projects by how long they took (or have taken so far)

    @param projects: List of dictionaries, one per project
    @return list of project group dictionaries, sorted from short to long

    """
    projects_by_time_bucket = defaultdict(list)
    for project in projects:
        start_date = parse_date(project['started'])
        end_date = parse_date(project['completed']) if project['completed'] else datetime.now()
        duration = end_date - start_date
        bucket = min(filter(lambda cutoff: cutoff > duration.days,
                            DURATIONS_BY_CUTOFF.keys()))
        projects_by_time_bucket[bucket].append(project)
    project_groups = [{'title': DURATIONS_BY_CUTOFF[cutoff],
                       'projects': projects_by_time_bucket[cutoff]}
                      for cutoff in sorted(projects_by_time_bucket.keys())]
    return project_groups
