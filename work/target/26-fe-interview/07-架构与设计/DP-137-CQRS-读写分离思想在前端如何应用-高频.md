---
title: [DP-137] CQRS 读写分离思想在前端如何应用？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-137：CQRS 读写分离思想在前端如何应用？（高频）
**答**：
- CQRS：读模型（Query）与写模型（Command）分开——前端对应"展示用 selector/视图模型，变更用 command/action"，读写路径不再共用一团 state。
- 落地形态：写侧 store 只存最小事实（实体 + 变更 action），读侧用 selector 派生多视图（排序、过滤、聚合），互不污染（DP-078 reselect 即读模型）。
- 收益：读性能优化（记忆化）不影响写逻辑；写规则集中可校验；离线场景可本地写 + 远端同步。

```javascript
// 写模型：最小事实 + 变更命令（不存任何派生数据）
const createTodoStore = () => {
  let state = { todos: [] };                                  // 只有事实
  const commands = {                                          // 写侧：命令语义命名
    add: (text) => { state = { todos: [...state.todos, { id: crypto.randomUUID(), text, done: false }] }; emit(); },
    toggle: (id) => {
      state = { todos: state.todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)) };
      emit();
    },
  };
  const listeners = new Set();                                // 观察者：读模型订阅变更
  const emit = () => listeners.forEach((l) => l());
  // 读模型：selector 派生视图，记忆化避免重算
  const queries = {
    byStatus: (done) => state.todos.filter((t) => t.done === done),
    count: memoize((done) => state.todos.filter((t) => t.done === done).length),
    remaining: () => state.todos.filter((t) => !t.done).length,
  };
  const subscribe = (l) => (listeners.add(l), () => listeners.delete(l));
  return { commands, queries, subscribe };                    // 读写显式分离
};
const store = createTodoStore();
store.subscribe(() => render(store.queries.byStatus(false))); // 视图只读
store.commands.add('写周报');                                  // 用户操作走命令
```
