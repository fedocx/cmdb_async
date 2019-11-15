
from BaseHandler import  BaseHandler
import tornado
import modules
import json
from urlmap import urlmap
from app1 import *

# @urlmap(r'/')
# class MainHandler(BaseHandler):
#     @tornado.web.asynchronous
#     @tornado.web.authenticated
#     def get(self):
#         group = self.current_user
#         username = self.get_secure_cookie('username')
#         self.render("index.html",user=username,group=group)
#     def post(self):
#         str = self.get_argument("test",None)
#         username = self.get_secure_cookie('username')
#         num = self.application.db.query(UserModule).filter(UserModule.svn==2).count()
#         allnum = self.application.db.query(UserModule).filter(or_(UserModule.svn==2,UserModule.git==2,UserModule.jump==2,UserModule.sqlaudit==2,UserModule.vpn==2)).count()
#         self.set_status(200)
#         data = {'num':num,'allnum':allnum}
#         self.write(json.dumps(data))

@urlmap(r'/property')
class PropertyStat(BaseHandler):
    # @tornado.web.authenticated
    def get(self):
        #self.render('property.html')
        self.write("敬请期待!!!")
#class MonitoringPlatform(BaseHandler):
#    def get(self):
#        self.render('monitoring.html')

"""
正则匹配template下的html文件。
"""

@urlmap(r"/(.*)\.html")
class ReadTemplateHandler(BaseHandler):
    # @tornado.web.authenticated
    def get(self,template):
        # group = self.current_user
        # username = self.get_secure_cookie('username')
        # self.render("{0}.html".format(template),group=group)
        self.render("{0}.html".format(template))

"""
1、定义debug调试功能；模板路径；静态文件路径；用来设置静态文件地址的等方法。
2、定义路由。
"""
def make_app():
    settings={
        # 'cookie_secret':'bZJc2sWbQ8yU7ACkHn/VB9oXwEdvS0R0kRvJ5/xJ89E==',
        'debug':True,
        'template_path':'template/',
        'static_path':'template/assets',
        'static_url_prefix':'/assets/',
        'ui_modules':modules,
        # 'xsrf_cookies':True,
        'login_url':'/login'
    }
    app = tornado.web.Application(handlers=urlmap.handlers,**settings)
    # app.db = session
    return app

"""
在8888端口开始监听。启动事件循环，开始监听网络事件。
"""
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
