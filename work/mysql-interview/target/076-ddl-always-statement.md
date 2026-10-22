# 076 为什么 DDL 在 binlog 里总是语句形式

> 分类：日志类 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**DDL** / **STATEMENT** / **binlog_format** / **mysqlbinlog**
> 原文锚点：第 352 段「无论我们在配置中指定的是哪种日志格式，那么在执行这个 DDL 操作的时候啊，所使用的呢都是基于这个段的日志格式来进行记录的」

## 一句话总述
**DDL 一律以语句（STATEMENT）形式记录**，不受 `binlog_format` 设置影响——因为 DDL 不产生"行变更"，没有行镜像可记。

## 面试官视角
- **考察意图**：你是否清楚 binlog 记录的**粒度边界**（行 vs 语句），以及 DDL 与 DML 的本质区别。
- **P5** 能说出三种格式 / **P6** 知道 DDL 不受格式影响 / **P7** 能延伸到"DDL 无法按行回滚、所以 online DDL 要谨慎"的工程含义。
- **红旗**：① "改成 ROW 后 DDL 也记行变更"；② 把 DDL 当成可拆小事务的操作。
- **惊艳点**：DDL 记语句意味着**一条 `ALTER TABLE` 在从库同样要完整重放**——大表 DDL 的复制延迟由此而来 `[经验]`。验证：`ALTER` 一张大表后 `mysqlbinlog` 直接可读到原句。

## 主问答
**Q（面试官原话）：** binlog_format=ROW 的时候，ALTER TABLE 在 binlog 里记的是什么？

**A：**
1. **先给结论**：记的是**这条 DDL 语句本身**，即语句（STATEMENT）形式，与 `binlog_format` 无关。
2. **再给机制**：ROW 的"行镜像"是描述**数据行增删改**的；DDL 改的是**表的 schema 元数据**，不存在"哪一行被改了"，因此只能原样记录语句，从库直接重放。
3. **最后给边界**：这也意味着 DDL 在主从上是**同一条语句各执行一次**——大表 ALTER 会在从库造成同样长的执行时间与复制延迟；生产需要 gh-ost / pt-online-schema-change 之类工具或分批处理。

**加分层**：因为 DDL 记语句，`mysqlbinlog` 查看 DDL 段**无需 `-v`**，人工可读性天然就有。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | binlog 有几种格式 | 概念 | S / ROW / MIXED | 换题 → 不及格 |
| L2 | DDL 记成什么 | 机制 | 语句形式 | 判 P5 |
| L3 | 为什么不能记行 | 原理 | 无行变更可记 | 判 P6 |
| L4 | 对主从意味着什么 | 工程含义 | 从库同样重放、同样耗时 | 判 P6+ |
| L5 | 大表 DDL 怎么办 | 架构 | 在线改表工具、避开高峰 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 变化点 | 现在该怎么答 |
|---|---|---|
| 5.6 / 5.7 | 行为一致 | DDL 恒为语句 |
| 8.0 | 引入原子 DDL | 语句记录不变，但 DDL 具备原子性 |
| 8.0 | INSTANT DDL（8.0.12+） | 部分加列可秒级，仍需评估复制 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'binlog_format';            -- 即便为 ROW
ALTER TABLE stock ADD COLUMN remark VARCHAR(64);
SHOW BINLOG EVENTS IN 'mysql-bin.000006' LIMIT 20;
```

```bash
# DDL 段可直接读，不需要 -v
mysqlbinlog --start-datetime='2026-10-16 03:00:00' /data/mysqllog/mysql-bin.000006 | grep -i 'ALTER'
```

## ⚠️ 原文纠错
原文"基于这个段的日志格式"是机翻音译，**"段"应还原为"语句"（STATEMENT / statement-based）**，不是"数据段"；原文结论（DDL 恒按语句记录）正确。核对范围：第 346~353 段。

## 总结与追问预判
- DDL **恒记语句**，格式参数管不到它。
- 工程含义：大表 DDL 主从都慢，需在线改表方案。
- 下一题：见 070（binlog_format）、073（ROW 日志瘦身）。
