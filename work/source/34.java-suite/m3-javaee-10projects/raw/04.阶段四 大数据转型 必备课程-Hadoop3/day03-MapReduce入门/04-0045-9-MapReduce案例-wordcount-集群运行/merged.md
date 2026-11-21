# 9-MapReduce案例-wordcount-集群运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\9-MapReduce案例-wordcount-集群运行【海量资源尽在 ubkz.com】.mp4
- 时长 7分5秒（音频 425s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在写完整个MapperReduce的代码之后接下来我们去测试我们的代码那怎么测试呢它的测试非常简单首先需要将我们这个module打成一个加包然后把这个加包上传到我们的集群上来去运行在去打成加包之前我们来打开这个POM的插面首先需要在这里加一个配置packing加这个表示我们的打包方式是加包好
[00:30] 做完这个之后呢接下来我们打开右边这个my one project在这里还要做一件事情那点一下这个test在这里点击这个这个意思呢就是我在打包的时候呢跳过测试代码的执行OK那这个时候呢我们来双击package稍等让它去打包好这时候已经打成了打完之后呢我们来看这里多了一个target目录我们需要将这个包呢
[01:06] 我直接放在桌面上桌面之后呢我们来上传到我们的Linux我进到这个Export Software这个目录我来去上传一下找到这个桌面好找到桌面之后呢我们来看D03OK把它添加一下添加完之后呢你可以对这个加包呢做一个重名在这里我就不做修改了那怎么去运行它呢这个命令叫Hadoop
[01:36] 后面跟上个加表示我要去运行加包那后面呢跟上这个加包的名字OK后面呢还要跟上这个主类的一个全路径类名什么是主类呢也就是我们的这个里边一个交门点右键有一个copy reference选中这个类然后呢粘贴他的全路径名就是包名加上这个类名来我们来直接运行稍等
[02:08] OK他开始执行我们的MapReduce他说呢启动了一个任务正在运行这个任务这是任务的一个编号好稍等这个运行呢需要消耗很多的CPU和内存大概运行时间呢得一二十秒OK这地方报错了我们来看一下我直接把它Ctrl加C先关掉这地方报了一个错误他说这个一个运行是异常他说呢这个
[02:36] class not found expression类没发现哪个类呢他说这个word count Mapper这个类没发现不对啊我们word count Mapper就是这个类啊我们在job门里边你看已经指定了这个Mapper我点一下进去可以啊为什么他没发现呢我再来看一下下面呢也是这个类没发现那什么原因呢是这个原因就是我们要打包放在集群上运行的时候呢
[03:06] 我们需要做一个配置就是打包放在集群运行时需要做一个配置那怎么配置呢这里面还是个job一个方法叫set加by class这个地方要指定啊你这个主类它的一个class对象我们要去把这个der class主类的class对象给它ok class对象这样做完之后呢应该就没有问题了
[03:43] 那这个时候呢我们再重新打一次吧双机械clean现在清除一下清除之后再重新打包好稍等好打包完成打包完成之后呢咱们来直接开始拷贝它放在桌面上替换然后呢再一次把这个上传一下我们呢这样我们把刚才那个先删掉RMD03-F直接删掉
[04:23] 再上传一次上传一次之后呢我们回到桌面还是这个好上传完之后呢咱们呢可以直接运行刚才的命令再来一次就是这条命令回车走来看看是否可以这地方又报错了他说呢这个输出目录已经存在了这是我们这个word count这个out已经存在了是因为我刚才运行的时候呢他给我们建了这个word count你要把它先删掉那怎么删呢我们用hdfs dfs
[04:57] 然后呢rm-r删一个word count然后呢-out把这个先删掉好删掉之后呢我们再来看看可不可以走再看这个任务是否能够完成再启动稍等一下好map0%reduce 0%好map100%map阶段已经完成了接下来该reduce了好这个时候你只要看到这些信息呢
[05:43] 就完成了OK Reduce 百分百好 这些是它的一些一些计数器输出的一些信息那我们来看一下这个结果记着我们这个案例呢是做单词统计如果没有问题的话呢它会在根目录下面呢创建一个目录叫 word count.out在这里边应该有个文件这个文件呢就是记录了每个单词出现的次数我们点一下进去你发现这里边有个刚 success这个是一个它的一个
[06:12] 一个教研文件不用管这被个part-200这就是我们要的最终的一个结果文件我们可以点开我们可以当一下来看一下好这里边呢我这边好多文件我们可以点开看一下完成时打开稍等打开走你看到没有这个文件里边是不是就是对我们原文件做的一个单词统计每个单词出现了多少次OK
[06:42] 到此为止呢我们这个word count案例呢就完成了我们也经过了验证了好这是一个非常基础性的一个word count案例这个案例也非常的重要基本上我们后面的案例呢都是在这个基础上呢做了一些改变或者做了一些增强好关于word count案例呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
            <groupId>org.apache.Hadoop</groupId>
            <artifactId>Hadoop-common</artifactId>
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
    11 hello, Hadoop
    23 world.hdfs
    33 Hadoop.java
```

画面 7：
```java
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.util.ToolRunner;

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
-rw-r--r-- itt Hadoop 20 B Apr 27 17:55 3 0 B test
```

画面 10：
```bash
[root@node01 software]# Hadoop jar day03_mapreduce_wordcount-1.0-SNAPSHOT.jar cn.itcast.mapreduce.JobMain
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
2 Hadoop 2
3 hello 2

