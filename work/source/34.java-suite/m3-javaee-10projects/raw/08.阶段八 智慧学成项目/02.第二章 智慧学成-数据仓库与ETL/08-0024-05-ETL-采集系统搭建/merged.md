# 05-ETL-采集系统搭建

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\05-ETL-采集系统搭建_【海量资源尽在 666java.com】.mp4
- 时长 12分58秒（音频 779s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来学习搭建采集系统,步骤一共有三个。
[00:04] 第一个,配置KafkaConnector。
[00:08] KafkaConnector是Kafka插件的总成,咱们这里使用的插件是Kafuka2HDFS,就是把Kafka的消息持久化到HDFS上。
[00:21] 这里只需要把这个插件配置到Kafka容器中即可。
[00:26] 第二个,部署采集系统。
[00:28] 咱们的采集系统是用于接收用户的行为数据的接收用户的行为数据这里只需要把它给部署起来即可第三个部署学成在线的web前端学成在线的web前端就是把用户的行为数据这里使用JS买点的方式发送到咱们的采集系统它们三个是相互依赖组成最终
[00:58] 组成最终的采集系统以上三个步骤呢文档是在另外两个独立的文档中就是采集系统的部署使用以及咱们的Kafka Connector使用文档咱们按键步骤首先来看第一个Kafka Connector的使用文档切到这里这个文档里边介绍了代码的编写以及它的打包方式还有它的依赖是如何打包的咱们呢
[01:32] 这里只看配置因为咱们的教学目标是大数据的一个从采集清洗到统计分析最终落地到优酷的一个流程这里的代码不是咱们的重点感兴趣可以去了解一下咱们这里就直接配置首先建立一个Kafuka 2 HDFS的目录把咱们的Live目录复制进去这里其实咱们要看一下资料路径里边
[02:02] 在资料路径里面有Kafka的原码以及打包好的依赖咱们这里就直接使用打包好的依赖在package的目录这里有一个打包好的依赖这个呢咱们需要上传到服务器上然后上传完成之后呢按照这个步骤进行一个配置咱们需要去服务器上创建这样一个目录这里呢我直接连到终端上目录的话这里是在
[02:32] OPP-JAS目录这里就直接在这里边进行一个新建Maker.jr然后目录名是这个然后咱们切换到这个目录里切换到这个目录里边切换到这个目录之后呢咱们把这个文件上传到这个目录这里使用WINCP进行一个上传刷新一下就是把刚才的创建的目录就创建出来了这个地方呢
[02:59] 是有一个缓存是之前测试的hub遗留下来的这里把文件上传过来上传完成之后就进行解包即可这里使用unzip进行一个解包好解包完成了咱们可以在这看得到这时候其实这个就可以把它给删掉了因为咱们最终需要的lab包已经出来然后删掉小心咱们再回到文档
[03:34] 这里这是咱们第一步的目录结构已经创建好了咱们可以对比一下用这个WINCPKafka下边Libre下边的这些目录咱们再清了文档这个时候把创建好的目录要上传到Kafka容器中需要在容器中新建Plugins目录然后把Kafka2 HDFN S这个目录再复制到Plugins目录中咱们呢现在
[04:07] Kafka的安装目录中创建 plugins 目录把它复制一下,哎,剪错了复制不是剪接这个时候咱们再开一个终端登录咱们的容器中这里使用 dark exec咱们需要终端加-it 这个参数咱们需要的容器是Kafka这里终端是 baseKafka
[04:35] -2.1.2.1-2.2.0就是咱们的安装目录然后切换进去切换进去完之后在这里新建新建咱们的PluginsMakerDL这个地方错了我来复制一下防止就是单词打错导致等会不能启动这里目录创建好之后咱们切换到这个目录中然后拿到它的绝对路径拿到绝对路径的目的就是等会要用
[05:10] 这里呢咱们切到上层目录直接使用Dark的CP命令把这个目录给复制到咱们的目标容器中咱目标容器就是Kafka咱们的路径就是这个Plugins目录下好这里已经复制完成复制完成呢咱们执行一下那个查看目录的命令这里已经可以看到已经就是把这个给复制进来复制进来呢咱们切到咱们的Kafka的根目录中
[05:40] 就是安装目录中进行一个启动咱们来看这里还没到启动这里还有一个配置就是上面这个插件放到对应的目录之后咱们需要对这个插件对应有一个配置下面这个配置文件就是咱们需要配置的项配置的项就在这个配置文件中首先一共是七行需要配置然后是分为三块把这个也复制一下这个地方
[06:12] 切到咱们的configure目录中现在是在根目录呢直接cd到configure目录然后找到的那个文件configure dd d d就就就就是这个然后使用vm面子进行一个编辑然后tab补全这里呢是我之前配置的时候已经编辑好了这是咱们之前编辑过的就是把之前的给注释掉然后新增这两行
[06:46] 也是把之前的给注释掉新增这两行这个地方最后边就是咱们的插件目录配置的时候也是把插件配置到最后以上配置确认是OK的之后咱们直接退出即可退出完成之后就是咱们的一个启动这个时候再切到咱们的Kafka的安装目录来看咱们的启动命令上面这个启动命令是咱们测试的时候启动
[07:15] 执行完命令之后确认没有报错然后就可以把它给停止掉使用咱们后台启动的方式但是咱们这里测试呢还有很多操作一直使用咱们前台启动的方式到最终就是完全没有问题的时候再使用后台启动的方式咱们来把它给启动起来开回车看有没有报错这个地方看到finish
[07:46] 而且没有看到错误这个 error 等于 0 没有看到错误就说明启动成功了启动成功了之后下面还有一步操作就是提交collector这个提交collector就是把咱们刚才配置的插件让它进行一个生效就是说我这里指定我要使用的这个转换器然后它的转换器有哪些参数给它配置进去咱们先把这个链接给复制了这个链接
[08:17] 咱们就是访问这个链接的时候使用的是postman在这里直接c念一个就行了然后把地址给粘过来这个地方参数是post的请求这个地方还需要注意一点咱们启动的connect是在服务器上启动的但是这里文档中给的地址是什么localhost咱们肯定是访问不到的这个时候就需要咱们配置的域名进行一个访问咱们的域名是学成
[08:45] 再信到Kafkakfk Kafka这个时候呢这个路路径就对了对了之后就把这个给复制过来粘过来因为他是 jsonjson 的话在 border 里边直接选 raw然后这个地方选择 json就行了把它粘进来进行一个 send请求完之后如果没有报错它就会显示把原来的信息给返回过来
[09:16] 没有报错就是这样的一个返回这个时候其实咱们也可以来日志里边查看往上看这个地方已经看到了Connection Class这个就是咱们刚才提交的咱们可以对比一下往上拉一点这个就是咱们刚才提交的就是说我要使用这个类进行一个转换操作咱们的逻辑就是把它把卡帕拉消息持久化到那个HDFS上
[09:48] 那第一步咱们就完成了咱们来切到文档看第二步第二步是启动咱们的采集系统采集系统的话就是咱们采集系统的一个部署使用文档这里有原码的说明以及项目的介绍不是咱们的重点咱们的重点还是部署感兴趣的话可以去了解这里部署它是依赖于Kinect的咱们已经把Kinect给启动好HDFS ZOOkeeper还有卡普卡都是使用的容器
[10:20] 咱们容器也是启动好的这个配置也OK咱们直接看采集系统的一个部署采集的系统的部署咱们是这个它的源码路径还有咱们的包路径在资料中已经提供咱们来看资料这个就是咱们打好的包上面的就是源码咱们直接使用打好的包然后把这个包上传到咱们的服务器上上传服务器使用这个WNSAP
[10:50] 还是放传到这个JAS这个目录这里呢咱们再切到文档这里呢上传的时候咱们这是采集服务另外啊还有一个是咱们的web前台web前台是这个咱们把这两个都一起上传上去切到SAP然后拖进来就行咱们在采集系统这个地方部署它有两种方式一种是单机启动一种是附带进行的一个启动这里呢
[11:24] 我就以单机的方式直接启动它可以让咱们快速的进行测试负载进行的测试使用的是NGX感兴趣的话你可以使用NGX的测试这里上传完成之后就可以直接启动切到咱们的一个终端来看一下传完没已经传完这里这个终端在用不能关咱们在这里使用这个终端-G12把它给启动起来好已经启动完成这里没有挖错
[12:00] 接着启动咱们的web前台web前台的话就是咱们的这个文档就是这个项目来终端进行一个启动这个目录也是在这然后使用table补全这个时候咱们的web前台已经启动好了启动完成之后咱们就是项目环境搭建这个地方已经完成了不是项目环境咱们采集系统的一个环境搭建已经完成了
[12:37] 这是第一个配置卡发卡Connector咱们配置的是卡发卡的2 HDFS插件第二个是采集性能部署非常简单因为咱们东西已经准备好源码打的包已经准备好直接启动集合然后部署外部显台也是直接启动集合好以上就是咱们采集系统搭建

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置和部署 Kafka-Connector（Kafka-to-hdfs），并测试其功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程大纲，当前章节为“3.2 采集系统搭建”，列出搭建步骤：1. 配置Kafka-Connector (Kafka-to-hdfs)；2. 部署采集系统；3. 部署学习在线web前端。资源路径显示为：授课资料 → 第2章 数据仓库与ETL → 采集系统 → Kafka-Connector使用说明.md。
画面2：在文件资源管理器中，显示了“package”目录下的文件，其中“Kafka-to-hdfs.zip”文件被选中。
画面3：在终端中，显示了正在解压多个JAR包，包括“libavro-1.7.4.jar”、“libcommons-beanutils-core-1.8.8.jar”等。
画面4：终端显示了用户登录后的提示符“xc@xc-online:~$”。
画面5：在Typora文档中，显示了Kafka Connector的目录结构，包括“lib”、“plugins”、“site-docs”等目录。并展示了需要修改的配置文件“connect-distributed.properties”的内容，其中包含需要修改的配置项：
# key.converter 与 value.converter 默认值
# key.converter=org.apache.Kafka.connect.storage.StringConverter
# value.converter=org.apache.Kafka.connect.storage.StringConverter
# 修改为：
key.converter=org.apache.Kafka.connect.storage.StringConverter
value.converter=org.apache.Kafka.connect.storage.StringConverter
# 启用开启json转换
# key.converter.schemas.enable=true
# value.converter.schemas.enable=true
# 修改为：
key.converter.schemas.enable=false
value.converter.schemas.enable=false
# 新增配置，指定自定义Connector的配置，这里是以插件的方式，这里使用的是绝对路径
plugin.path=/opt/kafka_2.11-2.0.0/plugins/Kafka-to-hdfs
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
    "hdfs.url": "hdfs://xc-online-Hadoop:9002",
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
画面10：在Typora文档中，显示了“4.1 软件环境”和“4.2 Kafka-Connector配置”章节，其中软件环境包括：Jdk:1.8、Nginx:1.6、Hadoop:2.6.5、Kafka:2.2.0、ZooKeeper:3.4.5。配置参考文档路径为：授课资料 → 第2章 数据仓库与ETL → 采集系统 → Kafka-Connector使用文档.md。
画面11：在WinSCP中，显示了“/opt/jars/Kafka-to-hdfs”目录，其中包含“hdfs”文件夹。
画面12：在WinSCP中，显示了“/opt/jars”目录，其中包含“Kafka-to-hdfs”和“wordcount.jar”两个文件。
画面13：终端显示了Kafka Connect启动后的日志，包括成功启动Connector、加入组、设置分区等信息。
画面14：终端显示了Spring Boot应用启动日志，包括Tomcat启动、Spring上下文初始化等信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面5：
-- config
-- libs
-- logs
-- plugins
  -- Kafka-to-hdfs
    -- lib
    -- Kafka-to-hdfs.jar
  -- ......
-- site-docs
在config目录 找到connect-distributed.properties，修改项目配置，新增加一项配置，详细修改如下：
# key.converter 与 value.converter 默认值
# key.converter=org.apache.Kafka.connect.storage.StringConverter
# value.converter=org.apache.Kafka.connect.storage.StringConverter
# 修改为：
key.converter=org.apache.Kafka.connect.storage.StringConverter
value.converter=org.apache.Kafka.connect.storage.StringConverter
# 启用开启json转换
# key.converter.schemas.enable=true
# value.converter.schemas.enable=true
# 修改为：
key.converter.schemas.enable=false
value.converter.schemas.enable=false
# 新增配置，指定自定义Connector的配置，这里是以插件的方式，这里使用的是绝对路径
plugin.path=/opt/kafka_2.11-2.0.0/plugins/Kafka-to-hdfs

画面9：
{
  "name": "visit_topic",
  "config": {
    "connector.class": "cn.itcast.bigdata.common.kafka_to_hdfs.MHFSinkConnector",
    "tasks.max": "1",
    "topics": "visit_topic",
    "hdfs.url": "hdfs://xc-online-Hadoop:9002",
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

