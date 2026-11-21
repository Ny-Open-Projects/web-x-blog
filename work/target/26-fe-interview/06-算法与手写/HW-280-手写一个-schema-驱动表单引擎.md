---
title: [HW-280] 手写一个 schema 驱动表单引擎：字段声明渲染与值收集
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-280：手写一个 schema 驱动表单引擎：字段声明渲染与值收集

**答**：
- 需求：实现 FormEngine：schema 字段声明 [{name, type, label, rules, visibleWhen, options}]；render() 按 schema 输出组件配置（type→组件映射可扩展）；values 收集（仅可见字段参与校验与提交）；visibleWhen(values) 动态可见性重算。
- 边界：不可见字段值保留在 values 但不提交（stripHidden）；type 注册表支持自定义组件；schema 变更热更新。
- 评分点：可见性驱动校验；stripHidden；组件注册表。

```javascript
class FormEngine {
  constructor(schema) { this.schema = schema; this.values = {}; this.widgets = new Map(); }
  registerWidget(type, comp) { this.widgets.set(type, comp); }   // 自定义组件注册
  visibleFields(values = this.values) {
    return this.schema.filter(f => !f.visibleWhen || f.visibleWhen(values));
  }
  render() {
    return this.visibleFields().map(f => ({
      widget: this.widgets.get(f.type) ?? defaultWidget(f.type),
      props: { label: f.label, options: f.options, value: this.values[f.name],
        onChange: v => this.setValue(f.name, v) },
    }));
  }
  setValue(name, v) {
    this.values[name] = v;
    if (this.schema.some(f => f.visibleWhen)) this.onVisibilityChange?.();   // 动态可见性重算
  }
  validate() {
    const errors = {};
    for (const f of this.visibleFields())                    // 仅可见字段校验
      for (const rule of f.rules ?? []) {
        const msg = RULES[rule.type](this.values[f.name], rule);
        if (msg) { errors[f.name] = msg; break; }
      }
    return { valid: !Object.keys(errors).length, errors };
  }
  submit() {
    const { valid, errors } = this.validate();
    if (!valid) return { valid, errors };
    const visible = new Set(this.visibleFields().map(f => f.name));
    const data = Object.fromEntries(Object.entries(this.values)
      .filter(([k]) => visible.has(k)));                     // stripHidden
    return { valid: true, data };
  }
}
const RULES = {
  required: v => v == null || v === '' ? '必填' : null,
  max: (v, r) => String(v).length > r.n ? `最长 ${r.n}` : null,
  pattern: (v, r) => !r.re.test(v ?? '') ? '格式错误' : null,
};
```
