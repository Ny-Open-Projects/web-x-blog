"""redis-py pipeline 批量写; 无 Redis 时对比逐条与攒批的往返次数模型"""
try:
    import redis
    client = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
    client.ping()
except Exception as exc:
    print("无可用 Redis, 原理说明:", exc)
    print("逐条: N 条命令 N 次 RTT; pipeline: N 条命令 1 次 RTT")
else:
    # 逐条写: 1000 次 RTT
    for i in range(100):
        client.set(f"batch:{i}", i)

    # pipeline 写: 1 次 RTT
    with client.pipeline(transaction=False) as pipe:   # transaction=False 纯攒包
        for i in range(100):
            pipe.set(f"batch:{i}", i * 10)
        pipe.incr("pipeline:runs")
        results = pipe.execute()                        # 一次性取回全部响应

    print("pipeline 返回响应数:", len(results))
    print("计数器:", client.get("pipeline:runs"))
