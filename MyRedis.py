import redis


r = redis.Redis(host='47.99.150.141', port=6375, decode_responses=True,password="celery",db=2)
keys = r.keys()
for i in keys:
    print(r.get(i))

