# 画面线理解：16.弹性分布式数据集RDD之常用算子操作（map）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\16.弹性分布式数据集RDD之常用算子操作（map）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:36, 02:02, 02:27, 02:56, 03:46, 04:32, 05:31, 06:30, 06:53, 08:00, 08:39, 09:22, 10:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:27:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写并运行一个 Spark Java 应用程序，重点是使用 map 操作对 RDD 进行转换。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Word 文档中关于 RDD 操作的讲解，包含 map 操作的 Scala 代码示例。
画面 2: 展示 Typora 中的 Spark RDD 常用算子操作文档，重点是 map 算子。
画面 3: 在 IntelliJ IDEA 中，展示创建 Maven 项目并编辑 pom.xml 文件，其中包含 Spark 依赖。
画面 4: 在 IntelliJ IDEA 中，展示项目结构和 pom.xml 文件，其中包含 Spark 依赖。
画面 5: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于 public void testMap() 方法的开头。
画面 6: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于 JavaSparkContext jsc 的声明处。
画面 7: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于创建 JavaRDD<Integer> rdd1 的代码行。
画面 8: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于 rdd1.map(new Function<Integer, Integer>() { ... }) 的代码行，弹出 Java 类型提示。
画面 9: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于 List<Integer> list = rdd2.collect(); 的代码行。
画面 10: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于 list.forEach(...) 的代码行，已添加 System.out.println(integer)。
画面 11: 在 IntelliJ IDEA 中，弹出“Create New Class”对话框，准备创建名为 MyFunction 的类。
画面 12: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于 rdd2 = rdd1.map(new MyFunction()); 的代码行。
画面 13: 在 IntelliJ IDEA 中，展示 RddOperation.java 文件，光标位于 rdd2 = rdd1.map(new MyFunction()); 的代码行，弹出 Java 类型提示。
画面 14: 展示 Typora 中的 Spark RDD 常用算子操作文档，重点是 map 算子。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 的 pom.xml 内容：
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.12</artifactId>
        <version>3.0.0</version>
        <scope>compile</scope>
    </dependency>
</dependencies>
```

画面 4 的 pom.xml 内容：
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.12</artifactId>
        <version>3.0.0</version>
        <scope>compile</scope>
    </dependency>
</dependencies>
```

画面 7 的代码：
```java
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
// 生成一个测试rdd数据集
JavaRDD<Integer> rdd1 = jsc.parallelize(Arrays.asList(1, 2, 3, 4, 5));
```

画面 8 的代码：
```java
rdd1.map(new Function<Integer, Integer>() {
    @Override
    public Integer call(Integer v1) throws Exception {
        return v1 * 2;
    }
});
```

画面 9 的代码：
```java
List<Integer> list = rdd2.collect();
```

画面 10 的代码：
```java
list.forEach(integer -> System.out.println(integer));
jsc.stop();
```

画面 12 的代码：
```java
JavaRDD<Integer> rdd2 = rdd1.map(new MyFunction());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2 和 14 的 PPT 标题：
6.3. RDD常用的算子操作
6.3.1. map
map是对RDD中的每个元素都执行一个指定的函数来产生一个新的RDD。任何原RDD中的元素在新RDD中都有且只有一个元素与之对应。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
