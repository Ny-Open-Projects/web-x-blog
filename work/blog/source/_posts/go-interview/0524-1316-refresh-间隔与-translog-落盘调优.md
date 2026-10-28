---
disableNunjucks: true
title: "1316 refresh 间隔与 translog 落盘调优"
date: 2026-10-06 18:20:09
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Elasticsearch | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**refresh_interval**/**translog**/**durability**
> 原文锚点：第 24~32 段「调大 refresh…translog 异步落盘」

## 一句话总述
提性能可放大 `index.refresh_interval`（降低近实时刷新频率，大文档收益显著）与把 `index.translog.durability` 设为 `async` 并加大 `sync_interval`（容忍少量丢失换吞吐）；两者都属"用一致性/可靠性换性能"的权衡。

## 面试官视角
- 考察意图：是否理解 refresh 与 translog 两个写入路径旋钮及其可靠性代价。
- 分档：P5 知 refresh 可调；P6 懂 translog 异步；P7 能讲清 durability=async 的丢失窗口与适用场景。
- 红旗答案：以为 refresh=0 最好；以为 translog 异步零风险。
- 惊艳点：**`refresh_interval` 调大对大文档（电子书/文章）提升极显著、对小文档帮助不大；`durability=async` 只在允许少量数据丢失的日志场景才值得** `[经验]`。

## 主问答
**Q（面试官原话）：** refresh 和 translog 怎么调来提性能？
**A：**
1. **结论**：放大 `index.refresh_interval`（如 30s/60s）减少刷新次数；`index.translog.durability=async` + 加大 `sync_interval` 降低 fsync 频率。
2. **机制**：refresh 把写缓冲变成可搜索的 segment，过频刷新耗费 IO/CPU；translog 默认 `request` 每次写都 fsync 保持久，改 `async` 后按间隔批量 fsync，吞吐上升但崩溃可能丢最后一段 `[经验]`。
3. **边界**：refresh>1s 对小文档收益小；`durability=async` 仅适合日志等可靠性要求低的场景，核心业务别碰。

**加分层：** 大文本场景调大 refresh 能合并更多 IO、释放 CPU 给搜索，是性价比最高的单参数。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | refresh 干嘛？ | 基础 | 变可搜索 | P5 |
| L2 | translog 异步？ | 机制 | durability=async | P6 |
| L3 | 丢数据吗？ | 代价 | 丢最后窗口 | P7 |
| L4 | 何时用 async？ | 场景 | 日志类低可靠 | P7 |
| L5 | 大文档收益？ | 细节 | refresh 调大显著 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 2.x+ | translog durability 参数 | 答"调大 refresh_interval + translog async 换吞吐" |

## 关键代码
```json
PUT /logs/_settings
{ "index.refresh_interval": "30s",
  "index.translog.durability": "async",
  "index.translog.sync_interval": "10s" }
```

## 总结与追问预判
两旋钮=refresh 频率 + translog 持久化策略，都是可靠性换性能。追问接"查询缓存与 routing 优化"。

## ⚠️ 原文纠错
1. 原文 refresh/translog 调优要点正确，仅术语崩坏：refresh的我→**refresh_interval**、translog落盘的间隔/flash→**translog 落盘（sync_interval）**、ASNC→**async（异步）**、GVM→**JVM**、集限/夜色→**集群/ES**。本卡已归一，事实无错 `[经验]`。
