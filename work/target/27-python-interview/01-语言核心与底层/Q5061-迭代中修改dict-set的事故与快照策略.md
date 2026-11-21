---
title: [Q5061] 迭代中修改 dict/set 的事故与快照策略
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5061 · 迭代中修改 dict/set 的事故与快照策略

> 难度:★★★★ | 标签:事故复盘, 迭代器, dict, RuntimeEerror, 防御式编程

**问**：线上服务周期性报 `RuntimeError: dictionary changed size during iteration`，只在流量高峰出现。为什么"迭代时删 key"会炸？为什么有时不炸？过滤场景该用哪三种安全写法，各自成本是什么？

**答**：结论：dict/set 迭代器不拷贝数据，只在每次 `next` 时检查版本号（`ma_version`/`ob_ref` 变化，3.12 前是 size 检查），检测到结构性变更（增删 key，改值不算）就抛 `RuntimeError`。**为什么高峰才炸**：低速流量下"迭代+删除"往往在循环体内立刻 break，或恰好没触发下一次 `next`（删的是最后一个元素后面没有再迭代），属于"没炸是运气不是正确"——这正是事故复盘里最危险的静默 bug。三种安全写法：a) **快照**：`for k in list(d)`——O(n) 内存拷贝 key 列表，字典小时最简单；b) **构造新容器**：`d = {k: v for k, v in d.items() if keep(v)}`——原子替换引用，无迭代变异，最推荐，但并发下要配合整体替换（不可变引用思维）；c) **收集后删除**：先迭代收集 `to_del`，再循环 `pop`——两趟 O(n)，适合大字典省快照内存。实战取舍：单线程小 dict 用快照；热路径大 dict 用构造替换；多线程/协程共享 dict 根本不该在迭代时变异，先上锁或换队列化变更。set 语义完全相同（版本号检查）。注意 `d.pop(k)` 在**迭代器外**才安全，`dict.popitem` 也改变 size。

```python
# file: code/01_语言核心与底层/q5061_dict_mutation.py
d = {i: i * 2 for i in range(1000)}

# 1) 危险写法: 迭代中删除 -> RuntimeError
try:
    for k in d:
        if k % 2 == 0:
            del d[k]
except RuntimeError as e:
    print("危险写法炸了:", e)

# 2) 快照写法: list(d) 拷贝 key, O(n) 额外内存
d2 = {i: i * 2 for i in range(1000)}
for k in list(d2):
    if k % 2 == 0:
        del d2[k]
print("快照法剩余:", len(d2))

# 3) 构造替换: 无迭代变异, 原子引用替换, 最推荐
d3 = {i: i * 2 for i in range(1000)}
d3 = {k: v for k, v in d3.items() if k % 2 != 0}
print("替换法剩余:", len(d3))

# 4) 两趟收集删除: 大字典省快照内存
d4 = {i: i * 2 for i in range(1000)}
to_del = [k for k, v in d4.items() if k % 2 == 0]  # items() 迭代时只读, 安全
for k in to_del:
    d4.pop(k, None)
print("两趟法剩余:", len(d4))

# 5) 改值不炸(非结构性变更), 演示一致性
d5 = {1: "a", 2: "b"}
for k in d5:
    d5[k] = "x"
print("只改值不炸:", d5)
```

**追问**：1) 为什么改 value 不炸、删 key 炸？——迭代器状态是"当前桶位置"，改 value 不动桶布局；增删 key 触发 rehash/桶数组变化，位置状态失效，版本号检测到就抛错。2) 并发两个线程一个迭代一个删除怎么办？——版本号检查只能给你"炸得明确"，不给你正确性：要正确性先加锁，或者用"构造替换 + 原子引用赋值"（CPython 的 GIL 保证单条字节码引用替换原子，但复合操作仍需锁）；不能依赖 GIL 当同步原语。3) list 迭代中 append 会不会炸？——不炸但语义陷阱：list 迭代器用递增索引，append 会"边迭代边吃到新元素"（经典 BFS 手法），插入已过位置则静默跳过——这也是不炸≠正确的另一个例子。

## 背诵要点
- dict/set 迭代器做版本号检查：增删 key（结构性变更）抛 `RuntimeError: dictionary changed size during iteration`，改 value 不炸。
- 三种安全写法：`list(d)` 快照（省事费内存）、构造新 dict 原子替换（最推荐）、两趟收集后 pop（大容器）。
- 不炸 ≠ 正确：list 迭代中 append 吃新元素、del 静默跳过；并发共享容器先加锁或队列化变更，不把 GIL 当锁。

## 复盘追问
- 你们代码里 `for ... in dict` 循环体内有没有增删 key？高峰偶发 RuntimeError 的根因链路能不能定位到具体提交？（提示：grep 循环体里的 del/pop/add，对照三种安全写法改造）
- 团队有没有静态检查或 code review 清单拦住"迭代中变异"？（提示：flake8 插件/AST 扫描循环体内容器方法调用；把本卡三种写法进 code style）
