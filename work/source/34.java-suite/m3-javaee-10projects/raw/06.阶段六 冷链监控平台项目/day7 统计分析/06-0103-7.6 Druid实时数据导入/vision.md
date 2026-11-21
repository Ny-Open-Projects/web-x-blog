# 画面线理解：7.6 Druid实时数据导入

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.6 Druid实时数据导入_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:17, 02:06, 02:26, 03:01, 03:38, 04:25, 04:55, 05:22, 05:40, 06:01, 06:20, 06:41, 07:05, 07:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:42:01

1) 这一组画面整体在讲如何通过 Druid 的 Kafka Indexing Service 实时导入数据，包括创建 Kafka Topic、配置 Spec 文件、提交 Supervisor 以及验证数据导入。

2) 按时间顺序列出每张画面的要点：
画面1：
- 内容：展示 Druid 文档中 3.6.2 实时导入章节，包含创建 Kafka Topic 的命令和列出 Topic 的命令。
- 代码：
  ```bash
  # 创建Kafka队列
  [root@node2-vn06 kafka 2.12-2.3.0]# ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wikipedia
  # 直接查看队列
  [root@node2-vn06 kafka 2.12-2.3.0]# ./bin/kafka-topics.sh --zookeeper 172.17.0.143:2181 --list
  mykafka
  wikipedia
  ```

画面2：
- 内容：展示 Druid 管理台的 Supervisors 页面，显示两个正在运行的 Kafka Supervisor 任务。
- 画面内容：Supervisors 列表包含 "all_device_message" 和 "wikipedia" 两个数据源，状态均为 Running。

画面3：
- 内容：展示用于定义数据导入规格的 JSON Spec 文件，包含数据源、解析器和维度配置。
- 代码：
  ```json
  {
    "type": "kafka",
    "dataschema": {
      "parser": {
        "type": "string",
        "parseSpec": {
          "format": "json",
          "timestampSpec": {
            "column": "time",
            "format": "auto"
          },
          "dimensionsSpec": {
            "dimensions": [
              "channel",
              "cityName",
              "comment",
              "countryIsoCode",
              "countryName",
              "isAnonymous",
              "isMinor",
              "isRobot",
              "isSpam",
              "isUnpatrolled",
              "metroCode",
              "namespace",
              "page",
              "regionIsoCode",
              "regionName"
            ]
          }
        }
      }
    }
  }
  ```

画面4：
- 内容：展示 JSON Spec 文件的完整内容，包含数据源、解析器和维度配置。
- 代码：
  ```json
  {
    "type": "kafka",
    "dataschema": {
      "parser": {
        "type": "string",
        "parseSpec": {
          "format": "json",
          "timestampSpec": {
            "column": "time",
            "format": "auto"
          },
          "dimensionsSpec": {
            "dimensions": [
              "channel",
              "cityName",
              "comment",
              "countryIsoCode",
              "countryName",
              "isAnonymous",
              "isMinor",
              "isRobot",
              "isSpam",
              "isUnpatrolled",
              "metroCode",
              "namespace",
              "page",
              "regionIsoCode",
              "regionName"
            ]
          }
        }
      }
    }
  }
  ```

画面5：
- 内容：展示 Druid 管理台的 Supervisors 页面，提示点击 "Submit supervisor" 按钮。
- 画面内容：Supervisors 页面，红色箭头指向 "Submit supervisor" 按钮。

画面6：
- 内容：展示 Druid 文档中 3.6.2 实时导入章节，包含创建 Kafka Topic 的命令和列出 Topic 的命令。
- 代码：
  ```bash
  # 创建Kafka队列
  [root@node2-vn06 kafka 2.12-2.3.0]# ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wikipedia
  # 直接查看队列
  [root@node2-vn06 kafka 2.12-2.3.0]# ./bin/kafka-topics.sh --zookeeper 172.17.0.143:2181 --list
  mykafka
  wikipedia
  ```

画面7：
- 内容：展示在终端中执行命令，将数据发送到 Kafka 队列，并验证数据已导入 Druid。
- 代码：
  ```bash
  # 解压示例数据
  [root@node2-vn06 druid]# cd /opt/druid/
  [root@node2-vn06 druid]# gunzip -c wiki.ticker-2015-09-12.sampled.json.gz
  [root@node2-vn06 druid]# ll
  [root@node2-vn06 druid]# grep wiki.ticker-2015-09-12.sampled.json
  # 执行生产者程序，将数据发送至Kafka队列
  export KAFKA_OPTS="-Dfile.encoding=UTF-8"
  [root@node2-vn06 druid]# cd /opt
  [root@node2-vn06 druid]# ./opt/software/kafka_2.12-2.3.0/bin/kafka-console-producer.sh --broker-list 172.17.0.143:9092 --topic wikipedia
  # 查看Kafka队列中的消息
  [root@node2-vn06 druid]# ./opt/software/kafka_2.12-2.3.0/bin/kafka-console-consumer.sh --bootstrap-server 172.17.0.143:9092 --topic wikipedia --from-beginning
  ```

画面8：
- 内容：展示在终端中查看 Kafka 队列中的数据，数据包含多个字段，如 channel、cityName、comment 等。
- 代码：
  ```json
  {"added": "2015-09-12T00:00:00.000Z", "channel": "ru.wikipedia", "cityName": "null", "comment": "м: а ч и н к", "countryIsoCode": "null", "countryName": "null", "isAnonymous": "false", "isMinor": "false", "isRobot": "false", "isSpam": "false", "isUnpatrolled": "false", "metroCode": "null", "namespace": "Main", "page": "Александр", "regionIsoCode": "null", "regionName": "null", "timestamp": "2015-09-12T00:00:00.000Z", "title": "Александр", "type": "add", "user": "Александр", "wiki": "ru.wikipedia"}
  ```

画面9：
- 内容：展示 Druid 管理台的 Supervisors 页面，显示两个正在运行的 Kafka Supervisor 任务。
- 画面内容：Supervisors 列表包含 "all_device_message" 和 "wikipedia" 两个数据源，状态均为 Running。

画面10：
- 内容：展示在终端中查看 Kafka 队列中的数据，数据包含多个字段，如 channel、cityName、comment 等。
- 代码：
  ```json
  {"added": "2015-09-12T00:00:00.000Z", "channel": "ru.wikipedia", "cityName": "null", "comment": "м: а ч и н к", "countryIsoCode": "null", "countryName": "null", "isAnonymous": "false", "isMinor": "false", "isRobot": "false", "isSpam": "false", "isUnpatrolled": "false", "metroCode": "null", "namespace": "Main", "page": "Александр", "regionIsoCode": "null", "regionName": "null", "timestamp": "2015-09-12T00:00:00.000Z", "title": "Александр", "type": "add", "user": "Александр", "wiki": "ru.wikipedia"}
  ```

画面11：
- 内容：展示 Druid 文档中 3.6.2 实时导入章节，包含创建 Kafka Topic 的命令和列出 Topic 的命令。
- 代码：
  ```bash
  # 创建Kafka队列
  [root@node2-vn06 kafka 2.12-2.3.0]# ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wikipedia
  # 直接查看队列
  [root@node2-vn06 kafka 2.12-2.3.0]# ./bin/kafka-topics.sh --zookeeper 172.17.0.143:2181 --list
  mykafka
  wikipedia
  ```

画面12：
- 内容：展示 Druid 文
