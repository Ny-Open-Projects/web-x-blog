# 056 join_buffer_size 按表数成倍分配

> 分类：服务器配置 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**join_buffer_size** / **每表一份** / **BNL**
> 原文锚点：第 299~301 段「如果一个查询中关联了多个表，那么就会在每一个关联的表中分配一个这样的连接缓冲…每个查询可能会有多个连接缓冲的存在」

## 一句话总述
`join_buffer_size` 是**每线程、且按关联表数量成倍分配**的连接缓冲：一个 5 表 JOIN 可能一个连接就吃掉 5 份，所以它比 `sort_buffer_size` 更容易被低估。

## 面试官视角
- **考察意图**：看你是否知道 JOIN 缓冲不是"一查询一份"，以及能否识别 Block Nested Loop。
- **P5** 知道无索引 JOIN 会用到它 / **P6** 说清**每关联表一份**且只在无索引时生效 / **P7** 能挂到 `Using join buffer` 与 8.0.18+ hash join。
- **红旗**：① "调大能优化所有 JOIN"；② 不知只有无索引 JOIN 才用；③ 忘记它随连接数放大。
- **惊艳点**：Extra 出现 `Using join buffer (Block Nested Loop)` 才说明它在起作用；**有索引的 JOIN 用不上它** `[经验]` —— 验证：`EXPLAIN` 对比 Extra。

## 主问答
**Q（面试官原话）：** join_buffer_size 和 sort_buffer_size 有什么不一样？调大能优化 JOIN 吗？

**A：**
1. **先给结论**：差别在**分配份数**——它是**每个关联表一份**，一个查询可能分配多份；且只对**无法走索引**的 JOIN 有效。
2. **再给机制**：被驱动表无索引时，MySQL 把驱动表的行攒进 buffer 再批量比对（Block Nested Loop），减少被驱动表扫描轮次。
3. **最后给边界**：有索引的 JOIN 走索引查找，压根不用它；JOIN 慢的第一动作是**给被驱动表加索引**。它同样是每线程变量，多表 JOIN × 高并发是放大重灾区。

**加分层**：8.0.18 起等值连接可用 hash join 替代 BNL，buffer 角色由 hash 表接管——答题要带版本。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 这个参数干什么 | 概念 | 无索引 JOIN 的缓冲 | 换题 → 不及格 |
| L2 | 和排序缓冲区别 | 机制 | 按表数成倍分配 | 判 P5 |
| L3 | 什么时候才用得上 | 边界 | 被驱动表无索引 | 判 P6 |
| L4 | 调大的代价 | 权衡 | 多表 × 并发放大内存 | 判 P6+ |
| L5 | JOIN 慢的正解 | 架构判断 | 加索引 / 8.0 hash join | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 5.6 / 5.7 | JOIN 主要靠 BNL，join buffer 是核心通道 | "无索引 JOIN 才用，别全局调大" |
| 8.0.18+ | 引入 **hash join**（等值连接），BNL 被逐步替代 | 补一句"8.0.18 后等值 JOIN 可能走 hash join" |

## 关键代码
```sql
-- 1. 识别是否真的用到了 join buffer
EXPLAIN SELECT a.id, b.name
FROM orders a JOIN users b ON a.user_id = b.id;
-- Extra 出现 "Using join buffer (Block Nested Loop)" => 被驱动表没走索引，参数才相关

-- 2. 正解：给被驱动表补索引后重看执行计划
ALTER TABLE users ADD INDEX idx_id (id);

-- 3. 参数现状（注意是每线程变量）
SHOW VARIABLES LIKE 'join_buffer_size';
SET SESSION join_buffer_size = 4194304;   -- 仅对当前大查询临时放宽，避免全局放大
```

## ⚠️ 原文纠错
原文"一个查询中关联了多个表，就会在每一个关联的表中分配一个这样的连接缓冲"方向正确；需补一句更准确的约束：**只有无法使用索引的关联表**才会用到 join buffer，有索引的表不分配——原文未区分该前提，容易被误读成"JOIN 越多必然分配越多"。机翻音译（joininbackset、连接缓冲池）已还原为 join_buffer_size、join buffer。

## 总结与追问预判
- 按**表数**成倍分配（比排序缓冲更狠），且只在**无索引 JOIN** 时生效。
- 优化 JOIN 的第一动作永远是**补索引**。
- 下一题：见 055（sort_buffer_size）、050（每线程缓冲内存总账）。
