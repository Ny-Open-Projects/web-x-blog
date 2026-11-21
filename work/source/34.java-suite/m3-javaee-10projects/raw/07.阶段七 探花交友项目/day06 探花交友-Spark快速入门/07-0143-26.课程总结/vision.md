# 画面线理解：26.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\26.课程总结_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:14, 00:23, 00:33, 00:39, 01:07, 01:14, 01:44, 02:03, 02:13, 02:40, 03:11, 03:47, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:34:23

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了Spark框架的基础知识，包括其概念、架构、环境搭建、程序编写与任务调度等内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：课程介绍，目录结构显示“1. Spark概述”、“2. 搭建Spark集群”、“3. Spark角色介绍”、“4. 体验Spark程序”、“5. 编写Spark应用”、“6. Spark任务调度”等章节。
画面2：讲解Spark是什么，指出其为专为大规模数据处理设计的快速通用计算引擎，由UC Berkeley AMP Lab开发，官网为http://spark.apache.org/。
画面3：展示Spark的通用性，支持批处理、流处理、机器学习和图计算，图示显示Spark SQL、Spark Streaming、MLlib、GraphX等模块。
画面4：讲解搭建Spark集群，指出可在Windows或Linux上运行，推荐使用CentOS 6.5版本，下载地址为http://spark.apache.org/downloads.html。
画面5：显示Spark HA高可用部署说明，包含环境变量配置（如JAVA_HOME、SPARK_HOME）和启动脚本（/start-all.sh）。
画面6：展示Spark架构图，包含Driver Program、Cluster Manager、Worker Node等组件，Worker Node包含Executor和Cache。
画面7：讲解执行第一个Spark程序，命令行示例为：/run-example --master spark://node1:7077,node2:7077,node3:7077 SparkPi 10。
画面8：讲解Spark-Shell，展示如何使用Scala编写Spark程序，示例代码为：sc.textFile("file:///itcast/word.txt").flatMap(...).map(...).reduceByKey(...).collect()。
画面9：讲解创建Spark工程，显示Maven新建项目界面，Group Id为cn.itcast.spark，Artifact Id为my-spark-test，Version为1.0-SNAPSHOT。
画面10：展示WordCount程序的Java代码，包含SparkConf配置、SparkContext创建、文件读取和转换操作。
画面11：展示优化后的WordCount程序代码，包含map和reduceByKey操作，以及关闭资源的代码。
画面12：讲解maven打包，显示Maven生命周期中的package阶段被选中，打包后生成my-spark-test-1.0-SNAPSHOT.jar文件。
画面13：讲解RDD的依赖关系，图示区分窄依赖（narrow dependency）和宽依赖（wide dependency），窄依赖包括map、filter、union等，宽依赖包括groupByKey、join等。
画面14：讲解Spark任务调度流程，图示显示RDD Objects → DAGScheduler → TaskScheduler → Worker的流程，DAGScheduler将DAG拆分为Stage，TaskScheduler将TaskSet提交给Worker执行。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```bash
# 在宿主机上输入如下内容
export JAVA_HOME=/usr/local/src/jdk1.8.0_141  #jdk地址
export SPARK_MASTER_HOST=node1  #master的ip地址
export SPARK_MASTER_PORT=7077  #master的端口
mv slaves.template slaves
vim slaves
#输入如下内容
node1
node2
node3
#远程拷贝到其它机器
scp -r spark node2:/itcast/
scp -r spark node3:/itcast/
#添加环境变量（3台都添加）
vim ~/.bashrc
export SPARK_HOME=/itcast/spark
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
source ~/.bashrc
#启动
cd /itcast/spark/sbin
./start-all.sh
```

画面7：
```bash
#进入到bin目录
./run-example --master spark://node1:7077,node2:7077,node3:7077 SparkPi 10
```

画面8：
```bash
#进入如下命令：
sc.textFile("file:///itcast/word.txt").flatMap(...).map(...).reduceByKey(...).collect()
```

画面9：
```bash
Group Id: cn.itcast.spark
Artifact Id: my-spark-test
Version: 1.0-SNAPSHOT
```

画面10：
```java
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import scala.Int;
import scala.tuple2;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;
public class WordCountApp {
    public static void main(String[] args) {
        // spark的配置
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
