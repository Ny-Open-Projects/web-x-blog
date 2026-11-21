---
title: [V3-276] 动态表单引擎（schema 驱动）的设计方案是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-276：动态表单引擎（schema 驱动）的设计方案是什么？
**答**：
- 三层协议：schema（字段元数据：type/label/rules/options）→ 引擎（递归渲染 + 状态管理 + 校验编排）→ 渲染器（各 type 对应组件的映射表，可注册自定义）。
- 联动建模：用**声明式表达式**（`visibleWhen: { field: 'type', eq: 'vip' }`）+ 少量钩子函数，避免 schema 里写业务代码导致不可测。
- 状态管理：值统一存扁平 formModel，字段路径（a.b.0.c）读写；联动引擎监听变化批量计算各字段 visible/disabled/options。
- 校验编排：schema rules → async-validator 描述对象，按字段注册，提交前全量校验并聚焦首个错误。
- 性能：大表单按"字段级组件"拆分 + 动态组件缓存（KeepAlive），联动计算结果 memo 化避免全表重算。

```typescript
// schema 示例
const schema = [
  { field: 'userType', label: '用户类型', type: 'select',
    options: [{ label: '普通', value: 'normal' }, { label: 'VIP', value: 'vip' }],
    rules: [{ required: true, message: '请选择' }] },
  { field: 'level', label: 'VIP 等级', type: 'number',
    visibleWhen: { field: 'userType', eq: 'vip' },         // 声明式联动
    rules: [{ type: 'number', min: 1, max: 6 }] },
  { field: 'coupon', label: '优惠券', type: 'asyncSelect',
    optionsLoader: '/api/coupons',                          // 异步选项
    disabledWhen: { field: 'level', lt: 3 } },
];
// 引擎核心：单字段渲染器 + visible 计算
function isFieldVisible(field, model) {
  const w = field.visibleWhen;
  return !w || (w.eq !== undefined ? model[w.field] === w.eq : true)
       && (w.lt !== undefined ? model[w.field] < w.lt : true);
}
// 渲染：<component :is="typeMap[field.type]" v-bind="field" v-model="model[field.field]" />
```
