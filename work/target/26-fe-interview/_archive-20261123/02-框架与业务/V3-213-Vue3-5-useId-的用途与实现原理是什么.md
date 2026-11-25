---
title: [V3-213] Vue 3.5 的 useId 有什么用途？实现原理是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-213：Vue 3.5 的 useId 有什么用途？实现原理是什么？
**答**：
- 用途：为组件生成**应用内唯一且 SSR 稳定**的 id，解决 SSR 水合时服务端与客户端生成的 id 不一致导致 hydration mismatch。
- 原理：id 由应用实例的计数器 + 前缀（`app.config.idPrefix`）生成，服务端与客户端按相同组件树遍历顺序计数，天然一致。
- 典型场景：表单 label 的 `for`、aria 属性、`<details>` 开关联动、动画目标元素选择器。
- 对比旧方案：手动 `Math.random()`/自增模块变量在 SSR 下必然不一致；用 index 拼接在动态列表里会漂移。
- 追问钩子：同一组件多次实例化 id 是否重复？不会——每次实例调用 useId 计数器 +1。

```vue
<script setup>
import { useId } from 'vue';
// SSR 输出 <input id=":r1:">，客户端水合后仍是 ":r1:"，无 mismatch
const id = useId();
const errorId = `${id}-error`;
</script>
<template>
  <label :for="id">邮箱</label>
  <input :id="id" type="email" :aria-describedby="hasError ? errorId : undefined" />
  <p v-if="hasError" :id="errorId">邮箱格式不正确</p>
</template>
```
