---
title: [NODE-318] 消息队列深水区：大消息与载荷治理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-318：消息队列深水区：大消息与载荷治理？
**答**:
- 大消息问题：Kafka 默认 1MB 上限（大 payload 拖慢整分区与复制）；消息里塞大 JSON 是反模式。
- 治理方案：引用模式——消息只带事件元数据+数据地址（对象存储 key/DB id），消费方按需拉取；消息级压缩 zstd；schema 瘦身（只发变更字段）。
- 边界：小事件（<64KB）直发；大载荷（图片/导出结果）走引用；中间量高频事件裁剪字段。
- 监控：消息体积分布 P99——>100KB 的 topic 进治理清单。

```javascript
// 引用模式
await producer.send({ messages: [{
  value: JSON.stringify({
    type: 'report.generated', version: 1, reportId,
    payloadRef: { store: 'oss', key: `reports/${reportId}.json`, size, hash },   // 引用而非正文
  }),
}]});
// 消费端：按需拉取
const meta = JSON.parse(message.value);
const data = meta.payloadRef ? await oss.get(meta.payloadRef.key) : meta.data;
```
