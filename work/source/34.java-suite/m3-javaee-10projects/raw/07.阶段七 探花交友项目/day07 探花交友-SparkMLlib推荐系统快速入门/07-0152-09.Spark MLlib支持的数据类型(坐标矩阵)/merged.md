# 09.Spark MLlib支持的数据类型（坐标矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\09.Spark MLlib支持的数据类型（坐标矩阵）_【海量资源尽在 666java.com】.mp4
- 时长 4分56秒（音频 296s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个坐标矩阵那么它的这个全称呢叫做什么Conordinate Matrix那么它呢是也是一个分布式的一个矩阵啊那么它的每一个这个条目呢都是由一个元组来组成的那么其中的包括三部分内容一部分呢是它的i和j那么就可以认为是它的一个坐标那么value呢就它的一个值
[00:28] 那么可以看到i呢是它的行的索引g呢是列的索引然后呢value呢是它的一个值那么只有在我们的矩阵的两个维度都很大的时候啊并且呢这是一个稀疏的一个矩阵的时候呢才应该去使用它啊这是它的一个使用的一个场景那么接下来呢我们就来看一下它如何去做一个使用呢那么我们还是呢去
[00:56] 把上面这个代码呢我们来做一个拷贝然后呢我们去把它呢去修改一下然后做一些测试好那么我们拷贝一下然后呢我们这个所测试的是什么呢是叫做坐标矩阵对不对好那么来写一下叫什么呢坐标矩阵下面呢我们把这个方法名呢来改一下
[01:20] 这个改成什么呢coordinate c o r d 啊然后呢这个coordinate matrix这个呢就是我们的一个坐标矩阵然后呢下面这个代码呢我们来调整一下那么先把这个呢我们先把它删除掉然后呢我们定义一个什么呢coordinate matrix啊那我们来看一下它呢是需要有哪些参数那么我们就给它去提供哪些参数啊就可以了那么我们来看一下它的一个构造的一个参数那么
[01:48] 他需要呢也是一个rdd对吧但是他需要的是一个matrix entity那么这个呢跟我们之前所构建这个index的row是不是又不一样了所以说我们需要去再给他来构建一下啊那么这个我们是不是就啊不需要他了然后呢在这个位置啊那我们最终其实可以返回谁呢就可以了啊是不是返回那个什么matrix entity对吧
[02:14] matrixedit那就是下面的这个了它对吧我们去new一个这个对象那么我们来看一下它需要什么我们给它提供什么就好了那我们来看一下在这那么我们可以看到它是不是需要有三个这个参数一个是ilong类型一个是j一个是value对吧那么我们来看一下如何给它去做一个提供呢那我们读取到我们的数据是不是我们有三列
[02:41] 那我们是不是可以把它第一列作为它的一个i第二列作为一个j那第三列呢作为它的一个值做这样的一个隐私啊那我们就不需要这个操作了对不对就不需要去转它了那我们就这么来玩那么第一个呢是none类型那么none.valueof ss0然后呢第二个呢也是none类型.什么的valueof然后呢ss1那么第三个要注意了
[03:11] 第三个呢是double类型对吧那么double.valueof然后呢来一个ss什么呢2哎ok好那么这样的话呢我们就已经构造完成了把这个范型呢来改一下那我们把这个rdd啊这个去掉那么就来一个这个rdd吧rdd然后呢转成一个rdd哎ok那么这样的话呢我们就已经构建好一个什么呢我们的一个坐标坐标的一个矩阵
[03:39] 下面呢我们就来尝试的去获取它里面的一些这个atrix就实体那么我们通过这个通过我们这个坐标矩阵呢就可以拿到它的一个atrix然后呢我们去把它再转成一个什么呢转成一个什么呢Java的一个rdd然后呢我们再来一个connector那么这样的话是不是就可以得到它的一个集合了对不对那我们就用它吧
[04:07] 然后呢我们是不是对它呢就可以去做一个便利了对吧那么我们就直接写这个connector.forEach然后呢我们通过Lamb的表达式呢去做一个输出做一个输出这样的话呢就拿到它的值了对不对好那我们来执行一下看一下这个效果好那么我们来看一下执行的结果呢是这样的就是那我们可以看到那么这两个是不是就是我们的坐标的一个矩阵对吧你可以看到
[04:37] 这个他们的这个坐标是不是1和2那么3呢这个是他的一个值那么45认为是他的一个坐标然后呢6呢是他的一个值哎OK好那么这个呢其实就是我们这个坐标矩阵的一个使用哎OK好那么关于这个坐标矩阵那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spark MLlib 的 CoordinateMatrix 类来处理和操作分布式矩阵数据。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示测试方法 testIndexedRowMatrix 的代码，其中创建了 IndexedRowMatrix 并打印其行数和列数，然后将 RDD 转换为 JavaRDD 并遍历打印每个 IndexedRow。
代码：
@Test
public void testIndexedRowMatrix() {
    JavaRDD<IndexedRow> rdd2 = rdd1.map(v -> new IndexedRow(v.size(), v));
    IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
    System.out.println(indexedRowMatrix.numRows());
    JavaRDD<IndexedRow> rdd3 = indexedRowMatrix.rows().toJavaRDD();
    List<IndexedRow> list = rdd3.collect();
    list.forEach(indexedRow -> System.out.println(indexedRow));
}

