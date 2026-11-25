---
title: [MFW-656] 笔试：手写 Suspense 流序模拟器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-656：笔试：手写 Suspense 流序模拟器

**答**：实现 `simulateStreamOrder(boundaries, { globalTimeout })`。boundaries: `{ name, resolveMs, fallback }[]`（按树序声明）。规则：1) 树序发送：shell 先发（t=0：所有 fallback）——各边界按 resolveMs 到达顺序流式发送（完成序非树序）；2) 全局超时：resolveMs > globalTimeout 的边界 → 发送 fallback 值（不等待——超时降级 RBL-655）；3) 返回事件序列 `Array<{ t, event: 'shell'|'resolve'|'timeout', name? }>`（时序可审计）；4) 总传输时间 = max(所有 resolveMs ≤ timeout 的)。边界：空 boundaries（只 shell）；全部超时（全 fallback）；resolveMs=0（立即）。

```javascript
function simulateStreamOrder(boundaries = [], { globalTimeout = 5000 } = {}) {
  const events = [{ t: 0, event: 'shell' }];
  const pending = boundaries.map(b => ({ ...b,
    timedOut: b.resolveMs > globalTimeout }));
  // 按完成序排序（resolveMs 升序；超时的排最后）
  const ordered = [...pending].sort((a, b) => {
    if (a.timedOut !== b.timedOut) return a.timedOut ? 1 : -1;
    return a.resolveMs - b.resolveMs;
  });
  for (const b of ordered) {
    if (b.timedOut) {
      events.push({ t: globalTimeout, event: 'timeout', name: b.name });
    } else {
      events.push({ t: b.resolveMs, event: 'resolve', name: b.name });
    }
  }
  const resolved = pending.filter(b => !b.timedOut);
  return {
    events,
    totalTime: resolved.length ? Math.max(...resolved.map(b => b.resolveMs), 0) : 0,
    fallbacks: pending.filter(b => b.timedOut).map(b => b.name),
  };
}

// 自测
const boundaries = [
  { name: 'header', resolveMs: 10, fallback: 'H-skel' },      // 快
  { name: 'trending', resolveMs: 100, fallback: 'T-skel' },
  { name: 'personalized', resolveMs: 8000, fallback: 'P-skel' },  // 超 5s
  { name: 'footer', resolveMs: 5, fallback: null },
];
let r = simulateStreamOrder(boundaries, { globalTimeout: 5000 });
// 事件序：shell(0) → footer(5) → header(10) → trending(100) → personalized timeout(5000)
console.log(r.events.map(e => e.name ?? e.event).join(','));
// shell,footer,header,trending,timeout
console.log(r.totalTime === 100);                        // 只算非超时
console.log(r.fallbacks.join(',') === 'personalized');   // 超时降级

// 完成序 ≠ 树序（footer 树序最后但 resolve 最先）
console.log(r.events[1].name === 'footer');

// 全超时
r = simulateStreamOrder([{ name: 'x', resolveMs: 99999, fallback: 'x' }],
  { globalTimeout: 100 });
console.log(r.totalTime === 0 && r.fallbacks.join(',') === 'x');

// 空
r = simulateStreamOrder([], { globalTimeout: 100 });
console.log(r.events.length === 1 && r.events[0].event === 'shell');
```

**评分点**：
- 完成序发送（resolveMs 排序——流式解耦完成序与树序 RBL-655）；超时降级（fallback 值）
- totalTime 只计非超时（超时边界的 fallback 即发——不计等待）；事件序列可审计
- 边界（空/全超时/立即）；树序与完成序的分离验证
- 能说清「多 Suspense 按完成序而非树序发送——流式的本质是解耦完成顺序与显示顺序」属于加分
