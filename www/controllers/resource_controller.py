#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' resource_controller handlers '

from coroweb import get, post
from com.phoenix.resource import ResourceService

@get('/api/resources')
def manage_resources(request):
    srv = ResourceService()
    rootResource = srv.rootResource
    return dict(resources=rootResource.items)
