---
title: "[Q5229] next(iterator, default) 的契约：只吞 StopIteration"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5229 · next(iterator, default) 的契约：只吞 StopIteration，不吞业务异常

难度：P6 ｜ 标签：next、StopIteration、default 参数、迭代器耗尽、PEP 479、异常语义

**问**：`next(it, default)` 的 default 在什么情况下生效？迭代器抛出 ValueError 时会被 default 吞掉吗？耗尽后再取会怎样？为什么"拿 StopIteration 当业务信号"是反模式？它与 `iter(callable, sentinel)`（Q023）是什么关系？

**答**：
结论：`next(it, default)` 的契约是：调用 `it.__next__()`，**仅在它抛 StopIteration 时**返回 default——这个"耗尽即默认"是一次性的短路：迭代器一旦耗尽就是永久状态，之后每次 `next` 都返回同一个 default，不会再有任何数据。**业务异常（ValueError/KeyError/网络错误）原样穿透**，default 不会掩盖它们——这正是两参 next 与 `try/except StopIteration` 的等价处：它只把"正常结束"这个信号转译成值，不碰错误。反模式警示：在数据层用 `raise StopIteration` 表达"没有数据"会让上层 default 语义混淆"该停"与"该报错"；更隐蔽的是**生成器内部**的 StopIteration——PEP 479（Q5078）把它转成 RuntimeError，因为生成器函数体内 StopIteration 有特殊含义（结束自身），从回调里漏出来的 StopIteration 会被误认为"生成器正常结束"。两参 next 最稳的用途是"取首条或空兜底"：`first = next(rows, None)` 一行完成空表分支。

取舍：a) 判空取首条：`next(it, None)` + None 分支，比 try/except 或 `len()` 物化整个列表省；b) 需要区分"没有数据"与"数据错误"：**绝不在数据层抛 StopIteration**，定义专用异常（如 EmptyResult）或返回 None 显式表达；c) 消费方拿到 default 后要意识到迭代器已耗尽：想重试必须重建迭代器（生成器不可重放，Q1296 的一次性陷阱）；d) default 传 None 还是哨兵：调用方需要区分"空"与"值恰为 None"时用对象哨兵（Q1282），否则 None 足够；e) next 三参形式不存在——default 只能有一个，且第二参数必须显式给，漏给会让 StopIteration 直接抛出。

实战：事故形态是"分页拉取任务里用 `next(batch_iter)` 判断结束，某批次内部数据库超时被包装成 StopIteration 向外抛，上层循环把它当成'正常取完'提前退出，整夜任务静默漏跑一半数据；修复为数据层显式抛 QueryError，循环边界只用真正的耗尽信号"。下面演示契约、穿透行为与反模式。

```python
# next(iterator, default) 的契约: 只吞 StopIteration, 不吞业务异常
def gen_raise() -> "list[int]":
    yield 1
    raise ValueError("业务故障")


print("[1] default 只兜 StopIteration, 迭代器抛真异常时原样穿透")
it = iter([1])
print("    next(it) =", next(it))
print("    next(it, '默认值') =", next(it, "默认值"), " <- 耗尽后给 default")
print("    再取仍拿 default:", next(it, "默认值"), "(迭代器已永久耗尽)")

try:
    next(gen_raise(), "默认值")
except ValueError as exc:
    print("[2] 生成器内抛 ValueError:", exc, "| default 不会掩盖它")

print("[3] 经典坑: 默认值参数把'该停'和'出错'混成一路")
sentinel_rows = [["a", "b"], [], ["c"]]
def fetch(row: "list[str]") -> str:
    if not row:
        raise StopIteration("伪装耗尽的数据异常")   # 反例: 拿 StopIteration 当业务信号
for row in sentinel_rows:
    try:
        v = next(iter(row))
    except StopIteration:
        v = "<empty>"
    print(f"    row={row} -> {v}")
print("[4] 生成器内部 StopIteration 会被 PEP 479 转成 RuntimeError, 勿在生成器里 raise StopIteration")

print("[5] next 两参最稳的用途: 取首条或空兜底")
rows = iter([])
first = next(rows, None)
print("    空结果首条 =", first, "-> 空表/有表分支可以平滑写")
```

**追问一**：为什么 PEP 479 要把生成器内的 StopIteration 转成 RuntimeError？—— 3.7 之前，生成器体内任何 StopIteration（包括底层迭代器耗尽漏出来的）都会被解释器当作"生成器该结束了"，导致循环体悄悄提前终止——一个深层 bug 的现象是"结果无故变短"。PEP 479 把语义钉死：生成器的结束只能由"函数体自然返回"触发，体内冒出的 StopIteration 一律 RuntimeError 显式炸出来。这与两参 next 的契约呼应：StopIteration 是**迭代协议内部语言**，业务代码不得伪造或消费它。

**追问二**：`next(it, default)` 与 `iter(callable, sentinel)`（Q023）怎么配合？—— 两者是同一协议的两端：`iter(callable, sentinel)` 把"调用到返回哨兵为止"包装成迭代器（哨兵本身不产出），`next(it, default)` 把"耗尽"翻译成默认值。典型组合：`next(iter(partial.recv_chunk, b''), None)` 这类"读到 EOF 给默认"的写法。注意哨兵必须是**可比较相等且数据里不会出现的值**（如独立对象 object()），否则会把正常数据误判为结束——与 default 侧"区分空与 None"的哨兵思想（Q1282）是同一个镜像。

## 背诵要点
- next(it, default) 只在 __next__ 抛 StopIteration 时给 default；业务异常原样穿透；耗尽是永久态，重试需重建迭代器。
- 数据层禁止 raise StopIteration 当业务信号；生成器体内 StopIteration 被 PEP 479 转 RuntimeError。
- 两参 next 甜点位：取首条空兜底；与 iter(callable, sentinel) 配合做"读到 EOF 给默认"。

## 复盘追问
- 夜间任务静默漏跑一半数据，根因是？（数据层把超时包装成 StopIteration，上层循环误判耗尽；改显式异常类型）
- 耗尽后的迭代器再 next 会怎样？想重试怎么办？（永久返回 default；生成器不可重放，重建迭代器）
