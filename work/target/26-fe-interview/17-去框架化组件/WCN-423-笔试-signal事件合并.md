---
title: [WCN-423] 笔试：高频事件（input）写入信号的「帧合并」优化。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-423：笔试：高频事件（input）写入信号的「帧合并」优化。
**答**：`frameSet(sig, v)`：同一帧内多次写合并（rAF 前 Last-Wins），帧边界统一 set。与直接 set 的对比（写次数统计）。

```javascript
let pending = new Map(), rafId = null;
function frameSet(sig, v) {
  pending.set(sig, v);
  if (rafId === null) rafId = requestAnimationFrame(() => {
    rafId = null;
    for (const [s, val] of pending) s.set(val);   // 一帧一次传播
    pending.clear();
  });
}
// 100 次 input → 写传播 1 次（Last-Wins）

```

**评分点**：
- pending 缓存 + rAF 统一 flush。
- Last-Wins 语义（中间值丢弃）。
- 统计对比：连续 input 100 次 → 实际传播 1-2 次。
- 边界：元素卸载时 pending flush（不丢终值）。
