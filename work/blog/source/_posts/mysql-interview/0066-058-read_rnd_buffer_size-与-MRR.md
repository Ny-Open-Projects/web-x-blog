---
disableNunjucks: true
title: "058 read_rnd_buffer_size 与 MRR"
date: 2026-10-16 02:16:14
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：服务器配置 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**read_rnd_buffer_size** / **MRR** / **回表随机 IO**
> 原文锚点：第 310~311 段「read_rnd_buffer_size 控制的是索引缓冲区的大小…只会在有查询需要的时候才会为该缓冲分配内存，并且也只会分配需要的内存大小」

## 一句话总述
`read_rnd_buffer_size` 是**每线程**的"按主键顺序回表"缓冲：把索引查到的主键先攒下来排序，再**顺序**回表读行，把随机 IO 变成顺序 IO（即 MRR）。

## 面试官视角
- **考察意图**：区分 `read_buffer_size`（顺序扫）与 `read_rnd_buffer_size`（排序后回表），看你是否懂回表代价。
- **P5** 知道有个 read_rnd 缓冲 / **P6** 说清它服务于**回表前主键排序** / **P7** 挂到 MRR 执行计划并知调大代价。
- **红旗**：① "就是索引缓存，越大越好"；② 与 `key_buffer_size` 混为一谈；③ 忘记随连接数放大。
- **惊艳点**：MRR 生效时 Extra 出现 `Using MRR`，且收益**取决于数据是否离散**——主键本就有序时几乎无收益 `[经验]` —— 验证：`EXPLAIN` 对比 `optimizer_switch` 的 `mrr` 开关。

## 主问答
**Q（面试官原话）：** read_buffer_size 和 read_rnd_buffer_size 到底差在哪？

**A：**
1. **先给结论**：前者服务**顺序扫描**（全表/范围扫），后者服务**二级索引回表前的排序**，是把随机读变顺序读的关键。
2. **再给机制**：二级索引范围扫拿到的主键常是乱序的，直接回表即随机 IO；MRR 先把主键放进这块缓冲排序，再按主键顺序回表。
3. **最后给边界**：收益只在**回表且主键离散**时明显；按主键顺序访问或索引已覆盖（不回表）时几乎不起作用。它是**每线程**分配，调大要按并发做乘法。

**加分层**：优先让索引**覆盖查询**（Extra 出现 `Using index`），从根上消掉回表，比调这块缓冲有效得多。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 两个 read 缓冲有什么区别 | 概念 | 顺序扫 vs 排序回表 | 换题 → 不及格 |
| L2 | 它解决什么问题 | 机制 | 随机 IO → 顺序 IO | 判 P5 |
| L3 | 什么时候没收益 | 边界 | 不回表 / 主键已有序 | 判 P6 |
| L4 | 调大的代价 | 权衡 | 每线程 × 连接数放大 | 判 P6+ |
| L5 | 回表怎么根治 | 架构判断 | 建覆盖索引 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 5.6+ | MRR（Multi-Range Read）可用，由 `optimizer_switch` 的 `mrr` / `mrr_cost_based` 控制 | "5.6 起有 MRR，默认按代价决定是否启用" |
| 8.0 | 优化器能力增强，MRR 判定更依赖代价模型 | 补一句"是否走 MRR 看执行计划，不由参数单独决定" |

## 关键代码
```sql
-- 1. 是否走 MRR：看 Extra
EXPLAIN SELECT * FROM orders WHERE user_id BETWEEN 100 AND 200;
-- Extra 出现 "Using MRR" 即 MRR 生效，此时 read_rnd_buffer_size 才真正参与

-- 2. 开关状态（默认 mrr=on、mrr_cost_based=on）
SELECT @@optimizer_switch\G

-- 3. 参数核对（每线程，按需分配但同样受连接数放大）
SHOW VARIABLES LIKE 'read_rnd_buffer_size';
SHOW VARIABLES LIKE 'read_buffer_size';
```

## ⚠️ 原文纠错
原文称 read_rnd_buffer_size"只会分配需要的内存大小，而不是参数指定的大小"——这一点**与官方文档对同类每线程缓冲的描述不一致且难以跨版本确认**，此处标注 `[存疑]`，运维上仍应按"每线程、可能全额分配"的保守口径做内存预算（与 050 卡一致）。另一处：原文把它称作"索引缓冲区"，易与 MyISAM 的 `key_buffer_size` 混淆，已厘清。机翻音译（readINDbettersize、myssl）已还原为 read_rnd_buffer_size、MySQL。

## 总结与追问预判
- 差别在**排序后回表**；收益只在离散回表场景，覆盖索引才是根治。
- 每线程分配，调大前先算并发乘法。
- 下一题：见 057（read_buffer_size）、050（每线程缓冲总账）。
