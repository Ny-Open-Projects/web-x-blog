# 画面线理解：13-热门学科排名-统计分析-销售量-周-代码-根据日期获取数据并计算涨幅

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\13-热门学科排名-统计分析-销售量-周-代码-根据日期获取数据并计算涨幅_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:27, 04:05, 08:47, 09:36, 10:45, 11:07, 11:16, 11:50, 12:30, 13:02, 13:43, 13:54, 14:08, 14:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:18:39

1) 这一组画面整体在讲如何通过Hive SQL和Spark SQL分别实现课程销售数据的周度销售金额及同比变化率计算，并对比两种技术方案的执行过程与结果。

2) 按时间顺序列出每张画面的要点：

画面1：
- 界面：Hue - Editor，连接到Hive。
- 状态：未输入任何SQL语句，提示“你没有保存任何查询”。
- 数据库列表：左侧显示Hive数据库，包括data_agency, data_course, data_dimen, data_platform, data_subject, default。

画面2：
- 界面：Hue - Editor，连接到Hive。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行结果：查询成功，返回14行数据，包含course_category_dim_id, sale_num, sale_percent。

画面3：
- 界面：Hue - Editor，连接到Hive。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行结果：查询成功，返回14行数据，包含course_category_dim_id, sale_num, sale_percent。

画面4：
- 界面：Hue - Editor，连接到Hive。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行结果：查询成功，返回14行数据，包含course_category_dim_id, sale_num, sale_percent。

画面5：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面6：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面7：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面8：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面9：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category
