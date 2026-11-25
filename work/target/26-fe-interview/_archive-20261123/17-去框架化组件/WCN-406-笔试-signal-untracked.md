---
title: [WCN-406] 笔试：实现 untracked（不建立依赖的读取）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-406：笔试：实现 untracked（不建立依赖的读取）。
**题目**：`untracked(fn)`：fn 内的信号读取不加入当前 effect/computed 的依赖。与 peek(sig)（单次免追踪读取）两个 API。

```javascript
let untrackedDepth = 0;
export function untracked(fn) {
  untrackedDepth++;
  try { return fn(); } finally { untrackedDepth--; }
}
export const peek = (sig) => untracked(() => sig.get());
// track 时：if (untrackedDepth > 0) return;  → 跳过依赖收集

```

**评分点**：
- 栈标记：untracked 时压入「免追踪哨兵」，track 跳过。
- peek 直接读内部值（不触发 track）。
- 语义：快照读取（如比较 prev 值）。
- 嵌套正确性（untracked 内再 effect 正常追踪）。
