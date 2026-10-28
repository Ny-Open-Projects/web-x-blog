---
disableNunjucks: true
title: "016 SET PERSIST 在线持久化"
date: 2026-10-15 23:19:07
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：MySQL 8.0 新特性/配置 | 难度：L2 | 题型：概念主问 | 频率：低 | 关键词：**SET PERSIST** / **在线改参数** / **重启不丢失**
> 原文锚点：第 277~279 段「8.0 在线改系统变量可选持久化，重启不丢失」

## 一句话总述
MySQL 8.0 支持 **SET PERSIST**：在线修改系统变量并**持久化到 `mysqld-auto.cnf`**，重启后不丢失——解决「运行时改了但配置文件没改、重启配置不一致」的老问题。

## 面试官视角
- **考察意图**：是否了解 8.0 配置管理的改进。
- **P5** 知道 8.0 能持久化改参数。
- **P6** 能区分 `SET PERSIST` 与 `SET GLOBAL`、以及 `PERSIST_ONLY`。
- **P7** 能讲持久化文件与配置文件优先级、回滚方式。
- **红旗**：说「SET GLOBAL 也会重启生效」。
- **惊艳点**：点出 `SET PERSIST_ONLY` 只写文件不改运行值，适合需重启的参数 `[源码]`。

## 主问答
**Q：8.0 的 SET PERSIST 有什么用？**
**A：**
1. **结论**：`SET PERSIST var=val` 在线改参数并写入 `mysqld-auto.cnf`，**重启仍生效**；`SET PERSIST_ONLY` 只写文件不改当前运行值。
2. **机制**：之前 `SET GLOBAL` 重启即丢，易产生「运行值与配置不一致」的性能隐患；PERSIST 把两者统一。
3. **边界**：`auto.cnf` 优先级高于 `my.cnf` 同名项；要回退需 `RESET PERSIST` 或删文件，不能只改 my.cnf。
**加分层**：变更前先 `PERSIST_ONLY` 评估、择机重启，是可灰度手法。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | PERSIST 干啥 | 概念 | 持久化改参 | 换题 |
| L2 | 和 GLOBAL 区别 | 基础 | 重启是否生效 | 判 P5 |
| L3 | PERSIST_ONLY 呢 | 原理 | 只写文件不改运行 | 判 P6 |
| L4 | 优先级/回滚 | 工程 | auto.cnf>my.cnf | 判 P6+ |
| L5 | 线上管过吗 | 实战 | 讲配置漂移案例 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| MySQL 8.0+ | SET PERSIST 自 8.0 引入 | 按上述答；5.7 无持久化 |

## 关键代码
```sql
SET PERSIST max_connections = 1000;        -- 运行+持久化
SET PERSIST_ONLY innodb_buffer_pool_size = '4G'; -- 仅持久化，需重启
RESET PERSIST max_connections;            -- 撤销持久化
```

## ⚠️ 原文纠错
未发现技术性错误。机翻「安度表空间/表演ancesilmer」已还原为 undo 表空间/performance_schema。

## 总结与追问预判
- SET PERSIST 统一运行值与配置文件，消除配置漂移。
- 下一题：见 015（角色）、011（8.0 安全）。
