# 画面线理解：10.Spark MLlib支持的数据类型（分块矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\10.Spark MLlib支持的数据类型（分块矩阵）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:59, 01:03, 01:09, 01:33, 01:50, 02:01, 02:49, 03:25, 03:31, 03:41, 03:51, 03:56, 04:16, 04:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:40:05

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark MLlib 中使用 CoordinateMatrix 转换为 BlockMatrix 并执行矩阵加法操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Java 代码，用于读取文件并创建 MatrixEntry 对象。
- 代码片段：
  ```java
  JavaRDD<String> fileRdd = jsc.textFile(path: "F:\\code\\files\\a.txt");
  JavaRDD<MatrixEntry> rdd = fileRdd.map(v -> {
      String[] ss = v.split(" ");
      return new MatrixEntry(Long.valueOf(ss[0]), Long.valueOf(ss[1]), Double.valueOf(ss[2]));
  });
  ```
- 画面中显示了测试通过的运行结果。

画面2：
- 展示了测试方法 `testCoordinateMatrix` 的代码，用于测试坐标矩阵转换。
- 代码片段：
  ```java
  @Test //测试分布式矩阵，坐标矩阵
  public void testCoordinateMatrix() {
      SparkConf sparkConf = new SparkConf().setMaster("local[*]").setAppName("TestMLlib");
      JavaSparkContext jsc = new JavaSparkContext(sparkConf);
      JavaRDD<String> fileRdd = jsc.textFile(path: "F:\\code\\files\\a.txt");
      JavaRDD<MatrixEntry> rdd = fileRdd.map(v -> {
          String[] ss = v.split(" ");
          return new MatrixEntry(Long.valueOf(ss[0]), Long.valueOf(ss[1]), Double.valueOf(ss[2]));
      });
  ```
- 画面中显示了测试通过的运行结果。

画面3：
- 展示了测试方法 `testCoordinateMatrix` 的代码，用于测试坐标矩阵转换。
- 代码片段：
  ```java
  @Test //测试分布式矩阵，坐标矩阵
  public void testCoordinateMatrix() {
      SparkConf sparkConf = new SparkConf().setMaster("local[*]").setAppName("TestMLlib");
      JavaSparkContext jsc = new JavaSparkContext(sparkConf);
      JavaRDD<String> fileRdd = jsc.textFile(path: "F:\\code\\files\\a.txt");
      JavaRDD<MatrixEntry> rdd = fileRdd.map(v -> {
          String[] ss = v.split(" ");
          return new MatrixEntry(Long.valueOf(ss[0]), Long.valueOf(ss[1]), Double.valueOf(ss[2]));
      });
  ```
- 画面中显示了测试通过的运行结果。

画面4：
- 展示了创建 CoordinateMatrix 对象的代码。
- 代码片段：
  ```java
  CoordinateMatrix coordinateMatrix = new CoordinateMatrix(rdd.rdd());
  ```
- 画面中显示了测试通过的运行结果。

画面5：
- 展示了 PPT 页面，标题为“1.3. RDD、DataSet、DataFrame区别及转化”。
- 画面中显示了代码片段：
  ```java
  CoordinateMatrix matrix = new CoordinateMatrix(rdd.rdd());
  //分块矩阵
  BlockMatrix blockMatrix = matrix.toBlockMatrix();
  //对每个分块矩阵进行检验，默认该分块矩阵是否正确，如果不正确会抛出异常
  blockMatrix.validate();
  BlockMatrix addBlockMatrix = blockMatrix.add(blockMatrix);
  List<Tuple2<Tuple2<Object, Object>, Matrix>> collect = addBlockMatrix.blocks().toJavaRDD().collect();
  for (Tuple2<Tuple2<Object, Object>, Matrix> tuple2MatrixTuple2 : collect) {
      System.out.println(tuple2MatrixTuple2);
  }
  ```
- 画面中显示了测试通过的运行结果。

画面6：
- 展示了代码片段：
  ```java
  coordinateMatrix.toBlockMatrix()
  ```
- 画面中显示了测试通过的运行结果。

画面7：
- 展示了代码片段：
  ```java
  blockMatrix.
  ```
- 画面中显示了测试通过的运行结果。

画面8：
- 展示了代码片段：
  ```java
  addBlockMatrix.
  ```
- 画面中显示了测试通过的运行结果。

画面9：
- 展示了代码片段：
  ```java
  addBlockMatrix.blocks().toJavaRDD()
  ```
- 画面中显示了测试通过的运行结果。

画面10：
- 展示了代码片段：
  ```java
  addBlockMatrix.blocks().toJavaRDD().collect()
  ```
- 画面中显示了测试通过的运行结果。

画面11：
- 展示了代码片段：
  ```java
  collect.forEach(tuple2MatrixTuple2 -> System.out.println(tuple2MatrixTuple2));
  ```
- 画面中显示了测试通过的运行结果。

画面12：
- 展示了代码片段：
  ```java
  collect.forEach(tuple2MatrixTuple2 -> System.out.println(tuple2MatrixTuple2));
  ```
- 画面中显示了测试通过的运行结果。

画面13：
- 展示了代码片段：
  ```java
  List<Tuple2<Tuple2<Object, Object>, Matrix>> collect = addBlockMatrix.blocks().toJavaRDD().collect();
  collect.forEach(tuple2MatrixTuple2 -> System.out.println(tuple2MatrixTuple2));
  ```
- 画面中显示了测试通过的运行结果。

画面14：
- 展示了 PPT 页面，标题为“1.2.4.4. 分块矩阵”。
- 画面中显示了代码片段：
  ```java
  @Test
  public void testCoordinateMatrix() {
      SparkConf sparkConf = new SparkConf().setMaster("local[*]").setAppName("TestMLlib");
      JavaSparkContext jsc = new JavaSparkContext(sparkConf);
      JavaRDD<String> rdd = jsc.textFile("F:\\code\\files\\a.txt");
      JavaRDD<MatrixEntry> rdd2 = rdd.map(v -> {
          String[] ss = v.split(" ");
          return new MatrixEntry(Long.valueOf(ss[0]), Long.valueOf(ss[1]), Double.valueOf(ss[2]));
      });
      CoordinateMatrix matrix = new CoordinateMatrix(rdd2.rdd());
      //转化得到分块矩阵
      BlockMatrix blockMatrix = matrix.toBlockMatrix();
      //对每个分块矩阵进行检验，默认该分块矩阵是否正确，如果不正确会抛出异常
      blockMatrix.validate();
  ```
- 画面中显示了测试通过的运行结果。
