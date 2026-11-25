---
title: [WEB-544] QPACK：HTTP/3 为什么把 HPACK 换成 QPACK
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-544：QPACK：HTTP/3 为什么把 HPACK 换成 QPACK

**答**：
- 根因是 h2 里 HPACK 依赖单流的有序字节流，而 QUIC 流之间独立交付，若还按 HPACK 编码，一个头块丢了要等重传，所有流都被堵住——把队头阻塞从传输层请回了应用层
- QPACK 的解法：把「必须按序」的部分拆成两条独立的单向流（编码/解码流），头块里只引用动态表索引；引用还没收到的条目时可以阻塞该请求流，但不阻塞其他流
- 两个关键参数：`SETTINGS_QPACK_BLOCKED_STREAMS`（允许阻塞的流数）和 `SETTINGS_QPACK_MAX_TABLE_CAPACITY`（动态表大小）——调小延迟友好但压缩率降，调大反之
- 实战影响：动态表是按连接维度的，连接频繁重建（弱网）会让动态表命中率暴跌，头部体积回升；长连接场景 QPACK 收益才明显
- 排查手段：对比 h2/h3 下同一页面请求头总字节数，若 h3 明显偏大，先查动态表是否因连接重建失效

```javascript
// 头部体积对比采样：评估 QPACK 实际收益
const sample = performance.getEntriesByType('resource')
  .filter(e => e.nextHopProtocol.startsWith('h3'))
  .map(e => ({ url: e.name, proto: e.nextHopProtocol, size: e.transferSize }));
beacon({ proto: 'h3', headerSizeSum: sample.reduce((s, x) => s + x.size, 0) });
```
