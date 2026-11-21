# 10.Spark MLlib支持的数据类型（分块矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\10.Spark MLlib支持的数据类型（分块矩阵）_【海量资源尽在 666java.com】.mp4
- 时长 4分48秒（音频 289s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下分块矩阵那么分块矩阵呢叫做block matrix它呢是支持我们矩阵去做分块的这样的一个分布式的一个矩阵那么它是由这样的一个结构去组成的那么什么结构呢整体来看呢是两部分那么第一部分呢是一个这个int int这样的一个结构那么第二个呢是matrix而前面这个int int这样的一个结构呢
[00:29] 是指的是我们这个举证所处的举证的一个索引的一个位置啊而matrix呢就表示在这个位置上面的一个指的一个举证那么这个分块式举证呢它是支持这种加法和这个乘法的并有一些这个辅助的函数呢去用于去检验这个分块式举证是否是正确的那么接下来呢我们来看一下如何去
[00:58] 去使用这个分块式这个矩阵那么我们把上面这个呢来做一个拷贝然后呢我们去做一些这个修改那么其实呢这个分块这个矩阵呢它呢就可以直接由这个坐标矩阵来转换得到啊那我们来看这个叫什么呢叫做分块分块分块矩阵那么我们这个改成什么呢block好那么这个呢就是一个分块矩阵
[01:30] 那么它如何去通过一个坐标矩阵去转成一个分块矩阵呢我们一起来看一下那么它是通过什么呢就通过这个matrix然后呢去to一个什么blockmatrix就可以得到一个块矩阵分块矩阵那么也就是说那么我们可以通过前面所写的这个什么呢坐标矩阵直接去做一个转换点什么呢
[01:59] to一个block一个matrix那么这样的话我们其实就得到一个什么呢分块矩阵OK那么这个就是我们去转化转化得到一个分块矩阵那么有了这个分块矩阵之后呢我们可以去通过它的比如说它提供了一个validator一个校验的方法这个是什么呢校验我们的这个分块是否正确
[02:27] 如果不正确的话如果不正确会抛出异常啊会抛出异常当然了如果正确的话那当然就不会抛出异常了那么接下来呢我们就可以通过我们这个分块矩阵呢去做一些操作比如说前面我们提到过啊它是不是支持了这种加法和乘法的操作比如说呢我们做一个这个按的操作啊相加比如说我把我自身这这个
[02:57] 这个矩阵的分块矩阵的做一个相加这个操作那我们来看一下那么比如说这个我们就叫按着什么block按着这个block matrix叫它那么这个就是两个矩阵是吧两个两个这个矩阵相加这样的一个操作那么接下来我们就可以去拿到这个矩阵中的一些一些这个
[03:26] 内容了比如说blocks那它的所有的分货然后呢我们再去再去什么呢to一个java的一个rdd然后呢我们再去做一个我们的一个这个connector就可以拿到它所有的这个内容了那我们接下来呢我们去得到它的一个connector那么下面呢我们做一个便利那么通过这个connector点什么呢for each然后呢
[03:54] 去把它呢直接就打印出来那我们来看一下它这个结果啊是什么样的一个结果呢好那我们来运行一下走让我们等待它的一个执行那么我们可以看到这个结果呢就是在这个位置对吧那么显然呢这两个结果呢可以看到因为我们刚刚做了一个什么操作啊是不是做了一个这个相加的这个操作对吧那么我们可以看到之前它的值是不是三对吧然后相加之后说变成了六
[04:24] 然后呢下面这个呢是不是就变成了12对吧以之前的数字呢是123对吧然后呢456然后相加呢是12哎OK那么其实这个呢就是我们啊给大家所讲的这个分块这个矩阵那么它呢是由我们之前的这个坐标矩阵呢就可以直接来转化得到这样的一个分块矩阵了哎OK好嘞好那么关于这个分块矩阵那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

