---
title: [MFW-715] 笔试：手写 Flight 流处理器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-715：笔试：手写 Flight 流处理器

**答**：实现 `createStreamProcessor()`。方法：`push(chunk: { id, data, refs?: string[] })`。规则：1) **有序处理**：chunk 到达即应用（无依赖时）；2) **依赖挂起**：refs 引用未到达的 chunk → 挂起（pending）；依赖到达时自动应用挂起的 chunk（递归——A 等 B、B 到达时 A 也应用）；3) **重复去重**：已应用的 id 忽略；4) **解析失败容错**：apply 抛错 → 该 chunk 跳过但后续继续（不中断流）；5) `stats()` 返回 `{ applied, skipped, pending }`。边界：无 refs（直接应用）；循环引用（A 等 B、B 等 A——pending 互相等待——需要循环检测或超时：标记 pending 超过 N 个 chunk 后警告）；refs 指向已应用（正常）。

```javascript
function createStreamProcessor({ maxPending = 50 } = {}) {
  const applied = new Set();
  const pending = new Map();                             // depId -> [chunk]
  const stats = { applied: 0, skipped: 0, pending: 0 };

  function tryApply(chunk) {
    if (applied.has(chunk.id)) return;                   // 幂等
    applied.add(chunk.id);
    stats.applied++;
    // 递归应用等待此 chunk 的
    const waiting = pending.get(chunk.id);
    if (waiting) {
      pending.delete(chunk.id);
      waiting.forEach(w => tryApply(w));
    }
  }
  function push(chunk) {
    // 循环引用保护：pending 过大警告
    if (pending.size > maxPending)
      console.warn(`pending ${pending.size} > ${maxPending}——疑似循环引用`);
    // 依赖检查
    const refs = chunk.refs ?? [];
    const missing = refs.filter(r => !applied.has(r));
    if (missing.length) {
      for (const dep of missing) {
        (pending.get(dep) || pending.set(dep, []).get(dep)).push(chunk);
      }
      stats.pending = pending.size;
      return;
    }
    try {
      tryApply(chunk);
    } catch (e) {
      stats.skipped++;                                   // 容错：跳过不中断
    }
  }
  return { push, stats: () => ({ ...stats, pending: pending.size }) };
}

// 自测
const applied = [];
const proc = createStreamProcessor();
proc.push = ((orig) => (chunk) => {
  orig(chunk);
  if (applied.length < proc.stats().applied) applied.push(chunk.id);
})(proc.push);

// 无依赖：直接应用
proc.push({ id: 1, data: 'A' });
console.log(proc.stats().applied === 1);

// 依赖挂起：chunk 2 等 chunk 1（已应用）→ 直接
proc.push({ id: 2, data: 'B', refs: ['1'] });
console.log(proc.stats().applied === 2);

// 依赖未到达：挂起
proc.push({ id: 4, data: 'D', refs: ['3'] });
console.log(proc.stats().pending === 1);                 // 等 chunk 3

// 依赖到达 → 自动应用
proc.push({ id: 3, data: 'C' });
console.log(proc.stats().applied === 4);                 // 3 应用 + 4 自动应用

// 重复去重
proc.push({ id: 3, data: 'C-dup' });
console.log(proc.stats().applied === 4);                 // 幂等

// 循环引用：A 等 B、B 等 A
const p2 = createStreamProcessor();
p2.push({ id: 'x', data: 'X', refs: ['y'] });
p2.push({ id: 'y', data: 'Y', refs: ['x'] });
console.log(p2.stats().applied === 0 && p2.stats().pending === 2);   // 互相等待
```

**评分点**：
- 依赖挂起与自动应用（递归——A 等 B、B 到达时 A 自动应用）；重复去重（幂等）
- 解析失败容错（跳过不中断流——流式容错）；循环引用的 pending 警告（不死锁但标注）
- 边界（无 refs/循环/重复）；stats 可观测
- 能说清「Flight 利用 HTTP 单响应有序性设计线性解析——依赖挂起用引用延迟绑定（RBL-503）解决乱序依赖」属于加分
