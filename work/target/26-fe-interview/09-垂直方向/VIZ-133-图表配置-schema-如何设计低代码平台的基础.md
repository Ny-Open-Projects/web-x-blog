---
title: [VIZ-133] 图表配置 schema 如何设计？低代码平台的基础
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-133：图表配置 schema 如何设计？低代码平台的基础
**答**：schema 三职责：**约束**（JSON Schema 校验非法配置）、**生成表单**（schema → 属性面板）、**文档**（字段注释即文档）。设计要点：① 分区——data 数据绑定 / style 样式 / interaction 交互 / event 事件四大块，路径稳定便于版本迁移；② 类型系统——基础类型 + 枚举 + 条件显示（如 type=line 才显示 smooth）；③ 数据绑定用字段引用，与 dataset 列元数据联动校验；④ 版本化——schemaVersion + 迁移函数链，旧配置升级不丢配置。落地：JSON Schema + ajv/formily。

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "schemaVersion": "2.1.0",
  "type": "object",
  "properties": {
    "chartType": { "type": "string", "enum": ["line", "bar", "pie"] },
    "dataBinding": {
      "type": "object",
      "properties": {
        "datasetId": { "type": "string", "title": "数据集" },
        "x": { "type": "string", "title": "维度字段" },
        "y": { "type": "array", "items": { "type": "string" }, "title": "指标字段" },
        "agg": { "type": "string", "enum": ["sum", "avg", "count", "max", "min"], "default": "sum" }
      },
      "required": ["datasetId", "x", "y"]
    },
    "style": {
      "type": "object",
      "properties": {
        "smooth": { "type": "boolean", "default": false, "visibleIf": { "chartType": "line" } },
        "palette": { "type": "string", "title": "主题色板", "enum": ["default", "cool", "warm"] }
      }
    }
  },
  "required": ["chartType", "dataBinding"]
}
```
