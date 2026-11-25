---
title: [AV-386] OT（操作变换）与 CRDT 的本质差异
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-386：OT（操作变换）与 CRDT 的本质差异

**答**：
- OT：中心服务器对并发操作做变换（transform(op, against)），逻辑清晰但实现复杂、依赖中心。
- CRDT：数据结构本身保证交换/结合/幂等（可交换收敛），去中心化、离线友好，空间开销大。
- 选型：文档类（纯文本）两者皆可；画板/离线优先用 CRDT（Yjs/Automerge）；强中心管控用 OT。

```javascript
// CRDT 一致性验证（交换性）
function crdtMergeCommutes(a, b, applyFn) {
  const s1 = structuredClone(base); applyFn(s1, a); applyFn(s1, b);
  const s2 = structuredClone(base); applyFn(s2, b); applyFn(s2, a);
  return JSON.stringify(s1) === JSON.stringify(s2);   // 交换次序无关
}
// OT transform 概念：
// transform(op1, op2) -> op1'  （op1 对 op2 之后的状态重新定位）
```
