# 1241 sql_safe_updates：UPDATE/DELETE 生产护栏

> 分类：MySQL 锁 | 难度：L3 | 题型：配置题 | 频率：中 | 关键词：**sql_safe_updates** / **UPDATE 放行规则** / **DELETE 更严** / **防全表锁** / **LIMIT**
> 原文锚点：第 26~44 段「sql_safe_updates=1…UPDATE 满足 WHERE带索引 或 WHERE+LIMIT…DELETE 需索引 或 非恒定WHERE+LIMIT 且不可为恒定条件」

## 一句话总述
线上开启 `sql_safe_updates=1`，MySQL 会拦截"可能全表扫描"的写操作：`UPDATE` 只需 `WHERE` 带索引 **或** 带 `LIMIT` 即可放行；`DELETE` 更严——需 `WHERE` 带索引列，或"非恒定 `WHERE` + `LIMIT`"，且 `WHERE` 不可为恒定条件（如 `WHERE 1=1`）。

## 面试官视角
- 意图：是否知道有生产护栏能从配置层挡住"无索引 UPDATE/DELETE 锁全表"。
- P5 知有 safe-updates 开关；P6 说清 UPDATE/DELETE 各自放行条件；P7 知 DELETE 比 UPDATE 严、恒定条件被禁、仍需自测执行计划。
- 红旗：以为开了 safe-updates 就绝对安全；忽略"有索引但优化器仍选全表扫"的情况。
- 惊艳点：UPDATE 带 `LIMIT` 即可放行（即使无索引），而 DELETE 带 `LIMIT` 时 `WHERE` 还不能是恒定条件——二者宽松度不同 `[经验]`。

## 主问答
**Q（面试官原话）：** 怎么从配置上防止 UPDATE/DELETE 无索引锁全表？
**A：**
1. **开启护栏**：`SET sql_safe_updates=1`（会话或写进配置文件），默认关闭 `[源码]`。
2. **UPDATE 放行条件**：`WHERE` 带索引列，**或** 同时带 `WHERE` 与 `LIMIT`（此时 `WHERE` 可无索引、可为恒定条件）。
3. **DELETE 更严**：须 `WHERE` 带索引列，**或** "非恒定 `WHERE` + `LIMIT`"；`WHERE` 不能为恒定条件（如 `1=1`）。
4. **判定依据**：解析器按语句结构判断，不实际执行；目的是阻断全表扫描式写。
5. **仍要自测**：即使 `WHERE` 有索引，优化器也可能选全表扫——护栏不保证一定走索引，须 `EXPLAIN` 确认 `[边界]` 见 1238-type-conversion-lock。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 有护栏吗 | 概念 | sql_safe_updates | 换题 |
| L2 | UPDATE 条件 | 规则 | 索引或LIMIT | 判 P5 |
| L3 | DELETE 区别 | 差异 | 更严/禁恒定 | 判 P6 |
| L4 | 恒定条件 | 边界 | DELETE 禁之 | 判 P6+ |
| L5 | 开了就安全？ | 实战 | 仍须EXPLAIN | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 5.6+ | 语义稳定 | 写配置文件持久化，生产建议开启 |

## 关键代码
```sql
-- 开启护栏（会话级）
SET sql_safe_updates = 1;

-- ✅ UPDATE 带 LIMIT 即放行（即使 age 无索引）
UPDATE t SET name='x' WHERE age = 2 LIMIT 100;

-- ❌ 纯无索引 UPDATE 被拦截
-- UPDATE t SET name='x' WHERE age = 2;  -- ERROR: safe-updates 拒绝

-- ✅ DELETE 带索引列放行
DELETE FROM t WHERE id = 10;

-- ❌ DELETE 恒定条件即使带 LIMIT 也被拒
-- DELETE FROM t WHERE 1=1 LIMIT 100;  -- ERROR
```

## 总结与追问预判
- safe-updates：UPDATE 宽松（索引或 LIMIT），DELETE 严（索引 或 非恒定 WHERE+LIMIT、禁恒定）。
- 预判：无索引 UPDATE 后果 → 见 1241-update-no-index-lock；优化器选全表扫 → 见 1241-force-index-optimizer；类型转换事故 → 见 1238-type-conversion-lock。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语 `[经验]`。事实核校：sql_safe_updates=1 的 UPDATE/DELETE 放行规则、DELETE 比 UPDATE 严、恒定条件被禁——均正确，未做更正。
