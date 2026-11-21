# 画面线理解：6.4 Flink工程pom文件介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.4 Flink工程pom文件介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：10 帧 @ 00:16, 01:02, 01:10, 01:13, 01:16, 01:39, 02:03, 02:04, 02:05, 02:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:31:16

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编辑 Maven 项目的 pom.xml 文件，配置 Apache Flink 相关依赖和仓库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 pom.xml 文件的 properties 和 repositories 部分，其中定义了 flink.version、java.version、scala.binary.version 等属性，以及 Apache snapshots 仓库配置。
画面 2: 展示了 Apache Flink 核心依赖的配置，包括 flink-java、flink-streaming-java、flink-connector-kafka_2.11 等，版本号使用了 ${flink.version} 和 ${scala.binary.version} 变量。
画面 3: 展示了 flink-connector-kafka_2.11 的依赖配置，版本号为 1.8.0。
画面 4: 展示了 flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 5: 展示了 flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 6: 展示了 flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 7: 展示了 flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 8: 展示了 flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 9: 展示了 flink-connector-haifa_2.11 的依赖配置，版本号为 1.8.0。
画面 10: 展示了 pom.xml 文件的开头部分，包括 <artifactId>、<version>、<packaging>、<name> 等元素，以及 properties 和 repositories 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <flink.version>1.8.0</flink.version>
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
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-avro</artifactId>
    <version>1.8.0</version>
</dependency>

<!-- Apache Flink dependencies -->
<!-- These dependencies are provided, because they should not be packaged into the JAR file. -->
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-java</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-streaming-java_${scala.binary.version}</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 5:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 6:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 7:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 8:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 9:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-kafka_2.11</artifactId>
    <version>1.8.0</version>
</dependency>
```

画面 10:
```xml
<artifactId>cold-flink</artifactId>
<version>1.0.0</version>
<packaging>jar</packaging>
<name>cold-flink</name>

<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <flink.version>1.8.0</flink.version>
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
