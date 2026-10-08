# 1226 COUNT 的语义本质：统计"参数值不为 NULL"的行

> 分类：数据库 / MySQL | 难度：L3 | 题型：语义题 | 频率：高 | 关键词：**COUNT(*) / COUNT(1) / COUNT(字段)** / **NULL 不计入** / **统计非 NULL**
> 原文锚点：第 2~6 段「count 统计符合条件结果集数量；统计的是函数参数值不为 NULL 的记录数；主键/1 表示全部记录；非主键字段遇 NULL 不累计」

## 一句话总述
`COUNT` 统计的是**「参数值不为 NULL」**的行数——这是理解三者差异的钥匙。`COUNT(*)`、`COUNT(1)`、主键列的 `COUNT(主键)` 都统计**全部行**（因为 * / 1 / 主键永不为 NULL）；只有 `COUNT(非主键字段)` 会**跳过该字段为 NULL 的行**。网上"COUNT(*) 最慢"是典型误区。

## 面试官视角
- 意图：考察对 `COUNT` 语义的**精确理解**——绝大多数人只背"性能排序"，却说不清"为什么"`。
- P5 能说清 `COUNT(字段)` 排除 NULL；P6 能讲清 `COUNT(*)`/`COUNT(1)`/`COUNT(主键)` 语义等价（都计全部行）；P7 能点出"* 不是读全部字段、而是 ANSI 规定的计行语法糖"。
- 红旗：以为 `COUNT(*)` 会读所有列（实际不读列值）；把 `COUNT(1)` 和 `COUNT(0)` 混为一谈（0 也非 NULL，同样计全部行）。
- 惊艳点：点出"COUNT 的参数是任何非 NULL 常量都计全部行（COUNT(4)、COUNT(3) 等价 COUNT(1)）"，并说明 `COUNT(*)` 与 `COUNT(1)` 在 MySQL 内部被优化成同一执行路径。

## 主问答
**Q（面试官原话）：** `COUNT(*)`、`COUNT(1)`、`COUNT(字段名)` 到底有什么区别？
**A：**
1. **结论**：三者差异**只在语义、不在"快慢"的直觉**——`COUNT` 统计的是**参数值不为 NULL 的记录数**。
2. **机制**：
   - `COUNT(*)`：ANSI SQL 规定的"计行"语法，`*` 不表示读全部字段，而是**统计所有行**（含任意列 NULL 的行也计入）。
   - `COUNT(1)`：参数为常量 `1`（非 NULL），**逐行给 1、统计全部行**，语义与 `COUNT(*)` 等价。MySQL 内部把 `COUNT(*)` 优化成与 `COUNT(1)` 相同路径。
   - `COUNT(主键)`：主键非空，**统计全部行**，语义与前两者等价。
   - `COUNT(非主键字段)`：若该字段为 **NULL**，这一行**不计入**——这是唯一与前三者不同的地方。
3. **边界**：`COUNT(任意非 NULL 常量)` 都等价于 `COUNT(1)`（如 `COUNT(4)`、`COUNT(3)` 都计全部行）；但 `NULL` 不是 0、也不是空串，它是"未知"，所以 `COUNT(NULL)` 恒为 0 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | COUNT 计什么 | 语义 | 参数值非 NULL 的行 | 判 P5 |
| L2 | COUNT(*) 读列吗 | 误区 | 不读列，只计行 | 判 P6 |
| L3 | 字段 NULL 怎么办 | 差异 | 不计入 | 判 P6 |
| L4 | COUNT(1) vs COUNT(*) | 等价 | 内部同路径 | 判 P7 |
| L5 | COUNT(0) 计吗 | 边界 | 0 非 NULL，计全部行 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 5.x / 8.0 | 无 | `COUNT(*)` 与 `COUNT(1)` 被优化等价；`COUNT(字段)` 排除 NULL 恒定 `[经验]` |
| SQL 标准 | 无 | `COUNT(*)` 计行、`COUNT(expr)` 计 expr 非 NULL 为 SQL 标准语义 |

## 关键代码
```sql
-- COUNT 统计的是"参数值不为 NULL"的行数
SELECT COUNT(*)    FROM t;     -- 统计全部行（含任意列 NULL 的行也计入）
SELECT COUNT(1)    FROM t;     -- 等价 COUNT(*)，统计全部行
SELECT COUNT(id)   FROM t;     -- id 是主键非空，统计全部行
SELECT COUNT(name) FROM t;     -- name 为 NULL 的行【不计入】！
SELECT COUNT(4)    FROM t;     -- 任意非 NULL 常量都计全部行，等价 COUNT(1)
SELECT COUNT(NULL) FROM t;     -- 恒为 0（NULL 不是 0、不是空串，是"未知"）
```

## 总结与追问预判
- `COUNT` 计"参数非 NULL 行"；`COUNT(*)`/`COUNT(1)`/`COUNT(主键)` 语义等价都计全部行；`COUNT(字段)` 排除 NULL。
- 预判：执行时怎么选索引 → 见 1226-count-index-choice；性能排序与 MyISAM 对比 → 见 1226-count-performance-rank；Go 层统计总条数 → 见 1246-go-count-total（侧重 Scan 传地址，不冲突）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"count 统计参数值非 NULL 记录数、COUNT(*)/COUNT(1)/COUNT(主键) 语义等价计全部行、COUNT(非主键字段) 遇 NULL 不计入、COUNT(任意非 NULL 常量) 等价 COUNT(1)"的描述，与 MySQL/SQL 标准语义一致。仅做了 ASR 解码将多组术语崩坏词（浪值→NULL、康特→COUNT、snaack→SELECT、组件→主键、二级索引→二级索引、技术索引→聚簇索引、warwarming→warning、roctt→row count 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
