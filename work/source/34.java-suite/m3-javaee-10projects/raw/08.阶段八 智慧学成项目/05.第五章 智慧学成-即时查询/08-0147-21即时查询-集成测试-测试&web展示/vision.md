# 画面线理解：21即时查询-集成测试-测试&web展示

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\21即时查询-集成测试-测试&web展示_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:53, 02:05, 02:28, 03:42, 04:29, 05:02, 05:27, 06:08, 06:50, 08:01, 08:46, 09:19, 09:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:07:35

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 NIFI 流处理系统将数据写入 HBase 和 Elasticsearch，并通过 Web 界面展示最终数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档中“4.4 测试”章节，说明测试流程包括 NIFI 采集生产数据、执行程序将数据写入 Elasticsearch 和 HBase，并在 Spark-web 上查看任务。
画面 2: 在 Elasticsearch 的 Kibana 界面中，展示查询到的课程数据，包含 course_name、video_name、user_name、date_info 等字段。
画面 3: 在终端中执行命令，进入 NIFI 的 Docker 容器，列出 HBase 表，并对表进行 disable、drop、list、scan 操作。
画面 4: 在 Hue 的 File Browser 界面中，展示 Hive 数据库 data_course 下的多个事实表（fact）和维度表（dim）。
画面 5: 在 Hue 的 Table Browser 界面中，展示数据表 learning_course_online_dwm 的元数据信息。
画面 6: 在 Hue 的 Table Browser 界面中，页面加载中，显示加载动画。
画面 7: 在终端中执行命令，对 HBase 表进行 disable、drop、list、scan 操作，显示操作结果。
画面 8: 在 Web 界面中，展示“在线详情”页面，包含学生昵称、课程名称、视频名称、学习时间、学习时长等字段。
画面 9: 在 Web 界面中，展示查询到的数据，包含学生昵称、课程名称、视频名称、学习时间、学习时长等字段。
画面 10: 在浏览器开发者工具中，展示对在线详情页面的 HTTP 请求和响应信息。
画面 11: 在 Web 界面中，展示查询到的数据，包含学生昵称、课程名称、视频名称、学习时间、学习时长等字段。
画面 12: 展示课程文档中“5 web展示”章节，说明数据写入 HBase 和 Elasticsearch 后，可通过 Web 界面查看效果，并提供在线演示 URL。
画面 13: 展示课程文档中“5 web展示”章节，说明数据写入 HBase 和 Elasticsearch 后，可通过 Web 界面查看效果，并提供在线演示 URL。
画面 14: 展示课程文档中“5 web展示”章节，说明数据写入 HBase 和 Elasticsearch 后，可通过 Web 界面查看效果，并提供在线演示 URL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 3:
```bash
[rootox@online-nifi script]# cd /opt/tngs/docker
[rootox@online-nifi script]# ls
hbase-1.2.8 cdh4.6/bin/
[rootox@online-nifi script]# cd /opt/tngs/docker/hbase-1.2.8 cdh4.6/bin/
[rootox@online-nifi script]# ./hbase shell
hbase(main):002:0> list
TABLE
demo
learningOnlineDetail
2 rows in 0.1930 seconds
hbase(main):003:0> disable 'LearningOnlineDetail'
0 row(s) in 2.3590 seconds
hbase(main):004:0> drop 'LearningOnlineDetail'
0 row(s) in 2.2500 seconds
hbase(main):005:0> list
TABLE
demo
1 row(s) in 0.0050 seconds
hbase(main):006:0> list
TABLE
LearningOnlineDetail
2 row(s) in 8.0260 seconds
hbase(main):007:0> scan 'learningOnlineDetail'
```

画面 7:
```bash
hbase(main):002:0> list
TABLE
demo
2 rows in 0.1930 seconds
hbase(main):003:0> disable 'LearningOnlineDetail'
0 row(s) in 2.3590 seconds
hbase(main):004:0> drop 'LearningOnlineDetail'
0 row(s) in 2.2500 seconds
hbase(main):005:0> list
TABLE
demo
1 row(s) in 0.0050 seconds
hbase(main):006:0> list
TABLE
LearningOnlineDetail
2 row(s) in 8.0260 seconds
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“4.4 测试”，内容包括测试流程：1. NIFI 采集生产数据；2. 执行流程程序，程序自动写入到 Elasticsearch，数据保存到 HBase；3. 在 Spark-web 上查看提交的任务。
画面 12: PPT 标题为“5 web展示”，内容包括：数据落地到 Elasticsearch、HBase 后，就可以使用 Web 界面查看效果，在线演示详情 URL: http://xc-online:4000/#/onlineDetail。
画面 13: PPT 标题为“5 web展示”，内容包括：数据落地到 Elasticsearch、HBase 后，就可以使用 Web 界面查看效果，在线演示详情 URL: http://xc-online:4000/#/onlineDetail。
画面 14: PPT 标题为“5 web展示”，内容包括：数据落地到 Elasticsearch、HBase 后，就可以使用 Web 界面查看效果，在线演示详情 URL: http://xc-online:4000/#/onlineDetail。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
