# 206. 外连接 LEFT/RIGHT JOIN 与全连接模拟

> 分类：数据库 | 难度：L2 | 题型：概念+手写 | 频率：高 | 关键词：**LEFT JOIN** / **RIGHT JOIN** / **NULL 填充** / **全连接模拟** / **FULL OUTER JOIN**
> 原文锚点：第8章 8-3「外连接含左连接与右连接：左连接返回左表所有记录（右表无匹配填 NULL），右连接反之；全连接=某表有匹配即返回（MySQL 不支持原生 FULL OUTER JOIN）」

## 一句话总述
**LEFT JOIN 返回左表全部记录、右表无匹配则填 NULL；RIGHT JOIN 反之**；"全连接"在 MySQL 没有原生 `FULL OUTER JOIN`，需用 `LEFT JOIN ... UNION RIGHT JOIN` 模拟。

## 面试官视角
- **考察意图**：是否分清左/右外连接的"保哪一侧全部"，并知道 MySQL 的全连接模拟套路。
- **P5** 能写出 LEFT/RIGHT JOIN 并说清"保左/保右全部、另一侧无匹配填 NULL" / **P6** 能手算示例（左连接下 a 的 ID=2 在 b 中无匹配→BID/BVAL 为 NULL） / **P7** 能说出"MySQL 不支持 FULL OUTER JOIN，用 LEFT JOIN UNION RIGHT JOIN 模拟全连接"。
- **红旗**：认为 RIGHT JOIN 比 LEFT JOIN 更强（其实只是左右互换，左连接写 `b LEFT JOIN a` 即可替代右连接）；以为 MySQL 有 `FULL JOIN` 关键字。
- **惊艳点**：能点出"实际项目几乎只用 LEFT JOIN，右连接可读性差、常被改写为左连接"的工程偏好 `[经验]`。

## 主问答
**Q（面试官原话）：** 什么是左连接和右连接？全连接怎么写？

**A · 标准答案骨架：**
1. **左连接 LEFT JOIN**：返回**左表所有记录**，即使右表中没有匹配行；右表无匹配时对应列填 **NULL**。语法只需把 INNER JOIN 改成 `LEFT JOIN`。
2. **右连接 RIGHT JOIN**：与左连接相反，返回**右表所有记录**，左表无匹配填 NULL。它只是左右互换，**任何 RIGHT JOIN 都能改写成 LEFT JOIN**（交换两表位置），所以实际项目几乎只写 LEFT JOIN。
3. **全连接（FULL OUTER JOIN）**：语义是"只要某一侧表存在匹配就返回"（左右两侧都不匹配的行也保留、另一侧填 NULL）。**关键事实：MySQL 不支持原生的 `FULL OUTER JOIN`**，必须用 `LEFT JOIN ... UNION RIGHT JOIN`（去重合并）来模拟。

**加分层**：左连接手算示例——a(ID,val)={(1,'AB'),(2,'AC')}、b={(1,'AD'),(3,'BC')}：`a LEFT JOIN b ON a.id=b.id` 结果为两行：`(AID=1,BID=1,aval='AB',bval='AD')` 与 `(AID=2,BID=NULL,aval='AC',bval=NULL)`（a 的 ID=2 在 b 中无匹配，填 NULL）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 左连接返回什么 | 基本认知 | 左表全部+右表无匹配填 NULL | 换题 → 不及格 |
| L2 | 右连接怎么改写 | 是否懂等价 | 左右表互换变 LEFT JOIN | 判 P5 |
| L3 | 左连接示例结果 | 手算能力 | a 的 ID=2 行 BID/BVAL 为 NULL | 判 P6 |
| L4 | MySQL 有 FULL JOIN 吗 | 版本事实 | 无，用 LEFT UNION RIGHT 模拟 | 判 P6+ |
| L5 | 为什么少用 RIGHT JOIN | 工程偏好 | 可读性差，全用 LEFT 改写 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| MySQL 各版本均不支持 `FULL OUTER JOIN` | PostgreSQL/Oracle 原生支持 FULL JOIN | 面试按"MySQL 用 UNION 模拟"答；跨库项目需确认目标库是否原生支持 |

## 关键代码
```sql
-- 左连接：左表 a 全部返回，b 无匹配填 NULL [实测, MySQL 8]
SELECT a.id AS AID, b.id AS BID, a.val AS aval, b.val AS bval
FROM a LEFT JOIN b ON a.id = b.id;
-- 结果两行：(1,1,'AB','AD') 与 (2,NULL,'AC',NULL)

-- MySQL 模拟全连接（FULL OUTER JOIN）
SELECT a.id, b.id, a.val, b.val FROM a LEFT JOIN b ON a.id=b.id
UNION
SELECT a.id, b.id, a.val, b.val FROM a RIGHT JOIN b ON a.id=b.id;
```

## ⚠️ 原文纠错
- 机翻还原：「elevejoin」→ **LEFT JOIN**；「rightjoin」→ **RIGHT JOIN**；「nuve」→ **NULL**；「全连接」→ **full join / FULL OUTER JOIN**。
- 原文对全连接只给出概念定义（"只要某表有匹配就返回"），**未演示且未说明 MySQL 不支持原生 FULL OUTER JOIN**——已补"用 LEFT JOIN UNION RIGHT JOIN 模拟"这一面试高频考点。
- 原文称左连接"把 innerjoin 改成 elevejoin 即可"，准确为 `INNER JOIN` → `LEFT JOIN`。

## 总结与追问预判
外连接的核心是"保哪一侧全部、另一侧填 NULL"，且**MySQL 无原生全连接、需 UNION 模拟**是高频易错点。面试官常追问"LEFT 和 RIGHT 能互相替代吗""FULL JOIN 在 MySQL 怎么写"。衔接：**SQL 编写原则（见 204 卡）**、**内连接（见 205 卡）**。
