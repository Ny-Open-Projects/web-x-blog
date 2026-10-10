# 1245 EXPLAIN 详解（三）全貌（深挖）

> 分类：MySQL 调优 | 难度：中高 | 题型：原理深挖 | 频率：高 | 关键词：**key_len、ref、rows、filtered、Extra、覆盖索引、ICP**

> 原文锚点：第 1~86 段「key_len 计算、ref、rows、filtered、Extra 常用与进阶标记」

## 思路与架构
EXPLAIN 后半段列可分为「量化」与「补充」两类：
- 量化：key_len（索引最大长度，可反推联合索引用到几列）、ref（等值匹配对象）、rows（预估扫描行）、filtered（过滤后占比）。
- 补充：Extra —— 覆盖/下推/后过滤（Using index / Using index condition / Using where）、资源兜底（Using join buffer / Using filesort / Using temporary）、半连接策略（FirstMatch / LooseScan / Materialize / DuplicateWeedout）。
key_len 的计算式是关键技能：列字节数 +（变长 +2）+（可空 +1），按定义最大长度算。

## 方案取舍
- 用 key_len 反推索引利用率：比只看 key 更精确，能判断联合索引到底命中前几列。
- rows 与 filtered 联合看：单看 rows 会高估，rows × filtered 才接近真实参与行数；join 中还可用驱动表 rows×filtered 估算被驱动表访问次数。
- 见到 Using filesort / Using temporary：优先给排序/分组字段建合适索引，而不是调大 sort_buffer / tmp_table_size。
- 见到 Using where 且 rows 很大：说明条件没走索引，考虑改写条件或补索引。
- ICP（Using index condition）是好事：5.6+ 默认开启，能显著减少回表。

## 答题技巧
1. 开口定位：key_len/ref/rows/filtered 是量化列，Extra 是补充信息列。
2. 会算 key_len：`varchar(30)` + utf8mb4 + 可空 = 30×4+2+1 = 123；`varchar(255)` = 1023；合计 1146。
3. 讲 ref/rows：ref 是等值匹配对象（多见 const），rows 是预估扫描行（越小越好）。
4. 讲 filtered：过滤后占比，越大越好；rows×filtered 估 join 次数；它不是核心指标，核心是 type/key/rows。
5. 收尾 Extra：覆盖(Using index) ≠ 下推(Using index condition)；filesort/temporary 是加索引红灯；实战话术「先看 type/key/rows，再用 key_len 判命中列数，最后看 Extra 找优化点」。

## 细节与核心 API

**key_len 反推联合索引用到几列**（列字节数 + 变长+2 + 可空+1，按定义最大长度算）：

```sql
-- varchar(30)+utf8mb4+可空 = 30*4 + 2 + 1 = 123；varchar(255)+utf8mb4+可空 = 1023
EXPLAIN SELECT * FROM t WHERE a='x' AND b='y';
-- key_len=123   → 仅命中 a；key_len=1146 → 命中 a+b（123+1023）
```

**rows × filtered 才接近真实参与行数**；join 中驱动表 `rows×filtered` 估被驱动表访问次数。

**Extra 标记**：

```text
Using index           → 覆盖索引（免回表，好事）
Using index condition  → ICP 下推（5.6+ 默认开，减回表）
Using where           → 条件没走索引（rows 大时考虑补索引）
Using filesort / Using temporary → 排序/分组没索引（加索引优于调大 sort_buffer_size）
Using join buffer     → 未用索引的 join（BNL 兜底）
```

> 边界：EXPLAIN 列与拓扑见 1243；type 谱系见 1244；本卡只讲 key_len/ref/rows/filtered/Extra。
