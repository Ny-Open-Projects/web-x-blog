# 画面线理解：9-MapReduce案例-wordcount-集群运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\9-MapReduce案例-wordcount-集群运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:54, 01:06, 01:56, 02:26, 02:54, 03:39, 04:24, 04:50, 05:13, 05:45, 05:57, 06:36, 06:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:55:27

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Hadoop 的 WordCount MapReduce 程序的开发、编译、打包、提交和结果查看全过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：在 IntelliJ IDEA 中打开项目 day03_mapreduce_wordcount，展示 pom.xml 文件内容，其中包含 Maven 依赖配置，如 <groupId>cn.itcast</groupId>、<artifactId>day03_mapreduce_wordcount</artifactId>、<version>1.0-SNAPSHOT</version>、<packaging>jar</packaging>，以及 <repository> 配置，指向 cloudera 的仓库。

画面 2：在 IDEA 的 Run 窗口中，执行 Maven 的 package 命令，输出日志显示正在构建项目 day03_mapreduce_wordcount 1.0-SNAPSHOT，编译成功。

画面 3：显示 Windows 操作系统的桌面，右键点击“此电脑”或“我的电脑”图标，弹出菜单，用于演示操作系统的操作。

画面 4：在 IDEA 中，项目结构显示构建成功，target 目录下生成了 jar 文件 day03_mapreduce_wordcount-1.0-SNAPSHOT.jar。

画面 5：在 Linux 系统的 SecureCRT 终端中，显示 Hadoop 任务提交失败的日志，错误信息为：java.lang.RuntimeException: java.lang.ClassNotFoundException: Class cn.itcast.mapreduce.WordCountMapper。

画面 6：在 IDEA 中，展示 WordCountMapper.java 文件内容，其中定义了 Map 方法，将输入的 K1 和 V1 转换为 K2 和 V2。

画面 7：在 IDEA 中，展示 JobMain.java 文件内容，其中设置了输入路径、输出路径和 Mapper 类。

画面 8：在 Linux 系统的 SecureCRT 终端中，执行解压命令，但弹出一个文件复制对话框，提示“文件复制失败”。

画面 9：在 Hadoop 的 Web UI 界面中，显示文件系统目录，包含多个文件，如 bigtxt.txt、hello.txt 等。

画面 10：在 Linux 系统的 SecureCRT 终端中，执行 Hadoop 命令，将 jar 文件上传到 HDFS 并提交任务。

画面 11：在 Linux 系统的 SecureCRT 终端中，显示 Hadoop 任务成功执行的日志，包括 map 和 reduce 阶段完成，以及文件系统计数器和作业计数器。

画面 12：在 Hadoop 的 Web UI 界面中，显示文件系统目录，与画面 9 相同。

画面 13：在 Windows 系统的 EditPlus 文本编辑器中，显示一个文本文件，内容为单词和出现次数的列表，如 "hello 2"、"world 2"。

画面 14：在 Windows 系统的画图程序中，展示 MapReduce 的流程图，包括 Map 阶段、Shuffle 阶段和 Reduce 阶段，以及各阶段的数据转换。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.itcast</groupId>
    <artifactId>day03_mapreduce_wordcount</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <repositories>
        <repository>
            <id>cloudera</id>
            <url>https://repository.cloudera.com/artifactory/cloudera-repos</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>3.1.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
```

画面 2：
```bash
INFO  Building day03_mapreduce_wordcount 1.0-SNAPSHOT
INFO  maven-resources-plugin:2.6:resources (default-resources) @ day03_mapreduce_wordcount --
WARNING Using platform encoding (UTF-8 actually) to copy filtered resources, i.e. build is platform dependent!
INFO  Copying 0 resource
INFO  maven-compiler-plugin:3.1:compile (default-compile) @ day03_mapreduce_wordcount --
```

画面 4：
```xml
<groupId>cn.itcast</groupId>
<artifactId>day03_mapreduce_wordcount</artifactId>
<version>1.0-SNAPSHOT</version>
<packaging>jar</packaging>
```

画面 5：
```bash
Error: java.lang.RuntimeException: java.lang.ClassNotFoundException: Class cn.itcast.mapreduce.WordCountMapper
```

画面 6：
```java
public class WordCountMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    map方法是将k1和v1转为k2和v2
    key：是v1
    value：是v2
    context：表示MapReduce上下文对象
    // K1 V1
    0 hello world
    11 hello, hadoop
    23 world.hdfs
    33 hadoop.java
```

画面 7：
```java
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.util.ToolRunner;

public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(getConf(), "mapreduce_wordcount");
        //第一步：设置读取文件的格式
        job.setInputFormatClass(TextInputFormat.class);
        //第二步：设置Mapper类
        job.setMapperClass(WordCountMapper.class);
        //第三步：设置输出格式
        job.setOutputFormatClass(TextOutputFormat.class);
        //第四步：设置Reducer类
        job.setReducerClass(WordCountReducer.class);
        //第五步：设置输出的key和value的类型
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);
        //第六步：设置输入和输出路径
        FileInputFormat.setInputPaths(job, new Path("hdfs://node01:8020/wordcount"));
        FileOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount_out"));
        //第七步：提交任务
        return job.waitForCompletion(true) ? 0 : 1;
    }
}
```

画面 8：
```bash
[root@node01 software]# rm day03_ma
[root@node01 software]# rz waiting to receive.
?A zmodem ??.
```

画面 9：
```html
Browse Directory
Show 25 entries
Permission Owner Group Size Last Modified Replication Block Size Name
-rw-r--r-- itt supergroup 0 B Apr 28 11:03 3 128 MB a.txt
drwxr-xr-x root supergroup 0 B Apr 28 16:58 3 0 B app
-rw-r--r-- root supergroup 194 B Apr 24 10:52 0 128 MB export
-rw-r--r-- itt hadoop 20 B Apr 27 17:55 3 0 B test
```

画面 10：
```bash
[root@node01 software]# hadoop jar day03_mapreduce_wordcount-1.0-SNAPSHOT.jar cn.itcast.mapreduce.JobMain
```

画面 11：
```bash
INFO  mapreduce.Job: Job job_1556425124335_0009 running in uber mode : false
INFO  mapreduce.Job: map 100% reduce 100%
INFO  mapreduce.Job: Job job_1556425124335_0009 completed successfully
File System Counters
FILE: Number of bytes read=197
FILE: Number of bytes written=43169
FILE: Number of read operations=0
FILE: Number of large read operations=0
FILE: Number of write operations=0
HDFS: Number of bytes read=178
HDFS: Number of bytes written=70
HDFS: Number of read operations=8
HDFS: Number of large read operations=0
Job Counters
Number of write operations=2
```

画面 13：
```text
1 flume 1
2 hadoop 2
3 hello 2
