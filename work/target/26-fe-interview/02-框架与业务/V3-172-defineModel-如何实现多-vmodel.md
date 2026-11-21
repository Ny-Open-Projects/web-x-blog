---
title: [V3-172] defineModel 如何实现多 v-model 与修饰符？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-172：defineModel 如何实现多 v-model 与修饰符？
**答**：
- defineModel 在 3.4 转正：子组件内部读写 model.value，自动生成对应 props/emit，不再手写 update:modelValue。
- 多 v-model：每个 defineModel 用不同名（title、content），模板里 `v-model:title="t"` 一一对应。
- 修饰符：通过 defineModel 的第二个参数拿到 modifiers（如 trim、自定义 capitalize），在 set 前做转换。
- 注意：3.4 之前需手写 props + emit；defineModel 返回的是自定义 ref，父组件不传时仍有本地值可用（配合默认值）。

```vue
<!-- components/RichInput.vue —— 双 v-model + trim 修饰符 -->
<script setup lang="ts">
// 多 v-model：title 与 content 各自独立，互不干扰
const title = defineModel<string>("title", { required: true });
const content = defineModel<string>("content", { default: "" });

// 捕获 v-model.trim 这类修饰符
const [rawTitle, titleModifiers] = defineModel<string>("rawTitle", {
  set(v) {
    // set 钩子：写入前转换（这里实现 .trim 语义）
    if (titleModifiers.trim) return v.trim();
    return v;
  },
});
const raw = rawTitle; // 重命名避免与上方冲突，读写走 raw
</script>

<template>
  <input v-model="title" placeholder="标题" />
  <textarea v-model="content" placeholder="内容" />
  <input v-model.trim="raw" placeholder="自动去首尾空格" />
  <p>父组件同步：{{ title }} / {{ content }} / {{ raw }}</p>
</template>

<!-- 父组件使用：
     <RichInput v-model:title="t" v-model:content="c" v-model.trim:rawTitle="r" />
     等价于 3.4 之前的手写版：
     :title="t" @update:title="t = $event" -->
```
