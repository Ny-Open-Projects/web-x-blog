---
title: [WEB-075] RTT 如何影响首屏时间？如何量化每一段的网络开销？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-075：RTT 如何影响首屏时间？如何量化每一段的网络开销？
**答**：
- 首屏前的网络串行链：DNS（1 RTT 起）→ TCP 握手（1 RTT）→ TLS 握手（1.2 为 2 RTT、1.3 为 1 RTT）→ 发请求等首字节（1 RTT 起），每段都按 RTT 计价。
- 以 100ms RTT 估算：纯新建 HTTPS 连接约 4-5 个 RTT，即 400-500ms 只花在"开始传数据之前"；这就是 keep-alive、会话复用、HTTP/2/3 多路复用被反复强调的原因。
- 量化工具：`curl -w` 输出各阶段耗时，浏览器侧看 Resource Timing 的 domainLookup/connect/secureConnection/TTFB 区间。
- 前端优化对应动作：预解析 DNS、preconnect 预握手、CDN 把 RTT 变短。

```bash
# 用 curl -w 量化一次请求的每个阶段耗时
curl -o /dev/null -s -w '
DNS 解析      %{time_namelookup}s
TCP 建连      %{time_connect}s
TLS 完成      %{time_appconnect}s
首字节 TTFB   %{time_starttransfer}s
总耗时        %{time_total}s
' https://example.com/
# time_connect 减 time_namelookup 约等于 1 个 TCP RTT
# time_appconnect 减 time_connect 约等于 TLS 握手耗时的 RTT 数
```

```html
<!-- 前端侧提前吃掉这些 RTT：预解析与预握手 -->
<link rel="dns-prefetch" href="//api.example.com">
<link rel="preconnect" href="https://api.example.com" crossorigin>
```
