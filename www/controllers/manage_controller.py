#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' manage_controller handlers '

from coroweb import get, post
from com.phoenix.common import get_page_index

@get('/manage')
def manage():
    return 'redirect:/manage/comments'

@get('/manage/users')
def manage_users(*, page='1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': get_page_index(page)
    }

@get('/manage/comments')
def manage_comments(*, page='1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page)
    }

@get('/manage/datasources')
def manage_datasources(*, page='1'):
    return {
        '__template__': 'datasources.html',
        'page_index': get_page_index(page)
    }

@get('/manage/datasources/create')
def manage_datasources_create(*, page='1'):
    return {
        '__template__': 'datasource_edit.html',
        'id': '',
        'action': '/api/datasources'
    }

@get('/manage/datasources/{id}')
def manage_datasources_edit(*, id):
    return {
        '__template__': 'datasource_edit.html',
        'id': id,
        'action': '/api/datasources/%s' % id
    }

@get('/manage/metadata')
def manage_metadata(*, page='1'):
    return {
        '__template__': 'metadata.html',
        'page_index': get_page_index(page)
    }
