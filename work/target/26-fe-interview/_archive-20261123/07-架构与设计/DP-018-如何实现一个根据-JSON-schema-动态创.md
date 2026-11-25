---
title: [DP-018] 如何实现一个"根据 JSON schema 动态创建表单控件"的控件工厂？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-018：如何实现一个"根据 JSON schema 动态创建表单控件"的控件工厂？（高频）
**答**：
- 低代码/配置化表单的核心：schema 描述"要什么控件、什么校验"，工厂负责把 schema 变成组件实例。
- 三件套：控件注册表（type → 组件）、props 适配器（schema 字段 → 组件 props）、校验规则装配（复用策略模式）。
- 扩展新控件 = 注册新表项，业务渲染代码零修改（OCP）。
- 加分点：说明 v-model/受控值的统一接入方式——所有控件都遵循 `value + onChange` 协议。

```vue
<script setup>
import { computed } from 'vue';

// 控件注册表：type -> 组件，工厂核心
const registry = {
  input: InputControl,
  select: SelectControl,
  checkbox: CheckboxControl,
};
function registerControl(type, comp) { registry[type] = comp; } // 扩展点

// 简化的内置控件（统一 value/update 协议，即 v-model）
const InputControl = {
  props: ['modelValue', 'schema'],
  emits: ['update:modelValue'],
  template: `<input :value="modelValue" :placeholder="schema.placeholder"
             @input="$emit('update:modelValue', $event.target.value)" />`,
};
const SelectControl = {
  props: ['modelValue', 'schema'],
  emits: ['update:modelValue'],
  template: `<select :value="modelValue" @change="$emit('update:modelValue', $event.target.value)">
    <option v-for="o in schema.options" :key="o" :value="o">{{ o }}</option></select>`,
};
const CheckboxControl = {
  props: ['modelValue', 'schema'],
  emits: ['update:modelValue'],
  template: `<input type="checkbox" :checked="modelValue"
             @change="$emit('update:modelValue', $event.target.checked)" />`,
};

const props = defineProps({ schema: Array });
const model = defineModel(); // 整个表单的数据对象
// 工厂分派：schema 驱动渲染
const controls = computed(() =>
  props.schema.map((field) => ({ field, comp: registry[field.type] || registry.input }))
);
</script>

<template>
  <form>
    <label v-for="{ field, comp } in controls" :key="field.name">
      {{ field.label }}
      <component :is="comp" v-model="model[field.name]" :schema="field" />
    </label>
  </form>
</template>

<!-- 使用：schema 即配置，新增控件只需 registerControl('rate', RateControl)
<SchemaForm v-model="form" :schema="[
  { type: 'input', name: 'name', label: '姓名', placeholder: '请输入' },
  { type: 'select', name: 'city', label: '城市', options: ['北京', '上海'] },
]" /> -->
```
