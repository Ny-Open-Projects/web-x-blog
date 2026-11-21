# 画面线理解：08.Spark MLlib支持的数据类型（行索引矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\08.Spark MLlib支持的数据类型（行索引矩阵）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:38, 00:46, 01:33, 02:03, 02:24, 03:07, 03:36, 04:01, 04:25, 04:39, 04:52, 05:06, 05:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:38:59

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark MLlib 中使用 IndexedRowMatrix，包括创建、获取行列数、转换为 JavaRDD<IndexedRow> 并收集数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示代码中创建 RowMatrix，调用 numRows() 和 numCols() 方法获取行数和列数。
画面2：在代码中高亮显示 RowMatrix 的 numRows() 和 numCols() 方法，注释说明其含义。
画面3：在代码中高亮显示 IndexedRowMatrix 类的定义，展示其继承关系和构造函数。
画面4：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。
画面5：在代码中高亮显示 RowMatrix 的返回类型和相关类。
画面6：在代码中高亮显示 IndexedRowMatrix 的源码，展示其 case class 定义和注释。
画面7：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。
画面8：在代码中高亮显示 IndexedRowMatrix 的 numCols() 方法，展示其返回类型。
画面9：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。
画面10：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。
画面11：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。
画面12：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。
画面13：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。
画面14：在代码中高亮显示 IndexedRowMatrix 的构造函数，展示其参数类型。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
RowMatrix rowMatrix = new RowMatrix(vectorJavaRDD.rdd());
System.out.println(rowMatrix.numRows()); //行数
System.out.println(rowMatrix.numCols()); //列数
```

画面2：
```java
RowMatrix rowMatrix = new RowMatrix(vectorJavaRDD.rdd());
System.out.println(rowMatrix.numRows()); //行数
System.out.println(rowMatrix.numCols()); //列数
```

画面3：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix();
```

画面4：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
```

画面5：
```java
return
  RowMatrix (org.apache.spark.mllib.linalg.distributed)
  RuntimeException (java.lang)
  Runtime (java.lang)
  Runnable (java.lang)
  Readable (java.lang)
  ReflectiveOperationException (java.lang)
  RuntimePermission (java.lang)
  Random (java.util)
```

画面6：
```java
case class IndexedRow(index: Long, vector: Vector)
```

画面7：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
```

画面8：
```java
numCols()
long
void
```

画面9：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
System.out.println(indexedRowMatrix.numRows());
System.out.println(indexedRowMatrix.numCols());
```

画面10：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
System.out.println(indexedRowMatrix.numRows());
System.out.println(indexedRowMatrix.numCols());
```

画面11：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
System.out.println(indexedRowMatrix.numRows());
System.out.println(indexedRowMatrix.numCols());
```

画面12：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
System.out.println(indexedRowMatrix.numRows());
System.out.println(indexedRowMatrix.numCols());
```

画面13：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
System.out.println(indexedRowMatrix.numRows());
System.out.println(indexedRowMatrix.numCols());
```

画面14：
```java
IndexedRowMatrix indexedRowMatrix = new IndexedRowMatrix(rdd2.rdd());
System.out.println(indexedRowMatrix.numRows());
System.out.println(indexedRowMatrix.numCols());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
