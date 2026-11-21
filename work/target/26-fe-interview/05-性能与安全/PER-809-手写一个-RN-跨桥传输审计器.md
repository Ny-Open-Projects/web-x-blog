---
title: [PER-809] 手写一个 RN 跨桥传输审计器：统计 bridge 消息大小与频率并输出超标点
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-809：手写一个 RN 跨桥传输审计器：统计 bridge 消息大小与频率并输出超标点

**答**：
- 需求：包装 bridge.send，按调用点（调用方传入 tag）统计：消息条数、总字节、p75/p95 字节、最大单条；频率超 60 次/秒的 tag 标记为 high-freq；单条超 256KB 标记 oversized；输出超标报告（按总字节降序）。
- 边界：JSON.stringify 失败（循环引用）按 0 计并标记 unserializable；时间窗滑动统计（60s）而非全量平均。
- 评分点：滑动窗口频率统计；p75/p95 正确性；unserializable 兜底。

```javascript
function createBridgeAuditor({ windowMs = 60000, freqLimit = 60, sizeLimit = 256 * 1024 } = {}) {
  const events = new Map();                     // tag -> [{t, bytes}]
  return {
    wrap(bridge) {
      const raw = bridge.send.bind(bridge);
      bridge.send = (payload, tag = 'unknown') => {
        let bytes = 0, unserializable = false;
        try { bytes = JSON.stringify(payload).length; } catch { unserializable = true; }
        const arr = (events.get(tag) ??= []);
        const now = Date.now();
        arr.push({ t: now, bytes });
        while (arr.length && now - arr[0].t > windowMs) arr.shift();  // 滑动窗口
        return raw(payload);
      };
    },
    report() {
      const now = Date.now();
      return [...events].map(([tag, arr]) => {
        const live = arr.filter(e => now - e.t <= windowMs);
        const sizes = live.map(e => e.bytes).sort((a, b) => a - b);
        const pick = p => sizes.length ? sizes[Math.floor(sizes.length * p)] : 0;
        return { tag, count: live.length,
          totalMB: +(sizes.reduce((s, b) => s + b, 0) / 1048576).toFixed(2),
          p75: pick(0.75), p95: pick(0.95),
          highFreq: live.length > freqLimit,
          oversized: sizes.some(b => b > sizeLimit) };
      }).sort((a, b) => b.totalMB - a.totalMB);
    },
  };
}
```
