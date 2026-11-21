# 画面线理解：12.推荐系统之搭建工程

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\12.推荐系统之搭建工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:10, 00:26, 00:33, 00:37, 00:43, 01:23, 01:26, 01:35, 01:41, 01:58, 02:05, 02:11, 02:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:58:55

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spark 的推荐系统搭建，包括 Maven 依赖配置和应用配置文件的设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Maven POM 文件的开头部分，包含项目基本信息和父模块配置。
画面2：展示 Java 代码中保存发布数据到 MongoDB 的逻辑，包括设置 ID、创建时间、保存对象等。
画面3：与画面2内容相同，为同一代码段的重复展示。
画面4：展示 Maven POM 文件中父模块配置和依赖部分的开头。
画面5：展示 PPT 页面，标题为“2.2. 配置文件 app.properties”，并显示了其中的 Spark MongoDB 输入 URI 配置。
画面6：展示 Maven POM 文件中 Spark 依赖的配置。
画面7：展示 Maven POM 文件中排除 javax.servlet 依赖的配置。
画面8：展示 Maven POM 文件中排除 javax.servlet 依赖的配置，光标在版本号上。
画面9：展示 Maven POM 文件中排除 javax.servlet 依赖的配置，光标在版本号上。
画面10：展示 Maven POM 文件中排除 javax.servlet 依赖的配置，光标在版本号上。
画面11：展示 PPT 页面，标题为“2.2. 配置文件 app.properties”，并显示了其中的 Spark MongoDB 输入 URI 配置。
画面12：展示 PPT 页面，标题为“使用 Spark MLlib 进行推荐”，并显示了推荐系统相关的 Java 包导入语句。
画面13：展示 Maven POM 文件中依赖部分的完整内容，包括 Spark、MongoDB、Servlet、Lombok 和 Redis 依赖。
画面14：展示 PPT 页面，标题为“day08-推荐 - Typora”，并显示了 app.properties 文件中 Redis 集群节点配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>itcast-tanhua</artifactId>
        <groupId>cn.itcast.tanhua</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <packaging>jar</packaging>
    <artifactId>itcast-tanhua-spark</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-mllib_2.12</artifactId>
            <version>2.4.3</version>
            <!--scope>runtine</scope-->
            <exclusions>
                <exclusion>
                    <groupId>javax.servlet</groupId>
                    <artifactId>javax.servlet-api</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
```

画面2：
```java
try {
    //填充数据
    publish.setId(ObjectId.get());
    publish.setCreated(System.currentTimeMillis()); //发布时间
    publish.setCtType(1); //查看权限
    //增加自增长的pid
    publish.setPid(this.idService.createId(type,"publish", publish.getId()));
    //保存动态信息
    this.mongoTemplate.save(publish);
    //写入到自己的相册表中
    Album album = new Album();
    Album.setId(ObjectId.get());
    album.setPublishId(publish.getId()); //动态id
    album.setCreated(System.currentTimeMillis());
    //将相册对象写入到MongoDB中
    this.mongoTemplate.save(album, collectionName: "quanzi_album_"
    //查询当前用户的好友数据，将动态数据写入到好友的时间线表中
```

画面5：
```properties
spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua.recommend.quanzi.201910017
```

画面6：
```xml
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-mllib_2.12</artifactId>
    <version>2.4.3</version>
    <!--scope>runtine</scope-->
    <exclusions>
        <exclusion>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面7：
```xml
<dependency>
    <groupId>org.mongodb.spark</groupId>
    <artifactId>mongo-spark-connector_2.12</artifactId>
    <version>2.4.1</version>
</dependency>
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>3.1.0</version>
    <!--scope>provided</scope-->
</dependency>
```

画面8：
```xml
<dependency>
    <groupId>org.mongodb.spark</groupId>
    <artifactId>mongo-spark-connector_2.12</artifactId>
    <version>2.4.1</version>
</dependency>
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>3.1.0</version>
    <!--scope>provided</scope-->
</dependency>
```

画面9：
```xml
<dependency>
    <groupId>org.mongodb.spark</groupId>
    <artifactId>mongo-spark-connector_2.12</artifactId>
    <version>2.4.1</version>
</dependency>
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>3.1.0</version>
    <!--scope>provided</scope-->
</dependency>
```

画面10：
```xml
<dependency>
    <groupId>org.mongodb.spark</groupId>
    <artifactId>mongo-spark-connector_2.12</artifactId>
    <version>2.4.1</version>
</dependency>
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>3.1.0</version>
    <!--scope>provided</scope-->
</dependency>
```

画面11：
```properties
spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua.recommend.quanzi.201910017
```

画面12：
```java
package com.tanhua.spark.mongo;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.mllib.recommendation.ALS;
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel;
```

画面13：
```xml
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-mllib_2.12</artifactId>
    <version>2.4.3</version>
    <!--scope>runtine</scope-->
    <exclusions>
        <exclusion>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>org.mongodb.spark</groupId>
    <artifactId>mongo-spark-connector_2.12</artifactId>
    <version>2.4.1</version>
</dependency>
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>3.1.0</version>
    <!--scope>provided</scope-->
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
</dependency>
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>3.1.0</version>
</dependency>
```

画面14：
```properties
redis.cluster.nodes = 192.168.31.81:6379,192.168.31.81:6380,192.168.31.81:6381
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PPT标题为“2.2. 配置文件 app.properties”，内容为 Spark MongoDB 输入 URI 配置。
画面11：PPT标题为“2.2. 配置文件 app.properties”，内容为 Spark MongoDB 输入 URI 配置。
画面12：PPT标题为“使用 Spark MLlib 进行推荐”，内容为 Java
