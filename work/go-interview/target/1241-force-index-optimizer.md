# 1241 优化器选全表扫时：FORCE INDEX 干预

> 分类：MySQL 调优 / 锁 | 难度：L3 | 题型：排错题 | 频率：中 | 关键词：**FORCE INDEX** / **优化器选错** / **type=ALL** / **type=range** / **统计信息**
> 原文锚点：第 40~46 段「WHERE带索引但优化器走全表扫…用 FORCE INDEX 强制…确保走索引范围扫描防全表加锁」

## 一句话总述
即使 `WHERE` 带了索引列，优化器也可能因统计信息不准或数据分布评估而选**全表扫描（type=ALL）**——后果与"无索引"相同：全表行锁。可用 `FORCE INDEX` 提示强制走索引，并以 `EXPLAIN` 确认 `type=range`（索引范围扫描）而非 `ALL`。

## 面试官视角
- 意图：是否知道"有索引 ≠ 一定走索引"，以及优化器选错时如何干预。
- P5 知 FORCE INDEX 语法；P6 说清有索引仍全扫的原因与后果；P7 知用 EXPLAIN 验证 type、先确认测试环境走范围扫描。
- 红旗：以为 WHERE 有索引就绝对安全；不开 EXPLAIN 就上生产。
- 惊艳点：safe-updates 只拦"结构上看无索引"，**拦不住"有索引但优化器选全扫"**——后者必须靠 EXPLAIN + FORCE INDEX `[经验]`。

## 主问答
**Q（面试官原话）：** WHERE 明明有索引，为什么还是全表扫？怎么强制走索引？
**A：**
1. **优化器可能选错**：索引列存在，但优化器评估全表扫成本更低（统计信息过期/数据倾斜/回表代价大）→ `type=ALL` `[源码]`。
2. **后果同无索引**：全表扫描 → 所有记录加 next-key 锁，阻塞增删改。
3. **FORCE INDEX 强制**：用 `FORCE INDEX(idx)` 提示优化器使用指定索引，避免错选全扫。
4. **验证**：`EXPLAIN` 看 `type` 应为 `range`（索引范围扫描）而非 `ALL`；上生产前在测试机确认锁范围 `[边界]` 见 1244-range-index-all。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 有索引还全扫？ | 概念 | 优化器选错 | 换题 |
| L2 | 怎么强制 | 语法 | FORCE INDEX | 判 P5 |
| L3 | 验证方式 | 工具 | EXPLAIN type | 判 P6 |
| L4 | 为何错选 | 原理 | 统计/成本 | 判 P6+ |
| L5 | 与生产关系 | 实战 | 先测后上 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 全版本 | FORCE INDEX 长期支持 | 现代也可用 optimizer hint（8.0 的 /*+ INDEX() */）替代 |

## 关键代码
```sql
-- ❌ 有索引但优化器选全扫（type=ALL）→ 全表行锁
EXPLAIN UPDATE t SET name='x' WHERE age = 2;  -- 可能 type=ALL

-- ✅ 强制走索引，确保范围扫描（type=range）
EXPLAIN UPDATE t FORCE INDEX(idx_age) SET name='x' WHERE age = 2;
-- 或 8.0 写法：UPDATE t /*+ INDEX(t idx_age) */ SET name='x' WHERE age = 2;

-- 判定：type=range 表示只扫必要索引区间；type=ALL 表示仍全表扫，需继续优化
```

## 总结与追问预判
- 有索引≠走索引；优化器选全扫同样锁全行；FORCE INDEX + EXPLAIN 验证。
- 预判：无索引 UPDATE 后果 → 见 1241-update-no-index-lock；safe-updates 护栏 → 见 1241-sql-safe-updates；EXPLAIN type 退化链 → 见 1244-range-index-all。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语 `[经验]`。事实核校：有索引仍可能全表扫、FORCE INDEX 强制走索引、EXPLAIN 看 type 验证——均正确，未做更正。
