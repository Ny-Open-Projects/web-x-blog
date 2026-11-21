# 画面线理解：07即时查询-数据采集-用户学习采集

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\07即时查询-数据采集-用户学习采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:02, 02:13, 02:41, 03:38, 04:01, 04:28, 04:52, 05:57, 06:28, 06:47, 07:01, 07:33, 07:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:56:42

1) 这一组画面整体在讲如何通过 Kafka Connect 配置将用户学习行为数据采集并写入 HDFS，以及如何通过 Hue 查看采集结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Typora 文档中“2.1.1 采集配置”章节，说明只需添加用户学习的 Kafka Connect 配置，提供 JSON 格式的配置内容。
画面2：展示 Typora 文档中“3.3.1.1 课程访问量JS埋点代码”，列出用于采集课程访问量的 JavaScript 代码片段。
画面3：展示 Typora 文档中“2.1.1 采集配置”章节，强调配置内容。
画面4：展示 Postman 中向 http://xc-online-kafka:8083/connectors 发送 POST 请求，请求体为 JSON 格式的 Kafka Connect 配置。
画面5：展示 Typora 文档中“2.1.1 采集配置”章节，强调配置内容。
画面6：展示浏览器中 CKplayer 播放器界面，鼠标悬停在“Network”标签页。
画面7：展示 Typora 文档中“2.1.3 查看采集结果”章节，说明使用命令查看 Kafka 消费数据，并展示 Hue File Browser 中的文件内容。
画面8：展示浏览器中 CKplayer 播放器界面，弹出右键菜单。
画面9：展示 Xshell 终端，执行 docker exec 命令进入容器并进入 bash。
画面10：展示 Hue File Browser 中的文件内容，显示采集到的用户访问数据。
画面11：展示浏览器中 CKplayer 播放器界面。
画面12：展示浏览器中 CKplayer 播放器界面。
画面13：展示 Hue File Browser 中的文件内容，显示采集到的用户访问数据。
画面14：展示 Typora 文档中“2.2 维度采集-课程视频维度”章节，说明业务系统展示视频名称和视频来源，使用 NIFR 进行采集，并列出相关资料。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```json
{
  "url": "http://xc-online-kafka:8083/connectors",
  "请求方式": "POST",
  "json 参数": {
    "name": "user_lean_topic",
    "config": {
      "connector.class": "cn.itcast.bigdata.common.kafka_to_hdfs.hdfs.HdfsSinkConnector",
      "tasks.max": "1",
      "topics": "user_lean_topic",
      "hdfs.url": "hdfs://xc-online-hadoop:9000/",
      "flush.size": "100",
      "expression": "yyyy-MM-dd",
      "hdfs.path": "/user/hive/external/data_course/learning_course_online_source/",
      "name": "user_lean_topic"
    }
  }
}
```
画面4：
```json
{
  "name": "user_lean_topic",
  "config": {
    "connector.class": "cn.itcast.bigdata.common.kafka_to_hdfs.hdfs.HdfsSinkConnector",
    "tasks.max": "1",
    "topics": "user_lean_topic",
    "hdfs.url": "hdfs://xc-online-hadoop:9000/",
    "flush.size": "100",
    "expression": "yyyy-MM-dd",
    "hdfs.path": "/user/hive/external/data_course/learning_course_online_source/",
    "name": "user_lean_topic"
  }
}
```
画面7：
```bash
/kafka-console-consumer.sh --bootstrap-server xc-online-kafka:9092 --topic user_lean_topic
```
画面9：
```bash
docker exec -it xc-online-kafka bash
```
画面10：
```
/user/hive/external/data_course/learning_course_online_source/2019-12-10/
```
画面13：
```
/user/hive/external/data_course/learning_course_online_source/2019-12-11/
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
