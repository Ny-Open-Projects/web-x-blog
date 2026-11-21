# 6.4 Flink工程pom文件介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.4 Flink工程pom文件介绍_【海量资源尽在 666java.com】.mp4
- 时长 2分10秒（音频 130s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来看一看我们Flink工程的泡沫文件当然了我们Flink工程有好几种途径可以创建一种途径是说我们能够创建Maven工程的方式然后在创建完Maven工程之后在泡沫文件里边添加一些我们的这个依赖包那另外一种方式是我们通过Maven的这种Generator
[00:21] 这种方式就是说我通过Maywind的Flink它的一个模板工程来创建我本地的一个Flink工程当然了在两种方式里边我们在泡沫文件里边都需要添加我们的一些引用这种引用的话一个是我们的这种code commentcode comment里边有我们要引用的这个消息也就是说是实时数据的消息它的一个这种实体类
[00:48] 那么还有一个是我们需要把我们返回类我们返回类也是在我们的code comment里面用到的那么flinkavril的话实际上是一个虚立化的一个工具是Flink工具啊Flink进行虚立化的一个啊我们使用了1.8.0的这个版本那下面的话是Flink-java和Flink-streaming-java这两个这两个jar 包
[01:15] 那还有一个的话是我们的这个flinkconnect的一个卡不卡这个因为我们的程序是要访问我们的这个卡不卡访问我们卡不卡堆列里边拿到我们实时计算的数据那同时把计算完的结果也发送到卡不卡里边去所以说我们需要使用的是flinkconnect干这个卡不卡这样的一个加包那当然我们还有一个叫flinkconnectredis
[01:44] 这个是我们需要在Flink实际计算的时候我们从Redis里边拿到缓存数据如果我们存储完了计算完了之后呢我们需要把数据存储到我们的MySQL里边去所以说我们需要用了一个MySQL Connect-Java这样的一个jar 包这就是我们的一个在Flink里边用到的一些jar 包

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编辑 Maven 项目的 pom.xml 文件，配置 Apache Flink 相关依赖和仓库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 pom.xml 文件的 properties 和 repositories 部分，其中定义了 Flink.version、java.version、scala.binary.version 等属性，以及 Apache snapshots 仓库配置。
画面 2: 展示了 Apache Flink 核心依赖的配置，包括 Flink-java、Flink-streaming-java、Flink-connector-kafka_2.11 等，版本号使用了 ${Flink.version} 和 ${scala.binary.version} 变量。
画面 3: 展示了 Flink-connector-kafka_2.11 的依赖配置，版本号为 1.8.0。
画面 4: 展示了 Flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 5: 展示了 Flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 6: 展示了 Flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 7: 展示了 Flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 8: 展示了 Flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 9: 展示了 Flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 10: 展示了 pom.xml 文件的开头部分，包括 <artifactId>、<version>、<packaging>、<name> 等元素，以及 properties 和 repositories 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <Flink.version>1.8.0</Flink.version>
    <java.version>1.8</java.version>
    <scala.binary.version>2.11</scala.binary.version>
    <maven.compiler.source>${java.version}</maven.compiler.source>
    <maven.compiler.target>${java.version}</maven.compiler.target>
</properties>

<repositories>
    <repository>
        <id>apache.snapshots</id>
        <name>Apache Development Snapshot Repository</name>
        <url>https://repository.apache.org/content/repositories/snapshots/</url>
        <releases>
            <enabled>false</enabled>
        </releases>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
</repositories>
```

画面 2:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-avro</artifactId>
    <version>1.8.0</version>
</dependency>

<!-- Apache Flink dependencies -->
<!-- These dependencies are provided, because they should not be packaged into the JAR file. -->
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-java</artifactId>
    <version>${Flink.version}</version>
    <scope>provided</scope>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-streaming-java_${scala.binary.version}</artifactId>
    <version>${Flink.version}</version>
    <scope>provided</scope>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 5:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 6:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 7:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 8:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 9:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 10:
```xml
<artifactId>cold-Flink</artifactId>
<version>1.0.0</version>
<packaging>jar</packaging>
<name>cold-Flink</name>

<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <Flink.version>1.8.0</Flink.version>
    <java.version>1.8</java.version>
    <scala.binary.version>2.11</scala.binary.version>
    <maven.compiler.source>${java.version}</maven.compiler.source>
    <maven.compiler.target>${java.version}</maven.compiler.target>
</properties>

<repositories>
    <repository>
        <id>apache.snapshots</id>
        <name>Apache Development Snapshot Repository</name>
        <url>https://repository.apache.org/content/repositories/snapshots/</url>
        <releases>
            <enabled>false</enabled>
        </releases>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
</repositories>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

