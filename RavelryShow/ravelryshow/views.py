from collections import defaultdict
import locale
from pyramid.view import view_config

from fetch_data import fetch_project_data


@view_config(route_name='home', renderer='templates/projects.pt')
def all_projects_view(request):
    """Return all projects in one group"""
    data_dict = fetch_project_data()
    return {'user': data_dict['user'],
            'project_groups': [{'title': 'All Projects',
                               'projects': data_dict['projects']}]}


@view_config(route_name='by_for', renderer='templates/projects.pt')
def by_recipient_view(request):
    """Group projects by the "made for" field"""
    data_dict = fetch_project_data()
    all_projects = data_dict['projects']
    projects_by_recipient = defaultdict(list)
    for project in all_projects:
        recipient = project['madeFor']
        projects_by_recipient[recipient].append(project)
    sorted_recipients = sorted(projects_by_recipient.keys(),
                               cmp=lambda x,y: locale.strcoll(x.lower(), y.lower()))
    project_groups = [{'title': recip,
                       'projects': projects_by_recipient[recip]}
                      for recip in sorted_recipients]
    return {'user': data_dict['user'],
            'project_groups': project_groups}
