# 画面线理解：18.弹性分布式数据集RDD之常用算子操作（flatMap）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\18.弹性分布式数据集RDD之常用算子操作（flatMap）_【海量资源尽在 666java.com】.mp4
- 抽帧：11 帧 @ 01:42, 01:49, 01:51, 01:53, 01:55, 01:58, 02:00, 02:06, 02:07, 02:15, 02:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:29:25

1) 这一组画面整体在讲什么（一句话）：
演示 Spark 中 flatMap 操作的代码实现、执行过程和结果输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示 Typora 文档，标题为“6.3.3. flatMap”，内容解释 flatMap 与 map 的区别。
- 代码示例：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator()); List<String> list = rdd2.collect(); for (String o : list) { System.out.println(o); } }

画面2：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFilter。
- 代码：JavaRDD<Integer> rdd2 = rdd1.filter(v1 -> v1 > 2); List<Integer> list = rdd2.collect(); list.forEach(integer -> System.out.println(integer)); jsc.stop();
- 控制台输出：3, 4, 5。
- 控制台日志显示 Spark 任务执行完成。

画面3：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFilter。
- 代码：JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(a -> Arrays.asList(a.split(" ")).iterator());
- 控制台日志与画面2相同。

画面4：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：.setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台日志与画面2相同。

画面5：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台日志与画面2相同。

画面6：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台日志与画面2相同。

画面7：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：.setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台输出：hello, world, hello, spark。
- 控制台日志显示 SparkContext 成功停止。

画面8：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 运行结果：Tests passed: 1 of 1 test (15 s 863 ms)。
- 显示测试通过。

画面9：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 控制台日志显示 Spark 任务执行过程，包括 TaskSetManager、Executor 等组件的启动和完成。
- 日志显示任务完成，SparkContext 停止。

画面10：
- 显示 Typora 文档，标题为“6.3.3. flatMap”，内容解释 flatMap 与 map 的区别。
- 代码示例：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator()); List<String> list = rdd2.collect(); for (String o : list) { System.out.println(o); } }

画面11：
- 显示 Typora 文档，标题为“6.3.3. flatMap”，内容解释 flatMap 与 map 的区别。
- 代码示例：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator()); List<String> list = rdd2.collect(); for (String o : list) { System.out.println(o); } }

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
@Test
public void testFlatMap() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
    // 数据压缩操作
    JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
    //收集数据
    List<String> list = rdd2.collect();
    for (String o : list) {
        System.out.println(o);
    }
}
```

画面2：
```java
JavaRDD<Integer> rdd2 = rdd1.filter(v1 -> v1 > 2);
List<Integer> list = rdd2.collect();
list.forEach(integer -> System.out.println(integer));
jsc.stop();
```

画面3：
```java
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark"));
JavaRDD<String> rdd2 = rdd.flatMap(a -> Arrays.asList(a.split(" ")).iterator());
```

画面4：
```java
.setMaster("local[*]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark"));
JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
```

画面5：
```java
public void testFlatMap() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark"));
    JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
```

画面6：
```java
public void testFlatMap() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark"));
    JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
```

画面7：
```java
.setMaster("local[*]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello spark"));
JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
```

画面8：
- 无代码。

画面9：
```text
19/08/12 22:58:14 INFO TaskSetManager: Starting task 0.0 in stage 0 (TID 0, local)
19/08/12 22:58:14 INFO Executor: Running task 0.0 in stage 0 (TID 0, local)
19/08/12 22:58:14 INFO Executor: Finished task 0.0 in stage 0 (TID 0, local)
19/08/12 22:58:14 INFO TaskSetManager: Finished task 0.0 in stage 0
