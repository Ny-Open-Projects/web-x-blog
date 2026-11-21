# 画面线理解：02_zk分布式主键_环境准备

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\02_zk分布式主键_环境准备【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:45, 01:37, 01:59, 02:04, 02:14, 02:22, 02:26, 02:29, 02:35, 02:43, 02:55, 03:00, 03:39, 03:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:05:20

1) 这一组画面整体在讲如何在项目中使用 Curator 客户端接入 ZooKeeper 实现分布式主键封装，包括依赖导入、配置文件设置和枚举封装。

2) 按时间顺序列出每张画面的要点：
画面1: 展示文档中“1 分布式主键封装”章节，重点是“1.1 依赖导入”，并提示在 `heima-leadnews/heima-leadnews-common/pom.xml` 中引入依赖。
画面2: 在 Linux 终端中，进入 `zookeeper-3.4.6` 目录，执行 `ls` 查看文件，然后执行 `./bin/zkServer.sh status` 检查 ZooKeeper 服务状态。
画面3: 展示文档中“1.1 依赖导入”部分，强调在 `heima-leadnews/heima-leadnews-common/pom.xml` 中引入依赖。
画面4: 在 IntelliJ IDEA 中，展示 `heima-leadnews` 项目的 `pom.xml` 文件，其中 `modules` 部分列出了多个子模块。
画面5: 展示文档中“1.1 依赖导入”部分，光标在 XML 代码中，提示在 `heima-leadnews/heima-leadnews-common/pom.xml` 中引入依赖。
画面6: 在 IntelliJ IDEA 中，展示 `heima-leadnews` 项目的 `pom.xml` 文件，其中包含多个依赖版本声明，如 `curator.version 4.2.0`。
画面7: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，其中包含 `dependencies` 部分，显示了 `reflections` 依赖。
画面8: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，其中包含 `dependencies` 部分，显示了 `spring-boot-starter-data-redis` 依赖。
画面9: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，其中 `curator` 依赖被选中，下方显示了 `fastjson` 依赖及其 `exclusions` 配置。
画面10: 展示文档中“1.2 配置文件”部分，说明配置文件为 `heima-leadnews-common/src/main/resources/zookeeper.properties`，并列出其内容。
画面11: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common` 项目的 `pom.xml` 文件，光标在 `dependencies` 部分，显示了 `fastjson` 依赖及其 `exclusions` 配置。
画面12: 展示文档中“1.3 枚举封装”和“1.4 序列封装”部分，说明创建 `ZkSequenceEnum` 枚举用于定义通过 ZooKeeper 生成的 ID 枚举。
画面13: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common/src/main/resources/zookeeper.properties` 文件，其中包含 `zk.host` 和 `zk.sequence-path` 配置。
画面14: 在 IntelliJ IDEA 中，展示 `heima-leadnews-common/src/main/resources/zookeeper.properties` 文件，光标在 `zk.sequence-path` 配置行上。

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
[root@localhost ~]# cd zookeeper-3.4.6
[root@localhost zookeeper-3.4.6]# ls
build.xml  conf  ivy.xml  NOTICE.txt  README.txt  zookeeper-3.4.6.jar  zookeeper-3.4.6.tar.gz  zookeeper-3.4.6.tar
[root@localhost zookeeper-3.4.6]# ./bin/zkServer.sh status
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
        <module>service-mycat</module>
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
    <elasticsearch.version>7.2.0</elasticsearch.version>
    <ali.core.version>4.1.1</ali.core.version>
    <ali.green.version>3.4.1</ali.green.version>
    <kafka.version>2.1.7</kafka.version>
    <kafka.client.version>2.0.1</kafka.client.version>
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
