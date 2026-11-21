# 画面线理解：5-MapReduce案例-wordcount-准备工作

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\5-MapReduce案例-wordcount-准备工作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:39, 01:05, 01:22, 01:59, 02:15, 02:59, 03:14, 03:46, 03:52, 03:58, 04:23, 04:45, 05:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:43:35

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Hadoop MapReduce 编写一个 WordCount 程序，包括数据准备、Mapper 和 Reducer 的自定义实现、项目结构搭建及 Maven 配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Hadoop MapReduce 的工作流程图，包括：
  - 原文件（a.txt）通过 TextInputFormat 读取。
  - Map 阶段：将输入数据（K1, V1）转换为中间键值对（K2, V2）。
  - Shuffle 阶段：对 K2 进行分区、排序、规约和分组。
  - Reduce 阶段：将 K2 和 V2 转换为最终结果（K3, V3）。
- 画面中包含一个 Notepad++ 窗口，显示了名为 "Note03.md" 的文件，但内容被遮挡。

画面 2：
- 展示了 Typora 编辑器中的 WordCount 课程文档。
- 内容包括：
  - 需求：在一堆给定的文本文件中统计输出每一个单词出现的总次数。
  - Step 1. 数据格式准备：
    1. 创建一个新文件：`cd /export/servers` 和 `vim wordcount.txt`。
    2. 向其中放入以下内容并保存：
      ```
      hello,world,hadoop
      world,hdfs
      hadoop,java
      ```
  - Step 2. Mapper：展示了 Mapper 类的 Java 代码框架：
    ```java
    public class WordCountMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    @Override
    ```

画面 3：
- 展示了 Typora 编辑器中的 WordCount 课程文档。
- 内容包括：
  - Step 1. 数据格式准备：
    1. 创建一个新文件：`cd /export/servers` 和 `vim wordcount.txt`。
    2. 向其中放入以下内容并保存：
      ```
      hello,world,hadoop
      world,hdfs
      hadoop,java
      ```
  - Step 2. Mapper：展示了 Mapper 类的 Java 代码框架：
    ```java
    public class WordCountMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    @Override
    ```

画面 4：
- 展示了 SecureCRT 的终端界面。
- 当前用户为 [root@node01 servers]#，终端处于空闲状态，等待输入命令。

画面 5：
- 展示了 Hadoop 的 Web 界面（HDFS 浏览器）。
- 路径为 /wordcount，显示了一个名为 wordcount.txt 的文件。
- 文件信息：
  - 权限：-rw-r--r--
  - 所有者：root
  - 组：supergroup
  - 大小：71 B
  - 最后修改时间：Apr 30 18:07
  - 块大小：128 MB
  - 复制数：1

画面 6：
- 展示了 Hadoop MapReduce 的工作流程图。
- 内容与画面 1 类似，但未显示完整的 Reduce 阶段输出。

画面 7：
- 展示了 Hadoop MapReduce 的工作流程图。
- 内容与画面 6 类似，但显示了 Reduce 阶段的输出结果：
  - K3: hello, world, hadoop, hdfs
  - V3: 2, 2, 2, 1

画面 8：
- 展示了 IntelliJ IDEA 中创建新模块的界面。
- 选择的模块类型为 "Maven"。
- 项目 SDK 为 "jdk1.8.0_241"。
- 点击 "Next" 按钮。

画面 9：
- 展示了 IntelliJ IDEA 中的 Maven pom.xml 文件。
- 文件内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <groupId>cn.itcast.mapreduce</groupId>
      <artifactId>day03_mapreduce_wordcount</artifactId>
      <version>1.0-SNAPSHOT</version>
      <packaging>jar</packaging>
      <name>day03_mapreduce_wordcount</name>
      <description>day03_mapreduce_wordcount</description>
      <properties>
          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
          <maven.compiler.source>1.8</maven.compiler.source>
          <maven.compiler.target>1.8</maven.compiler.target>
      </properties>
      <parent>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-parent</artifactId>
          <version>2.1.10.RELEASE</version>
          <relativePath/>
      </parent>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-web</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-test</artifactId>
              <scope>test</scope>
          </dependency>
      </dependencies>
      <build>
          <plugins>
              <plugin>
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-maven-plugin</artifactId>
                  <configuration>
                      <mainClass>cn.itcast.mapreduce.JobMain</mainClass>
                  </configuration>
                  <executions>
                      <execution>
                          <goals>
                              <goal>repackage</goal>
                          </goals>
                      </execution>
                  </executions>
              </plugin>
          </plugins>
      </build>
  </project>
  ```

画面 10：
- 展示了 IntelliJ IDEA 中的项目结构。
- 右键点击 "day03_mapreduce_wordcount" 模块，弹出菜单。
- 选择 "Analyze" 选项。

画面 11：
- 展示了 IntelliJ IDEA 中的 Maven pom.xml 文件。
- 文件内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <groupId>cn.itcast.mapreduce</groupId>
      <artifactId>day03_mapreduce_wordcount</artifactId>
      <version>1.0-SNAPSHOT</version>
      <packaging>jar</packaging>
      <name>day03_mapreduce_wordcount</name>
      <description>day03_mapreduce_wordcount</description>
      <properties>
          <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
          <maven.compiler.source>1.8</maven.compiler.source>
          <maven.compiler.target>1.8</maven.compiler.target>
      </properties>
      <parent>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-parent</artifactId>
          <version>2.1.10.RELEASE</version>
          <relativePath/>
      </parent>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-web</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-test</artifactId>
              <scope>test</scope>
          </dependency>
      </dependencies>
      <build>
          <plugins>
              <plugin>
                  <groupId>org.springframework.boot</groupId>
                  <artifactId>spring-boot-maven-plugin</artifactId>
                  <configuration>
                      <mainClass>cn.itcast.mapreduce.JobMain</mainClass>
                  </configuration>
                  <executions>
                      <execution>
                          <goals>
                              <goal>repackage</goal>
                          </goals>
                      </execution>
                  </executions>
              </plugin>
          </plugins>
      </build>
  </project>
  ```

画面 12：
- 展示了 IntelliJ IDEA 中的项目结构。
- 右键点击 "mapreduce"
