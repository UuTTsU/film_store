import json
import redis

rd = redis.StrictRedis(port=6379)


class Redis:
    def __init__(self):
        self.rd = redis.StrictRedis(port=6379)

    def set(self, cache_key, input_data):
        dumped_data = json.dumps(input_data)
        self.rd.set(cache_key, dumped_data,30)
        return True

    def get(self, cache_key):
        cache_data = self.rd.get(cache_key)
        if not cache_data:
            return False
        cache_data_json = json.loads(cache_data)
        return cache_data_json


