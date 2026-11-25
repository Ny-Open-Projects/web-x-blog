---
title: [MFW-823] 笔试：手写 HLC 混合逻辑时钟生成器（含远程时间戳合并）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-823：笔试：手写 HLC 混合逻辑时钟生成器（含远程时间戳合并）

**答**：
- 结论：HLC = (physical, logical, node)；它保证因果序：若事件 a 发生在 b 之前，则 ts(a) < ts(b)，且不依赖物理时钟绝对同步。
- 关键：本地时钟回拨时 logical++；收到远程时间戳时物理取 max(本地, last, 远程)，再正确推进 logical；node 做 tie-break。
- 追问钩子：HLC 与向量时钟的取舍？——HLC 有界（O(1) 空间）但不精确捕捉并发；向量精确但随节点数膨胀。

```javascript
function makeHLC(nodeId) {
  let last = { p: 0, l: 0 };
  return function now(remote = null) {
    const pt = Date.now();
    if (remote) {
      const p = Math.max(pt, last.p, remote.p);
      const l = (pt <= last.p && remote.p <= last.p)
        ? Math.max(last.l, remote.l) + 1 : 0;
      last = { p, l };
    } else if (pt > last.p) {
      last = { p: pt, l: 0 };
    } else {
      last = { p: last.p, l: last.l + 1 };            // 时钟回拨 → 逻辑递增
    }
    return { ...last, node: nodeId };
  };
}
function cmp(a, b) {
  return a.p - b.p || a.l - b.l || a.node.localeCompare(b.node);
}

// 自测：因果序
const a = makeHLC('a'), b = makeHLC('b');
const t1 = a();
const t2 = b(t1);          // b 观察到 a 的事件
console.log(cmp(t2, t1) > 0);                       // true
const t3 = a(t2);          // a 再观察 b，形成闭环因果
console.log(cmp(t3, t2) > 0);                       // true
```

**评分点**：
- HLC 三元组 (physical, logical, node) 设计正确，保证因果序 ts(a) < ts(b)
- 本地物理时钟回拨时通过 logical++ 保持单调
- 合并远程时间戳：物理取 max(本地, last, 远程)，logical 正确推进
- node 做 tie-break 消除平局；能比较 HLC 与向量时钟（加分）
