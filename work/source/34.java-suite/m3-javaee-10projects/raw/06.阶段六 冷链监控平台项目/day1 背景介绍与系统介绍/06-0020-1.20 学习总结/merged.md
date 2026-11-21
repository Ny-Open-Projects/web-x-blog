# 1.20 学习总结

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day1 背景介绍与系统介绍
- 源文件：06.阶段六 冷链监控平台项目\day1 背景介绍与系统介绍\1.20 学习总结_【海量资源尽在 666java.com】.mp4
- 时长 2分30秒（音频 151s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来总结一下我们今天的学习那首先呢我们需要了解我们整个的业务背景知识这个业务背景知识包括物流行业冷链行业 冷链监控行业这三者之间呢其实是一个逐步递进的一个关系那么冷链监控行业呢它的目标是监控这种
[00:20] 仓库车队车辆上的一些温度和湿度那么对于我们的平台来讲我们用到的什么样的一个架构体系来对它进行监控这种架构体系包括我们整个系统的业务到底是个什么样子的那么我们整个系统它所处的任务和数据流程图以及我们系统用到的哪些技术这些技术是如何来部署和衔接的
[00:46] 从我们的整个应用层面来讲的话系统拆分成什么样的一些微服务而这些微服务之间是如何来使用的还有包括我们需要了解我们整个系统运行时的一些基础的中间件和组件那么本系统它用到的一个非常重要的一个点就是大数据平台的一些组件包括Apache的FlinkJade和Subset
[01:13] 那么Apache Flink Dread Superset它们在我们整个系统里边到底是做了什么样的一个角色比如说无论是说从前端的这种设备提交上来之后我们的Flink实时计算还是说实时计算的结果存储到Dread里边去通过Superset来进行查询这是我们在大数据平台里我们的大数据组件提供的一些功能
[01:37] 那么我们的应用系统啊应用的服务包括有哪一些应用服务这些应用服务的端口是什么应用服务之间的关系是什么我们需要了解那我们在第一天呢还需要了解我们整个系统它的一个数据结构这个数据结构的话包括我们的用户库包括我们的业务库还有一个定时任务的一个库定时任务库的话是我们用了Cutter的一些定时任务那最后的话我们给大家介绍了一个叫公共的
[02:08] 组建工程啊google comment公共组建工程到底包含了哪些内容这个每个内容里边包括我们的和一个比较主要的一些公共的一些类包括统一返回结果然后呢我们的这个分页的一些工具以及我们自定义的一个异常等等这一些那通过本章的学习大家能够了解这样的一些知识

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个物流行业的微服务系统的技术架构与部署方案，涵盖业务背景、技术选型、系统拆分、环境搭建与代码实现。

2) 按时间顺序列出每张画面的要点：
画面1：业务背景，介绍物流行业实体流动过程，评价物流体系的五个主要因素（品质、数量、成本、效率、安全）。
画面2：任务流程图（2.2）与数据流程图（2.3），展示从物流仓储到数据处理、实时计算、数据可视化等环节。
画面3：技术架构图（2.5），展示三层架构：前端（Element UI, Echarts, Vuejs, Nodejs）、中间件（SpringMVC, Spring Boot, Spring Cloud Gateway, Eureka, MyBatis, MyBatis plus, Googet, Netty）和底层（Kafka, Flink, Quartz, Superset）。
画面4：物理部署图（2.6）与微服务拆分（2.7），展示Nginx、Netty、Kafka、Redis、MySQL、HBase等服务的部署结构，以及cold-chain-monitor模块的微服务拆分。
画面5：微服务拆分（2.7），展示cold-chain-monitor模块的微服务拆分，包括用户服务、业务管理服务、实时数据服务等，并展示服务注册与发现的架构图。
画面6：系统环境（3.1.1），介绍JDK 8+，并提供Oracle JDK下载链接和安装命令。
画面7：系统环境（3.1.2-3.1.4），介绍Docker、Kafka和ZooKeeper、redis的安装命令。
画面8：大数据组件（3.2.1 Apache Flink），介绍Flink的流处理特性。
画面9：Apache Flink的流处理特性，展示数据流处理的流程图。
画面10：应用服务（3.3.1 后台服务），展示各服务的端口、说明和启动命令。
画面11：前台应用（3.3.2），展示Tomcat的前端配置文件和应用目录。
画面12：定时任务库（4.3.1 CROM触发器），展示表结构。
画面13：数据结构（4.3.2），展示定时任务库的表结构。
画面14：自定义异常（5.3），展示自定义异常类MyException的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面6：
```
https://download.oracle.com/otn/java/jdk/8u202-linux-x64.rpm
[root@node2-v806 software]# wget https://download.oracle.com/otn/java/jdk/8u202-linux-x64.rpm
[root@node2-v806 software]# mv jdk-8u202-linux-x64.rpm jdk-8u202-linux-x64.rpm
[root@node2-v806 software]# rpm -ivh jdk-8u202-linux-x64.rpm
```

