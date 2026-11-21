# Kafka-Connecter使用文档

- 来源：04.阶段四 大数据转型 必备课程-Hadoop3\JavaEE中级进修课资料（新版）\08.基于大数据的智慧学成项目课程\day03\资料\第2章-数据仓库与ETL\采集系统\Kafka-Connecter使用文档【海量资源尽在 666java.com】.pdf
- 页数：12
- 抽取：pypdf 文本层



<!-- page 1 -->
Kafka Connect 介绍  
本⽂⽬标是使⽤  Kafka Connect 把 kafka 中的消息持久化到 hdfs 中 , 以下是对 Kafka Connect 简单介绍 :
Kafka Connect 是⼀个⽤于将数据流输⼊和输出 Kafka 的框架。以下是 Connect 的主要概念
以下是详细说明
Connectors:
Tasks:
Workers ：
Converters ：
Transforms:
Connectors ：通过管理 task 来协调数据流的⾼级抽象
Tasks ：如何将数据复制到 Kafka 或从 Kafka 复制数据的实现
Workers ：执⾏ Connector 和 Task 的运⾏进程
Converters ：  ⽤于在 Connect 和外部系统发送或接收数据之间转换数据的代码
Transforms ：更改由连接器⽣成或发送到连接器的每个消息的简单逻辑
 Kafka Connect 中的 connector 定义了数据应该从哪⾥复制到哪⾥。 connector 实例是⼀种逻辑作业，负
责管理 Kafka 与另⼀个系统之间的数据复制。在⾃定义 Connect 时需要编写代码 , 并指定 Task
 Task 是 Connect 中数据处理的⻆⾊ , 处理 topic 数据的流向 , 根据实际需求进⾏处理 , Task 是 Connect 指
定的 , 与 Connect ⼀⼀对应。在⾃定义 Connect 时需要编写 Task 的代码。
是 Connect ⼯作的⽅式，  Kafka 提供了两种模式 : Standalone 和  Distributed 。
Standalone ：  单机模式，⽤单⼀进程负责执⾏所有 connector 和 task 。
Distributed ：  集群模式，在分布式模式下，你可以使⽤相同的组启动许多 worker 进程。它们⾃动协调以
跨所有可⽤的 worker 调度 connector 和 task 的执⾏。如果你添加⼀个 worker 、关闭⼀个 worker 或某个
worker 意外失败，那么其余的 worker 将检测到这⼀点，并⾃动协调，在可⽤的 worker 集重新分发
connector 和 task 。
启动时选择两者之⼀，  ⽆需编写代码  ！
kafka 提供的有 REST API, 可直接提交任务⾮常⽅便
在向 Kafka 写⼊或从 Kafka 读取数据时， Converter 是使 Kafka Connect ⽀持特定数据格式所必需的。
task 使⽤转换器将数据格式从字节更改为连接内部数据格式，反之亦然，  Kafka 默认提供以下
converters ：
AvroConverter ：与 Schema Registry ⼀起使⽤
JsonConverter ：适合结构数据
StringConverter ：简单的字符串格式
ByteArrayConverter ：提供不进⾏转换的 “ 传递 ” 选项
Connector 可以配置转换，以便对单个消息进⾏简单且轻量的修改。这对于⼩数据的调整和事件路由⼗分⽅
便，且可以在 connector 配置中将多个转换链接在⼀起。

<!-- page 2 -->
0 环境依赖  
Kafka Connect 的依赖关系如下 :
提交 connectors <--- Kafka Connect ( Workers ) <--- Kafka <--- zookeeper
所以要先启动 zookeeper 、 kafka 和 Kafka Connect( Workers ) 才能提交 connectors
这⾥假定你已配置好 zookeeper 和 Kafka, 接下来详细说明 Kafka Connect 的启动及提交 connectors
 
1 Connector 代码及配置  
kafka 消息持久化到 hdfs 有现成的开源⽅案 : https://github.com/conﬂuentinc/kafka-connect-hdfs, 采
⽤的存储格式是 avro, 项⽬要求使⽤ txt ⽂本格式 , 所以不能使⽤现在⽅案 , 需要⼿写 Connect, 代码如下 :
1.1 代码  
项⽬名为 : kafka-to-hdfs
pom.xml
HdfsSinkConnector.jar
    <dependencies>
        <dependency>
            <groupId>org.apache.kafka</groupId>
            <artifactId>connect-api</artifactId>
            <version>2.2.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-client</artifactId>
            <version>2.6.5</version>
        </dependency>
    </dependencies>
package cn.itcast.bigdata.common.kafka_to_hdfs.hdfs;
import cn.itcast.bigdata.common.kafka_to_hdfs.config.Version;
import org.apache.kafka.common.config.ConfigDef;
import org.apache.kafka.connect.connector.Task;
import org.apache.kafka.connect.sink.SinkConnector;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
/**
 * <P>
 * ⾃定义 hdfs Connector
 * </p>

<!-- page 3 -->
*
 */
