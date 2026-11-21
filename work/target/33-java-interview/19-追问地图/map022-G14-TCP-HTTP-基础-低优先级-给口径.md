---
title: "G14. TCP/HTTP 基础（低优先级，给口径）"
date: 2026-11-18
categories: [Java面试, 追问地图]
tags: [Java面试, 补漏卡, 33]
type: 补漏卡
disableNunjucks: true
---

### G14. TCP/HTTP 基础（低优先级，给口径）

**【口径（知道即可，不展开）】** 三次握手（确认双向通信能力）/四次挥手（TIME_WAIT 等待 2MSL 防旧包）；TIME_WAIT 过多 = 频繁短连接，开连接复用解决；HTTP/2 多路复用解决队头阻塞（应用层仍有），HTTP/3 QUIC 基于 UDP；HTTPS = TLS 握手换密钥 + 对称加密传输。P10 层的考察点只有一个：**这些决定了你的连接池/超时/keep-alive 参数怎么配**（呼应 G9），纯原理题极少出现。

---
