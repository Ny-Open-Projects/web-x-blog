# 137 force merge 的注意事项与触发差异

> 分类：Elasticsearch 存储 | 难度：L4 | 题型：运维题 | 频率：中 | 关键词：**force merge**/**max_num_segments**/**IO 消耗**/**磁盘预留**/**关副本**/**大段负载**
> 原文锚点：第 75~94 段「force merge 注意事项与触发差异」

## 一句话总述
手动 `force merge` 是重度 IO/CPU 操作：影响查询吞吐、大索引可能跑数天、段拷贝需额外磁盘空间（可暂关副本腾空间）；通过 `max_num_segments` 指定最终段数。与自然写入触发的 merge 不同——自然只合小段，API 调用会合入大段、负载显著更大。

## 面试官视角
- 考察意图：懂不懂 force merge 的运维代价，以及「自然 merge vs 人工 force merge」的负载差异。
- 分档：P5 知 force merge 指定段数；P6 知耗 IO/CPU、需预留磁盘；P7 知大索引跑数天、关副本腾空间、与自然的差异。
- 红旗答案：以为 force merge 随便跑没代价；或不知道需预留磁盘。
- 惊艳点：点出「几百 TB 索引 force merge 可能超数天」「可暂关副本腾出空间给 merge」。

## 主问答
**Q（面试官原话）：** 手动 force merge 要注意什么？
**A：**
1. **资源消耗大**：merge 是 IO/CPU 密集型，与查询争资源，一般选业务低峰期做。
2. **耗时长**：几百 TB 大索引可能执行超数天，应避免频繁执行。
3. **磁盘预留**：merge 涉及段拷贝（尤其大段），需额外磁盘空间；可暂时关闭副本腾出空间给 merge。
4. **max_num_segments**：指定合并后每分片最终段数，如设 1 把所有段合并成单段。
5. **与自然 merge 差异**：数据自然写入触发的 merge 只合小段；显式 force merge API 会把大段也纳入，给集群带来更大合并负载。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | force merge 干嘛？ | 基础 | 指定最终段数 | P5 |
| L2 | 有什么代价？ | 运维 | IO/CPU 大、影响查询 | P6 |
| L3 | 怎么腾磁盘？ | 细节 | 暂关副本 | P6 |
| L4 | 和自然 merge 差？ | 差异 | API 合大段负载大 | P7 |
| L5 | 大索引多久？ | 进阶 | 几百 TB 可能数天 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 全版本 | force merge 为人工操作 | 大索引慎用；8.x 对 frozen/closed 索引语义有补充 |

## 关键代码
```json
// 合并成每分片 1 段（仅适合只读/不再写入的索引）
POST /idx/_forcemerge?max_num_segments=1
```

## 总结与追问预判
force merge 是「收尾型」操作，代价高、需规划。配合前面不可变/merge 机制，可完整回答 ES 段生命周期。

## ⚠️ 原文纠错
1. 事实核校： [经验] force merge 重 IO/CPU、大索引耗数天、需预留磁盘/暂关副本、max_num_segments 指定段数、自然只合小段/API 合大段——均正确。
2. 崩坏词归一：源码将 force merge 音译为 firstmerge/firstmergy、max_num_segments 音译为 masternumbergments/masknumbersegments、副本 音译为 副本、Elasticsearch 音译为崩坏词（本卡统一为 Elasticsearch）。
