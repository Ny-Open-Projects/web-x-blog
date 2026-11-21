# 02_zk分布式主键_环境准备

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\02_zk分布式主键_环境准备【海量资源尽在 666java.com】.mp4
- 时长 4分12秒（音频 252s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位下面咱们就来进入今天的第一个章节有一个分布式主件的封装这个咱们主要用的是当前的Sockkeeper当然这里边也说了一个东西就是说此功能可以用Macad、Values和Sockkeeper都可以轻松实践而考虑中间件的负载均衡和演示Sockkeeper实战应用的目的咱们这次是采用Sockkeeper来去生成分布式自增ID
[00:27] 好在实际项目中呢其实这种方式呢也是非常常用的一种手段好吧那咱们话不多说来咱们直接去在代码上去做一些看怎么去做啊那下面呢首先呢做代码之前呢或者说咱们封装这个之前呢首先呢要去把环境搭建一下那这里边呢首先咱们要去连接当前的组keeper使用一个当前的这种jar 包啊这jar 包但是jar 包之前呢你首先呢得有组keeper的环境
[00:55] 那环境的话呢其实今天呢我就把它装到了当前的一个Linux上面那这个呢你可以打开看一下啊比如说打开这里面是有个组keeper啊然后你去上你去上传然后之后呢有一个bin我当前我这份呢是已经启动了好可以查看一下状态当前状态呢其实已经在启动的状态如果说你的Linux上没有的话呢你需要去安装当前的组keeper并且呢这个组keeper安装的时候
[01:27] 你要知道它是依赖于或者说有Java JDK的环境才行要不然的话它肯定启动不正宫所以说这个你安装的时候需要注意一下好吧行那今天的课上的课上上完之后呢我也会把当前的当前的这个Linux镜像啊直接去放到资料中大家也可以直接去挂载我这个镜像也是可以的好吧那行啊这个环境有了环境有了之后呢咱们下面就去导入当前的POM文件
[01:56] 这个popup文件其实在我们已经导入了就是当前组keeper的一个客户端在那可以打开当前的复工程里边你可以去搜一下当前这个包看有没有这个包你搜一下其实这已经定义完了在当前的comment中也定义完了这个事你不用去特意再去操作如果说你后期自己去集成的时候那这个事你不能忘了
[02:30] 好吧行啊你看这一块其实组keeper的客户端已经都导入进来了然后下面呢其实这个导入完之后呢还没有完是吧首先呢你要去连上当前的组keeper你还需要有一个配置文件那这配置文件的话咱们就在当前common下面创建一个组keeper.publish打开然后srcman下面有个resource然后可以在这右键创建一个啊那这个时候呢里边写啥呢里边咱们就直接拷贝过来就可以了啊
[03:05] 第一个是当前Zokekeeper的一个提指我这个提指就是当前Linux上的一个提指叫192.168.220.145它目标档口是2181这个是有一个Zokekeeper自动存储的闹的节点咱们需要去有一个存储的路径就是当前项目下边有一个Sugun-C目录行那这个你说之前咱们好像不是在这写死的你看当前MySQL中是不是不是写死的
[03:33] 咱们是不是在当前某个环境下边去配置啊是可以的啊咱们为了方便一些啊咱们现在就不在这去写了你直接在这写让他去读当前的配置就可以了在实际开发的时候如果说你有切换环境的需求的话你就得去在哪啊就得去在这三个不同的环境中去配置不同的什么呢Zokeper的地址这能理解吧好
[04:00] 那目前的话咱们就在开发阶段咱们在这就暂时写死了他默认都是加载的当前的这个ZOOkeeper的环境好那这环境咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在项目中使用 Curator 客户端接入 ZooKeeper 实现分布式主键封装，包括依赖导入、配置文件设置和枚举封装。

