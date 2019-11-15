#!/usr/bin/env python
#coding: utf8

import tornado
from tornado.web import RequestHandler
from sqlalchemy.sql import or_,desc


class BaseHandler(RequestHandler):
    def render(self,*args,**kwargs):
        # user_name = self.get_secure_cookie('username')
        # user_info = self.application.db.query(UserModule).filter(UserModule.username==user_name).first()
        super(BaseHandler,self).render(*args,**kwargs)
        # super(BaseHandler,self).render(user_info=user_info,*args,**kwargs)
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    # def on_finish(self):
        # self.db.close_all()

    # def get_current_user(self):
        #print self.get_secure_cookie('group')
        #print self.get_secure_cookie('username')
        # return self.get_secure_cookie('group')

    # def get_user(self):
        #print self.get_secure_cookie('group')
        # return self.get_cookie('c')

    # @tornado.web.authenticated
    # def prepare(self):
    #     pass

    # @property
    # def db(self):
    #     return self.application.db
