#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhihe xing'

import os
from com.phoenix.common import get_current_folder

class Resource(object):
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def appendItem(self, item):
        self.items.append(item)
    
    def setItems(self, items):
        self.items = items
        return self
    
    def clearItems(self):
        self.items = []
    
    def __str__(self):
        strItems = ''
        for item in self.items:
            strItems += item.__str__() + ','
        
        return self.name if len(self.items) == 0 else '%s:[%s]' % (self.name, strItems[:-1])

class ResourceFactory(object):
    def __init__(self, dataFile):
        self.initDataFile(dataFile)

    def load(self):
        with open(self.dataFile) as fr:  
            content = fr.read()
            try:
                # resource = self.parse(content)
                import com.phoenix.expression.factory as exp
                tokens = exp.TokenFactory(content).parse()
                resources = self.token2Resource(tokens)
                resource = resources[0] if len(resources) > 0 else None
            except ValueError as err:
                print(err.args)

        if resource is None:
            resource = Resource("root")

        return resource

    def save(self, resource):
        str = resource.__str__()
        with open(self.dataFile, 'w') as fw:  
            fw.write(str)

    def token2Resource(self, tokens):
        resources = []
        for token in tokens:
            resource = Resource(token.name)
            if len(token.children) > 0 :
                resource.items = self.token2Resource(token.children)
            resources.append(resource)

        return resources

    def parse22(self, exp):
        posBegin = 0
        pos = 0
        tokens = []
        token = ResourceToken(exp)
        token.begin(posBegin)
        tokens.append(token)
        for char in exp:
            if char == ':' :
                token.hasItems = True
                token.setName(exp[posBegin: pos])
                posBegin = pos + 1
            elif char == '[' :
                posBegin = pos + 1
                token = ResourceToken(exp)
                token.begin(posBegin)
                tokens.append(token)
            elif char == ']' :
                token.end(pos)

                top = tokens[len(tokens) - 1]
                token[len(tokens) - 2].items.append(top)
                tokens.remove(len(tokens) - 1)
            elif char == ',' :
                top = tokens[len(tokens) - 1]
                if top.hasItems == False:
                    top.setName(exp[posBegin: pos])
                    top.end(pos)

                token[len(tokens) - 2].items.append(top)
                tokens.remove(len(tokens) - 1)
                posBegin = pos + 1

                token = ResourceToken(exp)
                token.begin(posBegin)
                tokens.append(token)
            pos += 1

    def parse(self, str):
        posBegin = 0
        posEnd = len(str)
        resource = None
        pos = str.find(':', posBegin)
        if pos > -1 :
            resource = Resource(str[posBegin:pos])
            
            if str[pos + 1] == '[' and str[-1] == ']':
                posBegin = pos + 2
                posEnd = len(str) - 1
                pos = str.find(',', posBegin, posEnd)
                while(pos > -1):
                    subResource = self.parse(str[posBegin:pos])
                    resource.appendItem(subResource)
                    posBegin = pos + 1
                    pos = str.find(',', posBegin, posEnd)
                
                subResource = Resource(str[posBegin:posEnd])
                resource.appendItem(subResource)
            else:
                # raise ValueError("Invalid resource","resource must contain '[' and ']' after ':'. str=%s" % str)
                resource = Resource(str)
        elif posEnd > 0:
             resource = Resource(str)

        return resource

    def initDataFile(self, dataFile):
        current_file = os.path.abspath(__file__)
        current_dir = os.path.abspath(os.path.dirname(current_file))
        #current_dir = get_current_folder()
        filePath = os.path.join(current_dir, '..', '..', '..', 'conf',dataFile)
        if not os.path.exists(filePath):
            os.system(r'touch %s' % filePath)
        self.dataFile = filePath

class ResourceToken(object):
    def __init__(self, exp):
        self.exp = exp
        self.posBegin = -1
        self.posEnd = -1
        self.hasItems = False
        self.items = []
    
    def setName(self, name):
        self.name = name
        return self
    
    def getName(self):
        return self.name
    
    def begin(self, posBegin):
        self.posBegin = posBegin
        return self
    
    def end(self, posEnd):
        self.posEnd = posEnd
    
    def len(self):
        return self.posEnd - self.posBegin

class ResourceService(object):
    def __init__(self):
        self.factory = ResourceFactory('resoucrce.core')
        
        self.rootResource = gl.get_value('rootResource')
        if self.rootResource is None :
            self.rootResource = self.factory.load()
            gl.set_value('rootResource', self.factory.load())

    def add(self, resource):
        if isinstance(resource, str):
            self.rootResource.appendItem(self.factory.parse(resource))
        else:
            self.rootResource.appendItem(resource)
        
        self.factory.save(self.rootResource)
    
    def update(self, resource):
        try:
            index = self.rootResource.items.index(resource)
            self.rootResource.items[index] = resource
            self.factory.save(self.rootResource)
        except ValueError:
            print('update resource occur error!')
    
    def updateWithIndex(self, index, resource):
        try:
            index = int(index)
            self.rootResource.items[index] = resource
            self.factory.save(self.rootResource)
        except ValueError:
            print('update resource occur error!')
    
    def updateWithName(self, name, resource):
        try:
            res = [item for item in self.rootResource.items if item.name == name]
            if res:
                index = self.rootResource.items.index(res[0])
                self.rootResource.items[index] = resource
                self.factory.save(self.rootResource)
        except ValueError:
            print('update resource occur error!')
        
    def remove(self, resource):
        try:
            if isinstance(resource, str):
                index = int(resource)
            else:
                index = self.rootResource.items.index(resource)
            del self.rootResource.items[index]
            self.factory.save(self.rootResource)
        except ValueError:
            pass
        
    def removeByName(self, name):
        try:
            res = [item for item in self.rootResource.items if item.name == name]
            if res:
                index = self.rootResource.items.index(res[0])
                del self.rootResource.items[index]
                self.factory.save(self.rootResource)
        except ValueError:
            pass

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('resource 初始化')
    
    import com.phoenix.globalvar as gl
    gl._init()