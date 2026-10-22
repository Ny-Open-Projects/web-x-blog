# 068 慢查询的四个过滤条件

> 分类：日志类 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**long_query_time** / **log_queries_not_using_indexes** / **管理命令** / **只看成功的**
> 原文锚点：第 255~272 段「long_query_time 是一个以秒为单位的时间，可以有六位小数…log_queries_not_using_indexes 设置为 ON 则会把所有没有使用索引的 SQL 记入慢查询日志，不论执行时间是否超过阈值」

## 一句话总述
慢查询只记**执行成功**的查询，命中四个条件之一即记录：超 `long_query_time`、`log_queries_not_using_indexes` 未走索引、管理命令（`log_slow_admin_statements`）、从库回放（`log_slow_slave_statements`）。

## 面试官视角
- **考察意图**：看你是否知道"慢查不是只按时间判定"，以及 `long_query_time=0` 抓全量的狠招。
- **P5** 知道 `long_query_time` 是阈值 / **P6** 说出未走索引是独立条件 / **P7** 列全四条并指出"只记成功查询"。
- **红旗**：① 以为只按执行时间判；② 长开"未走索引"不知日志会爆；③ 不知支持微秒。
- **惊艳点**：`long_query_time` 支持**六位小数（微秒级）**，设 `0` 就是**记录全部查询**——临时抓全量时用，但必须马上关 `[经验]` —— 验证：`SET GLOBAL long_query_time = 0;` 观察日志增速。

## 主问答
**Q（面试官原话）：** 什么样的 SQL 会进慢查询日志？只看执行时间吗？

**A：**
1. **先给结论**：不只时间，共四类判定，且**只记录执行成功的查询**。
2. **再给机制**：① `long_query_time`——默认 10 秒，单位秒、**可带六位小数**，设 0 记全部；② `log_queries_not_using_indexes=ON`——**未走索引即记录，无视时间阈值**；③ `log_slow_admin_statements=ON`——记录 `ALTER TABLE` / `CREATE INDEX` / `DROP INDEX` / `OPTIMIZE` / `REPAIR TABLE` 等管理命令；④ `log_slow_slave_statements=ON`——基于 **statement 格式**复制时记录从库回放的慢 SQL。
3. **最后给边界**：②③④ 默认都是 **OFF**；②一旦开启在索引不规范的库上会**瞬间刷爆日志**，只能短时开启；④因现在普遍用 **ROW 格式** binlog，已很少启用。

**加分层**：抓全量（设 0）和开"未走索引"都是**短时诊断动作**，用完必须复位——慢查日志写爆同样会拖垮实例。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 多久算慢查询 | 概念 | long_query_time 阈值 | 换题 → 不及格 |
| L2 | 没走索引记不记 | 机制 | 独立条件，需手动开 | 判 P5 |
| L3 | 管理命令记不记 | 边界 | 默认不记，需开 | 判 P6 |
| L4 | 失败的查询记不记 | 细节 | 不记，只记成功 | 判 P6+ |
| L5 | 抓全量的代价 | 工程判断 | 日志暴涨，必须复位 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 5.6 / 5.7 | `long_query_time` 默认 10 秒；参数名含 `slave` | "默认 10 秒，注意旧命名" |
| 8.0 | 复制相关术语改为 **replica**（`log_slow_replica_statements` 为新版名，旧名仍兼容） | "8.0 起称 replica，但答题可用旧名并说明" |

## 关键代码
```sql
-- 1. 时间阈值（秒，支持六位小数；设 0 = 记录全部）
SET GLOBAL long_query_time = 1;                    -- 1 秒，生产常用
SET GLOBAL long_query_time = 0.500000;             -- 500 毫秒

-- 2. 未走索引即记录（短时诊断用，日志会暴涨）
SET GLOBAL log_queries_not_using_indexes = ON;

-- 3. 管理类命令 / 从库回放（默认均 OFF）
SET GLOBAL log_slow_admin_statements = ON;
SET GLOBAL log_slow_slave_statements = ON;         -- 仅 statement 格式复制下有效
```

## ⚠️ 原文纠错
原文关于四个条件的描述准确，未发现技术错误。补充两点：① 原文未强调"**只记录执行成功的查询**"这一前提，它正是慢查日志**不能替代通用查询日志**做行为审计的原因；② `log_slow_slave_statements` 仅在 **statement 格式** binlog 下有意义，ROW 格式下无效——原文提到"现在很少用 statement"但未点明该前提。机翻音译（longquatetime、logqueriesnotuse、logslowandmestatement、loveslowslaverstatements、阀值）已还原为 long_query_time、log_queries_not_using_indexes、log_slow_admin_statements、log_slow_slave_statements、阈值。

## 总结与追问预判
- 四类判定，②③④ 默认 **OFF**；**只记成功**的查询。
- `long_query_time=0` 抓全量是狠招，用完即复位。
- 下一题：见 067（开关与路径）、065（为何慢查替代不了通用日志）。
