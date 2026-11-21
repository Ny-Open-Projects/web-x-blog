# 画面线理解：05-ETL-采集系统搭建

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\05-ETL-采集系统搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:18, 02:18, 03:18, 04:17, 05:47, 06:44, 07:40, 08:32, 09:30, 10:14, 10:49, 11:14, 11:44, 12:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:42:22

1) 这一组画面整体在讲如何配置和部署 Kafka-Connector（kafka-to-hdfs），并测试其功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程大纲，当前章节为“3.2 采集系统搭建”，列出搭建步骤：1. 配置Kafka-Connector (kafka-to-hdfs)；2. 部署采集系统；3. 部署学习在线web前端。资源路径显示为：授课资料 → 第2章 数据仓库与ETL → 采集系统 → Kafka-Connector使用说明.md。
画面2：在文件资源管理器中，显示了“package”目录下的文件，其中“kafka-to-hdfs.zip”文件被选中。
画面3：在终端中，显示了正在解压多个JAR包，包括“libavro-1.7.4.jar”、“libcommons-beanutils-core-1.8.8.jar”等。
画面4：终端显示了用户登录后的提示符“xc@xc-online:~$”。
画面5：在Typora文档中，显示了Kafka Connector的目录结构，包括“lib”、“plugins”、“site-docs”等目录。并展示了需要修改的配置文件“connect-distributed.properties”的内容，其中包含需要修改的配置项：
# key.converter 与 value.converter 默认值
# key.converter=org.apache.kafka.connect.storage.StringConverter
# value.converter=org.apache.kafka.connect.storage.StringConverter
# 修改为：
key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.storage.StringConverter
# 启用开启json转换
# key.converter.schemas.enable=true
# value.converter.schemas.enable=true
# 修改为：
key.converter.schemas.enable=false
value.converter.schemas.enable=false
# 新增配置，指定自定义Connector的配置，这里是以插件的方式，这里使用的是绝对路径
plugin.path=/opt/kafka_2.11-2.0.0/plugins/kafka-to-hdfs
画面6：终端显示了Kafka Connect的配置文件内容，包括“bootstrap.servers”、“group.id”、“key.converter”、“value.converter”等配置项。
画面7：终端显示了Kafka Connect启动日志，包括加载插件、注册插件等信息。
画面8：在Postman中，显示了提交Connector的请求地址：http://localhost:8083/connectors，请求类型为POST。
画面9：在Postman中，显示了提交Connector的JSON配置内容：
{
  "name": "visit_topic",
  "config": {
    "connector.class": "cn.itcast.bigdata.common.kafka_to_hdfs.MHFSinkConnector",
    "tasks.max": "1",
    "topics": "visit_topic",
    "hdfs.url": "hdfs://xc-online-hadoop:9002",
    "flush.size": "100",
    "position": "yyy-MM-dd",
    "hdfs.path": "/user/xc/online/data/course/visit_source",
    "name": "visit_topic",
    "tasks": [
      {
        "connector": "visit_topic",
        "task": 0
      }
    ],
    "type": "sink"
  }
}
画面10：在Typora文档中，显示了“4.1 软件环境”和“4.2 Kafka-Connector配置”章节，其中软件环境包括：Jdk:1.8、nginx:1.6、hadoop:2.6.5、kafka:2.2.0、zookeeper:3.4.5。配置参考文档路径为：授课资料 → 第2章 数据仓库与ETL → 采集系统 → Kafka-Connector使用文档.md。
画面11：在WinSCP中，显示了“/opt/jars/kafka-to-hdfs”目录，其中包含“hdfs”文件夹。
画面12：在WinSCP中，显示了“/opt/jars”目录，其中包含“kafka-to-hdfs”和“wordcount.jar”两个文件。
画面13：终端显示了Kafka Connect启动后的日志，包括成功启动Connector、加入组、设置分区等信息。
画面14：终端显示了Spring Boot应用启动日志，包括Tomcat启动、Spring上下文初始化等信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面5：
-- config
-- libs
-- logs
-- plugins
  -- kafka-to-hdfs
    -- lib
    -- kafka-to-hdfs.jar
  -- ......
-- site-docs
在config目录 找到connect-distributed.properties，修改项目配置，新增加一项配置，详细修改如下：
# key.converter 与 value.converter 默认值
# key.converter=org.apache.kafka.connect.storage.StringConverter
# value.converter=org.apache.kafka.connect.storage.StringConverter
# 修改为：
key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.storage.StringConverter
# 启用开启json转换
# key.converter.schemas.enable=true
# value.converter.schemas.enable=true
# 修改为：
key.converter.schemas.enable=false
value.converter.schemas.enable=false
# 新增配置，指定自定义Connector的配置，这里是以插件的方式，这里使用的是绝对路径
plugin.path=/opt/kafka_2.11-2.0.0/plugins/kafka-to-hdfs

画面9：
{
  "name": "visit_topic",
  "config": {
    "connector.class": "cn.itcast.bigdata.common.kafka_to_hdfs.MHFSinkConnector",
    "tasks.max": "1",
    "topics": "visit_topic",
    "hdfs.url": "hdfs://xc-online-hadoop:9002",
    "flush.size": "100",
    "position": "yyy-MM-dd",
    "hdfs.path": "/user/xc/online/data/course/visit_source",
    "name": "visit_topic",
    "tasks": [
      {
        "connector": "visit_topic",
        "task": 0
      }
    ],
    "type": "sink"
  }
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT标题为“3.2 采集系统搭建”，内容包括搭建步骤和资源路径。
画面5：PPT标题为“Kafka Connect 代码及配置”，内容包括目录结构和配置文件修改说明。
画面10：PPT标题为“4.1 软件环境”和“4.2 Kafka-Connector配置”，内容包括软件环境和配置参考文档路径。

5) 无。
