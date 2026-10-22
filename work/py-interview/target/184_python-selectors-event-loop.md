# 184. Python selectors 模块与事件循环

> 分类：网络 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**selectors** / **DefaultSelector** / **register** / **EVENT_READ** / **事件循环** / **回调**
> 原文锚点：第 37~66 段「Python3 的 selectors 模块提供 DefaultSelector 按平台选 IO 模型；register/unregister/modify/select；官方示例用事件循环 + 回调实现异步 TCP 回显服务器」

## 一句话总述
Python 标准库 **`selectors`** 是对 `select`/`poll`/`epoll` 的**高级跨平台封装**：`DefaultSelector` 按 OS 自动选底层实现（**Linux→epoll、macOS→kqueue**），用 **`register` 注册 fd + 事件类型（`EVENT_READ`/`EVENT_WRITE`）+ 回调**，**`select()` 阻塞到就绪后回调解派**——这就是"事件循环 + 回调"模型，回调地狱后来被**协程（asyncio）**解决。

## 面试官视角
- **考察意图**：是否真的用过高阶封装写过多路复用，理解"事件循环 + 回调"与"协程"的演进关系。
- **P5** 能说出 DefaultSelector 自动选型、register/select 怎么用 / **P6** 能讲清 register(fd, events, data) 把回调绑在 data 上、select 返回就绪 (key, events) 后按事件类型分发 / **P7** 能对比"回调模型"与"协程模型"，说清回调地狱的痛点与 asyncio 的解法。
- **红旗**：以为 selectors 和 select 是同一个模块；或认为 `select()` 返回的是"数据"（实际返回就绪的 (key, events) 对，数据要自己 recv）。
- **惊艳点**：`modify()` 本质就是 **先 `unregister` 再 `register`** 的语法糖；Linux 下 `DefaultSelector` 实际就是 `EpollSelector`——一行 `type(sel)` 即可验证 `[源码]`（Python 标准库 `selectors` 模块）。

## 主问答
**Q（面试官原话）：** Python 里的 selectors 模块怎么用？它和我们说的事件循环是什么关系？

**A · 标准答案骨架：**
1. **先给结论**：`selectors` 把平台相关的 select/poll/epoll **统一成一套 API**，`DefaultSelector` 在 Linux 自动用 **epoll**、macOS 用 **kqueue**；核心套路是"**注册 fd + 事件 + 回调，循环 select 分发**"。
2. **再给机制**：`register(fd, EVENT_READ|EVENT_WRITE, data=回调)` 把回调挂在 key 上；`select(timeout)` **阻塞到任一 fd 就绪**，返回 `[(key, events), ...]`；循环里按 `events` 判断可读/可写，**取出 key.data 执行对应回调**（accept 连接→注册读回调→读数据→发回）。这就是**事件循环 + 回调**。
3. **最后给边界**：回调层层嵌套形成**回调地狱**（异步编程缺陷）；Python 后来用**协程（asyncio，3.4 引入、3.5+ 用 async/await）**把"回调"改写成"看似同步的顺序代码"来解决——`selectors` 是理解 asyncio 事件循环底层的钥匙。

**加分层**：官方 `selectors` 文档示例就是一个**异步 TCP echo 服务器**（并发回显客户端数据），它全程**非阻塞**，`accept` 拿到的客户端 socket 会再 `register` 一个读回调——看清这层嵌套就懂了回调模型 `[源码]`（Python 标准库 `selectors` 模块文档示例）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | selectors 干嘛 | 基本认知 | 跨平台多路复用封装 | 换题 → 不及格 |
| L2 | DefaultSelector 选型 | 是否背的 | Linux→epoll/macOS→kqueue | 判 P5 |
| L3 | select 返回什么 | 真理解 | 就绪 (key,events) 非数据 | 判 P6 |
| L4 | 回调 vs 协程 | 架构判断 | 回调地狱与 asyncio | 判 P6+ |
| L5 | 手写 echo server | 实战经验 | register 嵌套回调 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.4 引入 selectors 模块至今 | 无 | select 模块 2/3 皆有；selectors 为 3.4+ 新增高级封装；asyncio 协程 3.5+ 用 async/await |

## 关键代码
```python
import selectors, socket
# DefaultSelector 在 Linux 自动选 epoll [实测, py3.13]
sel = selectors.DefaultSelector()
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("0.0.0.0", 8888)); srv.listen()
srv.setblocking(False)
def on_accept(key, mask):
    conn, _ = key.fileobj.accept()            # accept 回调
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, data=on_read)
sel.register(srv, selectors.EVENT_READ, data=on_accept)
while True:
    for key, mask in sel.select():            # 阻塞到就绪，返回 (key,events)
        key.data(key, mask)                   # 分发到注册的回调
```

## ⚠️ 原文纠错
原文音译需还原：「**inventread / inventright**」→ **EVENT_READ / EVENT_WRITE**；「**defaultlector**」→ **DefaultSelector**；「**reject / seject / onreject**」→ **register / unregister**；「**macself**」→ **accept**；「**携程**」→ **协程**；「**实践循环**」→ **事件循环**；「**回掉**」→ **回调**；「**业务编程**」→ **异步编程**。表述微调：原文"python二提供 select 模块、python三改进出 select 模块"混淆了二者——应说 **select 模块 2/3 皆有，selectors 是 Python 3.4 新增的高级封装**。核对范围：第 37~66 段 selectors 接口与官方 echo 示例。

## 总结与追问预判
- selectors = 跨平台多路复用封装；DefaultSelector 自动选型；register + select + 回调 = 事件循环；回调地狱由协程解决。
- 顺势会问：**select/poll/epoll 底层（见 183 卡）**、**协程与 asyncio（后续章）**。
