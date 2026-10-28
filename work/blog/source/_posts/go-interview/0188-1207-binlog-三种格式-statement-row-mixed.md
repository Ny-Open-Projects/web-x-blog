---
disableNunjucks: true
title: "1207 binlog 三种格式：statement / row / mixed"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：数据库内核 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**statement** / **row** / **mixed**
> 原文锚点：第 5~18 段「binlog 有三种格式，包括 statement 格式 row 格式以及 mix 格式」

## 一句话总述
binlog 记录数据变更，有三种格式：statement 记 SQL 原文、row 记每行改动、mixed 自动选；现代 MySQL 默认 row，因为它对复制最安全。

## 面试官视角
- 意图：是否理解三种格式的取舍与何时切换。
- P5 说清三格式区别 / P6 懂 row 默认且知 statement 的不确定性 / P7 知 mixed 自动切 row 的触发条件与生产选型。
- 红旗：说 row 省空间；说 statement 永远一致。
- 惊艳点：含 UUID/now/rand 或临时表时 mixed 必切 row，否则主从数据漂移 —— 验证 `[外部/MySQL]`。

## 主问答
**Q（面试官原话）：** binlog 有哪几种格式？各自什么优缺点？
**A：**
1. **结论**：statement 记原始 SQL、row 记每行变更、mixed 二者折中，默认 row。
2. **机制**：statement 省日志量但依赖执行结果确定（now/rand/UUID 在主从可能不一致）；row 按行记录保证复制准确，但 DDL 全表改会造成巨量日志。
3. **边界**：mixed 对普通操作记 statement，遇到无法保证复制一致（NDB、UUID/USER/FOUND_ROWS/ROW_COUNT、INSERT DELAYED、UDF、临时表）时自动切 row。
**加分层：** 生产优先 row（安全）并配 binlog_row_image=MINIMAL 控日志量。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 三格式 | 概念 | statement/row/mixed | 换题 |
| L2 | row 默认 | 机制 | 复制准确 | 判 P5 |
| L3 | 何时切 row | 边界 | 不确定函数 | 判 P6 |
| L4 | 日志量权衡 | 权衡 | minimal | 判 P6+ |
| L5 | 主从漂移 | 实战 | 函数不确定 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 5.7.7+ 默认 row `[外部/MySQL][经验]` | 5.7.7 前默认 statement | 默认 row，mixed 仅作兼容 |

## 关键代码
```sql
-- 查看与设置格式（示意，未验证）
SHOW VARIABLES LIKE 'binlog_format';
SET GLOBAL binlog_format = 'ROW';
```

## 总结与追问预判
- statement 省空间但不确定、row 最安全默认、mixed 自动切。
- 预判：刷盘时机 → 见 1207；写入流程 → 见 1207。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对各格式优劣与 mixed 自动切 row 的触发条件；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
