# 11.Spark MLlib支持的数据类型（分块矩阵补充说明）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\11.Spark MLlib支持的数据类型（分块矩阵补充说明）_【海量资源尽在 666java.com】.mp4
- 时长 3分24秒（音频 205s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们把这个刚刚我们所看到这个结果呢给大家来解释一下可能有同学呢会对这个结果中的这个位置是可能会不太理解啊就是说我们当前这个矩阵它其实是一个五行六列的这样的一个矩阵那么为什么它是一个五行六列呢它其实和这个坐标是有关系的啊那我们可以来看一下画了这样的一个这个表格的这个图
[00:25] 那么在这个表格这个图里面呢其实我们要能够看懂它这样的一个矩阵啊那么比如说第一个这个方格呢其实它的一个坐标呢要注意它是0逗号0是这样的一个啊是这样的一个坐标而第二个呢就变成什么呢它的坐标就是01啊这样的一个坐标而这个第三个呢就是什么呢就是0逗号2这样的一个坐标而这个呢就是什么呢
[00:55] 这个就是1逗号0这样的一个坐标然后呢这个就是什么呢122逗号0这样的一个坐标这个大家应该能够理解吧2逗号0这样的坐标那么当然了其他的呢就类似了对吧其他就类似了那么我们可以看一下我们这个6这个数字啊那么它所在的坐标呢就是12这个坐标来我们来看一下在哪个位置啊1是不是就是在
[01:21] 哪个位置呢就是这个是01是不是x坐标啊是在这12说对的二是不是在这呀所以说我们这个66.0的这个数字呢啊把这个呃标标红一下吧标成这个哎就就这样吧
[01:38] 还标准红色那么这个就是我们6.0的这个数字所在的位置对吧那么同理我们这个12.0这个它所在的坐标是45那么所以它应该在哪里这个是不是应该是在这个位置对吧那么001234是不是在这那么5是012345是不是在这对吧那么所以这个应该就是
[02:05] 这个就是我们的12.0这样的一个数字的一个位置所以可以看一下我们整个这个行数是几行呢12345是不是五行列数呢是不是几列呢123456六列所以说最终的一个结果就是五行六列的这样的一个矩阵这个大家理解了吗其实呢还有一个小窍门的告诉大家呢就在这个位置就说那么我们这个矩阵的一个行列数
[02:35] 就等于你最后一个这个位置的这个它的坐标的这个横坐标和重坐标啊然后呢各加一就可以了比如这个就是4啊这个就是4加1是55加1呢是6啊五行六列啊这样的一个坐标了哎OK好那么这个呢我们就把之前的啊之前的这个结果呢给大家来补充一下那么我们可以把这个给大家截个图吧这个呢就是我们刚刚啊所看到的我们的这个结果啊
[03:06] 这个结果的一个说明那么往到下面来吧这个就是一个结果的一个说明OK好所以它是一个所以它是一个什么五行六列的这样的一个矩阵了OK好关于这个说明呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

