"""旁路缓存的并发双读: 未命中风暴的实测与单飞抑制"""
import threading
import time

db_reads = {"count": 0}
db_lock = threading.Lock()

def slow_db_read(key):                                # 模拟一次 40 ms 的回源
    with db_lock:
        db_reads["count"] += 1
    time.sleep(0.04)
    return "value-of-" + key

def storm(cache, key, n, per_key_lock):
    barrier = threading.Barrier(n)
    lock_for_key = threading.Lock()
    results = [None] * n

    def worker(i):
        barrier.wait()                                # 32 个请求同时到达
        if per_key_lock:
            with lock_for_key:                        # 单飞: 只放一个回源
                if key not in cache:
                    cache[key] = slow_db_read(key)
        else:
            if key not in cache:                      # 无控制: 谁没命中谁回源
                cache[key] = slow_db_read(key)
        results[i] = cache[key]

    ts = [threading.Thread(target=worker, args=(i,)) for i in range(n)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return results

N = 32
db_reads["count"] = 0
storm({}, "item:42", N, per_key_lock=False)
print("无控制并发双读: %d 个并发未命中 -> 回源 %d 次 (数据库被打了 %d 倍)" % (N, db_reads["count"], db_reads["count"]))

db_reads["count"] = 0
cache = {}
storm(cache, "item:42", N, per_key_lock=True)
print("加键级互斥锁:   %d 个并发未命中 -> 回源 %d 次 (其余全部等首次回源后读缓存)" % (N, db_reads["count"]))
assert db_reads["count"] == 1
assert all(v == "value-of-item:42" for v in cache.values() if v)
print("结论: 未命中风暴是缓存击穿的微观形态, 键级互斥让回源从 N 次塌缩成 1 次,")
print("      工程上再加'等待超时后直接读库'的逃生门, 防止持锁线程挂死造成雪崩")
