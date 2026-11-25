---
title: "[Q5156] linecache 无界缓存与大 traceback 内存账"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5156 · linecache 无界缓存与大 traceback 内存账

难度：P6 ｜ 标签：linecache、traceback、内存账、容量规划

**问**：`linecache` 是给谁用的、它为什么没有淘汰机制？一个把百万行日志文件喂给 traceback 渲染的服务为什么内存翻倍？如何用 `checkcache`/`clearcache`/`lazycache` 控制这笔内存账？

**答**：
结论：`linecache` 是 traceback、`inspect.getsource`、doctest 等的底层行缓存：**整文件按行读进 `linecache.cache` 字典常驻进程**，无大小上限、无 TTL、无淘汰——设计假设是"被缓存的源码文件小且固定"，一旦用错对象（渲染错误上下文时读了日志文件/数据文件）就变成无界内存账。每个文件条目是 `(size, mtime, lines_list, fullname)`，`lines_list` 把整文件拆成带 `\n` 的行列表，内存约为文件大小 ×1.2–1.5（str 头开销）。事故链路：异常处理器里 `traceback.format_exception(..., file=custom)` 或 `inspect` 对动态生成的大文件反复取行 → `cache` 字典按文件路径累积 → RSS 与异常量同步上涨。

取舍：linecache 的价值在"同一文件重复取行"的摊销（traceback 渲染一帧只取 1-3 行，却不必每次打开文件）；对"每个文件只用一次"的场景，缓存只增加成本。控制手段：① 渲染完调 `linecache.checkcache()` 清理 mtime 已变条目（不是全清，省命中的那部分）；② 自管场景直接 `clearcache()`；③ 动态内容用 `lazycache` 挂 getter 惰性填充；④ 最好的办法是别让它碰大文件——异常上下文自己截取前后 N 行传给渲染器。

实战：全局异常中间件里把 traceback 渲染封装为"取文件路径 + 行号 → 手动读 ±5 行"，跳过 linecache；需要保留 linecache 时在 finally 里 `checkcache()`；监控上加一条 `len(linecache.cache) × 均值文件大小` 的内存账指标，跟 RSS 曲线对照。

```python
import linecache, os, sys, tempfile, tracemalloc

# 1) 构造一个"大文件"（模拟日志），并走 linecache 渲染异常上下文
d = tempfile.mkdtemp()
big = os.path.join(d, "big.log")
with open(big, "w") as f:
    for i in range(200_000):
        f.write(f"2026-11-21 line {i} some log payload padding text\n")

tracemalloc.start()
lines = linecache.getlines(big)            # 整文件进 cache，常驻
cur, peak = tracemalloc.get_traced_memory()
print("cached lines:", len(lines), " traced MB: %.1f" % (peak / 1e6))
entry = linecache.cache[big]
print("entry tuple: (size=%d, mtime, lines, fullname)" % entry[0])

# 2) 单行访问同样触发整文件缓存 —— 只取 1 行也吃下整文件内存
linecache.clearcache()
one = linecache.getline(big, 150_000)
print("got one line:", one.strip())

# 3) checkcache：只清 mtime 失效条目（文件被改写后）
os.utime(big, (0, 0))
linecache.checkcache()
print("after checkcache:", big in linecache.cache)   # False
linecache.clearcache()

# 4) lazycache：挂惰性 getter，不立刻读内容
linecache.clearcache()
class _SourceLoader:                          # linecache 要求 loader 提供 get_source
    def get_source(self, name):
        with open(name) as f:
            return f.read()

linecache.lazycache(big, module_globals={"__name__": "big", "__loader__": _SourceLoader()})
# 3.12+ 惰性条目是 1 元组 (get_lines,)，内容直到 getlines 才填充
entry = linecache.cache.get(big)
print("lazycache staged:", entry is not None and len(entry) == 1)
print("lines only after read:", linecache.getlines(big)[0].strip(),
      "len(entry) now:", len(linecache.cache[big]))
linecache.clearcache()

# 5) 替代方案：自己截取上下文，不进 linecache
with open(big, "rb") as f:
    f.seek(0, 2); size = f.tell()
    f.seek(max(0, size - 500))
    tail = f.read().decode().splitlines()[-5:]
print("manual tail lines:", len(tail), "—— 无缓存驻留")
```

**追问一**：traceback 渲染为什么依赖 linecache 而不是现读？——异常帧需要"源码行 + 行号 + 函数名"组合，且同一帧可能在 `__repr__`/日志多次渲染；linecache 以文件为单位摊销 open+read+decode 成本，并把 `__pycache__` 下 pyc 反解源码（`lazycache` + loader）也统一在这里。这是为"源码文件"设计的缓存，不是通用文件缓存。

**追问二**：`checkcache` 判断失效的成本是什么、为什么它不能当淘汰策略用？——对每个缓存条目做一次 stat（mtime/size 比对），条目多时也是一笔 syscall 账；它只清"失效"不清"冷"，长期不变的大文件永远留着——所以它是正确性工具，不是内存治理工具。

## 背诵要点
- linecache 整文件常驻 `linecache.cache`、无上限无淘汰，设计对象是源码文件，喂日志/数据文件就是无界内存账。
- `getlines/getline` 一行也触发整文件缓存；`checkcache` 只清 mtime 失效条目，`clearcache` 全清，`lazycache` 惰性填充。
- 治理：异常渲染自己截 ±N 行，或渲染后 checkcache；监控 `len(cache)×文件大小` 对照 RSS。

## 复盘追问
- 服务 RSS 随异常量上涨，tracemalloc 显示增长点全在 traceback 渲染栈，如何证实是 linecache 并修复？（objgraph/快照看 cache 字典；修复为手动上下文截取，讨论保留调试信息的折衷）
- 若异常发生在 exec 动态生成的代码里，linecache 如何拿到源码？（lazycache + 伪造 module_globals/loader 提供虚拟文件，讨论其与 pdb 的配合）
