---
title: "[Q5082] setrecursionlimit 调高引发 C 栈溢出的崩溃事故复盘"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5082 · setrecursionlimit 调高引发 C 栈溢出的崩溃事故复盘

难度：★★★★☆ ｜ 标签：递归 / C 栈 / 事故复盘 / 3.12 演进

**问**：生产上为了解析深层嵌套 JSON，有人直接 `sys.setrecursionlimit(10**6)`，随后进程段错误（segfault）直接死掉而不是抛 RecursionError。为什么调高限制会导致段错误？3.12 之后这个故事有什么变化？

**答**：
- **结论**：`sys.setrecursionlimit` 只改 CPython 的**Python 层递归计数上限**，不扩大线程的 **C 栈**。递归调用最终要走 C 解释器帧栈，限制超过 C 栈容量（主线程一般 8MB，可按 ulimit 查）后，栈底越界写直接段错误——进程没有机会抛异常、没有 traceback、监控只见 SIGSEGV。这是"改配置反而制造崩溃"的经典事故。
- **取舍**：3.11/3.12 做了缓解：3.11 起 Python-to-Python 调用不再逐层消耗 C 栈（帧挂在 data stack 上），3.12 加入 C 栈溢出检测，纯 Python 递归超深时**安全抛 RecursionError** 而不是崩溃；但递归穿过 C 层（`json.loads`、`repr`、`__del__` 链、C 扩展回调）时依然可能踩 C 栈。所以正确做法是：要么把深度需求交给迭代/显式栈改写，要么用独立线程调大 `threading.stack_size` 跑深递归。
- **实战**：复盘要点——1）崩溃无 traceback + SIGSEGV 先查最近是否动过 recursionlimit；2）3.12+ 上限测试应观测"安全 RecursionError 的实际深度"（受 C 栈与调用形态双重约束，并非等于 setrecursionlimit 的值）；3）`json.loads` 深嵌套在 3.12 的 C 解析器里有自己的安全网，但自研 C 扩展没有。

```python
"""3.12+：调高 recursionlimit 后纯 Python 递归会安全抛错而非段错误"""
import sys, threading

def deep(n):
    if n <= 0:
        return 0
    return 1 + deep(n - 1)

print("默认递归限制:", sys.getrecursionlimit())
try:
    deep(5000)
except RecursionError:
    print("默认限制下：RecursionError（符合预期）")

# 调高到 10^6：3.12+ 纯 Python 递归有 C 栈检测兜底，安全抛 RecursionError
sys.setrecursionlimit(1_000_000)
try:
    deep(500_000)
    print("竟然递归完成（说明 C 栈足够大，别在生产模仿）")
except RecursionError as e:
    print("3.12+ 安全兜底：RecursionError 出现在实际深度", sys.getrecursionlimit(), "以内")
finally:
    sys.setrecursionlimit(1000)  # 复位，防止污染后续逻辑

# 穿过 C 层的深递归（repr 链）在旧版本是段错误高危区，3.12 亦有检测：
class Node:
    def __init__(self):
        self.next = None

a = Node()
cur = a
# 只造 100 层做演示（造 10^6 层仍属危险操作，交给迭代实现）
for _ in range(100):
    cur.next = Node()
    cur = cur.next
print("浅层对象链 repr 正常:", len(repr(a)) > 0)
```

**追问链**
1. 如果一定要处理 50 万层深的嵌套结构，工程上怎么做？
   1. 三条路：迭代改写（显式栈/循环，JSON 场景换用流式或扁平 schema）；`threading.stack_size(64*1024*1024)` + 专用线程跑递归；3.12+ 也可评估 C 侧解析器的深度开关（如 `json` 的实现自带限制）。
   2. 追问：为什么调 `threading.stack_size` 比调 `ulimit -s` 更可控？——它是进程内显式声明，只影响新建线程，不用动系统限制，也不影响主线程/第三方库的栈假设。
2. 3.11 的帧结构变化（帧外置到 data stack）和 3.12 的 C 栈检测分别解决什么？
   1. 前者让纯 Python 递归的内存成本从"每层一个 C 栈帧"降为"每层一个堆上帧对象"，后者在真要爆 C 栈前主动抛 RecursionError，把段错误变成可捕获异常。

## 背诵要点
- setrecursionlimit 只改 Python 层计数，不扩 C 栈；超 C 栈 = SIGSEGV，无 traceback。
- 3.11 帧外置 + 3.12 C 栈检测：纯 Python 深递归改为安全抛 RecursionError；穿过 C 层仍高危。
- 正解：迭代改写 / threading.stack_size 专用线程 / 显式深度预算。

## 复盘追问
- 深层嵌套 JSON 打击面如何提前预警？压测时用什么手段注入深度样本？
- faulthandler 在 SIGSEGV 场景能留下什么线索？为什么仍建议生产开启？
