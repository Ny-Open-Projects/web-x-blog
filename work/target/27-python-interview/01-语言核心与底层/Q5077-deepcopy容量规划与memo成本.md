---
title: [Q5077] deepcopy 的 memo 容量与拷贝策略容量规划
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5077 · deepcopy 的 memo 容量与拷贝策略容量规划

> 难度:★★★★ | 标签:容量规划, copy, 内存

**问**：配置中心要把一份 500MB 的对象树下发给 200 个 worker，每个 worker 拿到副本后局部修改。`deepcopy` 一次的成本结构是什么？memo（`_deepcopy_memo`）是干嘛的、什么情况会把拷贝变成 O(n²)？什么时候应该放弃 deepcopy 改共享/序列化/COW 方案？

**答**：结论：deepcopy 的成本 = **递归遍历 + memo 字典**双份账：每复制一个对象都往 memo 里登记"原对象 id → 副本"，作用有二——处理共享引用（两处指向同一 list 只拷一份，副本里仍共享）和**断环**（自引用结构不死循环）。容量账：a) memo 本身随节点数线性增长，拷完才释放，中途内存峰值 ≈ 原树 + 副树 + memo（每条目 dict entry 约 100B，千万节点 memo 单独吃 1GB+）；b) O(n²) 出现在**误解耦**：如果不小心传入的是"链表式互引用大对象"且每次拷贝都从根开始，或者循环里反复 deepcopy 同一棵树做小修改——每轮全树复制，正确做法是**只拷要改的子树**（copy.copy 浅层 + 局部 deepcopy）或用不可变结构重建；c) 大树的替代方案按成本排序：进程间直接共享用 `multiprocessing.shared_memory`（Q5509）或 fork COW（Q5053，注意 refcount 触碰会让 COW 页逐渐复制）；跨序列化边界的用 pickle 协议 5（out-of-band buffer 让大 buffer 不走 pickle 流，Q5009）；真正只读的场景给不可变对象 + 引用传递，零拷贝。取舍：deepcopy 的隐藏税还包括**自定义类默认走 `__reduce_ex__` 反射路径**，比 `__deepcopy__` 手写慢数倍；性能敏感类型应在类上实现 `__deepcopy__`。

```python
# file: code/01_语言核心与底层/q5077_deepcopy_memo.py
import copy, sys, time, tracemalloc

# 1) memo 的两个作用: 共享引用保持 + 断环
shared = [1, 2, 3]
tree = {"a": shared, "b": shared}
d = copy.deepcopy(tree)
print("副本仍共享同一子对象:", d["a"] is d["b"], "| 与原件断开:", d["a"] is not shared)

loop = []; loop.append(loop)          # 自引用环
d2 = copy.deepcopy(loop)
print("环被 memo 断开且保持自引用:", d2[0] is d2)

# 2) 深浅混合策略: 只拷要改的子树, 其余浅引用
big_leaf = {"rows": list(range(100_000))}
root = {"leaf": big_leaf, "meta": {"v": 1}}
root2 = copy.copy(root)               # 浅拷根
root2["meta"] = copy.deepcopy(root["meta"])   # 只深拷小枝
root2["meta"]["v"] = 2
print("改 meta 不动大 leaf:", root2["leaf"] is big_leaf, "| meta 隔离:", root2["meta"] is not root["meta"])

# 3) 成本对比: 全树 deepcopy vs 局部策略
tracemalloc.start()
t0 = time.perf_counter()
full = copy.deepcopy(root)
t_full = time.perf_counter() - t0
t1 = time.perf_counter()
partial = copy.copy(root); partial["meta"] = copy.deepcopy(root["meta"])
t_partial = time.perf_counter() - t1
print(f"全树 deepcopy: {t_full*1000:.1f}ms | 局部: {t_partial*1000:.3f}ms (大 leaf 未复制)")
tracemalloc.stop()

# 4) 反模式: 循环里反复 deepcopy 同一棵树 -> O(n * 全树)
t0 = time.perf_counter()
for _ in range(3):
    _ = copy.deepcopy(root)           # 事故模式: 每次修改都整树拷贝
print("循环整树拷贝 3 次耗时: %.0fms (次数涨=时间线性恶化, 应改局部拷贝)" % ((time.perf_counter()-t0)*1000))

# 5) 自定义 __deepcopy__ 控制成本
class Cost:
    def __deepcopy__(self, memo):
        return self                    # 不可变/共享安全: 免拷贝
c = Cost(); print("自定义免拷贝:", copy.deepcopy(c) is c)
print("python:", sys.version.split()[0])
```

**追问**：1) memo 为什么用 `id()` 做键？——对象可能不可哈希（list/dict 自身），id 是身份的稳定键；副作用是 memo 强引用所有原件与副本，拷贝完成前整树两份都不可回收，这决定了峰值内存估法：**峰值 ≈ 2×树 + memo**。2) `copy.copy` 与 deepcopy 对"不可变原子"怎么处理？——int/str/tuple(全不可变成员) 直接返回原对象（is 相同），所以浅拷贝嵌套 tuple 树几乎零成本，设计"不可变值对象"能从根上免掉拷贝账。3) fork COW 共享为什么后来还是复制了？——CPython 每次 refcount-- 都要写对象头，触碰过的页被复制；缓解是 3.12 immortal objects（Q5013）让常驻对象 refcount 不再写页，或 `gc.freeze()` 把长期对象移出可回收集（Q5053）。

## 背诵要点
- deepcopy 成本=递归+memo：memo 维持共享引用与断环，用 id() 做键，峰值内存 ≈ 2×树 + memo。
- O(n²) 事故模式=循环里反复整树 deepcopy；改为浅拷根 + 只 deepcopy 修改的子树，或不可变重建。
- 大对象按成本选：只读传引用/不可变、进程内共享 shared_memory、fork 用 gc.freeze + immortal、跨边界用 pickle 协议 5 out-of-band。

## 复盘追问
- 你们的配置热更新路径上是整树 deepcopy 还是局部拷贝？改一次配置的 P99 是多少？（提示：压测 deepcopy 全树耗时与峰值内存，把"只拷 delta"的收益量化进容量账）
- worker 多进程场景下，配置对象的 COW 页触碰率有没有监控过？（提示：用 smaps 的 Private_Dirty 增长观察，配合 gc.freeze，见 Q5053/Q6029）
