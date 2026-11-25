---
title: [WCN-127] Vue Vapor 编译产物的结构与运行时助手有哪些？v-if/v-for 编译成什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-127：Vue Vapor 编译产物的结构与运行时助手有哪些？

**答**：
- 产物结构：`setup()` 返回一个匿名函数（或直接副作用块），内部是"创建 DOM + 注册 renderEffect"的命令式代码；不再返回 vnode 树。
- 核心 runtime helper：`template()`（静态骨架克隆）、`renderEffect(fn)`（绑定更新）、`setText/setClass/setProp`（定向更新）、`createIf`（分支容器）、`createFor`（keyed 列表）、`createSlot`（插槽桥接）。
- v-if → `createIf(() => cond.value, () => 分支渲染函数)`：条件变化只切换分支内容；v-for → `createFor(source, renderItem, keyFn)`：增量增删移。
- 事件：`on(el, 'click', handler)` 直接 addEventListener，无合成事件层。
- 与 vdom 模式共存：同一 runtime 里 vapor 组件与 vdom 组件可以互相嵌套（通过 bridge helper），允许按页面渐进迁移。

```vue
<!-- Vapor 模板 -->
<template>
  <div v-if="show">{{ msg }}</div>
  <ul><li v-for="it in list" :key="it.id">{{ it.name }}</li></ul>
</template>
```

```javascript
// 编译产物（示意）
const t0 = template('<div></div>');
const t1 = template('<ul><li></li></ul>');
setup(() => {
  const ifBlock = createIf(() => show.value, () => {
    const el = t0();
    renderEffect(() => setText(el, msg.value));
    return el;
  });
  const forBlock = createFor(() => list.value, (it) => {
    const li = t1().firstChild;
    renderEffect(() => setText(li, it.name));
    return li;
  }, (it) => it.id);
});
```
