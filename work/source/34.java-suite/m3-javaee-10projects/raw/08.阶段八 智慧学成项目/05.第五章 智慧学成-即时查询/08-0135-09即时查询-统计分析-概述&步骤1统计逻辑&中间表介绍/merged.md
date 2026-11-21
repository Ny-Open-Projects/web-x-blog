# 09即时查询-统计分析-概述&步骤1统计逻辑&中间表介绍

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\09即时查询-统计分析-概述&步骤1统计逻辑&中间表介绍_【海量资源尽在 666java.com】.mp4
- 时长 5分23秒（音频 323s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来进行统计分析的学习,统计分析呢,一共分为两步,第一步呢,是关联相关维度,然后呢,是统计学习时长,第二步呢,是将数据保存到ES以及HBase中,这里呢,ES是保存查询资段以及Rowkey,HBase呢,是保存咱们统计分析好的完整数据,以上呢,就是咱们统计分析的
[00:31] 就是两个步骤的一个概述接下来呢咱们进行关联维度和统计分析的学习通过关联维度和统计分析的学习呢咱们需要掌握能够对原始数据进行维度的关联统计相关的时长最终呢将数据保存到数据仓库中首先呢咱们来看一下咱们的统计逻辑这里呢是第一步是根据日期来
[01:01] 在HDFS中获取原始数据获取原始数据之后呢这里需要对原始数据进行相关的处理就是关联维度这里呢维度咱们在原型阶段已经分析过下面呢咱们会还有一个中间表在中间表的时候呢也会有详细的一个介绍然后呢是统计学习时长统计完学习时长之后呢就是保存到数据仓库中
[01:31] 这里保存到数据仓库中是并没有最终是落地到HBase和YAS中这里保存到数据仓库中又称之为中间表就是咱们步骤一统计分析完成之后又称之为中间层的清洗最终在中间层生成中间表也就是第四步最终保存到中间表接下来咱们来看中间表的表结构
[02:01] 咱们在第二步的时候提到了这个关联相关的维度这里呢咱们关联相关的维度在咱们中间表中一共是关联了课程的维度课程视频的维度以及呢用户的维度咱们呢从中间表的第一个字段开始讲起第一个字段呢是课程中间表的这个ID这个ID呢是用户学习IDURO ID直接生成
[02:32] 第二个呢是课程ID课程ID呢咱们在采集的时候已经获取了这个课程ID这里呢课程ID本身就是课程维度ID直接就是拿过来使用接下来是课程名称课程名称呢是通过课程ID来关联课程维度进行获取接下来是视频名称视频名称呢是通过关联视频维度的ID来获取这里呢视频维度的ID就是视频ID咱们呢也是直接拿过来的
[03:02] 接下来呢是用户ID用户ID咱们在采集的时候也获取到了也就是用户的维度ID接下来是用户名用户名呢是通过用户维度进行获取通过用户维度来关联这个用户ID来获取咱们的用户名因为用户ID咱们是获取到了可以通过这个来获取用户名接下来呢是学期时间这个学期时间呢是用户的真正的一个学期时间
[03:32] 是以时间戳的方式进行一个存储的这个时间呢是保存的开始学习视频的这个时间因为咱们在JS买点采集的时候为了计算这个学习时长是每一分钟来发送一次这个用户学习行为的数据这个呢开始时间就是第一次发送这个时间就是咱们学用户学习的开始时间咱们这里记录的也是那个第一次的一个时间
[04:05] 用户学习时长就是咱们存用户开始学习到开始学习结束这中间的一个时长咱们呢是通过计算的方式来获取因为咱们在获取这个用户行为数据的时候是采用JS买点的每一分钟来进行一个获取咱们来直接统计这个学习时间出现多少次然后根据这个
[04:35] 相关的关联进行计算即可就可以得到这里的学习时长接下来是DataInfo这个就是具体的一个日期咱们学习时间是时间车的格式对于用户来说直接查看是不友好的咱们为了方便查看这个地方把它给格式化成yyy-mm-dd的这种日期格式很直观的可以进行查看以上就是咱们统计分析的概述
[05:06] 加上咱们步骤一关联相关温度统计分析的一个统计逻辑和咱们统计完成之后产生中间表的一个表结构的介绍通过学习呢需要理解这些好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Hadoop.hbase.io.ImmutableBytesWritable
import org.apache.Spark.sql.SparkSession
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

