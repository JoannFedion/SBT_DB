import json
import redis
import time

r = redis.Redis(host='localhost', port=6379)

with open("file.json") as f:
    data = json.loads(f.read())
# data = json.load(open('large-file.json', 'r'))

start_time = time.time()
r.set('data_string', json.dumps(data))
end_time = time.time()
print(f"Сохранение (как строка): {end_time - start_time}")

start_time = time.time()
r.get('data_string')
end_time = time.time()
print(f"Чтение (как строка) {end_time - start_time}")

start_time = time.time()
r.hset('data_hash', mapping=data)
end_time = time.time()
print(f"Сохранение (как hset): {end_time - start_time}")

start_time = time.time()
r.hgetall('data_hset')
end_time = time.time()
print(f"Чтение (как hset) {end_time - start_time}")

start_time = time.time()
r.zadd('data_zset', data)
end_time = time.time()
print(f"Сохранение (как zset): {end_time - start_time}")

start_time = time.time()
r.zrange('data_zset', 0, -1, withscores=True)
end_time = time.time()
print(f"Чтение (как zset) {end_time - start_time}")

start_time = time.time()
r.rpush('data_list', json.dumps(data))
end_time = time.time()
print(f"Сохранение (как list) {end_time - start_time}")

start_time = time.time()
r.lrange('data_list', 0, -1)
end_time = time.time()
print(f"Чтение (как list) {end_time - start_time}")