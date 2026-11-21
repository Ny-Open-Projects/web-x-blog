---
title: [V3-339] defineExpose 与泛型组件（generic）的编译产物是什么样？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-339：defineExpose 与泛型组件（generic）的编译产物是什么样？
**答**：
- `<script setup>` 的内部变量默认封闭：编译产物把 setup 返回给渲染函数的内容限制在模板用到的绑定；`defineExpose({ open, close })` 显式声明父组件通过 ref 可访问的成员。
- 产物上 defineExpose 变成 `exposed: { open, close }` 挂到实例，父组件 `comp.value.open()` 走的是 exposed 对象而非整个 setup 闭包。
- 泛型组件：`<script setup lang="ts" generic="T extends string">` 编译成 `function Component(props) {...}` 包裹一层类型参数，类型层生成 `ComponentType<T>`。
- 运行时泛型被擦除，纯类型能力；类型检查由 vue-tsc 完成，能让 `useList<T>` 组件的 props 回调拿到精确类型。
- 常见坑：expose 的是响应式值时要暴露 ref/函数而非解构值，否则拿到的是快照。
```javascript
// 泛型 Select<T> 的类型产物示意
// function Select<T>(props: { items: T[]; onChange: (v: T) => void }) {...}
```
