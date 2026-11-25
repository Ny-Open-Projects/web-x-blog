---
title: [924] 笔试手写：实现 replaceEqualDeep 结构共享
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 笔试题, TanStack Query, 手写]
type: 笔试题
---

## 924：笔试手写：实现 replaceEqualDeep 结构共享

**答**：实现 replaceEqualDeep(prev, next)：递归比较，深相等时返回 prev 引用（引用稳定）；对象/数组部分变更时「未变字段保留旧引用，变更字段用新值」；长度/键集合不等直接返回新值。

```js
function replaceEqualDeep(prev, next) {
  if (prev === next) return prev;
  if (typeof prev !== 'object' || typeof next !== 'object' ||
      prev === null || next === null) return next;
  if (Array.isArray(prev) !== Array.isArray(next)) return next;
  if (Array.isArray(prev)) {
    if (prev.length !== next.length) return next;
    let same = true; const out = new Array(prev.length);
    for (let i = 0; i < prev.length; i++) {
      out[i] = replaceEqualDeep(prev[i], next[i]);
      if (out[i] !== prev[i]) same = false;
    }
    return same ? prev : out;                    // 全等返回旧引用
  }
  const pk = Object.keys(prev), nk = Object.keys(next);
  if (pk.length !== nk.length) return next;
  let same = true; const out = {};
  for (const k of pk) {
    if (!(k in next)) return next;
    out[k] = replaceEqualDeep(prev[k], next[k]);
    if (out[k] !== prev[k]) same = false;
  }
  return same ? prev : out;
}
const prev = { a: 1, list: [{ id: 1, x: 1 }, { id: 2, x: 2 }] };
const next = { a: 1, list: [{ id: 1, x: 1 }, { id: 2, x: 3 }] };
const r = replaceEqualDeep(prev, next);
console.log(r.list[0] === prev.list[0]);   // true：未变项引用保留
console.log(r.list[1] === prev.list[1]);   // false：变更项用新值
```

**评分点**：
- 深相等返回旧引用（引用稳定核心语义）
- 部分变更时逐字段递归保留旧引用
- 数组长度/键集合不等短路返回新值
- 能讨论：React.memo 配合价值（未变子树不重渲染）、循环引用防护

