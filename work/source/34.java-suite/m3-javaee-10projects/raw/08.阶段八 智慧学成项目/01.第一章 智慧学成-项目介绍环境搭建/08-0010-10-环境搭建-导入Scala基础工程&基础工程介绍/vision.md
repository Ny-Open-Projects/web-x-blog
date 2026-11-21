# 画面线理解：10-环境搭建-导入Scala基础工程&基础工程介绍

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\10-环境搭建-导入Scala基础工程&基础工程介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:03, 00:34, 01:06, 01:35, 02:39, 03:55, 04:09, 04:33, 04:54, 05:06, 05:24, 05:36, 05:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:33:22

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中导入 Scala 基础工程，并介绍项目结构和 Maven 依赖坐标。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前章节为“2.3 导入基础工程”，并演示在 IDEA 中点击“Open”导入项目，弹出“Preparing workspace...”窗口。
画面2：展示 IDEA 启动界面，选中“Import Project”选项，准备导入项目。
画面3：展示导入后的项目结构，包含多个模块，如“xc-common-entity”、“xc-service-search”等，以及“Platform.scala”文件内容。
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
        <spark.version>2.3.2</spark.version>
        <mysql.version>8.0.16</mysql.version>
        <hadoop.version>2.6.0</hadoop.version>
        <chive.version>1.1.8</chive.version>
        <base.version>1.2.0</base.version>
        <log.version>11.0</log.version>
        <elasticsearch.version>6.4.0</elasticsearch.version>
        <kafka.version>2.1.0</kafka.version>
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
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-sql_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-streaming_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive-thriftserver_2.11</artifactId>
            <version>${spark.version
