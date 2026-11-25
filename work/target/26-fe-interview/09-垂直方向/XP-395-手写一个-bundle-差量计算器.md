---
title: [XP-395] 手写一个 bundle 差量计算器
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-395：手写一个 bundle 差量计算器

**答**：
- 需求：implement diffBundle(prev, next)。prev/next 为 { file: bytes }（内容 hash 为 key）；输出 { added, removed, same } 与传输优化建议：相同 hash 文件不重传、仅传新增；diffKB 汇总。
- 边界：next 删除的文件记 removed（服务端同步清理）；prev 为空全量新增；hash 冲突忽略（同 key 视同相同）。
- 评分点：三类 diff；差量建议；KB 汇总；空 prev

```javascript
function diffBundle(prev = {}, next = {}) {
  const added = [], removed = [], same = [];
  for (const k of Object.keys(next))
    prev[k] ? same.push(k) : added.push(k);
  for (const k of Object.keys(prev))
    if (!next[k]) removed.push(k);
  const diffKB = +(added.reduce((s, k) => s + next[k], 0) / 1024).toFixed(1);
  return { added, removed, same,
    diffKB,
    advice: diffKB < prevTotal(prev) / 10
      ? '差量包收益高，走差量下发' : '差异过大走整包' };
}
function prevTotal(prev) { return Object.values(prev).reduce((s, v) => s + v, 0); }
```
