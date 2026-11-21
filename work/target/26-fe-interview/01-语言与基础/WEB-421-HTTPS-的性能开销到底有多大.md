---
title: [WEB-421] HTTPS 的性能开销到底有多大，如何压到可忽略
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-421：HTTPS 的性能开销到底有多大，如何压到可忽略

**答**：
- 开销集中在握手：TCP 1-RTT + TLS 1-RTT（1.3），约多几十到一百多毫秒（跨洲更高）；数据传输层的对称加密已接近免费（有 AES 硬件指令）
- CPU 开销在握手阶段的非对称运算，QPS 极高的网关才会感知
- 压到可忽略的手段：TLS 1.3 / 0-RTT、Session 复用、HTTP/2 或 HTTP/3 连接复用（少建连接）、OCSP 装订、证书链完整（避免客户端额外拉中间证书）
- 结论话术：现代服务「HTTPS 慢」的说法已过时，真正的收益（可缓存、HTTP/2 前提、安全）远大于成本

```bash
# 用 curl 计时看握手占比
curl -w "dns:%{time_namelookup} tcp:%{time_connect} tls:%{time_appconnect} total:%{time_total}\n" -so /dev/null https://example.com
```
