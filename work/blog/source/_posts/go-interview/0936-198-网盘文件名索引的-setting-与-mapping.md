---
disableNunjucks: true
title: "198 网盘文件名索引的 setting 与 mapping"
date: 2026-10-06 18:53:33
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Elasticsearch 索引建模 | 难度：L3 | 题型：应用题 | 频率：中 | 关键词：**refresh_interval**/**IK 分词**/**ik_max_word**/**ik_smart**/**doc_values 策略**/**ctime 预排序**
> 原文锚点：第 24~72 段「网盘文件索引结构与 mapping 设计」

## 一句话总述
文件名索引是「小文本+高实时」场景：refresh_interval=1s、分片数 840、ctime 预排序；mapping 上 doc_id/uid/doc_type 用 keyword 关 doc_values，file_name 用 text+IK（索引 ik_max_word、搜索 ik_smart）并加小写归一与 HTML 标签过滤。

## 面试官视角
- 考察意图：能不能把「业务字段语义」精确映射到「类型+属性+分词器」三层决策。
- 分档：P5 知 filename 必须 text；P6 知 doc_values 按是否排序决定开关、IK 双分词器；P7 知 refresh_interval 与实时性/性能的权衡。
- 红旗答案：file_size/ctime 也用 keyword；或索引搜索都用 ik_max_word。
- 惊艳点：点出「索引细粒度 ik_max_word 保证召回、搜索粗粒度 ik_smart 保证精度」的分工。

## 主问答
**Q（面试官原话）：** 文件名索引的 mapping 你怎么定？
**A：**
1. **字段清单**：doc_id、uid、file_type、file_size、ctime、file_name。
2. **setting**：refresh_interval=1s（文件名实时性高，默认也 1s，小文本设大无益）；分片 840；`index.sort.field=ctime` 逆序（新上传排前）。
3. **analysis**：IK 分词器，索引用 ik_max_word（细粒度切词）、搜索用 ik_smart（粗粒度），加 lowercase filter 大小写归一、char filter 去 HTML 标签。
4. **等值字段关 doc_values**：doc_id/uid/doc_type 只 term 过滤不排序 → keyword + doc_values:false，省磁盘与内存。
5. **范围字段用数值**：file_size、ctime 需 range → long 类型（不能 keyword，否则 range 失效）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | file_name 用什么类型？ | 基础 | text + IK | P5 |
| L2 | 为什么 doc_id 关 doc_values？ | 取舍 | 只等值过滤不排序 | P6 |
| L3 | ik_max_word 和 ik_smart 区别？ | 原理 | 索引细/搜索粗 | P6 |
| L4 | refresh_interval 设 1s 代价？ | 权衡 | 实时性高但 segment 多、开销大 | P7 |
| L5 | 为什么 ctime 预排序？ | 进阶 | 查询固定按 ctime 排序，免运行时排序 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 6.x+（IK 插件） | IK 需独立安装；index.sort.field 6.0+ | 索引/搜索分词器分离是标准做法 |

## 关键代码
```json
{
  "settings": {
    "index.refresh_interval": "1s",
    "index.number_of_shards": 840,
    "index.sort.field": "ctime",
    "index.sort.order": "desc",
    "analysis": {
      "analyzer": {
        "ik_index":  { "type": "custom", "tokenizer": "ik_max_word", "filter": ["lowercase"], "char_filter": ["html_strip"] },
        "ik_search": { "type": "custom", "tokenizer": "ik_smart", "filter": ["lowercase"] }
      }
    }
  },
  "mappings": {
    "properties": {
      "doc_id":    { "type": "keyword", "doc_values": false },
      "uid":       { "type": "keyword", "doc_values": false },
      "file_size": { "type": "long" },
      "ctime":     { "type": "long" },
      "file_name": { "type": "text", "analyzer": "ik_index", "search_analyzer": "ik_search" }
    }
  }
}
```

## 总结与追问预判
文件名索引的精髓是「类型按查询语义、属性按是否排序/聚合、分词器按索引/搜索分工」。下一步常问 content 索引为何不同（压缩）。

## ⚠️ 原文纠错
1. 事实核校： [经验] refresh 1s 适用小文本高实时、IK 索引细/搜索粗、doc_values 按排序取舍、ctime 预排序、数值字段 range——均正确。
2. 崩坏词归一：源码将 mapping 音译为 making/品、settings 音译为 setting/masetting、ik_max_word 音译为 ipadmassword、ik_smart 音译为 xmart、char filter 音译为「掐filter」、index.sort.field 音译为「点stafield」、must 音译为 master字句、should 音译为秀的子句、慢查询 音译为漫查；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
