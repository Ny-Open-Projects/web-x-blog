---
title: [WEB-572] 笔试：手写 TTFB 按协议/RTT 分桶统计报表
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 可观测]
type: 笔试题
---

## WEB-572：笔试：手写 TTFB 按协议/RTT 分桶统计报表

**答**：实现 `buildReport(entries)`：输入一批 navigation/resource timing 对象，输出按 `{协议}x{RTT档}` 二维分桶的 TTFB 统计。要求：① 协议取 `nextHopProtocol`，未知归 `other`；② RTT 取 `navigator.connection.rtt`（0-100/100-300/300+ 三档）；③ 每桶输出 count/p50/p75/p90；④ 缺 rtt 数据的样本归 `nortt` 桶。给出实现与调用示例。

```javascript
function p(arr, q) {
  if (!arr.length) return null;
  const s = [...arr].sort((a, b) => a - b);
  return s[Math.min(s.length - 1, Math.floor(q * (s.length - 1)))];
}

function buildReport(entries, connRtt) {
  const buckets = {};
  for (const e of entries) {
    const proto = e.nextHopProtocol || 'other';
    const rtt = connRtt == null ? 'nortt'
      : connRtt < 100 ? 'rtt<100' : connRtt < 300 ? 'rtt100-300' : 'rtt300+';
    const ttfb = e.responseStart - e.startTime;
    if (ttfb < 0) continue; // 无效样本
    const key = `${proto}|${rtt}`;
    (buckets[key] ||= { count: 0, arr: [] });
    buckets[key].count++;
    buckets[key].arr.push(ttfb);
  }
  return Object.fromEntries(Object.entries(buckets).map(([k, b]) => [k, {
    count: b.count, p50: p(b.arr, .5), p75: p(b.arr, .75), p90: p(b.arr, .9),
  }]));
}

// 调用: buildReport(performance.getEntriesByType('navigation'), navigator.connection?.rtt)
```

**评分点**：
- ttfb 计算用 responseStart - startTime 且过滤负值
- rtt 缺失有兜底桶而不是丢样本
- 分位数计算正确（排序 + 索引），count 与分位并存
- 二维分桶 key 设计支持后续按维度聚合
