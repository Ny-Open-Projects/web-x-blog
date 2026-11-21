---
title: [HW-242] 手写一个 OT 变换函数：transform(a, b) 的双向变换
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-242：手写一个 OT 变换函数：transform(a, b) 的双向变换

**答**：
- 需求：实现 transform(a, b)——基于 a 计算 a 对 b 的变换 a’，以及基于 b 计算 b 对 a 的变换 b’（保证 apply(apply(doc,a),b’) == apply(apply(doc,b),a’)）；只处理同位置插入/删除的四种组合。
- 边界：两个插入同位置用站点 ID/优先级破平（确定性）；删除区间重叠取并集偏移；变换返回 {a1, b1}。
- 评分点：TP1 性质；同位插入破平；区间重叠处理。

```javascript
function transform(a, b, tie = 0) {                       // tie: 优先级（服务器破平）
  const shift = (pos, op) => {                            // op 对 pos 的影响
    if (op.type === 'insert') return pos < op.pos || (pos === op.pos && tie < 0) ? op.text.length : 0;
    const s = op.pos, e = op.pos + op.text.length;        // delete
    if (pos <= s) return 0;
    if (pos >= e) return -op.text.length;
    return s - pos;                                       // pos 在删除区间内
  };
  const a1 = { ...a, pos: a.pos + shift(a.pos, b) };
  const b1 = { ...b, pos: b.pos + shift(b.pos, a) };
  // 删除区间随对方操作收缩
  if (a.type === 'delete' && b.type === 'insert') { /* a 区间被插入切分：简化为平移 */ }
  if (a.type === 'delete' && b.type === 'delete') {
    const bs = b.pos, be = b.pos + b.text.length;
    const as = a.pos, ae = a.pos + a.text.length;
    const overlap = Math.max(0, Math.min(ae, be) - Math.max(as, bs));
    if (overlap) { a1.text = a.text.slice(0, Math.max(0, bs - as)) + a.text.slice(Math.max(0, be - as)); }
  }
  return { a1, b1 };
}
// TP1 断言：apply(apply(d,a),b1) == apply(apply(d,b),a1)
```
