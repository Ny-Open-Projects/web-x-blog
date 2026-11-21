---
title: [Q5013] immortal objects 在 3.12+ 的实际表现与 refcount 观测
date: 2026-11-19
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5013 · immortal objects 与 refcount 观测

> 难度:★★★ | 标签:GC, immortal, PEP 683, 3.12+

**问**：PEP 683 不朽对象（immortal objects）解决什么问题？哪些对象是不朽的？3.12 前后怎么观测引用计数差异——为什么小整数 `sys.getrefcount(1)` 在 3.12+ 看起来「不真实」？

**答**：问题：True/False/None/小整数/内部单例被**每个**子解释器、每段代码反复引用，refcount 高频写导致：① 缓存行在多核间弹跳（多解释器扩展性瓶颈）；② 3.12 前的 fork+COW 场景里，父进程 refcount 字段被写 → 触发内存页复制，fork 优化失效。PEP 683 把这批对象标记为不朽：**refcount 字段写成极大值（IMMORTAL_REFCOUNT）后不再增减**，GC 直接跳过。哪些：None/True/False/NotImplemented/Ellipsis、-5~256 小整数、内部 intern 字符串、空的 tuple/frozenset 等。观测差异：3.11 里 `sys.getrefcount(1)` 返回真实（巨大且波动）计数；3.12+ 恒定返回一个固定大数（如 4294967295 量级），「看起来不真实」恰恰证明不朽机制生效——引用它**不再写计数**，这是 fork+COW 进程省内存的直接证据。

```python
# 基线:任何版本可跑；3.12+ 与 3.11 输出差异即本题考点
import sys

x = 1
before = sys.getrefcount(1)
ys = [1] * 10000                          # 大量新引用
after = sys.getrefcount(1)
print("3.11 口径: after-before ≈ 10000；3.12+ 口径: 差值 = 0（或恒定）")
print("refcount:", before, "->", after, "delta =", after - before)

# 不朽对象集合探测：3.13+ 提供 _Py 检查的稳定入口有限，
# 通用的观测口径：refcount 恒定且极大 + gc 不追踪
print("None tracked by gc:", __import__("gc").is_tracked(None))     # False
print("小整数 tracked:", __import__("gc").is_tracked(1))            # False

# fork+COW 收益（原理演示）：不朽对象页不再被写，父进程页不被复制
# 实测方法：fork 前后对比 /proc/self/smaps_rollup 的 Pss（Linux）；macOS 无 smaps，跳过实测
import platform
if platform.system() == "Linux":
    pss = [l for l in open("/proc/self/smaps_rollup") if l.startswith("Pss")]
    print(pss)
```

**追问**：1) 不朽对象怎么回收？——不回收：生命周期=解释器生命周期，销毁时才整体释放；这也意味着把大量对象手动 immortal（如 C 扩展调用 `Py_SET_REFCNT` 到 immortal 值）会泄漏。2) 与 3.12 `gc.freeze()` 什么关系？——互补：freeze 把**现有追踪对象**移出代际回收（fork 前调用防 COW 抖动），immortal 是**标记位**让对象天然免疫；freeze 可恢复，immortal 不可逆。3) 多解释器（subinterpreters）为什么依赖它？——共享单例若计数会被不同解释器写，no-GIL/多解释器下就是数据竞争；immortal 让它们真正只读共享。

## 背诵要点
1. PEP 683：单例/小整数/intern 串标记不朽，refcount 写成极大值不再增减，GC 跳过。
2. 观测口径：3.11 `getrefcount(1)` 波动 ≈ 引用数；3.12+ 恒定差值 0 —— 恒定即不朽生效。
3. 与 gc.freeze 互补：freeze 是 fork 前的一次性快照操作（可逆），immortal 是永久标记（不可逆）。

## 复盘追问
1. 为什么 fork+COW 场景下 refcount 写是杀手？（提示：任何写都会复制物理页，包括「无害」的计数自增）
2. 你的服务大量缓存 intern 字符串，3.12 后内存有什么变化？（提示：高频单例页不再复制，RSS 降低；但新增动态对象照常）
