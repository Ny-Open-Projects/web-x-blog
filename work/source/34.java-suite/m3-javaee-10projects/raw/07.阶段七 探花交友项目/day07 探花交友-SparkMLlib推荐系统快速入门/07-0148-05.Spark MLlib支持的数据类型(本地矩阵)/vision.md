# 画面线理解：05.Spark MLlib支持的数据类型（本地矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\05.Spark MLlib支持的数据类型（本地矩阵）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:47, 00:51, 00:52, 01:09, 01:13, 01:17, 01:19, 01:38, 01:40, 02:02, 02:03, 02:06, 02:07, 02:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:37:13

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
