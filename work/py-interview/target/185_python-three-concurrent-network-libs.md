# 185. Python 三大并发网络库总览

> 分类：网络 | 难度：L2 | 题型：对比题 | 频率：中 | 关键词：**Tornado** / **gevent** / **asyncio** / **IO多路复用** / **协程** / **monkey patch**
> 原文锚点：第 1~19 段「常见的 Python 并发网络库有三个：Tornado、gevent、asyncio；它们底层都基于 IO 多路复用；Python2 无原生并发库，Go 内置 goroutine」

## 一句话总述
Python 生态三大并发网络库 **Tornado（FriendFeed 开源的 Web 微框架）**、**gevent（greenlet 绿色线程 + monkey patch）**、**asyncio（Python3 内置、协程 + 事件循环）**，**底层全部建立在 IO 多路复用之上**；差异在"回调 / 绿色线程 / 原生协程"三种并发范式，以及是否依赖 monkey patch 改写标准库。

## 面试官视角
- **考察意图**：是否真正用过至少一种，并理解它们"殊途同归——都绕不开 IO 多路复用"。
- **P5** 能说出三者名字与一句话定位 / **P6** 能讲清三者并发范式差异（回调 vs greenlet vs 原生协程）及 monkey patch 是什么 / **P7** 能对比选型（微服务轻量用 Tornado，打补丁兼容老代码用 gevent，新项目用 asyncio/aiohttp），并指出它们共同的 IO 多路复用底座。
- **红旗**：把三者当成完全不同的技术（其实底层都是 epoll/kqueue）；或认为 gevent 用"线程"并发（是 greenlet 用户态调度，不是 OS 线程）。
- **惊艳点**：三者都**不创造新 IO 能力**——`monkey.patch_all()` 把 `socket` 换成非阻塞 + 自研事件循环，本质和手写 `selectors` 是同一件事，只是封装层级不同 `[经验]`。

## 主问答
**Q（面试官原话）：** 你用过哪些 Python 并发网络库？它们的底层实现有什么共性？

**A · 标准答案骨架：**
1. **先给结论**：常用三个——**Tornado**（Web 微框架，回调/协程）、**gevent**（greenlet 绿色线程 + monkey patch）、**asyncio**（Python3 内置，原生协程 + 事件循环）；**共同底座都是 IO 多路复用（epoll/kqueue）**。
2. **再给机制**：Tornado 靠自身 IOLoop 与非阻塞 socket + 协程；gevent 用 **greenlet** 做用户态微线程，并用 **monkey patch** 把标准库阻塞调用改写成非阻塞；asyncio 用 **`async/await` 协程 + 事件循环**，底层仍走 select/epoll。
3. **最后给边界**：Python2 时代**没有原生并发库**（需靠 Tornado/gevent 这类第三方）；对比之下 Go 语言**内置 goroutine** 原生支持——这是语言层级的设计差异，不是库能补的。

**加分层**：选型上——老项目兼容用 gevent（patch 一下即可），Web 微服务用 Tornado，新项目优先 asyncio/aiohttp（标准库、无需第三方补丁）`[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 三个库名字 | 基本认知 | Tornado/gevent/asyncio | 换题 → 不及格 |
| L2 | 底层共性 | 是否背的 | 都基于 IO 多路复用 | 判 P5 |
| L3 | monkey patch | 真理解 | 改标准库阻塞为非阻塞 | 判 P6 |
| L4 | 三者选型 | 架构判断 | 老项目/微服务/新项目 | 判 P6+ |
| L5 | 手写过框架 | 实战经验 | 基于 selectors 自研 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 2.x（无原生并发库） | Python 3.4 引入 asyncio（Guido 主导的 Tulip 项目） | Python2 需第三方；Python3.4+ 有标准库 asyncio，3.5+ 用 async/await |

## 关键代码
```python
# 三者底层都归到"事件循环 + 非阻塞 socket" [实测]
import selectors
sel = selectors.DefaultSelector()   # Tornado IOLoop / gevent hub / asyncio loop 底层同理
# gevent 的 monkey patch 把 socket 换成非阻塞版：
# from gevent import monkey; monkey.patch_all()   # 改写标准库阻塞调用
```

## ⚠️ 原文纠错
原文多处音译需还原：「**torto一 / tomato / tonight / tennel / tonito / tanto**」→ **Tornado**；「**event / gvent / gone / joygevent**」→ **gevent**；「**asiRO / sro / s三l / l三l / CCIO / siglRO / ARYCTP / AROHTDP / LORGGDP / LOHTTPP / LOIGGDP / sinkIO**」→ **asyncio / aiohttp**；「**fritfeed**」→ **FriendFeed**；「**monountainpech / monkeyph / monueph**」→ **monkey patch（猴子补丁）**；「**grouppen**」→ **goroutine**；「**左侧/非左侧 socket**」→ **阻塞/非阻塞 socket**；「**pythrm**」→ **Python**；「**flash跟jung网站**」→ **Flask 跟 Django**；「**矩阵口**」→ **gunicorn**；「**yshark**」→ **Wireshark**；「**car**」→ **curl**；「**HTTP派**」→ **HTTPie**；「**HTTPB / HTTP并掉ORG**」→ **httpbin.org**；「**四个八端口**」→ **8888 端口**；「**RO多路复用 / wero多路复用 / l多的费用**」→ **IO 多路复用**；「**消费者编程**」→ **异步编程**。**Web 框架** 在原文中被音译为「外部」字头的框架表述（外→Web 音译），统一还原为 **Web 框架**。概念正确：三者底层均基于 IO 多路复用；Python2 无原生并发库、Go 内置 goroutine。核对范围：第 1~19 段 三大库总览。

## 总结与追问预判
- Tornado/gevent/asyncio 三范式不同，底座都是 IO 多路复用；差异在并发模型与是否 monkey patch。
- 顺势会问：**Tornado 细节（见 186 卡）**、**gevent（见 187 卡）**、**asyncio（见 188 卡）**、**IO 多路复用底层（见 182/483 卡）**。
