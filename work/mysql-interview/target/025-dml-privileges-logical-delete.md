# 025 DML 类权限与逻辑删除

> 分类：用户管理 | 难度：L1 | 题型：八股题 | 频率：高 | 关键词：**SELECT/INSERT/UPDATE/DELETE** / **逻辑删除** / **最小权限**
> 原文锚点：第 70~77 段「一般用户包括程序使用的数据库账号只需要具有这些 DML 权限就可以了，甚至在一些公司的安全标准中一般用户连 delete 权限都没有」

## 一句话总述
应用账号的日常权限就是 **SELECT / INSERT / UPDATE / DELETE**；安全标准更严的公司**连 DELETE 都不给**，改用 UPDATE 做**逻辑删除**。

## 面试官视角
- **考察意图**：看你是否接触过真实的权限基线，而不只会写 `GRANT ALL`。
- **P5** 能说出四个 DML 权限。
- **P6** 能说清业务账号只要这四个，只读账号只给 `SELECT`。
- **P7** 能讲出逻辑删除的动机（可追溯、可恢复），并指出查询需全带过滤条件的代价。
- **红旗**：① 张口 `GRANT ALL ON *.*`；② 以为逻辑删除后查询不用加条件。
- **惊艳点**：撤销 DELETE 权限后，误删风险由**权限层**兜底 `[经验]` —— 验证：`REVOKE DELETE ON appdb.* FROM 'app'@'%';` 后执行 DELETE 直接报 1142。

## 主问答
**Q（面试官原话）：** 你们线上业务账号开什么权限？为什么有的公司连 DELETE 都不给？

**A：**
1. **结论**：业务账号通常只开 **SELECT、INSERT、UPDATE、DELETE**；更严的**只给前三个**，删除走逻辑删除。
2. **机制**：逻辑删除 = 用 `UPDATE` 把 `is_deleted` 之类标记位置位，**不物理删行**；查询统一带 `is_deleted = 0`。
3. **边界**：代价是**每张表查询都要带过滤条件**，漏写就查出"已删除"数据；唯一索引与归档策略也要重新设计。

**加分层**：不给 DELETE 是用**权限层**兜底误删，比靠代码 review 可靠；代价是所有删除场景都要改造成 UPDATE。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | DML 有哪些权限 | 概念 | SELECT/INSERT/UPDATE/DELETE | 换题 → 不及格 |
| L2 | 只读账号给什么 | 最小权限 | 只给 SELECT | 判 P5 |
| L3 | 逻辑删除怎么实现 | 工程方案 | UPDATE 置标记位 | 判 P6 |
| L4 | 逻辑删除副作用 | 权衡判断 | 查询过滤、唯一索引、归档 | 判 P6+ |
| L5 | 你们怎么定基线 | 实战 | 账号分级与审计机制 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6 / 5.7 / 8.0 | 权限名称与语义全版本一致 | 按"四个 DML + 逻辑删除"答，无版本翻转 |

## 关键代码
```sql
GRANT SELECT, INSERT, UPDATE ON appdb.* TO 'app'@'192.168.1.%';
UPDATE appdb.orders SET is_deleted = 1, deleted_at = NOW() WHERE id = 10086;
SELECT * FROM appdb.orders WHERE is_deleted = 0 AND user_id = 7;
```

## ⚠️ 原文纠错
原文把 DML 解释为"数据控制语句"——**标准说法是数据操纵语言（Data Manipulation Language）**，DCL 才是数据控制语言，已按标准术语修正。机翻音译（sinserinsert、阿 PG、XQ）已还原为 INSERT、UPDATE、DELETE。

## 总结与追问预判
- 业务账号四件套：SELECT / INSERT / UPDATE / DELETE；**DELETE 常被安全基线砍掉**。
- 逻辑删除 = UPDATE 置标记；代价是查询过滤与唯一索引复杂度。
- 下一题：见 026（SHOW PRIVILEGES）、027（GRANT 授权与最小权限）。
