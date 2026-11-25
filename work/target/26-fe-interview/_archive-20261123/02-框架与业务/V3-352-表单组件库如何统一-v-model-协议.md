---
title: [V3-352] 表单组件库如何统一 v-model 协议？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-352：表单组件库如何统一 v-model 协议？
**答**：
- 统一约定：所有输入类组件走 `modelValue` + `update:modelValue`；特殊语义（日期范围、级联多值）用具名 v-model：`v-model:start` / `v-model:end`。
- 封装基类 composable：`useFieldModel(defineModel())` 统一提供 dirty/校验/格式化钩子，组件只写视图。
- 修饰符透传：`defineProps<{ modelModifiers?: object }>()`，在 composable 统一实现 number/trim，组件不重复写。
- 值归一化：入库前统一「空值语义」（'' vs null vs undefined），由 composable 的 normalize 层处理，避免各组件不一致。
- 兼容旧版：组件库同时支持 v-model（3.x）与 .sync（2.x）时，用编译目标判断，产品层文档标注协议差异。
```javascript
function useVModel(props, emit, key = 'modelValue') {
  return computed({
    get: () => props[key],
    set: (v) => emit(`update:${key}`, v)
  })
}
```