画面2：
要点：展示 SparkConf 初始化代码，设置应用名称和 Master 为本地模式，然后创建 JavaSparkContext。
代码：
SparkConf sparkConf = new SparkConf().setAppName("SparkMLlib").setMaster("local[1]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);

画面3：
要点：展示读取文件并转换为 Vector 的代码，以及创建 IndexedRowMatrix 的部分代码。
代码：
JavaRDD<Vector> rdd1 = fileRdd.map(v -> {
    String[] ss = v.split(regex);
    double[] ds = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        ds[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(ds);
});

画面4：
要点：展示创建 CoordinateMatrix 的代码，以及 IDE 中的类成员提示。
代码：
CoordinateMatrix coordinateMatrix = new CoordinateMatrix(...);

画面5：
要点：展示创建 CoordinateMatrix 的代码，以及 IDE 中的类成员提示。
代码：
CoordinateMatrix coordinateMatrix = new CoordinateMatrix(...);

画面6：
要点：展示 CoordinateMatrix 的源码，其中定义了 MatrixEntry 类和 CoordinateMatrix 类的注释。
代码：
case class MatrixEntry(i: Long, j: Long, value: Double)
/**
 * Represents a matrix in coordinate format.
 * @param entries matrix entries. A non-positive value means unknown, and then the number of rows will be determined by the max row index plus one.
 * @param nRows number of rows.
 * @param nCols number of columns.
 */

画面7：
要点：展示创建 MatrixEntry 的代码，以及 IDE 中的 Long 类方法提示。
代码：
return new MatrixEntry(Long.valueOf(ss[0]), Long.valueOf(ss[1]), Double.valueOf(ss[2]));

画面8：
要点：展示创建 MatrixEntry 的代码，以及 IDE 中的 String 类方法提示。
代码：
return new MatrixEntry(Long.valueOf(ss[0]), Long.valueOf(ss[1]), Double.valueOf(ss[2]));

画面9：
要点：展示创建 CoordinateMatrix 的代码，以及 IDE 中的 CoordinateMatrix 类方法提示。
代码：
CoordinateMatrix coordinateMatrix = new CoordinateMatrix(rdd);

画面10：
要点：展示创建 CoordinateMatrix 的代码，以及 IDE 中的 CoordinateMatrix 类方法提示。
代码：
CoordinateMatrix coordinateMatrix = new CoordinateMatrix(rdd);

画面11：
要点：展示调用 entries() 方法获取矩阵条目。
代码：
coordinateMatrix.entries();

画面12：
要点：展示调用 entries().toJavaRDD().collect() 方法获取矩阵条目列表。
代码：
coordinateMatrix.entries().toJavaRDD().collect();

画面13：
要点：展示使用 collect().forEach() 方法遍历并打印每个 MatrixEntry。
代码：
List<MatrixEntry> collect = coordinateMatrix.entries().toJavaRDD().collect();
collect.forEach(matrixEntry -> System.out.println(matrixEntry));

画面14：
要点：展示 PDF 文档中关于 CoordinateMatrix 的说明，以及对应的测试代码。
代码：
@Test
public void testCoordinateMatrix() {
    SparkConf sparkConf = new SparkConf().setAppName("SparkMLlib").setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> rdd1 = jsc.textFile("F:\\code\\files\\a.txt");
    JavaRDD<MatrixEntry> rdd2 = rdd1.map(v -> {
        String[] ss = v.split(regex);
        return new MatrixEntry(Long.valueOf(ss[0]), Long.valueOf(ss[1]), Double.valueOf(ss[2]));
    });
    CoordinateMatrix matrix = new CoordinateMatrix(rdd2.rdd());
    List<MatrixEntry> collect = matrix.entries().toJavaRDD().collect();
}

3) 无。

4) 无。

5) 无。

