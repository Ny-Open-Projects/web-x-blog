---
title: [Q1778] 同 query 并发合并:singleflight 去重
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1778 · 同 query 并发合并:singleflight 去重

> 难度:★★★☆ | 标签:LLM 运维, 并发, 缓存击穿

**问**:热点问题瞬间来了几十个相同 query,全都打到模型,怎么合并?

**答**:singleflight 模式:相同 key 的并发请求,第一个到达者真正执行,其余注册为跟随者挂起等待,首到者完成后把结果或异常广播给全部跟随者。这样底层调用次数恒等于不同 key 数,而不是并发请求数,热点击穿被结构性消除;异常也要广播,跟随者拿到和首到者一致的失败,而不是各查各的。实现要点是注册与执行之间用锁保证原子,完成时先落结果再唤醒,等待要有超时,防止首到者崩溃把跟随者永久挂起。

```python
# file: code/06_Agent与LLM及系统设计/q1778_singleflight.py
"""同 query 并发合并:singleflight 让相同 key 的并发请求共享一次执行与结果。"""
import threading
import time


class Singleflight:
    def __init__(self):
        self._lock = threading.Lock()
        self._inflight = {}

    def do(self, key, fn):
        with self._lock:
            if key in self._inflight:
                event, box = self._inflight[key]     # 跟随者:共享首到者执行
                follower = True
            else:
                event, box = threading.Event(), {"result": None, "error": None}
                self._inflight[key] = (event, box)
                follower = False
        if follower:
            event.wait(timeout=5)
            if box["error"] is not None:
                raise box["error"]
            return box["result"]
        try:
            box["result"] = fn()                     # 只有首到者执行
            return box["result"]
        except Exception as e:
            box["error"] = e                         # 异常同样广播给跟随者
            raise
        finally:
            with self._lock:
                self._inflight.pop(key, None)
                event.set()


CALLS = {"n": 0}
CALL_LOCK = threading.Lock()


def slow_lookup(key):
    with CALL_LOCK:
        CALLS["n"] += 1
    time.sleep(0.15)                                 # 模拟慢调用,给并发窗口
    return "value:" + key


if __name__ == "__main__":
    sf = Singleflight()
    gate = threading.Barrier(4)
    results = []

    def worker(key):
        gate.wait(timeout=5)                         # 四线程同时对同一 key 发起
        results.append(sf.do(key, lambda: slow_lookup(key)))

    threads = [threading.Thread(target=worker, args=("q1",)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=5)

    assert len(results) == 4 and all(r == "value:q1" for r in results)
    assert CALLS["n"] == 1, "相同 key 的 4 个并发请求只执行 1 次底层调用"

    assert sf.do("q2", lambda: slow_lookup("q2")) == "value:q2"
    assert CALLS["n"] == 2, "不同 key 各自执行"
    print("singleflight 通过:同 key 并发合并执行共享结果,不同 key 互不影响")
```

**追问**:
- key 怎么定? 答:请求语义的规范化哈希,包括模型、参数与消息体,参数不同不能合并,否则返回错答案。
- 和语义缓存什么区别? 答:singleflight 合并进行中的并发请求,语义缓存命中已完成的相似请求,一个管瞬时风暴一个管历史重复。
