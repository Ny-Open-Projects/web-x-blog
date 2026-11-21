# 29.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\29.课程总结_【海量资源尽在 666java.com】.mp4
- 时长 3分12秒（音频 193s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢我们做一个总结那么今天呢我们给大家主要讲了什么内容呢我们来回顾一下啊那么就是我们讲了这个SPARK的MLlib那么什么是SPARK MLlib它呢其实就是SPARK的一个在机器学习方面的一个
[00:19] 这样的一个内库对吧它提供了有很多的一些这个算法那么我们其实重点要使用它的是在这一块的什么ALS这样的一个推荐的一个算法然后呢我们又去讲了这个MLlib所支持的一些数据类型有这个本地向量级向量标签还有本地矩阵还有分布式矩阵这样的一些数据的一个这个结构那么我们这个就不一一去讲了
[00:45] 然后后面我们讲了这个RDD还有DataSet Data Frame他们的一个区别以及这个转化关系这个大家要理解然后能够去掌握下面我们就讲了一些推荐系统然后讲什么是推荐系统对吧然后讲一些推荐系统在电商或者说其他领域中的一些应用然后我们又讲了一些推荐系统的业务流程然后我们给大家讲了什么协同过滤算法
[01:14] 基于用户的过滤算法那么基于这个商品的推荐算法这个我们都讲了然后呢我们讲了用户的偏好数据的这个收集相关的一些这个知识OK然后呢我们也讲了一些这个相似度一些算法那么有这个什么欧几里德PLC还有这个夹角的预选值然后呢还有一个TinyMoto这样的一个参数
[01:40] 它的一些相关的一些这个相似度的一些算法然后呢我们讲了一个最近淋雨这样的一个概念然后呢在最后呢我们讲了这个交替最小二乘法这个是我们今天需要重点掌握的内容那么重点呢我们是要讲后掌握后面的这个实战那么前面的这个最小二乘法和交替最小二乘法的一个原理呢大家有一个了解啊
[02:08] 就可以了那后面我们是不是有讲了这个als的一个算法的一个流程然后呢我们就基于前面所讲的这个流程呢然后呢我们去做了一个实战那我们准备了有10万条这样的一个数据啊就是用户对电影评价这样的一个数据做一个具体的一个实战然后呢我们又去讲了一下这个什么呢als算法的一个建模然后呢又去做具体的实战
[02:37] 那么我们先讲了什么呢就是最基本的一个使用然后呢我们又在之前最基本的一个使用的基础之上呢我们做了优化改进那么优化改进这一块呢就更具有什么呢就是实际的使用的一个价值和意义那么希望大家呢把重点放到这一块然后呢去吸收啊去学习它OK那么以上呢其实就是今天我们所讲的一些内容今天主要就是我们在讲
[03:06] 推荐了对吧OK好那么关于我们的课程的一个总结呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程系统介绍Spark MLlib推荐系统的核心概念、算法原理及实战代码，涵盖数据类型、协同过滤、相似度算法和ALS模型训练等模块。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：课程说明，介绍Spark MLlib的学习目标，包括了解其定义、支持的数据类型、推荐系统、协同过滤、相似度算法、交叉最小二乘法等。
画面2：介绍本地向量，列出Local vector、Labeled point、Local matrix、Distributed matrix的定义。展示导入MLlib的Maven依赖：<dependency><groupId>org.apache.Spark</groupId><artifactId>Spark-mllib_2.12</artifactId><version>2.4.3</version></dependency>。展示密集向量的Java代码：package cn.itcast.Spark; import org.apache.Spark.mllib.linalg.Vector; import org.apache.Spark.mllib.linalg.Vectors;
画面3：介绍RDD、DataSet、DataFrame的转化关系，展示一个Student类的Java代码：package cn.itcast.Spark; import java.io.Serializable; public class Student implements Serializable { private Long id; private String name; private Integer age; public Long getId() { return id; } public void setId(Long id) { this.id = id; } public String getName() { return name; } public void setName(String name) { this.name = name; } public Integer getAge() { return age; } public void setAge(Integer age) { this.age = age; } }
画面4：介绍推荐系统，说明其解决信息过载问题。展示电商推荐系统先行者：亚马逊、京东、优酷、土豆、新浪、QQ、网易等。
画面5：展示当当网和京东的推荐页面截图。
画面6：介绍协同过滤算法，展示“用户A”和“用户B”指向“物品C”的示意图。
画面7：介绍基于用户的推荐UserCF，说明其核心思想和问题。展示QQ、电商等场景的推荐逻辑。
画面8：介绍用户偏好收集和数据归一化，说明归一化处理方法。
画面9：介绍相似度算法，列出欧氏距离、皮尔逊相关系数、余弦相似度、Tanimoto系数等。
画面10：展示欧氏距离计算公式。
画面11：展示交叉最小二乘法（ALS）的原理图，包含Rating Matrix、User Feature Matrix、Movie Feature Matrix。
画面12：展示ALS算法流程图，包含“初始化Spark与数据集”、“切分测试集和验证”、“训练ALS模型”、“验证结果”等节点。
画面13：展示ALS算法实战的数据说明，列出示例数据。
画面14：展示ALS算法实战的代码，包括数据建模和优化改进部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
<dependency>
<groupId>org.apache.Spark</groupId>
<artifactId>Spark-mllib_2.12</artifactId>
<version>2.4.3</version>
</dependency>

