import tornado
import math

class Paging(tornado.web.UIModule):
    def render(self,total,page,pagesize,feature_id):
        totalPage = int(math.ceil(total/float(pagesize)))
        # pageranges = range(1,totalPage+1)
        pageranges = filter(lambda x:x<=totalPage,filter(lambda x:x>0,range(page-5,page+6)))
        #if len(pageranges) == 0:
        #    pageranges = [1]
        total = total

        return self.render_string('page.html',pagesize=pagesize,feature_id=feature_id,pageranges=pageranges,currentPage=page,totalpage=totalPage,total=total)
