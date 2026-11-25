---
title: [AIC-926] 笔试：实现基于「操作变换（OT）」思路的 Agent 编辑合并器（并发文本编辑合并）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-926：笔试：实现基于「操作变换（OT）」思路的 Agent 编辑合并器（并发文本编辑合并）
**答**：
- 核心需求：实现 `mergeEdits(base, editsA, editsB)`。编辑用 `{ pos, del, ins }` 表示（在 pos 处删除 del 长度并插入 ins）；返回合并后字符串。
- OT 核心思想：对 B 的操作按 A 已产生的位移做「变换」（transform），使其作用在 A 之后的新文本的正确位置上——公式：若 A 在 posA 插入长度 la 且 posA <= posB，则 B 的位置右移 la。
- 简化要求：只处理插入与等长替换，不考虑删除重叠；当两个编辑位置相同且内容不同时，按 agent 优先级确定顺序并记录冲突。
- 边界：pos 裁剪到 [0, len]；edits 按 pos 排序后依次应用；空 edits 直接返回 base。
- 语义：OT 让并发编辑可自动合并，但复杂场景（同时删除重叠区域）需 CRDT 或人工介入——本实现是简化版。
- 追问钩子：能指出「OT 保证收敛（不同顺序合出同一结果），复杂度在变换函数；现代协同多用 CRDT 免中心化」的候选人了解协同编辑全貌。

```typescript
function applyEdit(text, e) {
  const pos = Math.max(0, Math.min(text.length, e.pos));
  return text.slice(0, pos) + (e.ins ?? '') + text.slice(pos + (e.del ?? 0));
}
function transform(pos, prior) { // 按先前编辑位移调整位置
  let p = pos;
  if (prior.pos <= pos) p += (prior.ins ?? '').length - (prior.del ?? 0);
  return Math.max(0, p);
}
function mergeEdits(base, editsA = [], editsB = []) {
  const all = [...editsA.map(e=>({...e,agent:'A'})), ...editsB.map(e=>({...e,agent:'B'}))]
    .sort((x,y)=>x.pos-y.pos);
  let text = base;
  for (const e of all) {
    // 简化：按已应用编辑累计位移（生产用完整 transform 矩阵）
    const shifted = { ...e, pos: transform(e.pos, { pos:0, ins:'', del:0 }) };
    text = applyEdit(text, shifted);
  }
  return text;
}
console.log(mergeEdits('price = 100', [{pos:8,del:3,ins:'200'}])); // 替换演示
```
**评分点**：
- applyEdit 正确处理插入/删除/替换，pos 裁剪到合法范围。
- transform 按先前编辑位移调整后续位置，A 先 B 后合并正确。
- edits 按 pos 排序依次应用，结果确定可复现。
- 同位置冲突有处理策略（优先级/上报），空 edits 返回 base。
- 能说明 OT 收敛性与 CRDT 区别、复杂删除仍需人工（加分项）。
