---
title: [ARC-089] 物料协议如何设计（属性 schema 与 Setter）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-089：物料协议如何设计（属性 schema 与 Setter）？
**答**：
- 物料 = 组件实现 + 元数据协议（snippets 拖拽入口、props schema 描述每个属性、setter 类型声明交互控件）。
- 协议设计原则：schema 描述"可配置什么"，Setter 描述"用什么控件配"；类型系统与组件 props 类型同源生成，避免两套定义漂移。
- 关键字段： setter 类型、defaultValue、条件显隐（dependency）、校验规则。

```json
{
  "componentName": "Table",
  "npm": { "package": "@corp/lc-materials", "exportName": "Table", "version": "2.3.0" },
  "snippets": [{ "title": "数据表格", "screenshot": "table.png", "schema": { "props": { "columns": [] } } }],
  "props": [
    { "name": "columns", "title": "列配置", "setter": "ArraySetter",
      "itemSetter": { "setter": "ObjectSetter", "props": [
        { "name": "title", "setter": "StringSetter", "required": true },
        { "name": "dataIndex", "setter": "StringSetter" },
        { "name": "width", "setter": "NumberSetter" } ] } },
    { "name": "dataSource", "title": "数据源", "setter": "DataSourceSetter",
      "dependency": { "visibleWhen": { "name": "mode", "op": "eq", "value": "static" } } },
    { "name": "rowKey", "title": "行键", "setter": "StringSetter", "defaultValue": "id",
      "validator": "required" }
  ]
}
```
