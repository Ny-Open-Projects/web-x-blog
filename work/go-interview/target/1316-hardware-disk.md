# 1316 ES 硬件与磁盘层优化

> 分类：Elasticsearch | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**RAID**/**path.data**/**swap**/**index_buffer**
> 原文锚点：第 1~13 段「RAID/多盘挂载/关 swap/index buffer」

## 一句话总述
ES 硬件层优化：日志/冷数据可用 RAID（如 RAID10）机械盘控成本，性能敏感直接上 SSD；单节点可挂多块盘用 `path.data` 多目录分摊；关 swap 防内存交换；写并发高时调大 `indices.memory.index_buffer_size`（默认 JVM heap 10%）。

## 面试官视角
- 考察意图：是否从硬件/OS 层理解 ES 性能杠杆，而非只背索引参数。
- 分档：P5 知 SSD 快、关 swap；P6 懂 path.data 多盘、buffer 参数；P7 能讲清 buffer 是分片共用、静态配置、按 heap 比例。
- 红旗答案：以为 ES 只用一块盘；以为 index buffer 是每分片独立。
- 惊艳点：**`indices.memory.index_buffer_size` 是所有分片共用的堆内存池（默认 JVM heap 10%），调大对高写入吞吐收益明显，且是静态配置需重启节点** `[经验]`。

## 主问答
**Q（面试官原话）：** ES 在硬件和 OS 层面怎么优化？
**A：**
1. **结论**：磁盘用 RAID10/SSD；单节点挂多盘用 `path.data` 逗号分隔多目录分摊 IO；关 swap；写多则调 `indices.memory.index_buffer_size` 到 20%。
2. **机制**：多盘挂载让写入分散到不同物理盘、提升吞吐并省机架成本（CPU/内存比盘贵）；buffer 是全局共享的堆内存区，给每个分片的索引写入做缓冲，调大减少刷盘次数 `[经验]`。
3. **边界**：`path.data` 多目录要求**分片数 > 磁盘数**否则部分盘闲置；swap 必须关，否则 GC 后内存被换出致严重抖动。

**加分层：** 机械盘 RAID 适合日志类低成本集群；性能型直接 SSD，IO 等待直接决定写入/刷新延迟。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 用什么盘？ | 基础 | RAID10/SSD | P5 |
| L2 | 多盘怎么挂？ | 配置 | path.data 多目录 | P6 |
| L3 | buffer 是啥？ | 机制 | 堆内存共用池 | P6 |
| L4 | swap 为何关？ | OS | 防内存交换抖动 | P7 |
| L5 | 默认多少？ | 细节 | heap 10% 静态 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 5.x+ | 多盘 path.data 长期支持 | 答"RAID10/SSD + path.data 多盘 + 关 swap + 调 buffer" |

## 关键代码
```yaml
# elasticsearch.yml
path.data: /data1/es,/data2/es,/data3/es   # 多盘分摊
indices.memory.index_buffer_size: 20%        # 高写入场景调大（静态，需重启）
bootstrap.memory_lock: true                  # 等效关 swap 的兜底
```

## 总结与追问预判
硬件层=RAID/SSD + 多盘 path.data + 关 swap + 调 buffer。追问接"索引级排序与文档 ID 选型"。

## ⚠️ 原文纠错
1. 原文硬件层优化要点正确，仅 ASR 术语崩坏，本卡已归一：read/读→**RAID**、read一零→**RAID10**、磁盘点贝塔→**path.data**、GVMhip→**JVM heap**、indexesmemoryindexbuffersize→**indices.memory.index_buffer_size**、集限→**集群**。事实无错 `[经验]`。
2. 精度补正：原文"index buffer 默认 JVM heap 10%"准确；多盘挂载要求"分片数>磁盘数"原文亦有提及，本卡沿用。
