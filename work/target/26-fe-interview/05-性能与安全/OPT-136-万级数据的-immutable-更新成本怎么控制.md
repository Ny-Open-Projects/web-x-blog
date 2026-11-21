---
title: [OPT-136] 万级数据的 immutable 更新成本怎么控制？结构共享/Immer 收益在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-136：万级数据的 immutable 更新成本怎么控制？结构共享/Immer 收益在哪？

**答**：
- 浅拷贝一份 10 万条数组是 O(n) 的内存与 CPU 消耗；深拷贝更糟。Immutable 的核心收益是**结构共享**：修改只新建"从根到被改节点"的路径，其余节点引用复用。
- Immer 用 Proxy 写出"可变代码"，内部只复制被修改路径（copy-on-write），未变子树 `===` 相等——React.memo/依赖数组因此大量跳过重渲染。
- 不上库的轻量版：更新单条时只复制外层数组 + 该条对象，其余引用不变，配合 memo 就能避免全列表 diff。
- 注意：Proxy 包装本身有开销，高频小更新（动画值/输入框）不要走 Immer，保持原生 setState 即可。

```javascript
// 一一对应：结构共享验证——修改一条，其余引用 === 复用（Immer 与手写对照）
const { produce } = require('immer');

const users = Array.from({ length: 100000 }, (_, i) => ({ id: i, name: `u${i}`, score: 0 }));

// 方案A Immer：Proxy copy-on-write
const next1 = produce(users, draft => { draft[3].score = 100; });
console.log('immer:', next1 === users, next1[0] === users[0], next1[3] === users[3]);
// => false true false —— 外层换了、未改节点全复用

// 方案B 手写最小结构共享：无 Proxy 开销，更适热路径
function updateUser(list, id, patch) {
  return list.map(u => (u.id === id ? { ...u, ...patch } : u)); // 未命中项返回原引用
}
const next2 = updateUser(users, 3, { score: 100 });
console.log('manual:', next2 === users, next2[0] === users[0], next2[3] === users[3]);
// => false true false —— React.memo 比较时 99999 条直接跳过

// 配套：列表行组件 memo 后 diff 成本从 O(n) 降到 O(1)
// const Row = React.memo(({ user }) => <li>{user.name}</li>);
```
