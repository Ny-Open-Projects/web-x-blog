# 10-环境搭建-导入Scala基础工程&基础工程介绍

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\10-环境搭建-导入Scala基础工程&基础工程介绍_【海量资源尽在 666java.com】.mp4
- 时长 6分11秒（音频 371s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来导入基础工程,通过本节的学习,一定要将Skala的基础工程给导入成功,因为后面咱们都是基于这个基础工程进行开发的。
[00:13] 这里文档里边也有对应的一个导入步骤,咱们直接打开开发工具进行导入。
[00:21] 这里选择Open,选择你的原码路径,我这里原码路径是在地盘的扣带目录下。
[00:29] 选择这个学程就是XC-Anslers-UK这个地方导入项目之后它会告诉你没有配置什么project-JDK并没有配置其实不光JDK没有配置是不是sdk咱们也没有配置sdk是scala的sdk接下来咱们首先把JDK和sdk给配置了点击fail
[00:59] 然后是project kit下面这个settings下面project kitstrat kit这个选项然后进行点击在弹出这个菜单呢sdk这个地方配置咱们JDK点击加号然后弹出菜单选择JDK这里呢咱们JDK安装目录是在dee vtools目录下的java目录选择咱们的目录即可gdk1.8
[01:31] 这里已经导入成功,点击下update接下来是SDK的配置,SDK是选择Global,然后Libraries点击加号,选择Skala的SDK这里咱们选择Blue,找到咱们Skala SDK的目录这里是Skala,我倒是在地盘,DV TOS目录下的Skala目录内有一个Skala 2.1.8,点击OK
[02:01] 这个时候呢他会选择这个库你要添加到哪个模块咱们呢就添加到副工程就是XC-S因为下面是子模块咱们直接添加到副工程点击双击或者点击下面的OK都可以这时候呢已经成功了添加成功了点击update然后点击OK这个地方还没有报还报一个JDK找不着是因为咱们添加完成之后并没有对它进行一个配置
[02:33] 点击setup JDK这个时候呢你要使用哪个版本咱们就选用JDK 1.8点击ok即可相同的scala这个地方它已经识别了因为已经配置好配置好完成之后呢接下来咱们对工程进行一个介绍XZ common intree这个工程下面包含了咱们项目所使用的所有实体这个实体呢咱们已经创建好了可以直接拿来使用这是实体的一个
[03:06] 接下来是Common Utils这里边有咱们所要使用的所有的工具类包括日期工具类IP工具类Redis工具类Zipfer工具类等等这些工具类也是可以直接拿来使用的XZ Service Offline这是咱们的离线分析所有的离线分析都在这个目录内接下来是
[03:34] XC,Source,RT这个是咱们的实时分析所有的实时分析代码都在这个目录内接下来是XC,Source,Search咱们的即时查询的代码在这个目录内这里基础配置已经好基础配置介绍完了之后咱们回到文档这个地方有一个基础工程的一个介绍这里已经介绍完成接下来是卖用坐标的一个介绍咱们还回到开发工具咱们这里规定的版本
[04:09] 就是Hadoop的版本,Hyroid的版本,HBase的版本这里和咱们在开始CDH环境介绍的时候所使用的版本是保持一致的这里有一个谷歌的PortalBuff这个是解决版本冲突的接下来这是Skala的版本咱们用的是2.1.8这是MySQL的版本因为咱们需要独显MySQL这里使用的8.0.16
[04:42] 最新版本接下来是Spark的配置有这么多依赖接下来是Hadoop的配置Hadoop指导了一个Klynt接下来是Hive的配置Hive的配置还是蛮多的有这么多接下来是HBase的配置HBase有这么多这里相关的依赖也已经排除掉就是说有冲突的也已经排除掉接下来是Json的配置这里用到了Fast的Json还有JsonLab以及GTJson
[05:14] 这都是项目中其他包进行的一个相关依赖依赖进来的接下来是日志的配置日志的配置结束之后是Kafka的配置以及redis的配置还有Elasticsearch的配置以及这是工具类通用工具类的一个配置这是commons的pull这是现成相关的这是IP工具类最后是咱们的测试类以上就是所有的埋问坐标
[05:48] 好咱们回到文档导入基础工程呢以及基础工程的介绍还有Maiwan坐标的介绍就到这里一定要把基础工程给导入进来而且呢配置成功配置成功呢一个标志就是这里没有暴错这里呢也看不到暴错就可以了好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中导入 Scala 基础工程，并介绍项目结构和 Maven 依赖坐标。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前章节为“2.3 导入基础工程”，并演示在 IDEA 中点击“Open”导入项目，弹出“Preparing workspace...”窗口。
画面2：展示 IDEA 启动界面，选中“Import Project”选项，准备导入项目。
画面3：展示导入后的项目结构，包含多个模块，如“xc-common-entity”、“xc-Service-search”等，以及“Platform.scala”文件内容。
画面4：在 IDEA 中打开“Project Structure”对话框，选中“Global Libraries”选项卡。
画面5：展示“Platform.scala”文件内容，其中定义了 case class PlatformOfflineBiz。
画面6：展示课程目录，当前章节为“2.3.2 Scala基础工程介绍”，并演示在 IDEA 中打开项目结构。
画面7：展示“pom.xml”文件内容，其中包含项目的基本配置和依赖信息。
画面8：在“pom.xml”中高亮显示“<dependency>”标签，展示依赖配置。
画面9：在“pom.xml”中高亮显示“<dependency>”标签，展示 Hive 相关依赖。
画面10：在“pom.xml”中高亮显示“<dependency>”标签，展示 Hive Shell 依赖。
画面11：在“pom.xml”中高亮显示“<dependency>”标签，展示 Kafka 依赖。
画面12：在“pom.xml”中高亮显示“<dependency>”标签，展示 Redis 依赖。
画面13：展示课程目录，当前章节为“2.3.3 Maven坐标介绍”，并展示“pom.xml”中部分依赖坐标。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```scala
package cn.itcast.xc.entity

/**
 * 平台首页数据业务实体类
 */
case class PlatformOfflineBiz(
  clazz: String,
  total_count: Int,
  yesterday_count: Int,
  years: String,
  months: String,
  days: String
)
```

画面7：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.itcast</groupId>
    <artifactId>xc-analysis</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <properties>
        <java.version>1.8</java.version>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
        <scala.version>2.11.8</scala.version>
        <Spark.version>2.3.2</Spark.version>
        <mysql.version>8.0.16</mysql.version>
        <Hadoop.version>2.6.0</Hadoop.version>
        <chive.version>1.1.8</chive.version>
        <base.version>1.2.0</base.version>
        <log.version>11.0</log.version>
        <Elasticsearch.version>6.4.0</Elasticsearch.version>
        <Kafka.version>2.1.0</Kafka.version>
    </properties>

    <repositories>
        <repository>
            <id>scala-tools.org</id>
            <name>Scala Tools Maven Repository</name>
            <url>http://scala-tools.org/repo-releases</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>com.google.protobuf</groupId>
            <artifactId>protobuf-java</artifactId>
            <version>3.5.0</version>
        </dependency>
        <dependency>
            <groupId>org.scala-lang</groupId>
            <artifactId>scala-library</artifactId>
            <version>${scala.version}</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>${mysql.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-core_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-sql_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-hive_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-streaming_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-hive_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-Hive-thriftserver_2.11</artifactId>
            <version>${Spark.version

