# 1252 面试 SQL（三） 深挖：行列互换与复杂报表

> 覆盖源 12-52 全文：窗口函数三兄弟（主卡已讲）+ 行列互换（行转列 pivot）。本附录专攻「行列互换」实战与复杂报表串联。

## 思路与架构

```text
行列互换(pivot) 思路
├─ 行转列: 聚合函数(MAX/SUM) + CASE WHEN 把每行值映射为列 + GROUP BY 维度
├─ 缺科补零: CASE WHEN 无值则 0
└─ 复杂报表: 窗口函数排名 + pivot 转列 串联
```

## 方案取舍
- **CASE WHEN + 聚合 vs 原生 PIVOT**：MySQL 无 `PIVOT` 关键字，标准写法用 `MAX(CASE WHEN subject='语文' THEN score ELSE 0 END)` + `GROUP BY student_id`；可移植到所有 SQL 引擎 [经验]。
- **行转列 vs 列转行**：行转列用聚合+CASE；列转行(列拆多行)用 `UNION ALL` 或 `LATERAL`，方向相反不混。
- **聚合选 MAX 还是 SUM**：每(学生,学科)唯一时用 MAX/SUM 等价；多行时用 SUM 才能汇总。

## 答题技巧
- 行转列模板：先 `SELECT 维度列`，再对每个目标列写 `MAX(CASE WHEN 学科=?' THEN 成绩 ELSE 0 END) AS 列名`，最后 `GROUP BY 维度列` [经验]。
- 主动边界到 `1250-groupby-rollup-case`(GROUP BY+CASE 报表)、`1251-rank-second`(排名)，构成报表 SQL 全栈 [边界]。

```sql
-- 行列互换：成绩表(学号,学科,分数) → 列显示 语文/数学/英语/物理/化学/生物
SELECT student_id,
       MAX(CASE WHEN subject='语文' THEN score ELSE 0 END) AS 语文,
       MAX(CASE WHEN subject='数学' THEN score ELSE 0 END) AS 数学,
       MAX(CASE WHEN subject='英语' THEN score ELSE 0 END) AS 英语,
       MAX(CASE WHEN subject='物理' THEN score ELSE 0 END) AS 物理,
       MAX(CASE WHEN subject='化学' THEN score ELSE 0 END) AS 化学,
       MAX(CASE WHEN subject='生物' THEN score ELSE 0 END) AS 生物
FROM   score
GROUP  BY student_id;
-- 未选学科成绩补 0；MAX 在每(学号,学科)唯一时等价于取值
```
