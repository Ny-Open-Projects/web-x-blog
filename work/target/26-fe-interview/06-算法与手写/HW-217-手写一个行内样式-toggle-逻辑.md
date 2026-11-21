---
title: [HW-217] 手写一个行内样式 toggle 逻辑：部分选中加粗的正确行为
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-217：手写一个行内样式 toggle 逻辑：部分选中加粗的正确行为

**答**：
- 需求：实现 toggleMark(range, mark)：选中区全部含该样式 → 移除；否则 → 对整个 range 添加（跨 block 各自添加并归一化）；部分选中时添加后与已有区间自动归一合并。
- 边界：collapsed（无选区）时记录"下一个输入继承样式"（pendingMark）；跨 block 逐 block 处理各自偏移。
- 评分点：toggle 判定（全含才移除）；pendingMark 机制。

```javascript
function toggleMark(doc, range, mark, pending) {
  if (range.isEmpty()) { pending.add(mark); return; }          // 无选区：下段继承
  const { head, tail } = range.normalized();
  const allHas = everyCharHas(doc, range, mark);
  forBetween(doc, head, tail, (b, s, e) => {
    if (allHas) b.marks = subtractMark(b.marks, mark, s, e);   // 全含：移除
    else b.marks.push({ ...mark, start: s, end: e });          // 否则：全加
    normalizeMarks(b);
  });
}
function everyCharHas(doc, range, mark) {
  let all = true;
  forBetween(doc, range.normalized().head, range.normalized().tail, (b, s, e) => {
    for (let i = s; i < e; i++)
      if (!b.marks.some(m => m.type === mark.type && m.start <= i && i < m.end)) all = false;
  });
  return all;
}
function subtractMark(marks, mark, s, e) {                     // 区间做减法
  const out = [];
  for (const m of marks) {
    if (m.type !== mark.type) { out.push(m); continue; }
    if (m.end <= s || m.start >= e) { out.push(m); continue; } // 不相交
    if (m.start < s) out.push({ ...m, end: s });               // 左残段
    if (m.end > e) out.push({ ...m, start: e });               // 右残段
  }
  return out;
}
```
