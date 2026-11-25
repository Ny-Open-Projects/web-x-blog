---
title: [XP-127] 设计一个跨端表单引擎（schema 驱动多端渲染）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-127：设计一个跨端表单引擎（schema 驱动多端渲染）？
**答**：
- 架构：**JSON Schema 表单协议**（字段类型/校验/联动/布局）为单一事实源 → 各端 renderer（Web/RN/Flutter/小程序）解析渲染 → core 层共享校验与联动逻辑（XP-122 分层同构）。
- 协议设计要点：字段级 `visibleWhen/requireWhen` 声明式联动（表达式引擎受限词表，拒绝任意代码）、异步校验（唯一性检查）、动态选项源（字典接口）、分步表单与草稿。
- 校验唯一实现：校验规则在 core 用纯 TS 实现，各端 renderer 只负责 UI 呈现——错误文案、触发时机（blur/submit）协议化，保证跨端行为一致（XP-107）。
- 类型链路：Schema → codegen 生成 TS 类型（提交 payload 类型安全）；Schema 版本化，旧端宽容读取（XP-112 原则）。
- 治理：表单 Schema 走配置平台下发（运营可配、发版免更）；渲染埋点（字段级放弃率）回流优化表单设计。

```json
{
  "formVersion": "1.3.0",
  "steps": [{ "id": "base" }, { "id": "detail" }],
  "fields": [
    {
      "key": "phone",
      "type": "input",
      "label": "手机号",
      "inputType": "tel",
      "required": true,
      "validators": [
        { "kind": "pattern", "value": "^1\\d{10}$", "message": "手机号格式不正确" },
        { "kind": "async", "api": "/check/phone-unique", "message": "该手机号已注册", "trigger": "blur" }
      ]
    },
    {
      "key": "company",
      "type": "input",
      "visibleWhen": { "field": "userType", "op": "eq", "value": "enterprise" },
      "requiredWhen": { "field": "userType", "op": "eq", "value": "enterprise" }
    },
    {
      "key": "city",
      "type": "select",
      "optionsSource": { "api": "/dict/cities", "labelKey": "name", "valueKey": "code" },
      "layout": { "colSpan": 2 }
    }
  ],
  "draft": { "enabled": true, "ttlHours": 72 }
}
// 联动表达式受限词表（eq/ne/in/gt/empty），拒绝任意代码——安全与跨端一致前提
// core：validate(schema, value) 纯 TS 实现，触发时机协议化；各端 renderer 只管 UI
// codegen：schema → TS 提交 payload 类型；配置平台下发 + 字段级放弃率埋点回流
```
