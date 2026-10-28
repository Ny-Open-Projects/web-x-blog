---
disableNunjucks: true
title: "077 binlog 怎么清理：自动过期与手动 PURGE"
date: 2026-10-16 03:47:08
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：日志类 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**expire_logs_days** / **binlog_expire_logs_seconds** / **PURGE BINARY LOGS**
> 原文锚点：第 409~418 段「二进制日志的数据量就会不断的增长，所以我们必须要定期的对二进制日志进行清理…我们可以设置 expire_logs_days 参数来设置二进制日志的过期时间」

## 一句话总述
binlog 只增不减，**自动过期**（`expire_logs_days` / `binlog_expire_logs_seconds`）或**手动 PURGE BINARY LOGS**（按文件名/按时间点）二选一，清理前**先备份**。

## 面试官视角
- **考察意图**：磁盘被 binlog 打满是最常见运维事故，看你有没有清理策略。
- **P5** 知道要定期清理 / **P6** 能说全自动与手动两条路 / **P7** 会讲"过期时间要**大于**最慢从库的延迟窗口 + 备份周期"，并知道 8.0 换成了秒级变量。
- **红旗**：① 直接 `rm` 删文件（索引与实例状态会错乱）；② 用 `RESET MASTER` 当清理手段；③ 过期时间设得比备份周期还短。
- **惊艳点**：设过期时间的判据是 **"从库最坏延迟 + 一次全备间隔"** `[经验]`。验证：`SHOW SLAVE STATUS` 的落后量与备份频率对齐。

## 主问答
**Q（面试官原话）：** binlog 把磁盘撑爆了，你怎么处理？

**A：**
1. **先给结论**：配自动过期（8.0 用 `binlog_expire_logs_seconds`），紧急时用 `PURGE BINARY LOGS` 手动删；**清前先备份**。
2. **再给机制**：`expire_logs_days` 是**动态参数**，MySQL 在**日志轮转或实例启动**时清理已过期文件；`PURGE BINARY LOGS TO 'mysql-bin.000010'` 删除该文件**之前**的所有日志（保留 000010 本身），`PURGE BINARY LOGS BEFORE '2026-10-16 00:00:00'` 按时间点删。
3. **最后给边界**：**不要用操作系统 `rm` 直接删**（`mysql-bin.index` 与实例认知会不一致）；`RESET MASTER` 是**清空全部**并重置序号，只应在初始化的场景用；过期时长必须覆盖**从库延迟 + 全备周期**，否则从库要的日志已被删、备份也补不回来。

**加分层**：删除正在被从库读取的 binlog 会直接让复制报错中断——这也是"过期时间 > 延迟窗口"的硬约束来源。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | binlog 会自己删吗 | 概念 | 不会，需配置或手动 | 换题 → 不及格 |
| L2 | 自动清理怎么配 | 参数 | expire_logs_days / seconds | 判 P5 |
| L3 | 手动清用什么命令 | 操作 | PURGE BINARY LOGS | 判 P6 |
| L4 | 为什么不能 rm | 边界 | index 与实际不一致 | 判 P6+ |
| L5 | 过期时间怎么定 | 设计 | 覆盖延迟与备份周期 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 变化点 | 现在该怎么答 |
|---|---|---|
| 5.7 | expire_logs_days（天，默认 0） | 老版本通用 |
| 8.0.x | 新增 binlog_expire_logs_seconds（秒） | 优先用秒级变量 |
| ≥ 8.0.28 | 秒级变量默认 2592000（30 天） `[经验]` | "8.0.28 起默认 30 天" |

## 关键代码
```sql
SHOW VARIABLES LIKE 'expire_logs_days';
SET GLOBAL binlog_expire_logs_seconds = 604800;      -- 8.0 推荐，7 天
PURGE BINARY LOGS TO 'mysql-bin.000010';             -- 删 000010 之前
PURGE BINARY LOGS BEFORE '2026-10-16 00:00:00';      -- 按时间点删
SHOW BINARY LOGS;
```

```bash
# 切新文件后再 PURGE，是紧急释放空间的常用顺序
mysql -uroot -p -e "FLUSH LOGS; PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 3 DAY);"
```

## ⚠️ 原文纠错
原文只讲了 `expire_logs_days` 天级参数，未提 **8.0 的 `binlog_expire_logs_seconds` 秒级变量**（8.0.28 起默认 30 天），卡面已补充并标 `[经验]`；原文"清理前最好先备份""PURGE 两种形式"的描述正确。机翻「extraloss」「扩置dinarylovesto」「pot单日lototomyCQ」还原为 expire_logs_days、PURGE BINARY LOGS、/path/mysql-bin。核对范围：第 409~418 段。

## 总结与追问预判
- 清理三件套：**自动过期 / PURGE / 先备份**；**禁止 rm、慎用 RESET MASTER**。
- 过期时长 = 从库最坏延迟 + 全备周期。
- 下一题：见 078（日志轮转）、072（relay log 清理）。
