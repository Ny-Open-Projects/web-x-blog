---
title: [V3-354] defineModel 与 TS 泛型组件的组合实践是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-354：defineModel 与 TS 泛型组件的组合实践是什么？
**答**：
- 泛型选择器：`generic="T extends { id: number }"` + `const value = defineModel<T>()`，父组件使用时 value 类型自动推断为 T，回调 onChange(v: T) 精确。
- defineModel 的 get/set 转换器也可以用泛型：get 把服务端值转本地形态、set 转回去，类型保持双向一致。
- 与 defineSlots 组合：作用域插槽参数 `item: T`，整个组件（数据、值、插槽）类型贯通。
- 限制：泛型仅在 vue-tsc 下生效，运行时擦除；模板内类型推断依赖准确的 props 声明，不要用 any 兜底。
- 典型落地：AutoComplete<T>、Cascader<T>、DataTable<T> 三类高频泛型组件。
```javascript
// <script setup lang="ts" generic="T extends { id: number; label: string }">
const value = defineModel<T>({ required: true })
const emit = defineEmits<{ select: [item: T] }>()
```
