# 1226 COUNT 性能排序与 MyISAM 的差异

> 分类：数据库 / MySQL | 难度：L3 | 题型：对比题 | 频率：高 | 关键词：**性能排序** / **MyISAM O(1)** / **InnoDB MVCC** / **近似总数**
> 原文锚点：第 41~64 段「排序：COUNT(*)=COUNT(1) > COUNT(索引字段) > COUNT(主键) > COUNT(非索引字段)；MyISAM 无 WHERE 走 O(1) 变量；InnoDB 因 MVCC 不行；近似值用 information_schema/SHOW TABLE STATUS」

## 一句话总述
不带 WHERE 时 `COUNT` 的**性能排序**为：`COUNT(*) ≈ COUNT(1) > COUNT(索引字段) > COUNT(主键) > COUNT(非索引字段)`。根因是索引选择（二级索引最小优先）与是否要读字段值判 NULL。另一个高频点：**MyISAM 无 WHERE 的 `COUNT(*)` 走 O(1)**（维护好的行数变量），而 **InnoDB 因 MVCC 每个事务可见行不同、做不到**，只能扫索引。

## 面试官视角
- 意图：考察能否把"语义差异 + 索引选择"综合成**一句性能排序**，并解释 MyISAM/InnoDB 的根本差异。
- P6 能背出完整排序；P7 能解释"为什么 COUNT(主键) 比 COUNT(索引字段) 慢"（主键走聚簇索引全字段、索引字段走二级索引但多一步判 NULL，综合下主键反而更慢）。
- 红旗：把排序记反（如以为 COUNT(*) 最慢）；不知道 MyISAM 的 O(1) 优势及 InnoDB 为何不行。
- 惊艳点：点出"InnoDB 要准确总数，可在应用层维护计数表/缓存"，把知识落到工程实践（也见 1246 的缓存思路）。

## 主问答
**Q（面试官原话）：** 这几种 COUNT 谁快谁慢？MyISAM 和 InnoDB 在 COUNT(*) 上有区别吗？
**A：**
1. **结论**：不带 WHERE 的性能排序——`COUNT(*) ≈ COUNT(1) > COUNT(索引字段) > COUNT(主键) > COUNT(非索引字段)`。
2. **机制（排序根因）**：
   - `COUNT(*)`/`COUNT(1)`：**不读字段值、不判 NULL**，优先最小二级索引，最快。
   - `COUNT(索引字段)`：走二级索引但**要读字段值、判 NULL**，略慢于前两者。
   - `COUNT(主键)`：走**聚簇索引（全字段）**，比二级索引 IO 大，慢于索引字段。
   - `COUNT(非索引字段)`：无索引可走，只能**全表扫描**，最慢。
3. **机制（MyISAM vs InnoDB）**：MyISAM 无 WHERE 的 `COUNT(*)` 直接读**维护好的行数变量，O(1)**（无事务、行数确定）；InnoDB 支持事务 + **MVCC**，同一时刻不同事务可见行数不同，**无法维护单一行数变量**，只能扫索引。因此 InnoDB 要准确总数要么扫索引，要么**应用层维护计数表/缓存**。
4. **边界（近似值）**：InnoDB 不需精确总数时，可用 `SHOW TABLE STATUS` 或 `information_schema.tables.TABLE_ROWS` 取**近似值**（不遍历索引树）`[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 谁最快 | 排序 | COUNT(*)/COUNT(1) | 判 P5 |
| L2 | 谁最慢 | 排序 | COUNT(非索引字段) 全表扫 | 判 P6 |
| L3 | 主键为何比索引字段慢 | 机制 | 聚簇全字段 IO 大 | 判 P6 |
| L4 | MyISAM 为何 O(1) | 深度 | 无事务行数确定 | 判 P7 |
| L5 | InnoDB 准确总数怎么办 | 工程 | 计数表/缓存/近似值 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 5.x / 8.0 | 无 | 性能排序恒定；MyISAM O(1)、InnoDB 因 MVCC 需扫索引恒定 `[经验]` |
| 8.0 | 系统表迁 InnoDB | `information_schema.tables` 在 8.0 近似统计仍可用，取近似值 |

## 关键代码
```sql
-- 1) 性能排序（不带 WHERE）：COUNT(*) ≈ COUNT(1) 最快，COUNT(非索引字段) 最慢
SELECT COUNT(*) FROM t;        -- 走最小二级索引，不读列值、不判 NULL
SELECT COUNT(age) FROM t;      -- 走二级索引，但读 age 值判 NULL，略慢
SELECT COUNT(id) FROM t;       -- 走聚簇索引（全字段），比二级索引 IO 大
SELECT COUNT(name) FROM t;     -- name 无索引 → 全表扫描，最慢

-- 2) MyISAM 无 WHERE 的 COUNT(*) 走 O(1) 维护变量
SELECT COUNT(*) FROM myisam_t; -- 直接读行数变量

-- 3) InnoDB 近似值（不遍历索引树）：SHOW TABLE STATUS / information_schema
SHOW TABLE STATUS LIKE 'user';                       -- Rows 列为近似值
SELECT TABLE_ROWS FROM information_schema.tables
WHERE table_schema = DATABASE() AND table_name='user'; -- 近似值
```

## 总结与追问预判
- 排序：`COUNT(*)≈COUNT(1) > COUNT(索引字段) > COUNT(主键) > COUNT(非索引字段)`；MyISAM O(1)、InnoDB 因 MVCC 需扫索引。
- 预判：语义本质 → 见 1226；索引选择机制 → 见 1226；Go 层计数 → 见 1246；MyISAM 布局 → 见 1217。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"性能排序（COUNT(*)=COUNT(1) > COUNT(索引字段) > COUNT(主键) > COUNT(非索引字段)）、MyISAM 无 WHERE 走 O(1) 行数变量、InnoDB 因 MVCC 无法维护单一行数变量、近似值用 SHOW TABLE STATUS/information_schema"的描述，与 MySQL 行为一致（MyISAM 确实维护行数变量供无 WHERE 的 COUNT(*) O(1) 返回；InnoDB 因 MVCC 不维护）。仅做了 ASR 解码将多组术语崩坏词（浪值→NULL、组件→主键、二级索引→二级索引、技术索引→聚簇索引、mysam→MyISAM、inlDB→InnoDB、roctt→row count、rose→rows 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
