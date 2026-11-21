# 画面线理解：03.Spark MLlib支持的数据类型（本地向量集）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\03.Spark MLlib支持的数据类型（本地向量集）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:44, 01:32, 01:56, 02:23, 03:09, 04:05, 04:35, 04:59, 05:42, 06:35, 07:01, 09:37, 10:31, 11:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:35:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中使用 Spark MLlib 的 Vector 类创建并操作稠密向量和稀疏向量。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Spark MLlib 文档中“1.2. 支持的数据类型”章节，其中包含一个表格，列出了 Local vector、Labeled point、Local matrix、Distributed matrix 等类型及其定义。下方是引入 MLlib 依赖的 Maven 依赖配置。
画面 2: 展示了 Maven 依赖配置的完整内容，包括 <groupId>org.apache.spark</groupId> 和 <artifactId>spark-core_2.11</artifactId> 等。
画面 3: 展示了 IntelliJ IDEA 中的项目结构，包含 src/main/java 和 test/java 目录，以及 TestMLlib.java 文件。
画面 4: 展示了 TestMLlib.java 文件中定义的 @Test 方法 testDense()，用于测试稠密向量。
画面 5: 展示了 testDense() 方法中创建稠密向量的代码：Vector dense = Vectors.dense(3, 5, 2, 7); 并调用 apply(1) 获取下标为1的值。
画面 6: 展示了文档中“1.2.1.2. 稀疏型数据集”章节，包含 testSparse() 方法的代码示例，用于创建稀疏向量。
画面 7: 展示了 testSparse() 方法的代码，用于创建稀疏向量。
画面 8: 展示了 Vectors 类的 API 文档，包括 dense、sparse、fromJson 等方法。
画面 9: 展示了 testSparse() 方法中定义稀疏向量的代码，使用 Vectors.sparse(size, indices, values)。
画面 10: 展示了 testSparse() 方法中调用 sparse.apply(i) 获取指定下标值的代码。
画面 11: 展示了 testSparse() 方法中定义稀疏向量并打印下标2、3、4的值，运行结果为 2.0、7.0。
画面 12: 展示了 testSparse() 方法中定义稀疏向量并打印下标2、3、4的值，运行结果为 2.0、0.0、7.0。
画面 13: 展示了 testSparse() 方法中定义稀疏向量并打印下标2、3、7的值，运行结果为 2.0、0.0、0.0。
画面 14: 展示了文档中“1.2.2. 向量标签”章节，但画面中未显示具体代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-core_2.11</artifactId>
    <version>2.4.3</version>
</dependency>
```

画面 2:
```xml
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-core_2.11</artifactId>
    <version>2.4.3</version>
</dependency>
```

画面 3:
无代码，仅显示项目结构。

画面 4:
```java
@Test
public void testDense() {
```

画面 5:
```java
Vector dense = Vectors.dense(3, 5, 2, 7); //定义密集型数据集
double v = dense.apply(1); //根据下标获取值
System.out.println(v);
```

画面 6:
```java
@Test
public void testSparse() {
    int[] indexes = new int[]{1, 2, 3};
    double[] values = new double[]{9, 5, 2, 7};
    Vector sparse = Vectors.sparse(4, indexes, values); //定义稀疏型数据集
    System.out.println(sparse.apply(2)); //获取下标为2的值
    System.out.println(sparse.apply(3)); //获取下标为3的值
    System.out.println(sparse.apply(4)); //获取下标为4的值
}
```

画面 7:
```java
@Test
public void testSparse() {
```

画面 8:
```java
dense(double firstValue, double... otherValues)
dense(double[] values)
sparse(int size, Seq<Tuple2<Object, Object>> elements)
sparse(int size, Iterable<Tuple2<Integer, Double>> elements)
fromJson(String json)
fromML(Vector v)
fromFrozen(Vector v)
MAX_HASH_NNZ
```

画面 9:
```java
@Test
public void testSparse() {
    int[] indexes = new int[]{1, 2, 3};
    double[] values = new double[]{9, 5, 2, 7};
    Vector sparse = Vectors.sparse(4, indexes, values); //定义稀疏型数据集
```

画面 10:
```java
sparse.apply(2);
```

画面 11:
```java
@Test
public void testSparse() {
    int[] indexes = new int[]{1, 2, 3};
    double[] values = new double[]{9, 5, 2, 7};
    Vector sparse = Vectors.sparse(4, indexes, values); //定义稀疏型数据集
    System.out.println(sparse.apply(2)); //获取下标为2的值
    System.out.println(sparse.apply(3)); //获取下标为3的值
    System.out.println(sparse.apply(4)); //获取下标为4的值
}
```

画面 12:
```java
@Test
public void testSparse() {
    int[] indexes = new int[]{1, 2, 3};
    double[] values = new double[]{9, 5, 2, 7};
    Vector sparse = Vectors.sparse(4, indexes, values); //定义稀疏型数据集
    System.out.println(sparse.apply(2)); //获取下标为2的值
    System.out.println(sparse.apply(3)); //获取下标为3的值
    System.out.println(sparse.apply(4)); //获取下标为4的值
}
```

画面 13:
```java
@Test
public void testSparse() {
    int[] indexes = new int[]{1, 2, 3};
    double[] values = new double[]{9, 5, 2, 7};
    Vector sparse = Vectors.sparse(4, indexes, values); //定义稀疏型数据集
    System.out.println(sparse.apply(2)); //获取下标为2的值
    System.out.println(sparse.apply(3)); //获取下标为3的值
    System.out.println(sparse.apply(7)); //获取下标为7的值
}
```

画面 14:
无代码，仅显示文档标题“1.2.2. 向量标签”。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.2. 支持的数据类型”，表格内容如下：
| 类型名称 | 释义 |
| --- | --- |
| Local vector | 本地向量。主要向 Spark 提供一组可进行操作的数据集合 |
| Labeled point | 向量标签，让用户能够分类不同的数据集合 |
| Local matrix | 本地矩阵。将数据集合以矩阵形式存储在本地计算机中 |
| Distributed matrix | 分布式矩阵。将数据集合以矩阵形式存储在分布式计算机中 |

画面 6: PPT 标题为“1.2.1.2. 稀疏型数据集”，下方有代码示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
