---
title: [BAS-107] HTTP keep-alive 解决什么问题？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-107：HTTP keep-alive 解决什么问题？
**答**：
- 每个请求都新建 TCP 连接要付三次握手和慢启动的开销；keep-alive 让一条 TCP 连接复用多个请求。
- HTTP/1.1 默认开启，但同一连接请求串行，存在队头阻塞：前一个响应没完，后续请求必须排队。
- HTTP/2 单连接多路复用（并行流）解决应用层队头阻塞；HTTP/3 换 QUIC 进一步解决 TCP 层队头阻塞。

```http
HTTP/1.1 200 OK
Connection: keep-alive
Keep-Alive: timeout=5, max=100
# 同一条 TCP 连接在超时或达到 max 个请求前持续复用
```
