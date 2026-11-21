# 画面线理解：7.19 项目实战 - 数据实时存储

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.19 项目实战 - 数据实时存储_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:11, 00:34, 01:03, 01:24, 02:21, 02:43, 03:53, 04:21, 04:26, 04:58, 05:22, 05:34, 05:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:50:16

1) 这一组画面整体在讲如何配置和使用 Apache Druid 的 Kafka Indexing Service 来实时摄取和处理 Kafka 数据，并展示数据结构和查询结果。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Druid 的架构图，说明数据从 Kafka 经过 Indexing Service 处理后写入 Druid，同时显示了配置文件中添加的索引服务列表。
画面2: 展示数据表结构，列出设备相关字段及其类型、长度、主键和备注。
画面3: 展示数据表结构，列出温度、湿度、设备状态等字段及其类型、长度和备注。
画面4: 展示 Druid Web UI 的 Supervisors 页面，显示一个正在运行的 Kafka 数据源任务。
画面5: 展示数据表结构，列出经纬度和提交时间字段及其类型、长度和备注。
画面6: 展示 Druid Web UI 的 Query 页面，输入 SQL 查询语句并准备执行。
画面7: 展示 Druid 的 JSON 配置文件，定义了数据源、解析器和维度。
画面8: 展示 Druid 的 JSON 配置文件，定义了索引配置，包括数据类型、维度压缩和编码。
画面9: 展示 Druid 的 JSON 配置文件，定义了 IO 配置，包括 Kafka 主题、副本数、任务持续时间等。
画面10: 展示 Druid 的 JSON 配置文件，定义了 IO 配置，包括 Kafka 主题、副本数、任务持续时间等。
画面11: 展示 Druid 的 JSON 配置文件，定义了 IO 配置，包括 Kafka 主题、副本数、任务持续时间等。
画面12: 展示 Druid Web UI 的 Supervisors 页面，显示一个正在运行的 Kafka 数据源任务。
画面13: 展示 Druid Web UI 的 Tasks 页面，显示多个任务状态，其中有一个正在运行。
画面14: 展示 Druid 的 JSON 配置文件，定义了 IO 配置，包括 Kafka 主题、副本数、任务持续时间等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
druid.extensions.loadList=["druid-hdfs-storage", "druid-kafka-indexing-service", "druid-datasketches", "mysql-metadata-storage"]

画面2:
| 名称 | 类型 | 长度 | 是否主键 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- |
| meterCode | varchar | 50 | 1 |  | 设备编码 |
| meterId | varchar | 50 |  |  | 设备ID |
| meterName | varchar | 100 |  |  | 主机id |
| hostId | varchar | 50 |  |  | 主机编码 |
| hostName | varchar | 100 |  |  | 主机名称 |
| houseId | varchar | 50 |  |  | 仓库id |
| houseCode | varchar | 50 |  |  | 仓库编码 |
| houseName | varchar | 100 |  |  | 仓库名称 |
| companyId | varchar | 50 |  |  | 公司id |
| companyName | varchar | 100 |  |  | 公司名称 |

画面3:
| 名称 | 类型 | 长度 | 备注 |
| --- | --- | --- | --- |
| tem | int | 5 | 温度 |
| maxTem | int | 5 | 温度上限 |
| minTem | int | 5 | 温度下限 |
| hum | int | 5 | 湿度 |
| maxHum | int | 5 | 湿度上限 |
| minHum | int | 5 | 湿度下限 |
| temAlert | int | 5 | 0 | 温度状态：1：高温，0：正常，-1：低温 |
| humAlert | int | 5 | 0 | 湿度状态：1：高温，0：正常，-1：低温 |
| state | int | 5 | 设备状态:1-在用，0-停用，2-异常 |
| lon | varchar | 30 | 经度 |
| lat | varchar | 30 | 纬度 |
| curtime | varchar | 50 | CURRENT_TIMESTAMP | 提交时间 |

