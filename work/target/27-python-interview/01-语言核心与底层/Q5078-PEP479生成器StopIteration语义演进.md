---
title: [Q5078] PEP 479：生成器 StopIteration 语义的版本演进
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5078 · PEP 479：生成器内 StopIteration 语义演进

> 难度:★★★☆ | 标签:版本演进, 生成器, PEP479

**问**：老代码里生成器函数体内部 `raise StopIteration` 来"结束迭代"，升级 Python 3.7+ 后直接变 RuntimeError，为什么？PEP 479 的动机、`from __future__ import generator_stop` 的迁移期角色、以及它对 async 生成器/`yield from` 链的影响是什么？

**答**：结论：PEP 479（3.5 引入可选、**3.7 起默认强制**）把"生成器体内 StopIteration 逃逸出帧"改为 RuntimeError。动机是 PEP 380 的 `yield from` 带来了一个致命歧义：`yield from sub` 靠**捕获 sub 的 StopIteration 来判断子迭代结束**，如果生成器体内某行代码（比如被调函数、`next()` 用尽迭代器）自己也抛 StopIteration，外层会把"内部异常"误当成"迭代完成"，静默吞错提前退出——这类 bug 的表象是"迭代莫名少了一截"。演进时间线：3.5 允许 `from __future__ import generator_stop` 提前切换语义（当时切换后 StopIteration 被**转成 RuntimeError**）；3.7 起行为成为语言默认且 future import 失效（无害但冗余）；3.8 起提示移除。影响面：a) 生成器/协程体内不得让 StopIteration 逃逸——需要提前结束要么 `return`（等价 StopIteration 且干净）、要么自己 catch；b) async 生成器同理，且 3.8+ 里 async 函数体 `await` 一个抛 StopIteration 的兼容对象同样危险（要转 StopAsyncIteration）；c) `next(it, default)` 带默认值是防御写法，`next(it)` 裸用在生成器体内是隐患；d) 迁移检查清单：grep 生成器体内的裸 `next(`、`raise StopIteration`、以及任何"靠异常传播控制流"的库调用。实战：把"提前结束"统一写 `return`；包装外部回调时显式 `except StopIteration: return` 或用 `contextlib.suppress` 并注释原因。

```python
# file: code/01_语言核心与底层/q5078_pep479.py
import sys

# 1) 事故复现: 生成器体内 StopIteration 逃逸 -> RuntimeError (3.7+ 默认)
def bad_gen():
    yield 1
    raise StopIteration            # PEP 479 前会"正常结束", 现在炸

g = bad_gen()
print("第一个 yield:", next(g))
try:
    next(g)
except RuntimeError as e:
    print("PEP 479 下变为 RuntimeError:", e)

# 2) 为什么: yield from 靠 StopIteration 判定子迭代结束, 存在吞错歧义
def sub():
    yield "s1"
    return                          # 子迭代结束 -> StopIteration 被 yield from 捕获

def outer():
    r = yield from sub()            # 内部若误抛 StopIteration 会被误判为正常结束
    yield ("got", r)

print(list(outer()))

# 3) 正确写法: 提前结束用 return
def good_gen(items):
    for it in items:
        if it == "stop":
            return                  # 等价干净的结束, 不是裸 next
        yield it
print(list(good_gen(["a", "stop", "b"])))

# 4) 防御写法: 生成器体内调用 next 必须带 default
def safe_gen(it):
    v = next(it, None)              # 裸 next(it) 抛 StopIteration 会炸成 RuntimeError
    yield v
print(list(safe_gen(iter([]))))

# 5) async 生成器同样受约束; StopAsyncIteration 才是异步迭代结束信号
async def agen():
    yield 1
    return                          # 不能 raise StopIteration/StopAsyncIteration
print("async 生成器 3.7+ 同规则; python:", sys.version.split()[0])
```

**追问**：1) `return` 在生成器里到底做了什么？——字节码上等价于抛 `StopIteration(value)`，但发生在**生成器帧自身**而非体内代码，`yield from`/for 循环按协议处理它，语义无歧义；这也是为什么 `return value` 在生成器里值只能通过 `StopIteration.value` / `yield from` 的返回值拿到。2) 为什么 3.5-3.6 要 future import 过渡而不是直接改？——PEP 479 是行为破坏：依赖"体内 StopIteration=结束"的老代码（常见于手写解析器）会从静默错误变为报错，future import 让团队提前一个版本暴露所有违规点，配合测试逐个改 return；3.7 强制后 future import 变 no-op。3) 生成器抛出的异常链怎么看？——RuntimeError 会带 `__cause__` 指向原始 StopIteration（3.9+ traceback 显示 caused by），排查时先看 cause 里的原始抛出点。

## 背诵要点
- PEP 479：3.5 可选、3.7 默认——生成器体内 StopIteration 逃逸一律 RuntimeError，根因是 yield from 靠它判定子迭代结束，体内逃逸会吞错。
- 提前结束统一写 `return`（= StopIteration.value 机制）；体内调 `next()` 必须带 default 防御。
- async 生成器同规则，结束信号是 StopAsyncIteration；迁移清单：裸 next、raise StopIteration、异常控制流调用。

## 复盘追问
- 你们有没有升级 3.6→3.7/3.8 后"迭代提前结束"变报错的模块？当时怎么定位的？（提示：RuntimeError 的 __cause__ 链指向原始 StopIteration 抛出点）
- 手写解析器/状态机代码里还有多少"异常当控制流"的写法？（提示：本卡清单 grep 一轮，把裸 next 换 next(it, default) 并补单测覆盖结束分支）
