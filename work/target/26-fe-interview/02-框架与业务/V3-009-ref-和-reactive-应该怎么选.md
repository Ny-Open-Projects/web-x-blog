---
title: [V3-009] ref 和 reactive 应该怎么选？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-009：ref 和 reactive 应该怎么选？
**答**：
- 官方与社区主流推荐：默认用 ref，只对"局部成组的状态"用 reactive。
- ref 可以整体替换 `.value`、可以直接传给组合函数、类型简单。
- reactive 不能整体替换、解构丢响应式、离开 setup 作用域后引用容易失控。
- reactive 适合表单对象、批量配置这类"结构稳定、只改字段"的状态。

```vue
<script setup lang="ts">
import { ref, reactive } from "vue";

// 推荐默认用 ref：类型简单、可整体替换、可组合复用
const keyword = ref("");
const list = ref<string[]>([]);

// reactive 适合结构稳定的表单对象
const form = reactive({
  page: 1,
  size: 10,
  status: "all",
});

function reset() {
  // form = { page: 1, size: 10, status: "all" }; // 报错：不能整体替换
  Object.assign(form, { page: 1, size: 10, status: "all" });
  keyword.value = "";
  list.value = [];
}
</script>
```
