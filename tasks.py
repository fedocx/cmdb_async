from celery import Celery
import time

# app = Celery('tasks', broker='pyamqp://celery:celery@localhost:5672/celery_host/')
# app = Celery('tasks', broker='pyamqp://celery:celery@localhost:5672/celery_host', backend='redis://:celery@47.99.150.141:6375/2')
app = Celery('tasks', broker='redis://:celery@47.99.150.141:6375/1', backend='redis://:celery@47.99.150.141:6375/2')

@app.task
def add(x, y):
    time.sleep(600)
    return x + y