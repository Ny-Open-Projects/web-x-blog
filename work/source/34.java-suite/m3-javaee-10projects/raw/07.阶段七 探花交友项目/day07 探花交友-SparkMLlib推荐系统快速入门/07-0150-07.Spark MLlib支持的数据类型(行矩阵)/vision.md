# 画面线理解：07.Spark MLlib支持的数据类型（行矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\07.Spark MLlib支持的数据类型（行矩阵）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:43, 02:01, 02:36, 03:15, 03:42, 04:52, 05:21, 06:15, 06:43, 07:11, 07:53, 08:34, 08:48, 09:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:38:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 Spark MLlib 的 RowMatrix 类，通过读取文本文件并转换为行矩阵进行数据处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程目录结构，当前在“1.2.4.1. 行矩阵”章节，代码编辑器中显示了创建 SparkConf、JavaSparkContext 并读取文本文件的代码片段。
画面 2: 代码编辑器中显示了测试方法 testMatrix() 的内容，其中创建了一个稠密矩阵并打印，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 3: 代码编辑器中显示了测试方法 testRowMatrix() 的定义，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 4: 代码编辑器中显示了 testRowMatrix() 方法的开头部分，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 5: 代码编辑器中显示了 SparkConf 类的 API 文档，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 6: 代码编辑器中显示了 testRowMatrix() 方法的完整代码，其中创建了 SparkConf、JavaSparkContext，并读取了文件 F:\code\files\a.txt，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 7: 代码编辑器中显示了 fileRDD.map() 方法的代码，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 8: 代码编辑器中显示了 fileRDD.map() 方法的代码，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 9: 代码编辑器中显示了 fileRDD.map() 方法的代码，其中对字符串进行分割并创建 double 数组，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 10: 代码编辑器中显示了 fileRDD.map() 方法的代码，其中对字符串进行分割并创建 double 数组，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 11: 代码编辑器中显示了 testRowMatrix() 方法的完整代码，其中将 RDD 转换为 RowMatrix，下方的测试运行结果为“Tests passed: 1 of 1 test - 999 ms”，输出为“1.0 3.0 5.0”。
画面 12: 代码编辑器中显示了 testRowMatrix() 方法的完整代码，其中打印了行矩阵的行数和列数，下方的测试运行结果为“Tests passed: 1 of 1 test - 882 ms”，输出为“1.0 3.0 5.0”。
画面 13: 代码编辑器中显示了 testRowMatrix() 方法的完整代码，下方的测试运行结果为“Tests passed: 1 of 1 test - 882 ms”，输出为“1.0 3.0 5.0”。
画面 14: 展示了课程目录结构，当前在“1.2.4.1. 行矩阵”章节，代码编辑器中显示了 testRowMatrix() 方法的完整代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public void testRowMatrix() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("SparkMLib")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> rdd1 = jsc.textFile("F:\\code\\files\\a.txt");
```

画面 2:
```java
@Test
public void testMatrix() {
    double[] values = new double[]{1, 2, 3, 4, 5, 6};
    Matrix matrix = Matrices.dense(numRows, numCols, values);
    System.out.println(matrix);
}
```

画面 3:
```java
@Test //测试分布式矩阵，行矩阵
public void testRowMatrix() {
    RowMatrix rowMatrix = new RowMatrix();
}
```

画面 4:
```java
@Test //测试分布式矩阵，行矩阵
public void testRowMatrix() {
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
}
```

画面 5:
```java
SparkConf sparkConf = new SparkConf()
    .setMaster("local[*]")
    .setAppName("TestMLlib");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
JavaRDD<String> fileRdd = jsc.textFile(path: F:\code\files\a.txt);
```

画面 6:
```java
@Test //测试分布式矩阵，行矩阵
public void testRowMatrix() {
    SparkConf sparkConf = new SparkConf().setMaster("local[*]").setAppName("TestMLlib");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    //读取文件
    JavaRDD<String> fileRdd = jsc.textFile(path: F:\code\files\a.txt);
    RowMatrix rowMatrix = new RowMatrix(fileRdd.rdd());
}
```

画面 7:
```java
fileRdd.map(v -> {
    double[] ds = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        ds[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(ds);
});
```

画面 8:
```java
fileRdd.map(v -> {
    double[] ds = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        ds[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(ds);
});
```

画面 9:
```java
fileRdd.map(v -> {
    String[] ss = v.split(regex: " ");
    double[] ds = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        ds[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(ds);
});
```

画面 10:
```java
fileRdd.map(v -> {
    String[] ss = v.split(regex: " ");
    double[] ds = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        ds[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(ds);
});
```

画面 11:
```java
//读取文件
JavaRDD<String> fileRdd = jsc.textFile(path: F:\code\files\a.txt);
JavaRDD<Vector> vectorJavaRDD = fileRdd.map(v -> {
    String[] ss = v.split(regex: " ");
    double[] ds = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        ds[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(ds);
});
RowMatrix rowMatrix = new RowMatrix(vectorJavaRDD.rdd());
```

画面 12:
```java
RowMatrix rowMatrix = new RowMatrix(vectorJavaRDD.rdd()); //行矩阵
System.out.println(rowMatrix.numRows()); //行数
System.out.println(rowMatrix.numCols()); //列数
```

画面 13:
```java
RowMatrix rowMatrix = new RowMatrix(vectorJavaRDD.rdd()); //行矩阵
System.out.println(rowMatrix.numRows()); //行数
System.out.println(rowMatrix.numCols()); //列数
```

画面 14:
```java
public void testRowMatrix() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("SparkMLib")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> rdd1 = jsc.textFile("F:\\code\\files\\a.txt");
    JavaRDD<Vector> vectorJavaRDD = rdd1.map(v -> {
        String[] ss = v.split(regex: " ");
        double[] ds = new double[ss.length];
        for (int i = 0; i < ss.length; i++) {
            ds[i] = Double.valueOf(ss[i]);
        }
        return Vectors.dense(ds);
