---
title: [PER-592] 前端监控如何与后端 APM 打通？一条慢页面的 trace 怎么串起前端和后端数据？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-592：前端监控如何与后端 APM 打通？一条慢页面的 trace 怎么串起前端和后端数据？

**答**：
- 串联协议是 W3C Trace Context（见 566），打通的关键是**前后端共用同一 traceId 语义**：前端 span 上报到自己的 APM 通道时带 traceparent，后端网关从 header 提取并延续 trace；前端错误/慢样本上报也带 traceId。
- 排障闭环：慢样本（LCP p95 会话）-> 点开看该会话的 API trace 列表（每请求 span + 后端耗时分解）-> 直接跳转到后端 APM 的 trace 详情（网关/服务/DB 各段），一次点击完成前后端会诊。
- 需要治理的断点：网关不透传 header（配置遗漏）、前端 span 与后端 span 时间不同步（时钟偏差，用服务器时间校正）、第三方接口不透传（trace 断链，标注外部边界）。
- 数据对齐：前端 span 的耗时口径（客户端测得的 RTT）与后端 span（服务端处理时长）之差 = 网络传输，这个差值本身是排障信号。

```javascript

// 慢样本 -> 关联 trace 列表的数据结构
function attachTrace(sessionReport) {
  return {
    ...sessionReport,
    traceId: window.__traceId,
    apiSpans: window.__apiSpans.map(s => ({
      url: s.url, clientMs: s.dur,                          // 客户端测得（含网络）
      serverMs: s.serverTiming?.dur ?? null,                // Server-Timing 头里后端耗时
      netMs: s.serverTiming ? s.dur - s.serverTiming.dur : null, // 差值 = 网络传输
      traceparent: s.traceparent,                           // 后端 APM 可直接跳转
    })),
  };
}
// Server-Timing: dur=123 说明后端处理 123ms -> 客户端总 890ms -> 网络/等待占 767ms，问题在网络层
```
