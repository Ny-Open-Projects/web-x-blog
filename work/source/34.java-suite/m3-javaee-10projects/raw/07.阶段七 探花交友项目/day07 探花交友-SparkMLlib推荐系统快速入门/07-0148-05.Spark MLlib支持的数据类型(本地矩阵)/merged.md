# 05.Spark MLlib支持的数据类型（本地矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\05.Spark MLlib支持的数据类型（本地矩阵）_【海量资源尽在 666java.com】.mp4
- 时长 2分35秒（音频 155s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下本地矩阵那么我们在做大数据计算的时候呢那我们很多时候呢会用到矩阵的这种方式呢来处理我们的一些数据啊那么其实这样做呢也是为了去提升一些计算的效率那么我们比如说我们在部署在单机中的一些本地矩阵呢那么就是可以存储的我们一些这种结果的数据的
[00:26] 那么我们可以举个例子比如说呢我们去有这样的一个数组就是13456啊这样的一个数组那我们就可以把它分成两行三列啊这样的一个矩阵那么就方便我们这个处理了那么可以看到最终结果呢就会有这样的一个这个结果哎OK好那么接下来呢我们就来写这个代码我们来测试一下那么我们打开我们的idea然后呢下面我们去写一个测试用例呃test metric
[00:56] Rix然后呢我们去写一个什么呢test这个是我们测试我们的什么的本地矩阵好那么接下来我们来看一下这个矩阵应该怎么样定义呢那么我们通过matrix然后呢去做一个构建有这个est这个matrix然后呢我们先去通过一个test来去做一个构建
[01:22] 那么第一个参数呢那么就是我们的一个行的一个数量啊然后呢第二个参数就是列的一个数量比如两行三列那么第三个参数呢就是我们的一个value的值数组或者说我们的数据那我们定义一个这个double的一个数组是我们的一个values它呢就等于new一个double然后呢我们这个里面写一个123456
[01:51] 这是我们的一个数据然后呢我们把这个数据呢去转成我们的一个本地的这样的一个矩阵那我们来看一下这个矩阵啊然后呢我们就可以把这个矩阵呢去打印出来了哎OK这个其实就是我们的一个本地的矩阵了好来看一下它的一个结果啊那么其实呢我们就可以看到
[02:13] 这个结果呢就是我们把我们之前的一个这个数据集呢我们已经把它转成一个本地的一个矩阵两行三列啊这样的一个矩阵可以看到是不是有三列啊哎OK好那么其实这个呢就是我们啊所讲的一个本地矩阵哎OK好那么关于这个本地矩阵呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 Spark MLlib 的 LabeledPoint 和 Matrix 类创建和操作稠密向量、稀疏向量及矩阵，并通过单元测试验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 TestMLlib.java 文件中定义稠密向量和 LabeledPoint 的代码，以及运行结果，输出了稠密向量和 LabeledPoint 的内容。
画面2：在代码中注释“密集型标签”，并高亮显示了创建稠密向量和 LabeledPoint 的代码。
画面3：在代码中高亮显示了 Java 的访问修饰符（private, protected, public, default）。
画面4：在代码中高亮显示了 Java 的内置类（如 Void, Boolean, Double 等）。
画面5：在代码中高亮显示了 Java 的包（如 java.lang, java.util 等）。
画面6：在代码中高亮显示了 Java 的类（如 Matrix, Vector, LabeledPoint 等）。
画面7：在代码中高亮显示了 Java 的方法（如 diag, srand, rand, sprand 等）。
画面8：在代码中高亮显示了 Java 的类（如 Double, DataOutput, DataOutputStream 等）。
画面9：在代码中高亮显示了 Java 的类（如 short, super, switch 等）。
画面10：在代码中高亮显示了 Java 的类（如 Matrix, Matrices, Double 等）。
画面11：在代码中高亮显示了 Java 的类（如 Matrix, Matrices, Double 等）。
画面12：在代码中高亮显示了 Java 的类（如 Matrix, Matrices, Double 等）。
画面13：在代码中高亮显示了 Java 的类（如 Matrix, Matrices, Double 等）。
画面14：展示了一个 PPT 页面，标题为“1.2.3. 本地矩阵”，内容包括本地矩阵的定义、示例代码和运行结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
Vector dense = Vectors.dense(firstValue: 9, ...otherValues: 5, 2, 7); //定义密集型数据集
LabeledPoint lp = new LabeledPoint(label: 1, dense); //定义向量标签
System.out.println(lp.label()); //打印标签
System.out.println(lp.features()); //打印特征，数据集
System.out.println(lp);

int[] indexes = new int[]{0,1,5,9};
double[] values = new double[]{9,5,2,7};
Vector sparse = Vectors.sparse(size: 10, indexes, values); //定义稀疏型数据集
```

画面4：
```java
int[] indexes = new int[]{0,3,5,9};
double[] values = new double[]{9,5,2,7};
Vector sparse = Vectors.sparse(size: 10, indexes, values); // 定义稀疏型数据集
LabeledPoint lp2 = new LabeledPoint(label: 2, sparse); // 定义向量标签
System.out.println(lp2.label());
System.out.println(lp2.features());
```

画面6：
```java
@Test //测试本地矩阵
public void testMatrix() {
```

画面7：
```java
@Test //测试本地矩阵
public void testMatrix() {
    double[] values = new double[]{1, 2, 3, 4, 5, 6};
    Matrix mx = Matrices.dense(2, 3, values);
    System.out.println(mx);
}
```

画面14：
```java
@Test
public void testMatrix() {
    double[] values = new double[]{1, 2, 3, 4, 5, 6};
    Matrix mx = Matrices.dense(2, 3, values);
    System.out.println(mx);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
标题：1.2.3. 本地矩阵
内容：
- 大数据运算中，为了更好地提升计算效率，可以更多地使用矩阵运算处理数据。
- 静态矩阵就是一个很好的存储方法。
- 例如一个数组Array (1,2,3,4,5,6)，将其分为2行3列的矩阵：
```java
@Test
public void testMatrix() {
    double[] values = new double[]{1, 2, 3, 4, 5, 6};
    Matrix mx = Matrices.dense(2, 3, values);
    System.out.println(mx);
}
```
运行结果：
```
1.0 3.0 5.0
2.0 4.0 6.0
```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

