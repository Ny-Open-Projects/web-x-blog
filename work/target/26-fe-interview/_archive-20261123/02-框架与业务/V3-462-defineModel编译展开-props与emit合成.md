---
title: [V3-462] defineModel 编译展开：props/emit 的宏合成
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-462：defineModel 编译展开：props/emit 的宏合成

**答**：
- defineModel 是 3.4+ 的编译宏：编译展开为「modelValue prop 声明 + emit('update:modelValue') + 本地代理 ref」三件套——宏在编译期消费，运行时不存在 defineModel 函数
- 本地 ref 的实现：返回一个 customRef——读时返回 modelValue prop，写时同时更新本地值 + emit 事件（乐观本地更新，防父组件未同步时的闪烁）
- 带 name 参数：`const title = defineModel('title')` 编译为 title prop + update:title 事件——多 v-model 支持与 v-model:title 使用对应
- 修饰符：`defineModel('title', { get/set 转换 })` 与 v-model 修饰符（.trim/.lazy）自动联动——lazy 的实现是本地 ref 的事件时机变化
- 与手写 props+emit 的差异：defineModel 的本地代理让「子组件内部立即生效再通知父级」，手写方案必须等父组件回传——交互延迟的隐藏差异

```vue
<script setup>
const title = defineModel('title', { default: '' });
title.value = 'x';    // 本地立即生效 + emit('update:title', 'x')
</script>
<!-- 编译展开 ≈ -->
<!-- props: { title: { default: '' } }, emits: ['update:title'],
     内部: customRef(read: () => props.title, write: v => { local = v; emit(...) }) -->
```
