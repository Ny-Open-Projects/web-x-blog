# 画面线理解：13.编写Spark应用（代码优化）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\13.编写Spark应用（代码优化）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:26, 00:39, 00:52, 01:15, 01:31, 01:40, 01:54, 02:17, 02:37, 03:21, 03:50, 04:15, 04:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:25:56

1) 这一组画面整体在讲如何使用 Java API 实现 Spark 的 WordCount 程序，并展示代码编写、调试、运行及优化过程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 WordCountApp.java 文件的完整代码，包含读取文件、扁平化、映射、按 key 聚合、收集和打印结果等步骤，最后调用 jsc.stop() 关闭 Spark 上下文。
画面2: 代码聚焦在 flatMap 操作，将字符串按空格分割成单词数组。
画面3: 代码聚焦在 mapToPairRDD，将每个单词映射为 (单词, 1) 的键值对。
画面4: 代码聚焦在 reduceByKeyRDD，对相同单词的计数进行累加。
画面5: 代码聚焦在 collect() 操作，将结果收集到驱动程序并打印。
画面6: 代码聚焦在 for 循环，用于遍历 collect() 返回的列表并打印每个单词及其出现次数。
画面7: 代码聚焦在 collect().foreach() 操作，使用函数式编程风格打印结果。
画面8: 代码聚焦在运行时，显示程序正在使用 Java 1.8 运行。
画面9: 展示 pom.xml 文件内容，其中包含 Spark 核心依赖。
画面10: 代码聚焦在 jsc.stop()，用于关闭 Spark 上下文。
画面11: 代码聚焦在 SparkConf 配置，设置应用名称和本地模式。
画面12: 展示 Spark Web UI 界面，显示 Spark Master 地址和已完成的应用程序列表。
画面13: 代码聚焦在 reduceByKey 操作的实现，定义了累加器函数。
画面14: 展示优化后的 WordCountApp.java 代码，使用链式调用简化了操作。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面9: pom.xml 内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.spark</groupId>
    <artifactId>my-spark-test</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.12</artifactId>
            <version>2.4.3</version>
        </dependency>
    </dependencies>
</project>
```

画面11: SparkConf 配置代码：
```java
SparkConf sparkConf = new SparkConf()
    .setAppName("WordCountApp2") // 本地模式，并且使用cpu的内核数相同的线程数进行执行
    .setMaster("local[*]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
```

画面14: 优化后的代码：
```java
package cn.itcast.spark;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;
import java.util.Arrays;
import java.util.List;

public class WordCountApp {
    public static void main(String[] args) {
        // 设置 spark 配置文件信息
        SparkConf sparkConf = new SparkConf()
            .setAppName("WordCountApp") // 本地模式，所有任务的驱动
            .setMaster("local[*]"); // 本地模式，所有任务的驱动
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);

        // 读取文件
        JavaRDD<String> linesJavaRDD = jsc.textFile("F://code/word.txt");

        // 对文件中每一行单词进行下划线切分，并且按照空格切分，对相同单词进行累加
        List<Tuple2<String, Integer>> list = linesJavaRDD
            .flatMap(s -> {
                String[] ss = s.split(" ");
                return Arrays.asList(ss).iterator();
            })
            .mapToPair(s -> new Tuple2<>(s, 1))
            .reduceByKey((v1, v2) -> v1 + v2)
            .collect();

        // 打印结果
        list.forEach(obj -> System.out.println(obj._1() + " 出现的次数为：" + obj._2()));
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面9: PPT 标题为“Spark快速入门.md”，左侧目录结构包含“2.3 数据变量登录”、“2.4 开始安装”、“2.5 Spark HA 而可用部署”、“3. Spark角色介绍”、“4. 体验 Spark 程序”、“5. Spark架构”、“6. RDD概述”等章节。
画面12: Spark Web UI 界面显示 Spark Master 地址为 spark://itcast:7077，状态为 ALIVE，已完成的应用程序列表包含四个 Spark 应用，每个应用显示名称、核心数和内存使用量。

5) 无。
