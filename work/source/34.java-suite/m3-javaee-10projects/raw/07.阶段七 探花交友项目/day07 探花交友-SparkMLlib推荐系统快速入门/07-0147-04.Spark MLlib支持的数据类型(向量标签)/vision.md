# 画面线理解：04.Spark MLlib支持的数据类型（向量标签）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\04.Spark MLlib支持的数据类型（向量标签）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:45, 01:13, 01:37, 01:51, 02:23, 02:32, 03:07, 03:29, 03:39, 03:51, 04:10, 04:17, 04:22, 04:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:36:42

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 Spark MLlib 的 Vector 和 LabeledPoint 类来创建和操作稠密型、稀疏型向量以及带标签的样本数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 `testSparse()` 方法，用于创建并操作一个稀疏向量，其中定义了索引数组和值数组，并调用 `apply()` 方法获取指定索引位置的值。
画面 2: 展示了 `testLabeledPoint()` 方法的开始，准备定义一个带标签的样本。
画面 3: 展示了 `testDense()` 方法，用于创建一个稠密向量，并通过 `apply()` 方法获取指定索引位置的值。
画面 4: 展示了 `testLabeledPoint()` 方法的完整代码，其中创建了一个 `LabeledPoint` 对象，标签为 1，特征向量为稠密向量。
画面 5: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 6: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 7: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 8: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 9: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 10: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 11: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 12: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 13: 展示了 `testLabeledPoint()` 方法中创建 `LabeledPoint` 对象的代码，其中特征向量为稠密向量。
画面 14: 展示了 PPT 页面，标题为“1.2.2. 向量标签”，内容解释了向量标签在 MLlib 中用于标记样本，用于分类问题中区分不同类别，以整数 0、1、2 进行标记，例如：正类样本标记为 1，非正类样本标记为 0。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Test //测试稀疏型的数据集
public void testSparse(){
    int[] indexes = new int[]{0,1,5,9};
    double[] values = new double[]{9,5,2,7};
    Vector sparse = Vectors.sparse(size: 10, indexes, values); //定义稀疏型数据集
    System.out.println(sparse.apply(0));
    System.out.println(sparse.apply(2));
    System.out.println(sparse.apply(5));
    System.out.println(sparse.apply(7));
}
```

画面 3:
```java
package cn.itcast.spark;
import org.apache.spark.mllib.linalg.Vector;
import org.apache.spark.mllib.linalg.Vectors;
import org.junit.Test;

@Test
public void testDense(){
    Vector dense = Vectors.dense(firstValue: 9, ...otherValues: 5, 2, 7); //定义密集型数据集
    double v = dense.apply(1); //根据下标获取值
    System.out.println(v);
}

@Test //测试稀疏型的数据集
public void testSparse(){
    int[] indexes = new int[]{0,1,5,9};
    double[] values = new double[]{9,5,2,7};
    Vector sparse = Vectors.sparse(size: 10, indexes, values); //定义稀疏型数据集
    System.out.println(sparse.apply(0));
    System.out.println(sparse.apply(2));
    System.out.println(sparse.apply(5));
    System.out.println(sparse.apply(7));
}
```

画面 4:
```java
@Test //测试向量标签
public void testLabeledPoint(){
    //密集型标签
    Vector dense = Vectors.dense(firstValue: 9, ...otherValues: 5, 2, 7); //定义密集型数据集
    LabeledPoint lp = new LabeledPoint(label: 1, dense); //定义向量标签
    System.out.println(lp.label()); //打印标签
    System.out.println(lp.features()); //打印特征，数据集
    System.out.println(lp);
}
```

画面 6:
```java
@Test //测试向量标签
public void testLabeledPoint(){
    //密集型标签
    Vector dense = Vectors.dense(firstValue: 9, ...otherValues: 5, 2, 7); //定义密集型数据集
    LabeledPoint lp = new LabeledPoint(label: 1, dense); //定义向量标签
    System.out.println(lp.label()); //打印标签
    System.out.println(lp.features()); //打印特征，数据集
    System.out.println(lp);
}
```

画面 8:
```java
@Test //测试向量标签
public void testLabeledPoint(){
    //密集型标签
    Vector dense = Vectors.dense(firstValue: 9, ...otherValues: 5, 2, 7); //定义密集型数据集
    LabeledPoint lp = new LabeledPoint(label: 1, dense); //定义向量标签
    System.out.println(lp.label()); //打印标签
    System.out.println(lp.features()); //打印特征，数据集
    System.out.println(lp);
}
```

画面 10:
```java
@Test //测试向量标签
public void testLabeledPoint(){
    //密集型标签
    Vector dense = Vectors.dense(firstValue: 9, ...otherValues: 5, 2, 7); //定义密集型数据集
    LabeledPoint lp = new LabeledPoint(label: 1, dense); //定义向量标签
    System.out.println(lp.label()); //打印标签
    System.out.println(lp.features()); //打印特征，数据集
    System.out.println(lp);
}
```

画面 12:
```java
@Test //测试向量标签
public void testLabeledPoint(){
    //密集型标签
    Vector dense = Vectors.dense(firstValue: 9, ...otherValues: 5, 2, 7); //定义密集型数据集
    LabeledPoint lp = new LabeledPoint(label: 1, dense); //定义向量标签
    System.out.println(lp.label()); //打印标签
    System.out.println(lp.features()); //打印特征，数据集
    System.out.println(lp);
}
```

画面 14:
```java
1.2.2. 向量标签
向量标签用于MLlib中机器学习算法做标记。在分类问题中，可以将不同的数据集分成若干份，以整数0、1、2进行标记，例如：正类样本标记为1，非正类样本标记为0。
@Test
public void testLabeledPoint(){
    Vector vd = Vectors.dense(9, 5, 2, 7); //定义稠密向量
    LabeledPoint lp = new LabeledPoint(1, vd); //定义带标签的向量
    System.out.println(lp.features()); //打印特征
    System.out.println(lp.label()); //打印标签
    System.out.println("-------------");
}
int[] indexes = new int[]{0, 1, 2, 3};
double[] values = new double[]{9, 5, 2, 7};
Vector vd2 = Vectors.sparse(4, indexes, values); //定义稀疏型向量
LabeledPoint lp2 = new LabeledPoint(2, vd2); //定义带标签的向量
System.out.println(lp2.features()); //打印特征
System.out.println(lp2.label()); //打印标签
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
标题：1.2.2. 向量标签
内容：
- 向量标签用于MLlib中机器学习算法做标记。
- 在分类问题中，可以将不同的数据集分成若干份，以整数0、1、2进行标记，例如：正类样本标记为1，非正类样本标记为0。
- 代码示例：
  ```java
  @Test
  public void testLabeledPoint(){
      Vector vd = Vectors.dense(9, 5, 2, 7); //定义稠密向量
      LabeledPoint lp = new LabeledPoint(1, vd);