public class HdfsSinkConnector extends SinkConnector {
    public static final String HDFS_URL = "hdfs.url";
    public static final String HDFS_PATH = "hdfs.path";
    private static final ConfigDef CONFIG_DEF = new ConfigDef()
            .define(HDFS_URL, ConfigDef.Type.STRING, ConfigDef.Importance.HIGH, 
"hdfs url")
            .define(HDFS_PATH, ConfigDef.Type.STRING, ConfigDef.Importance.HIGH, 
"hdfs path");
    private String hdfsUrl;
    private String hdfsPath;
    private Map<String, String> settings;
    @Override
    public void start(Map<String, String> map) {
        settings = map;
        hdfsUrl = map.get(HDFS_URL);
        hdfsPath = map.get(HDFS_PATH);
    }
    @Override
    public Class<? extends Task> taskClass() {
        return HdfsSinkTask.class;
    }
    @Override
    public List<Map<String, String>> taskConfigs(int maxTasks) {
        List<Map<String, String>> taskConfigs = new ArrayList<>(maxTasks);
        for (int i = 0; i < maxTasks; i++) {
            taskConfigs.add(settings);
        }
        return taskConfigs;
    }
    @Override
    public void stop() {
        // TODO: what's necessary to stop the connector
    }
    @Override
    public ConfigDef config() {
        return CONFIG_DEF;
    }
    @Override
    public String version() {
        return Version.getVersion();
    }
}

<!-- page 4 -->
HdfsSinkTask.java
package cn.itcast.bigdata.common.kafka_to_hdfs.hdfs;
import cn.itcast.bigdata.common.kafka_to_hdfs.config.Version;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.kafka.connect.sink.SinkRecord;
import org.apache.kafka.connect.sink.SinkTask;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Collection;
import java.util.Date;
import java.util.Map;
import java.util.UUID;
/**
 * <P>
 * ⾃定义任务处理
 * </p>
 *
 */
