# 07.Spark MLlib支持的数据类型（行矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\07.Spark MLlib支持的数据类型（行矩阵）_【海量资源尽在 666java.com】.mp4
- 时长 9分12秒（音频 552s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个行矩阵那么行矩阵呢它是最基本的一种矩阵的类型那么行矩阵呢其实顾名思义啊就是以行作为我们的一个基本的一个方向的一个矩阵的一个存储的一个格式那么列的作用呢相对啊较小啊相对较小那么我们可以把它理解成呢行矩阵是一个巨大的一个这个特征向量的一个集合
[00:28] 而每一行呢就是一个具有相同格式的一个项量的一个数据那么且每一行的项量内容呢都可以单独的取出来进行操作那么这样的一种矩阵呢就叫什么呢行矩阵啊那么接下来呢我们就通过代码演示的方式呢来做一个演示那么接下来呢我们首先呢创建一个文件那么这个文件的名字呢叫做A.txt当然了这个文件名呢可以随意那么文件中的内容呢是有这样的一个内容
[00:58] 就是有两行这个数据123256那么分别呢有三列每一行之间呢有一个空格去做一个分割那么接下来呢我们把这个文件呢去做一个读取然后呢把它转化成一个行举证哎OK好那么接下来呢我们来操作一下那么我们找到呃我们的这个我的这个呃code下面有一个fails目录然后呢在这个fails目录中呢我们去创建一个A点text
[01:26] 那么我们来创建一个文本吧然后呢去创建一个它然后呢把它呢去存储到哪里呢存储到这个code下面有一个fails下面呢有一个这adian text然后呢这个文本类型呢就是这样的text而编码呢改成这个utf-8这样的一个编码下面呢我们把这个内容呢就拷贝过来
[01:51] 有两行这样的一个数据那么接下来呢我们就来进行编码来去读取这个文件啊去转化成一个行举证那么我们写一个测试用力然后呢test什么呢叫做raw matrix然后呢我们来看一下怎么样去写这个测试用力呢那么我们来写下这个测试什么呢测试我们的这个分布分布是
[02:19] 矩阵中的什么呢横矩阵矩阵好那么接下来来看一下代码怎么写呢首先呢我们先去看一下这个rawmatrix这样的一个对象然后呢去new一个这个rawmatrix那么它需要什么一样的一些参数呢我们可以看一下啊那么它是需要一个什么呢是不是需要一个rdd啊
[02:45] 那么所以呢接下来呢我们是不是就需要通过Spark去读取我们刚刚所创建的这个A.txt文件然后呢才能得到这个RDD啊对不对那么前面其实我们也说到过就是我们的分布式矩阵它的存储是存储在哪里呢是不是一个或者是多个这个RDD中所以呢在这个位置显然呢就需要通过Spark去读取这个文件了
[03:12] 那我们需要呢来定义一个叫做java的一个Spark的contactor对象gsc然后呢去new一个啊这个对象然后呢需要一个配置对不对所以呢我们定义一个叫做什么呢Spark啊Spark什么呢呃然后呢config啊config然后呢写一个Spark config等于new一个Spark config
[03:39] 然后呢我们去给他设置一些参数对吧set一个什么呢master然后呢就是local然后呢是一个c然后呢再set一个什么呢app name那么我们就写一个什么呢就写我们那个测试用力吧叫test什么呢ml liveok好那么写这样的一个config那么传递到这个里面来是不是就得到一个gsc了那么接下来我们就需要什么呢去
[04:09] 读取啊去读取我们的一个文件那么通过这个jsc点什么呢点text fill然后去做一个读取文件呢是在我的F盘下面有一个code目录下面有一个什么呢fails然后下面有一个a.txt这样的一个文件去做个读取那么它读取了之后呢就会变成一个什么呢我们的一个这个fail吧
[04:38] 叫做Fill的一个RDD这样的一个对象那么我们就需要去把它是不是去传递过来来看一下行不行呢显然是不可以对不对它需要什么呢它需要的是一个RDD对象看对吗也并不是为什么呢我们来看一下那么其实我们可以看到它所需要的一个类型是一个RDD没错但是RDD中所存储的并不是一个字符创
[05:07] 而是什么呢而是我们那个Vector那么所以说呢我们需要还需要对它做一个我们的一个转化那么怎么样转化呢这样来做一个转化那么通过这个fail 而滴滴点什么呢做一个map的一个操作对吧那我们对每一行的数据呢做一个操作做什么操作呢我们来看一下它的具体的一个操作那么在前面呢其实我们提到过它所存储的是一个什么呢双精度浮点形的这样的一个
[05:37] 那么也就是说我们现在读到的是一个我们的一个文本对吧是不是就是一个这个字符串对吧我们需要转成一个double所以说我们应该这么来玩首先呢我们需要对我们的拿到的这一行数据呢按照空格是不是去做一个分割对吧做一个分割那么我们来看一下那么就比较叫SS那么分割之后呢我们需要去便利我们这个数组中的每一个这个
[06:06] 我们的一个数字然后把它转成一个double类型那么所以说呢我们还需要去干嘛呢我们还需要定义一个什么呢double类型的一个数组我们定义到下面来啊这个double类型double类型的一个数组比如说叫ds吧等于什么呢等于new一个double类型的一个数组长度呢它和我们前面的这个就是字部串就是空格
[06:37] 进行Split之后的长度呢是一样的接下来呢我们需要对它呢去做一个便利啊便利就叫什么呢forfor i因为我们需要使用这个下标然后呢i呢小于谁呢是不是ss.length这样的一个操作然后呢接下来呢我们就需要给我们这个ds呢去填充这个值
[07:03] 它就等于什么呢是不是我们写一个double.valueof去转一下转谁呢ss这个i这个操作大家能看懂吗就是需要对每一个这个字数字的一个这样的一个字符串去做一个double类型的一个转化最后呢是不是就可以得到一个这个double类型的啊这样的一个这个数组了那么最后呢我们就可以做一个return了return什么呢这个vector然后呢来一个什么呢dense
[07:33] 然后呢给他设置一个谁呢我们的一个DS这样的话呢我们是不是得到一个vector对象了那么他所接收到的那就一个是一个什么呢是不是我们的一个叫做vector吧然后呢这个rdd啊加把rdd然后呢把它呢就可以转成一个这个rdd啊这样的话呢我们就构造完成我们的一个什么呢叫做我们的一个行举证对吧哎行举证
[07:59] 好那么接下来呢我们就可以把我们这个行举证的一些他的一些这个信息呢打印出来比如说我们打印他的一些这个行数和什么呢和这个列数和这个列数列数啊好那么这个是他的行数行数啊下面这个什么呢列列数啊哎OK好那我们来执行一下好那我们来等待他的一个执行
[08:33] 好那么执行结果呢就已经出来了我们来看一下那我们其实可以看到它的一个输出呢是这样的就是哎呃二对吧那么第一个这个输出代表的行数是二那么第二个输出呢是劣数那就是三那就跟我们所预期的是不一样那么这个是不是就是我们的一个这个行举证啊哎呀OK好那么呃
[08:57] 那么我们来看一下那么最终跟我们在讲义中所看到的结果是不是一样那么这个就是我们的行数这个就是我们的一个列数OK好嘞好那么关于我们的这个行举这呢先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

