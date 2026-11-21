# 18.弹性分布式数据集RDD之常用算子操作（flatMap）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\18.弹性分布式数据集RDD之常用算子操作（flatMap）_【海量资源尽在 666java.com】.mp4
- 时长 2分21秒（音频 142s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来看一下FlatMap那么这个FlatMap呢,它和这个Map呢是非常相似的啊那么它们的区别呢,其实就在于说我们之前的这个Map操作,它是在处理之后啊只能生成一个元素,就是每一个元素啊,只能生成一个而这个原有的RDD中呢,这个元素经过这个FlatMap操作之后呢可以生成多个元素来做
[00:28] 来构建新的一个RDD那么其实这个操作我们前面的也用过就是下面我们写这个例子那么我们来看一下那么这个例子呢其实就是我们去构造了一个RDD有两个我们的数据对吧一个是Hello World一个呢就是Hello Spark那么每一个这个句子中间呢都有一个空格那么下面呢我们通过这个FlatMap对它做一个这个操作之后呢我们就可以去
[00:58] 得到一个新的一个RDD而这个操作呢是我们把每一个这个S其实就代表着是不是每一个我们这个G做一个split然后拿到它的一个迭代器那么这样的话呢是不是原有的一个这个元素就会对应着有多个这个元素啊那么这个呢其实它就是和这个MAP操作的一个最大的一个区别当然了它们的相同点呢都是会对原有的元素
[01:27] 做每一个元素的一个逐一的一个处理那么这个我们就不去敲这个例子了因为前面我们在word count中也用过这样相似的这样的一个操作OK好那么大家可以把这个代码去拷贝到我们的测试用力中去运行一下那么下面我来给大家演示一下我们把这个代码来做一下拷贝然后丢到这个位置来然后我们去做一个
[01:55] 这种方法的一个处理好那么我们来等待它的一个执行好那么我们来看一下这个最后的一个执行结果那么就是这样的一个结果了那么我们来点一下在这那么可以看到是不是将我们之前的空格是不是做了这样的一个分割OK那么这个就是我们的flatmap的一个操作好那么关于这个flatmap操作就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Spark 中 flatMap 操作的代码实现、执行过程和结果输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示 Typora 文档，标题为“6.3.3. flatMap”，内容解释 flatMap 与 map 的区别。
- 代码示例：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator()); List<String> list = rdd2.collect(); for (String o : list) { System.out.println(o); } }

画面2：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFilter。
- 代码：JavaRDD<Integer> rdd2 = rdd1.filter(v1 -> v1 > 2); List<Integer> list = rdd2.collect(); list.forEach(integer -> System.out.println(integer)); jsc.stop();
- 控制台输出：3, 4, 5。
- 控制台日志显示 Spark 任务执行完成。

画面3：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFilter。
- 代码：JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(a -> Arrays.asList(a.split(" ")).iterator());
- 控制台日志与画面2相同。

画面4：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：.setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台日志与画面2相同。

画面5：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台日志与画面2相同。

画面6：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台日志与画面2相同。

画面7：
- 显示 IntelliJ IDEA，代码文件为 RddOperation.testFlatMap。
- 代码：.setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
- 控制台输出：hello, world, hello, Spark。
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
- 代码示例：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator()); List<String> list = rdd2.collect(); for (String o : list) { System.out.println(o); } }

画面11：
- 显示 Typora 文档，标题为“6.3.3. flatMap”，内容解释 flatMap 与 map 的区别。
- 代码示例：public void testFlatMap() { SparkConf sparkConf = new SparkConf().setAppName("RddOperation").setMaster("local[*]"); JavaSparkContext jsc = new JavaSparkContext(sparkConf); JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark")); JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator()); List<String> list = rdd2.collect(); for (String o : list) { System.out.println(o); } }

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
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
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
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark"));
JavaRDD<String> rdd2 = rdd.flatMap(a -> Arrays.asList(a.split(" ")).iterator());
```

画面4：
```java
.setMaster("local[*]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark"));
JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
```

画面5：
```java
public void testFlatMap() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark"));
    JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
```

画面6：
```java
public void testFlatMap() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark"));
    JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
```

画面7：
```java
.setMaster("local[*]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world", "hello Spark"));
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

