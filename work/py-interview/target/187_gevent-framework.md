# 187. gevent 框架

> 分类：网络 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**gevent** / **greenlet** / **monkey patch** / **gunicorn** / **绿色线程** / **协程**
> 原文锚点：第 37~51 段「gevent 是基于绿色线程（greenlet）的高性能并发网络库，用 monkey patch 把内置阻塞库改非阻塞，常与 gunicorn 配合作为 WSGI 服务器，以 gevent.spawn 并发」

## 一句话总述
**gevent** 是基于 **greenlet（用户态绿色线程）** 的并发网络库：用 **`monkey.patch_all()` 把标准库阻塞调用（socket/threading 等）替换成非阻塞实现**，再由**事件循环（libev）**调度这些 greenlet，从而"看似同步写、实则并发跑"——常与 **gunicorn** 搭配作为 WSGI 服务器。

## 面试官视角
- **考察意图**：是否理解 greenlet 不是线程、monkey patch 改了什么、为何能和老同步代码共存。
- **P5** 能说出 gevent = greenlet + monkey patch / **P6** 能讲清 monkey patch 把 socket 换成非阻塞、事件循环调度 greenlet、spawn 创建协程 / **P7** 能说清 greenlet 是**用户态微线程（非 OS 线程）**，并点出 monkey patch 的副作用（全局改写标准库，可能与其他库冲突）。
- **红旗**：以为 gevent 用"多线程"并发（其实是单 OS 线程内的 greenlet 协作式调度）；或不知道 monkey patch 要**在 import 其他库之前**打。
- **惊艳点**：`monkey.patch_all()` 的实质是**把 `socket.socket` 换成 gevent 的非阻塞版本 + 自研事件循环**，和手写 `selectors` 是同一件事——gevent 只是把"改写 + 调度"封装好了 `[源码]`（gevent 文档 "Greenlet" / "Monkey patching" 章节）。

## 主问答
**Q（面试官原话）：** gevent 是怎么实现高并发的？monkey patch 有什么用？

**A · 标准答案骨架：**
1. **先给结论**：gevent 用 **greenlet（轻量用户态协程）** 而非 OS 线程做并发单位，单线程内可开成千上万个；再用 **monkey patch** 把标准库里阻塞的 socket/threading 换成非阻塞版本。
2. **再给机制**：`from gevent import monkey; monkey.patch_all()` **必须在 import 其他库之前**调用，它把 `socket`、`time.sleep` 等替换成 gevent 的非阻塞实现；之后用 `gevent.spawn(func)` 创建 greenlet，事件循环（底层 libev，C 实现）在 IO 阻塞点自动切换 greenlet——**写起来像同步，跑起来是并发**。
3. **最后给边界**：greenlet 是**协作式调度**（不在 IO 点主动让出就会卡住整个循环），且 monkey patch **全局改写标准库**，可能与依赖原生线程/信号的库冲突；CPU 密集任务它帮不上忙。

**加分层**：gevent 常与 **gunicorn + gevent worker** 部署成 WSGI 服务器，老同步代码几乎零改动就能获得并发 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | gevent 干嘛 | 基本认知 | greenlet + monkey patch | 换题 → 不及格 |
| L2 | monkey patch 作用 | 是否背的 | 改阻塞为标准非阻塞 | 判 P5 |
| L3 | greenlet 是什么 | 真理解 | 用户态协程非线程 | 判 P6 |
| L4 | 副作用 | 架构判断 | 全局改写/冲突风险 | 判 P6+ |
| L5 | gunicorn 部署 | 实战经验 | gevent worker 配置 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| gevent 长期稳定（依赖 greenlet + libev） | 无重大翻转 | greenlet 是 C 扩展；monkey.patch_all() 需最早执行；仍广泛用于兼容老同步代码 |

## 关键代码
```python
from gevent import monkey, spawn
monkey.patch_all()                       # 必须最先执行：改写 socket 等为非阻塞 [实测]
import requests
def fetch(i):
    r = requests.get("https://httpbin.org/get")   # 已被 patch 成非阻塞
    print(i, len(r.text))
spawn(fetch, 1); spawn(fetch, 2)        # 两个 greenlet 并发
```

## ⚠️ 原文纠错
原文音译需还原：「**event / gvent / gone / joygevent**」→ **gevent**；「**monueph / monkeyph**」→ **monkey patch**；「**sport方法**」→ **spawn 方法（gevent.spawn）**；「**绿色线程**」正确（即 greenlet）；「**矩阵口**」→ **gunicorn**；「**HTTP并掉ORG**」→ **httpbin.org**；「**soofener**」→ **socket**；「**pythrm**」→ **Python**；「**joygevent**」→ **用 gevent**；「**RO多路复用**」→ **IO 多路复用**。事实修正：原文称 gevent"底层是 C 语言实现"——准确说是 **greenlet（C 扩展）+ libev（C 事件循环）** 的组合，greenlet 是**用户态微线程**而非 OS 线程。概念正确：monkey patch 改标准库阻塞调用、gevent.spawn 并发、常与 gunicorn 配合、底层基于 IO 多路复用。核对范围：第 37~51 段 gevent。

## 总结与追问预判
- gevent = greenlet + monkey patch + libev 事件循环；单线程内协作式并发，老代码零改。
- 顺势会问：**Tornado（见 186 卡）**、**asyncio（见 188 卡）**、**monkey patch 与 IO 多路复用关系（见 185 卡）**。
