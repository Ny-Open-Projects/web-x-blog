---
title: [Q974] 订阅 binlog 同步缓存: canal 模式
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q974 · 订阅 binlog 同步缓存: canal 模式

> 难度:★★★★ | 标签:缓存一致性, binlog

**问**:binlog 订阅同步缓存的链路是什么?比应用层双删好在哪?

**答**:链路:业务只写数据库 -> canal/flink-cdc 伪装从库拉 binlog -> 解析出表与行变更 -> 投递 MQ -> 缓存更新服务按变更删除/更新对应 key。优势:一、权威性——以数据库实际提交的变更为准,应用代码漏删、事务回滚误删都不存在;二、解耦——业务代码零侵入;三、顺序性——同一行的变更在单分区内有序。代价:引入 canal+MQ 组件、秒级延迟、需要处理 binlog 位点管理与重启续传。适用:一致性要求"最终一致但必须可靠"的核心数据(商品、库存展示层)。代码演示 oplog -> 失效服务的最小模型,对应 canal 的职责。

```python
# file: code/04_数据库与缓存/q974_binlog_sync.py
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
```

**追问**:
- 为什么投 MQ 而不直接删?——削峰与重试:大事务洪峰时直接删会打爆缓存,经 MQ 排队消费且失败可重投。
- binlog 是 ROW 还是 STATEMENT 模式?——同步缓存必须 ROW 模式,能拿到每行前后镜像;STATEMENT 只有 SQL 文本,语义还原不可靠。

---
