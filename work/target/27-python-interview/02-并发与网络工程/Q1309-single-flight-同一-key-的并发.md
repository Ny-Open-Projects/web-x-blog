---
title: [Q1309] single-flight:同一 key 的并发请求合并成一次执行
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1309 · single-flight:同一 key 的并发请求合并成一次执行

> 难度:★★★★ | 标签:single-flight, 请求合并, 缓存击穿

**问**:缓存失效瞬间 100 个线程同时去查同一个 key,怎么保证后端只被打一次?

**答**:这就是 single-flight(请求合并):进程内维护一张"进行中"表,key 换成一个 Future。第一个到达者成为 leader,登记 Future 后真正执行;后续到达者发现表里有 Future,直接 await 它的结果,不再发起自己的执行。leader 完成后 set_result 唤醒全部跟随者,并把自己从表里摘掉——注意摘除必须在 set_result 之后语义上成立、且在 finally 里做,保证异常时跟随者也能拿到异常而不是永远等待。它同时治三种病:缓存击穿(热点 key 失效)、重复计算(昂贵函数并发调用)、以及放大写压力(同 key 并发写合并)。局限也要会讲:只合并"此刻进行中"的,leader 完成瞬间新来的请求会再执行一次;要彻底防重需要结果缓存配合。下面的演示 10 个线程同 key 并发,底层只执行一次。

```python
# file: code/02_并发与网络工程/q1309_single_flight.py
import concurrent.futures
import threading
import time


class SingleFlight:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._inflight = {}   # key -> Future

    def run(self, key: str, fn):
        with self._lock:
            fut = self._inflight.get(key)
            if fut is not None:
                leader = False
            else:
                fut = concurrent.futures.Future()
                self._inflight[key] = fut
                leader = True
        if not leader:
            return fut.result()   # 跟随者: 等同一个结果或异常
        try:
            result = fn()
            fut.set_result(result)
            return result
        except BaseException as exc:
            fut.set_exception(exc)
            raise
        finally:
            with self._lock:
                self._inflight.pop(key, None)


def main() -> None:
    sf = SingleFlight()
    calls = {"n": 0}
    lock = threading.Lock()

    def slow_load() -> str:
        with lock:
            calls["n"] += 1
        time.sleep(0.2)               # 模拟昂贵的后端调用
        return f"payload-{calls['n']}"

    results = []
    errors = []

    def requester() -> None:
        try:
            results.append(sf.run("hot-key", slow_load))
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=requester) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len(results) == 10 and len(set(results)) == 1
    assert calls["n"] == 1, f"底层应只执行一次, 实际 {calls['n']}"
    print(f"10 个并发请求合并为 {calls['n']} 次执行, 结果一致: {results[0]}")

    # 异常也会传播给全部跟随者, 不会有人挂起
    def broken() -> None:
        raise RuntimeError("boom")
    errs = []
    threads = [threading.Thread(target=lambda: errs.append(capture(sf, "k", broken)))
               for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert all(isinstance(e, RuntimeError) for e in errs) and len(errs) == 3
    print(f"异常路径: {len(errs)} 个请求全部快速拿到异常, 无人挂起")


def capture(sf, key, fn):
    try:
        return sf.run(key, fn)
    except Exception as exc:
        return exc


if __name__ == "__main__":
    main()
```

**追问**:1) leader 完成后立刻来了新请求怎么办?——表里已经摘掉了,新请求会再执行一次;要彻底防重就在 run 外再包一层结果缓存,形成"缓存 + single-flight"的经典组合。2) 为什么摘除要在 finally 里?——leader 抛异常时若不摘除,跟随者 await 永远挂起;finally 里 set_exception + 摘除保证「跟随者要么拿到结果要么拿到异常」,这是请求合并实现最容易漏的路径。3) 与幂等存储(Q1339)、结果缓存怎么组合?——三层防线:single-flight 合并「此刻并发」、幂等存储覆盖「重试窗口」、结果缓存承接「完成后新请求」;击穿治理(缓存章 Q174)就是这套组合拳,面试要能画出三层的覆盖区间。4) 生产陷阱?——Future 无异常透传,跟随者拿 None 误当成功;key 构造不一致(参数序列化方式不同导致合并失败);等待者无超时,leader 卡死全体挂起;合并层把「不该合并」的请求也合了(带副作用的操作被合并执行一次,语义错)。

---
