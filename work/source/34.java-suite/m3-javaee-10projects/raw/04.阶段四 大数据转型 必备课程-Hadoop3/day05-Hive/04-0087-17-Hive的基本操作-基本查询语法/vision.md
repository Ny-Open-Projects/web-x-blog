# 画面线理解：17-Hive的基本操作-基本查询语法

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\17-Hive的基本操作-基本查询语法【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:35, 04:20, 04:53, 05:16, 05:47, 06:11, 06:30, 06:56, 07:33, 08:29, 09:29, 10:24, 10:50, 11:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:34:28

1) 这一组画面整体在讲 Hive 查询语法，包括 SELECT 语句、常用函数及逻辑运算符，并通过终端演示执行效果。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：讲解 Hive SELECT 语句语法结构，包括 SELECT、FROM、WHERE、GROUP BY、CLUSTER BY、DISTRIBUTE BY、SORT BY、LIMIT 等子句，并说明排序操作对性能的影响。
代码：
SELECT [ALL | DISTINCT] select_expr, select_expr, ...
FROM table_reference
[WHERE where_condition]
[GROUP BY col_list [HAVING condition]]
[CLUSTER BY col_list]
[ DISTRIBUTE BY col_list ] [SORT BY col_list]
[ LIMIT number ]

画面2：
要点：讲解 SELECT 语句的全表查询和选择特定列，介绍列别名的用法。
代码：
select s_id ,c_id from score;
select s_id as myid ,c_id from score;

画面3：
要点：继续讲解 SELECT 语句，展示使用 AS 关键字为列设置别名。
代码：
select s_id as myid ,c_id from score;

画面4：
要点：在 SecureCRT 终端中执行 Hive SQL 语句，展示设置 reduce 任务数的配置命令。
命令：
set hive.exec.reducers.bytes.per.reducer=<number>
set hive.exec.reducers.max=<number>
set mapreduce.job.reduces=<number>

画面5：
要点：在 SecureCRT 终端中执行 Hive SQL 语句，展示查询结果和执行时间。
命令：
hive> select * from score;
Time taken: 0.237 seconds. Fetched: 3 row(s)

画面6：
要点：展示 Hive 中的逻辑运算符表，包括基本比较运算符和 IS NULL 运算符。
表格结构：
| 运算符 | 说明 |
|--------|------|
| A=B | 基本数据类型 |
| A<>B | 基本数据类型 |
| A<B | 基本数据类型 |
| A<=B | 基本数据类型 |
| A>B | 基本数据类型 |
| A>=B | 基本数据类型 |
| A [NOT] BETWEEN B AND C | 基本数据类型 |
| A IS NULL | 所有数据类型 |

画面7：
要点：在 SecureCRT 终端中显示查询结果，展示多行数据。
数据：
01 01 80 201806
01 02 90 201806
01 03 99 201806
02 01 80 201806
03 01 02 80 201806
03 03 03 80 201806
05 02 87 201806
07 02 89 201806
07 03 80 201806
01 01 80 201807
01 02 90 201807
01 03 99 201807
02 01 80 201807
03 01 02 80 201807
03 03 03 80 201807
05 02 87 201807
07 02 89 201807
