#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' metadata_controller handlers '

from aiohttp import web
from coroweb import get, post, put, delete
from com.phoenix.apis import Page, APIError, APIValueError, APIResourceNotFoundError, APIPermissionError

from com.phoenix.models import DataSource
from com.phoenix.common import get_page_index

@get('/api/metadata/analyse/{dsId}/{db}/{table}/partitions')
async def api_metadata_analyse_partition(request, *, dsId,db,table):
    ds = await DataSource.find(dsId)
    from com.phoenix.connections.connectionFactory import get_Connection
    conn = get_Connection(ds)
    conn.computeStats(db,table)

    dsMetadata = ds.get_MetadataSource()
    from com.phoenix.connections.connectionFactory import get_Connection
    conn = get_Connection(dsMetadata)
    arr = conn.analysePartition(db,table)
    result = {}
    for item in arr:
        result[item["table_name"] + '.' + item["partition_name"]]= dict(num_files=item["num_files"], num_rows=item["num_rows"], total_size=item["total_size"])
    return result

@get('/api/metadata/analyse/{dsId}/{db}/{table}')
async def api_metadata_analyse_table(request, *, dsId,db,table):
    ds = await DataSource.find(dsId)
    from com.phoenix.connections.connectionFactory import get_Connection
    conn = get_Connection(ds)
    conn.computeStats(db,table)

    dsMetadata = ds.get_MetadataSource()
    from com.phoenix.connections.connectionFactory import get_Connection
    conn = get_Connection(dsMetadata)
    arr = conn.analyse(db,table)
    result = {}
    for item in arr:
        result[item["db_name"] + '.' + item["table_name"]]= dict(num_files=item["num_files"], num_rows=item["num_rows"], total_size=item["total_size"])
    return result

@post('/api/metadata/analyse/{dsId}/{db}')
async def api_metadata_analyse(request, *, dsId,db,tables):
    ds = await DataSource.find(dsId)
    dsMetadata = ds.get_MetadataSource()
    from com.phoenix.connections.connectionFactory import get_Connection
    conn = get_Connection(dsMetadata)
    arr = conn.analyse(db,tables)
    result = {}
    for item in arr:
        result[item["db_name"] + '.' + item["table_name"]]= dict(num_files=item["num_files"], num_rows=item["num_rows"], total_size=item["total_size"])
    return result

@get('/api/metadata/setting')
async def get_metadata_setting(request):
    import json
    json_file=getMetadataSettingJsonFile()
    with open(json_file) as fr:  
        settings = json.load(fr)
    return settings

@post('/api/metadata/setting')
async def save_metadata_setting(request, *, settings):
    import json
    json_file=getMetadataSettingJsonFile()
    with open(json_file, 'w') as fw:  
        json.dump(settings, fw, ensure_ascii=False)
    return {'result': 'ok'}

def getMetadataSettingJsonFile():
    import os
    current_file = os.path.abspath(__file__)
    current_dir = os.path.abspath(os.path.dirname(current_file))
    json_file=os.path.join(current_dir,'..', 'static','js','metadata.settings.json')
    if not os.path.exists(json_file):
        os.system(r'touch %s' % json_file)
    return json_file