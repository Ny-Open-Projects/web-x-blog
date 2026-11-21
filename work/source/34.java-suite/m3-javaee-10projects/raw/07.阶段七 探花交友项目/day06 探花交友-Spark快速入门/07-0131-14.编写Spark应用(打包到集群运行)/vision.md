# 画面线理解：14.编写Spark应用（打包到集群运行）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\14.编写Spark应用（打包到集群运行）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:56, 01:48, 03:31, 04:03, 05:04, 05:49, 06:16, 06:56, 08:38, 09:36, 10:11, 11:10, 11:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:26:36

1) 这一组画面整体在讲如何在集群中打包并运行一个基于 Spark 的 Java WordCount 应用程序。

2) 按时间顺序列出每张画面的要点：
画面1：在 Typora 中查看课程笔记，内容为“5.3.1. 修改pom文件”，并展示了修改后的 pom.xml 文件内容，其中 Spark Core 依赖版本为 2.4.3。
画面2：在 IntelliJ IDEA 中展示项目结构，选中 pom.xml 文件，显示其内容，其中 Spark Core 依赖版本为 2.4.3，且 scope 为 provided。
画面3：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，正在设置 SparkConf 并创建 JavaSparkContext，读取本地文件。
画面4：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，将文件路径从硬编码改为从命令行参数 args[0] 读取。
画面5：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，实现 flatMap 操作，按空格分割字符串。
画面6：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，实现 mapToPair 操作，将单词映射为 (单词, 1) 的元组。
画面7：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，实现 reduceByKey 操作，对相同单词的计数进行累加。
画面8：在 Xshell 中登录到 Spark 集群的节点，查看本地文件夹，确认 spark-2.4.3-bin-hadoop2.7.tgz 文件存在。
画面9：在 Xshell 中执行 tar -zxvf 命令解压 Spark 安装包。
画面10：在浏览器中打开 Spark Master 的 Web UI，显示集群状态为 Standby，无运行或已完成的应用。
画面11：在 EditPlus 中编写 spark-submit 命令，用于提交 WordCount 应用到 Spark 集群。
画面12：在 Xshell 中进入 Spark 的 bin 目录，列出可执行命令。
画面13：在 Xshell 中执行 spark-submit 命令，提交 WordCount 应用，并在终端中查看输出结果。
画面14：在 Typora 中查看课程笔记，内容为“5.3.2. 修改代码”，并展示了 WordCountApp.java 的代码结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.12</artifactId>
        <version>2.4.3</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面2：
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.12</artifactId>
        <version>2.4.3</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面3：
```java
public static void main(String[] args) {
    SparkConf sparkConf = new SparkConf()
        .setAppName("WordCountApp");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> fileRdd = jsc.textFile(path: "F:/code/word.txt");
    JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
        @Override
        public Iterator<String> call(String s) throws Exception {
            String[] ss = s.split(regex: " ");
            return Arrays.asList(ss).iterator();
        }
    });
```
画面4：
```java
JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(regex: " ");
        return Arrays.asList(ss).iterator();
    }
});
```
画面5：
```java
JavaPairRDD<Object, Integer> mapToPairRdd = flatMapRdd.mapToPair(new PairFunction<String, Object, Integer>() {
    @Override
    public Tuple2<Object, Integer> call(String s) throws Exception {
        return new Tuple2<>(s, 1);
    }
});
```
画面6：
```java
JavaPairRDD<Object, Integer> reduceByKeyRdd = mapToPairRdd.reduceByKey(new Function2<Integer, Integer, Integer>() {
    @Override
    public Integer call(Integer v1, Integer v2) throws Exception {
        return v1 + v2;
    }
});
```
画面7：
```java
// 保存结果到指定的目录或文件
reduceByKeyRdd.saveAsTextFile(args[1]);
```
画面11：
```bash
./spark-submit --master spark://node1:7077 --class cn.itcast.spark.WordCountApp3 /itcast/my-spark-test-1.0-SNAPSHOT.jar itcast/word.txt itcast/wc
```
画面13：
```bash
19/04/18 13:11:40 INFO ShutdownHookManager: Deleting directory /tmp/spark-bf747d11-6790-4ce2-82b2-f4844aa6a06b
[root@itcast spark]# cd /itcast/
[root@itcast itcast]# ll
总用量 8
-rw-r--r-- 1 root root 28 4月 18 13:11 part-00000
-rw-r--r-- 1 root root 21 4月 18 13:11 part-00001
-rw-r--r-- 1 root root 0 4月 18 13:11 _SUCCESS
[root@itcast itcast]# cat part-00000 part-00001
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“5.3.1. 修改pom文件”。
画面14：PPT 标题为“5.3.2. 修改代码”。

5) 不要评价画面美观，不要输出与课程无关的内容。
