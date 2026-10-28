---
disableNunjucks: true
title: "046 SESSION 与 GLOBAL 作用域"
date: 2026-10-16 00:53:10
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：服务器配置 | 难度：L3 | 题型：排障题 | 频率：高 | 关键词：**SET SESSION** / **SET GLOBAL** / **只对新建连接生效**
> 原文锚点：第 209~228 段「SET GLOBAL 修改后，所有在修改之后新建的连接都会使用新的配置参数…对当前 session 使用的变量值并不会修改」

## 一句话总述
`SET SESSION` 只影响**当前线程**，`SET GLOBAL` 影响全局但**只作用于之后新建的连接**，**当前会话不变**——所以改完 `wait_timeout` 后自己这条连接还是老值。

## 面试官视角
- **考察意图**：这是"我明明改了参数，怎么没生效"的标准答案，考的是作用域理解。
- **P5** 知道有 session 级与 global 级两种改法。
- **P6** 能说清 GLOBAL 改后**当前会话不变、新连接才生效**。
- **P7** 能指出**并非所有变量都有 session 级**（如 `max_connections` 只能全局），以及 `wait_timeout` 这类需要**两级都设**才对当前连接生效。
- **红旗**：① 改完 GLOBAL 就以为当前连接也变了；② 对 `max_connections` 用 `SET SESSION`；③ 不知道要重连验证。
- **惊艳点**：`wait_timeout` 需**同时设 GLOBAL 和 SESSION** 才能对当前连接生效；只看 `SHOW VARIABLES` 会被当前会话值误导 `[经验]` —— 验证：`SHOW GLOBAL VARIABLES` 与 `SHOW VARIABLES` 对比即可看出层级差异。

## 主问答
**Q（面试官原话）：** 我执行了 `SET GLOBAL wait_timeout=300`，为什么我这个连接看到的还是 28800？

**A：**
1. **结论**：因为 **GLOBAL 只影响修改之后新建的连接**，当前会话的变量值**不会回溯改变**。
2. **机制**：变量按作用域取值——会话建立时从全局值**拷贝**一份；之后全局再改，已存在的会话不重新读取。
3. **边界**：要让当前连接也生效，需**再执行一次 `SET SESSION wait_timeout=300`**，或断开重连；另外 `max_connections` 这类影响整机的变量**只有全局级，没有会话级**。

**加分层**：验证改动是否落全局，要用 `SHOW GLOBAL VARIABLES`，而不是 `SHOW VARIABLES`（后者默认显示会话值）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 有几个作用域 | 概念 | SESSION / GLOBAL | 换题 → 不及格 |
| L2 | GLOBAL 改了当前会话变吗 | 核心机制 | 不变，只影响新连接 | 判 P5 |
| L3 | 怎么让当前连接也变 | 处置 | 再 SET SESSION 或重连 | 判 P6 |
| L4 | 所有变量都有会话级吗 | 边界 | 不是，如 max_connections | 判 P6+ |
| L5 | 怎么验证改动生效 | 排查手法 | SHOW GLOBAL VARIABLES | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.7 及之前 | 仅 SESSION / GLOBAL 两级 | 按"改全局 + 手工同步配置文件"答 |
| 8.0 | 增加 `SET PERSIST`，把修改持久化到 `mysqld-auto.cnf` | 现在补一句"8.0 用 PERSIST 防重启丢失" |

## 关键代码
```sql
SET GLOBAL wait_timeout = 300;
SHOW VARIABLES LIKE 'wait_timeout';         -- 仍是 28800（会话值未变）
SHOW GLOBAL VARIABLES LIKE 'wait_timeout';  -- 300（全局已改）
SET SESSION wait_timeout = 300;             -- 让当前连接也生效
```

## ⚠️ 原文纠错
原文演示 `wait_timeout` 默认 28800 秒、设 GLOBAL 后当前 session 仍为 28800——与 MySQL 行为一致，未发现技术错误。补充一点原文未强调的：验证全局值应使用 `SHOW GLOBAL VARIABLES`，直接 `SHOW VARIABLES` 看到的是会话值。机翻音译（watertimeboat、shoplogovariables）已还原为 wait_timeout、SHOW GLOBAL VARIABLES。

## 总结与追问预判
- GLOBAL 改后**当前会话不变**，只影响新建连接；需再 `SET SESSION` 或重连。
- 验证用 `SHOW GLOBAL VARIABLES`；`max_connections` 无会话级。
- 下一题：见 045（动态 vs 只读参数）、047（配置漂移检测）。
