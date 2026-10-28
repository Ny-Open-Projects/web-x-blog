---
disableNunjucks: true
title: "1240 SHOW PROCESSLIST：锁等待排查的第一现场"
date: 2026-10-07 23:50:44
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：数据库 / MySQL 锁 | 难度：L3 | 题型：实操题 | 频率：高 | 关键词：**SHOW PROCESSLIST、连接 ID、STATE、INFO、information_schema**

> 原文锚点：第 1~24 段「显示哪些线程正在运行…如果当前用户有 SUPER 权限就可以看到所有的线程…如果有线程正在 update 或者是 insert 某个表，这个进程的 state 就是 updating 或者是 inserting…它的数据来源其实是 information_schema 里面的 processlist 这张表」

## 一句话总述
`SHOW PROCESSLIST` 列出当前所有连接线程的运行状态，是排查锁等待最直接的入口：看 `STATE` 是否含锁关键字、看 `TIME` 是否异常偏大、看 `INFO` 是哪条语句卡住。

## 面试官视角
P6 会说「用它看有哪些连接」；P7 必须能**逐列解释含义**并说出数据来源（`information_schema.PROCESSLIST`）、权限要求，以及**默认 Info 只显示前 100 字符、要看完整语句得加 `FULL`** 这个实战细节。

## 主问答
**Q（面试官原话）：** 线上说数据库卡住了，你第一条命令敲什么？结果每一列都代表什么？

1. **ID**：连接 ID，可用 `SELECT CONNECTION_ID()` 查当前连接的 ID，用于精确定位自身会话 `[源码]`。
2. **USER**：启动该线程的用户，如 root `[源码]`。
3. **HOST**：发送请求客户端的 **IP 与端口号**，据此可反查是哪个客户端进程 `[源码]`。
4. **DB**：当前线程**所选定的默认数据库**；若连接后未指定库则为 NULL。注意它是「当前选择的库」，而非语句实际操作的库 `[源码]`。
5. **COMMAND**：当前命令类型，如 `Query`、`Sleep` `[源码]`。
6. **TIME**：该状态已持续的**秒数**，数值异常大即为可疑长事务 `[源码]`。
7. **STATE**：操作状态；**出现锁相关关键字即说明该语句正被其他操作阻塞**；执行写入时常见 updating 或 inserting `[源码]`。
8. **INFO**：正在执行的语句，默认只显示前 100 个字符，需看完整语句用 `SHOW FULL PROCESSLIST` `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 排查锁等待先看什么？ | 答不出 SHOW PROCESSLIST |
| L2 | 哪几列最关键？ | 答不出 STATE / TIME / INFO |
| L3 | 想要完整 SQL 怎么办？ | 答不出加 FULL |
| L4 | 数据来源是哪张表？ | 答不出 information_schema.PROCESSLIST |
| L5 | DB 列的含义陷阱？ | 答不出「当前选择的库，非语句操作的库」 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 5.x / 8.0 | 列名与语义基本一致 | 按 ID/USER/HOST/DB/COMMAND/TIME/STATE/INFO 作答 |
| 5.7 起 | information_schema 部分视图被 performance_schema 取代 | processlist 表仍可用 |
| 8.0 起 | 查看全部线程需 PROCESS 权限 | 传统说法为 SUPER 权限 |
| 所有版本 | Info 截断 | 默认 100 字符，FULL 看全量 |

## 关键代码
```sql
-- 查看当前所有线程（INFO 列截断为前 100 字符）
SHOW PROCESSLIST;

-- 查看完整语句
SHOW FULL PROCESSLIST;

-- 等价的 SQL 查询方式，便于过滤与聚合
SELECT ID, USER, HOST, DB, COMMAND, TIME, STATE, INFO
FROM information_schema.PROCESSLIST
WHERE COMMAND <> 'Sleep'
ORDER BY TIME DESC;

-- 查看当前连接的 ID
SELECT CONNECTION_ID();
```

## 总结与追问预判
**看锁等待三件套：STATE 含锁关键字、TIME 偏大、INFO 是被阻塞的语句**。追问常是「看不到全部语句怎么办」——加 `FULL`；「想按条件过滤怎么办」——直接查 `information_schema.PROCESSLIST`。聚合分析见同批 1240-processlist-agg。

## ⚠️ 原文纠错
1. 事实核校：线程列表、SUPER/PROCESS 权限、writing 状态、HOST 含端口、DB 为当前选择库、TIME 单位为秒、STATE 含锁关键字——均与 MySQL 官方手册一致 `[经验]`。
2. 补充：原文称「只能列出前一百条数据」表述不准——真正被截断的是 **INFO 列的 100 个字符**，而非只返回 100 行；要看完整语句应使用 `SHOW FULL PROCESSLIST` `[经验]`。
3. 崩坏词归一：源码将若干 MySQL 命令名、系统库名与状态关键字音译为多组崩坏词，本卡统一为规范写法 `[经验]`。
