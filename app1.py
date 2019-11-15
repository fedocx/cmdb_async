import tornado
from  BaseHandler  import BaseHandler
from urlmap import urlmap
import redis


@urlmap(r'/app')
class test(BaseHandler):


    def get(self):
        self.set_status(300)
        self.render("index.html")


