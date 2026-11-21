# Nifi使用文档

- 来源：04.阶段四 大数据转型 必备课程-Hadoop3\JavaEE中级进修课资料（新版）\08.基于大数据的智慧学成项目课程\day03\资料\第2章-数据仓库与ETL\Nifi使用文档【海量资源尽在 666java.com】.pdf
- 页数：27
- 抽取：pypdf 文本层



<!-- page 1 -->
Niﬁ 使⽤⽂档
 
1, Apache Niﬁ 概念  
1.1, NIFI 简介  
Apache NiFi 是⼀个易于使⽤，功能强⼤且可靠的系统，⽤于处理和分发数据。可以⾃动化管理系统间
的数据流。它⽀持⾼度可配置的指⽰图的数据路由、转换和系统中介逻辑，⽀持从多种数据源动态拉取
数据。 NiFi 原来是 NSA 的⼀个项⽬，⽬前已经代码开源，是 Apache 基⾦会的顶级项⽬之⼀。
NiFi 是基于 Java 的，使⽤ Maven ⽀持包的构建管理。  NiFi 基于 Web ⽅式⼯作，后台在服务器上进⾏调
度。⽤⼾可以为数据处理定义为⼀个流程，然后进⾏处理，后台具有数据处理引擎、任务调度等组件。
 
1.2, NIFI 核⼼概念  
FlowFile ：表⽰通过系统移动的每个对象，包含数据流的基本属性
FlowFile Processor （处理器）：负责实际对数据流执⾏⼯作
Connection （连接线）：负责不同处理器之间的连接，是数据的有界缓冲区
Flow Controller （流量控制器）：管理进程使⽤的线程及其分配
Process Group （过程组）：进程组是⼀组特定的进程及其连接，允许组合其他组件创建新组件
 
1.3, NIFI 构架  
NiFi 在主机操作系统上的 JVM 内执⾏。 JVM 上的 NiFi 的主要组件如下：
1.3.1, ⽹络服务器

<!-- page 2 -->
Web 服务器的⽬的是托管 NiFi 的基于 HTTP 的命令和控制 API 。
1.3.2, 流控制器  
流控制器是操作的⼤脑。它提供⽤于扩展程序运⾏的线程，并管理扩展程序接收资源以执⾏的时间表。
1.3.3, 扩展  
有各种类型的 NiFi 扩展在其他⽂档中描述。这⾥的关键是扩展在 JVM 中运⾏和执⾏。
1.3.4, FlowFile 存储库  
FlowFile 存储库是 NiFi 跟踪⽬前在流程中活动的给定 FlowFile 的知识状态。存储库
实现是可插拔的。默认⽅法是位于指定磁盘分区上的持久写⼊前端⽇志。
1.3.5, 内容存储库  
Content Repository 是给定 FlowFile 的实际内容字节。存储库的实现是可插拔的。默认⽅法是⼀个相当
简单的机制，它将数据块存储在⽂件系统中。可以指定多个⽂件系统存储位置，以便获得不同的物理分
区，以减少任何单个卷上的争⽤。
1.3.6, 源头存储库  
Provenance Repository 是存储所有来源的事件数据的地⽅。存储库构造是可插⼊的，默认实现是使⽤
⼀个或多个物理磁盘卷。在每个位置内，事件数据被索引和可搜索。
作为功能强⼤的数据处理和分发组件， sNiFi ⾃然原⽣⽀持集群部署⽅式（推荐部署⽅式）。 NiFi 集群部
署模式如下图：
集群模式下， NiFi 集群中的每个节点对数据执⾏相同的任务，但是每个节点都在不同的数据集上进⾏操
作。和⼤部分⼤数据组件⼀样， NiFi 集群使⽤ Apache ZooKeeper 提供协调服务。  Apache ZooKeeper
选择⼀个 NiFi 节点作为集群协调器，故障转移由 ZooKeeper ⾃动处理。  所有集群节点向集群协调器报告
⼼跳和状态信息。集群协调器负责节点的断开和连接。  此外， ZooKeeper 会为每个集群选举⼀个节点
作为集群主节点。  作为 DataFlow 管理器，您可以通过任何节点的⽤⼾界⾯（ UI ）与 NiFi 集群进⾏交
互。您所做的任何更改都会同步到集群中的所有节点，从⽽允许多个⼊⼝点。
 
2, NIFI 环境搭建 - 单机  
2.1, 运⾏环境准备。

