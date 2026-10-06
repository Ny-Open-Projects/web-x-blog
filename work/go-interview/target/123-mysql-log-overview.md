# 123 MySQL 四大日志总览

> 分类：MySQL 日志 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**错误日志**/**慢查询日志**/**通用查询日志**/**binlog**
> 原文锚点：第 1~113 段「MySQL 中有哪些日志及重要配置」

## 一句话总述
MySQL 主要有**错误日志、慢查询日志、通用查询日志、二进制日志（binlog）**四类，分别服务于诊断、优化、审计与复制/恢复。

## 面试官视角
- 考察意图：能否说清四类日志的定位，并理解 binlog 是后续 redo 对比与主从复制的前提。
- 分档：P5 知四类名字；P6 知各自用途；P7 能把 binlog 与 redo 的关系讲清。
- 红旗答案：把 binlog 当成"错误日志"或"慢日志"的别名。
- 惊艳点：点出 binlog 是 **server 层、跨存储引擎**，与 InnoDB 的 redo 职责不同。

## 主问答
**Q（面试官原话）：** MySQL 有哪几类日志，分别干什么？
**A：**
1. **错误日志（error log）**：记启动、运行、关闭中的异常（崩溃、表损坏、参数错误），用 `log_error` 指定路径、`perror` 查错误码。
2. **慢查询日志（slow query log）**：记超过 `long_query_time` 的 SQL，是性能优化第一抓手，用 `mysqldumpslow` 聚合。
3. **通用查询日志（general log）**：记所有连接/断开/每条 SQL，量大，**生产慎开**，默认关、默认落系统盘。
4. **二进制日志（binlog）**：server 层逻辑日志，记所有更改数据的操作，用于**备份恢复与主从复制**，需 `mysqlbinlog` 查看。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 四类日志干嘛？ | 定位 | 诊断/优化/审计/复制 | P5 |
| L2 | 哪类不能随便开？ | 风险 | general log 量大 | P6 |
| L3 | binlog 哪层？ | 架构 | server 层跨引擎 | P6 |
| L4 | binlog 和错误日志区别？ | 区分 | 变更复制 vs 服务异常 | P7 |
| L5 | 为何有 binlog 还要 redo？ | 进阶 | 见 12-4 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.5+ | 8.0 将 `log_warnings` 改名 `log_error_verbosity` | 答四类日志定位；binlog 实质差异归 12-4 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'log_error';
SHOW VARIABLES LIKE 'slow_query%';
SHOW VARIABLES LIKE 'general_log%';
```

## 总结与追问预判
四类日志定位不同：错误日志看服务健康、慢日志找慢 SQL、通用日志全量审计、binlog 支撑复制与恢复。binlog 是后续 redo 对比与主从一致性的核心，实质差异见 12-4。

## ⚠️ 原文纠错
1. 事实核校： [经验]四类日志定义与用途、8.0 将 `log_warnings` 更名为 `log_error_verbosity`（默认 2），均正确。
2. 标题标"（一）"但实际只铺日志体系与 binlog 配置，redo/binlog 实质差异在 12-4（二），本卡不重复。
3. 崩坏词归一：redolog/radiolog→redo log、inlog/和inlog→binlog、circle→SQL、漫长日志→慢查询日志、mysqldumpsnow→mysqldumpslow、马刺go八点零→MySQL 8.0、PIL→perror、wordlive→/var/lib/mysql。
