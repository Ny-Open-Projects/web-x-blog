---
title: [V3-010] reactive 有哪些使用限制？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-010：reactive 有哪些使用限制？
**答**：
- 解构会丢失响应式：解构出来的是普通值，必须用 toRefs 保持连接。
- 不能整体替换：`state = newState` 换掉了 Proxy 引用，视图仍监听旧代理。
- 只能代理对象类型，`reactive(1)` 无效并告警。
- 对同一对象重复 reactive 返回同一代理，代理对象再 reactive 也返回自身。

```vue
<script setup lang="ts">
import { reactive, isReactive, toRefs } from "vue";

const state = reactive({ count: 0, name: "Tom" });

// 1. 解构丢失响应式
const { count } = state; // count 是普通 number，不再触发视图更新

// 2. 不能整体替换（state 是 const 的 Proxy 引用）
// state = reactive({ count: 1 }); // 报错

// 3. 基本类型无法代理
const num = reactive(1 as any); // 开发环境警告，返回原始值
console.log(isReactive(num)); // false

// 正确做法：toRefs 解构或改用 ref
const refs = toRefs(state); // { count: Ref<number>, name: Ref<string> }
refs.count.value++; // 仍与 state.count 双向同步
</script>
```
