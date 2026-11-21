---
title: [R19-128] immer 的结构共享对 React 性能意味着什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-128：immer 的结构共享对 React 性能意味着什么？
**答**：
- produce 只复制被修改路径上的节点，未改动子树的引用保持不变。
- 这正是 React 浅比较（memo、依赖数组）能生效的前提：改一个深层字段，兄弟节点的 memo 不失效。
- 复杂嵌套 reducer 用 produce 替代层层展开（...state, a: {...state.a, b: ...}），可读性与正确性双提升。
- 注意：immer 返回新引用的成本与修改路径成正比，超大数据集（上万条）要配合分页/虚拟化。

```jsx
// immer 结构共享：改哪里只复制哪里，未改动的引用保持不变
import { produce } from 'immer';

const baseState = [
  { id: 1, name: 'a', tags: ['x'] },
  { id: 2, name: 'b', tags: ['y'] },
];

const nextState = produce(baseState, draft => {
  draft[1].name = 'B';      // 直接改 draft，immer 负责生成新树
});
// baseState === nextState        false —— 顶层引用变了，React 会重渲染
// baseState[0] === nextState[0]  true  —— 结构共享，Row 的 memo 依旧跳过
// baseState[1] === nextState[1]  false —— 只有改动路径被复制

// React 中的实战：复杂嵌套 reducer 用 produce 替代层层展开
function todosReducer(state, action) {
  switch (action.type) {
    case 'renameTag':
      return produce(state, draft => {
        draft.byId[action.id].tags = draft.byId[action.id].tags.map(
          t => (t === action.old ? action.next : t),
        );
      });
    default:
      return state;
  }
}
```
