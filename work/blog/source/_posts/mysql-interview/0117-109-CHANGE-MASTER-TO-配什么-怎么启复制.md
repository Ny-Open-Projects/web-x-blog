---
disableNunjucks: true
title: "109 CHANGE MASTER TO 配什么、怎么启复制"
date: 2026-10-16 06:37:58
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：架构/复制 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**CHANGE MASTER TO** / **MASTER_AUTO_POSITION** / **明文密码** / **START SLAVE**
> 原文锚点：第 148~158 段「最基本的需要指定 master 实例的 IP 地址、master_user 和 master_password」

## 一句话总述
配复制链路本质上就是给 **IO 线程**填「连谁、用什么账号、从哪个位点（或哪组 GTID）开始拉」，配完再 `START SLAVE` 拉起两个线程。

## 面试官视角
- **考察意图**：是不是只会复制粘贴一条命令，能不能说清每个参数的用途与风险。
- **P5** 能写出主机+账号+密码三件套 / **P6** 知道 GTID 下换成 `MASTER_AUTO_POSITION=1` 且**不需要**位点 / **P7** 会主动提「明文密码会落进 `master_info` 文件/表，是安全隐患」。
- **红旗**：「GTID 模式也要指定文件和偏移量」；「密码明文写进去没关系」；「`START SLAVE` 只启动一个线程」。
- **惊艳点**：`CHANGE MASTER TO` 里的密码会明文存进 `mysql.slave_master_info` 表（当 `master_info_repository=TABLE` 时），有该库读权限的人就能看到 —— 验证：`SELECT User_name, User_password FROM mysql.slave_master_info;`（8.0.36 `[经验]`）。

## 主问答
**Q：配置复制链路要执行哪些命令？GTID 模式下有什么不同？**
**A：**
1. **先给结论**：`CHANGE MASTER TO` 配链路参数 → `START SLAVE` 启线程 → `SHOW SLAVE STATUS\G` 看 `Slave_IO_Running` / `Slave_SQL_Running` 双 Yes。
2. **再给机制**：日志点模式要显式给 `MASTER_LOG_FILE` + `MASTER_LOG_POS`；GTID 模式改给 **`MASTER_AUTO_POSITION=1`**，从库把自己已执行的 GTID 集发给主库，由主库算差量，省掉人工找位点。
3. **最后给边界**：`MASTER_AUTO_POSITION=1` **必须两端都开 GTID**，一侧没开直接报错；改链路前要先 `STOP SLAVE`。
**加分层**：账号密码写进 `CHANGE MASTER TO` 会明文落盘，生产建议配合只读权限账号 + 限制 `mysql` 系统库访问，别用高权限账号做复制。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 启复制的命令 | 概念 | CHANGE MASTER TO + START SLAVE | 换题 |
| L2 | 最少要几个参数 | 基础 | 主机 + 账号 + 密码 | 判 P5 |
| L3 | GTID 下还用位点吗 | 机制 | 不用，用 AUTO_POSITION | 判 P6 |
| L4 | 密码存在哪 | 安全 | slave_master_info 明文 | 判 P6+ |
| L5 | 改链路前要做什么 | 实战 | 先 STOP SLAVE 再改 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | **8.0.23 起术语改名为 `SOURCE_*`/`REPLICA`**：`CHANGE REPLICATION SOURCE TO`、`START REPLICA`，旧名仍兼容 | 新环境写新名，老环境旧名，两种都要认得 |

## 关键代码
```sql
-- GTID 模式：不需要位点，只需 AUTO_POSITION
CHANGE MASTER TO
  MASTER_HOST='192.168.1.91',
  MASTER_USER='repl',
  MASTER_PASSWORD='***',
  MASTER_AUTO_POSITION=1;
START SLAVE;
-- 验收：两个 Running 都必须是 Yes，Seconds_Behind_Master 趋近 0
SHOW SLAVE STATUS\G
```

## ⚠️ 原文纠错
原文提到「现在的 master 版本中出于安全考虑，不建议把复制用户的账号密码保存在 master_info 中」但未展开——实际机制是：`master_info_repository=TABLE` 时明文落入 **`mysql.slave_master_info` 表**，改为 FILE 时落入 `master.info` 文件，**两者都是明文**；已按实际存储方式重写。机翻「趁着master」「masself」还原为 **`CHANGE MASTER TO` / `START SLAVE`**。

## 总结与追问预判
- 链路三件套 + GTID 一个开关，验收看双 Yes。
- 下一题：见 098（日志点 vs GTID 选型）、110（半同步怎么开）。
