#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' metadata_controller handlers '

from aiohttp import web
from coroweb import get, post, put, delete
from apis import Page, APIError, APIValueError, APIResourceNotFoundError, APIPermissionError

from models import DataSource
from common import get_page_index

