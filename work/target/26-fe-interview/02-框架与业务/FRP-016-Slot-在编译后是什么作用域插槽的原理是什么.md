---
title: [FRP-016] Slot 在编译后是什么？作用域插槽的原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-016：Slot 在编译后是什么？作用域插槽的原理是什么？

**答**：
- 默认插槽：父组件模板中的插槽内容被编译成**子组件 vnode 的 children**，子组件 `<slot>` 出口就是渲染这段 children（渲染发生在父组件作用域）。
- 作用域插槽：内容编译成一个**返回 vnode 的函数** `(slotProps) => vnode`，作为 props 传给子组件；子组件渲染时**调用该函数并传参**——数据在子组件产生，但 vnode 依然由父组件作用域闭包创建。
- 这就是"数据源是子组件、渲染权在父组件"的实现；`v-slot="slotProps"` 就是函数参数。
- Vue3 统一了普通与作用域插槽：普通插槽也是函数（惰性求值），避免 Vue2 中普通插槽在父渲染时就求值的差异。

```vue
<!-- 一一对应：作用域插槽的编译产物还原 -->
<!-- 父组件 -->
<template>
  <List :items="rows">
    <template #item="{ item, index }">
      <li>{{ index }}. {{ item.name }}</li>
    </template>
  </List>
</template>
<script setup>
import { ref } from 'vue';
const rows = ref([{ name: 'a' }, { name: 'b' }]);
</script>

<!-- 子组件 List：slot 出口调用父传来的函数并传参 -->
<template>
  <ul><slot v-for="(item, index) in items" :key="index" :item="item" :index="index" /></ul>
</template>
<script setup>
defineProps({ items: Array });
</script>
```

```javascript
// 简化实现，帮助理解：插槽编译后就是 props 上的函数
// 父组件编译产物（近似）：
function parentRender() {
  const rows = [{ name: 'a' }, { name: 'b' }];
  return h(List, { items: rows }, {
    // 具名插槽编译为函数：参数由子组件调用时传入，闭包仍是父作用域
    item: ({ item, index }) => h('li', null, `${index}. ${item.name}`),
  });
}

// 子组件内部渲染插槽出口（近似）：
function renderSlots(instance) {
  const slotFn = instance.slots.item;              // 拿到父传来的函数
  instance.props.items.forEach((item, index) => {
    const vnode = slotFn({ item, index });         // 子组件传参调用 —— 作用域插槽的本质
    mount(vnode, instance.subTree.el);
  });
}
```

## 三、Vue 特色组件机制
