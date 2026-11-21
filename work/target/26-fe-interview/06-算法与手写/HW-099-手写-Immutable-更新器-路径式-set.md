---
title: [HW-099] 手写路径式不可变更新——setIn/getIn/updateIn，共享未变更引用（结构共享）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：Redux 式不可变更新的核心是**结构共享**：只沿路径克隆，路径外的兄弟节点保持原引用（React.memo/shouldComponentUpdate 依赖引用相等才有效）。实现递归：浅拷贝当前层，只替换目标键的克隆结果。

```javascript
const isObj = (v) => v && typeof v === 'object';
function setIn(obj, path, value) {
  if (!path.length) return value;
  const [head, ...rest] = path;
  const clone = Array.isArray(obj) ? obj.slice() : { ...obj };   // 浅拷贝当前层
  clone[head] = setIn(clone[head], rest, value);                 // 只递归目标分支
  return clone;
}
function getIn(obj, path) {
  return path.reduce((o, k) => (o == null ? o : o[k]), obj);
}
function updateIn(obj, path, updater) {
  return setIn(obj, path, updater(getIn(obj, path)));
}
// 结构共享验证：
const state = { a: { b: { c: 1 } }, d: { e: 2 } };
const next = setIn(state, ['a', 'b', 'c'], 9);
// next.a !== state.a（变更路径已克隆）；next.d === state.d（兄弟分支共享原引用）✔
// next.a.b !== state.a.b（中间层也克隆）；next.a.b.c === 9
// updateIn(state, ['a', 'b', 'c'], (v) => v + 1) 等价糖
// 数组路径：setIn(state, ['list', 2, 'done'], true) —— slice 浅拷贝数组后同样共享
```

**评分点**：
- 结构共享验证点说清：变更路径克隆、兄弟分支引用不变（这是性能与 React 更新的关键）。
- 数组与对象双路径支持；中间层逐层克隆。
- getIn 对 null 中间层的容错。
- 能对比 Immer（proxy 写时复制）与手写 setIn 的取舍。
