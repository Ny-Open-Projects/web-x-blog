---
title: [ZSM-018] Zustand selector 返回数组/Map/Set 这类新引用怎么办？浅比较够用吗？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-018：Zustand selector 返回数组/Map/Set 这类新引用怎么办？浅比较够用吗？
**答**：
- 数组：selector 内 filter/map 每次返回新数组，浅比较按元素逐个 Object.is，元素是原始值时够用；元素是对象且每次重建则仍会渲染。
- 对象元素：应让 store 里存的对象在 set 时保持引用稳定（不可变更新只在变化时新建），或 selector 只挑出原始值字段。
- Map/Set：Object.is 只比引用，内容相同的不同实例永远不相等，浅比较也失效；要么引用复用，要么用 subscribeWithSelector 自己写比较器（第四参 equalityFn）。
- 兜底：`useStore(selector, customEqual)`（旧版）或自定义比较函数做深比较/字段比较，代价是每次变更都要跑比较器。

```javascript
// 深比较兜底：比较 Map 的内容
const isEqual = (a, b) =>
  a.size === b.size && [...a.entries()].every(([k, v]) => b.get(k) === v)

const big = useStore(
  s => new Map(s.items.map(i => [i.id, i])),
  isEqual, // 自定义 equalityFn，替换默认 Object.is
)
```
