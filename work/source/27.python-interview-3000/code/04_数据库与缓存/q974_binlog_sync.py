"""binlog 同步缓存最小模型: oplog 解析 -> 删除缓存"""
import queue
import threading
import time

def business_write(db, oplog_q, key, value):
    db[key] = value                           # 1. 业务只写库
    oplog_q.put(("UPDATE", key, value))       # 2. 数据库产生变更记录(binlog)

def cache_sync_worker(db, oplog_q, cache, stop):
    while not stop.is_set():
        try:
            op, key, value = oplog_q.get(timeout=0.1)
        except queue.Empty:
            continue
        if op in ("UPDATE", "DELETE"):
            cache.pop(key, None)               # 3. 解析变更并失效缓存
            print(f"binlog 事件 {op} {key} -> 缓存已失效, db={db.get(key)}")

if __name__ == "__main__":
    db, cache = {"goods:1": "v1"}, {"goods:1": "v1"}
    q, stop = queue.Queue(), threading.Event()
    threading.Thread(target=cache_sync_worker,
                     args=(db, q, cache, stop), daemon=True).start()

    business_write(db, q, "goods:1", "v2")
    time.sleep(0.3)
    print("缓存内容:", cache, "<- 已随 binlog 失效, 下次读回源新值")
    stop.set()
