# 画面线理解：12.编写Spark应用（wordcount应用）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\12.编写Spark应用（wordcount应用）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:49, 01:47, 02:34, 03:25, 05:14, 06:45, 07:50, 09:13, 10:00, 11:01, 12:07, 12:41, 13:24, 14:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:25:23

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建一个 Spark Java 应用，并编写一个 WordCount 程序。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档“Spark快速入门1.md”，内容为“5.1、创建工程”，并展示 IntelliJ IDEA 的“New Project”窗口，用于创建新项目。
画面 2: 显示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 Maven 项目配置。
画面 3: 显示 EditPlus 编辑器界面，无具体内容。
画面 4: 显示 IntelliJ IDEA 中的 `pom.xml` 文件，光标在 `<version>2.4.1</version>` 行，弹出“Create New Class”对话框。
画面 5: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，代码开始编写 Spark 应用的主函数。
画面 6: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写读取文件的代码，`JavaRDD<String>` 类型。
画面 7: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `flatMap` 函数，弹出方法提示。
画面 8: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `flatMap` 函数的实现。
画面 9: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `mapToPair` 函数的实现。
画面 10: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `reduceByKey` 函数的实现。
画面 11: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `reduceByKey` 函数的实现，弹出方法提示。
画面 12: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `reduceByKey` 函数的实现。
画面 13: 显示 Typora 文档“Spark快速入门1.md”，内容为“5.2、编写WordCount程序”，并展示 `WordCountApp.java` 文件的代码结构。
画面 14: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，代码已编写完成，底部显示“Job 0 finished: collect at WordCountApp.java:50, took 0.956583 s”，表示程序执行成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.spark</groupId>
    <artifactId>my-spark-test</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面 4:
```xml
<version>2.4.1</version>
<dependency>
</dependency>
<build>
    <plugins>
        <!-- java编译插件 -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.1</version>
            <configuration>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

画面 5:
```java
package cn.itcast.spark;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaSparkContext;
class WordCountApp {
    public static void main(String[] args) {
        SparkConf sparkConf = new SparkConf()
                .setAppName("WordCountApp")
                .setMaster("local[*]");
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    }
}
```

画面 6:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
```

画面 7:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 8:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 9:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 10:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 11:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 12:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 13:
```java
package cn.itcast.spark;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import java.util.Arrays;
import java.util.List;
import java.util.Iterator;
public class WordCountApp {
    public static void main(String[] args) {
        //设置spark的配置文件
        SparkConf sparkConf = new SparkConf()
                .setAppName("WordCountApp")
                .setMaster("local[*]");
        //创建spark上下文对象，它是程序的入口，所有的操作都通过它来执行
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
        //读取文件
        JavaRDD<String> linesJavaRDD = jsc.textFile("F://code//word.txt");
        //对文件中每一行进行按空格切分，并且按照单词进行汇总
        List<Tuple2<String, Integer>> list = linesJavaRDD.flatMap(s -> {
            String[] words = s.split(" ");
            return Arrays.asList(words).iterator();
        }).map(s -> new Tuple2<>(s, 1)).reduceByKey((v1, v2) -> v1 + v2).collect();
        for (Tuple2<String, Integer> obj : list) {
            System.out.println(obj);
        }
    }
}
```

画面 14:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“5.1、创建工程”。
画面 13: PPT 标题为“5.2、编写WordCount程序”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
