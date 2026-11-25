---
title: [PER-1253] 手写一个 CLS 来源归因器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1253：手写一个 CLS 来源归因器

**答**：
- 需求：实现 attributeCLS(entries)。entries 为 layout-shift 事件（含 value, sources: [{ node, prevRect, currRect }]）；输出 { total, byTag: { tag: sum } }，tag 取 source 节点标签名（无 sources 的 shift 归 unknown）；byTag 按 sum 降序；输出 top 元素选择器（每类一个样本）。
- 边界：value <= 0.001 忽略；sources 为空归 unknown；tag 未知返回 unknown。
- 评分点：阈值过滤；标签聚合；样本记录；排序输出

```javascript
function attributeCLS(entries) {
  const byTag = {}; const samples = {};
  let total = 0;
  for (const e of entries) {
    if (e.value <= 0.001) continue;
    total += e.value;
    const src = e.sources?.[0];
    const tag = src?.node?.tagName?.toLowerCase() ?? 'unknown';
    byTag[tag] = (byTag[tag] ?? 0) + e.value;
    samples[tag] ??= src?.node?.className ?? tag;
  }
  return { total: +total.toFixed(3),
    byTag: Object.fromEntries(Object.entries(byTag)
      .sort((a, b) => b[1] - a[1])
      .map(([t, v]) => [t, +v.toFixed(3)])),
    samples };
}
```