画面5:
| 名称 | 类型 | 长度 | 备注 |
| --- | --- | --- | --- |
| lon | varchar | 30 | 经度 |
| lat | varchar | 30 | 纬度 |
| curtime | varchar | 50 | CURRENT_TIMESTAMP | 提交时间 |

画面7:
{
  "type": "kafka",
  "dataSchema": {
    "dataSource": "all_device_message",
    "parser": {
      "type": "string",
      "parseSpec": {
        "format": "json",
        "timestampSpec": {
          "column": "curtime",
          "format": "yyyyMMddHHmmss"
        },
        "dimensionsSpec": {
          "dimensions": [
            "companyId",
            "companyname",
            "curtime",
            "hostid",
            "hostname",
            "housecode",
            "metercode",
            "meterid",
            "metername",
            "lon",
            "lat",
            "maxTem",
            "minTem",
            "maxHum",
            "minHum"
          ]
        }
      }
    }
  }
}

画面8:
{
  "type": "kafka",
  "rollup": false,
  "intervals": null,
  "transformSpec": {
    "filter": null,
    "transforms": []
  },
  "tuningConfig": {
    "type": "kafka",
    "maxRowsInMemory": 1000000,
    "maxBytesInMemory": 0,
    "maxRowsPerSegment": 5000000,
    "intermediatePersistPeriod": "PT10M",
    "basePersistDirectory": "/opt/druid/var/temp",
    "maxPendingPersists": 0,
    "indexSpec": {
      "type": "concise"
    },
    "dimensionCompression": "lz4",
    "metricCompression": "lz4",
    "longEncoding": "longs"
  }
}

画面9:
{
  "type": "kafka",
  "buildV90Directly": true,
  "reportParseExceptions": false,
  "handoffConditionTimeout": 0,
  "resetOffsetAutomatically": false,
  "segmentWriteOutMediumFactory": null,
  "chatThreads": null,
  "chatRetries": 8,
  "httpTimeout": "PT10S",
  "shutdownTimeout": "PT60S",
  "offsetFetchPeriod": "PT30S",
  "intermediateHandoffPeriod": "P2147483647D",
  "logParseExceptions": false,
  "maxParseExceptions": 2147483647,
  "maxSavedParseExceptions": 0,
  "skipSequenceNumberAvailabilityCheck": false
}

画面10:
{
  "ioConfig": {
    "topic": "all_device_message",
    "replicas": 1,
    "taskCount": 1,
    "taskDuration": "PT6000S",
    "consumerProperties": {
      "bootstrap.servers": "172.17.0.143:9092"
    }
  }
}

画面11:
{
  "ioConfig": {
    "topic": "all_device_message",
    "replicas": 1,
    "taskCount": 1,
    "taskDuration": "PT6000S",
    "consumerProperties": {
      "bootstrap.servers": "172.17.0.143:9092"
    }
  },
  "pollTimeout": 100,
  "startDelay": "PT5S",
  "period": "PT30S",
  "useEarliestOffset": false,
  "completionTimeout": "PT1200S",
  "lateMessageRejectionPeriod": null,
  "earlyMessageRejectionPeriod": null,
  "stream": "all_device_message",
  "useEarliestSequenceNumber": false
}

画面14:
{
  "ioConfig": {
    "topic": "all_device_message",
    "replicas": 1,
    "taskCount": 1,
    "taskDuration": "PT6000S",
    "consumerProperties": {
      "bootstrap.servers": "172.17.0.143:9092"
    }
  },
  "pollTimeout": 100,
  "startDelay": "PT5S",
  "period": "PT30S",
  "useEarliestOffset": false,
  "completionTimeout": "PT1200S",
  "lateMessageRejectionPeriod": null,
  "earlyMessageRejectionPeriod": null,
  "stream": "all_device_message",
  "useEarliestSequenceNumber": false,
  "context": null,
  "
