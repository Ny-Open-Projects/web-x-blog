---
title: [WEB-066] 逐字段拆解一个 HTTP 请求报文，每部分的职责是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-066：逐字段拆解一个 HTTP 请求报文，每部分的职责是什么？
**答**：
- 请求行：方法 + 请求目标 + 协议版本，决定"做什么、对谁做、用什么语义说话"。
- 请求头按职责分组：条件头（If-None-Match/If-Modified-Since）、内容协商头（Accept/Accept-Encoding）、连接头（Connection/Host）、安全头（Origin/Referer）。
- 空行（CRLF）是头部与 Body 的分界，解析器靠它判断头结束。
- Body 由 Content-Type 和 Content-Length/Transfer-Encoding 描述，可能完全为空（GET）。
- 面试时能现场默写一个完整请求并解释每个头的作用，是网络功底的直接证明。

```http
POST /api/login HTTP/1.1          # 请求行：方法 + 路径 + 版本
Host: api.example.com             # 唯一必须的 HTTP/1.1 头，虚拟主机路由依据
User-Agent: Mozilla/5.0 Chrome    # 客户端标识，UA 检测的来源（已不被信任）
Accept: application/json          # 内容协商：我要什么类型的响应
Accept-Encoding: gzip, br         # 我支持哪些压缩算法
Content-Type: application/json    # 请求体的媒体类型
Content-Length: 38                # 请求体字节数，接收方据此切分
Origin: https://www.example.com   # CORS 判定的来源站点
Cookie: session=abc123            # 自动携带的会话凭证
Connection: keep-alive            # 连接复用声明

{"username":"fe","password":"***"}  # 空行之后的请求体
```
