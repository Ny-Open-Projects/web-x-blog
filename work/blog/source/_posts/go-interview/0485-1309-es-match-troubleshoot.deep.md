---
disableNunjucks: true
title: "1309 ES 已索引查不到根因树深挖"
date: 2026-10-10 12:51:51
categories: [Go面试题集]
tags: [Go面试题集]
---

## 思路与架构
```text
"已索引查不到"根因树：
- match(OR/AND)：查询 term 集 ⊆ 索引 term 集？
  - AND 要求 ⊆ 全包含；差一个 term 即不召回。
  - 差异来自 查询 analyzer ≠ 索引 analyzer。
- match_phrase：term 都在 + position 连续？
  - 不连续 ← 长词被再细分插入中间 term（IK max_word 高发）。
  - slop 放宽间隔，但过大损召回质量。
排查顺序：_analyze 对齐 term → 判 match/phrase 语义 → _termvectors 看 position → 统一 analyzer + 必要时 _reindex。
```

## 方案取舍
```text
- 召回率 vs 精度：ik_max_word 细粒度召回高但易插中间 term（phrase 坑多）；ik_smart 粗粒度少坑但召回低。按业务取舍。
- AND vs OR：确定性查询用 AND（全包含），模糊检索用 OR（至少命中）。
- slop：phrase 容忍间隔的应急阀，治标；治本是统一 analyzer / 换粗粒度。
- 一致性原则：search_analyzer 与索引 analyzer 必须一致，否则必现"查不到"。
```

## 答题技巧
```text
- 被问"查不到"：先抛根因"查询/索引分词不一致"，再分 match(term 集) 与 phrase(position) 两路。
- 必点工具：_analyze 看 term、_termvectors 看 position，别靠肉眼猜。
- 收尾落架构：建索引统一 analyzer、按需选 IK 粒度、analyzer 改动要 _reindex 才生效。

```

## 细节与核心 API

**对齐查询与索引分词（别靠肉眼猜）：**

```json
// 看某字段实际切出的 term
GET /my_idx/_analyze { "field": "content", "text": "测试文本" }
// 看已索引文档 term 的 position（phrase 排查）
GET /my_idx/_termvectors/1 { "fields": ["content"], "positions": true, "offsets": true }
```

**match / match_phrase 控制召回与精度：**

```json
// match 默认 OR（高召回）；operator=and 要求 term 全包含
{ "query": { "match": { "content": { "query": "测试 文本", "operator": "and" } } } }
// match_phrase 校验"相邻同序"，slop 放宽间隔（治标，治本是统一 analyzer）
{ "query": { "match_phrase": { "content": { "query": "测试文本", "slop": 1 } } } }
// 统一 analyzer（索引/搜索不一致必现查不到）
PUT /my_idx { "settings": { "analysis": { "analyzer": { "default": { "type": "ik_max_word" } } } } }
```

**根因树落地：**

```text
查不到 → ① match 用 AND：查询 term 集 ⊆ 索引 term 集？差一个即不召回
        ② match_phrase：term 都在 + position 连续？长词再细分插中间 term → 不连续
        ③ 一致原则：search_analyzer 必须与索引 analyzer 一致，否则必现查不到
```
