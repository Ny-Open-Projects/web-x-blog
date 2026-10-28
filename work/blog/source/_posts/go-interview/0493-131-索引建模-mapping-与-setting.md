---
disableNunjucks: true
title: "131 索引建模：mapping 与 setting"
date: 2026-10-07 10:59:46
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：搜索 / Elasticsearch | 难度：L3 | 题型：操作题 | 频率：高 | 关键词：**索引、mapping、setting、字段类型、建模、文档**

> 原文锚点：第 50~59 段「类似 MySQL 建表…建模需设索引的 mapping 与 setting…setting 是索引相关设置、mapping 是字段设置…写入一条数据是文档，含唯一 id」

## 一句话总述
ES 建索引类比关系库建表：建模要设 `settings`（索引级配置，如分片数）和 `mappings.properties`（字段名与类型）。写入的一条数据叫文档（document），有唯一 `_id`；删了再建，返回 acknowledged 即成功。

## 面试官视角
P6 能说出 mapping/setting 区别；P7 要讲清 mapping 决定字段如何分词与检索（text/keyword 之分），以及建模前先想清查询模式，避免后期改 mapping 代价高。

## 主问答
**Q（面试官原话）：** ES 怎么建索引/建模？

1. **两个配置**：`settings` 管索引级设置（分片/副本），`mappings.properties` 管字段名与类型 `[源码]`。
2. **字段类型**：mappings 里定义 id/name/age 等字段及其类型，决定如何索引与检索 `[源码]`。
3. **写文档**：向索引写入一条数据即一个文档，含唯一 `_id` 与字段值 `[源码]`。
4. **删建确认**：删除再创建索引，返回 `acknowledged:true` 表示建好 `[实测]`。
5. **先想查询**：建模前先定查询模式；mapping 一旦有数据难改，需 reindex `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 建模设啥？ | 答不出 mapping/setting |
| L2 | 两者区别？ | 说不出字段 vs 索引 |
| L3 | 文档是？ | 答不出含 _id |
| L4 | 类型怎么选？ | 答不出 text/keyword |
| L5 | 改 mapping？ | 答不出需 reindex |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ES 全版本 | mapping+setting | 建模两步 |
| 7.x | type 固定 _doc | 不再多 type |
| 任意版本 | mapping 难改 | 改需 reindex |

## 关键代码
```go
// 建索引并定义 mapping（id/name/age）
body := `{"mappings":{"properties":{"name":{"type":"text"},"age":{"type":"integer"}}}`
es.Indices.Create("user", es.Indices.Create.WithBody(strings.NewReader(body)))
```

## 总结与追问预判
**mapping 决定检索行为**。type 演进是 ES 一大坑——见同批 131-type-evolution。

## ⚠️ 原文纠错
1. 事实核校：建模需 settings+mappings、字段类型、文档含 _id、acknowledged 确认——均准确 `[经验]`。
2. 补充：原文「类比 MySQL 建表」，精确 7.x 后一个索引≈一张表、type 固定 _doc，勿再类比库 `[经验]`。
3. 崩坏词归一：源码将 Elasticsearch、Lucene、索引、映射、文档、集群等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
