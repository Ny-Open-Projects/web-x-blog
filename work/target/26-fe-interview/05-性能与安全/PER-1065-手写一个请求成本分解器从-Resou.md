---
title: [PER-1065] 手写一个请求成本分解器：从 Resource Timing 输出握手占比
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1065：手写一个请求成本分解器：从 Resource Timing 输出握手占比

**答**：
- 需求：实现 costBreakdown(entries)。entries 为 resource timing 数组；每条输出 { name, dns, tcp, tls, wait, download, handshakeShare }（各段 ms，share 保留 1 位）；汇总输出 { slowest, handshakeHeavy }：slowest 为总耗时最长条目，handshakeHeavy 为握手占比 > 40% 的条目列表。
- 边界：secureConnectionStart 为 0 时 tls = 0；domainLookupStart 缺失段记 0；空数组返回 { slowest: null, handshakeHeavy: [] }；share 分母为 0 时 share = 0。
- 评分点：分段计算；缺失段兜底；占比分母 0；汇总归类

```javascript
function costBreakdown(entries) {
  if (!entries.length) return { slowest: null, handshakeHeavy: [] };
  const seg = e => {
    const dns = Math.max(0, e.domainLookupEnd - e.domainLookupStart);
    const tcp = Math.max(0, e.connectEnd - e.connectStart);
    const tls = e.secureConnectionStart
      ? Math.max(0, e.requestStart - e.secureConnectionStart) : 0;
    const wait = Math.max(0, e.responseStart - e.requestStart);
    const download = Math.max(0, e.responseEnd - e.responseStart);
    const total = e.responseEnd - e.startTime;
    return { dns, tcp, tls, wait, download, total,
      handshakeShare: total ? +((dns + tcp + tls) / total * 100).toFixed(1) : 0 };
  };
  const items = entries.map(e => ({ name: new URL(e.name).pathname, ...seg(e) }));
  return { slowest: items.reduce((a, b) => (b.total > a.total ? b : a)),
    handshakeHeavy: items.filter(i => i.handshakeShare > 40) };
}
```
