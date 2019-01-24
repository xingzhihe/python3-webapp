#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhihe xing'

'''
基本解析单元
'''
class Token(object):
    def __init__(self, expression, name):
        self.expression = expression
        self.indexBegin = -1
        self.indexEnd = -1
        self.length = 0
        self.name = name

    # 开始位置
    def begin(self, index):
        self.indexBegin = index
        return self

    # 结束位置
    def end(self, index):
        self.indexEnd = index
        self.length = self.indexEnd - self.indexBegin
        return self

'''
字符串解析单元
'''
class TokenString(Token):
    def __init__(self, expression, name):
        super().__init__(expression, name)
        self.children = []

    # 追加子单元
    def appendChild(self, token):
        self.children.append(token)
        return self

    # 删除子单元
    def removeChild(self, token):
        self.children.remove(token)
        return self

    # 清空字段元集合
    def clearChildren(self):
        del self.children[:]
        return self

'''
逗号单元 ,
'''
class TokenComma(Token):
    def __init__(self, expression):
        super().__init__(expression, ',')

'''
冒号单元 :
'''
class TokenColon(Token):
    def __init__(self, expression):
        super().__init__(expression, ':')

'''
中括号单元 []
'''
class TokenSquareBucket(Token):
    def __init__(self, expression):
        super().__init__(expression, '[]')
        self.children = []
'''
左中括号单元 [
'''
class TokenOpeningSquareBucket(Token):
    def __init__(self, expression):
        super().__init__(expression, '[')

'''
左中括号单元 ]
'''
class TokenClosingSquareBucket(Token):
    def __init__(self, expression):
        super().__init__(expression, ']')