<!-- page 3 -->
Apache niﬁ 即可运⾏在 Windows 平台，也可运⾏在 Linux 平台，需要安装 jdk （ niﬁ 1.x 以上需要 jdk8 以
上， 0.x 需 jdk7 以上）和 maven （⾄少 3.1.0 以上版本）。
2.2, 下载  
NIFI 下载地址：http://niﬁ.apache.org/download.html
下载当前版本的 NiFi ⼆进制⼯程，⽬前最新的版本为 1.9.2 。
按需下载 !
 
2.3, 修改默认端⼝  
同⼀系统启动多个服务时 , 避免端⼝冲突 , 建议修改默认端⼝
配置⽂件位置 : niﬁ-1.9.2/conf/niﬁ.properties
 
2.4, 启动  
以 linux 版本为例 , 解压并启动
# ⽂件第 137 ⾏是 nifi 端⼝配置 , 这⾥修改为 : 58080
......
134 # web properties #
135 nifi.web.war.directory=./lib
136 nifi.web.http.host=
137 nifi.web.http.port=58080  # 修改默认端⼝为: 58080
138 nifi.web.http.network.interface.default=
139 nifi.web.https.host=
140 nifi.web.https.port=
141 nifi.web.https.network.interface.default=
142 nifi.web.jetty.working.directory=./work/jetty
......
## 下载⽬录为 /opt
# 进⼊⽬录
cd /opt
# 解压⽂件

<!-- page 4 -->
执⾏启动命令后 , 需要等待  1 - 5 分钟  ( 根据电脑配置  ), 可以查看⽇志 , 看到端⼝ ( 这⾥配置的是 58080 ) 说
明启动成功 , 查看⽇志操作如下 :
启动成功后访问  : ip:58080/niﬁ 进⾏查看 , 访问界⾯如下 :
 
tar zxvf nifi-1.9.2-bin.tar.gz
# 得到⽬录 : nifi-1.9.2, 进⼊ bin ⽬录并查看⽬录内容
cd nifi-1.9.2/bin && ls
# 结果 : dump-nifi.bat  nifi-env.bat  nifi-env.sh  nifi.sh  run-nifi.bat  status-
nifi.bat
# 使⽤  nifi.sh 进⾏单机运⾏操作 , 常⽤参数如下 :
# ./nifi.sh --help
# Usage nifi {start|stop|run|restart|status|dump|install}
## 以下是常⽤命令
# 启动：
./nifi.sh start
# 关闭：
./nifi.sh stop
# 重启：
./nifi.sh restart
# 状态：
./nifi.sh status
# ⽇志⽬录 : nifi-1.9.2/logs
cd logs && tail -f nifi-app.log
# 看到如下⽇志说明启动成功 ( ip 根据你电脑的 ip ⽽定 , 可能不⼀样  )

<!-- page 5 -->
2.5, 常⽤组件  
2.5.1, 处理器 ( processor )  
niﬁ 内部提供了各个处理器模块 , 根据不同的需求 , 选择不同的处理器进⾏拼装 , 从⽽组成⼀个完整的流处
理组 .
 
2.5.2, 数据流传⼊点（ input-port ）  
虽说是数据流输⼊点，但是并不是整体数据流的起点。它是作为组与组之间的数据流连接的传⼊点与输
出点。
 
2.5.3, 数据流输出点（ output-port ）  
同理上⾯的输⼊点。它是作为组与组之间的数据流连接的传⼊点与输出点。
2.5.4, 组 (process-group)  
组相当于系统中的⽂件夹，作⽤就是使数据流的各个部分看起来更⼯整，思路更清晰，不⾄于从头到尾
⼀条线阅读起来⼗分不⽅便。
2.5.5, 远程组 (remote process-group)  
添加远程的组。
2.5.6, 聚合 (funnel)

<!-- page 6 -->
⽤于将来⾃多个 Connections 的数据合并到⼀个 Connection 中。
2.5.7 模版 (template)  
可以将若⼲组件组合在⼀起以形成更⼤的组，从该组创建数据流模版。这些模板也可以导出为 XML 并导
⼊到另⼀个 NiFi 实例中，从⽽可以共享这些组。
2.5.8, 便签（ label ）  
可放置在画布空⽩处，写上备注信息。
2.6, 导航 (Navigate)  
Navigate 是对⼯作区进⾏预览，点击放⼤缩⼩可调整视野，蓝框区域就是⼯作区当前的界⾯，可⽤⿏标
在这部分进⾏移动从⽽调整⼯作区的视野。
2.7, 操作区 (Operate)

