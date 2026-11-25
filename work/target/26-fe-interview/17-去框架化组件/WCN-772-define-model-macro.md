---
title: [WCN-772] 如何实现 defineModel 风格的双向绑定编译宏？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-772：如何实现 defineModel 风格的双向绑定编译宏？

**答**：
- 结论：defineModel() 是编译宏，编译期把 `const model = defineModel()` 转换为 `props.modelValue` 读取 + `emit('update:modelValue', val)` 写入；返回一个可写的 ref/computed。
- 宏在编译期展开并擦除，运行时不存在；支持参数 `defineModel('title')` → `title` prop 与 `update:title` 事件；类型信息从泛型推导。
- 追问钩子：多个 defineModel 同时用如何避免 emit 名冲突？考察「按参数名生成独立 update 事件」。

```javascript
// 源码：const count = defineModel()
// 编译展开为：
function setup(props, { emit }) {
  const count = {
    get value() { return props.modelValue; },
    set value(v) { emit('update:modelValue', v); },
  };
  return { count };
}
// 带参数：defineModel('title')
function setup2(props, { emit }) {
  return { title: {
    get value() { return props.title; },
    set value(v) { emit('update:title', v); },
  } };
}
console.log('defineModel 是零运行时开销的编译宏');
```
