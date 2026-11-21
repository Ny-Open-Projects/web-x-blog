# 画面线理解：11即时查询-统计分析-步骤1：代码-注册udf函数

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\11即时查询-统计分析-步骤1：代码-注册udf函数_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:31, 00:39, 00:48, 00:51, 01:01, 01:48, 01:51, 03:16, 03:39, 04:01, 04:23, 04:28, 05:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:59:43

1) 这一组画面整体在讲如何使用 Spark SQL 读取 HDFS 中的用户学习行为原始数据，并通过 UDF 自定义函数处理学习时长，最终将结果写入 Hive 表。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Scala 代码，定义 SparkSession，读取 HDFS 中的原始数据，创建临时视图，并设置 Hive 动态分区模式。
画面2：展示 PPT 内容，介绍“3.1.2 中间表结构”，说明用户学习中间表的字段及其来源。
画面3：展示 PPT 内容，介绍“3.1 步骤: 关联维度统计分析”，列出统计逻辑步骤。
画面4：展示 PPT 内容，介绍“1.4 ODS数据存储分析-用户学习”，说明数据存储格式、存储方式和数据样例。
画面5：展示 PPT 内容，介绍“1.3.2 ODS层数据结构-用户学习”，列出采集字段、字段说明、数据格式和数据样例。
画面6：展示 PPT 内容，介绍“1.3.2 ODS层数据结构-用户学习”，列出采集字段、字段说明、数据格式和数据样例。
画面7：展示 PPT 内容，介绍“3.1.1 统计逻辑”，列出统计步骤。
画面8：展示 PPT 内容，介绍“1.4 ODS数据存储分析-用户学习”，说明数据存储格式、存储方式和数据样例。
画面9：展示 Scala 代码，继续编写主函数，准备读取数据。
画面10：展示 Scala 代码，通过 `spark.udf.register` 注册自定义函数 `getUid`。
画面11：展示 Scala 代码，定义 `main` 函数，初始化 SparkSession 和 SparkContext。
画面12：展示 Scala 代码，继续编写主函数，注册自定义函数 `getUid`。
画面13：展示 Scala 代码，定义 `minConvertDayHourMin` 函数，用于将秒数转换为天、小时、分钟和秒。
画面14：展示 Scala 代码，继续编写主函数，注册自定义函数 `minConvertDayHourMin`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```scala
val sc = spark.sparkContext
val date_info = "2019-12-11"
val learnSource = sc.textFile(path = s"/user/hive/external/data_course/learning_course_online_source/${date_info}")
val learnSourceRDD = learnSource.map(_.split(regexp = "\t")).map(arr => {
  UserLearnOnline(arr(0), arr(1), arr(2), arr(3), arr(4), arr(5).toLong)
})
spark.createDataFrame(learnSourceRDD).createOrReplaceTempView(viewName = "learn_source_tmp")
```

画面10：
```scala
spark.udf.register(name = "getUid", () => {
  getUid()
})
```

画面12：
```scala
spark.udf.register(name = "getUid", () => {
  getUid()
})
```

画面14：
```scala
spark.udf.register(name = "minConvertDayHourMin", (time: Long) => {
  minConvertDayHourMin(time)
})
```

4) PPT 标题、架构图/流程图的结构、表格数据（逐字原样抄录）：
画面2：
标题：3.1.2 中间表结构
表格：
| 用户学习中间表字段 | 源数据字段 | 字段说明 |
| --- | --- | --- |
| learning_course_online_id | - | 用户学习id, uuid生成 |
| course_id | 通过course_id关联 | 课程id |
| course_name | 通过course_id关联 | 课程名称 |
| video_id | 通过course_video_id关联 | 视频id |
| user_id | user_id | 用户id |
| user_name | 通过user_id关联 | 用户名 |
| learn_time | learn_time | 学习时间 |

画面3：
标题：3.1 步骤: 关联维度统计分析
子标题：3.1.1 统计逻辑
列表：
1. 根据日期从hdfs中获取原始数据
2. 关联相关维度表
3. 统计学习时长
4. 保存到数据仓库中

画面4：
标题：1.4 ODS数据存储分析-用户学习
子标题：数据存储格式：hdfs 文本文件
子标题：数据存储方式：按年-月-日目录名，每天的数据存在一个目录中，如：/user/hive/external/data_course/learning_course_online_source/${format('yyyy-MM-dd')}
子标题：数据内容格式：数据块行：\n
子标题：数据样例：
```
c88d0387fa5943d09904498c7f04b0c
2e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c62400aa3160286618305
Chrome 157050891
c88d0387fa5943d09904498c7f04b0c
92e6e6dff3c6240