<!-- page 7 -->
PS: 右键⼯作区空⽩处也可以弹出操作菜单
 
2.7.1, 配置 (Conﬁguration)  
 根据在当前⼯作区选中的组件 , 进⾏属性配置 , 可配置所有组件或组
2.7.2, 启⽤ (enable)  
 启⽤组件 , 不能操作组
2.7.3, 禁⽤ (disable)  
 禁⽤组件 , 不能操作组
2.7.4, 开始 (start)  
 启动选择的组件或组 , 不选择启动所有
2.7.5, 停⽌ (stop)  
 停⽌选择的组件或组 , 不选择停⽌所有
2.7.6, 创建模版 (create template)  
 根据选择的组件或组创建模版
2.7.7, 上传模版 (upload template)  
 上传已保存的模版
 
3, NIFI 处理器  
3.1, 处理器介绍  
3.1.1, 查看处理器  
1, 选择处理器组件

<!-- page 8 -->
2, 弹出窗⼝显⽰的就是所有处理器
 
3.1.2, 常⽤处理器  - 整理  
ExecuteScript : 执⾏脚本处理器 , ⽀持 : clojure, ecmascript, groovy, lua, python, ruby
QueryDatabaseTable : 数据库查询处理器 , ⽀持 : mysql
ConvertAvroToJSON : avro 数据格式转换为  json
SplitJson : 将 JSON ⽂件拆分为多个单独的 FlowFiles, ⽤于由 JsonPath 表达式指定的数组元素。

<!-- page 9 -->
EvaluateJsonPath : 根据 FlowFile 的内容评估⼀个或多个 JsonPath 表达式。这些表达式的结果将分配
给 FlowFile 属性，或者写⼊ FlowFile 本⾝的内容，具体取决于处理器的配置。
ReplaceText : ⽂本组装与替换 , ⽀持正则表达式
PutHDFS : 将 FlowFile 数据写⼊ Hadoop 分布式⽂件系统（ HDFS ）
PutHiveQL : 执⾏ hive ddl/dml 命令 , 如 : insert, update
PublishKafka_2_0 : 根据配置将消息发送到 kafka topic
SelectHiveQL : 执⾏ hive select 语句并获取结果
PutSQL : 执⾏ SQL 的 insert 或 update 命令
GetFile : 从⽬录中的⽂件创建 FlowFiles 。
PutFile : 将 FlowFile 数据写⼊⽂件
GetHDFS : 从 Hadoop 分布式⽂件系统获取⽂件
CaptureChangeMySQL : 从 MySQL 数据库中检索更改数据捕获（ CDC ）事件。 CDC 事件包括
INSERT ， UPDATE ， DELETE 操作。事件作为单个流⽂件输出，这些⽂件按操作发⽣的时间排序。
ExecuteStreamCommand : ⼀般⽤于执⾏ sh 脚本
更多功能等待去发掘
 
3.2, 配置处理器  
3.2.1, 添加⼀个处理器  
以 GetFile 为例 :

<!-- page 10 -->
3.2.2, 配置处理器配置项说明  
右键 () 要配置的处理器 , 会弹出配置项菜单 , 如下图 :
选项说明 :
Conﬁgure（配置）：此选项允许⽤⼾建⽴或更改处理器的配置。
Start（启动或停⽌）：此选项允许⽤⼾启动或停⽌处理器 ; 该选项可以是 Start 或 Stop ，具体取决
于处理器的当前状态。
Disable（启⽤或禁⽤）：此选项允许⽤⼾启⽤或启⽤处理器 ; 该选项将为 “ 启⽤ ” 或 “ 禁⽤ ” ，具体取
决于处理器的当前状态。
View data provenance（查看数据来源）：此选项显⽰ NiFi 数据来源表，其中包含有关通过该处
理器路由 FlowFiles 的数据来源事件的信息。
View status history（查看状态历史记录）：此选项打开处理器统计信息随时间的图形表⽰。
View usage（查看⽤法）：此选项将⽤⼾带到处理器的使⽤⽂档。
View connection →  Upstream（查看连接 → 上游）：此选项允许⽤⼾查看和 “ 跳转 ” ⼊处理器的
上游连接。当处理器连接进出其他进程组时，这尤其有⽤。
View connection →  Downstream（查看连接 → 下游）：此选项允许⽤⼾查看和 “ 跳转 ” 到处理器
外的下游连接。当处理器连接进出其他进程组时，这尤其有⽤。
Centere in view（视图中⼼）：此选项将画布的视图置于给定的处理器上。
Change color（更改颜⾊）：此选项允许⽤⼾更改处理器的颜⾊，这可以使⼤流量的可视化管理
更容易。
Group （添加到组）：把当前处理器添加到组
Create template（创建模板）：此选项允许⽤⼾从所选处理器创建模板。
Copy（复制）：此选项将所选处理器的副本放在剪贴板上，以便可以通过右键单击⼯作区并选择
“ 粘贴 ” 将其粘贴到⼯作区上的其他位置。复制粘贴操作也可以使⽤按键 Ctrl-C 和 Ctrl-V 完成。
Delete（删除）：此选项允许从画布中删除处理器。

