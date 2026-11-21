# 04.Spark MLlib支持的数据类型（向量标签）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\04.Spark MLlib支持的数据类型（向量标签）_【海量资源尽在 666java.com】.mp4
- 时长 5分9秒（音频 310s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来看一下向量标签那么向量标签呢,它呢主要是用于我们的MLib中的机器学习的一些算法的做标记在分类问题中呢,我们可以将不同的数据呢去分成若干的份然后呢,给每一类这个数据呢去做一个标记比如说把它标记为是0,1,2这样的一个标记
[00:23] 那么我们举个例子呢就是说比如说我们去做这个邮箱的时候呢可能我们需要去标记哪些是垃圾邮件哪些是非垃圾邮件那我们就可以呢把这个垃圾邮件标记为1或者说非垃圾邮件标记为2这样的一个逻辑啊好那么接下来呢我们来看一下这个项链标签怎么去使用那么下面我们来看一下那么我们在这个位置呢还是来写一个测试用例啊比如说叫做public word
[00:52] test什么呢labellabel什么呢point然后呢我们去加一个什么呢test注解那么这个呢我们就在测试什么呢测试我们的一个项链标签标签好那么下面我们来看一下怎么去玩呢那么我们同样呢可以给我们的稀疏型的这个数据集呢去添加这个标签那么也可以给密集型的数据集呢去添加这个标签
[01:23] 那么首先呢我们先来测试谁呢先来测试我们的这个叫做密集型密集型的密集型的这个标签我们先来测试它那么我们把这个呢来靠一下就是我们定义了一个密集型的这样的一个数据集是9527接下来呢我们就来定义我们这个labelport那么我们去new一个这个labellabelport的对象
[01:52] 然后呢我们可以看到它有两个参数啊那么第一个这个参数呢就是给我们这个数据集去定一个标签那么你比如说呢我们把这个数据集的标签呢给它设置为1第二个呢就是我们这个数据集了那么我们这样的话呢我们这个向量的一个标签呢就已经定义好了那么这个就是我们的定义我们的一个向量的一个标签OK
[02:16] 好那我们来看一下这个如何去做使用呢比如说我们设置为这个LP啊LP呃然后呢我们去打印一些内容那么你比如说呢我们可以啊把它的这个label呢打印出来那么我们也可以把什么呢把它的啊这个啊Fields这个能打印出来就是Fields呢就代表着它的一些这个特征啊就是它的这个数据集了那么我们还可以去打印啊我们直接把这个LP打印出来吧
[02:44] 那么这个就它的一个什么呢打印打印它的一个标签那么下面这个呢就在打印它的一个这个特征特征其实就是它的一个数据集了然后呢这个呢就是把这个整个这个labport的对象呢去打印出来那么我们这个呢就不写了好那我们来执行一下吧然后呢走我们来看一下结果那么OK那么可以看到这样的一个结果呢就是
[03:13] 首先第一个这个1呢就代表着我们的一个标签就是说我们这么一堆啊这个数据啊它这个标签呢就是1然后呢这个就是我们的一个数据集然后下面这个打印呢就是我们数据集加我们这个标签啊整个对象呢打印出来了那么这个呢其实就是密集型的啊这个数据集所使用这个向量标签那么我们可以看到那么稀疏型的数据集能使用吗当然是可以使用的那么你比如说我们把这个呢拷过来对吧
[03:42] 这个就是我们前面所定义的我们这个一个稀疏型的一个数据集那么我们同样的也来给他定义一个什么的标签定义一个标签那么标签呢我们设置为二然后呢我们这个设置我们这个数据集这个呢也是在定义什么的定义我们的一个项链标签然后呢我们去给他去写一个什么的LP2吧LP2
[04:09] 好然后呢我们去把它的一些相关内容打印出来那么我们就直接打印这个对象然后呢再打印它的一些level那么还可以去打印什么呢它的一些这个特征了那么我们再来执行一下走那我们来看一下这个执行的一个结果那么我们其实可以看到呢在上面这个
[04:32] 这个打印啊我框起来这个打印呢其实就是我们刚刚所谓我们的这个西苏型的一个数据集呢去做一个打印那么其实可以看到呢这个它的一个标签为二这后面是所对应的它的一些数据啊那么这个标签为二啊这个是数据啊数据集哎OK好那么其实这个呢就是什么呢向量标签的一个使用那么就可以为我们前面所讲的这种向量集或者数据集呢去给它去干嘛呢去设置一些这个标签
[05:01] 那我们以后面就可以根据这个标签的去做一些这种分类了ok好那么关于这个向量标签那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.Spark;
import org.apache.Spark.mllib.linalg.Vector;
import org.apache.Spark.mllib.linalg.Vectors;
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

