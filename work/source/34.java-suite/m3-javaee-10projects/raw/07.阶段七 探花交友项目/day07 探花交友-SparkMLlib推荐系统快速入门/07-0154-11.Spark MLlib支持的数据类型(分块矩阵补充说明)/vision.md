# 画面线理解：11.Spark MLlib支持的数据类型（分块矩阵补充说明）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\11.Spark MLlib支持的数据类型（分块矩阵补充说明）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:40, 00:46, 00:51, 00:59, 01:17, 01:41, 02:08, 02:57, 03:04, 03:08, 03:15, 03:18, 03:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:40:34

1) 这一组画面整体在讲 Spark MLlib 中的分块矩阵（BlockMatrix）概念及其在矩阵运算中的应用，通过图形化网格和代码演示来说明。

2) 按时间顺序列出每张画面的要点：
画面1：在绘图软件中创建一个 3x3 的网格，作为矩阵的可视化基础。
画面2：在网格左上角的第一个单元格中输入坐标“(0.0)”。
画面3：在“(0.0)”右侧的单元格中输入坐标“(0.1)”。
画面4：在“(0.1)”右侧的单元格中输入坐标“(0.2)”。
画面5：在网格第二行第一个单元格中输入坐标“(1.0)”。
画面6：在 IntelliJ IDEA 中，显示了 Spark 项目结构和测试结果，终端输出了测试通过信息和矩阵元素“(1,2) 6.0”和“(4,5) 12.0”。
画面7：IntelliJ IDEA 中的测试结果窗口，显示测试通过，终端输出与画面6相同。
画面8：在绘图软件中，将“(1,0)”单元格中的值设为“6.0”，“(2,0)”单元格中的值设为“12.0”，并用红色字体显示。
画面9：画面8的延续，未做修改。
画面10：在 PicPick 图像编辑软件中，对画面8中的网格图像进行标注和调整。
画面11：在 Typora 中打开的 Spark MLlib 文档，显示了“1.2.4.4. 分块矩阵”章节，其中包含 Java 代码片段：
```java
public void testCoordinateMatrix() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("SparkMLlib")
        .setMaster("local[1]");
    JavaRDD<String> rdd = jsc.textFile("F:/code/files/a.txt");
    JavaRDD<Matrix> rdd = rdd.map(v -> {
        String[] ss = v.split(",");
        return new Matrix(Long.valueOf(ss[0]), Double.valueOf(ss[1]), Double.valueOf(ss[2]));
    });
    CoordinateMatrix matrix = new CoordinateMatrix(rdd.rdd());
}
```
画面12：Typora 文档中，代码继续执行分块矩阵转换：
```java
BlockMatrix blockMatrix = matrix.toBlockMatrix();
// 对分块矩阵进行迭代，确认该分块是否正确，如果正确则输出异常
blockMatrix.validate();
BlockMatrix addBlockMatrix = blockMatrix.add(blockMatrix); // 加法
List<Tuple2<Tuple2<Object, Object>, Matrix>> collect = addBlockMatrix.blocks().toJavaRDD().collect();
for (Tuple2<Tuple2<Object, Object>, Matrix> tuple2MatrixTuple2 : collect) {
    System.out.println(tuple2MatrixTuple2);
}
```
画面13：Typora 文档中，代码输出结果：
```java
((0,0),5 x 6 CSCMatrix
(1,2) 6.0
(4,5) 12.0)
```
画面14：Typora 文档中，代码输出结果与画面13相同，但显示的网格图中“(1,0)”单元格的值为“6.0”，“(2,0)”单元格的值为“12.0”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面11代码：
```java
public void testCoordinateMatrix() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("SparkMLlib")
        .setMaster("local[1]");
    JavaRDD<String> rdd = jsc.textFile("F:/code/files/a.txt");
    JavaRDD<Matrix> rdd = rdd.map(v -> {
        String[] ss = v.split(",");
        return new Matrix(Long.valueOf(ss[0]), Double.valueOf(ss[1]), Double.valueOf(ss[2]));
    });
    CoordinateMatrix matrix = new CoordinateMatrix(rdd.rdd());
}
```
画面12代码：
```java
BlockMatrix blockMatrix = matrix.toBlockMatrix();
// 对分块矩阵进行迭代，确认该分块是否正确，如果正确则输出异常
blockMatrix.validate();
BlockMatrix addBlockMatrix = blockMatrix.add(blockMatrix); // 加法
List<Tuple2<Tuple2<Object, Object>, Matrix>> collect = addBlockMatrix.blocks().toJavaRDD().collect();
for (Tuple2<Tuple2<Object, Object>, Matrix> tuple2MatrixTuple2 : collect) {
    System.out.println(tuple2MatrixTuple2);
}
```
画面13代码输出：
```java
((0,0),5 x 6 CSCMatrix
(1,2) 6.0
(4,5) 12.0)
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。
