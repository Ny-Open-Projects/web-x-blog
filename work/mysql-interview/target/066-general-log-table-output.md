# 066 general_log 表输出与密码安全

> 分类：日志类 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**mysql.general_log** / **CSV 引擎** / **密码不明文**
> 原文锚点：第 171~180 段「general_log 除了可以保存在日志文件中之外，还可以保存在 MySQL 的表中…这个表是 CSV 存储引擎的表，密码的明文是不会被记录到日志中的」

## 一句话总述
`log_output=TABLE` 时通用日志写入 **`mysql.general_log`** 表（**CSV 引擎**，可直接 SQL 查询）；表/文件内容都**不记录密码明文**，用完需 `TRUNCATE` 清理。

## 面试官视角
- **考察意图**：考"日志能不能直接查"这个实用技巧，以及你对**日志里会不会泄露密码**这个安全问题的判断。
- **P5** 知道日志可以落到表里。
- **P6** 能说出表名 `mysql.general_log`、CSV 引擎、可用 SQL 检索。
- **P7** 能主动澄清**密码不会被明文记录**，并说明用完要 `TRUNCATE`、文件会归零。
- **红旗**：① "开通用日志会泄露密码"；② 用 `DELETE` 清大表（慢且不回收）；③ 说表是 InnoDB。
- **惊艳点**：`mysql.general_log` 是 **CSV** 引擎表，物理上就是数据目录下的 CSV 文件，所以 `TRUNCATE` 后**文件大小立刻归零** `[经验]` —— 验证：`TRUNCATE` 前后 `ls -l mysql/general_log.CSV`。

## 主问答
**Q（面试官原话）：** 通用日志能不能直接查？开启的话密码会不会被记下来？

**A：**
1. **先给结论**：能。设 `log_output=TABLE` 后日志进 `mysql.general_log`，可直接用 SQL 过滤；**密码明文不会被记录**。
2. **再给机制**：该表是 **CSV 存储引擎**（不是 InnoDB），落在数据目录下以 CSV 文件形式存在；字段包含事件时间、用户主机、线程 ID、服务器 ID、命令类型与语句内容。
3. **最后给边界**：用完必须清理——对表用 `TRUNCATE`（不是 `DELETE`，见 060 卡），清理后底层 CSV 文件**大小归零**；同时别长期开，通用日志的量级问题不因存表而消失。

**加分层**：表输出的好处是**可以用 SQL 精确筛查**（按用户、按时间、按语句模式），比 grep 文件高效——这正是排查时值得切 TABLE 的理由。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 日志能存到表里吗 | 概念 | mysql.general_log | 换题 → 不及格 |
| L2 | 用什么引擎 | 机制 | CSV | 判 P5 |
| L3 | 密码会不会泄露 | 安全边界 | 明文不记录 | 判 P6 |
| L4 | 怎么清理 | 工程判断 | TRUNCATE，文件归零 | 判 P6+ |
| L5 | 什么时候选表输出 | 权衡 | 需 SQL 精确筛查时 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 5.6 / 5.7 | `log_output` 支持 FILE / TABLE / NONE | "可选文件、表或两者" |
| 8.0 | 语义不变；`mysql.general_log` 仍为 CSV 引擎 | 同上 |

## 关键代码
```sql
SET GLOBAL log_output = 'TABLE';        -- 或 'FILE'，或 'FILE,TABLE'
SET GLOBAL general_log = ON;

-- 直接 SQL 筛查（比 grep 文件高效）
SELECT event_time, user_host, argument
FROM mysql.general_log
WHERE argument LIKE '%UPDATE orders%'
ORDER BY event_time DESC LIMIT 20;

-- 用完清理：TRUNCATE 而非 DELETE
SET GLOBAL general_log = OFF;
TRUNCATE TABLE mysql.general_log;
```

## ⚠️ 原文纠错
原文"密码的明文不会被记录到日志中"正确（`CREATE USER ... IDENTIFIED BY` 的密码在日志中被改写/不落明文），未发现技术错误。补充原文未点名的参数：切换输出目标靠 **`log_output`**（FILE/TABLE/NONE），原文只描述了结果未给出参数名。机翻音译（jerulogg、jneylog、铭文、战略vlog）已还原为 general_log、general_log、明文、general_log。

## 总结与追问预判
- 表输出 = **可 SQL 筛查**；CSV 引擎、`TRUNCATE` 即归零。
- 密码**不明文**落日志，但仍应按敏感数据管控日志访问。
- 下一题：见 065（通用日志代价）、067（慢查询日志）。
