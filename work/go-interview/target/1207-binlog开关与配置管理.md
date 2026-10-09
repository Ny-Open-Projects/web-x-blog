# 1207 binlog 开关与配置管理

> 分类：数据库内核 | 难度：L1 | 题型：八股题 | 频率：中 | 关键词：**log_bin** / **binlog_format** / **skip-log-bin**
> 原文锚点：第 29~58 段「binlog_format 配置项、log_bin、skip-log-bin、SHOW BINARY LOGS、PURGE」

## 一句话总述
binlog 在 mysqld 段用 binlog_format/log_bin 配置，MySQL 8.0 默认开启；可用 SHOW BINARY LOGS、SHOW MASTER STATUS 查看，用 PURGE/RESET MASTER 管理。

## 面试官视角
- 意图：是否实际配过、查过、清理过 binlog。
- P5 会开关 / P6 知 log_bin 与 log_bin_basename 区别 / P7 知 PURGE 不影响在跑从库。
- 红旗：以为 skip-log-bin 是默认开启；混淆 log_bin 下划线与 log-bin 中横线。
- 惊艳点：log_bin 用下划线、log-bin 用中横线是两条不同配置，别记反 —— 验证 `[外部/MySQL]`。

## 主问答
**Q（面试官原话）：** 怎么开启和查看 binlog？
**A：**
1. **结论**：`log_bin=ON` 并设 `log_bin_basename` 即开启；MySQL 8.0 默认开。
2. **机制**：`binlog_format` 设格式；`log_bin_index` 记录所有 binlog 位置；`skip-log-bin` 可关闭。
3. **边界**：`log_bin`（下划线）是状态/开启键，`log-bin`（中横线）是路径基名配置，二者不是同一项。
**加分层：** 生产定期 PURGE BEFORE 清理，避免磁盘被 binlog 填满。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么开 | 概念 | log_bin | 换题 |
| L2 | 默认开吗 | 机制 | 8.0 默认 | 判 P5 |
| L3 | 查看命令 | 边界 | SHOW BINARY LOGS | 判 P6 |
| L4 | 清理风险 | 权衡 | PURGE/RESET | 判 P6+ |
| L5 | 清理误伤从库 | 实战 | 复制位点 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 8.0 默认开 `[外部/MySQL][经验]` | 5.7 及以前默认可能关闭 | 8.0 下 log_bin ON 是默认 |

## 关键代码
```sql
-- 查看与清理 binlog（示意，未验证）
SHOW VARIABLES LIKE 'log_bin';
SHOW BINARY LOGS;
SHOW MASTER STATUS;
PURGE BINARY LOGS BEFORE '2023-12-18 00:00:00';
```

## 总结与追问预判
- log_bin 开、binlog_format 选格式、SHOW/PURGE 管理；下划线≠中横线。
- 预判：格式选型 → 见 1207；刷盘 → 见 1207。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 log_bin / binlog_format / skip-log-bin 与 SHOW、PURGE 命令拼写；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
