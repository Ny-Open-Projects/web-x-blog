# 画面线理解：18-Hive的基本操作-分组和多表连接

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\18-Hive的基本操作-分组和多表连接【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:34, 02:33, 04:52, 06:25, 07:24, 08:46, 10:08, 11:12, 12:26, 13:31, 14:54, 16:28, 16:48, 17:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:40:47

1) 这一组画面整体在讲什么（一句话）：
演示 Hive SQL 中 GROUP BY 和 LEFT JOIN 的使用及常见错误处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Hive SQL 教程页面，内容包括 WHERE 子句、GROUP BY 语句和 HAVING 语句。
- 代码示例：
  - `select * from score where s_score > 88 or s_id = '01';`
  - `select * from score where s_id not in ('01','02');`
  - `select s_id ,avg(s_score) from score group by s_id;`
  - `select s_id ,max(s_score) from score group by s_id;`
- 画面中显示了 SecureCRT 连接窗口，提示正在连接到 192.168.174.120。

画面2：
- 在 SecureCRT 中执行了 Hive SQL 语句：`select s.id,s.score,max(s.score) from score group by s.id;`
- 执行结果：出现错误 `FAILED: SemanticException [Error 10025]: Line 1:12 Expression not in GROUP BY key 's_score'`，说明在 GROUP BY 后不能直接使用非分组字段的聚合函数。

画面3：
- 在 SecureCRT 中执行了设置 reducer 数量的命令：
  - `set hive.exec.reducers.max=<number>`
  - `set mapreduce.job.reducers=<number>`
- 执行了 Hive SQL 语句：`select s.id,s.score,max(s.score) from score group by s.id;`
- 执行成功，返回结果：
  - `01 89.66666666666666`
  - `07 93.5`
- 执行时间：35.027 秒，获取 2 行数据。

画面4：
- 在 SecureCRT 中执行了 `desc score;` 命令，查看表结构。
- 输出结果：
  - `s_id string`
  - `c_id string`
  - `s_score int`
  - `month string`
  - `Partition Information`
  - `# col_name data_type comment`
  - `month string`
- 同时显示了 Typora 中的 Notion02.md 文件内容，但未完整显示。

画面5：
- 在 SecureCRT 中执行了 LEFT JOIN 查询语句：
  - `SELECT s.s_id, s.s_score, stu.stu_name, stu.s_birth FROM score s LEFT JOIN stu ON s.s_id = stu.s_id;`
- 执行成功，输出了 36 行数据，包含学生 ID、成绩、姓名和出生日期。

画面6：
- 在 SecureCRT 中执行了 `select * from teacher t left join course c on t.` 命令，但未完整输入。
- 屏幕显示了部分查询结果，包含教师姓名、课程名称等信息。

画面7：
- 在 SecureCRT 中执行了 `select * from teacher t left join course c on t.` 命令，但未完整输入。
- 屏幕显示了部分查询结果，包含教师姓名、课程名称等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```sql
select * from score where s_score > 88 or s_id = '01';
select * from score where s_id not in ('01','02');
select s_id ,avg(s_score) from score group by s_id;
select s_id ,max(s_score) from score group by s_id;
```

画面2：
```sql
hive> select s.id,s.score,max(s.score) from score group by s.id;
```

画面3：
```sql
set hive.exec.reducers.max=<number>
set mapreduce.job.reducers=<number>
```

画面4：
```sql
hive> desc score;
OK
s_id string
c_id string
s_score int
month string
Partition Information
# col_name data_type comment
month string
Time taken: 0.184 seconds, Fetched: 8 row(s)
```

画面5：
```sql
hive> SELECT s.s_id, s.s_score, stu.stu_name, stu.s_birth FROM score s LEFT JOIN stu ON s.s_id = stu.s_id;
```

画面6：
```sql
hive> select * from teacher t left join course c on t.
```

画面7：
```sql
hive> select * from teacher t left join course c on t.
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 无 PPT 标题或架构图/流程图。
- 无表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
- 无。
