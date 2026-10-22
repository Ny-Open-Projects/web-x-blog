# 181. 用原始 Socket 手工发送 HTTP 请求

> 分类：网络/Python | 难度：L2 | 题型：代码题 | 频率：中 | 关键词：**HTTP报文** / **Host头** / **\r\n\r\n** / **recv循环**
> 原文锚点：第 60~85 段「HTTP 基于 TCP；用 socket 构造请求行(GET+路径+版本)+Host 头+\r\n\r\n 空行，send 后 recv 响应；requests 库/爬虫/Web 框架底层皆是 socket」

## 一句话总述
HTTP 跑在 TCP 之上：建好 TCP 连接后，**手工拼 HTTP 报文**（`请求行 GET / HTTP/1.1` + `Host:` 头 + 空行 `\r\n\r\n`）通过 `sendall` 发出，再 `recv` 读回响应。理解这一步，就明白 `requests`、爬虫、Web 框架的本质。

## 面试官视角
- **考察意图**：是否理解"HTTP 只是 TCP 上的一段约定格式的文本"，而非只会调 `requests`。
- **P5** 能说出"先 TCP 连接再发 HTTP 文本" / **P6** 能讲清报文为何要 `Host` 头与结尾双 `\r\n\r\n` / **P7** 能指出 `recv(1024)` 只读部分、需循环读到空（连接关闭）或按 Content-Length 读全。
- **红旗**：认为"发 HTTP 必须装 requests 库"；或漏写 `Host` 头导致 400。
- **惊艳点**：手工 socket 发 HTTP 时，`\r\n\r\n` 是"头部结束"的分界——少一个 `\r\n` 服务端会一直等头部；这正是很多自写客户端 卡死 的根因 —— 验证：抓包看 `0d 0a 0d 0a` 字节 `[实测]`。

## 主问答
**Q（面试官原话）：** 不用 requests，怎么用 socket 发一个 HTTP 请求？

**A · 标准答案骨架：**
1. **先给结论**：HTTP 基于 TCP——先 `connect(主机, 80)`，再把**协议文本**拼好 `sendall`，最后 `recv` 读响应。
2. **再给机制**：报文 = `请求行`（如 `GET / HTTP/1.1`）+ `Host:` 头 + **空行 `\r\n\r\n`**（标志头部结束）；HTTP/1.1 **必须带 Host 头**（虚拟主机靠它区分域名）。
3. **最后给边界**：`recv(1024)` 通常**只读回部分**；要拿完整响应需**循环 recv 直到返回空字节**（短连接服务端关连接）或按 `Content-Length` 累计读全。

**加分层**：`requests`、各种爬虫、乃至 Web 框架，底层都是"socket + HTTP 文本协议"的封装——看懂这一层，所有上层工具不再黑盒 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 为什么能裸 socket 发 HTTP | 基本认知 | HTTP 基于 TCP 文本 | 换题 → 不及格 |
| L2 | 报文怎么结尾 | 是否背的 | \r\n\r\n 空行 | 判 P5 |
| L3 | 为什么必须 Host 头 | 有没有真理解 | 虚拟主机/1.1 强制 | 判 P6 |
| L4 | 怎么读完整响应 | 架构判断 | 循环 recv/Content-Length | 判 P6+ |
| L5 | 你读过 HTTP 库源码吗 | 实战经验 | socket 封装/连接池 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| HTTP/1.1（RFC 7230） | Host 头自 1.1 起强制 | 以 1.1 为准；可提 HTTP/2 已非文本、不能裸 socket 拼 |

## 关键代码
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.baidu.com", 80))                 # HTTP 默认 80 端口 [实测]
req = "GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n"
s.sendall(req.encode("utf-8"))                    # 手工构造请求行+Host+空行
resp = s.recv(1024)                               # 仅读到部分，生产需循环读全
print(resp.decode("utf-8", errors="replace"))
s.close()
```

## ⚠️ 原文纠错
原文第 60~85 段音译需还原：「**STP/STTP/GTP**」→ **HTTP**；「**PCP**」→ **TCP（HTTP 建立在 TCP 之上）**；「**sooft/solid/surfit**」→ **socket**；「**百度点com**」→ **baidu.com**；「**三道二**」→ **send（发送）**；「**SCTB杠r杠n**」→ **`\r\n`（CRLF）**；「**一零二四**」→ **1024（recv 缓冲区大小）**；「**surface**」→ **socket**。手工发 HTTP 的请求行+Host+空行 `\r\n\r\n` 构造正确。核对范围：第 60~85 段 socket 发 HTTP 请求。

## 总结与追问预判
- HTTP=TCP 上的文本协议；手工拼请求行+Host+\r\n\r\n 发出，循环 recv 读全。
- 顺势会问：**HTTP 报文结构（见 173 卡）**、**TCP 客户端（见 180 卡）**。
