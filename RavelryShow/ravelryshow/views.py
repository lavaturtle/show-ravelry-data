from pyramid.view import view_config

from fetch_data import fetch_project_data
import transforms


@view_config(route_name='home', renderer='templates/projects.pt')
def all_projects_view(request):
    """Return all projects in one group"""
    data_dict = fetch_project_data()
    project_groups = transforms.all_projects_transform(data_dict['projects'])
    return {'user': data_dict['user'],
            'project_groups': project_groups}


@view_config(route_name='by_for', renderer='templates/projects.pt')
def by_recipient_view(request):
    """Group projects by the "made for" field"""
    data_dict = fetch_project_data()
    project_groups = transforms.by_recipient_transform(data_dict['projects'])
    return {'user': data_dict['user'],
            'project_groups': project_groups}
