#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' metadata_controller handlers '

from aiohttp import web
from coroweb import get, post, put, delete
from com.phoenix.apis import Page, APIError, APIValueError, APIResourceNotFoundError, APIPermissionError

from com.phoenix.models import DataSource
from com.phoenix.common import get_page_index

@post('/api/metadata/analyse/{dsId}/{db}')
async def api_datasource_create(request, *, dsId,db,tables):
    ds = await DataSource.find(dsId)
    dsMetadata = ds.get_MetadataSource()
    from com.phoenix.connections.connectionFactory import get_Connection
    conn = get_Connection(dsMetadata)
    arr = conn.analyse(db,tables)
    result = {}
    for item in arr:
        result[item["db_name"] + '.' + item["table_name"]]= dict(num_files=item["num_files"], num_rows=item["num_rows"], total_size=item["total_size"])
    return result
