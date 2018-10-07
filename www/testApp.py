#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhihe xing'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

import orm
from coroweb import add_routes, add_static

from config import toDict

from models import User, Comment, Blog, next_id

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
env = Environment(loader=FileSystemLoader(path))

async def users(request):
    tpl=env.get_template("test.html")
    users = await User.findAll()
    for u in users:
        print(u)
    model={
        '__template__': 'users.html',
        'name':'xingzhihe',
        'age':2897,
        'users': users
    }
    dic=toDict(model)
    return web.Response(body=tpl.render(**dic))

async def init(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='root', db='awesome')
    global app
    app = web.Application(loop=loop)
    #env = Environment(loader=PackageLoader('yourapplication', 'templates'))
    app.router.add_route('GET', '/users', users)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
    
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()