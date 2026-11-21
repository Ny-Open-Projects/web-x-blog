# 12.推荐系统之搭建工程

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\12.推荐系统之搭建工程_【海量资源尽在 666java.com】.mp4
- 时长 2分38秒（音频 158s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来搭建我们的这个Spark系统那么首先呢我们下面呢我们来创建工程啊那么我们就还是在我们的这个工程中啊来创建一个子模块然后呢去new一个module然后呢我们去输入这个叫my叫炭化然后呢Spark好然后呢我们下一步然后呢去输入它点击finish完成
[00:27] 那么工程呢就创建好了那么接下来呢我们来导入一些相关的一些这个依赖那我们把这个dependence然后呢全部都拷贝过来好那我们就都拷到这个里面来OK好那我们来看一下这个里面导入的一些相关的一些依赖那么首先呢导入的是我们的Spark的MLib这样的一个依赖然后呢这个呢是我们要导入的是
[00:55] 就是mongodb spag的一个连接那么原因是呢我们想我们要使用这个spag去读取到我们的mongodb然后呢去读取mongodb中的数据啊所以我们必须要通过一个驱动包然后来连接到我们的mongodb啊才可以去获取到数据啊这就是我们所需要的一个驱动包
[01:19] 然后下面这个是Serverlet API那么要把它引入进来那么要注意的是在上面这个位置我们要把它之前使用的2.5的版本要给它排除掉然后引入到我们统一使用的3.1这个里面来3.1.0这样的一个版本那么所以我们需要上面排除一下然后下面做一个引入要不然可能会出问题的然后我们会引入Longbook这样的一个依赖
[01:48] 然后再引入redis因为我们最终还是需要把结果数据去写入到我们的redis中所以说这个也是必须要有的好接下来我们来编写配置文件那么配置文件我们基本我们写两个我们来看一下好那么我们把这个先来写出来一会我们这个有用那么来写一个叫做app properties然后我们把这两个拷贝过来
[02:16] 那么一个是我们mongodb的一个URL一个就是我们的一个redis的一个redis的一个cluster就是我们redis的一个集群的一个这样的一个配置OK好那么到这里我们的基本的工程的搭建以及我们这个配置文件那我们就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    <artifactId>itcast-tanhua-Spark</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-mllib_2.12</artifactId>
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
Spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua.recommend.quanzi.201910017
```

画面6：
```xml
<dependency>
    <groupId>org.apache.Spark</groupId>
    <artifactId>Spark-mllib_2.12</artifactId>
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
    <groupId>org.mongodb.Spark</groupId>
    <artifactId>mongo-Spark-connector_2.12</artifactId>
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
    <groupId>org.mongodb.Spark</groupId>
    <artifactId>mongo-Spark-connector_2.12</artifactId>
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
    <groupId>org.mongodb.Spark</groupId>
    <artifactId>mongo-Spark-connector_2.12</artifactId>
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
    <groupId>org.mongodb.Spark</groupId>
    <artifactId>mongo-Spark-connector_2.12</artifactId>
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
Spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua.recommend.quanzi.201910017
```

画面12：
```java
package com.tanhua.Spark.mongo;
import org.apache.Spark.api.java.JavaPairRDD;
import org.apache.Spark.api.java.JavaRDD;
import org.apache.Spark.mllib.recommendation.ALS;
import org.apache.Spark.mllib.recommendation.MatrixFactorizationModel;
```

画面13：
```xml
<dependency>
    <groupId>org.apache.Spark</groupId>
    <artifactId>Spark-mllib_2.12</artifactId>
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
    <groupId>org.mongodb.Spark</groupId>
    <artifactId>mongo-Spark-connector_2.12</artifactId>
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

