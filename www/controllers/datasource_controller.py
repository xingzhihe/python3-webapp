#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' datasource_controller handlers '

from aiohttp import web
from coroweb import get, post, put, delete
from apis import Page, APIError, APIValueError, APIResourceNotFoundError, APIPermissionError

from models import DataSource
from common import get_page_index

@get('/api/datasources')
async def api_datasource_findAll(*, page='1'):
    page_index = get_page_index(page)
    num = await DataSource.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    datasources = await DataSource.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, datasources=datasources)

@get('/api/datasources/{id}')
async def api_datasource_findById(*, id):
    ds = await DataSource.find(id)
    return ds

@post('/api/datasources')
async def api_datasource_create(request, *, db_type, host, database, port, user, password, options):
    ds = DataSource(db_type=db_type, host=host, database=database, port=port, user=user, password=password, options=options)
    await ds.save()
    return ds

@put('/api/datasources/{id}')
async def api_datasource_update(id, request, *, db_type, host, database, port, user, password, options):
    ds = await DataSource.find(id)
    ds.db_type=db_type
    ds.host=host
    ds.database=database
    ds.port=port
    ds.user=user
    ds.password=password
    ds.options=options
    await ds.update()
    return ds

@delete('/api/datasources/{id}')
async def api_datasource_delete(request, *, id):
    ds = await DataSource.find(id)
    await ds.remove()
    return dict(id=id)

@get('/api/datasources/{id}/databases')
async def api_datasource_databases(*, id):
    ds = await DataSource.find(id)
    from impalaConnection import showDatabases
    databses = showDatabases(ds)
    return dict(databses=databses)

@get('/api/datasources/{id}/databases/{db}/tables')
async def api_datasource_tables(*, id, db):
    ds = await DataSource.find(id)
    ds['database'] = db
    from impalaConnection import showTables
    tables = showTables(ds)
    return dict(tables=tables)
