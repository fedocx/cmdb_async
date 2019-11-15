import time
from AsyncCelery import cele


@cele.task
def havefun(args):
    # do something
    # ...

    # 模拟执行耗时任务
    print
    u"开始执行celery任务"
    time.sleep(10)
    print
    u"celery任务结束"

    return args