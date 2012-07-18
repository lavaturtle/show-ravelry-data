"""Different ways of organizing the project data

Each function takes a list of "project" dictionaries and returns a list of
"project group" dictionaries.

A "project group" dictionary has format
{'title': sometitle,
 'projects': [project_dict]}

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


def duration_transform(projects):
    """Group projects by how long they took (or have taken so far)

    @param projects: List of dictionaries, one per project
    @return list of project group dictionaries, sorted from short to long

    """
    time_buckets = {1: 'Less than a day',
                    7: 'Less than a week',
                    30: 'Less than a month',
                    366: 'Less than a year',
                    1000000000: 'More than a year'}

    def parse_date(date_str):
        date_format = '%Y-%m-%d'
        return datetime.strptime(date_str, date_format)

    projects_by_duration = defaultdict(list)
    for project in projects:
        start_date = parse_date(project['started'])
        end_date = parse_date(project['completed']) if project['completed'] else datetime.now()
        delta = end_date - start_date
        duration = delta.days
        bucket = min(filter(lambda cap: cap > duration,
                            time_buckets.keys()))
        projects_by_duration[bucket].append(project)
    project_groups = [{'title': time_buckets[cap],
                       'projects': projects_by_duration[cap]}
                      for cap in sorted(projects_by_duration.keys())]
    return project_groups
