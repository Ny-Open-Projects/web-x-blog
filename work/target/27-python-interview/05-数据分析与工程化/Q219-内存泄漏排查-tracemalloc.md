---
title: [Q219] 内存泄漏排查:tracemalloc
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q219 · 内存泄漏排查:tracemalloc

> 难度:★★★★ | 标签:tracemalloc, 内存泄漏, gc

**问**:服务 RSS 缓慢上涨最终 OOM,你怎么定位?

**答**:先确认是真泄漏还是**内存碎片/缓存无上限**(如全局 list 一直 append、lru_cache 无界)。工具链:**tracemalloc** 在 Python 层精确到分配代码行——`start()` 采样,定时 `take_snapshot()`,两次快照 `compare_to` 按增量排序,top 文件+行号直接指认泄漏点;**objgraph** 找引用链(`find_backref_chain`)看谁持有了本该释放的对象;**gc.get_objects/gc.collect** 检测循环引用。经典根因:全局缓存无界、闭包/异常对象被日志持有、C 扩展(如 pandas 临时大对象)、跨请求持有 session。生产建议:低频开启 tracemalloc(有 2 倍左右开销),配合按请求的内存指标。

```python
# file: code/05_数据分析与工程化/q219_tracemalloc.py
import tracemalloc


class Cache:
    # 无界缓存:内存泄漏的典型形态
    def __init__(self):
        self._data = {}

    def put(self, key, value):
        self._data[key] = value


def leak_simulation():
    tracemalloc.start()
    cache = Cache()
    before = tracemalloc.take_snapshot()
    for i in range(10_000):
        cache.put(f"key-{i}", "x" * 64)
    after = tracemalloc.take_snapshot()
    stats = after.compare_to(before, "lineno")
    top = stats[0]
    tracemalloc.stop()
    return top.size_diff


def test_detect_growth():
    growth = leak_simulation()
    # 检测到明显增长,证明定位到了泄漏点
    assert growth > 10_000
```

**追问**:
- tracemalloc 和 memory_profiler 区别?——tracemalloc 定位"哪行代码分配了增长",memory_profiler 看进程整体 RSS 随时间曲线,通常先用后者确认泄漏再用前者定位。
- tracemalloc 的开销?——采样模式约 2 倍内存追踪成本,生产常开低采样频率;只对可疑进程/时段开启。
- lru_cache 怎么变成泄漏?——maxsize=None 无界缓存键不断增长;方法上缓存还持有 self。排查时先查全局容器与缓存。
- objgraph 的用法?——`objgraph.growth()` 看类型增长、`find_backref_chain` 找持有链;谁引用了它,谁就是泄漏源。