public class HdfsSinkTask extends SinkTask {
    public static final String HDFS_URL = "hdfs.url";
    public static final String HDFS_PATH = "hdfs.path";
    public static String hdfsUrl;
    public static String hdfsPath;
    public static String expression;
    private static Configuration conf;
    private static FSDataOutputStream os;
    private static FileSystem hdfs;
    public HdfsSinkTask() {
    }
    @Override
    public String version() {
        return Version.getVersion();
    }
    @Override
    public void start(Map<String, String> map) {
        hdfsUrl = map.get(HDFS_URL);
        hdfsPath = map.get(HDFS_PATH);
        expression = map.get("expression");
        conf = new Configuration();
        conf.set("fs.defaultFS", hdfsUrl);
        // 这两个是与 hdfs append 相关的设置
        conf.setBoolean("dfs.support.append", true);

<!-- page 5 -->
conf.set("dfs.client.block.write.replace-datanode-on-failure.policy", 
"NEVER");
        try {
            hdfs = FileSystem.get(conf);
            Path path = new Path(hdfsPath + getFilePath(hdfsPath, expression));
            if (hdfs.exists(path)) {
                os = hdfs.append(path);
            } else {
                os = hdfs.create(path);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void put(Collection<SinkRecord> collection) {
        for (SinkRecord record : collection) {
            try {
                System.out.println("write info------------------------" + 
record.value().toString() + "-----------------");
                System.out.println("FSDataOutputStream="+os);
                os.write((record.value().toString()).getBytes("UTF-8"));
                os.hsync();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    @Override
    public void stop() {
        try {
            os.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    /**
     * ⽣成⽂件路径
     * @param hdfsPath
     * @param expression
     * @return
     */
    public String getFilePath(String hdfsPath, String expression) {
        if (null != expression && expression.startsWith("yyyy")) {
            if (hdfsPath.endsWith("/")) {
                return new SimpleDateFormat(expression).format(new Date()) + "/" 
+ UUID.randomUUID().toString().replaceAll("-", "");
            }
            return "/" + new SimpleDateFormat(expression).format(new Date()) + 
"/" + UUID.randomUUID().toString().replaceAll("-", "");
        } else {
            if (hdfsPath.endsWith("/")) {

<!-- page 6 -->
1.2 打包  
1.2.1 打 jar 包  
开发⼯具 Maven 视图 , 点击 package, 即可打包
                return (System.currentTimeMillis() / 1000)+ "." + 
UUID.randomUUID().toString().replaceAll("-", "");
            }
            return "/" + (System.currentTimeMillis() / 1000) + "." + 
UUID.randomUUID().toString().replaceAll("-", "");
        }
    }
}
package cn.itcast.bigdata.common.kafka_to_hdfs.config;
import java.util.Properties;
/**
 * <P>
 * TODO
 * </p>
 *
 */
public class Version {
    private static String version = "unknown";
    static {
        try {
            Properties props = new Properties();
            props.load(Version.class.getResourceAsStream("/kafka-to-
hdfs.properties"));
            version = props.getProperty("version", version).trim();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static String getVersion() {
        return version;
    }
}

<!-- page 7 -->
⽣成的 kafka-to-hdfs.jar, 在项⽬ target ⽬录
 
1.2.2 打包依赖  
在项⽬根⽬录执⾏命令 :
相关依赖会复制到项⽬⽬录下的 lib ⽬录中 , 如下图所⽰ :
# 把依赖的 jar copy 到 lib ⽬录 
mvn dependency:copy-dependencies -DoutputDirectory=lib

<!-- page 8 -->
重要 : 把 kafka-to-hdfs.jar 也复制到 lib ⽬录 , 以便后⾯使⽤  !
1.3 资料路径  
打包好的 kafka-to-hdfs 在资料中的路径：
2 启动 Kafka - Connector  
2.1 配置  
 
先新建⼀个 kafka-to-hdfs ⽬录 , 把 lib ⽬录复制到 kafka-to-hdfs 内 , ⽬录结构如下图 :
.
└──  授课资料
    └──  第 2 章 - 数据仓库与 ETL
        └──  code
            └──  package
            └──  kafka-to-hdfs.zip // 源码
                 └──  kafka-to-hdfs_lib.zip // 包含依赖的打包
.
`-- kafka-to-hdfs
    `-- lib
        |-- kafka-to-hdfs.jar
        |-- .....

<!-- page 9 -->
在 kafka ( 项⽬中需要上传到 kafka 容器中  ) 的安装⽬录新建  plugins ⽬录把 kafka-to-hdfs ⽬录复制进去 ,
最终⽬录结构如下图 :
 
在 conﬁg ⽬录  找到 connect-distributed.properties, 修改 4 项⽬配置 , 新增加⼀项⽬配置 , 详细修改如下 :
以上配置完成 , 接下来是启动及测试
2.2 启动  
启动命令如下 :
 
. ( kafka ⽬录  )
|-- LICENSE
|-- NOTICE
|-- bin
|-- config
|-- libs
|-- logs
|-- plugins
|   `-- kafka-to-hdfs
|       `-- lib
|           |-- kafka-to-hdfs.jar
|           |-- ......
|-- site-docs
## key.converter 与  value.converter 默认值
# key.converter=org.apache.kafka.connect.json.JsonConverter
# value.converter=org.apache.kafka.connect.json.JsonConverter
## 修改为 :
key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.storage.StringConverter
## 是否开启 json 转换
# key.converter.schemas.enable=true
# value.converter.schemas.enable=true
## 修改为 :
key.converter.schemas.enable=false
value.converter.schemas.enable=false
## 新增配置 , 指定⾃定义 Connector 的配置 , 这⾥是以插件的⽅式 , 这⾥使⽤的是绝对路径
plugin.path=/opt/kafka_2.11-2.2.0/plugins/kafka-to-hdfs
# 进⾏ kafka 安装⽬录 , 执⾏下⾯命令启动
./bin/connect-distributed.sh ./config/connect-distributed.properties
# 启动过程中没有发现报错说明启动成功 , 可以使⽤ ctrl + c 结束 , 然后后台启动 
# 后台启动⽅式
nohup $KAFKA_HOME/bin/connect-distributed.sh $KAFKA_HOME/config/connect-
distributed.properties >$KAFKA_HOME/logs/output_distributed 2>&1 &

<!-- page 10 -->
3 提交  Connector  
3.1 提交  Connector  
提交接⼝ : http://localhost:8083/connectors
请求类型 : POST
参数类型 : JSON
3.2 Connector 其他 REST API  
注意这⾥是本机测试 , ip 为 : localhost, 你测试时以你的为准
查询所有  Connector:
查询指定  Connector 状态
查询指定  Connector 配置参数
{
  "name": "visit_topic", 
  "config": {
    "connector.class": 
"cn.itcast.bigdata.common.kafka_to_hdfs.hdfs.HdfsSinkConnector", 
    "tasks.max": "1", 
    "topics": "visit_topic", 
    "hdfs.url": "hdfs://xc-online-hadoop:9000/",
    "flush.size": "100", 
    "expression":"yyyy-MM-dd", 
    "hdfs.path": "/user/hive/external/data_course/course_visit_source/", 
    "name": "visit_topic" 
  }
}
# 接⼝
http://localhost:8083/connectors
# 请求⽅试
GET
# 参数
⽆
# 接⼝
http://localhost:8083/connectors/{name}/status
# 请求⽅试
GET
# 参数  - Path Val
指定 Connector 的名字

<!-- page 11 -->
删除指定  Connector
 
4 测试  
测试⽅式 :
流程图如下 :
 
效果如下图 :
# 接⼝
http://localhost:8083/connectors/{name}/config
# 请求⽅试
GET
# 参数  - Path Val
指定 Connector 的名字
# 接⼝
http://localhost:8083/connectors/{name}
# 请求⽅试
DELETE
# 参数  - Path Val
指定 Connector 的名字
js 埋点  --> 
    数据发送到采集服务器  --> 
        采集服务器数据发送 kafka --> 
            kafka-connect 监听 topic --> 
                数据持久化到 hdfs

<!-- page 12 -->
最终 hdfs 上保存 js 埋点获取的数据，  如下图所⽰：
