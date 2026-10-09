# 1250 SQL 自定义排序与 NULL 置后

> 分类：SQL 技巧 | 难度：L2 | 题型：实操题 | 频率：中 | 关键词：**ORDER BY FIELD**/**自定义顺序**/**NULL 排最后**/**IS NULL 条件排序**
> 原文锚点：第 7~20 段「自定义排序（FIELD）+ NULL 排最后」

## 一句话总述
MySQL 里想按「指定 ID 列表的顺序」返回，用 `ORDER BY FIELD(id, 7,3,1,...)`；想让 NULL 排到最后，用 `ORDER BY (col IS NULL)` 利用条件返回 0/1 升序置于前。

## 面试官视角
- 考察意图：是否掌握 ORDER BY 的高级用法，而非只会 `ORDER BY col ASC/DESC`。
- 分档：P5 能写出 FIELD 自定义排序；P6 能解释 NULL 置后为什么用 `(col IS NULL)`；P7 知 FIELD 非命中值返回 0 排最前、大列表下 FIELD 无法走索引。
- 红旗答案：用 `IN (...)` 期望保序（默认按 id 升序）；用 `col IS NOT NULL` 排序方向搞反导致 NULL 在前。
- 惊艳点：点出 FIELD 是「内存排序、不走索引」，列表很长时性能差；NULL 置后还能写 `ORDER BY col IS NULL, col ASC` [经验]。

## 主问答
**Q（面试官原话）：** 怎么按指定 ID 顺序返回？怎么让 NULL 排最后？
**A：**
1. **自定义顺序（保持指定 ID 列表次序）**：搜索拿到 ID 列表（如 `7,3,1,4,5,8,12`）后回表查数据，默认按主键升序返回、打乱原序。用 **`ORDER BY FIELD(id, 7,3,1,4,5,8,12)`** 让 MySQL 按你给的顺序排；未在列表中出现的行 FIELD 返回 0，会排在最前，需注意 [经验]。
2. **NULL 排到最后**：某列（如 k3）为 NULL 时想让它沉底，用 **`ORDER BY (col IS NULL)`**——非 NULL 行条件返回 0、NULL 行返回 1，升序下 0 在前 1 在后，于是 NULL 自动落到最后；等价写法 `ORDER BY col IS NULL, col ASC` [经验]。
3. **FIELD 的代价与替代**：FIELD 是**内存排序、不走索引**，ID 列表很长时性能差；若保序列表巨大，更稳妥是拉回应用层按 map 重排，而非在 SQL 里排 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 怎么保 ID 列表顺序？ | 排序语法 | ORDER BY FIELD(id, ...) | P5 |
| L2 | FIELD 未命中值排哪？ | 边界语义 | 返回 0，排最前 | P6 |
| L3 | NULL 为何用 IS NULL？ | 条件排序 | 返回 0/1，升序把 NULL(1)沉底 | P6 |
| L4 | FIELD 能走索引吗？ | 性能意识 | 不能，内存排序，大列表慢 | P7 |
| L5 | 还有哪些 NULL 处理？ | 知识广度 | COALESCE/IFNULL 填默认值再排 | P7+ |

## 版本与兼容性
- `FIELD()` 为 MySQL 独有函数；其他库用 `CASE`/`array_position`（PostgreSQL `idx()`）替代。NULL 排序方向各库默认不同（PostgreSQL 默认 NULL 最大）。

## 关键代码

```sql
-- 按指定 ID 列表顺序返回（搜索召回后保序回表）
SELECT * FROM t
ORDER BY FIELD(id, 7, 3, 1, 4, 5, 8, 12);

-- 让 NULL 排到最后（col IS NULL：非 NULL=0 在前，NULL=1 在后）
SELECT * FROM t
ORDER BY (col IS NULL), col ASC;   -- 等价写法，可读性更好
```

## 总结与追问预判
自定义排序与 NULL 处理是「写出贴合业务的 SQL」的硬技巧。更通用的聚合/分组技巧见同波 1250 的 GROUP BY+ROLLUP 与 CASE WHEN 分级。

## ⚠️ 原文纠错
1. 事实核校： [经验] FIELD 列表中的值应与列**同类型**，混类型会触发隐式转换、可能不走索引甚至排序异常——正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（自定义排序、NULL 值、升序、主键等）。