2) 按时间顺序列出每张画面的要点：
画面1: 展示文档中“1 分布式主键封装”章节，重点是“1.1 依赖导入”，并提示在 `heima-leadnews/heima-leadnews-common/pom.xml` 中引入依赖。
画面2: 在 Linux 终端中，进入 `ZooKeeper-3.4.6` 目录，执行 `ls` 查看文件，然后执行 `./bin/zkServer.sh status` 检查 ZooKeeper 服务状态。
画面3: 展示文档中“1.1 依赖导入”部分，强调在 `heima-leadnews/heima-leadnews-common/pom.xml` 中引入依赖。
画面4: 在 IntelliJ IDEA 中，展示 `heima-leadnews` 项目的 `pom.xml` 文件，其中 `modules` 部分列出了多个子模块。
画面5: 展示文档中“1.1 依赖导入”部分，光标在 XML 代码中，提示在 `heima-leadnews/heima-leadnews-common/pom.xml` 中引入依赖。
画面6: 在 IntelliJ IDEA 中，展示 `heima-leadnews` 项目的 `pom.xml` 文件，其中包含多个依赖版本声明，如 `curator.version 4.2.0`。
画面7: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，其中包含 `dependencies` 部分，显示了 `reflections` 依赖。
画面8: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，其中包含 `dependencies` 部分，显示了 `spring-boot-starter-data-redis` 依赖。
画面9: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，其中 `curator` 依赖被选中，下方显示了 `fastjson` 依赖及其 `exclusions` 配置。
画面10: 展示文档中“1.2 配置文件”部分，说明配置文件为 `heima-leadnews-common/src/main/resources/ZooKeeper.properties`，并列出其内容。
画面11: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，光标在 `dependencies` 部分，显示了 `fastjson` 依赖及其 `exclusions` 配置。
画面12: 展示文档中“1.3 枚举封装”和“1.4 序列封装”部分，说明创建 `ZkSequenceEnum` 枚举用于定义通过 ZooKeeper 生成的 ID 枚举。
画面13: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common/src/main/resources/ZooKeeper.properties` 文件，其中包含 `zk.host` 和 `zk.sequence-path` 配置。
画面14: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common/src/main/resources/ZooKeeper.properties` 文件，光标在 `zk.sequence-path` 配置行上。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```xml
<properties>
    <curator.version>4.2.0</curator.version>
</properties>
<!-- curator ZK 客户端 -->
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>${curator.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>${curator.version}</version>
</dependency>
```

画面2:
```bash
[root@localhost ~]# cd ZooKeeper-3.4.6
[root@localhost ZooKeeper-3.4.6]# ls
build.xml  conf  ivy.xml  NOTICE.txt  README.txt  ZooKeeper-3.4.6.jar  ZooKeeper-3.4.6.tar.gz  ZooKeeper-3.4.6.tar
[root@localhost ZooKeeper-3.4.6]# ./bin/zkServer.sh status
Mode: standalone
```

画面3:
```xml
<properties>
    <curator.version>4.2.0</curator.version>
</properties>
<!-- curator ZK 客户端 -->
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>${curator.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>${curator.version}</version>
</dependency>
```

画面4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.heima</groupId>
    <artifactId>heima-leadnews</artifactId>
    <packaging>pom</packaging>
    <version>1.0-SNAPSHOT</version>
    <modules>
        <module>heima-leadnews-common</module>
        <module>heima-leadnews-api</module>
        <module>heima-leadnews-article</module>
        <module>heima-leadnews-model</module>
        <module>heima-leadnews-utils</module>
        <module>Service-mycat</module>
    </modules>
    <!-- 地址Spring boot工程 -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
        <relativePath/>
    </parent>
```

画面5:
```xml
<properties>
    <curator.version>4.2.0</curator.version>
</properties>
<!-- curator ZK 客户端 -->
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>${curator.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>${curator.version}</version>
</dependency>
```

画面6:
```xml
<properties>
    <jsoup.version>1.10.2</jsoup.version>
    <jwt.version>1.0.1</jwt.version>
    <fastjson.version>1.2.58</fastjson.version>
    <fastjson.dataformat.version>1.2.58</fastjson.dataformat.version>
    <spring.jwt.version>0.9.0</spring.jwt.version>
    <spring.boot.admin.version>2.1.6</spring.boot.admin.version>
    <spring.cloud.version>Greenwich.SR1</spring.cloud.version>
    <curator.version>4.2.0</curator.version>
    <hanlp.version>1.3.4</hanlp.version>
    <fastdfs.version>0.2.0</fastdfs.version>
    <baomidou.version>1.11</baomidou.version>
    <junit.version>4.12</junit.version>
    <searchbox.version>6.3.1</searchbox.version>
    <Elasticsearch.version>7.2.0</Elasticsearch.version>
    <ali.core.version>4.1.1</ali.core.version>
    <ali.green.version>3.4.1</ali.green.version>
    <Kafka.version>2.1.7</Kafka.version>
    <Kafka.client.version>2.0.1</Kafka.client.version>
    <reflections.version>0.9.1</reflections.version>
</properties>
```

画面7:
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>heima-leadnews-common</artifactId>
    <packaging>jar</packaging>
    <name>heima-leadnews-common</name>
    <dependencies>
        <dependency>
            <groupId>com.heima</groupId>
            <artifactId>heima-leadnews-utils</artifactId>
        </dependency>
        <dependency>
            <groupId>org.reflections</groupId>
            <artifactId>reflections</artifactId>
        </dependency>
        <!-- Spring boot starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面8:
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>heima-leadnews-common</artifact

