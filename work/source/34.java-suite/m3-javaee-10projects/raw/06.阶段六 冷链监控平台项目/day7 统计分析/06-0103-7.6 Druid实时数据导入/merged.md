# 7.6 Druid实时数据导入

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.6 Druid实时数据导入_【海量资源尽在 666java.com】.mp4
- 时长 7分36秒（音频 456s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来看一看如何把实时数据导入到我们的Droid里面去那么所谓实时数据一种非常常见的一种数据其实就是卡普卡队列里边的数据那么因为我们的应用系统也好还是其他的一些服务把我们的数据实时拿到了数据之后就推到了卡普卡的队列里面去那么如果Droid监听卡普卡队列里边的数据
[00:28] 卡普卡对列里边来到数据之后呢JED就能把数据存储到JED里边去如果能达到这样的一个效果其实就叫做一个事实了对吧那么所以我们来演示一下如何把数据导入到我们的JED里边去那其实就包含两部分一部分是我们在卡普卡里边要添加一个对列添加一个topic那么
[00:54] 第二部分的话是我们需要在Droid里边添加一个任务Droid中添加的任务就添加一个监听卡普卡队列的一个supervisor也就是卡普卡的indexing这个Service那首先我们先创建一下我们的这个Droid卡普卡的一个队列那么这个队列呢我们用这个命令来进行添加那么卡普卡本身它自己在bin目录下有一个卡普卡topic
[01:23] 这样的一个sh文件那么他用了一个杠杠create啊zookkeeper是本地的一个本地的一个zookkeeper然后呢有一个topic的名字那么我们来看一下我们OK就在这里边那当前呢我们的topic这样就两个我现在要添加一个新的一个topic我使用这个命令来进行添加topic那添加完了之后呢
[01:53] 下一步的时候我就把下一步的时候我要创建我们在supervisor里边要添加一个任务那么这个supervisor就是我添加indexing的一个Service就是卡巴卡的indexing Service来监听卡巴卡的内容卡巴卡队列那么我们在页面上我们其实就点开我们的task然后点击submit supervisor
[02:22] 点开它之后呢我们把我们的这个数据结构填写进来这个数据结构我们稍微简单的介绍一下首先这个类型是卡不卡对吧那么我们的数据的模式数据模型数据的数据表名字叫wikipedia然后它的类型呢我们实际上把它是由一个string类型的进行解析然后数据的格式是一个json
[02:52] 那么数据的一些字段时间字段就是time字段那么数据的字段的名字啊所有的指标字段的名字和我们的wikipediawikipedia的这个里边就wiki的json格式的数据那里边是一样的那另外一块就是我们的ro操作ro操作里边会连接我们的topic到底是连这个连接哪一个也就是
[03:20] 我们的droid它连接哪一个卡普卡的一个topic同时我们的这种卡普卡的服务器的IP和地址那添加进写进来192.17.0.143然后冒号9092这是我们的一个supervisor它的一个内容那么我们在我们的页面里边添加一个supervisorOK那创建上那点击submit
[03:50] 那此时我们就有一个Kafka的一个叫做supervisor的或者Kafka的一个监听任务那么他监听了Kafka的一个队列Kafka队列是叫wikipedia那么此时我们在最的里面添加的就可以了那下一步我们就往我们的这个Kafka队列里面添加数据那么看看添加完数据之后呢会不会把数据实时的保存到我们的
[04:20] 追到里面去那我往里面添加数据的一个也比较简单那我们使用的是我们的这个叫做什么呢我们使用我们的Kafka它的提供的一个producer也就是说Kafka自己本身在闭目录下有一个Kafka自己
[04:49] 的一个providerproducerproducer就是提供者嘛对吧我们来用它来这个这个这个sh文件sh可执行程序来打开一个卡巴卡的topic然后打开之后呢我们把它把我们的数据贴下进来而这个数据呢就是我们在我们的这个测试数据里边的wikitaker这么一个json文件
[05:19] 我们cat一下我们打开这个有点长对吧有点长呢那是没关系我们随时我们找一条数据这条数据我们copy过来那么我们把它填扔到了我们的卡普卡队列里面去那么我们扔到卡普卡队列里面去之后呢那我看一看我们的数据里面会不会有这条记录了呢我们对它扫描里面OK它其实已经有了这条记录了对吧是不是非常快那我要查询
[05:51] 一下wikipedia啊那我此时已经拿到了这个数据了那同样道理我还可以把其他的数据跑不进来我放到我们的放到我们的队列里边去那么我们的罪的里边就已经就能拿到我们的数据了这个就是我们如何来创建我们的实时数据的一个导入简单来讲两部分一部分的话是我们创建我们的Kafka的一个队列那么这个Kafka队列
[06:23] 来实时的监听就是有了业务数据我们就把业务数据扔到Kafka对列里边去那第二部分来讲是我们在JED里边要添加的JED里边要添加一个我们的所谓的Kafkaindexing Service那么Kafkaindexing Service它是通过我们提交一个supervisor来创建的也就是说我提交一个监听任务我这个监听任务就监听Kafka对列而这个监听任务的数据格式呢
[06:52] 是有特定要求的包括我们的数据到底是什么类型的数据数据的时间是什么类型是哪个字段然后数据的每个字段是什么样的表的字段是什么样的以及我们监听的是Kafka队列Kafka队列的名字是什么数据是什么然后Kafka队列的服务器的IP地址和端口是什么那么有了这样的一个supervisor的数据格式
[07:19] 那么我们就可以监听我们刚才创建的卡布卡队列了那么如果有数据进入到卡布卡队列那么实时的就能存储到我们的J的里面去这就是我们整个把实时数据存储到把数据存储到我们的J的里面的一个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Druid 的 Kafka Indexing Service 实时导入数据，包括创建 Kafka Topic、配置 Spec 文件、提交 Supervisor 以及验证数据导入。

