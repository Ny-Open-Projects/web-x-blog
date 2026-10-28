---
disableNunjucks: true
title: "119 mysqldump 必背参数清单"
date: 2026-10-16 06:52:11
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：备份恢复 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**--single-transaction** / **--master-data** / **--routines** / **--triggers** / **--where**
> 原文锚点：第 79~99 段「single-transaction 会直接启动一个事务……对于 MyISAM 或 memory 这种非事务表，该参数无效」

## 一句话总述
九成场景只需记住四个：`--single-transaction`（不锁表的一致性快照）、`--master-data=2`（记位点/GTID）、`--routines` + `--triggers`（存过与触发器）、`--where`（条件导出）。

## 面试官视角
- **考察意图**：会不会只会 `mysqldump db > x.sql`，连一致性都不保证。
- **P5** 能说出 `--single-transaction` / **P6** 能说清 `--master-data` 取 1 与 2 的区别 / **P7** 会补「非事务引擎下 `--single-transaction` **无效**，必须 `--lock-all-tables`」。
- **红旗**：「不加参数也是一致性备份」；「`--master-data=1` 和 2 一样」；「触发器会被默认一起备份」。
- **惊艳点**：`--master-data=1` 生成的 `CHANGE MASTER TO` 是**可执行语句**（导入即生效），`=2` 是**注释**（需人工确认）——生产备份一律用 2（8.0.36 `[经验]`）。

## 主问答
**Q：mysqldump 备份时你都加哪些参数？为什么？**
**A：**
1. **先给结论**：`--single-transaction --master-data=2 --routines --triggers --events --set-gtid-purged=OFF`（按是否需要建从库调整最后一项）。
2. **再给机制**：`--single-transaction` 在**一个事务**里取一致性快照，备份期间**不阻塞写**；`--master-data` 记录备份时刻的 binlog 文件名与偏移量（GTID 模式下记录 `GTID_PURGED`），是从库对齐的锚点。
3. **最后给边界**：`--single-transaction` 只对**事务引擎**有效；库里有 MyISAM/Memory 表时要想保证一致性，得换 `--lock-all-tables`（会锁全库）。
**加分层**：`--where` 可做条件导出（如 `cnt > 20`），配合 `--no-create-info` 就能只导数据不导表结构，是数据抽取的常用组合。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么不加锁做备份 | 概念 | --single-transaction | 换题 |
| L2 | master-data 取 1 还是 2 | 基础 | 2（注释） | 判 P5 |
| L3 | 非事务表怎么办 | 机制 | --lock-all-tables | 判 P6 |
| L4 | 存过触发器默认导吗 | 边界 | 不，要显式加 | 判 P6+ |
| L5 | 怎么只导部分数据 | 实战 | --where + --no-create-info | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | 8.0.23+ 引入 `--source-data` 作为 `--master-data` 的新名；`--set-gtid-purged` 在 GTID 下默认 ON | 老环境写 `--master-data`，8.0 新环境可写 `--source-data` |

## 关键代码
```bash
# 通用一致性备份（不锁表 + 记位点 + 带存过/触发器/事件）
mysqldump --single-transaction --master-data=2 \
  --routines --triggers --events --set-gtid-purged=OFF db1 > db1.sql
# 条件导出：只导 cnt>20 的行，不带建表语句
mysqldump --single-transaction --where="cnt>20" --no-create-info db1 stock > part.sql
```
```sql
-- 备份前先看库里有没有非事务引擎表：有则 --single-transaction 不足以保证一致性
SELECT table_schema, table_name, engine FROM information_schema.tables
WHERE table_schema='db1' AND engine <> 'InnoDB';
```

## ⚠️ 原文纠错
原文提到 `--single-transaction`「启动一个事务」正确，但未明说**对非事务引擎无效**这一关键边界（原文只说「对其他存储引擎无效」），已在主问答第 3 条与追问链强调。机翻「singleconstruction / singleal三 / 杠e / 杠r / 杠tigers / rar」还原为 **`--single-transaction` / `--events` / `--routines` / `--triggers` / `--where`**。原文对 `--set-gtid-purged` 未展开，已补。

## 总结与追问预判
- 一致性、位点、对象三件套，条件导出靠 `--where`。
- 下一题：见 120（恢复时 GTID_PURGED 报错）、116（逻辑 vs 物理）。
