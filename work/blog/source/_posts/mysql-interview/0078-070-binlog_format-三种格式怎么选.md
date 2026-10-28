---
disableNunjucks: true
title: "070 binlog_format 三种格式怎么选"
date: 2026-10-16 02:38:02
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：日志类 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**STATEMENT** / **ROW** / **MIXED** / **主从一致**
> 原文锚点：第 346~352 段「binlog_format 是一个动态参数…二进制日志有三种格式，分别是 statement、row 以及 mixed…statement 是 5.7 版本之前默认使用的格式，其中记录的是进行数据修改时所执行的 SQL 语句」

## 一句话总述
`binlog_format` 三选一：**STATEMENT** 记 SQL 语句（日志小但有不确定的风险）、**ROW** 记行级变更（安全、日志大，**5.7.7 起默认**）、**MIXED** 由优化器按语句判定。

## 面试官视角
- **考察意图**：看你是否理解"日志格式 = 复制一致性"这条因果链。
- **P5** 能说出三种名字。
- **P6** 能说清 STATEMENT 记语句、ROW 记行，以及各自的日志量差异。
- **P7** 能指出 **STATEMENT 的不确定性风险**（`UUID()`、`NOW()`、非确定性函数与 `LIMIT` 无 ORDER BY），从而说明为什么默认改成了 ROW。
- **红旗**：① "ROW 更好所以永远用 ROW"；② 不知默认在 5.7.7 翻转；③ 认为 MIXED 是"随机选"。
- **惊艳点**：STATEMENT 格式 `mysqlbinlog` **直接读出 SQL**，ROW 是行镜像、需 `-v` 才可读 `[经验]` —— 验证：`mysqlbinlog -vv <binlog 文件>`。

## 主问答
**Q（面试官原话）：** binlog 有哪几种格式？你们线上用哪种，为什么？

**A：**
1. **先给结论**：STATEMENT / ROW / MIXED 三种；生产普遍选 **ROW**（5.7.7 起已是默认）。
2. **再给机制**：STATEMENT 记录**修改数据的 SQL 语句**，日志量小、可读性好，但遇到 `UUID()`、`NOW()` 这类**不确定函数**时，从库回放结果可能与主库不一致；ROW 记录**每行的前后镜像**，回放结果确定、最安全，代价是日志显著变大（批量更新尤其明显）。
3. **最后给边界**：MIXED 是"能用语句就用语句、不安全就退化成行"的折中；它是**动态**参数可在线改，但复制环境下切换要考虑**从库兼容与日志量突增**，别在高峰期动。

**加分层**：ROW 格式下日志变大是**为一致性付的费**——批量更新 100 万行，STATEMENT 一条语句、ROW 是 100 万条行记录，这正是大事务导致复制延迟的常见原因。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 有哪几种格式 | 概念 | S / R / MIXED | 换题 → 不及格 |
| L2 | 各记什么内容 | 机制 | 语句 vs 行镜像 | 判 P5 |
| L3 | STATEMENT 风险 | 边界 | 不确定函数致主从不一致 | 判 P6 |
| L4 | 为何默认改 ROW | 版本翻转 | 5.7.7 起为一致性 | 判 P6+ |
| L5 | ROW 代价怎应对 | 架构判断 | 拆大事务、控批量行数 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ≤ 5.7.6 | 默认 **STATEMENT** | 老实例需显式改为 ROW |
| ≥ 5.7.7 | 默认改为 **ROW** | "新版本默认 ROW，为的是一致性" |
| 8.0 | 默认仍为 ROW；复制术语改 replica | 同上 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'binlog_format';      -- 5.7.7+ 默认 ROW
SET GLOBAL binlog_format = 'ROW';         -- 动态参数；复制环境切换需评估
```

```bash
# ROW 格式默认看不懂，加 -v/-vv 输出可读的行变更
mysqlbinlog -vv --start-datetime='2026-10-16 02:00:00' /data/mysqllog/mysql-bin.000012 | head -60
```

## ⚠️ 原文纠错
原文"statement 是 5.7 版本之前默认使用的格式"需更精确：翻转点是 **5.7.7**（5.7.7 起默认改为 ROW），不是整个 5.7。原文对三种格式的定义正确。机翻音译（inlogformot、liyment肉、mix、mysqlinlog）已还原为 binlog_format、STATEMENT、ROW、MIXED、mysqlbinlog。

## 总结与追问预判
- 三种格式；**ROW 自 5.7.7 起默认**，用日志量换一致性。
- 大批量更新在 ROW 下是复制延迟的常见诱因。
- 下一题：见 069（如何开启 binlog）、059（binlog_cache_size）。
