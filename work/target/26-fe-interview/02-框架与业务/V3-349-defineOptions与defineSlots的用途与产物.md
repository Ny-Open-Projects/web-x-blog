---
title: [V3-349] defineOptions 与 defineSlots 的用途和产物是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-349：defineOptions 与 defineSlots 的用途和产物是什么？
**答**：
- defineOptions：在 `<script setup>` 中直接声明 name/inheritAttrs 等组件选项——以前要额外开普通 `<script>` 块写 `export default { name }`。
- defineSlots：纯类型宏，声明插槽签名 `defineSlots<{ default(props: { item: T }): any }>()`，让父组件使用作用域插槽时获得参数类型；运行时产物为空。
- 编译产物：defineOptions 合并进导出对象；defineSlots 擦除，仅 vue-tsc 消费。
- 组合应用：组件库导出 name（KeepAlive include 需要）+ 插槽类型（TS 工厂生成文档）。
- 注意 defineOptions 里不能重复声明 setup 相关宏已生成的选项（props/emits），会编译报错。
```javascript
defineOptions({ name: 'MyDialog', inheritAttrs: false })
defineSlots<{ footer(): any; default(props: { close: () => void }): any }>()
```
