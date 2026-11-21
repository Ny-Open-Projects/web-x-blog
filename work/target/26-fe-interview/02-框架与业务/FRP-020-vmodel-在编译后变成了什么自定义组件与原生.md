---
title: [FRP-020] v-model 在编译后变成了什么？自定义组件与原生表单有何差异？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-020：v-model 在编译后变成了什么？自定义组件与原生表单有何差异？

**答**：
- 组件上的 `v-model="x"` 编译为两条指令：`:modelValue="x"` + `@update:modelValue="x = $event"`——本质是"prop 下行 + 事件上行"的语法糖。
- 原生表单元素是特化处理：input 编译为 `:value` + `@input`，checkbox/radio 是 `:checked` + `@change`，select 是 `:value` + `@change`。
- 修饰符编译为运行时辅助：`.trim`/`.number` 是对事件 payload 的预处理；`.lazy` 把 input 事件换成 change。
- 参数形式 `v-model:title` 生成 `title` prop 与 `update:title` 事件，一个组件可有多组。

```vue
<!-- 一一对应：v-model 与其等价展开 -->
<!-- 写法一：v-model 语法糖 -->
<template>
  <input v-model.trim="message" />
  <MyInput v-model:title="title" v-model:index="idx" />
</template>

<!-- 写法二：编译后的等价写法（完全等价） -->
<template>
  <input :value="message" @input="message = $event.target.value.trim()" />
  <MyInput :title="title" @update:title="title = $event" :index="idx" @update:index="idx = $event" />
</template>

<script setup>
import { ref } from 'vue';
const message = ref('');
const title = ref('');
const idx = ref(0);
</script>
```

```javascript
// 简化实现，帮助理解编译产物：normalizeModel 的运行时逻辑
function resolveModelDirective(modifiers) {
  const { trim, number, lazy } = modifiers;
  const event = lazy ? 'change' : 'input'; // .lazy 换事件
  return {
    mounted(el, { value }) { el.value = value; },
    // 运行时监听：把 DOM 事件翻译成 update:modelValue 事件
    created(el, { modifiers: m }, vnode) {
      el.addEventListener(event, (e) => {
        let val = e.target.value;
        if (m.number) val = val === '' ? '' : Number(val);  // .number 预处理
        if (m.trim) val = val.trim();                       // .trim 预处理
        // 触发组件更新事件，父组件的 x = $event 得以执行
        vnode.props[`onUpdate:${m.modelKey || 'modelValue'}`]?.(val);
      });
    },
  };
}
```
