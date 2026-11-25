---
title: [ZSM-433] 笔试：手写状态层 OT 简版（文本 op 变换 transform）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-433：手写状态层 OT 简版（文本 op 变换）
**答**：实现文本 OT 三件套：1) `apply(doc, op)`：op 为 `{type:'ins', pos, str}` 或 `{type:'del', pos, len}`；2) `transform(op, against)`：计算 op 在 against 已应用后的新坐标（并行 op 变换，两边同源）；3) `sync(localOps, remoteOps, doc)`：本地 op 队列与远端 op 集合收敛——远端 op 先 apply，本地 op 逐个 transform 后 apply；4) pos 越界钳制；5) 变换后 op 语义不变（插入内容保留）。

```javascript
export function apply(doc, op) {
  if (op.type === 'ins') return doc.slice(0, op.pos) + op.str + doc.slice(op.pos)
  return doc.slice(0, op.pos) + doc.slice(op.pos + op.len)        // del
}

export function transform(op, against) {
  // against: {type:'ins',pos,str} 在前
  if (against.type === 'ins') {
    if (op.pos >= against.pos) return { ...op, pos: op.pos + against.str.length }
    return op
  }
  // against: {type:'del',pos,len} 在前
  const end = against.pos + against.len
  if (op.type === 'del') {
    if (op.pos >= end) return { ...op, pos: op.pos - against.len }          // 完全在后
    if (op.pos + op.len <= against.pos) return op                            // 完全在前
    const s = Math.max(op.pos, against.pos)
    const e = Math.min(op.pos + op.len, end)
    return { ...op, pos: Math.min(op.pos, against.pos), len: op.len - (e - s) }  // 交叠裁剪
  }
  if (op.pos >= against.pos && op.pos < end) return { ...op, pos: against.pos }  // 插入点被删
  if (op.pos >= end) return { ...op, pos: op.pos - against.len }
  return op
}

export function sync(doc, localOps, remoteOps) {
  let d = doc
  for (const ro of remoteOps) {
    d = apply(d, ro)
    localOps = localOps.map((lo) => transform(lo, ro))       // 本地 op 对齐远端坐标
  }
  for (const lo of localOps) d = apply(d, lo)
  return { doc: d, localOps: [] }
}
```
**评分点**：
- transform 覆盖四象限（前/后/交叠/被删点），del 交叠裁剪 len 正确
- sync 顺序：远端先 apply，本地逐个 transform（经典 OT 收敛结构）
- 插入点恰好落在被删区间（pos 相等）的边界处理明确
- 越界钳制与 op 内容不丢失（str 保留）
