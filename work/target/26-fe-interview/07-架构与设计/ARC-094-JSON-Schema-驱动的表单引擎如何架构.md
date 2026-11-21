---
title: [ARC-094] JSON Schema 驱动的表单引擎如何架构？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-094：JSON Schema 驱动的表单引擎如何架构？
**答**：
- 三层：schema 层（字段/校验/布局声明）、引擎层（解析 schema → 表单树 + 校验状态机）、渲染层（字段组件映射 Setter）。
- 支持动态行为：条件显隐、级联、异步选项源，全部声明式（表达式引用其他字段值）。
- 复杂逻辑逃生口：允许自定义组件接入（widget 注册机制），避免引擎语法膨胀成"模板语言"。

```typescript
// 表单引擎：schema 解析 + 状态机
interface FormSchema {
  fields: FormField[];
}
interface FormField {
  name: string;
  label: string;
  widget: 'input' | 'select' | 'date' | 'custom:RegionPicker';   // custom: 走注册的逃生口
  required?: boolean;
  validator?: { pattern?: string; max?: number; message?: string };
  visibleWhen?: { field: string; op: 'eq' | 'neq' | 'in'; value: unknown };
  optionsFrom?: string;                                          // 异步选项源 key
}

function buildFormState(schema: FormSchema, registry: Map<string, Widget>) {
  const values = reactive<Record<string, unknown>>({});
  const errors = reactive<Record<string, string | null>>({});
  const fields = schema.fields
    .map(f => ({
      ...f,
      widget: registry.get(f.widget) ?? fallbackInput,           // 逃生口：custom widget 注册
      visible: f.visibleWhen ? check(f.visibleWhen, values) : true,   // 响应式重算
    }));
  async function validate(name?: string) {
    const targets = name ? fields.filter(f => f.name === name) : fields;
    for (const f of targets.filter(f => f.visible)) {
      errors[f.name] = await runValidators(f, values[f.name]);   // 校验规则全来自 schema
    }
    return Object.values(errors).every(e => !e);
  }
  return { values, errors, fields, validate };
}
```
