---
title: [XP-385] 手写一个 setData 体积审计器
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-385：手写一个 setData 体积审计器

**答**：
- 需求：implement setDataAudit(calls)。calls 为 [{ page, size, ts }]；输出 { totalPages, avgKB, over100: [page], top }（超 100KB 的页面与 Top5 最大单次）；size 字节转 KB 保留 1 位。
- 边界：size <= 0 忽略；页面去重统计次数与总量；calls 空返回零值。
- 评分点：页面聚合；KB 换算；超标筛；Top5

```javascript
function setDataAudit(calls) {
  const byPage = new Map();
  for (const c of calls) {
    if (c.size <= 0) continue;
    const v = byPage.get(c.page) ?? { count: 0, total: 0, max: 0 };
    v.count++; v.total += c.size; v.max = Math.max(v.max, c.size);
    byPage.set(c.page, v);
  }
  const entries = [...byPage.entries()].map(([page, v]) =>
    ({ page, count: v.count, avgKB: +(v.total / v.count / 1024).toFixed(1),
      maxKB: +(v.max / 1024).toFixed(1) }));
  return { totalPages: entries.length,
    avgKB: +(calls.reduce((s, c) => s + c.size, 0) / (calls.length || 1) / 1024).toFixed(1),
    over100: entries.filter(e => e.maxKB > 100).map(e => e.page),
    top: entries.sort((a, b) => b.maxKB - a.maxKB).slice(0, 5) };
}
```