<!-- page 11 -->
3.2.3, 配置处理器  
以 GetFile 为例
⽅式 1: 右键选择  -- > Conﬁgure
⽅式 2: ⿏标左键双击处理器
配置窗⼝如下图 :
配置分为 4 个部分 : SETTING, SCHEDULING, PROPERTIES, COMMENTS, 接下来⼀⼀介绍
3.2.3.1, SETTING ( 设置  )

<!-- page 12 -->
3.2.3.2, SCHEDULING ( 任务调度  )  
 
PS: 不同的处理器 , 可能略有不同
3.2.3.3, PROPERTIES ( 属性  )

<!-- page 13 -->
PS: 不同处理属性不同
3.2.3.4, COMMENTS ( 注释  )  
 
修改完成 , 记得保存修改 , 点击右下⻆的  "APPLY" 保存修改

<!-- page 14 -->
4, 应⽤场景  
4.1, 执⾏脚本产⽣的数据保存到 hdfs 上  
⼀般⽤于⽣成测试数据 , 流程 :
ExecuteScript --> Connection --> PutHDFS
开始之前 : 新建组  "demo" 并进⼊组, 在 demo 中进⾏以下操作
4.1.1, 创建 ExecuteScript 处理器  
1, ⼯作区添加⼀个 ExecuteScript
 
 
2, ROPERTIES 标签⻚  Script Engine选择脚本语⾔为 : python, ⽤于⽣成模拟数据 , 操作如下 :

<!-- page 15 -->
ROPERTIES 标签⻚除了  Script Engine（脚本引擎）  还有其他  3 个参数以下是详细说明
这⾥以 Script Body 为例，  编写好的数据⽣成脚本如下 :
ps: ⽣成的数据很简单 , 3 个值 , 左到右分别是 : rid, ip_str, datestamp, ⼀次 1 万条
# 脚本⽂件，如果代码写在脚本内容，此项可空
Script File
# 脚本内容，如果引⼊了脚本⽂件，此项可空
Script Body
# 引⼊的模块⽬录，  不引⼊可留空
Module Directory
import datetime
import random
from org.apache.nifi.processor.io import StreamCallback
def datestamp():
    now_info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 60))
    time_info = now_info - delta
    time_str = time_info.strftime('%Y-%m-%d %H:%M:%S')
    return time_str
class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
        for i in xrange(1, 10000):

<!-- page 16 -->
4.1.2, 创建 PutHDFS 处理器  
把⽣成的数据存放到 hdfs 上，  新建 PutHDFS 的 Processor ，步骤如下：
PutHDFS 配置如下：
            ip_str = '.'.join(str(random.randint(1, 255)) for i in xrange(4))
            rid = random.randint(10000, 99999)
            outputStream.write(bytearray(str(rid) + '\t' + ip_str + '\t' + 
datestamp() + '\n'[::1].encode('utf-8')))
flowFile = session.create()
flowFile = session.write(flowFile, PyStreamCallback())
session.transfer(flowFile, REL_SUCCESS)

<!-- page 17 -->
niﬁ 表达式了解即可参考 : https://niﬁ.apache.org/docs/niﬁ-docs/html/expression-language-guide.ht
ml
 
4.1.3, 建⽴连接  
数据来源和数据⽬的地配置好后接下来把它们关联起来了，拖动 ExecuteScript Processor 上的箭头到
PutHDFS Processor 即可 , 操作如下：

