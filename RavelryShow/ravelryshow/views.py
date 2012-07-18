"""Definitions of Pyramid views

all_projects_view: Display all projects in one group
by_recipient_view: Display projects grouped by recipient
duration_view: Display projects grouped by duration

"""
from pyramid.view import view_config

from fetch_data import fetch_project_data
import transforms


def _view_from_transform(transform_fxn):
    """Define a Pyramid view callable based on a function from the 'transforms' module

    @param transform_fxn: Function that takes projects and returns project groups
    @return dict with 'user' and 'project_groups' keys

    """
    data_dict = fetch_project_data()
    project_groups = transform_fxn(data_dict['projects'])
    return {'user': data_dict['user'],
            'project_groups': project_groups}


@view_config(route_name='home', renderer='templates/projects.pt')
def all_projects_view(request):
    """Return all projects in one group"""
    return _view_from_transform(transforms.all_projects_transform)


@view_config(route_name='by_for', renderer='templates/projects.pt')
def by_recipient_view(request):
    """Group projects by the "made for" field"""
    return _view_from_transform(transforms.by_recipient_transform)


@view_config(route_name='duration', renderer='templates/projects.pt')
def duration_view(request):
    """Group projects by how long they took (or have taken so far)"""
    return _view_from_transform(transforms.duration_transform)
