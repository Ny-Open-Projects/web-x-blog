---
title: [V3-227] v-model 在编译后的完整产物是什么？原生表单与组件两条路径差在哪？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-227：v-model 在编译后的完整产物是什么？原生表单与组件两条路径差在哪？
**答**：
- 组件上：`v-model="x"` 编译为 `modelValue: x` + `'onUpdate:modelValue': $event => x = $event`，本质是 prop + 事件糖。
- 原生 input：编译为 `modelValue` 特殊处理——直接生成 `value: x` + `onInput`/`onChange` 绑定，并按修饰符注入转换函数。
- 修饰符编译：`.lazy`→input 改 change；`.number`→编译注入 `_n($event.target.value)`；`.trim`→`_s($event.target.value)`，全部是编译期函数包装。
- 与 defineModel 的关系：子组件用 defineModel 时，编译器帮子组件声明 modelValue prop 并在赋值时 emit update:modelValue，省掉手写双声明。
- 追问钩子：多 v-model 即多组 modelValue/事件对；动态参数 `v-model:[name]` 编译为动态 prop 键与事件键。

```javascript
// 原生：<input v-model.trim.number="age" />
// 编译产物
createElementVNode("input", {
  value: age,
  onInput: ($event) => { age = _n(_s($event.target.value)) },
});
// 组件：<Child v-model="title" v-model:subtitle="sub" />
createVNode(Child, {
  modelValue: title,
  'onUpdate:modelValue': ($event) => (title = $event),
  subtitle: sub,
  'onUpdate:subtitle': ($event) => (sub = $event),
});
// 子组件 defineModel 编译产物（示意）：
// props: { modelValue: null }, emits: ['update:modelValue']
// 赋值 model.value = v → emit('update:modelValue', v)
```
