---
title: [Q573] multiprocessing.Manager 与代理对象的陷阱
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q573 · multiprocessing.Manager 与代理对象的陷阱

> 难度:★★★☆ | 标签:Manager, 代理对象, IPC

**问**:Manager 和 shared_memory/Value 有什么本质区别?Manager 的 dict 是不是就线程/进程安全了?

**答**:Manager 起了一个独立的服务进程,其他进程拿到的是 Proxy 对象,每次操作都通过 socket/pickle 转发给服务进程,所以单个操作(如 `d[k] = v`)是原子的;但它慢一个数量级,且"复合操作"(`d[k] = d.get(k, 0) + 1`)依然是读-改-写两步,必须配合 `manager.Lock()`。另一个大坑:嵌套对象——往 proxy dict 里放一个普通 dict,读出来的副本是反 pickle 的新对象,原地修改不会同步回去,要用 `m.dict()` 做嵌套。Manager 的价值是任意 Python 对象的跨进程共享,代价是性能。

```python
# file: code/02_并发与网络工程/q573_manager.py
import multiprocessing as mp

N = 300  # Manager 每次操作都是一次 IPC 往返, 且 macOS spawn 子进程很慢,
         # 进程数与规模都要小, 保证 25s 内跑完


def race_worker(d) -> None:
    """复合操作不加锁: 演示丢失更新。"""
    for _ in range(N):
        d["count"] = d.get("count", 0) + 1


def safe_worker(d, lock) -> None:
    for _ in range(N):
        with lock:
            d["count"] = d.get("count", 0) + 1


def nested_worker(d) -> None:
    inner = d["inner"]        # 反 pickle 出来的本地副本(普通 dict)!
    inner["hit"] = inner.get("hit", 0) + 1  # 改的是副本, 不回传


if __name__ == "__main__":
    with mp.Manager() as mgr:
        d1 = mgr.dict()
        ps = [mp.Process(target=race_worker, args=(d1,)) for _ in range(2)]
        for p in ps:
            p.start()
        for p in ps:
            p.join()
        print(f"无锁复合操作: {d1['count']} / 期望 {2 * N}")

        d2 = mgr.dict()
        lk = mgr.Lock()
        ps = [mp.Process(target=safe_worker, args=(d2, lk)) for _ in range(2)]
        for p in ps:
            p.start()
        for p in ps:
            p.join()
        print(f"加锁复合操作: {d2['count']} / 期望 {2 * N}")
        assert d2["count"] == 2 * N, "加锁复合操作不允许丢失更新"

        d3 = mgr.dict()
        d3["inner"] = {}  # 普通嵌套 dict
        # 注意: 传给子进程的只能是 Proxy/可 pickle 对象, Manager 本体
        # 持有 weakref 与进程句柄, 传 mgr 会 TypeError: cannot pickle 'weakref'
        p = mp.Process(target=nested_worker, args=(d3,))
        p.start()
        p.join()
        print("嵌套普通 dict 修改丢失:", d3["inner"] == {})

        d4 = mgr.dict()
        d4["inner"] = mgr.dict()  # 嵌套也要用代理
        p = mp.Process(target=nested_worker, args=(d4,))
        p.start()
        p.join()
        print("嵌套 Manager dict 生效:", d4["inner"].get("hit"))
        assert d4["inner"].get("hit") == 1
```

**追问**:1) Manager 的性能瓶颈在哪,怎么优化?——每次操作一次 IPC 往返 + pickle;优化方向是批量读写(一次取回大对象本地处理)、或换成 Value/Array+锁、或重新设计为消息传递。2) 代理对象的边界?——proxy 方法转发 IPC;嵌套 proxy(m_list[i].append)一次调用多轮往返;Proxy 不可 pickle 传递给孙进程;比较/切片语义与本地对象有差。3) 与 shared_memory 的分工?——Manager 管「结构同步」(dict/list 语义);shared_memory 管「大块字节」(零拷贝,Q567);消息传递管「松耦合」。4) 生产陷阱?——循环里逐元素改 proxy(万次 IPC);proxy 对象长期持有(管理进程状态膨胀);Manager 进程崩溃全代理失效。

---
