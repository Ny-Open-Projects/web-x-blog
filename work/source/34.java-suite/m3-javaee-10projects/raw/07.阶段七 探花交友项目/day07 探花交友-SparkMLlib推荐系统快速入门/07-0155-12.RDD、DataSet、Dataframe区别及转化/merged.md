# 12.RDD、DataSet、Dataframe区别及转化

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\12.RDD、DataSet、Dataframe区别及转化_【海量资源尽在 666java.com】.mp4
- 时长 13分1秒（音频 781s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下这个RDD还有DataSet还有DataFrame它们的区别以及它们之间的转化那么我们首先呢需要去了解一下那么在Spark整个这个版本发展的过程中它会经历了这么几个发展的阶段那么我们知道RDD呢是Spark非常重要的一个这样的一个概念那么但是随着Spark的版本的发展呢它其实也是发生了一些改变的
[00:29] 那么在早期的时候呢Spark 1.0的时候那么主要呢使用的就是这个RDD啊这样的一个这个API或者说这样的一个概念那么随着Spark的版本的一个升级的话后面呢对于这种使用的需求的一个升级的话那么会出现新的一些API来取代了一些这个老的API那么我在Spark 1.3的时候呢
[00:55] 就出现了有叫什么date frame这样的一个API那么有了date frame这个API之后呢并不是说RDD这个API就不能使用了那么它只是对RDD做了一些这个升级做了一些升级那么也就是说date frame处于更高级的这样的一个位置而RDD呢是属于比较偏底层的这样的一个位置
[01:21] 那么随着Spark的版本继续的一个升级的话那么到了Spark 1.6版本的时候呢又出现了DataSet那么又对之前的DataFrame又做了进一步的这个升级那么接下来呢我们就是需要给大家来演示一下啊这个DataSet它的一些这个使用啊因为在我们现在使用的2.0版本中呢这个在Java API中呢
[01:48] 这个DataFrame和DataSet的统一的都是使用DataSet所以说我们就直接来看DataSet的一个使用了当然了RDD也是可以去使用的因为在前面我们使用的过程中都是使用这个RDD来做一个这个API的一个编写那么下面我们就来看一下那么Spark Circle所提供的这个DataFrame和DataSet的一个数据的一个抽象
[02:12] 那么DataFrame就是RDD加一个Scammer去形成这样的DataFrame那么我们可以认为它是一张二维表那么它的一个劣势就在于什么呢编译器不对表格中的字段进行做一个类型的检查而是在运行期间去做一个检查那么DataSet是Spark最新的一个数据的抽象而Spark的发展会逐步的将DataSet作为主要的一个数据的抽象
[02:42] 而弱化RDD和DataFrame那么这个其实也是现在我们所看到的一个这样的一个情况那么DataSet呢包含了DataFrame所有的优化的机制那么除此之外呢提供了以样例类啊为Scam模型的一些强力型它是这样的一些这个描述说明啊那么接下来呢我们就以代码的形式呢来给大家演示一下我们如何去使用这个新的这个API
[03:10] 那么接下来呢我们来做一个演示啊那么首先呢我们先创建一个类啊student这个类这个类中呢有三个这个属性一个是id一个是name一个是age啊这三个好那么分别呢它的类型呢是lang类型和字符刷类型和什么呢和我们的int类型那么接下来呢我们就把这个类呢来拷贝一下然后呢我们就丢到这个里面来吧我们就
[03:37] 随便去丢一个位置吧比如说就丢到这吧因为我们是做测试的嘛就写到这个test里面来那么下面呢都是写的一些它的相关的一些get和set的方法然后后面呢有一个toString这样的一个方法非常简单的一个加码BOK好那么接下来呢我们就来实际的来操作一下那么下面我们来准备一个文本文件这个文本文件呢叫做urlst test
[04:06] 我们再来新建一个吧再来新建一个还是存储到哪里存储到我们的code下面有个fails下面有的叫做urlsttext那么编码的设置为utf8然后我们把内容拷贝过来那么相当于是不是我现在的构造有4条数据对吧那么第一是1显然这个就是用户的ID然后名字叫张三
[04:35] 然后年龄是20那么下面李四王五赵六这么多一些数据那么接下来我们就通过我们的Spark去读取这个文件然后我去把它转成我们的一些student这样的一个rdd然后做一些操作那么要注意的是我们在这个位置我们并不是使用我们之前的 API而我们直接所使用的是一个Spark season这样的 API来取代之前我们的一个
[05:05] 这个什么呢呃java Spark contact这样的一个对象哎ok好那么下面我们就来写一个测试用力那我们还是写到这个里面吧然后呢我们在下面去写一个测试用力然后呢他的名字叫做test data set好那么我们来写这样的一个测试用力那么接下来呢我们在这个位置呢所使用的就是谁呢就是我们刚刚所看到这个什么Spark season啊Spark
[05:36] 去做一个操作那么我们通过这个SparkSparkSessionBuild通过它来做一个构建那么要注意的是这个我们这个位置要给它设置什么呢set一个master就谁呢local然后呢local scene然后呢点再set一个app name那我们就跟我们之前写的一样吧那就叫谁呢就叫
[06:08] 去哪呢就叫什么呢就叫这个testml level好那么我们写到哪呢是不是写到这个位置来对吧写到这个位置来好那我们把它就放到下面吧这样的话看的会更清楚一点然后呢设置了两个参数然后呢我们最后呢通过一个它的API呢叫做get or create来得到一个Spark这样的一个session然后呢通过这个Spark session
[06:41] 通过这个Spark session呢我们就可以去读取叫什么呢reader去读取读取谁呢读取我们的一个text fill那么我们需要读取的是在f盘下面的有一个叫做什么呢codef盘然后呢下面的一个code然后呢下面的应该是这样去写
[07:09] 这个code然后呢下面有一个fails然后呢下面有个users.text这样的一个编写那我们通过它呢就会得到我们还是要通过它呢再继续点啊得到一个我们的一个rdd啊然后呢我们得到一个java的一个rdd啊得到它
[07:31] 那么我们来看一下这个就是我们所熟悉的RDDRDD1吧设置为它那么有了它之后呢接下来呢我们来看一下怎么样去怎么样去转去得到我们所希望得到的一个dataset那么通过这个RDD1然后呢我们去做一个map的一个操作做一个map的操作那么我们把这个设置为V然后呢往上写那么接下来呢我们就去读取到我们这个
[08:02] V之后呢我们去split按照什么呢按照逗号是不是去做一个分割做一个逗号做一个分割那么得到一个SS然后呢接下来呢我们是不是就需要去便利就可以去通过我们这个SS来构造我们那个student的一个对象那么下面呢我们就来定义一个student的对象然后呢去
[08:30] 去new一个student对象去new一个student的对象然后呢我们去做一些这个set操作比如set id那么就是通过这个none.valueof ss0然后呢还有呢一些其他的set一些什么呢set age那么这个年龄呢就是我们的int类型然后呢这个是ssss应该是这个这个是2啊
[09:07] 然后呢下面这个namename呢是我们通我们就不需要转了因为本身就字不创那么就是通过sse来得到一啊这样得到哎OK那么这样的话呢我们把把这个年龄吧年龄放到这个下面来这样会看的啊比较清楚一些然后呢我们return一个什么呢student啊return一个student然后呢我们就会得到一个什么呢得到一个rdd
[09:38] RDD2那么这个RDD2中所存储的对象类型呢就是我们student的那么接下来呢我们来看一下如何去做一个转换那么我们通过这个Spark session点有一个create一个dataframe那么我们可以看到是不是可以传递一个RDD和我们的一个class对吧那我们就调用这个API点create dataframe
[10:08] 然后呢第一个API呢就是我们的RDD那就RDD2那么第二个第二个API呢就是我们的一个class那么就是student.class那么这样的话呢就会得到我们的一个dataset啊dataset那么有了这个dataset之后呢我们就可以做一些操作了比如说呢我们通过dataset.show这个方法然后呢我们这样就得到了啊
[10:37] 来写下这个就我们会就是转化转化得到我们的一个data set这个把这个改成大写的s好那么我们来执行一下看一下这个效果好那我们来看一下执行的一个结果那么可以看到在这个位置是不是就会得到我们这样的一个一张表像一张表的这样的一个
[11:05] 结构那么是不是把我们的数据呢是不是就转化成我们那个dataset啊这样的一个结构了那么除了这个直接售之外呢我们还会有一些其他的一些这个操作那么你比如说呢我们可以去掉落他的API有一个select列对吧比如说我只希望呢显示我的ID和什么呢和这个name这个列那么其他的是不希望去显示出来的那我就直接来一个show
[11:34] 这样去做一个操作那么走那我们来看一下这个效果好那我们来看一下这个结果是不是就可以这样去做一些这个操作对吧那么当然了我们也可以去按照一些这个比如自动要做排序比如说我们的ID去做一个倒序的一个排序那么也是可以的那么通过在这个位置有一个order有个orderorder by我们给它去设置一个这个自动
[12:01] 那我们设置这个根据ID呢去做一个倒序那就我们需要写一个dataset然后呢点什么呢就是我们获取的我们这个列啊所谓的ID这个列点什么呢desc哎这样的话呢就可以了好那我们再来执行一下走好那我们来看一下这个结果那么可以看到这个结果呢是不是就会符合我们的预期啊按照那个ID呢去做一个倒序的一个
[12:31] 排序对吧OK没有问题那么其实这个用法呢其实就是我们去使用了dataset所提供的一些API那么其实我们可以看到它要比我们之前的一些RDD API是不是更加的一些高级对吧可以做一些筛选那么也可以去做一些我们的一些排序等等这样的一些操作OK好那么关于我们的RDD和dataset还有DataFrame它们的一些区别以及转换那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写 Spark MLlib 代码，通过 RDD 转化为 DataFrame，并展示数据操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前章节为“1.3. RDD、DataSet、DataFrame区别及转化”，并显示 Student 类的 Java 代码。
画面 2: 在 IntelliJ IDEA 中打开项目，显示 Student 类的完整代码，包含 id、name、age 字段及 getter/setter 方法。
画面 3: 展示 TestMLib.java 文件中关于两个矩阵相加的代码，包含 System.out.println 输出语句。
画面 4: 在 TestMLib.java 中，光标位于 SparkSession.builder().appName().getOrCreate() 代码行，显示 SparkSession 的可用方法。
画面 5: 展示 TestMLib.java 中的 JavaRDD<Vector> rdd1 和 JavaRDD<IndexedRow> rdd2 的创建代码。
画面 6: 展示 TestMLib.java 中的 SparkSession.read().textFile("F:\\code\\files\\users.txt") 代码，用于读取文本文件。
画面 7: 展示 TestMLib.java 中的 JavaRDD<String> rdd1.map(...) 代码，用于将字符串按空格分割。
画面 8: 展示 TestMLib.java 中的 SparkSession.builder().appName("test").getOrCreate() 代码，用于创建 SparkSession。
画面 9: 展示 TestMLib.java 中的 JavaRDD<String> rdd1.map(...) 代码，用于将字符串按空格分割。
画面 10: 展示 TestMLib.java 中的 sparkSession.createDataFrame(...) 代码，用于将 RDD 转化为 DataFrame。
画面 11: 展示 TestMLib.java 中的 dataset.show() 代码，用于显示 DataFrame 数据。
画面 12: 展示 TestMLib.java 中的 dataset.select(col("id"), col("name")).orderBy(dataset.col("id")).show() 代码，用于选择并排序数据。
画面 13: 展示课程大纲，当前章节为“1.3. RDD、DataSet、DataFrame区别及转化”，并显示 Student 类的 Java 代码。
画面 14: 展示课程大纲，当前章节为“1.3. RDD、DataSet、DataFrame区别及转化”，并显示 Student 类的 Java 代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

