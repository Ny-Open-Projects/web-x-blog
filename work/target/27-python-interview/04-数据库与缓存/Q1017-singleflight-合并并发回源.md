---
title: [Q1017] singleflight: 合并并发回源
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1017 · singleflight: 合并并发回源

> 难度:★★★★ | 标签:缓存击穿, singleflight

**问**:热点 key 失效瞬间上千请求同时回源 DB,除了分布式锁还有什么解法?

**答**:singleflight(单飞):同进程内,对同一 key 的并发请求合并成一次真实回源——第一个请求执行加载,其余等待共享结果。它把"进程内并发"直接压成 1 次 DB 查询,与分布式锁互补:锁解决"跨实例互斥",singleflight 解决"实例内重复"。实现:in-flight 字典 {key: Future},首个请求占位,后来者 await/等待同一 Future,完成后统一返回;加载失败则异常共享。配合:逻辑过期(Q171 的思路)让热点永不物理失效,singleflight 兜住冷启动与版本切换;超时保护防止上游 hang 死拖住全部等待者。Go 的 golang.org/x/sync/singleflight 是同名词来源。

```python
# file: code/04_数据库与缓存/q1017_singleflight.py
"""singleflight: 同 key 并发回源合并为一次"""
import threading
import time

class SingleFlight:
    def __init__(self):
        self.inflight = {}
        self.lock = threading.Lock()

    def do(self, key, loader):
        with self.lock:
            if key in self.inflight:             # 已有同伴在加载
                fut = self.inflight[key]
                owner = False
            else:
                fut = {"event": threading.Event(), "value": None,
                       "error": None, "waiters": 0}
                self.inflight[key] = fut
                owner = True
            if not owner:
                fut["waiters"] += 1
        if owner:
            try:
                fut["value"] = loader()
            except Exception as e:
                fut["error"] = e
            finally:
                fut["event"].set()
                with self.lock:
                    self.inflight.pop(key, None)
        fut["event"].wait()
        if fut["error"]:
            raise fut["error"]
        return fut["value"]

if __name__ == "__main__":
    calls = []
    sf = SingleFlight()

    def slow_loader():
        time.sleep(0.3)                          # 模拟 DB 查询
        calls.append(1)
        return "db-result"

    results = []
    def worker():
        results.append(sf.do("hot:key", slow_loader))
    ts = [threading.Thread(target=worker) for _ in range(8)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print(f"8 个并发请求 -> DB 实际调用 {len(calls)} 次, 结果一致: {len(set(results)) == 1}")
```

**追问**:
- 多实例下 singleflight 会退化成什么?——每实例各 1 次回源(N 实例 N 次),要进一步压缩就在前面加分布式锁或逻辑过期,层次是 singleflight -> 锁 -> 逻辑过期。
- 等待者超时怎么办?——等待加超时,超时者返回降级值或自己降级去 DB;owner 加载失败异常要共享给等待者,不能让它们白等。

---
