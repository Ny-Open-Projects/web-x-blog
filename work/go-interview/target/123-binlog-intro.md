# 123 binlog 概述与基础配置

> 分类：MySQL 日志 | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**binlog**/**mysqlbinlog**/**binlog_expire_logs_seconds**
> 原文锚点：第 53~77 段「binlog 概述、查看与保留配置」

## 一句话总述
binlog 是 MySQL **server 层**的二进制逻辑日志，记录所有更改数据的操作，用于备份恢复与主从复制，须用 `mysqlbinlog` 查看。

## 面试官视角
- 考察意图：必考——"binlog 是什么层、干嘛用、和 redo 区别"，本卡铺基础，实质差异见 12-4。
- 分档：P5 知 binlog 用于复制/恢复；P6 知 server 层+二进制；P7 知 8.0 默认压缩加密。
- 红旗答案：说 binlog 是 InnoDB 特有的、或直接 cat 能看。
- 惊艳点：点出 8.0 起 binlog 默认开启且默认压缩加密。

## 主问答
**Q（面试官原话）：** binlog 是什么，为什么重要？
**A：**
1. **所属层级与用途**：binlog 由 server 层生成、跨存储引擎，记 insert/update/delete 及 DDL；主用**备份恢复、主从同步**。
2. **查看方式**：二进制存储，必须 `mysqlbinlog <file>` 解析；8.0 起默认**压缩+加密**，直接 `cat` 是乱码。
3. **保留与大小**：`binlog_expire_logs_seconds` 默认 2592000 秒（**30 天**）自动清理；`max_binlog_size` 默认 **100MB**（写满切下个文件）。
4. **配置加载**：按 `default-options` 顺序从左到右读，**后出现覆盖先出现**，当前目录 `my.cnf` 优先级最高。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | binlog 哪层？ | 基础 | server 层跨引擎 | P5 |
| L2 | 为何 cat 看不了？ | 细节 | 二进制，需 mysqlbinlog；8.0 还压缩 | P6 |
| L3 | 默认保留多久？ | 数值 | 30 天 | P6 |
| L4 | 单个多大？ | 数值 | 默认 100MB 满则切 | P7 |
| L5 | 和 redo 根本区别？ | 进阶 | 见 12-4 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.7 及以前 | 8.0 起默认开启且默认压缩加密 | 8.0 答"默认开+压缩加密"；早期需手动开、不加密 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'binlog_expire_logs_seconds';
SHOW VARIABLES LIKE 'max_binlog_size';
```
```bash
mysqlbinlog /var/lib/mysql/binlog.000001
```

## 总结与追问预判
binlog 是 server 层逻辑日志，撑起复制与恢复；8.0 默认开且压缩加密，保留 30 天、单文件 100MB，配置"后读覆盖先读"。

## ⚠️ 原文纠错
1. 事实核校： [经验]binlog 为 server 层逻辑日志、8.0 默认压缩加密、expire 默认 30 天、max 默认 100MB、配置"后读覆盖先读"，均正确。
2. 崩坏词归一：beinlog/blogo/BNlog/BLlog/banlog/windog→binlog、dataDIL→datadir、blologexpelogseconds→binlog_expire_logs_seconds、博客纠GB(max)→max_binlog_size、wordlive→/var/lib/mysql。
