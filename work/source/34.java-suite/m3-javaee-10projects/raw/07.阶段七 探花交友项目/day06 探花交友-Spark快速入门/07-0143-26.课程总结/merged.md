# 26.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\26.课程总结_【海量资源尽在 666java.com】.mp4
- 时长 4分32秒（音频 272s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们对今天的课程呢做一个总结那么今天呢我们首先呢给大家去讲一下什么是Spark那么对Spark呢有了一些了解包括它的一些发展的历史啊等等然后呢我们讲了Spark的一些特点就是什么呢比如说相当速度比较快啊然后呢易用性比较好然后呢通用强然后呢兼容性啊也是比较好的这样的一些特性
[00:29] 去进行动手去搭建我们的Spark的集群那么在我们的集群搭建完成之后那么我们去搭建了一个什么HA的一个高可用这样的一个部署当然了方案有两种第一种是基于文件系统做一个我们单点的一个恢复那么第二种是基于我们的Zoomkeeper去做一个HA的一个部署那么显然我们更推荐使用Zoomkeeper
[00:57] 然后我们就去动手给Zookeeper去做一个高可用集群的这样的一个搭建那么在我们集群搭建完成之后我们对Spark的一些相关的一些这种组件的一些角色给大家去做了一些这种了解了解完成之后我们去体验了一下Spark的程序我们所要是使用什么叫做门特卡罗的一个算法
[01:24] 来求解一个圆周率派的值那么其实就是让我们来体验一下Spark程序或者Spark集群是它能做什么事情那么现在我们肯定就比较清楚了然后我们去给大家讲了一下Spark sale的一个基本的一些使用然后我们最后是不是也去指定集群去做一些运行等等
[01:49] 那么接下来呢就是我们去编写Spark的应用这个呢是我们学习的重点那么我们呢是使用这个加二语言呢去进行了一个我们的应用的一个编写那么我们编写的应用呢其实是非常简单的一个应用就是什么呢我们的一个word count就是我们的一个字数的单词的一个统计
[02:12] 那么我们是不是去在文本中说了一些这个句子然后呢是其中的我们按照空格去做一个分割去统计啊它的一个单词啊这样的一个啊这样的小的一个例子啊但是呢这个例子虽然啊比较简单啊但是呢它这个里面所涉及的内容还是比较多的希望大家能够独立的把它呢去能够去敲出来
[02:36] 好,那么当然了这个代码呢我们做了一些这个优化优化之后呢主要是使用这个Lambda表达式呢对我们的API的使用呢去做了一些这个代码层面的一些这个优化当然我们也是推荐啊大家能够去按照这种Lambda表达式的形式呢去写这样的代码那么这样的话其实既简洁又高效啊OK
[02:59] 好 那么最后呢我们也给大家去演示了一下如何将我们自己所写的应用程序呢去打包在我们的集群中去做一些运行OK 好 那么这个呢我们已经都讲过了啊然后呢我们重点呢又去给大家讲了一下这个RDD因为RDD呢是我们去理解这个SPARK的一个这个基础和一个重点那我们需要把这个概念呢去理解清楚
[03:25] OK那么我们需要掌握它的一些这个常用的一些算子的操作然后呢我们又讲了SPARK的任务调动那么包括我们就讲了RDD的一些依赖关系这个宽依赖和窄依赖
[03:38] 那么这两个定义大家一定要取分清楚能够一眼就看出他们之间的一个关系那么正因为他们之间有依赖关系那么就可以根据这个依赖关系去形成一个有像无环图并且我们会根据这个宽依赖和窄依赖来形成不同的一些阶段去做处理那么最后就会形成整个的一个这样的一个调度过程了那么OK
[04:03] 好 那么这个以上呢就是我们今天的一些内容那么我们从最初的对Spark的一个这个了解然后到我们去搭建这个集群环境到我们编写我们的一些应用程序到最后呢去了解它的一些流程呢一些的一些原理啊比如说像RDD概念啊等等那么这样的话呢我们就完成了一个Spark的一个快速的一个入门OK 好 那么以上呢就是今天的课程的主要的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了Spark框架的基础知识，包括其概念、架构、环境搭建、程序编写与任务调度等内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：课程介绍，目录结构显示“1. Spark概述”、“2. 搭建Spark集群”、“3. Spark角色介绍”、“4. 体验Spark程序”、“5. 编写Spark应用”、“6. Spark任务调度”等章节。
画面2：讲解Spark是什么，指出其为专为大规模数据处理设计的快速通用计算引擎，由UC Berkeley AMP Lab开发，官网为http://Spark.apache.org/。
画面3：展示Spark的通用性，支持批处理、流处理、机器学习和图计算，图示显示Spark SQL、Spark Streaming、MLlib、GraphX等模块。
画面4：讲解搭建Spark集群，指出可在Windows或Linux上运行，推荐使用CentOS 6.5版本，下载地址为http://Spark.apache.org/downloads.html。
画面5：显示Spark HA高可用部署说明，包含环境变量配置（如JAVA_HOME、SPARK_HOME）和启动脚本（/start-all.sh）。
画面6：展示Spark架构图，包含Driver Program、Cluster Manager、Worker Node等组件，Worker Node包含Executor和Cache。
画面7：讲解执行第一个Spark程序，命令行示例为：/run-example --master Spark://node1:7077,node2:7077,node3:7077 SparkPi 10。
画面8：讲解Spark-Shell，展示如何使用Scala编写Spark程序，示例代码为：sc.textFile("file:///itcast/word.txt").flatMap(...).map(...).reduceByKey(...).collect()。
画面9：讲解创建Spark工程，显示Maven新建项目界面，Group Id为cn.itcast.Spark，Artifact Id为my-Spark-test，Version为1.0-SNAPSHOT。
画面10：展示WordCount程序的Java代码，包含SparkConf配置、SparkContext创建、文件读取和转换操作。
画面11：展示优化后的WordCount程序代码，包含map和reduceByKey操作，以及关闭资源的代码。
画面12：讲解maven打包，显示Maven生命周期中的package阶段被选中，打包后生成my-Spark-test-1.0-SNAPSHOT.jar文件。
画面13：讲解RDD的依赖关系，图示区分窄依赖（narrow dependency）和宽依赖（wide dependency），窄依赖包括map、filter、union等，宽依赖包括groupByKey、join等。
画面14：讲解Spark任务调度流程，图示显示RDD Objects → DAGScheduler → TaskScheduler → Worker的流程，DAGScheduler将DAG拆分为Stage，TaskScheduler将TaskSet提交给Worker执行。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```bash
# 在宿主机上输入如下内容
export JAVA_HOME=/usr/local/src/JDK 8.0_141  #jdk地址
export SPARK_MASTER_HOST=node1  #master的ip地址
export SPARK_MASTER_PORT=7077  #master的端口
mv slaves.template slaves
vim slaves
#输入如下内容
node1
node2
node3
#远程拷贝到其它机器
scp -r Spark node2:/itcast/
scp -r Spark node3:/itcast/
#添加环境变量（3台都添加）
vim ~/.bashrc
export SPARK_HOME=/itcast/Spark
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
source ~/.bashrc
#启动
cd /itcast/Spark/sbin
./start-all.sh
```