<!-- page 18 -->
PS: Automatically Terminate Relationships （⾃动终⽌关系）：为了使处理器被视为有效且能够运
⾏，处理器定义的每个关系必须连接到下游组件或⾃动终⽌。  ExecuteScript 连接到 PUTHDSF 后警告
消失 , 因为有了数据流向, 但  PUTHDFS 的警告还没消息 , 因为没有数据流向 , 这⾥没有后续操作 , 选择了
⾃动终⽌
 
4.1.4, 测试  
PS: 开始测试前 , 要确认 hdfs 是启动的
右键  组 "demo" ⼯作区的空⽩ , 点击操作菜单的 start( 开始 ) 选项 , 操作如下 :
 
整个流程下来⾮常简单 , 更多案例在课程中体现  !
5, NIFI 处理器开发  
5.1, 开始前奏  
Niﬁ 已经提供了很多可⽤的 Processor 资源，但是某些时候你依然需要去开发属于你⾃⼰的 Processor ，
例如从某些特殊的数据库中提取数据、提取不常⻅的⽂件格式，或者其他特殊情况。
官⽅开发⼿册 : https://niﬁ.apache.org/docs/niﬁ-docs/html/developer-guide.html
 
5.2, 基于 maven 创建项⽬

<!-- page 19 -->
5.2.1, 使⽤命令创建项⽬  
PS: 需要配置 maven 的 path, 保证  mvn 命令可⽤
指定⽬录执⾏ , 项⽬就创建在该⽬录下 , 创建命令如下 ,:
命令执⾏后 , 需要根据提⽰ , 输⼊项⽬相关信息 , 操作如下 :
 
5.2.2, 项⽬导⼊ idea  
idea 导⼊ maven 项⽬直接使⽤  open 的⽅式就⾏ , 操作如下 :
 
mvn archetype:generate -DarchetypeGroupId=org.apache.nifi -
DarchetypeArtifactId=nifi-processor-bundle-archetype -DarchetypeVersion=1.9.2 -
DnifiVersion=1.9.2

<!-- page 20 -->
5.3 ⾃定义处理器代码  
由于官⽅提交的处理器 , 并不能满⾜课程需要 , 这⾥开发了 3 个⾃⼰定义处理器 , 功能也都很简单 , 介绍如
下 :
1. Json-To-Hive : Json 数据⼀步存 hive
2. MySQL-BinLog-To-Hive : 监听 msyql binlog ⼀步存 hive
3. Wait-For-Next-Group : 根据数据流向及设置的超时时间单纯的等待
在提供资料⽬录中可以找到 , ⽬录结构如下 :
 
5.3.1 打包并安装到 NiFi  
以 Json-To-Hive.zip 为例 , 解压源码在源码根⽬录 , 执⾏打包命令 : mvn clean package -DskipTests , 等待
运⾏结束即可 , 然后在 Json-To-Hive/niﬁ-Json-To-Hive-nar/target ⽬录中找到打包好的⽂件 , 如下图所⽰ :
将 Json-To-Hive.nar 拷⻉到 NiFi 的 lib 下。
重启 NiFi 。
 
5.2.3 使⽤⾃定义处理器  
添加处理器时可以通过修改 Source 快速找到 , 课程中⾃定义处理器包名为 : cn.itcast.bigdata, 如下图所
⽰ :
......
└── 授课资料
    └── 第 2 章 - 数据仓库与 ETL
        ├── code
        │   ├── Json-To-Hive.zip
        │   ├── MySQL-BinLog-To-Hive.zip
        │   └── Wait-For-Next-Group.zip
        .....

