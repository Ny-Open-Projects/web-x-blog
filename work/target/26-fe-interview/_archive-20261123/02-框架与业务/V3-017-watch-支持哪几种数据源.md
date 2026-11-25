---
title: [V3-017] watch 支持哪几种数据源？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-017：watch 支持哪几种数据源？
**答**：
- 单个 ref、reactive 对象、getter 函数、以及它们组成的数组（多源）。
- reactive 对象隐式深度监听；ref 包对象默认只监听 .value 替换，深监听需 deep: true。
- 多源时回调的新旧值也是按位置对应的数组。
- getter 函数是最灵活的形式，可以监听组合状态。

```vue
<script setup lang="ts">
import { ref, reactive, watch } from "vue";

const count = ref(0);
const state = reactive({ user: { name: "Tom" } });

// 单个 ref
watch(count, (val, oldVal) => console.log(val, oldVal));

// getter 函数
watch(() => state.user.name, (name) => console.log(name));

// reactive 对象：隐式深度监听
watch(state, () => console.log("state changed"));

// 多源：数组形式，回调参数也是按位对应的数组
watch([count, () => state.user.name], ([c, n], [pc, pn]) => {
  console.log(c, n, pc, pn);
});
</script>
```
