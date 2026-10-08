# 1241 UPDATE 安全加锁深挖

> 分类：MySQL 锁 | 难度：L3 | 题型：深挖 | 频率：中 | 关键词：**安全加锁** / **EXPLAIN 验证** / **护栏** / **RR next-key**
> 原文锚点：第 1~46 段「无索引UPDATE锁全行…sql_safe_updates…FORCE INDEX…RR下next-key锁链」

## 思路与架构
UPDATE 安全加锁 = "先确认走索引范围扫描" + "开护栏兜底" + "必要时强制索引" 三道防线：
- **事前**：写语句的 `WHERE` 必带索引列；上生产前在测试机 `EXPLAIN` 确认 `type=range`。
- **事中**：开启 `sql_safe_updates=1` 挡住结构上看无索引的写。
- **兜底**：优化器仍选全扫时，用 `FORCE INDEX` 强制，再验 `type`。

## 方案取舍
```text
无索引 UPDATE 的锁范围（RR 下）：
──────────────────────────────────────────────
无索引/索引失效/优化器选全扫  →  全表扫描  →  所有记录加 next-key X 锁
                                      ├─ 含 Supremum 伪记录
                                      └─ 阻塞其他事务增删改（非表锁）
有索引且走 range             →  只锁扫过的索引区间（小范围）

护栏 vs 强制：
sql_safe_updates  → 拦"结构无索引"的写（UPDATE 宽松/DELETE 严）
FORCE INDEX       → 拦"有索引但优化器选全扫"（safe-updates 拦不住这类）
```

## 答题技巧
```text
面试话术（先答 FAQ，再给防护）：
1. 直接答：不会加表锁，但无索引→全表扫描→全表行被 next-key X 锁，阻塞增删改
2. 区分：全表行锁 ≠ 表锁（锁视图不同，见 1233-table-lock）
3. 防护一：WHERE 带索引 + 测试机 EXPLAIN 确认 type=range
4. 防护二：开 sql_safe_updates（UPDATE 需索引/LIMIT，DELETE 更严）
5. 防护三：优化器仍选全扫 → FORCE INDEX 强制，再验 type
6. 收尾：RC 下退化为记录锁不锁间隙，但全表扫仍锁全部记录行
```

> 边界：SELECT 侧同类事故（类型转换）见 1238-type-conversion-lock；UPDATE 底层加锁机制见 1236-update-locking；表锁本身见 1233-table-lock；EXPLAIN type 退化链见 1244-range-index-all；本卡只深挖"UPDATE 安全加锁三道防线"不重述各机制。
