---
title: [HW-252] 手写一个冲突提示 UI 数据：并发冲突区域检测与标记
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-252：手写一个冲突提示 UI 数据：并发冲突区域检测与标记

**答**：
- 需求：实现 ConflictMarker：收服务端广播的并发 op（与本地 pending 并发的），计算其影响区间与本地选区/未确认 op 区间重叠 → 生成冲突标记 [{range, mine, theirs, kind: edit-edit|insert-insert}]；提供 resolve 策略（theirs-wins / mine-wins / manual）的执行。
- 边界：区间重叠判定（含端点相切不算）；同一区域多冲突合并；manual 状态下本地 op 不自动应用。
- 评分点：区间重叠检测；冲突分类；策略执行。

```javascript
class ConflictMarker {
  constructor() { this.marks = []; }
  detect(localRange, serverOp) {
    const sRange = opRange(serverOp);
    const overlap = localRange.start < sRange.end && sRange.start < localRange.end;
    if (!overlap) return null;
    const kind = localRange.type === 'insert' && serverOp.type === 'insert'
      ? 'insert-insert' : 'edit-edit';
    const mark = { range: union(localRange, sRange), mine: localRange, theirs: sRange, kind };
    const prev = this.marks.find(m => m.range.start < mark.range.end && mark.range.start < m.range.end);
    if (prev) prev.range = union(prev.range, mark.range);   // 同区域合并
    else this.marks.push(mark);
    return mark;
  }
  resolve(mark, strategy, apply) {
    if (strategy === 'theirs-wins') { apply(mark.theirs); }
    if (strategy === 'mine-wins') { transform(mark.mine, mark.theirs); apply(mark.mine); }
    if (strategy === 'manual') { mark.state = 'manual'; return; }   // 人工 UI 处理
    this.marks = this.marks.filter(m => m !== mark);
  }
}
function opRange(op) {
  return { start: op.pos, end: op.pos + (op.type === 'insert' ? op.text.length : op.text.length), type: op.type };
}
function union(a, b) { return { start: Math.min(a.start, b.start), end: Math.max(a.end, b.end) }; }
```
