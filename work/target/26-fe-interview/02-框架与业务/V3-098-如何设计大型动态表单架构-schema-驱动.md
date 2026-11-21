---
title: [V3-098] 如何设计大型动态表单架构（schema 驱动）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-098：如何设计大型动态表单架构（schema 驱动）？
**答**：
- 配置与渲染分离：表单结构由 JSON schema 描述（字段、组件类型、校验规则、联动条件），渲染器负责解释执行。
- 新增表单只写配置不写组件代码，运营后台、低代码表单都是这个思路。
- 渲染器要点：按 component 名分发到对应控件；visibleWhen 用函数条件过滤字段；所有字段经 v-model 双写回 model。
- schema 本身要有 TS 类型与校验，防止配置写错静默失效。

```vue
<!-- components/FormRenderer.vue -->
<script setup lang="ts">
import { computed } from "vue";

export interface FieldSchema {
  prop: string;
  label: string;
  component: "ElInput" | "ElSelect" | "ElDatePicker";
  options?: { label: string; value: string }[];
  rules?: Record<string, unknown>[];
  visibleWhen?: (model: Record<string, unknown>) => boolean; // 联动显隐
}

const props = defineProps<{
  schema: FieldSchema[];
  modelValue: Record<string, unknown>;
}>();

const emit = defineEmits<{ "update:modelValue": [value: Record<string, unknown>] }>();

const visibleFields = computed(() =>
  props.schema.filter((f) => !f.visibleWhen || f.visibleWhen(props.modelValue))
);

function update(prop: string, value: unknown) {
  emit("update:modelValue", { ...props.modelValue, [prop]: value });
}
</script>

<template>
  <div class="form-renderer">
    <label v-for="field in visibleFields" :key="field.prop" class="field">
      <span>{{ field.label }}</span>
      <ElInput
        v-if="field.component === 'ElInput'"
        :model-value="String(modelValue[field.prop] ?? '')"
        @update:model-value="update(field.prop, $event)"
      />
      <ElSelect
        v-else-if="field.component === 'ElSelect'"
        :model-value="modelValue[field.prop]"
        :options="field.options"
        @update:model-value="update(field.prop, $event)"
      />
      <ElDatePicker
        v-else-if="field.component === 'ElDatePicker'"
        :model-value="modelValue[field.prop]"
        type="date"
        @update:model-value="update(field.prop, $event)"
      />
    </label>
  </div>
</template>
```