2) 按时间顺序列出每张画面的要点：
画面1：
- 内容：展示 Druid 文档中 3.6.2 实时导入章节，包含创建 Kafka Topic 的命令和列出 Topic 的命令。
- 代码：
  ```bash
  # 创建Kafka队列
  [root@node2-vn06 Kafka 2.12-2.3.0]# ./bin/Kafka-topics.sh --create --ZooKeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wikipedia
  # 直接查看队列
  [root@node2-vn06 Kafka 2.12-2.3.0]# ./bin/Kafka-topics.sh --ZooKeeper 172.17.0.143:2181 --list
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
    "type": "Kafka",
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
    "type": "Kafka",
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
  [root@node2-vn06 Kafka 2.12-2.3.0]# ./bin/Kafka-topics.sh --create --ZooKeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wikipedia
  # 直接查看队列
  [root@node2-vn06 Kafka 2.12-2.3.0]# ./bin/Kafka-topics.sh --ZooKeeper 172.17.0.143:2181 --list
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
  [root@node2-vn06 druid]# ./opt/software/kafka_2.12-2.3.0/bin/Kafka-console-producer.sh --broker-list 172.17.0.143:9092 --topic wikipedia
  # 查看Kafka队列中的消息
  [root@node2-vn06 druid]# ./opt/software/kafka_2.12-2.3.0/bin/Kafka-console-consumer.sh --bootstrap-server 172.17.0.143:9092 --topic wikipedia --from-beginning
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
  [root@node2-vn06 Kafka 2.12-2.3.0]# ./bin/Kafka-topics.sh --create --ZooKeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wikipedia
  # 直接查看队列
  [root@node2-vn06 Kafka 2.12-2.3.0]# ./bin/Kafka-topics.sh --ZooKeeper 172.17.0.143:2181 --list
  mykafka
  wikipedia
  ```

画面12：
- 内容：展示 Druid 文

