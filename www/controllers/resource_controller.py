#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' resource_controller handlers '

from coroweb import get, post, put, delete
from com.phoenix.resource import Resource, ResourceService

@get('/api/resources')
def manage_resources(request):
    srv = ResourceService()
    rootResource = srv.rootResource
    return dict(resources=rootResource.items)

@post('/api/resources')
def create_resources(request, *, name,items):
    resource = __dic2Resource__(name, items)
    # resource = Resource(name)
    # for item in items:
    #     resource.appendItem(Resource(item.name))

    srv = ResourceService()
    srv.add(resource)
    rootResource = srv.rootResource
    return dict(resources=rootResource.items)

@put('/api/resources/{index}')
def update_resources(request, *, index, name,items):
    resource = __dic2Resource__(name, items)
    # resource = Resource(name)
    # for item in items:
    #     resource.appendItem(Resource(item.name))

    srv = ResourceService()
    srv.updateWithIndex(index,resource)
    rootResource = srv.rootResource
    return dict(resources=rootResource.items)

@delete('/api/resources/{index}')
def remove_resources_index(request, *, index):
    srv = ResourceService()
    srv.remove(index)
    rootResource = srv.rootResource
    return dict(resources=rootResource.items)

@delete('/api/resources')
def remove_resources(request, *, name,items):
    resource = __dic2Resource__(name, items)
    # resource = Resource(name)
    # for item in items:
    #     resource.appendItem(Resource(item.name))

    srv = ResourceService()
    srv.remove(resource)
    rootResource = srv.rootResource
    return dict(resources=rootResource.items)

def __dic2Resource__(name,items):
    resource = Resource(name)
    for item in items:
        resource.appendItem(Resource(item['name']))
    
    return resource
