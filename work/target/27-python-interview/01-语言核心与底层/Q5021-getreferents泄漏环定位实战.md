---
title: [Q5021] gc.get_referents 泄漏环定位实战：谁拽住了对象
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5021 · gc.get_referents 泄漏环定位实战：谁拽住了对象

> 难度:★★★★☆ | 标签:gc, 内存泄漏, tracemalloc

**问**：tracemalloc 能看到哪行代码在涨内存，但看不到"这个对象为什么还活着"。怎么从嫌疑对象出发反查引用链，把泄漏根找到？引用环和真正的泄漏根要怎么区分？

**答**：两条链路互补：tracemalloc 回答"哪里分配的"（Q506），gc 回答"为什么没释放"。CPython 的环收集器本来就能回收纯引用环，所以环本身不是泄漏；泄漏的真正根是**环外仍有活引用拽着**——典型是全局容器、模块级缓存、闭包或异常 traceback 挂着。定位方法：用 `gc.get_objects()` 枚举全部存活对象，对每个候选调 `gc.get_referents(candidate)` 检查它直接引用了谁（实例的属性在 `__dict__` 里，需要下钻一层），找到"谁引用了嫌疑对象"，从环内一路爬到全局强引用即泄漏根。注意 `get_referents` 不受 `__slots__` 之外的封装影响、也不尊重"逻辑所有权"，拿到的是物理引用；`gc.get_referrers` 是反向接口但开销更大且结果含瞬时对象，生产上更常用"正向枚举 + 自查 referents"的组合。

```python
# file: code/01_语言核心与底层/q5021_leak_referrers.py
import gc, tracemalloc

class Node:
    def __init__(self, name):
        self.name = name
        self.peer = None            # 互相引用成环
        self.payload = "x" * 4096   # 让内存增长肉眼可见

LEAK_REGISTRY = []                  # 全局强引用:泄漏的根

def request(i):
    a = Node(f"node-{i}")
    b = Node(f"peer-{i}")
    a.peer, b.peer = b, a
    LEAK_REGISTRY.append(a)         # 业务只登记 a,却被 a.peer 把 b 拖住了

# --- 第一条链路:tracemalloc 看"哪里在涨" ---
tracemalloc.start()
snap1 = tracemalloc.take_snapshot()
for i in range(50):
    request(i)
snap2 = tracemalloc.take_snapshot()
diff = snap2.compare_to(snap1, "lineno")
print("内存增长 top1:", str(diff[0]).splitlines()[0])

# --- 第二条链路:gc 看"谁拽着它" ---
gc.collect()
peers = [o for o in gc.get_objects()
         if isinstance(o, Node) and o.name.startswith("peer-")]
print("不应存活的 peer 节点数:", len(peers))

def find_referrers(obj, want, limit=3):
    """谁的对象里直接引用了 obj(实例属性下钻一层 __dict__)"""
    found = []
    for cand in gc.get_objects():
        for ref in gc.get_referents(cand):
            if ref is obj:
                found.append(cand); break
            if isinstance(ref, dict) and any(v is obj for v in ref.values()):
                found.append(cand); break
        if len(found) >= limit:
            break
    return [o for o in found if isinstance(o, want)]

target = peers[0]
for r in find_referrers(target, want=Node):
    print(f"引用者: {type(r).__name__} {r.name!r} -> 它的名字以 node- 开头?",
          r.name.startswith("node-"))
print("结论: 环(a<->b)不是根,根是 LEAK_REGISTRY 这个全局强引用")
```

**追问**：1) 纯引用环为什么不需要人工断环？——环收集器按"可达性"回收，环内无外部引用即整体判死；要人工断环的场景是环上挂了带 `__del__`/外部资源的对象（Q1290）。2) `get_referents` 和 `get_referrers` 怎么选？——前者正向、可对单个对象精确查询，后者反向、要扫全堆且结果含垃圾瞬态；生产从"嫌疑对象"出发用前者。3) 为什么还要 tracemalloc？——它按分配点聚合，先告诉你"哪个函数在批量产出泄漏对象"，gc 链路再回答"它们被谁钉住"，两条链路一头一尾。

## 背诵要点
1. 环收集器能回收纯引用环；泄漏根=环外活引用（全局容器/模块缓存/traceback）。
2. `gc.get_referents(cand)` 查直接引用，实例属性要下钻 `__dict__` 一层。
3. tracemalloc 管"分配点"，gc 反查管"存活原因"，先前者定位后者归因。

## 复盘追问
1. 上了泄漏修复后，怎么在压测里证明"第 N 轮后 RSS 不再线性涨"？（提示：固定轮次/固定请求量的双快照对比 + RSS 增长斜率归零，参考 Q506/Q839）
2. `gc.get_objects()` 全堆枚举本身的开销怎么控制？（提示：只在诊断开关开启时执行，生产常驻服务用采样+限流，避免诊断动作压垮线上）