画面2：
package cn.itcast.Spark;
import org.apache.Spark.mllib.linalg.Vector;
import org.apache.Spark.mllib.linalg.Vectors;

画面3：
package cn.itcast.Spark;
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

画面7：
package cn.itcast.Spark;
import org.apache.Spark.mllib.recommendation.ALS;
import org.apache.Spark.mllib.recommendation.MatrixFactorizationModel;
import org.apache.Spark.mllib.recommendation.Rating;
import scala.Tuple2;

画面13：
def train(ratings: RDD[Rating], //需要训练的数据
rank: Int, //rank一般在20之间
iterations: Int, //算法中迭代次数，一般10次左右
lambda: Double, //ALS中的正则化参数，一般设置为0.01
blocks: Int, //并行计算的block数（为自动选择）
alpha: Double, //ALS隐式反馈变化率用于控制每次迭代修正的幅度
seed: Long //随机种子
): MatrixFactorizationModel = {
new ALS(blocks, blocks, rank, iterations, lambda, seed).run(ratings)
}

画面14：
package cn.itcast.Spark;
import org.apache.Spark.SparkConf;
import org.apache.Spark.api.java.JavaRDD;
import org.apache.Spark.api.java.JavaSparkContext;
import org.apache.Spark.mllib.recommendation.MatrixFactorizationModel;
import org.apache.Spark.mllib.recommendation.Rating;
import scala.Tuple2;
import java.util.List;

public class MyRecommend {
public static void main(String[] args) {
SparkConf sparkConf = new SparkConf()
.setAppName("MyRecommend");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
jsc.setLogLevel("WARN"); //设置日志级别
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：标题“3、协同过滤算法”，核心思想：协同过滤一般是在海量的用户中发掘出一小部分和你品位比较相似的，在协同过程中，这些用户成为邻居。然后根据他们喜欢的某项东西预测成一个排序的列表作为推荐给你。问题：如何确定一个用户和必有相似的品位？如何将邻居的喜好组织成一个排序的目录？
画面11：标题“7.3、ALS算法流程”，流程图：初始化Spark与数据集 → 切分测试集和验证 → 训练ALS模型 → 验证结果 → 不满足要求 → 返回训练。
画面12：标题“7.4、ALS算法实战”，数据说明：示例数据是用户、电影、评分的数据，其中用户有943人，电影有1682部，评分有100000条，文件在资料中。
画面13：标题“7.4.1、数据说明”，数据示例：1 196 242 3 881250949 2 186 302 3 891717742 3 22 377 3 878887116 4 244 51 2 880606923 5 166 346 1 886397596 6 298 474 4 884182806 7 215 265 2 881174868 8 253 465 5 891628467 9 305 451 3 886324817 10 6 86 5 883603013 11 62 257 2 879372434 12 286 1014 5 879761125 13 200 222 5 876082340 14 210 40 3 891035994 15 210 40 3 891035994

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

