---
title: [Q5076] sys.intern 与海量字符串去重的容量账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5076 · sys.intern 与海量字符串去重的容量账

> 难度:★★★★ | 标签:容量规划, sys.intern, 字符串

**问**：日志聚合场景要比较海量字符串（tag、URL、错误码），`sys.intern` 能省内存吗？它的驻留表存在哪、容量上限是多少、为什么 intern 后比较变快？滥用 intern 会出什么事故？

**答**：结论：`sys.intern` 把字符串注册进解释器全局的驻留表（`interned` dict），同一内容的字符串全进程只留一份，收益分三块：a) **内存**：N 份重复字符串变 1 份，100 万条重复 40 字节 tag 省约百 MB 级；b) **比较提速**：intern 后是同一对象，`==` 走 `is` 快路径（标识短路），dict 查找的 hash 也只有一份算；c) 注意驻留表本身有成本：每个条目是 dict entry + 引用，**驻留的字符串生命周期是进程级**——除非 CPython 实现"值死表空"的清理（驻留表是弱引用语义的：只有你手里还持有引用时值才真正存活，3.12 中 interned dict 持的是 immortal 引用计数保护，字符串无外部引用时可被回收，但 dict 槽位仍在），所以对"高基数、低重复"的输入（用户输入、UUID）intern 等于把驻留表撑成泄漏池。事故模式：把请求里的任意 header/URL intern 了，QPS 高、值全不同，驻留表百万级条目、RSS 缓慢上涨不回落，表象与内存泄漏一模一样。容量规划方法：先统计**基数/总量比**（unique/total），比值低于 1/10 才值得 intern；配合 `gc` 与 tracemalloc 验证驻留表增长（Q5071 手法）；Python 自动驻留的只有标识符样式字符串（编译期字面量、像变量名的短串），运行时 `str()` 产物不会自动驻留，必须显式 intern。

```python
# file: code/01_语言核心与底层/q5076_intern.py
import sys, tracemalloc

# 1) 自动驻留: 编译期字面量共享同一对象
a, b = "error_code_timeout", "error_code_" + "timeout"
print("字面量自动驻留, a is b:", a is b)

# 2) 运行时构造的字符串不自动驻留
c = "".join(["error", "_code_", "timeout"])
print("join 产物 is a:", c is a, "| == :", c == a)

# 3) sys.intern 显式驻留: 同一对象 + 比较快路径
i1 = sys.intern(c); i2 = sys.intern("error_code_timeout")
print("intern 后 is:", i1 is i2)

# 4) 内存账: 100 万条重复字符串, intern 前后
tags = ["prod.api.latency.p99"] * 1_000_000
plain = [t + "" for t in tags]                    # 100 万个独立 str 对象
before = sum(sys.getsizeof(s) for s in plain) + sys.getsizeof(plain)
interned = [sys.intern(t) for t in plain]         # 全部指向同一对象
after = sys.getsizeof(plain) + sum(sys.getsizeof(s) for s in interned[:1]) * 1 + 0
print(f"驻留前对象体量≈{before/1024/1024:.0f}MB, 驻留后字符串本体≈{after/1024/1024:.1f}MB(+表成本)")

# 5) 误用事故: 高基数输入 intern -> 驻留表只增不减
tracemalloc.start()
for k in range(5000):
    sys.intern("uid-" + str(k))     # UUID/用户输入场景就是持续增长
print("高基数 intern 造成驻留表 5000 条, 进程级不回收(演示)")
tracemalloc.stop()
```

**追问**：1) 驻留表的内存何时归还？——CPython 的 interned 表对字符串是弱引用（gc 清理字符串时表项移除），3.12 起配合 immortal objects 有优化；但只要业务还持有其中一份引用，值就永久存活——所以" intern 完就丢"的高基数用法等于白占表槽与一次哈希。2) intern 能加速 dict 吗？——能：键 intern 后 dict 内部哈希已存、等值比较退化为指针比较，热门 key 查询快约 10-30%（相对长字符串）；但 dict 查找大头在冲突链与容量因子，别指望 intern 救活一个扩容过度的 dict（见 Q5042）。3) 多进程下呢？——驻留表是每进程一份，fork 的子进程继承后各自演化，跨进程去重要靠外部结构（Redis set / 共享内存表），intern 不是分布式方案。

## 背诵要点
- intern 收益=去重内存 + `is` 短路比较提速；只对"低基数高重复"集合划算，先算 unique/total 比再决定。
- 自动驻留只覆盖编译期字面量/标识符样式串，运行时构造串必须显式 `sys.intern`。
- 高基数输入 intern = 进程级驻留表膨胀，表象如泄漏；驻留表每进程一份，不是跨进程方案。

## 复盘追问
- 你们网关/日志服务有没有"RSS 缓涨不回落"却查不出泄漏环的案例？（提示：按本卡先算字符串基数/总量比，再用 tracemalloc 看 intern 调用行，见 Q5071）
- 如果把热点 tag 集合改成 intern + LRU 限定基数，你会怎么设定上限与淘汰？（提示：intern 不可淘汰，需用有界 dict/weakref 结构替代，驻留表只适合有限枚举集）