画面7：
```
Docker pull wurstmeister/ZooKeeper
Docker run -d --name ZooKeeper -p 2181:2181 -t wurstmeister/ZooKeeper
Docker pull wurstmeister/Kafka
Docker run -d --name Kafka --publish 9092:9092 --link ZooKeeper --env KAFKA_ZOOKEEPER_CONNECT=zk:2181 --env KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://172.16.0.117 --env KAFKA_ADVERTISED_PORT=9092 -v /etc/localtime:/etc/localtime wurstmeister/Kafka:latest
```

画面10：
```
应用	端口	说明	启动命令
cold-Eureka	8001	服务注册中心	java -jar cold-Eureka-0.0.1-SNAPSHOT.jar &
cold-gateway	8080	API网关，前端统一入口	java -jar cold-gateway-0.0.1-SNAPSHOT.jar &
cold-user	8185	用户服务	java -jar cold-user-1.0.0.jar &
cold-admin	8181	管理服务	java -jar cold-admin-0.0.1-SNAPSHOT.jar &
cold-druid	8182	Druid查询服务	java -jar cold-druid-1.0.0.jar &
cold-monitor	8183	实时查询服务	java -jar cold-monitor-0.0.1-SNAPSHOT.jar &
cold-jobs	8184	定时任务服务	java -jar cold-jobs-0.0.1-SNAPSHOT.jar &
cold-netty-server	10010	netty服务器	java -jar cold-netty-server-1.0-SNAPSHOT.jar
cold-ui	8000	web服务，Tomcat	Service Tomcat start | stop | restart
```

画面12：
```
表名：QRZT_CRON_TRIGGERS
作用：存储触发器的cron表达式表。
名称	类型	长度	小数点	是否为NULL	主键	注释
SCHED_NAME	varchar	120	0	1	1	调度器名称
TRIGGER_NAME	varchar	200	0	1	1	触发器名称
TRIGGER_GROUP	varchar	200	0	1	1	触发器分组名称
CRON_EXPRESSION	varchar	120	0	1	0	CRON表达式
TIME_ZONE_ID	varchar	80	0	0	0	时区
```

画面14：
```
@Data
public class MyException extends RuntimeException {
    private static final long serialVersionUID = 1L;
    private String msg;
    private int code = 500;
    public MyException(String msg) {
        super(msg);
        this.msg = msg;
    }
    public MyException(String msg, Throwable e) {
        super(msg, e);
        this.msg = msg;
    }
    public MyException(String msg, int code) {
        super(msg);
        this.msg = msg;
        this.code = code;
    }
    public MyException(Throwable e) {
        super(e);
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：任务流程图（2.2）：物流仓储 → 数据采集 → 数据解析 → 数据序列化 → 数据处理 → 数据可视化。
画面3：技术架构图（2.5）：前端（Element UI, Echarts, Vuejs, Nodejs） → 中间件（SpringMVC, Spring Boot, Spring Cloud Gateway, Eureka, MyBatis, MyBatis plus, Googet, Netty） → 底层（Kafka, Flink, Quartz, Superset）。
画面4：物理部署图（2.6）：Nginx → Netty → Kafka → Redis → MySQL → HBase → 应用服务。
画面5：微服务拆分（2.7）：服务注册与发现 → 用户服务、业务管理服务、实时数据服务、定时任务服务、netty服务、web服务。
画面10：后台服务表格：应用、端口、说明、启动命令。
画面11：前台应用表格：前端Tomcat、配置文件、应用目录。
画面12：定时任务库表格：表名、作用、字段名、类型、长度、小数点、是否为NULL、主键、注释。
画面13：数据结构表格：表名、作用、字段名、类型、长度、小数点、是否为NULL、主键、注释。
画面14：自定义异常代码：MyException类的定义。

5) 无。

