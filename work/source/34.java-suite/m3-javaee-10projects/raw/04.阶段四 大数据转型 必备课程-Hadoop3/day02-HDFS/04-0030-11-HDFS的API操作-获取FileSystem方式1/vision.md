# 画面线理解：11-HDFS的API操作-获取FileSystem方式1

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\11-HDFS的API操作-获取FileSystem方式1【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:01, 01:21, 01:51, 02:56, 04:47, 07:09, 08:01, 09:30, 10:20, 10:42, 11:05, 11:52, 13:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:14:55

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Windows 系统中配置 Hadoop 环境并使用 Java API 获取 HDFS 的 FileSystem 对象。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 HDFS API 操作章节，列出在 Windows 系统配置 Hadoop 的四个步骤，其中第一步是将 apache-hadoop-3.1.1 文件夹解压到无中文空路径，第二步是设置 HADOOP_HOME 环境变量，第三步是将 hadoop.dll 放入 C:\Windows\System32，第四步是关闭 Windows 防火墙。
画面 2: 展示了 Maven 依赖配置，重点是添加 Hadoop 的 common、hdfs、hdfs-client 三个模块的依赖，版本号为 3.1.1。
画面 3: 展示了在 IDEA 中导入 Maven 项目，背景任务显示正在导入和更新索引。
画面 4: 展示了 Maven 依赖配置，重点是添加 Hadoop 的 common、hdfs、hdfs-client 三个模块的依赖，版本号为 3.1.1。
画面 5: 展示了获取 FileSystem 的两种方式，第一种方式是通过 Configuration 设置 fs.defaultFS，然后调用 FileSystem.get(configuration)。
画面 6: 展示了在 IDEA 中编写 Java 代码，提示需要导入 org.apache.hadoop.fs.FileSystem 包。
画面 7: 展示了在 Windows 系统中打开 C 盘，准备解压 Hadoop 文件。
画面 8: 展示了获取 FileSystem 的两种方式，第一种方式是通过 Configuration 设置 fs.defaultFS，然后调用 FileSystem.get(configuration)。
画面 9: 展示了在 IDEA 中编写 Java 代码，提示需要导入 org.apache.hadoop.fs.FileSystem 包。
画面 10: 展示了运行 Java 程序，输出了 FileSystem 的信息，显示了 HDFS 的连接信息。
画面 11: 展示了在 Windows 系统中打开 C 盘，准备解压 Hadoop 文件。
画面 12: 展示了运行 Java 程序，输出了 FileSystem 的信息，显示了 HDFS 的连接信息。
画面 13: 展示了 Hadoop 的源码，显示了 FileSystem 类的 get 方法的实现。
画面 14: 展示了运行 Java 程序，输出了 FileSystem 的信息，显示了 HDFS 的连接信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
第一步：将apache-hadoop-3.1.1文件夹解压到一个没有中文空路的路径下面
第二步：在windows上面配置hadoop的环境变量：HADOOP_HOME
第三步：把目录下的hadoop.dll文件放到系统盘里面去：C:\Windows\System32
第四步：关闭windows防火墙
```
画面 2:
```xml
<repositories>
    <repository>
        <id>cloudera</id>
        <url>https://repository.cloudera.com/artifactory/cloudera-repos/</url>
    </repository>
</repositories>
<dependencies>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-common</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-hdfs</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-hdfs-client</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面 3:
```
Importing Maven projects
Updating indices
Configuring Maven projects
```
画面 4:
```xml
<repositories>
    <repository>
        <id>cloudera</id>
        <url>https://repository.cloudera.com/artifactory/cloudera-repos/</url>
    </repository>
</repositories>
<dependencies>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-common</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-hdfs</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-hdfs-client</artifactId>
        <version>3.1.1</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面 5:
```java
@Test
public void getFileSystem1() throws IOException {
    Configuration configuration = new Configuration();
    //设置Configuration对象，设置的目的是来指定我们要操作的文件系统
    configuration.set("fs.defaultFS", "hdfs://node01:8020");
    //获取我们指定的文件系统，获取FileSystem就相当于获取了主节点中所有的元数据信息
    FileSystem fileSystem = FileSystem.get(configuration);
    System.out.println("fileSystem:"+fileSystem.toString());
}
```
画面 6:
```
new Con
```
画面 7:
```
Windows (C:)
```
画面 8:
```java
@Test
public void getFileSystem1() throws IOException {
    Configuration configuration = new Configuration();
    //设置Configuration对象，设置的目的是来指定我们要操作的文件系统
    configuration.set("fs.defaultFS", "hdfs://node01:8020");
    //获取我们指定的文件系统，获取FileSystem就相当于获取了主节点中所有的元数据信息
    FileSystem fileSystem = FileSystem.get(configuration);
    System.out.println("fileSystem:"+fileSystem.toString());
}
```
画面 9:
```
import org.apache.hadoop.fs.FileSystem;
import org.junit.jupiter.api.Test;
```
画面 10:
```
log4j:WARN No appenders could be found for logger (org.apache.hadoop.metrics2.lib.MutableMetricsFactory).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/fap.html#noconfig for more info.
fileSystem:DFSClient[clientName=DFSClient_NONMAPREDUCE_1851825033_1, ugi=lift (auth:SIMPLE)]
Process finished with exit code 0
```
画面 11:
```
Best (E:)
```
画面 12:
```
log4j:WARN See http://logging.apache.org/log4j/1.2/fap.html#noconfig for more info.
fileSystem:DFSClient[clientName=DFSClient_NONMAPREDUCE_1851825033_1, ugi=lift (auth:SIMPLE)]
Process finished with exit code 0
```
画面 13:
```java
if (scheme == null && authority == null) {
    return get(conf);
} else {
    if (scheme != null && authority == null) {
        URI defaultUri = getDefaultUri(conf);
        if (scheme.equals(defaultUri.getScheme()) && defaultUri.getAuthority() == null) {
            return get(defaultUri, conf);
        }
    }
}
String disableCacheName = String.format("fs.%s.impl.disable.cache", scheme);
if (conf.getBoolean(disableCacheName, false)) {
    LOGGER.debug("Bypassing cache to create filesystem {}", uri);
    return createFileSystem(uri, conf);
} else {
    return CACHE.get(uri, conf);
}
```
画面 14:
```
D:\develop\jdk8.0\bin\java ...
fileSystem:DFSClient[clientName=DFSClient_NONMAPREDUCE_352001840_1, ugi=lift (auth:SIMPLE)]
Process finished with exit code 0
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。
画面 8: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。
画面 12: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。
画面 14: PPT 标题为“1.9.3 获取 FileSystem 的几种方式”，内容包括“第一种方式”和“第二种方式”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
