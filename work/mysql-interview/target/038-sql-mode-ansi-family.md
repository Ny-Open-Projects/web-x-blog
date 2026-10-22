# 038 REAL_AS_FLOAT 与 PIPES_AS_CONCAT

> 分类：服务器配置 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**REAL_AS_FLOAT** / **PIPES_AS_CONCAT** / **双竖线**
> 原文锚点：第 94~126 段「使用了 REAL_AS_FLOAT 之后，REAL 就作为 FLOAT 类型的同义词…PIPES_AS_CONCAT 将双竖线视为字符串的连接符」

## 一句话总述
两个让 MySQL 更贴近标准 SQL 的 sql_mode 值：**`REAL_AS_FLOAT`**（REAL 是 FLOAT 而非 DOUBLE 的同义词）、**`PIPES_AS_CONCAT`**（`||` 是字符串连接而非逻辑或）。

## 面试官视角
- **考察意图**：这类值不常考，用来检验你是否真的翻过 sql_mode 取值表，还是只会背两三个。
- **P5** 知道 `||` 默认是"或"运算，字符串拼接用 `CONCAT()`。
- **P6** 能说出这两个值的作用与标准 SQL 的差异点。
- **P7** 能点出**不开 `PIPES_AS_CONCAT` 时的静默陷阱**：`'hello' || 'x'` 不报错，返回 0 并给一条警告。
- **红旗**：① 以为 `||` 在所有数据库都是字符串连接；② 以为 REAL 就是 FLOAT。
- **惊艳点**：默认下 `'hello' || 'mysql.com'` **不报错，返回 0**（字符串被转 double 做或运算）`[实测]` —— 验证：`SELECT 'hello' || 'mysql.com'; SHOW WARNINGS;` 结果为 0 并给出截断警告。

## 主问答
**Q（面试官原话）：** 我想用 `||` 拼字符串，在 MySQL 里怎么让它生效？REAL 类型默认是啥？

**A：**
1. **结论**：加 `PIPES_AS_CONCAT` 让 `||` 变成**字符串连接符**；加 `REAL_AS_FLOAT` 让 `REAL` 成为 **FLOAT** 的同义词（默认是 **DOUBLE**）。
2. **机制**：默认 `||` 是**逻辑或**，字符串会被隐式转数值参与运算，结果往往是无意义的 0；`CONCAT()` 才是默认可用的拼接方式。
3. **边界**：这两个值都属于"向标准 SQL 靠拢"的组合，可连同 `ANSI_QUOTES` 一起用 **`sql_mode=ANSI`** 一次性设置。

**加分层**：迁移 PostgreSQL / Oracle 时 `||` 是高频写法，不开这个模式就会**静默算错**——比报错更危险。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么拼字符串 | 概念 | `CONCAT()` | 换题 → 不及格 |
| L2 | `\|\|` 默认是什么 | 默认行为 | 逻辑或 | 判 P5 |
| L3 | 默认结果是什么 | 静默陷阱 | 返回 0 + 警告 | 判 P6 |
| L4 | REAL 默认对应什么 | 类型细节 | DOUBLE | 判 P6+ |
| L5 | 怎么一次性设置 | 组合值 | `sql_mode=ANSI` | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6 / 5.7 / 8.0 | 两个值语义未变，**默认都不开启** | 按"默认 `\|\|` 为或、REAL=DOUBLE"答 |

## 关键代码
```sql
SELECT 'hello' || 'mysql.com';   -- 默认：0（逻辑或），SHOW WARNINGS 有警告
SET SESSION sql_mode = 'PIPES_AS_CONCAT,REAL_AS_FLOAT';
SELECT 'hello' || 'mysql.com';   -- 开启后：hellomysql.com
CREATE TABLE t2 (id REAL);
SHOW CREATE TABLE t2;            -- 开启后显示 float
```

## ⚠️ 原文纠错
原文演示 `REAL` 默认建表结果为 **double**、开启后为 **float**——与官方一致，未发现技术错误。补充一点：原文未强调默认 `||` 场景会**产生警告但仍有结果输出**，这属于静默错误风险，卡面已单列。

## 总结与追问预判
- `PIPES_AS_CONCAT`：`||` 变拼接；不开则**静默返回 0**。
- `REAL_AS_FLOAT`：REAL 由 DOUBLE 变 FLOAT；`sql_mode=ANSI` 可一次启用这类组合。
- 下一题：见 037（ANSI_QUOTES）、039（严格/宽松模式）。
