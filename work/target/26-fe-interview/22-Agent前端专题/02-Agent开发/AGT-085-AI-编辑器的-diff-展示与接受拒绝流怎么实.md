---
title: [AGT-085] AI 编辑器的 diff 展示与接受拒绝流怎么实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-085：AI 编辑器的 diff 展示与接受拒绝流怎么实现？
**答**：
- AI 改代码要给 diff 而不是直接覆盖：行级 LCS diff 聚成 hunk，用户逐块或整体接受/拒绝，拒绝即还原快照。
- diff 算法：LCS 动态规划标记 same/add/del，相邻变更聚成 hunk；生产可直接用 diff 库，手写是为了讲清原理。
- 部分接受的应用逻辑：same 行保留原文，被接受 hunk 的 add 行插入，未接受 hunk 的 del 行保留——按 lineA 指针重建文件。
- AI 场景特有：模型可能只回传修改片段，需要按上下文 anchor 定位插入点，定位失败要提示重新生成而不是错插。

```typescript
// 行级 LCS diff + 块级接受拒绝
type Op = { type: 'same' | 'add' | 'del'; text: string; lineA?: number };
type Hunk = { id: number; ops: Op[] };

export function lineDiff(oldText: string, newText: string): { ops: Op[]; hunks: Hunk[] } {
  const a = oldText.split('\n'), b = newText.split('\n');
  const dp: number[][] = Array.from({ length: a.length + 1 }, () => new Array(b.length + 1).fill(0));
  for (let i = a.length - 1; i >= 0; i--)
    for (let j = b.length - 1; j >= 0; j--)
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  const ops: Op[] = [];
  let i = 0, j = 0;
  while (i < a.length && j < b.length) {
    if (a[i] === b[j]) { ops.push({ type: 'same', text: a[i], lineA: i }); i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) { ops.push({ type: 'del', text: a[i], lineA: i }); i++; }
    else { ops.push({ type: 'add', text: b[j] }); j++; }
  }
  while (i < a.length) ops.push({ type: 'del', text: a[i], lineA: i++ });
  while (j < b.length) ops.push({ type: 'add', text: b[j++] });
  // 相邻 add/del 聚成 hunk，供 UI 逐块接受/拒绝
  const hunks: Hunk[] = [];
  let current: Hunk | null = null;
  for (const op of ops) {
    if (op.type === 'same') { current = null; continue; }
    if (!current) { current = { id: hunks.length, ops: [] }; hunks.push(current); }
    current.ops.push(op);
  }
  return { ops, hunks };
}

// 部分接受：same 行保留原文，被接受 hunk 插入 add，未接受 hunk 保留 del
export function applyDiff(oldText: string, ops: Op[], hunks: Hunk[], accepted: Set<number>): string {
  const a = oldText.split('\n');
  const hunkOf = new Map<Op, number>();
  for (const h of hunks) for (const op of h.ops) hunkOf.set(op, h.id);
  const out: string[] = [];
  for (const op of ops) {
    if (op.type === 'same') out.push(op.text);
    else if (op.type === 'add' && accepted.has(hunkOf.get(op)!)) out.push(op.text);
    else if (op.type === 'del' && !accepted.has(hunkOf.get(op)!)) out.push(a[op.lineA!]);
  }
  return out.join('\n');
}
```
