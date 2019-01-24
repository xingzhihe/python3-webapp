#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhihe xing'

import com.phoenix.expression.tokens as tokens

class TokenFactory(object):
    def __init__(self, expression):
        self.expression = expression
        self.tokens = []
    
    def parse(self):
        self.__lexer()
        return self.__syntax()
    
    # 词法分析器
    def __lexer(self):
        posBegin = 0
        posEnd = 0
        keyChars = ':[],'
        for char in self.expression:
            posEnd += 1
            if char in keyChars:
                if posEnd > posBegin + 1:
                    name = self.expression[posBegin:posEnd]
                    token = tokens.TokenString(self.expression, name[:-1]).begin(posBegin).end(posEnd - 1)
                    self.tokens.append(token)
                    posBegin = posEnd - 1
                
                if char == ':' :
                     self.tokens.append(tokens.TokenColon(self.expression).begin(posBegin).end(posEnd))
                elif char == '[' :
                    self.tokens.append(tokens.TokenOpeningSquareBucket(self.expression).begin(posBegin).end(posEnd))
                elif char == ']' :
                    self.tokens.append(tokens.TokenClosingSquareBucket(self.expression).begin(posBegin).end(posEnd))
                elif char == ',' :
                    self.tokens.append(tokens.TokenComma(self.expression).begin(posBegin).end(posEnd))
                
                posBegin = posEnd
    
    # 语法分析器
    def __syntax(self):
        tokensParsed = self.__syntaxSquareBucket()
        tokensParsed.append(tokens.TokenComma(self.expression))
        tokensParsed = self.__syntaxComma(tokensParsed)
        
        return tokensParsed

    
    # 中括号语法分析
    def __syntaxSquareBucket(self):
        result = []
        # 中括号嵌套时用来保存堆栈信息
        tokensSquareBucket = []
        for pos in range(len(self.tokens)):
            token = self.tokens[pos]
            
            # 处理左中括号
            if isinstance(token, tokens.TokenOpeningSquareBucket) :
                tokenSquareBucket = tokens.TokenSquareBucket(token.expression).begin(pos)
                tokensSquareBucket.append(tokenSquareBucket)
            # 处理右中括号
            elif isinstance(token, tokens.TokenClosingSquareBucket) :
                tokenSquareBucket = tokensSquareBucket.pop()
                tokenSquareBucket.end(pos)
                tokenSquareBucket.children.append(tokens.TokenComma(self.expression))
                
                if len(tokensSquareBucket) > 0 :
                    tokensSquareBucket[-1].children.append(tokenSquareBucket)
                else:
                    result.append(tokenSquareBucket)
            elif len(tokensSquareBucket) > 0:
                tokensSquareBucket[-1].children.append(token)
            else:
                result.append(token)
        
        if len(tokensSquareBucket) > 0:
            raise ValueError("[]没有闭合")
        
        return result
    
    # 语法分析器
    def __syntaxComma(self, list):
        result = []
        for pos in range(len(list)):
            token = list[pos]
            
            # 处理逗号
            if isinstance(token, tokens.TokenComma) and pos > 0:
                tokenPrev = list[pos - 1]
                if isinstance(tokenPrev, tokens.TokenSquareBucket) and pos > 2 :
                    tokenColon = list[pos - 2]
                    tokenParent = list[pos - 3]
                    if isinstance(tokenColon, tokens.TokenColon) and isinstance(tokenParent, tokens.TokenString) :
                        tokenParent.children = self.__syntaxComma(tokenPrev.children)
                        result.append(tokenParent)
                    else:
                        raise ValueError(":[]格式错误")
                elif isinstance(tokenPrev, tokens.TokenString):
                    if pos > 2 :
                        tokenColon = list[pos - 2]
                        tokenParent = list[pos - 3]
                        if isinstance(tokenColon, tokens.TokenColon) and isinstance(tokenParent, tokens.TokenString) :
                            name = "%s:%s" % (tokenParent.name, tokenPrev.name)
                            tokenPrev = tokens.TokenString(self.expression, name).begin(tokenParent.indexBegin).end(tokenPrev.indexEnd)

                    result.append(tokenPrev)
                else:
                    raise ValueError(",格式错误")
        
        return result
            
            
