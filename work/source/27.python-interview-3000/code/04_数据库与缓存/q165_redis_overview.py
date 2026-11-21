"""redis-py 五大结构最小示例; 无 Redis 时用内存字典模拟语义"""
try:
    import redis
    client = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
    client.ping()
except Exception as exc:
    print("无可用 Redis, 仅打印语义:", exc)
else:
    client.set("counter", 0)
    print("String INCR:", client.incr("counter"))                  # 1

    client.hset("cart:u1", mapping={"sku1": 2, "sku2": 1})
    print("Hash 购物车:", client.hgetall("cart:u1"))               # {'sku1': '2', ...}

    client.rpush("mq:orders", "o1", "o2")
    print("List 出队:", client.lpop("mq:orders"))                  # o1

    client.sadd("tag:python", "u1", "u2")
    client.sadd("tag:redis", "u2", "u3")
    print("Set 交集:", client.sinter("tag:python", "tag:redis"))   # {'u2'}

    client.zadd("rank", {"alice": 90, "bob": 95})
    print("ZSet 榜单:", client.zrevrange("rank", 0, -1, withscores=True))
