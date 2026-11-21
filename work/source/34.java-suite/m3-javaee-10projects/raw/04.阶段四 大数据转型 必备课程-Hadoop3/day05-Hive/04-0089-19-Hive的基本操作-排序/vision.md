# 画面线理解：19-Hive的基本操作-排序

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\19-Hive的基本操作-排序【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:59, 01:28, 02:00, 04:39, 06:04, 06:38, 07:07, 08:43, 10:20, 12:34, 13:18, 14:43, 15:38, 16:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:44:51

1) 这一组画面整体在讲什么（一句话）：
讲解Hive中排序操作，包括全局排序、按别名排序、分区分组排序（DISTRIBUTE BY）和分组排序（CLUSTER BY）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 内容：展示Hive文档，章节为“2.9.1 全局排序”，讲解ORDER BY子句的用法。
- 代码：
  SELECT * FROM student s LEFT JOIN score sco ON s.s_id = sco.s_id ORDER BY sco.s_score DESC;

画面2：
- 内容：与画面1基本相同，仅光标位置不同，显示“2.9.2 按照别名排序”标题。

画面3：
- 内容：与画面1、2基本相同，光标在“DESC”后，准备执行排序。

画面4：
- 内容：终端显示Hive执行结果，查询学生平均分并按平均分排序。
- 命令：
  hive> select s_id,avg(s_score) avg from score group by s_id order by s_id,avg;

画面5：
- 内容：终端显示Hive执行结果，设置reduce数量为3。
- 命令：
  hive> set mapreduce.job.reduces=3;
  mapreduce.job.reduces=3

画面6：
- 内容：终端显示Hive执行结果，查询按s_id和s_score排序的数据。
- 数据：
  04 01 50 201807
  02 01 60 201807
  06 01 31 201807
  05 01 76 201807
  03 01 80 201807
  01 01 80 201806
  01 03 99 201807

画面7：
- 内容：终端显示Hive执行结果，查询按s_id和s_score排序的数据。
- 数据：
  02 01 70 201806
  03 03 80 201807
  05 01 87 201807
  07 02 89 201806
  01 02 90 201807
  06 01 99 201807
  04 01 50 201807
  02 01 60 201807
  06 01 31 201807
  05 01 76 201807
  03 01 80 201807
  01 01 80 201806
  01 03 99 201807

画面8：
- 内容：终端显示Hive执行命令，准备将查询结果写入本地目录。
- 命令：
  hive> insert overwrite local directory '/export/servers/hivedatas/sort' select * from score sort by s_score;

画面9：
- 内容：展示Hive文档，章节为“2.9.5 分区排序 (DISTRIBUTE BY)”，讲解DISTRIBUTE BY的用法。
- 代码：
  1. set mapreduce.job.reduces=7;
  2. insert overwrite local directory '/export/servers/hivedatas/sort' select * from score distribute by s_id sort by s_score;

画面10：
- 内容：终端显示Hive执行命令，设置reduce数量为7。
- 命令：
  hive> set mapreduce.job.reduces=7;
  mapreduce.job.reduces=7

画面11：
- 内容：终端显示Hive执行结果，查询按s_id和s_score排序的数据。
- 数据：
  04 01 50 201807
  02 01 60 201807
  06 01 31 201807
  05 01 76 201807
  03 01 80 201807
  01 01 80 201806
  01 03 99 201807

画面12：
- 内容：终端显示Hive执行结果，查询按s_id和s_score排序的数据。
- 数据：
  04 01 50 201807
  02 01 60 201807
  06 01 31 201807
  05 01 76 201807
  03 01 80 201807
  01 01 80 201806
  01 03 99 201807

画面13：
- 内容：终端显示Hive执行结果，查询按s_id和s_score排序的数据。
- 数据：
  04 01 50 201806
  05 01 76 201807
  05 02 87 201807
  07 02 89 201806
  01 02 90 201807
  06 01 99 201807
  04 01 50 201807
  02 01 60 201807
  06 01 31 201807
  05 01 76 201807
  03 01 80 201807
  01 01 80 201806
  01 03 99 201807

画面14：
- 内容：展示Hive文档，章节为“2.9.5 分区排序 (DISTRIBUTE BY)”，讲解DISTRIBUTE BY的用法。
- 代码：
  1. set mapreduce.job.reduces=7;
  2. insert overwrite local directory '/export/servers/hivedatas/sort' select * from score distribute by s_id sort by s_score;
