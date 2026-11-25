---
title: [1125] 笔试手写：实现 useQueryKeyDiffSync
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 缓存]
type: 笔试题
---

## 1125：笔试手写：实现 useQueryKeyDiffSync

**答**：筛选参数变化时保留可复用数据。实现 diffSync(prevKey, nextKey)：keys 为参数对象数组（如 [{ tab: 'a', q: 'x' }]）。输出：哪些参数变了（changed）、哪些没变（kept）；建议策略——全部 kept → 缓存完全复用；只有末端参数变 → keepPreviousData 展示旧数据 + 后台取新；关键维度（第一段）变 → 硬切新缓存。返回 { changed, kept, strategy }。

```js
function diffSync(prevKey, nextKey, critical = ['tab']) {
  const all = new Set([...Object.keys(prevKey), ...Object.keys(nextKey)]);
  const changed = [], kept = [];
  for (const k of all) {
    if (prevKey[k] !== nextKey[k]) changed.push(k);
    else kept.push(k);
  }
  const criticalChanged = changed.some(k => critical.includes(k));
  const strategy = changed.length === 0 ? 'reuse'
    : criticalChanged ? 'hard-switch'   // 关键维度变化：旧数据不可信，硬切
    : 'keep-previous';                  // 末端参数变化：旧数据可展示
  return { changed, kept, strategy };
}
```

**评分点**：
- changed/kept 分集（复用判定最小单元）
- 关键维度优先判定（criticalChanged 决定硬切）
- 三档策略映射到具体缓存行为
- 能讨论：keepPreviousData 的代价——旧数据短暂展示可能与新筛选矛盾，需视觉弱化
