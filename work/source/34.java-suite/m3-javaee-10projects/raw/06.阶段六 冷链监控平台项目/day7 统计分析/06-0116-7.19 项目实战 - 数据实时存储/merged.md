# 7.19 项目实战 - 数据实时存储

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.19 项目实战 - 数据实时存储_【海量资源尽在 666java.com】.mp4
- 时长 5分45秒（音频 345s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来看一看冷链设备监控平台它把我们的数据存储到这里边那么存储的数据的结构是一个什么样的那么我们来看一下这个数据结构首先的话是包含我们设备里边所属归属信息的一些状态一些信息包括我们的设备的编码设备所属的主机仓库和所属公司
[00:25] 那另外一部分的话是我们关于设备的它的温度和湿度的上下限那第三部分的话是我们这个设备的提交上来的数据的时候它的这个提交的温度和湿度以及由此计算出来的温度预警和湿度预警的这个状态这是我们的这个数据我们要把这个数据呢提交到我们的这个J的里面去那么首先我们需要创建一个supervisor
[00:56] 双人间supervider的一个任务也就是说在我们的这个DRAID的这个管理端上我们要submit一个supervisor而这个submit的supervisor其实是要保障我们的这个服务器也就是说我们的这个DRAID服务器能够把卡不卡对象卡不卡对链里边的数据集保存到我们的这个DRAID里边去那么我们来看一看这个supervisor它的一个
[01:25] 它的一个这个格式首先呢这个type是Kafka那表明我们其实是要用一个Kafka类型的那第二点来讲的话我们的这个数据的格式数据的datasource这个名字是all device message我们就把它名字其实和我们的Kafka对列名是一样的那我们的这个类型呢是一个string类型的而它的一个
[01:57] 数据的一个结构就是我们的这种叫做json格式的数据而数据的关于时间字段这个时间字段是cur time然后它的类型格式是YYYY4个YMMDD然后实际上就是个时间嘛中间没有没有什么这个分割我们可以看一眼我们的这个数据类型也就是说是我们的这种这个cur time
[02:26] 这个srtime的话是我们实际的一个数据嘛因为我们json卡普卡里的json的数据就是这样的一个类型的那我要把这个类型呢其实就是它的format它的格式就是这样的一个那我的这个dimension spec也就是说它的字段的名字那字段的名字就是和我们数据结构的名字是一样的对吧我把它我的数据结构的名字放进来那下一部分的话
[02:51] 其实是我们的metric spec其实是并没有设置metric spec当然也可以设置metric spec比如说像设置它的总数或者说是或者说平均值等等这些都是后边也可以用到的但是我们在当前这个例子里边并没有用到我的用到的一个叫做granularity数据的数据的时间那么这个时间的实际上是查询结果的
[03:20] 那么我可以按天来进行进行查询就是时间的一个力度对吧那么我在这里边实际上是设置的是按天的也可以按小时那么下一部分的话是我们的关于卡普卡的一个设置了这种卡普卡的设置的话类型的卡普卡然后最大的一个在内存最大的是相当于是这个设置多少是百千万十万百万一百万一百万
[03:50] 100万行那么这一块包括我们的中间有一个啊这个时间啊10m其实是个月吗那下一边呢都是一些默认的一些值默认的一些值来讲的话包括我们这个地方啊如果是http的话http这个是10秒的啊如果是啊shadow的话就是呃这个关闭的一个时间啊3030秒啊80秒等等最后的话
[04:23] 是我们针对的下面的话实际上是针对的我们的RO操作Kafka的Kafka里边的这个类型啊用Kafka的这个主题的名字啊然后他的这个Kafka的这个任务的执行的一个时间间隔然后这块是Kafka对列的IP和地址包括我们的Kafka
[04:55] 执行过程中需要用到的一些参数类似于时间间隔是否是从最早期的来加载那么这个其实就是我们定义Kafka对列和我们的Droid服务Droid存储之间的一个映射关系我们把这个映射关系在我们的这个task里面提交上那么提交完
[05:26] 也就是说在这儿的话是一个submit一个supervisor那么对它提交完之后呢我们其实这个数据就会存储到我们的J的里边来了这是我们对于J的一个数据实施存储的这样的一个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
druid.extensions.loadList=["druid-hdfs-storage", "druid-Kafka-indexing-Service", "druid-datasketches", "mysql-metadata-storage"]

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
  "type": "Kafka",
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
  "type": "Kafka",
  "rollup": false,
  "intervals": null,
  "transformSpec": {
    "filter": null,
    "transforms": []
  },
  "tuningConfig": {
    "type": "Kafka",
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
  "type": "Kafka",
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

