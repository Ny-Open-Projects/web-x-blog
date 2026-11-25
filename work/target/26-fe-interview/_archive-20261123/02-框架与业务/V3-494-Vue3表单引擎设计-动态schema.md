---
title: [V3-494] Vue3 表单引擎设计：动态 schema 驱动
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## V3-494：Vue3 表单引擎设计：动态 schema 驱动

**答**：
- schema 设计：`{ fields: [{ type, name, label, rules, visibleWhen, optionsFrom }] }`——type 决定渲染组件、visibleWhen 是声明式联动（表达式或函数）
- 渲染层：动态组件映射（component :is="fieldComp[field.type]"）+ v-bind="field.props"——字段组件注册表可扩展（业务自定义字段类型）
- 联动实现：visibleWhen/disableWhen 用「函数式求值」于 computed——依赖自动追踪（函数内读 reactive form）而不是自研观察器；这是 Vue 响应式白送的引擎能力
- 校验引擎：schema.rules → 异步校验器（防抖 + 竞态守卫），错误存独立 map；提交前全量校验聚合
- 与代码生成的取舍：schema 引擎灵活但调试链路长——分层策略：标准 CRUD 用引擎，复杂交互页手写；引擎只覆盖 70% 表单，剩余 30% 提供「自定义字段插槽」逃生口

```javascript
// schema 片段
{ name: 'city', type: 'select', label: '城市',
  visibleWhen: (f) => f.country === 'CN',
  optionsFrom: (f) => cityApi.byCountry(f.country),
  rules: [{ required: true }] }
// 引擎求值
const visible = computed(() => fields.value.filter(f => f.visibleWhen?.(form) ?? true));
```
