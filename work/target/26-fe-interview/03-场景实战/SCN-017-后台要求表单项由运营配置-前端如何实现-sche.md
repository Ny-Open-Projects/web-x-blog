---
title: [SCN-017] 后台要求"表单项由运营配置"，前端如何实现 schema 驱动的动态表单？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 笔试题, 11]
type: 笔试题
---

## SCN-017：后台要求"表单项由运营配置"，前端如何实现 schema 驱动的动态表单？
**答**：
- 思路：后端下发 JSON Schema（字段、控件类型、label、校验规则、选项），前端维护"类型 → 组件"的渲染分支，v-for 遍历渲染。
- 校验规则由 schema 翻译成 async-validator 规则交给 el-form 统一校验，避免逐字段手写。
- 复杂联动（选了 A 才显示 B）用 schema 的 visibleWhen 条件或 watch 指定字段处理；映射表模式扩展新控件只需加一个分支。

```vue
<script setup>
import { computed, ref } from 'vue';
// 后端下发的 schema（示例），也可来自接口
const schema = [
  { field: 'name', label: '姓名', type: 'input', required: true },
  { field: 'age', label: '年龄', type: 'number', required: false },
  { field: 'city', label: '城市', type: 'select', options: ['北京', '上海'] },
];
const model = ref({});
// schema 翻译为 async-validator 规则
const rules = computed(() =>
  Object.fromEntries(schema.filter((s) => s.required).map((s) => [
    s.field, { required: true, message: `${s.label}不能为空`, trigger: 'blur' },
  ])),
);
</script>

<template>
  <el-form :model="model" :rules="rules">
    <el-form-item v-for="item in schema" :key="item.field" :label="item.label" :prop="item.field">
      <el-select v-if="item.type === 'select'" v-model="model[item.field]">
        <el-option v-for="op in item.options" :key="op" :label="op" :value="op" />
      </el-select>
      <el-input-number v-else-if="item.type === 'number'" v-model="model[item.field]" />
      <el-input v-else v-model="model[item.field]" />
    </el-form-item>
  </el-form>
</template>
```

## 五、登录态与业务状态
