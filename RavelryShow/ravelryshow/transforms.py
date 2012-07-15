"""Different ways of organizing the project data

Each function takes a list of "project" dictionaries and returns a list of
"project group" dictionaries.

A "project group" dictionary has format
{'title': sometitle,
 'projects': [project_dict]}

"""
from collections import defaultdict
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
                               cmp=lambda x,y: locale.strcoll(x.lower(), y.lower()))
    project_groups = [{'title': recip,
                       'projects': projects_by_recipient[recip]}
                      for recip in sorted_recipients]
    return project_groups
