---
title: [V3-315] Vapor 的 createFor 如何做列表更新与 key 管理？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-315：Vapor 的 createFor 如何做列表更新与 key 管理？
**答**：
- `v-for` 编译成 `createFor(source, renderItem, getKey)`：source 是响应式列表，renderItem 为每项生成独立 DOM 块。
- key 存在时内部维护 key→block 的映射表：新增项只 renderItem 并插入，删除项直接 remove + 停止其作用域，没有「双端比较/LIS」那套 diff。
- 顺序变化用 DOM `insertBefore` 按新顺序重排已有块，块的子 effect 不重建——比 VDOM diff 少一层 vnode 对象。
- 无 key 时退化为按索引复用，动态点表达式重新求值，行为与 Vue3 VDOM 的「原地复用」一致。
- 注意：renderItem 里如果读取了列表外的响应式数据，需要作用域保证单项 block 可独立重渲染或整体重算，编译器会区分「项内依赖」与「外部依赖」。
```javascript
createFor(list, (item) => {
  const li = _template('<li> </li>')()
  _setText(li.firstChild, () => item.name)
  return li
}, (item) => item.id)
```
