# 183. select、poll、epoll 的区别与时间复杂度

> 分类：网络 | 难度：L2 | 题型：对比题 | 频率：高 | 关键词：**select** / **poll** / **epoll** / **O(N)** / **O(1)** / **就绪通知**
> 原文锚点：第 31~36 段「select、poll、epoll 三者主要区别在于索引就绪文件描述符的时间复杂度：select 是 O(N)、poll 是 O(N)、epoll 是 O(1)，连接数多时优先 epoll」

## 一句话总述
三者都是 Linux 下**就绪事件通知**机制，**本质差异在"每次调用如何找到就绪 fd"**：`select`/`poll` **每次调用都要把全量 fd 拷进内核并线性扫描**，复杂度 **O(N)**；`epoll` 把监听注册到内核红黑树、**只返回就绪 fd**，调用开销与总监听数无关（**O(1) 每事件**），故 C10K+ 必用 epoll。

## 面试官视角
- **考察意图**：是否知道"为什么连接数上去后 select/poll 会垮"，以及 epoll 解决了哪一步。
- **P5** 能背出 O(N)/O(N)/O(1) / **P6** 能解释"扫描 + 用户态/内核态拷贝"是 select/poll 的瓶颈，epoll 用红黑树 + 就绪链表消除它 / **P7** 能讲清 epoll 的 LT/ET 触发模式差异，能说 select 的 FD_SETSIZE=1024 上限。
- **红旗**：说"epoll 绝对比 select 快"（连接很少时差不多，甚至注册开销反而更重）；或把 O(1) 理解成"零成本"（epoll_wait 仍要返回就绪集合，是 O(就绪数)）。
- **惊艳点**：select 的 fd 上限是 **FD_SETSIZE（默认 1024）**，poll 用动态数组突破了它，但两者**每次调用仍全量扫描**——这才是 epoll 真正碾压的点 `[源码]`（Linux `fs/select.c`、`fs/eventpoll.c`）。

## 主问答
**Q（面试官原话）：** select、poll、epoll 有什么区别？为什么高并发都用 epoll？

**A · 标准答案骨架：**
1. **先给结论**：三者解决同一件事（**等哪些 fd 就绪**），差异在**查找就绪 fd 的成本**——select/poll 是 **O(N)**，epoll 是 **O(1) 每事件**；连接越多，前两者越慢，epoll 几乎不随连接数变慢。
2. **再给机制**：`select`/`poll` **每次调用**都要把监听 fd 集合**从用户态拷贝到内核态**，返回后应用再**线性遍历**整个集合挑出就绪的（N 越大扫描越久）；`epoll` 通过 `epoll_ctl` **注册一次**到内核红黑树，**就绪事件由回调挂进就绪链表**，`epoll_wait` 只取链表——**无需全量扫描、无需反复拷贝**。
3. **最后给边界**：`select` 还有 **FD_SETSIZE=1024** 的硬上限（poll 用数组突破）；epoll 的 O(1) 严格说是"**与总监听数无关**"，`epoll_wait` 返回就绪集合的成本是 **O(就绪数)**，并非字面零成本。

**加分层**：epoll 还区分 **LT（水平触发，默认，未读尽会反复通知）** 与 **ET（边缘触发，仅状态变化时通知一次，要求非阻塞 + 一次读尽）**——ET 性能更高但编码更苛刻 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 三者干嘛用 | 基本认知 | 监听多个 fd 就绪 | 换题 → 不及格 |
| L2 | 复杂度差异 | 是否背的 | O(N) vs O(1) | 判 P5 |
| L3 | 为什么 select 慢 | 真理解 | 拷贝 + 线性扫描 | 判 P6 |
| L4 | LT 与 ET | 架构判断 | 触发模式差异 | 判 P6+ |
| L5 | epoll 惊群/源码 | 实战经验 | accept 惊群、eventpoll.c | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Linux 2.5.44 引入 epoll 至今 | 无 | select/poll 属 POSIX，跨 Unix；epoll 是 Linux 专有，BSD 对应 kqueue |

## 关键代码
```python
import selectors, select
# epoll 在 Linux 下由 DefaultSelector 自动选用 [实测]
sel = selectors.DefaultSelector()            # Linux→EpollSelector, macOS→KqueueSelector
# 对比：select 模块手动传全量 fd 列表，每次调用都重传并扫描
rlist, _, _ = select.select([s1, s2, s3], [], [], 1.0)   # O(N) 扫描，N=监听总数
```

## ⚠️ 原文纠错
原文音译需还原：「**selectpool**」→ **select / poll**；「**put**」→ **poll**；「**apple / eppo / input**」→ **epoll**。原文给的复杂度 O(N)/O(N)/O(1) 与"连接数多优先 epoll"结论**正确**（标准面试口径）。补充：epoll 的 O(1) 应理解为"与总监听数无关，调用成本随就绪数走"，非字面零成本。核对范围：第 31~36 段 select/poll/epoll 对比。

## 总结与追问预判
- select/poll O(N) 瓶颈在"全量拷贝 + 线性扫描"；epoll 红黑树注册 + 就绪链表返回，O(1) 每事件。
- 顺势会问：**Python selectors 封装（见 184 卡）**、**为何多线程撑不住（见 182 卡）**。
