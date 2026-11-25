---
title: [V3-011] toRef 和 toRefs 的作用与区别是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-011：toRef 和 toRefs 的作用与区别是什么？
**答**：
- toRef 为响应式对象的单个属性创建 ref，读写与源属性双向同步。
- toRefs 把整个 reactive 对象转换成 ref 集合，常用于解构 props 或 setup 返回值。
- 源对象上不存在的属性，toRef 创建的 ref 也能保持联动（后续赋值会同步）。
- 它们解决的核心问题：解构/展开 reactive 对象时保持响应式。

```vue
<script setup lang="ts">
import { reactive, toRef, toRefs } from "vue";

const state = reactive({ name: "Tom", age: 18 });

// toRef：为单个属性创建 ref，与源属性双向同步
const nameRef = toRef(state, "name");
nameRef.value = "Jerry"; // state.name 同步变为 "Jerry"
state.age = 20; // 不影响 nameRef

// toRefs：把整个对象转成 ref 集合，常用于解构 props
function useFeature(props: { name: string; age: number }) {
  const { name, age } = toRefs(props); // 保持响应式的解构
  return { name, age };
}
</script>
```
