# 5-MapReduce案例-wordcount-准备工作

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\5-MapReduce案例-wordcount-准备工作【海量资源尽在 ubkz.com】.mp4
- 时长 5分9秒（音频 310s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们给大家详细讲解了word count这个案例整个的执行流程接下来呢我们通过代码的方式给大家呢去实现这个案例好打开我们的讲义在这里呢我们要做这个案例之前啊我们先要做一个准备工作什么准备工作呢比如说第一呢我们先要创建一个新的文件然后呢在这个文件中呢写一点数据也就是一些单词接下来
[00:28] 我们需要将这个文件上传到HDFS在HDFS里边建一个目录然后把这个文件放在这个目录下面好 接下来我们一步一步来去做首先我们进到Export Service在这里边我们要去建一个文件wordcount.tst接下来把这个文件的内容复制进去我再重新粘一下复制一下
[01:06] 好 粘贴保存退出接下来呢我们还要做一件事情需要将我们这个文件呢上传到HDFS上传之前呢首先呢需要在我们的根目录下面创建一个word count一个文件夹来 咱们来做HDFS DFS-MAKEDR在根目录下面创建word count好 稍等好 创建完之后呢
[01:37] 我们需要将这个文件上传到这个目录下面那就是hdfs dfs-put wordcount.txt上传到根目录下面的wordcount好稍等好上传完之后呢我们来看一下这个根目录下面你看是不是多了一个wordcount目录点一下进去里边呢有一个wordcount.txt好这个工作做完之后呢接下来我们就可以写程序了
[02:08] 怎么去写程序呢还是看我们刚才这个流程图在这个流程图呢一共有八个步骤那在这里呢有两个步骤呢需要我们重点去写这个代码第一呢是在map阶段在这个阶段呢我们需要去定义一个Mapper类其实这个Mapper类呢实际上是一个自定义的一个Mapper类我们需要去继承这个Mapper这个类然后重写呢这个里边的map方法在这个map方法里边呢
[02:37] 想办法将我们的K1和V1转成K2和V2好 这是MAP阶段还有一个地方需要我们重点去写呢是REDUCE阶段那我们呢需要去自定义一个REDUCER类也是继承一个类呢叫REDUCER重写REDUCE方法然后呢将我们的新的K2和V2转成了K3和V3来 接下来我们就重点呢来去写这两段代码那么首先呢我们要打开我们的ID
[03:06] 在这里呢我们先创建一个model创建一个model好这个里边呢我们点next在这里我写一个cndr idcast好我们来写个day03我们写的是map reduce然后word countokmap reduce word countnextok finish写完之后呢首先我们要做第一件事情我们要给它添加一个仓库的一些
[03:41] 价包的依赖Maven参考的价包依赖那我把上一次这个POM的插面中的文件呢这个内容呢直接复制过来好这个就从这个位置开始直接拷贝拷贝完之后直接粘到我们这个POM的插面中好让它引入价包好引入之后呢接下来呢我就先去建一个包吧在这里先建一个包这个包呢cn.itcast.mapreduce
[04:15] 好myReduce在这里面呢我们需要建三个类其实我们就要三个类第一个呢我们刚才说一个myPer类那就叫word count然后呢myPer还有一个类呢是我们的Reducer这地方呢我们来看word count Reducer那么老师不是两个类吗怎么还有一个类呢还有一个类呢是我们的主类也就是我们写在mint方法的一个类
[04:49] 比如说我们叫gelmanok是一个主类ok把这三个类呢先定义好好那到这里呢基本上我们把他的准备工作呢已经做好了那接下来我们就重点去写每一个类中的代码好我们先呢把这个停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
      hello,world,Hadoop
      world,hdfs
      Hadoop,java
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
      hello,world,Hadoop
      world,hdfs
      Hadoop,java
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
  - K3: hello, world, Hadoop, hdfs
  - V3: 2, 2, 2, 1

画面 8：
- 展示了 IntelliJ IDEA 中创建新模块的界面。
- 选择的模块类型为 "Maven"。
- 项目 SDK 为 "JDK 8.0_241"。
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

