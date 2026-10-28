---
disableNunjucks: true
title: "714 GORM 显式事务与 Savepoint 部分回滚"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：数据库 / GORM | 难度：L3 | 题型：用法题 | 频率：中 | 关键词：**Begin** / **Savepoint** / **RollbackTo** / **部分回滚**
> 原文锚点：第 32~40,50 段「通过 ORM begin 开启事务；设保存点 step1；创建 user5 后回滚到 step1；最终 user5 插入、user4 回滚；也可 Rollback 全部」

## 一句话总述
GORM 显式事务 `tx := db.Begin()` 后，用 `tx.SavePoint("step1")` 打标记、`tx.RollbackTo("step1")` 只回滚该点之后的操作（保留之前已写的），最后 `tx.Commit()`；若 `tx.Rollback()` 则全部回滚。比回调式更细——能**精确控制回滚到哪个保存点**，而非整段 error 全滚。

## 面试官视角
- 考察意图：会不会做"部分回滚"、知不知道 Savepoint 与回调式的粒度差异
- P5 知 Begin/Commit/Rollback；P6 能讲 Savepoint+RollbackTo 部分回滚；P7 能讲"何时选显式式而非回调式"
- 红旗：以为回滚只能全有全无；在显式式里忘记 Commit 导致连接悬挂
- 惊艳点：点出"Savepoint 让你在长事务里只撤最近几步（如 user5 回滚、user4 保留），是比回调 error 更细的粒度" [源码]

## 主问答
**Q（面试官原话）：** 只想回滚事务里的某几步，怎么办？
**A：**
1. **打点+定点回滚**：`tx := db.Begin()` 后 `tx.SavePoint("step1")` 标记；中途 `tx.Create(&u5)` 出错就 `tx.RollbackTo("step1")`——**只撤 step1 之后的操作**，step1 之前写的（如 u4）保留，再 `tx.Commit()` [源码]。
2. **全滚用 Rollback**：不指定保存点直接 `tx.Rollback()` 则**全部回滚**（u4、u5 都不留）[源码]。
3. **选型对比**：回调式适合"整段成或不成"；显式式+Savepoint 适合"长事务里要保留前半段、只撤后半段"的精细场景 [边界]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 怎么部分回滚 | 概念 | Savepoint | P5 |
| L2 | RollbackTo 范围 | 机制 | 仅撤之后 | P6 |
| L3 | 全滚怎么写 | 边界 | Rollback | P6+ |
| L4 | 何时用显式式 | 选型 | 长事务细粒度 | P7 |
| L5 | 连接风险 | 实战 | 记得 Commit | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| GORM v2 | Savepoint 支持 | 显式式部分回滚长期成立 |

## 关键代码
```go
tx := db.Begin()
tx.Create(&u4)
tx.SavePoint("step1")   // 标记：之前的操作保留
tx.Create(&u5)
tx.RollbackTo("step1")  // 仅回滚 u5（step1 之后）
tx.Commit()             // u4 入库，u5 撤销
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（goRM→GORM、事物→事务、测刻→savepoint、隐射→映射、TS轴back→Rollback、uz四/user五→u4/u5 等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- 显式式+Savepoint 做部分回滚，比回调 error 更细；记得 Commit 防止连接悬挂。
- 回调式见 714；事务总览见 714。
