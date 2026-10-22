# 171. TCP 四次挥手

> 分类：网络 | 难度：L2 | 题型：原理题 | 频率：高 | 关键词：**四次挥手** / **FIN** / **2MSL** / **状态转换**
> 原文锚点：第 79~87 段「四次挥手：FIN/ACK，状态转换 FIN_WAIT/CLOSE_WAIT/LAST_ACK，最后等待 2MSL」

## 一句话总述
TCP 关闭连接需**四次挥手**：主动方发 **FIN**（seq=x）→ 被动方回 **ACK**（ack=x+1）→ 被动方发 **FIN**（seq=y）→ 主动方回 **ACK**（ack=y+1）。主动方在 **TIME_WAIT** 需等待 **2MSL** 才彻底关闭。

## 面试官视角
- **考察意图**：是否理解"为什么挥手比握手多一次"（关闭是双向独立的），以及 TIME_WAIT/2MSL 的意义。
- **P5** 能口述四步与 FIN/ACK / **P6** 能讲清状态（`FIN_WAIT_1`/`FIN_WAIT_2`/`CLOSE_WAIT`/`LAST_ACK`/`TIME_WAIT`） / **P7** 能解释 2MSL（确保最后 ACK 到达 + 让旧报文失效）与 TIME_WAIT 过多的后果。
- **红旗**：以为挥手也是三次；或说不清为什么中间 ACK 与 FIN 不能合并。
- **惊艳点**：中间两次**不能合并**是因为被动方收到 FIN 后可能还有数据要发（半关闭），先回 ACK、数据发完才发 FIN —— 验证：对比"同时关闭"会合并成三次，但常规是四次 `[经验]`。

## 主问答
**Q（面试官原话）：** 那断开连接时的四次挥手呢？为什么是四次？

**A · 标准答案骨架：**
1. **先给结论**：四次挥手 = **FIN → ACK → FIN → ACK**，主动方与被动方各自单向关闭。
2. **再给机制**：① 主动方 `FIN`（状态 `FIN_WAIT_1`）；② 被动方 `ACK`（`CLOSE_WAIT`，主动方转 `FIN_WAIT_2`）；③ 被动方数据发完再 `FIN`（`LAST_ACK`）；④ 主动方 `ACK` 进入 `TIME_WAIT`，等 **2MSL** 后 `CLOSED`。
3. **最后给边界**：**ACK 与 FIN 不合并**是因为被动方可能仍有数据要传（TCP 支持半关闭）；主动方 `TIME_WAIT` 等 2MSL 是为"兜底最后 ACK 重传"和"让网络残留旧报文失效"。

**加分层**：大量短连接会堆积 TIME_WAIT，可借 `SO_REUSEADDR` 或调 `tcp_tw_reuse` 缓解——这是高并发服务的真实调优点 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 哪四步 | 基本认知 | FIN/ACK/FIN/ACK | 换题 → 不及格 |
| L2 | 为什么比握手多一次 | 是否背的 | 半关闭/双向独立 | 判 P5 |
| L3 | TIME_WAIT 干嘛 | 有没有真理解 | 等2MSL兜底 | 判 P6 |
| L4 | 2MSL 含义 | 架构判断 | 最大报文寿命两倍 | 判 P6+ |
| L5 | TIME_WAIT 过多怎么办 | 实战经验 | SO_REUSEADDR/tw_reuse | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| RFC 793 至今 | 无 | 四次挥手与 2MSL 稳定；可提 `tcp_tw_reuse`（Linux 仅客户端侧安全） |

## 关键代码
```python
import socket
s = socket.create_connection(("www.example.com", 80), timeout=5)
s.shutdown(socket.SHUT_WR)   # 主动发送 FIN，进入 FIN_WAIT_1 [实测]
s.close()                    # 最终 ACK，进入 TIME_WAIT
```

## ⚠️ 原文纠错
原文第 79~87 段音译需还原：「**FINV**」→ **FIN**；「**yite二**」→ **FIN_WAIT_2**；「**拉CCK**」→ **LAST_ACK**；「**classwhite**」→ **CLOSE_WAIT**；「**两岁大段**」→ **2MSL（两倍最大报文生存时间）**。挥手机制（FIN/ACK 四步、状态转换、等待 2MSL）正确。核对范围：第 79~87 段四次挥手。

## 总结与追问预判
- 四次挥手 FIN→ACK→FIN→ACK；TIME_WAIT 等 2MSL。
- 顺势会问：**TCP vs UDP（见 172 卡）**、**三次握手（见 170 卡）**。
