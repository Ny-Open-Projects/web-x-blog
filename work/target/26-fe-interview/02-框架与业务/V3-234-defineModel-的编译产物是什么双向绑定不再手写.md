---
title: [V3-234] defineModel 的编译产物是什么？子组件双向绑定为什么不再需要手写 prop+emit？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-234：defineModel 的编译产物是什么？子组件双向绑定为什么不再需要手写 prop+emit？
**答**：
- 编译器注入：`const model = defineModel()` 展开为 `modelValue` prop 声明 + `update:modelValue` emits 声明 + 一个内部 computed。
- 返回值是自定义 ref：读取返回 props.modelValue；写入执行 emit('update:modelValue', v) 并**本地乐观赋值**（父未同步期间子组件先显示新值，之后被父值校正）。
- 具名模型：`defineModel('title', { required: true })` 对应 `v-model:title`，编译成 title prop + update:title 事件。
- 修饰符：`defineModel({ set: (v) => v.trim() })` 或 `get/set` 转换函数在编译期包进 computed 的 get/set。
- 与旧写法对比：3.3 前要手写 `props: ['modelValue']` + emits + computed 中转三件套，defineModel 把样板收敛为一行。

```javascript
// <script setup> const model = defineModel({ type: String }) 编译产物（简化）
export default defineComponent({
  props: { modelValue: { type: String } },
  emits: ['update:modelValue'],
  setup(__props, { emit }) {
    const model = customRef((track, trigger) => ({
      get() { track(); return __props.modelValue; },
      set(v) { emit('update:modelValue', v); },
    }));
    return { model };
  },
});
// 父组件 <Child v-model="title" /> 照旧编译为 :modelValue + @update:modelValue
```
