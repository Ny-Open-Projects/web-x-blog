# 1229 事务访问模式与事务 ID 分配

> 分类：MySQL 事务 | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**READ ONLY** / **READ WRITE** / **事务 ID** / **InnoDB**
> 原文锚点：第 1~15 段「仅 InnoDB/NDB 支持事务；只读事务不可改普通表但可改临时表；只有对事务表做增删改才分配事务 ID」

## 一句话总述
MySQL 事务分只读（READ ONLY）与读写（READ WRITE，默认）两种访问模式；InnoDB 并不是一开启事务就分配事务 ID，而是**只有当事务对事务表做了增删改**才分配唯一 trx_id，纯查询不分配。

## 面试官视角
- 意图：考察候选人对"事务 ID 何时产生"这一常被忽略细节的掌握（红旗：以为 BEGIN 即分配事务 ID）。
- P5 知道 InnoDB/NDB 才支持事务；P6 能说清只读事务可改临时表、纯查询不分配 ID；P7 能指出 trx_id 是 MVCC 可见性判断的依据。
- 红旗：以为 START TRANSACTION 立刻分配事务 ID；以为只读事务完全不能写。
- 惊艳点：只读事务只能改临时表、且只有首次改临时表才分配 ID——说明 ID 与"是否产生写"强绑定。

## 主问答
**Q（面试官原话）：** 什么时候才会给一个事务分配事务 ID？
**A：**
1. **结论**：只有在对**事务表（InnoDB 表）的记录做了增删改**时才分配唯一事务 ID；只读事务、纯查询事务都不分配（或分配只读占位 ID）。
2. **机制**：`START TRANSACTION READ ONLY` 开只读事务，不能改普通表但可对临时表增删改，且只有首次改临时表才分配 ID；`START TRANSACTION READ WRITE`（默认）开读写事务，同样只有首次 DML 才分配 trx_id `[源码]`。
3. **边界**：非事务引擎（如 MyISAM）的修改无法回滚，因为它根本不产生事务 ID；判断一条 SQL 是否用到事务表可看 `EXPLAIN` 的 `Extra: Using temporary`（内部临时表不分配 ID）`[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 谁支持事务 | 基础 | InnoDB/NDB | 判 P5 |
| L2 | 只读能写吗 | 细节 | 可改临时表 | 判 P5+ |
| L3 | 何时分配 ID | 机制 | 改事务表才分配 | 判 P6 |
| L4 | ID 干啥用 | 进阶 | MVCC 可见性 | 判 P6+ |
| L5 | 非事务引擎 | 边界 | MyISAM 不可回滚 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 5.6 ~ 8.0 | 无 | 仅 InnoDB/NDB 支持事务、trx_id 写时才分配，长期成立 `[源码]` |

## 关键代码
```sql
-- 只读事务：可改临时表，不可改普通表；首次改临时表才分配事务 ID
START TRANSACTION READ ONLY;
CREATE TEMPORARY TABLE t1(id INT);   -- 允许
INSERT INTO t1 VALUES(1);            -- 允许，首次改临时表才分配 ID
-- INSERT INTO users VALUES(1);      -- 报错：只读事务不能改普通表
COMMIT;
```

## 总结与追问预判
- 事务 ID 与"是否写事务表"强绑定，是 MVCC 可见性的基础。
- 预判：ACID 四特性 → 见 124-acid-properties；隔离级别 → 见 1230-isolation-levels。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 InnoDB 事务支持、只读/读写访问模式与事务 ID 分配时机；仅做了 ASR 解码将多组术语崩坏词（如"英乐DB"→InnoDB、"事物"→事务、"安卓logo"→undo log、"starttransactionreadonly"→START TRANSACTION READ ONLY 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
