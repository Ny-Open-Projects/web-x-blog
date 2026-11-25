---
title: [WEB-256] 接口慢排查 SOP：从 TTFB 到数据库
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 排查]
type: 面试题
---

## WEB-256：接口慢排查 SOP：从 TTFB 到数据库

**答**：
- 拆 Timing：DevTools Network → Timing 面板，逐段定位——DNS（解析慢）→ Connection（TLS/握手）→ Request sent → Waiting (TTFB)（服务端处理慢）→ Content Download（响应体大）。
- TTFB 大：链路远（CDN 加速）或服务端慢（查后端 APM/慢 SQL/锁）。Download 大：接口返回冗余字段/大列表未分页，前端用压缩（br/gzip）+ 字段裁剪 + 分页。
- 复现与归因：curl -w 独立复测排除前端；比较接口直连与走网关的差异；核对是否串行请求链（瀑布图看依赖链）。
- 前端侧优化：并行化无依赖请求、合并高频小请求、加 HTTP 缓存/ETag、关键接口本地缓存。

```bash
# 用 curl 独立复测接口各阶段耗时
curl -w '\nDNS:%{time_namelookup} TCP:%{time_connect} TLS:%{time_appconnect} TTFB:%{time_starttransfer} TOTAL:%{time_total}\n' \
  -o /dev/null -s https://api.example.com/list
# TTFB 大 → 服务端问题；TOTAL-TTFB 大 → 响应体大，看压缩与字段
```
