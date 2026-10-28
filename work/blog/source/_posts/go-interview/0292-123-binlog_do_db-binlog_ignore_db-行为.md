---
disableNunjucks: true
title: "123 binlog_do_db / binlog_ignore_db 行为"
date: 2026-10-06 18:43:24
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：MySQL 日志 | 难度：L3 | 题型：陷阱题 | 频率：中 | 关键词：**binlog_do_db**/**binlog_ignore_db**/**STATEMENT**/**ROW**
> 原文锚点：第 78~113 段「binlog_do_db 与 binlog_ignore_db 行为」

## 一句话总述
`binlog_do_db`/`binlog_ignore_db` 控制"哪些库的变更写 binlog"，其行为**严重依赖 binlog 格式（STATEMENT/ROW）与当前 USE 的库**，是经典坑。

## 面试官视角
- 考察意图：高频陷阱——"配了 ignore 为什么还记了？"核心是 statement 看"当前库"、row 看"实际表库"。
- 分档：P5 知两参数互斥；P6 知 statement 看当前库；P7 知 row 看实际表库。
- 红旗答案：以为 ignore 配了就一定不记，不论怎么 USE。
- 惊艳点：点出 statement 下"未 USE 则 do_db 全失效"。

## 主问答
**Q（面试官原话）：** 配了 binlog_ignore_db=test，为什么 test 的变更还是进了 binlog？
**A：**
1. **互斥二选一**：`binlog_do_db=db` 只记该库；`binlog_ignore_db=db` 不记该库；多库写多行。
2. **STATEMENT 看"当前库"（USE 的库）**：**未 USE 任何库时 do_db 不生效，所有库都记**；USE 进被 ignore 的库操作它→不记，但跨库操作其他库→也不记（在当前库空间下）；USE 进未配 ignore 的库→所操作都记。
3. **ROW 看"实际变更表的库"**：DDL 始终记，DML 按真实表所属库过滤；在 ignore 库空间下跨库操作→只记 DML 不记 DDL，反之只记 DDL 不记 DML。
4. **实践建议**：`binlog_ignore_db` 更常用（如排除不重要的库减负），但 statement 下务必 USE 目标库，否则过滤失效。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 两参数为何互斥？ | 基础 | 一个只记一个不记 | P5 |
| L2 | statement 下没 USE 会怎样？ | 陷阱 | do_db 失效全记 | P6 |
| L3 | statement 下 USE ignore 库跨库？ | 陷阱 | 都不记 | P6 |
| L4 | row 与 statement 过滤依据？ | 区分 | row 看实际表库 | P7 |
| L5 | 生产怎么配最稳？ | 进阶 | ROW+显式 USE 或靠权限 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.7/8.0 | 无 | ROW 下过滤更稳定；STATEMENT 下极易踩坑，务必显式 USE |

## 关键代码
```ini
# my.cnf
binlog_ignore_db = test        # 不记录 test 库 binlog
# 或
binlog_do_db = app_db          # 只记录 app_db
```

## 总结与追问预判
do_db/ignore_db 生效取决于格式与 USE——STATEMENT 看"当前库"、ROW 看"真实表库"；生产优先 ROW + 显式 USE，避免 statement 下过滤意外失效。

## ⚠️ 原文纠错
1. 事实核校： [经验]STATEMENT 下"未 USE 则 do_db 不生效、所有库都记""USE ignore 库后跨库操作亦不记"、ROW 下按实际表库过滤且仅 DDL 必记，均符合 MySQL 官方行为，正确。
2. 崩坏词归一：blogUGB→binlog_do_db、BNlog一个logb/一个logDB/一个落地→binlog_ignore_db、一个low/一个落/一个law/gload→ignore_db、右子/右次/柚子→USE、lodML/GML→DML、GDL/DDL→DDL、银色→insert、增删感→增删改、肉→ROW、钛色库→test 库、twodatabes→show databases。
