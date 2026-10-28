---
disableNunjucks: true
title: "198 网盘搜索的 bool 查询与 routing 优化"
date: 2026-10-06 18:53:55
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Elasticsearch 查询优化 | 难度：L4 | 题型：应用题 | 频率：中 | 关键词：**bool 查询**/**must/should**/**boost**/**minimum_should_match**/**routing=UID**
> 原文锚点：第 84~106 段「文件名查询的 bool 结构与 routing 设计」

## 一句话总述
网盘搜索用 bool 查询：must 放「必须满足」的过滤（UID+ctime 范围+后缀），should 放 file_name 的 match（boost=1）与 match_phrase（boost=5）并设 minimum_should_match=1；再辅以 routing=UID 把同用户文档路由到同分片，查询只扫一个分片。

## 面试官视角
- 考察意图：会不会用 bool 分层（must/should）、用 boost 控制相关度、用 minimum_should_match 约束、用 routing 砍分片扫描。
- 分档：P5 知 must/should 区别；P6 知 boost 与 minimum_should_match；P7 知 routing 把查询收敛到单分片。
- 红旗答案：过滤条件放 should；或不设 minimum_should_match 导致 should 全空也召回。
- 惊艳点：点出「match_phrase 召回相关度更高故 boost 更高，且排序先 score 后 ctime」。

## 主问答
**Q（面试官原话）：** 这个网盘搜索的查询语句怎么写？
**A：**
1. **must 子句**：放硬性过滤——UID 等值、ctime 时间范围、文件后缀过滤，必须全部满足。
2. **should 子句**：放 file_name 的 match（operator=and，boost=1）与 match_phrase（boost=5）；match_phrase 相关度更高故权重更大。
3. **minimum_should_match=1**：should 至少命中一个，否则文档不被召回（避免 should 全空）。
4. **排序**：第一排序 score（boost 拉开差距），第二排序 ctime（业务时间序）。
5. **routing=UID**：同一用户文档落同一分片，查询指定 routing 只扫一个分片，免跨节点汇总。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | must 和 should 区别？ | 基础 | must 必须、should 可选加分 | P5 |
| L2 | boost 干嘛用？ | 原理 | 调相关度权重 | P6 |
| L3 | minimum_should_match 作用？ | 约束 | should 至少命中几个 | P6 |
| L4 | routing 为什么用 UID？ | 优化 | 同用户同分片，查询收敛 | P7 |
| L5 | routing 写错会怎样？ | 进阶 | 查不到文档（路由错位） | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 全版本 | routing 语义稳定 | must+should+minimum_should_match+routing 为标准组合 |

## 关键代码
```json
{
  "query": {
    "bool": {
      "must": [
        { "term": { "uid": "u123" } },
        { "range": { "ctime": { "gte": 1700000000 } } }
      ],
      "should": [
        { "match": { "file_name": { "query": "报告", "operator": "and", "boost": 1 } } },
        { "match_phrase": { "file_name": { "query": "季度报告", "boost": 5 } } }
      ],
      "minimum_should_match": 1
    }
  },
  "sort": [ { "_score": "desc" }, { "ctime": "desc" } ],
  "routing": "u123"
}
```

## 总结与追问预判
查询优化的三角：bool 分层管「逻辑」、boost/minimum_should_match 管「相关度」、routing 管「分片扫描面」。下一步常问 highlight 与 scroll 深翻页。

## ⚠️ 原文纠错
1. 事实核校： [经验] must 放硬过滤、should 放召回+boost、match_phrase 相关度更高、minimum_should_match=1、routing=UID 收敛分片——均正确。
2. 崩坏词归一：源码将 bool 音译为「布ars」、must 音译为 master字句、should 音译为秀的子句、match 音译为 mach、match_phrase 音译为 matchfreeze、routing 音译为 routine、score 音译为 school/scscscore；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
