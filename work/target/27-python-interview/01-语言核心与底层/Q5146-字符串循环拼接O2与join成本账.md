---
title: "[Q5146] 字符串循环拼接的 O(n²) 与 join 成本账"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5146 · 字符串循环拼接的 O(n²) 与 join 成本账

难度：P6 ｜ 标签：str、性能、容量规划、CPython 优化边界

**问**：导出服务把 10 万行记录拼成大字符串，`s += row` 写法在小数据没出事，数据涨到 10 万行后接口从 80ms 变 30s。为什么 `+=` 会退化成平方复杂度？CPython 的 in-place 优化边界在哪？`join` 为什么是 O(n)？

**答**：
结论：str 不可变，`s += t` 的语义是创建新串，理论成本 O(len(s)+len(t))，累计就是 O(n²)。CPython 对**唯一引用**的 str 做了 in-place realloc 优化（`unicode_concatenate` 优化：若左侧引用计数为 1，直接原地扩容），很多场景让 `+=` 看起来是线性——但这个优化有三个洞：① 循环体里其他变量持有引用（如先 `log(s)`、append 到列表）立即失效；② 依赖解释器实现（PyPy/未来版本不保证）；③ 只对 `s = s + t` 形式的特定字节码形态生效，跨作用域/被装饰的循环不保证。`str.join` 是两遍算法：先算总长度一次分配，再逐段拷贝，稳定 O(n)。

取舍：join 需要"先收集到列表"的额外代码形态，行数少、单段大时 `+=` 与 join 差异不大；**N 大且段多时 join 是唯一可依赖的线性方案**。io.StringIO 在需要"流式追加 + 中途读"时可用，但纯拼接不如 join。

实战：容量账——10 万行 × 每行 100B，`+=` 退化时累计拷贝约 10^5 × 5×10^6 字节量级（期望 O(n²/2)）；join 只做一次分配 ≈ 10MB。规范：多段字符串聚合一律 `"".join(parts)` 或 `parts.append` + join，`+=` 出现在循环里视为 code smell（可用 ruff/自定义规则拦）。

```python
import timeit

def concat_loop(rows):
    s = ""
    for r in rows:
        s += r          # CPython 有 in-place 优化，但优化条件脆弱
    return s

def concat_oops(rows):
    s = ""
    out = []
    for r in rows:
        s += r
        out.append(len(s))   # 持有引用不影响，但任何 escape（log/print）会让优化失效
    return s, len(out)

def join_path(rows):
    return "".join(rows)

n = 5000
rows = ["x" * 200] * n

t1 = timeit.timeit(lambda: concat_loop(rows), number=3)
t2 = timeit.timeit(lambda: join_path(rows), number=3)
print(f"n={n}: += {t1*1000:.2f}ms  join {t2*1000:.2f}ms")

# 增长曲线验证平方性：n 翻倍，+= 耗时约 4 倍（join 约 2 倍）
rows2 = ["x" * 200] * (n * 2)
t1b = timeit.timeit(lambda: concat_loop(rows2), number=3)
t2b = timeit.timeit(lambda: join_path(rows2), number=3)
print(f"n={2*n}: += {t1b*1000:.2f}ms  join {t2b*1000:.2f}ms")
print(f"ratio += {t1b/t1:.1f}x  ratio join {t2b/t2:.1f}x")

# 大文件聚合的等价姿势：写文件场景用 writelines，同样避免聚合大串
import io
buf = io.StringIO()
buf.writelines(rows)
print("writelines size:", len(buf.getvalue()))
```

**追问一**：为什么 CPython 不把 `+=` 优化成保证线性？——str 不可变是语言契约，任何"其他引用存在"的场景都无法原地扩容；解释器只能做保守的引用计数窥探优化，公开语义必须保持每次拼接新对象的可能性（`id(s)` 可变与否不可依赖）。

**追问二**：`bytes` 拼接也一样吗？——语义相同但 bytes 常走 `bytearray` 或 `b"".join`；网络收包场景 `bytearray += chunk` 是真原地扩容（可变对象），和 str 的"伪原地"本质不同。

**追问三**：如何快速定位线上是这类退化？——profile 显示热点在 str concat 字节码、内存分配器高频 realloc、CPU 时间随输入大小平方增长；用 ruff 的 PERF401/402 或 grep 循环内 `+=` 做静态排查。

## 背诵要点
- str 不可变，`+=` 理论 O(n²)；CPython 的 in-place 优化依赖引用计数为 1，可被 escape 破坏且不可依赖。
- `join` 先求总长一次分配再拷贝，稳定 O(n)；循环拼接一律 parts.append + join。
- bytes 收包场景用 `bytearray`（真原地）或 `b"".join`；大文件用 writelines 流式写。

## 复盘追问
- 导出服务改 join 后 CPU 降了但内存峰值涨了，怎么权衡？（join 一次分配≈总大小；对比 += 平方次 realloc 的分配器碎片，讨论峰值内存账与分块生成器方案）
- 如何在 code review 里制度化拦截这类模式？（ruff PERF 规则 + 关键服务压测基线对比，讨论误报处理）
