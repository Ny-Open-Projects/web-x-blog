---
title: [MFW-297] 从浏览器点击到 DB 行的 TraceID 贯穿实现
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-297：TraceID 贯穿

**答**:
- 链路：客户端 SDK 生成 traceparent（W3C 头）→ fetch 包装自动附头 → Server（RSC/Action）继承 context → DB 驱动 instrumentation 注释 SQL（pg的应用名/Commented tag）——一条线到底
- Next 特有处理：server fetch 的 outgoing 传播要手动（undici dispatcher 或 fetch 包装读 headers() 注入——框架不自动外传）
- 采样一致性：前端采样决定整条链（traceflags recorded）——服务端尊重入站采样位（不各自为政导致半条链）
- 查询体验：错误上报（MFW-283）附 traceId → 哨兵 issue 一键跳 trace——排障闭环的最后一公里

```javascript
// 客户端 fetch 包装
fetch(url, { headers: { traceparent: makeTraceParent() } })
// server 出站（RSC 内）
const out = await propagator.inject(headers())          // 读入站 context → 注入出站头
// SQL 注释：/* trace_id='...' */ → 慢查询日志反查链路
```
