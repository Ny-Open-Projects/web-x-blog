---
title: [V3-346] v-model 修饰符（.lazy/.number/.trim）在编译期是怎么处理的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-346：v-model 修饰符（.lazy/.number/.trim）在编译期是怎么处理的？
**答**：
- 编译期把修饰符编译进 props：`modelModifiers: { lazy: true, number: true }`，原生 input 的 v-model 展开为 value + 对应事件。
- .lazy：input 事件改 listen change（失焦才同步）；.number：赋值前 `parseFloat`（NaN 时保留原值）；.trim：`String(v).trim()`。
- 组件上的 v-model：子组件通过 `defineModel({ set: (v) => ... })` 或 props.modelModifiers 自行实现同语义。
- 编译器对「自定义修饰符」不做转换，只把修饰符对象传下去——语义完全由组件实现。
- 坑：.number 输入非数字时返回原字符串，表单层要用校验兜底；.trim 会改变用户输入的空格语义，密码类输入禁用。
```javascript
const model = defineModel({ set: (v) => Number.isNaN(+v) ? v : +v }) // 组件层实现 .number
```
