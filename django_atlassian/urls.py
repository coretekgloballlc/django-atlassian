# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import re_path

import views

urlpatterns = [
    re_path(r'^installed/$', views.installed, name='django-atlassian-installed'),
    re_path(r'^jira/$', views.JiraDescriptor.as_view(), name='django-atlassian-jira-connect-json'),
    re_path(r'^confluence/$', views.ConfluenceDescriptor.as_view(), name='django-atlassian-confluence-connect-json'),
]
