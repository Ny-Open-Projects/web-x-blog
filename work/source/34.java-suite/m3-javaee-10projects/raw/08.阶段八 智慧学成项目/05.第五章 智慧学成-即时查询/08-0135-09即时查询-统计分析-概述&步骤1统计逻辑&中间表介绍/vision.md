# 画面线理解：09即时查询-统计分析-概述&步骤1统计逻辑&中间表介绍

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\09即时查询-统计分析-概述&步骤1统计逻辑&中间表介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:27, 01:41, 02:00, 02:05, 02:50, 03:02, 04:19, 04:22, 04:31, 04:34, 05:01, 05:03, 05:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:58:01

1) 这一组画面整体在讲什么（一句话）：
讲解用户学习行为的统计分析流程，包括从HDFS获取原始数据、关联维度表、统计学习时长，并将结果保存到数据仓库（DWM层）和ES/HBase中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1: 展示文档目录结构，当前选中“3.2 步骤2: 保存到es, hbase”。
画面2: 展示“3.2.1 保存逻辑”和“3.2.2 代码”小节，代码部分显示了Scala包导入语句。
画面3: 展示“3.1.1 统计逻辑”和“3.1.2 中间表结构”小节，中间表结构表格中“course_name”字段的“源数据字段”为“通过course_id关联”。
画面4: 展示“3.1.2 中间表结构”小节，表格中“video_name”字段的“源数据字段”为“通过course_video_id关联”。
画面5: 展示“3.1.2 中间表结构”小节，表格中“user_id”字段的“源数据字段”为“user_id”。
画面6: 展示“3.1.2 中间表结构”小节，表格中“learn_time”字段的“源数据字段”为“learn_time”。
画面7: 展示“3.1.3 代码”小节，代码部分显示了“InstantQueryStep1ToHive.scala”文件名。
画面8: 展示“3.1.1 统计逻辑”小节，列出四个步骤：1. 根据日期从HDFS中获取原始数据；2. 关联相关维度表；3. 统计学习时长；4. 保存到数据仓库中。
画面9: 展示“3.1.2 中间表结构”小节，表格中“course_name”字段的“源数据字段”为“通过course_id关联”。
画面10: 展示“3.1.1 统计逻辑”小节，列出四个步骤。
画面11: 展示“3.1.3 代码”小节，代码部分显示了“InstantQueryStep1ToHive.scala”文件名。
画面12: 展示“3.1.3 代码”小节，代码部分显示了“InstantQueryStep1ToHive.scala”文件名。
画面13: 展示“3.1.2 中间表结构”小节，表格中“date_info”字段的“源数据字段”为“通过learn_time格式化”。
画面14: 展示“3 统计分析”章节标题和“3.1 步骤1: 关联维度统计分析”小节。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
```
InstantQueryStep2ToHBaseAndES.scala
package cn.itcast.xc.analysis.search
import cn.itcast.xc.analysis.common.EtlEnvironment
import cn.itcast.xc.analysis.common.EtlEnvironment.{config, esConfig, init, initCluster}
import cn.itcast.xc.entity.{LearningCourseOnlineDwm, LearningCourseOnlineEsIndex}
import cn.itcast.xc.utils.HBaseUtils
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.spark.sql.SparkSession
```

画面7代码：
```
InstantQueryStep1ToHive.scala
```

画面12代码：
```
InstantQueryStep1ToHive.scala
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3表格数据：
| 用户学习中间表字段 | 源数据字段 | 字段说明 |
| --- | --- | --- |
| learning_course_online_id | - | 用户学习id, uuid生成 |
| course_id | 通过course_id关联 | 课程维度id |
| course_name | 通过course_id关联 | 课程名称 |
| video_name | 通过course_video_id关联 | 视频名称 |
| user_id | user_id | 用户维度id |
| user_name | 通过user_id关联 | 用户名 |
| learn_time | learn_time | 学习时间 |
| learn_count | 通过learn_time计算 | 学习时长 |
| date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

画面4表格数据：
| 用户学习中间表字段 | 源数据字段 | 字段说明 |
| --- | --- | --- |
| learning_course_online_id | - | 用户学习id, uuid生成 |
| course_id | 通过course_id关联 | 课程维度id |
| course_name | 通过course_id关联 | 课程名称 |
| video_name | 通过course_video_id关联 | 视频名称 |
| user_id | user_id | 用户维度id |
| user_name | 通过user_id关联 | 用户名 |
| learn_time | learn_time | 学习时间 |
| learn_count | 通过learn_time计算 | 学习时长 |
| date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

画面6表格数据：
| 用户学习中间表字段 | 源数据字段 | 字段说明 |
| --- | --- | --- |
| learning_course_online_id | - | 用户学习id, uuid生成 |
| course_id | 通过course_id关联 | 课程维度id |
| course_name | 通过course_id关联 | 课程名称 |
| video_name | 通过course_video_id关联 | 视频名称 |
| user_id | user_id | 用户维度id |
| user_name | 通过user_id关联 | 用户名 |
| learn_time | learn_time | 学习时间 |
| learn_count | 通过learn_time计算 | 学习时长 |
| date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

画面13表格数据：
| 用户学习中间表字段 | 源数据字段 | 字段说明 |
| --- | --- | --- |
| learning_course_online_id | - | 用户学习id, uuid生成 |
| course_id | 通过course_id关联 | 课程维度id |
| course_name | 通过course_id关联 | 课程名称 |
| video_name | 通过course_video_id关联 | 视频名称 |
| user_id | user_id | 用户维度id |
| user_name | 通过user_id关联 | 用户名 |
| learn_time | learn_time | 学习时间 |
| learn_count | 通过learn_time计算 | 学习时长 |
| date_info | 通过learn_time格式化 | yyyy-MM-dd格式日期 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
