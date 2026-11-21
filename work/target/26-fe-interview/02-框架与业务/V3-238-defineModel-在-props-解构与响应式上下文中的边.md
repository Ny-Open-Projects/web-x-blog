---
title: [V3-238] defineModel 与 3.5 响应式 props 解构如何配合？有哪些边界问题？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-238：defineModel 与 3.5 响应式 props 解构如何配合？有哪些边界问题？
**答**：
- 3.5 的 props 解构：`const { msg = 'hi' } = defineProps<{ msg?: string }>()` 默认值合法且解构变量**保持响应式**（编译器转为访问 props.msg）。
- 与 defineModel 关系：defineModel 返回的是 ref 不是 prop，解构 `.value` 会丢响应式；要传给模板/子组件必须保留整个 ref。
- 边界 1：解构后再传给 watch——响应式解构变量可以直接作为 watch 源（编译器保证），普通变量解构（如 from ref.value）不行。
- 边界 2：`defineModel` + `defineProps` 同名冲突报编译错误：modelValue 既是 props 声明又是模型，只能二选一。
- 排查工具：报错信息带宏名与位置，Volar/oxc 插件会实时标红，先查同名声明与非法解构位置。

```vue
<script setup lang="ts">
// OK：响应式解构 + 默认值（3.5 稳定）
const { msg = 'hello', count = 0 } = defineProps<{ msg?: string; count?: number }>();
// OK：模型 ref 保持完整引用
const model = defineModel<string>('modelValue');
// 错误示例 1：解构 ref 丢响应式
// const { value: bad } = model;         // ❌ 只拿到当前值
// 错误示例 2：同名冲突
// const m = defineModel<string>(); const { modelValue } = defineProps<{ modelValue: string }>(); // ❌
// 正确把模型值给非响应式上下文（如事件回调）：
const onClick = () => submit(model.value); // 调用时读 .value，OK
</script>
```
