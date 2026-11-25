---
title: [WEB-110] WebSocket 握手是怎么完成的？各头的作用是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-110：WebSocket 握手是怎么完成的？各头的作用是什么？
**答**：
- WebSocket 复用 HTTP 建连：客户端发带 `Upgrade: websocket` + `Connection: Upgrade` 的 GET，服务器回 `101 Switching Protocols`，之后同一 TCP 连接切换为 WebSocket 二进制帧协议。
- `Sec-WebSocket-Key` 是随机 base64，服务器拼接固定 GUID 后取 SHA-1 base64 回填 `Sec-WebSocket-Accept`，证明对端真的懂 WebSocket 而非误配的代理。
- `Sec-WebSocket-Version: 13` 声明协议版本；Origin 头供服务端做跨站校验（防跨站 WebSocket 劫持）。
- 握手后帧层自带掩码（客户端→服务端必须掩码，防中间代理缓存污染）、opcode、分片，心跳由 ping/pong 帧承担。

```http
GET /chat HTTP/1.1
Host: ws.example.com
Upgrade: websocket            # 请求升级协议
Connection: Upgrade           # 声明hop-by-hop升级意图
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==   # 随机值，防缓存误判
Sec-WebSocket-Version: 13     # 协议版本
Origin: https://www.example.com   # 服务端据此做跨站校验

HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
# Accept = base64(sha1(Key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"))
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

# 101 之后：这条 TCP 连接不再是 HTTP，改为 WebSocket 帧协议双向通信
```