画面7：
```bash
#进入到bin目录
./run-example --master Spark://node1:7077,node2:7077,node3:7077 SparkPi 10
```

画面8：
```bash
#进入如下命令：
sc.textFile("file:///itcast/word.txt").flatMap(...).map(...).reduceByKey(...).collect()
```

画面9：
```bash
Group Id: cn.itcast.Spark
Artifact Id: my-Spark-test
Version: 1.0-SNAPSHOT
```

画面10：
```java
import org.apache.Spark.api.java.JavaPairRDD;
import org.apache.Spark.api.java.JavaRDD;
import org.apache.Spark.api.java.JavaSparkContext;
import org.apache.Spark.api.java.function.FlatMapFunction;
import org.apache.Spark.api.java.function.Function2;
import org.apache.Spark.api.java.function.PairFunction;
import scala.Int;
import scala.tuple2;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;
public class WordCountApp {
    public static void main(String[] args) {
        // Spark的配置
        SparkConf sparkConf = new SparkConf()
                .setAppName("WordCountApp"); // 应用名，并且使用cpu的核数相同的线程数执行
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
        // 读取文件
        JavaRDD<String> fileRdd = jsc.textFile("file:///code/word.txt");
        // 逻辑操作，并且按行分割
```

画面11：
```java
Function2<Integer, Integer, Integer> {
    @Override
    public Integer call(Integer v1, Integer v2) throws Exception {
        return v1 + v2;
    }
}
// 执行计算
List<Tuple2<Object, Integer>> collect = reduceByKey.collect();
for (Tuple2<Object, Integer> obj : collect) {
    System.out.println(obj._1 + "出现的次数为：" + obj._2);
}
// 关闭，释放资源
jsc.stop();
```

画面12：
```bash
mvn package
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：架构图中，Driver Program → Cluster Manager，Cluster Manager → Worker Node，Worker Node包含Executor和Cache。
画面13：图示中，窄依赖（narrow dependency）包括map、filter、union等，宽依赖（wide dependency）包括groupByKey、join等。
画面14：流程图中，RDD Objects → DAGScheduler → TaskScheduler → Worker，DAGScheduler将DAG拆分为Stage，TaskScheduler将TaskSet提交给Worker执行。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

