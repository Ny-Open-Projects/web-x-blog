---
title: [PER-808] RN 桥序列化的成本与优化：大对象跨桥传输的瓶颈与替代方案
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-808：RN 桥序列化的成本与优化：大对象跨桥传输的瓶颈与替代方案

**答**：
- 老架构 Bridge 的瓶颈：JS 与 Native 异步消息、JSON 序列化、跨线程拷贝三重开销——传 1MB 对象时序列化 + 拷贝可能占几十毫秒，且批量小消息合并成大 payload 同样卡。
- 典型问题场景：长列表一次性把全量数据传给 Native（应传 id/增量）；高频事件（滚动/手势）逐帧跨桥（应 Native 侧节流或合帧）。
- 新架构改善：JSI（JS Interface）让 JS 持有 Native 对象引用、同步调用、无序列化；TurboModule 按需加载 Native 模块。旧优化（减少跨桥次数）在 JSI 下依然有效，只是代价更低。
- 可落地优化（不分新旧架构）：跨桥 payload 体积审计、消息频率审计、大列表传索引而非全量、图片宽高在 Native 侧算完再回传。

```javascript
// 跨桥 payload 审计包装（老架构 Bridge，新架构 JSI 同理）
const origSend = NativeBridge.send;
let stat = { count: 0, bytes: 0, maxKB: 0 };
NativeBridge.send = function (payload) {
  const size = JSON.stringify(payload).length;
  stat.count++; stat.bytes += size;
  stat.maxKB = Math.max(stat.maxKB, size / 1024);
  if (size > 256 * 1024) console.warn('bridge payload > 256KB', stat);
  return origSend.call(this, payload);
};
// 优化模式：大列表传增量 + 索引
// BAD:  NativeBridge.send({ type: 'items', items: allItems })     // 全量
// GOOD: NativeBridge.send({ type: 'delta', index: 12, item: one }) // 增量
```
