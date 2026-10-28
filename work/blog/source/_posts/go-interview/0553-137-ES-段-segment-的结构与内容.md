---
disableNunjucks: true
title: "137 ES 段（segment）的结构与内容"
date: 2026-10-06 19:08:40
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Elasticsearch 存储 | 难度：L3 | 题型：概念题 | 频率：中 | 关键词：**段 segment**/**Lucene**/**倒排索引**/**stored field**/**doc_values**
> 原文锚点：第 1~18 段「ES 架构与段内四类数据」

## 一句话总述
ES 架构是「节点 → 分片(shard，即一个 Lucene 实例) → 段(segment，独立倒排索引)」；每个段内主要存四类数据：倒排索引、stored field（store=true 的字段原值）、doc_values（列式，供聚合/排序/脚本）、最近变更缓存。

## 面试官视角
- 考察意图：懂不懂 ES 在 Lucene 层面的物理组成，而非只停留在「索引/分片」概念。
- 分档：P5 知段是倒排索引；P6 知 stored field 与 doc_values 的区别与默认；P7 知 doc_values 列式压缩、按查询需求开关。
- 红旗答案：以为一个分片就是一个大文件；或分不清 stored field 与 doc_values 用途。
- 惊艳点：点出「stored field 用于取回原值、doc_values 用于聚合排序，二者职责不同」。

## 主问答
**Q（面试官原话）：** 一个 ES 分片底层到底存了什么？
**A：**
1. **三层架构**：节点(node) → 分片(shard，一个 Lucene 实例) → 段(segment，独立倒排索引，可单独读写)。
2. **倒排索引**：段的核心，包含单词词典(term dictionary)与倒排列表(postings)。
3. **stored field**：mapping 中 `store: true` 的字段会存原始值，本质列式结构；只搜不显示时可不设，text 类型不设能极大省空间。
4. **doc_values**：序列化的列式存储，极适合聚合/排序/脚本操作，数字类型压缩好；numeric 默认 true、text 默认 false。
5. **最近变更缓存**：段内还存一些反映最近变更的缓存数据。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 分片和段啥关系？ | 基础 | 分片含多个段 | P5 |
| L2 | stored field 干嘛？ | 用途 | 取回字段原值 | P6 |
| L3 | doc_values 默认？ | 细节 | numeric true / text false | P6 |
| L4 | 何时开 doc_values？ | 取舍 | 排序/聚合/脚本时开 | P7 |
| L5 | doc_values 为何省？ | 进阶 | 列式+数字压缩 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 全版本 | doc_values 自 2.x 起为默认列式 | 按查询语义开关 doc_values / store |

## 关键代码
```json
{
  "mappings": {
    "properties": {
      "id":   { "type": "keyword", "store": true, "doc_values": false },
      "name": { "type": "text", "store": false }
    }
  }
}
```

## 总结与追问预判
段是 ES 物理存储的最小单元，四类数据各司其职。下一步常问「为什么段不可变」——这是 ES 写入/搜索性能设计的根基。

## ⚠️ 原文纠错
1. 事实核校： [经验] 节点→分片→段三层、段含倒排/stored field/doc_values/缓存四类、store 与 doc_values 语义、numeric/text 默认值——均正确。
2. 崩坏词归一：源码将 Lucene 音译为 loosen/loser、segment 音译为 seven段/段、stored field 音译为 stoorefield、doc_values 音译为 DCYdeoes、mapping 音译为 making、Elasticsearch 音译为崩坏词（本卡统一为 Elasticsearch）。
