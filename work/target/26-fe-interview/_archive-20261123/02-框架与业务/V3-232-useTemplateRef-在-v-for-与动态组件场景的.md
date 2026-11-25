---
title: [V3-232] useTemplateRef 在 v-for 与动态组件场景怎么用？有什么坑？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-232：useTemplateRef 在 v-for 与动态组件场景怎么用？有什么坑？
**答**：
- v-for 内 ref：同一 ref 名出现在列表里，`useTemplateRef` 得到的是**数组**（按挂载顺序），元素增删后数组会同步但顺序不保证与数据一致，需要时在元素上用 `:ref` 函数写 map。
- 动态组件：`<component :is="x" ref="cmp">` 切换后 `cmp.value` 指向新实例；拿方法前要判空且注意异步组件未加载完成时为 null。
- 函数 ref 混用：`:ref="(el) => items.set(i, el)"` 时 el 在卸载时回调 null，map 要做清理，否则泄漏。
- 常见坑：把 useTemplateRef 的参数写成变量而非字面量——编译器要靠**字面量字符串**做类型推导，动态拼名字拿不到类型。
- 时机坑：setup 同步阶段 ref 还是 null，要在 onMounted 或 watch(target) 后访问。

```vue
<script setup>
import { useTemplateRef, onMounted, ref, watch } from 'vue';
const rowRefs = useTemplateRef('rows');        // 数组
const itemMap = ref(new Map());
const Comp = ref(null);
watch(rowRefs, (els) => console.log('列表 ref 变化', els?.length)); // 3.5 后 ref 数组可 watch
onMounted(() => itemMap.value.get(1)?.highlight());
</script>
<template>
  <li v-for="i in 5" :key="i" ref="rows">{{ i }}</li>
  <div v-for="i in 5" :key="'m' + i" :ref="(el) => el ? itemMap.set(i, el) : itemMap.delete(i)"></div>
  <component :is="Comp" ref="cmp" />
</template>
```
