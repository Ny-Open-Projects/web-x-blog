# 42. 基于生成器的协程：send / throw / 预激

> 分类：并发/协程 | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**send** / **预激** / **StopIteration**
> 原文锚点：第 11~34 段「PEP 342 对生成器做了增强…还可以向它发送数据，或者使用 throw 抛出异常」

## 一句话总述
PEP 342 给生成器加上 `send()` / `throw()` / `close()`，让 yield 从"单向产出"变成**双向通道**——这就是 Python 2 时代的**基于生成器的协程**，且必须**先预激**才能 send。

## 面试官视角
- **考察意图**：能否分清"生成器"与"生成器协程"这两个常被混用的概念。
- **P5** 知道 yield 能产出 / **P6** 能写出 send 双向传值 / **P7** 能说清预激、StopIteration 终结与 throw 的用途。
- **红旗**：① 直接给未启动的协程 send 非 None 值（会报 can't send non-None value）；② 说"协程就是生成器"；③ 不知道协程结束会抛 StopIteration。
- **惊艳点**：`yield` 写在**等号右边**时，`send` 进去的值会成为**该 yield 表达式的值**——这就是双向的关键。验证：运行下方示例 `[实测]`

## 主问答
**Q：什么是基于生成器的协程？它和普通生成器有什么不同？**
**A：**
1. **先给结论**：普通生成器只**产出**；生成器协程的 yield 还能**接收**调用方 send 进来的值，形成双向数据流。
2. **再给机制**：`c.send(v)` 把 v 送到**当前挂起的 yield 表达式**处，继续执行到下一个 yield；协程结束时抛 `StopIteration`。开始前必须先 `next(c)` 或 `c.send(None)` **预激**到第一个 yield。
3. **最后给边界**：`throw(exc)` 可在挂起点**注入异常**，`close()` 触发 `GeneratorExit` 终止；这套机制已被 3.5 的原生协程取代，**新代码不要用**。
**加分层**：它是历史的中间形态——理解它有助于读懂老代码（早期 asyncio、tornado），但生产代码一律用 `async/await`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 协程和生成器是一回事吗 | 术语 | 不是，多一条 send 通道 | 换题 → 不及格 |
| L2 | send 的值去了哪里 | 机制 | 成为 yield 表达式的值 | 判 P5 |
| L3 | 为什么必须先 next | 边界 | 未预激无法接收非 None | 判 P6 |
| L4 | 结束时会发生什么 | 反例 | 抛 StopIteration | 判 P6+ |
| L5 | 新代码还用这套吗 | 判断 | 不用，用 async/await | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 2.5（PEP 342）起 | Python 3.5（PEP 492）引入原生协程后本形态成为历史 | 只作"读懂老代码"讲，新代码用 async/await |

## 关键代码
```python
def coro():
    hello = yield "hello"        # yield 在等号右边：接收 send 进来的值
    yield hello
c = coro()
print(next(c))                   # hello  ← 预激，必须先做
print(c.send("world"))           # world
try:
    next(c)
except StopIteration:
    print("协程结束")
# c2 = coro(); c2.send("x")
# TypeError: can't send non-None value to a just-started generator
```

## ⚠️ 原文纠错
原文把协程、send、StopIteration 写成音译形式，已还原为标准术语；原文中 "PEP 342" 的编号被读成混乱数字，已校正为 **PEP 342**。原文"在 yield 处暂停执行"的表述正确。

## 总结与追问预判
- 生成器协程 = yield 双向 + 预激 + StopIteration 收尾；已是历史形态。
- 下一题：见 43（@coroutine 装饰器）、44（原生协程三者区分）。
