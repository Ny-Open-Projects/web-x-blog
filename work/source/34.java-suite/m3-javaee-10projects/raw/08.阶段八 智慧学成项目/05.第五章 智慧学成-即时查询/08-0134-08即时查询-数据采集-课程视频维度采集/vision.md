# 画面线理解：08即时查询-数据采集-课程视频维度采集

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\08即时查询-数据采集-课程视频维度采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:32, 00:47, 00:57, 01:07, 01:21, 01:58, 02:09, 02:37, 02:56, 03:08, 03:22, 03:41, 03:50, 04:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:57:16

1) 这一组画面整体在讲如何通过 Nifi 平台采集课程视频维度数据，并在 Hue 中查看和分析数据。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 Hue 的 File Browser 中，显示了 /user/hue 目录下的文件，包括一个名为 "J" 的文件夹和一个名为 "." 的文件夹。
画面 2: 在 Nifi Flow 界面中，弹出一个 "Upload Template" 对话框，提示选择模板文件 "课程视频维度采集.xml"。
画面 3: 在 Nifi Flow 界面中，显示了五个处理器的运行状态，包括 "时长维度"、"课程信息维度"、"用户-维度"、"课程分类-维度" 和 "课程视频-维度"。
画面 4: 在 Nifi 的 "课程视频 - 维度 Configuration" 页面，显示了三个控制器服务：DistributedMapCacheServer、HiveConnectionPool 和 DBCPConnectionPool，其中 HiveConnectionPool 和 DBCPConnectionPool 的状态为 "Enabled"。
画面 5: 与画面 4 相同，显示了三个控制器服务的状态。
画面 6: 在 Hue 的 Table Browser 中，显示了 "course_video_dim" 表的属性和列信息，包括表名、位置、文件数、大小以及列名和类型。
画面 7: 在 Hue 的 Table Browser 中，显示了 "course_video_dim" 表的样本数据，包括 course_video_dim_video_id、course_video_dim_video_name、course_video_dim_course_id 和 course_video_dim_video_duration 等字段。
画面 8: 在终端中，执行了 cd kafka 命令，进入 Kafka 目录，并执行了 ./kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic user_topic 命令，用于消费 Kafka 中的用户主题数据。
画面 9: 与画面 7 相同，显示了 "course_video_dim" 表的样本数据。
画面 10: 在 Hue 的 Table Browser 中，显示了 "course_video_dim" 表的更多样本数据，包括 "?????"、"java???"、"Hello World" 等内容。
画面 11: 在终端中，执行了 ./nifi-env.sh nifi-run-nifi.bat status.bat 命令，用于查看 Nifi 服务的状态，并显示了 Nifi 服务正在关闭。
画面 12: 在 Hue 的 Table Browser 中，页面正在加载中，显示一个加载图标。
画面 13: 在 Hue 的 Table Browser 中，显示了 "course_video_dim" 表的更多样本数据，包括 "JavaScriptVueJS"、"Vuejs 一节"、"Vuejs 二节"、"Vuejs 三节" 等内容。
画面 14: 在 Typora 编辑器中，显示了文档 "2.2 维度采集-课程视频维度" 的内容，包括业务系统展示视频名称、视频名称来自课程视频维度、使用 Nifi 进行采集、Nifi 配置位置等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2: 无
画面 3: 无
画面 4: 无
画面 5: 无
画面 6: 无
画面 7: 无
画面 8: cd kafka
./kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic user_topic
画面 9: 无
画面 10: 无
画面 11: ./nifi-env.sh nifi-run-nifi.bat status.bat
画面 12: 无
画面 13: 无
画面 14: 无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14: PPT 标题为 "2.2 维度采集-课程视频维度"，内容包括：
- 业务系统展示视频名称，视频名称来自课程视频维度，这里使用 Nifi 进行采集。
- Nifi 配置位置请参考：智慧学堂-第2章-ETL：维度数据采集。
- 3 统计分析
  - 3.1 步骤1: 关联维度统计分析
    - 3.1.1 统计逻辑
      1. 根据日期从 hdfs 中获取网站数据
      2. 关联相关维度表

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