<!-- page 21 -->
5.3.2 ⾃定义处理器源码说明  
5.3.2.1 Json-To-Hive  
处理上⼀处理器传来的 json 数据 , ⼀般是  ConvertAvroToJSON 处理器传来的数据 , 转为 Hive ⽀持的⽂
件格式 , 使⽤ insert 保存到 hive 中
核⼼转换代码如下 :
@Override
    public void onTrigger(ProcessContext context, ProcessSession session) {
        // 获取队列中数据个数
        int queueSize = session.getQueueSize().getObjectCount();
        // 获取并处理队列中的所有数据
        List<FlowFile> flowFiles = 
session.get(session.getQueueSize().getObjectCount());
        // 结果集接收数据 , 在循环外统⼀处理
        List<String> responseList = new ArrayList<>();
        // 获取字段对应关系
        String fieldsCorrespond = 
context.getProperty(FIELDS_CORRESPOND).getValue();
        // 获取分割符
        String splitter = context.getProperty(SPLITTER).getValue();
        // hive 表名
        String tableName = context.getProperty(TABLE_NAME).getValue();
        // 获取 hdfs 协议地址
        String hdfsUrl = context.getProperty(HDFS_URL).getValue();
        // 临时⽂件路径 , ⽀持表达式
        String tempFilePath = 
context.getProperty(TMP_FILE_PATH).evaluateAttributeExpressions().getValue();
        // 是否全量更新
        Boolean isItFull = context.getProperty(IS_IT_FULL).asBoolean();
        // 临时表名
        String tmpTableName = context.getProperty(TMP_TABLE_NAME).getValue();
        // 分区格式字段及⽅式
        String partitionedFormat = 
context.getProperty(PARTITIONED_FORMAT).evaluateAttributeExpressions().getValue(
);

<!-- page 22 -->
5.3.2.2 MySQL-BinLog-To-Hive  
这个处理器并不是直接去监控 MySQL 的 BinLog 数据 , ⽽是处理  RouteOnAttribute 处理器传来的数据 ,
这⾥监控 MySQL 使⽤的是CaptureChangeMySQL处理器 , 它把获取的数据交给RouteOnAttribute做
过虑 , MySQL-BinLog-To-Hive 是处理过虑后的数据 , 直接保存到 hive 中 , 核⼼代码如下 :
        // 转换分区映射
        Map<String, String> correspond = 
conversionFieldsCorrespond(fieldsCorrespond);
        flowFiles.forEach(flowFile -> {
            session.read(flowFile, in -> {
                String json = IOUtils.toString(in, "UTF-8");
                if (json != null && !json.isEmpty()) {
                    // 临时⽂件存放位置
                    FSDataOutputStream os = getFSOutputStream(hdfsUrl, 
tempFilePath);
                    // 处理  ConvertAvroToJSON
                    JSONObject.parseArray(json).forEach(obj -> {
                        log.info(" 当前 json: {}", obj.toString());
                        log.info(" 当前字段 : " + flowFiles);
                        JSONObject jsonObject = 
JSONObject.parseObject(obj.toString());
                        try {
                            StringBuffer buffer = new StringBuffer("");
                            for (String key : fieldList) {
                               
 buffer.append(jsonObject.getString(correspond.get(key))).append(splitter);
                            }
                            String result = buffer.substring(0, buffer.length() 
- splitter.length());
                            log.info(" 当前 json 处理结果 : " + result);
                            os.write((result + "\n").getBytes());
                            os.flush();
                        } catch (IOException e) {
                            transformException(e);
                            e.printStackTrace();
                        }
                    });
                    // 关闭⽂件
                    closeOs(os);
                }
            });
            // session 中删除 , 不然新的 FlowFile ⽆法提交
            session.remove(flowFile);
        });
    @Override
    public void onTrigger(ProcessContext context, ProcessSession session) {
        // 获取队列中数据个数
        int queueSize = session.getQueueSize().getObjectCount();
        log.info(" 队列中数据个数 : {}", queueSize);
        if (queueSize == 0) {
            return;
        }

<!-- page 23 -->
// 获取并处理队列中的所有数据
        List<FlowFile> flowFiles = 
session.get(session.getQueueSize().getObjectCount());
        log.info(" 取出数据个数为 : {}", queueSize);
        // 结果集接收数据 , 在循环外统⼀处理
        List<String> responseList = new ArrayList<>();
        List<String> unprocessedResponseList = new ArrayList<>();
        // 获取 mysql 数据库及表名
        String dbTable = context.getProperty(MYSQL_DB_TABLE).getValue();
        // 获取  hi 与  mysql 对应规则
        String fieldsCorrespond = 
context.getProperty(FIELDS_CORRESPOND).getValue();
        // 把对应关系转换为 map
        Map<String, String> correspondMap = 
conversionFieldsCorrespond(fieldsCorrespond);
        // hive 表名
        String tableName = context.getProperty(HIVE_TABLE_NAME).getValue();
        // hive 与  mysql 主键  对应关系 , hive 在前 mysql 在后
        String[] primaryKey = 
context.getProperty(PRIMARY_KEY).getValue().split(":");
        //  ⽣成 insert 语句  和  update 格式语句
        // 格式 : INSERT INTO az (id, user_id, act_user_name, repo_name, content, 
created_unix) VALUES (null, 1, 'xufan', 'wanxinp2p', '11', 1556507667),(null, 2, 
'xufan', 'wanxinp2p', '11', 1556507667);
        // UPDATE az SET user_id=3, act_user_name='xufan', 
repo_name='wanxinp2p', content='11', created_unix=1556507667 WHERE id=5;
        // insert 相关
        final String[] insert = {"INSERT INTO " + tableName};
        StringBuffer insertBuffer = new StringBuffer("");
        final int[] insertCount = {0};
        // update 相关
        String update = "UPDATE " + tableName + " SET ";
        flowFiles.forEach(flowFile -> {
            session.read(flowFile, in -> {
                String json = IOUtils.toString(in, "UTF-8");
                if (json != null && !json.isEmpty()) {
                    // 处理 mysql bin log, RouteOnAttribute 传过来的数据
                    JSONObject jsonObject = JSONObject.parseObject(json);
                    // 判断是否是要处理的数据库及表
                    String dt = jsonObject.getString("database") + "." + 
jsonObject.getString("table_name");
                    if (!dbTable.equals(dt)) {
                        // 不匹配直接结束当次处理
                        return;
                    }
                    String type = jsonObject.getString("type");
                    if (Types.INSERT.getType().equals(type)) {
                        StringBuffer namesBuffer = new StringBuffer("");
                        StringBuffer valuesBuffer = new StringBuffer("");
                        namesBuffer.append(" (");
                        valuesBuffer.append(" (");
                        jsonObject.getJSONArray("columns").forEach(obj -> {
                            // 解析数据

<!-- page 24 -->
JSONObject field = 
JSONObject.parseObject(obj.toString());
                            // 获取字段名
                            String name = field.getString("name");
                            // 判断此字段是否需要存⼊ hive
                            if (correspondMap.containsKey(name)) {
                                // 第⼀次进来处理  需要处理字段
                                if (insertCount[0] == 0) {
                                    String key = correspondMap.get(name);
                                    namesBuffer.append(key).append(",");
                                }
                                String value = field.getString("value");
                                // 增加 UTC 转北京时间时间戳
                                if (null != value && value.matches("^\\w{3} 
\\w{3} \\d{2} \\d{2}:\\d{2}:\\d{2} UTC \\d{4}$")) {
                                    value = utcToLocal(value) + "";
                                }
                                valuesBuffer.append("'" + value + 
"'").append(",");
                            }
                        });
                        // 拼接 names
                        if (insertCount[0] == 0) {
                            String names = namesBuffer.substring(0, 
namesBuffer.length() - 1) + ") VALUES ";
                            insert[0] = insert[0] + names;
                            insertCount[0] = 1;
                        }
                        String values = valuesBuffer.substring(0, 
valuesBuffer.length() - 1) + ") ,";
                        insertBuffer.append(values);
                    } else if (Types.UPDATE.getType().equals(type)) {
                        // 处理 update, ⽣成 update 语句
                        StringBuffer valBuffer = new StringBuffer("");
                        AtomicReference<String> id = new AtomicReference<>("");
                        jsonObject.getJSONArray("columns").forEach(obj -> {
                            // 解析数据
                            JSONObject field = 
JSONObject.parseObject(obj.toString());
                            // 获取字段名
                            String name = field.getString("name");
                            // 获取 value
                            String value = field.getString("value");
                            // 增加 UTC 转北京时间时间戳
                            if (null != value && value.matches("^\\w{3} \\w{3} 
\\d{2} \\d{2}:\\d{2}:\\d{2} UTC \\d{4}$")) {
                                value = utcToLocal(value) + "";
                            }
                            // 找到主键
                            if (name.equals(primaryKey[1])) {
                                id.set(value);
                            }
                            // 判断此字段是否需要存⼊ hive

<!-- page 25 -->
if (correspondMap.containsKey(name)) {
                                valBuffer.append(correspondMap.get(name) + "='" 
+ value + "',");
                            }
                        });
                        responseList.add(update + valBuffer.substring(0, 
valBuffer.length() - 1) + " WHERE " + primaryKey[0] + "='" + id.get() + "';\n");
                    } else {
                        // 其他情况不处理的类型 , 写⽇志
                        unprocessedResponseList.add(json + "\n");
                    }
                }
            });
            // session 中删除 , 不然新的 FlowFile ⽆法提交
            session.remove(flowFile);
        });
        // insert 最终拼装放⼊集合
        if (insertBuffer.length() > 0) {
            // 拼装
            insert[0] = insert[0] + insertBuffer.substring(0, 
insertBuffer.length() - 1) + ";\n";
            responseList.add(insert[0]);
        }
        // 有结果
        if (responseList.size() > 0) {
            // 正常 ( 成功 ) 流向
            dealWithFlowFile(session, responseList, SUCCESS);
        }
        // 有异常 , 写出异常数据
        if (HAS_EXCEPTION) {
            // 异常  流向
            dealWithFlowFile(session, EXCEPTION_MSG, EXCEPTION);
        }
        // 处理失败的情况
        if (queueSize > 0 && responseList.size() == 0) {
            // 创建⼀个新的 FlowFile ⽤于数据  失败  流向
            FlowFile failureFlowFile = session.create();
            // 处理异常数据
            failureFlowFile = session.write(failureFlowFile, out -> {
                out.write(" 队列中获取到数据 , 但未得到结果集 , 请检查
exceptionFlowFile\n".getBytes("UTF-8"));
            });
            // 有异常 , 数据流向 failure
            session.transfer(failureFlowFile, FAILURE);
        }
        // 未处理的类型或者数据
        if (unprocessedResponseList.size() > 0) {
            // 创建⼀个新的 FlowFile ⽤于数据  未处理  流向
            dealWithFlowFile(session, unprocessedResponseList, UNPROCESSED);
        }
    }

<!-- page 26 -->
5.3.2.3 Wait-For-Next-Group  
NiFi 处理器组之间数据通信使⽤的是 Output Port( 流出  ), Input Port( 流⼊  ), 但这两个处理器没办法保证
组与组之前是串⾏执⾏ , 这⾥使⽤⾃定义处理器 ( Wait-For-Next-Group ) 来解决这个问题 , Wait-For-
Next-Group 的功能⾮常纯粹 , 根据  判断上⼀处理器是否有流传过来  加  超时时间 来控制下⼀个处理器组
何时执⾏ , 数据流向还是基于  Output Port( 流出  ), Input Port( 流⼊  )
 
核⼼代码如下 :
    @Override
    public void onTrigger(final ProcessContext context, final ProcessSession 
session) throws ProcessException {
        FlowFile flowFile = session.get();
        if (null == flowFile) {
            return;
        }
        session.read(flowFile, in -> {
            String str = IOUtils.toString(in, "UTF-8");
            // 丢弃
            str = null;
        });
        // 获取 id
        String waitingTimeId = context.getProperty(WAITING_TIME_ID).getValue();
        // 获取等待时间
        Integer waitingTime = context.getProperty(WAITING_TIME).asInteger();
        AtomicDistributedMapCacheClient cache = 
context.getProperty(DISTRIBUTED_CACHE_SERVICE).asControllerService(AtomicDistrib
utedMapCacheClient.class);
        Boolean flag = false;
        // 获取存在缓存中的实体 , 如果 null, 说明组刚启动 , 还没有 flowFile 进⼊
        try {
            String waiting = flowFile.getAttribute("WAITING");
            // 判断是否为 wait 流
            if (StringUtils.isBlank(waiting)) {
                // 不是的话 , 转换为 wait 流
                session.putAttribute(flowFile, "WAITING", "true");
                putEntry(cache, waitingTimeId, waitingTime);
            } else {
                // wait 流中获取等待时间
                long currentTimeMillis = System.currentTimeMillis();
                WaitEntry entry = getEntry(cache, waitingTimeId);
                if (null == entry) {
                    entry = putEntry(cache, waitingTimeId, waitingTime);
                }
                Long milliSecond = entry.getMilliSecond();
                Integer wt = entry.getWaitingTime();
                // 判断是否等待超时
                if (currentTimeMillis > (milliSecond + wt * 1000)) {

<!-- page 27 -->
flag = true;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
        }
        if (flag) {
            // 等待结束数据流向
            flowFile = session.write(flowFile, out -> {
                try {
                    out.write("success".getBytes("UTF-8"));
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            session.transfer(flowFile, SUCCESS);
            // 清空 wait 队列
           
 session.remove(session.get(session.getQueueSize().getObjectCount()));
            try {
                cache.remove(waitingTimeId, stringSerializer);
            } catch (IOException e) {
            }
        } else {
            // 等待数据流向
            flowFile = session.write(flowFile, out -> {
                try {
                    out.write("wait".getBytes("UTF-8"));
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            session.transfer(flowFile, WAIT);
        }
    }
