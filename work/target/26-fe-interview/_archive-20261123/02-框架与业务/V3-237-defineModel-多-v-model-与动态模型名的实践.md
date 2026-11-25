---
title: [V3-237] defineModel 多模型与动态模型名（v-model:[arg]）怎么实践？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-237：defineModel 多模型与动态模型名（v-model:[arg]）怎么实践？
**答**：
- 多模型：一个组件可多次 `defineModel('start')` / `defineModel('end')`，各自独立 prop+emit，日期范围选择器是典型。
- 动态模型名：模板 `v-model:[field]="value"` 编译为动态 prop 键；defineModel 对动态名只能声明一个"默认模型"，动态字段建议封装到 props/emit 层而非依赖 defineModel。
- 组合实践：范围选择器内部把 start/end 定义为两个模型，暴露 `range` computed 给父层做整体读写，兼顾双向便利与整体校验。
- 类型：`defineModel<string[]>('tags', { default: () => [] })`——对象默认值必须用工厂函数，避免多实例共享引用。
- 坑：多模型时父组件漏传某个具名模型不报错但写入丢失，开发环境加 required: true 兜底。

```vue
<script setup>
const start = defineModel<Date>('start', { required: true });
const end = defineModel<Date>('end');
// 对父暴露整体读写：v-model="range" 内部拆解到两个模型
const range = computed({
  get: () => [start.value, end.value],
  set: ([s, e]) => { start.value = s; end.value = e; },
});
defineExpose({ range });
</script>
<!-- 父组件 -->
<!-- <DateRange v-model:start="form.begin" v-model:end="form.finish" /> -->
<!-- <DateRange v-model="form.range" />  经 defineExpose 的 range 联动 -->
```
