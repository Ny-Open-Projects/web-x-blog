# 1248 MySQL 版本差异：范围列后索引仍有效 + IS NULL 规则

> 分类：MySQL · 索引版本差异 | 难度：L3 | 题型：陷阱题 | 频率：中 | 关键词：**范围列** / **MySQL 8.0** / **IS NULL** / **IS NOT NULL** / **NOT IN**
> 原文锚点：第 41~43,53~56 段「IS NULL/IS NOT NULL 规则；范围列后索引在 8.0 仍有效（优化器按代价选列）」

## 一句话总述
两个易踩的版本/条件细节：① **MySQL 8.0 起"范围列后索引失效"不再成立**——优化器按代价自动选列，范围条件在前后续列仍可用；② **IS NULL / IS NOT NULL 是否走索引取决于字段是否允许 NULL**，且 `NOT IN` 在 5.8 前会使索引失效。

## 面试官视角
- 意图：考察是否还抱着过时经验（"范围列后全失效"），以及 NULL 相关索引规则的细节。
- 分档：P5 知最左前缀；P6 知 8.0 范围列例外；P7 能讲 IS NULL/IS NOT NULL 与字段是否允许 NULL 的关系。
- 红旗：一口咬定"范围查询后索引全失效"——在 8.0 是错的。
- 惊艳点：点出"字段不允许 NULL 时，IS NULL 与 IS NOT NULL 都失效；允许 NULL 时 IS NULL 走 ref、IS NOT NULL 失效"。

## 主问答
**Q（面试官原话）：** 听说范围查询会让后面索引列失效，对吗？
**A：**
1. **8.0 例外**：老经验"范围列后索引失效"在 **MySQL 8.0 不再绝对成立**。优化器按查询代价自动选索引列——如 `WHERE k2 > ? AND k1 = ?`，即便范围 `k2` 在前，`k1` 的索引列仍可能被选用。
2. **IS NULL 规则**：
   - 字段**不允许 NULL**：`IS NULL` 与 `IS NOT NULL` 都**导致索引失效**（无 NULL 值可匹配）。
   - 字段**允许 NULL**：`IS NULL` 走 `ref` 类型索引；`IS NOT NULL` 仍可能失效。
3. **NOT IN**：在 **MySQL 5.8（5.7/8.0 之前部分版本）前**，`NOT IN` 会使索引失效；新版已优化。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 范围列后失效？ | 基础 | 8.0 不成立 | P5 |
| L2 | 为什么 8.0 变 | 机制 | 优化器按代价选列 | P6 |
| L3 | IS NULL 规则 | 机制 | 取决于是否允许 NULL | P6+ |
| L4 | NOT IN | 版本 | 5.8 前失效 | P7 |
| L5 | 怎么验证 | 实战 | EXPLAIN key_len/type | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL < 5.7：范围列后失效、NOT IN 失效 | 8.0 优化器按代价选列，范围列后仍可用 | 答"8.0 起范围列后索引未必失效，以 EXPLAIN 为准；IS NULL 规则看字段是否允许 NULL" |

## 关键代码
```sql
-- 8.0：范围列 k2 在前，k1 索引列仍可能被用
EXPLAIN SELECT * FROM t WHERE k2 > 10 AND k1 = 5;
-- 允许 NULL 的 col：IS NULL 走 ref，IS NOT NULL 可能失效
EXPLAIN SELECT * FROM t WHERE col IS NULL;      -- type=ref
EXPLAIN SELECT * FROM t WHERE col IS NOT NULL;  -- 可能 type=ALL
```

## 总结与追问预判
- 别拿旧版本经验答新版本；NULL 相关索引规则看"字段是否允许 NULL"。
- 预判：最左前缀基础 → 见 1222；索引失效汇总 → 见 1222。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（如 circle→SQL、乐indv→InnoDB、索影→索引、note→NOT、oldby→ORDER BY、cirll→SQL），本卡统一为规范术语 `[经验]`。未做事实性更正。
