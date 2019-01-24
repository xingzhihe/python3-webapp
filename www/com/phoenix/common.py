#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'zhihe xing'

' common module '

import time, uuid

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

def get_current_folder():
    import os
    current_file = os.path.abspath(__file__)
    current_dir = os.path.abspath(os.path.dirname(current_file))
    return current_dir