# 177. HTTP 长连接（Keep-Alive）

> 分类：网络/HTTP | 难度：L2 | 题型：原理题 | 频率：中 | 关键词：**长连接** / **keep-alive** / **Content-Length** / **chunked**
> 原文锚点：第 98~120 段「HTTP/1.1 默认长连接，Connection: keep-alive 复用 TCP 连接；用 Content-Length 或 Transfer-Encoding: chunked 区分多个请求边界」

## 一句话总述
HTTP 基于 TCP，每次建连有三次握手/四次挥手开销。**HTTP/1.1 默认长连接（keep-alive）**复用同一 TCP 连接发多个请求；要区分"一次请求在哪结束"，靠 **Content-Length** 或 **Transfer-Encoding: chunked**（边生成边发、长度未知时）。

## 面试官视角
- **考察意图**：是否理解"为什么需要长连接"以及"复用连接后如何切分报文边界"这一对配套问题。
- **P5** 能说出 keep-alive 复用 TCP 连接 / **P6** 能讲清 Content-Length 与 chunked 两种边界方案 / **P7** 能指出 HTTP/1.1 长连接的"队头阻塞"缺陷，以及 HTTP/2 多路复用如何解。
- **红旗**：认为"长连接就是一直不断开、请求无限堆"；或说不清多个请求在同一连接上如何分隔。
- **惊艳点**：短连接每次都 TCP 握手/挥手，高并发下握手开销显著；但 HTTP/1.1 长连接仍有**队头阻塞**（一个慢响应堵住后续）——HTTP/2 用多路复用帧解决 —— 验证：`curl -v` 看 `Connection: keep-alive` 与多个请求复用同一连接 `[实测]`。

## 主问答
**Q（面试官原话）：** 什么是 HTTP 长连接？多个请求在同一个连接里怎么区分？

**A · 标准答案骨架：**
1. **先给结论**：**长连接（keep-alive）**让一个 TCP 连接服务多个 HTTP 请求，省去反复握手/挥手开销；HTTP/1.1 默认开启。
2. **再给机制**：复用连接后需界定"单个请求/响应边界"，两种方式——**Content-Length**（直接给总长度）或 **Transfer-Encoding: chunked**（分块，每块带大小、0 长度块表示结束，适合长度未知的动态内容）。
3. **最后给边界**：长连接不是"永远不关"，有超时与最大请求数；且 HTTP/1.1 仍有**队头阻塞**，HTTP/2 才用多路复用解决。

**加分层**：keep-alive 是"连接复用"，chunked 是"流式分块"——前者省握手、后者解"未知长度"难题，两者配合才是完整答案 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 为什么用长连接 | 基本认知 | 省 TCP 握手开销 | 换题 → 不及格 |
| L2 | 怎么区分请求边界 | 是否背的 | Content-Length/chunked | 判 P5 |
| L3 | chunked 何时用 | 有没有真理解 | 长度未知的动态内容 | 判 P6 |
| L4 | 长连接缺陷 | 架构判断 | 队头阻塞 | 判 P6+ |
| L5 | 你调过连接超时吗 | 实战经验 | keepalive 超时/连接池 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| HTTP/1.1（RFC 7230） | 默认 keep-alive；HTTP/2 多路复用 | 以 1.1 长连接为准；可提 2/3 已无队头阻塞 |

## 关键代码
```python
import http.client
conn = http.client.HTTPConnection("www.example.com")
# 显式声明长连接（HTTP/1.1 默认即此）[实测]
conn.request("GET", "/", headers={"Connection": "keep-alive"})
```

## ⚠️ 原文纠错
原文第 98~120 段音译需还原：「**STP长链接/TTP链接/长链接**」→ 长连接（keep-alive，复用底层 **TCP** 连接）；「**contentlength**」→ **Content-Length**；「**tranferincluding/chmp/chcksize/chckbody**」→ **Transfer-Encoding: chunked（分块传输）**；「**HTP链接/TTP**」→ **TCP 连接**。概念（HTTP/1.1 默认长连接、Connection: keep-alive、Content-Length 与 chunked 两种边界方案）正确。核对范围：第 98~120 段长连接。

## 总结与追问预判
- 长连接复用 TCP；Content-Length 或 chunked 界定边界；HTTP/1.1 有队头阻塞。
- 顺势会问：**Cookie 与 Session（见 178 卡）**、**报文结构（见 173 卡）**。
