---
title: [V3-123] Vue3 与 TypeScript 深度配合有哪些要点？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-123：Vue3 与 TypeScript 深度配合有哪些要点？
**答**：
- 泛型组件：`generic="T"` 让 props、emit、插槽全部随实例类型流动，表格/选择器类组件必备。
- 类型提取：用 ComponentProps 等工具复用组件的 props 类型，避免双份维护。
- defineProps/defineEmits 的类型参数即文档：emit 用元组声明 payload，调用处编译期报错。
- 实用类型体操：RequiredProps（可选转必填）、Pick 子集 props、为 v-model 约定 ModelProps。

```typescript
// types/component.ts —— Vue3 + TS 实用类型工具
import type { ComponentProps } from "vue-component-type-helpers";
import type MyTable from "@/components/MyTable.vue";

// 1. 复用组件 props 类型：给包装组件转发 props 时不用手写第二份
export type TableProps = ComponentProps<typeof MyTable>;

// 2. 提取组件实例上的 emit 签名（用于封装转发事件）
export type ExtractEmits<T> = T extends { $emit: infer E } ? E : never;

// 3. 可选字段转必填：表单提交前把草稿类型收紧为完整类型
export type RequiredProps<T> = { [K in keyof T]-?: T[K] };

// 4. v-model 双绑约定类型：统一 modelValue 与对应事件签名
export type ModelProps<T> = {
  modelValue: T;
  "onUpdate:modelValue": (value: T) => void;
};

// 5. 泛型组件的 props 引用另一个泛型（配 SFC 的 generic 属性使用）：
// <script setup lang="ts" generic="T extends { id: number | string }">
// defineProps<{ rows: T[]; selected?: T }>()   // rows 与 selected 类型联动
```
