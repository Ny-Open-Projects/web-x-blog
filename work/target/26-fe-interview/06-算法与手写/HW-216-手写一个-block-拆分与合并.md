---
title: [HW-216] 手写一个 block 拆分与合并：Enter 拆分 block 与 Backspace 合并相邻 block
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-216：手写一个 block 拆分与合并：Enter 拆分 block 与 Backspace 合并相邻 block

**答**：
- 需求：实现 splitBlock(pos)——offset 处拆为两个 block（后半段继承行内 marks 偏移调整）；mergeWithPrev(pos)——Backspace 在 block 头部时把当前 block 并入前一个（若类型相同），返回新光标。
- 边界：空 block 直接删除自身并入前一个；不同类型 block（标题/段落）默认不合并仅移动光标（可配置）；拆分后新 block id 重新生成。
- 评分点：marks 偏移平移；类型合并策略。

```javascript
function splitBlock(doc, pos, newId) {
  const b = doc.byId(pos.blockId);
  const rest = b.text.slice(pos.offset);
  const restMarks = b.marks.filter(m => m.end > pos.offset)
    .map(m => ({ ...m, start: Math.max(0, m.start - pos.offset),
      end: Math.max(0, m.end - pos.offset) }));    // marks 偏移平移
  b.text = b.text.slice(0, pos.offset);
  b.marks = b.marks.filter(m => m.end <= pos.offset);
  const nb = { id: newId, type: b.type, text: rest, marks: restMarks };
  doc.insertAfter(b.id, nb);
  return { blockId: nb.id, offset: 0 };            // 光标到新 block 头
}
function mergeWithPrev(doc, pos, { sameTypeOnly = true } = {}) {
  const b = doc.byId(pos.blockId);
  const prev = doc.prevOf(b.id);
  if (!prev) return null;
  if (sameTypeOnly && prev.type !== b.type) return { blockId: b.id, offset: 0 };   // 不合并只移动
  const offset = [...prev.text].length;
  prev.text += b.text;
  prev.marks.push(...b.marks.map(m => ({ ...m,
    start: m.start + offset, end: m.end + offset })));   // marks 平移
  doc.remove(b.id);
  return { blockId: prev.id, offset };                 // 光标在合并点
}
```
