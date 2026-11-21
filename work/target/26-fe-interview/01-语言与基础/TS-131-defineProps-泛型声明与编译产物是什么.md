---
title: [TS-131] defineProps 泛型声明与编译产物是什么关系？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-131：defineProps 泛型声明与编译产物是什么关系？
**答**：
- `<script setup>` 里给 defineProps 传"纯类型参数"，Vue 编译器在编译期把类型反向生成为运行时 props 声明，类型与运行时校验单一来源。
- withDefaults 给可选 prop 补默认值，同时收窄类型（去掉 undefined）。
- 限制：编译器只能识别简单类型（String/Number/Boolean/Array/Object/Function），复杂自定义类型运行时会退化为 Object/Function。

```typescript
// UserCard.vue
// <script setup lang="ts">
interface Props {
  title: string;   // 必填 string
  items: string[]; // 必填数组
  count?: number;  // 可选 number
}
const props = withDefaults(defineProps<Props>(), { count: 0 });
console.log(props.title, props.count);

// Vue 编译器生成的运行时声明（等价产物）：
// props: {
//   title: { type: String, required: true },
//   items: { type: Array, required: true },
//   count: { type: Number, required: false, default: 0 }
// }

// 坑：interface 里写 class 实例、函数精确签名时，
// 运行时只能得到 Object/Function 宽类型，精确校验需运行时声明 + PropType（TS-133）
```
