---
disableNunjucks: true
title: "138 term / match / match_phrase 对比与 text 坑"
date: 2026-10-06 18:47:22
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Elasticsearch 查询 | 难度：L3 | 题型：对比题 | 频率：高 | 关键词：**term**/**match**/**match_phrase**/**text 字段**
> 原文锚点：第 82~102 段「三者总结与 term 查 text 的失效演示」

## 一句话总述
term（精确不分词）、match（分词、默认 OR）、match_phrase（分词+同序相邻）三者**处理分词与匹配规则不同**；最易踩的坑是"用 term 查 text 字段查不到"——因为 text 写入时已分词。

## 面试官视角
- 考察意图：能否用一张对比表讲清三者差异，并指出 text 字段的 term 坑。
- 分档：P5 能列三者名字；P6 能讲分词差异；P7 能讲 text/keyword 坑与 `.keyword` 子字段。
- 红旗答案：把三者混为一谈或以为 term 能查 text。
- 惊艳点：点出"text 字段有 keyword 子字段，精确查用 `field.keyword`"。

## 主问答
**Q（面试官原话）：** 这三个查询到底怎么选？
**A：**
1. **term = 精确**：不分词，整串等值匹配；查 keyword/数值/日期，或 `text.keyword` 子字段。
2. **match = 全文**：分词 + 默认 OR 召回；查 text 全文，追求召回量。
3. **match_phrase = 短语**：分词 + 同序相邻；查 text 精确短语。
4. **text 字段坑**：text 写入被分词（"测试文本"→`测试`/`文本`），`term` 查整串"测试文本"倒排里不存在 → 查不到；正确做法是用 `term` 查 `field.keyword`，或用 `match`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 三者最大区别？ | 基础 | 分不分词 + 位置约束 | P5 |
| L2 | 用 term 查 text 为何空？ | 坑 | text 已分词，整串无 term | P6 |
| L3 | 怎么正确精确查 text？ | 解决 | 用 field.keyword | P7 |
| L4 | GET by ID 算哪种？ | 辨析 | 是文档 API 非查询类型 | P7 |
| L5 | 选型决策树？ | 进阶 | 等值→term；全文→match；短语→match_phrase | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 5.x~8.x | 无 | text 默认带 `.keyword` 子字段（ignore_above 默认 256）；精确过滤用 `.keyword` |

## 关键代码
```json
{ "term": { "content.keyword": { "value": "测试文本" } } }
```

## 总结与追问预判
三查询精度递增：term(精确) < match(全文) < match_phrase(短语)。text 字段被分词，term 整串查必空，须用 `.keyword` 子字段或 match。GET by ID 是文档 API 而非查询类型。

## ⚠️ 原文纠错
1. 事实核校： [经验] 三者分词/匹配差异、term 查 text 失效（因 text 已分词）、`.keyword` 子字段救场，均正确。
2. 崩坏词归一：起查询→GET 按 ID 获取文档、sefacget→GET、election中sech→Elasticsearch、word字/问日志→warn 日志。
