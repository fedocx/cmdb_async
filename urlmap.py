#!/usr/bin/env python
#coding: utf8

class Urlmap(object):
    def __init__(self):
        self.handlers = []

    def __call__(self,url,**kwargs):
        def _(cls):
            self.handlers.append((url,cls,kwargs))
            return cls
        return _

# print type(Urlmap)
urlmap = Urlmap()
