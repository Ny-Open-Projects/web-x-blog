---
title: [V3-029] provide/inject 如何做到类型安全？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-029：provide/inject 如何做到类型安全？
**答**：
- 直接用字符串 key 没有类型推导，推荐用 `InjectionKey<T>` 类型的 Symbol key。
- provide 端与 inject 端共享同一个 key 常量，注入值的类型自动推导。
- inject 可传默认值兜底；没有默认值且未注入时得到 undefined。
- 适合主题、用户信息、SDK 实例等跨层级只读或受控写入的数据。

```vue
<!-- Provider.vue（祖先组件） -->
<script setup lang="ts">
import { provide, ref } from "vue";
import type { InjectionKey, Ref } from "vue";

// 用 Symbol key + 类型标注，注入端获得完整类型推导
const ThemeKey: InjectionKey<Ref<"light" | "dark">> = Symbol("theme");

const theme = ref<"light" | "dark">("dark");
provide(ThemeKey, theme); // 后代任意层级可注入

// 后代组件中：
// const theme = inject(ThemeKey, ref("light")); // 类型自动为 Ref<"light" | "dark">
</script>

<template>
  <p>当前主题 {{ theme }}</p>
</template>
```
