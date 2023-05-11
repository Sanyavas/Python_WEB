import timeit

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def fibonacci(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    start = timeit.default_timer()
    fibonacci(35)
    print(f"Result f(35): {timeit.default_timer() - start}")