画面 2:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Integer getAge() { return age; }
    public void setAge(Integer age) { this.age = age; }
}

画面 3:
BlockMatrix addBlockMatrix = blockMatrix.add(blockMatrix);
System.out.println(addBlockMatrix.numCols());
System.out.println(addBlockMatrix.numRows());
List<Tuple2<Tuple2<Object, Object>, Matrix>> collect = addBlockMatrix.block
.collect().forEach(tuple2MatrixTuple2 -> System.out.println(tuple2MatrixTuple2));

画面 4:
SparkSession sparkSession = SparkSession.builder()
    .appName("test")
    .getOrCreate();

画面 5:
JavaRDD<Vector> rdd1 = fileRDD.map(v -> {
    String[] ss = v.split(" ");
    double[] da = new double[ss.length];
    for (int i = 0; i < ss.length; i++) {
        da[i] = Double.valueOf(ss[i]);
    }
    return Vectors.dense(da);
});
JavaRDD<IndexedRow> rdd2 = rdd1.map(v -> new IndexedRow(v.size(), v));

画面 6:
sparkSession.read().textFile("F:\\code\\files\\users.txt");

画面 7:
JavaRDD<String> rdd1 = sparkSession.read().textFile("F:\\code\\files\\users.txt").javaRDD();
JavaRDD<String> rdd1 = rdd1.map(v -> {
    String[] ss = v.split(" ");
    return ss[0];
});

画面 8:
SparkSession sparkSession = SparkSession.builder()
    .appName("test")
    .getOrCreate();

画面 9:
JavaRDD<String> rdd1 = sparkSession.read().textFile("F:\\code\\files\\users.txt").javaRDD();
JavaRDD<String> rdd1 = rdd1.map(v -> {
    String[] ss = v.split(" ");
    return ss[0];
});

画面 10:
Dataset<Row> dataSet = sparkSession.createDataFrame(rdd2, Student.class);

画面 11:
dataset.show();

画面 12:
dataset.select(col("id"), col("name")).orderBy(dataset.col("id")).show();

画面 13:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

画面 14:
import java.io.Serializable;
public class Student implements Serializable {
    private Long id;
    private String name;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

