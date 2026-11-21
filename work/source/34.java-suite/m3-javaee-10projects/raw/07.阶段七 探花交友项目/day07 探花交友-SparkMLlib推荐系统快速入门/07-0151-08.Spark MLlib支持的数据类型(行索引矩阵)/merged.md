# 08.Spark MLlib支持的数据类型（行索引矩阵）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\08.Spark MLlib支持的数据类型（行索引矩阵）_【海量资源尽在 666java.com】.mp4
- 时长 5分58秒（音频 359s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下行索引矩阵那么这个行索引矩阵呢其实就是在前面的我们的行矩阵的基础之上呢去增加这个索引这个功能那么接下来呢我们一起来看一下那我们就在之前这个代码的基础之上呢做一些这个改造那么就OK了那我们把这个代码呢就拷贝过来我们来改一下
[00:23] 然后我们可以看到我们接下来要测试的叫做什么行索引,索引矩阵那么我们在这个位置加一个什么index的是不是就去做这样的一个索引那么我们把下面这个就拿掉了不是使用的行矩阵而是什么使用的是index的来看一下那么index row matrix那么
[00:49] 我们是需要定义的一个是吧带索引的这样的一个行举证对不对好那我们去new一个它然后呢我们来看一下它的一个所需要的一个什么呢就是构造参数啊那我们来看一下啊那么这个构造参数呢它呢同样是一个rdd但是要注意呢它呢是需要一个对象叫什么呢index的row啊这样的一个对象而我们前面所提供这个rdd呢
[01:18] 它是一个vector这个对象那么显然是不匹配的所以我们还需要做进一步的处理我们需要把这个vector去转成它所需要的什么叫做index的law这样的一个对象我们来看一下怎么样去做操作我们同样还是去读取我们 a.txt这样的一个文件然后我们去做一个处理那么到这它其实已经
[01:46] 就完成了我们的一个这个行矩阵的一个输入对吧那我们接下来呢就来去来处理一下啊那我们还是去呃这样吧我们为了减血呢这个就来一只rdd1吧然后呢我们把这个rdd1呢做一个map的一个处理啊做一个map处理那我们这个就改成v吧呃然后呢我们来看一下这个里面怎么去实现呢我们就直接去
[02:15] new吧new一个什么呢它所需要的叫做什么呢index的row这样的一个对象那我们来看一下这个index row这个对象它也要有哪些这个参数呢那我们可以看到它需要有两个这个参数那么一个呢是index索引是一个浪类型那么另外一个呢就是这个vector那么这个呢是我们的vector对象那么我们就给它来做一个这个
[02:41] 输入那么第二个参数那就是这个V了对不对那么第一个参数我们需要给他去设置一个索引我们简单来做我们就直接使用我们这个V的一个set就可以了把这个封号好那么接下来我们来去拿到一个rddrdd2对吧然后拿到之后我们在这个位置就可以把它传递过来rdd2rdd2点什么
[03:08] 它所接受的是一个RDD并不是一个JavaRDD所以要从那个JavaRDD转成一个RDD好那么这样的话呢我们就拿到我们的一个什么呢这个叫行啊索引啊矩阵啊这样就拿到它了那么拿到它之后呢就可以做一些操作了那么首先呢我们其实可以去拿到它的一个行数和列数对吧那么我们来看一下它的一个number啊number rows
[03:37] 还有一个什么呢numbercolors然后呢这个是行数啊上面上面是行数下面这个是列数那么我们还可以通过什么呢通过它的一个方法叫做ros来拿到它的每一行这个数据啊那我们可以来看一下啊当然了它也可以直接转成普通的一个行举证啊那么也是可以的啊那么拿到一个这个ros
[04:04] 那么拿到ros之后呢其实我们就拿到他的一个这个rdd了那我们再去把它转成一个什么呢to吧to一个javardd这样的话我们会操作啊更加的一个方便比如说我们来一个rdd3吧rdd3那么接下来呢拿到这个之后呢我们就可以去啊拿到他的一做一个connect的操作拿到他的一些这个数据啊集合数据了那我们就可以去做一些这个便利了对吧
[04:32] 好那我们就来便利一下吧就是通过list吧点forEats然后呢通过一个Lamb的表达式去做一个输出了那么写一个indexindexZone这样的对象好那么接下来呢我们就来执行一下那么就可以打印他的一些行信息和列信息以及他的每行的一些数据的信息了OK好那我们来等待他的一个执行好那我们来看一下这个结果
[05:00] 那么在前面呢其实我们可以看到这个行信息是不是也就打印出来了对吧行列信息是不是打印出来了然后呢下面呢在这个位置是不是可以看到它呢是一个index的zo这样的一个对象那其中呢这个3呢是它的一个索引后面的123呢这个它的值然后呢这个3呢也是下一行的数据的一个索引而它呢就是它的一个值了那值呢是456
[05:28] 大家有东西说了这两个都是这个三吗那么当然了这个取决于你的这个数据啊取决于你的数据那么我们数据呢只有三个那么就是三了哎OK好那么其实这个呢就是给大家所讲的一个什么呢行索引的一个矩阵那么它相比较之前的这个行矩阵呢就是增加了一个索引了那么我们在这个位置呢就是用它的这个长度呢作为它的一个索引了哎OK好那么关于这个行索引矩阵呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  RowMatrix (org.apache.Spark.mllib.linalg.distributed)
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

