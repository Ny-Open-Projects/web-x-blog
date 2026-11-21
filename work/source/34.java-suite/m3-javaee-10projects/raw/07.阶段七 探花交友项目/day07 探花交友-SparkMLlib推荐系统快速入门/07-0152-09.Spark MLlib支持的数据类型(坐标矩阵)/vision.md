# 画面线理解：09.Spark MLlib支持的数据类型（坐标矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\09.Spark MLlib支持的数据类型（坐标矩阵）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:54, 01:05, 01:29, 01:42, 02:13, 02:26, 02:59, 03:07, 03:31, 03:53, 04:01, 04:18, 04:26, 04:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:39:28

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
