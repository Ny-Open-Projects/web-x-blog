# 画面线理解：29.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\29.课程总结_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:35, 00:57, 01:02, 01:07, 01:14, 01:19, 01:30, 01:56, 02:07, 02:09, 02:20, 02:34, 02:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:51:25

1) 这一组画面整体在讲什么（一句话）：
本课程系统介绍Spark MLlib推荐系统的核心概念、算法原理及实战代码，涵盖数据类型、协同过滤、相似度算法和ALS模型训练等模块。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：课程说明，介绍Spark MLlib的学习目标，包括了解其定义、支持的数据类型、推荐系统、协同过滤、相似度算法、交叉最小二乘法等。
画面2：介绍本地向量，列出Local vector、Labeled point、Local matrix、Distributed matrix的定义。展示导入MLlib的Maven依赖：<dependency><groupId>org.apache.spark</groupId><artifactId>spark-mllib_2.12</artifactId><version>2.4.3</version></dependency>。展示密集向量的Java代码：package cn.itcast.spark; import org.apache.spark.mllib.linalg.Vector; import org.apache.spark.mllib.linalg.Vectors;
画面3：介绍RDD、DataSet、DataFrame的转化关系，展示一个Student类的Java代码：package cn.itcast.spark; import java.io.Serializable; public class Student implements Serializable { private Long id; private String name; private Integer age; public Long getId() { return id; } public void setId(Long id) { this.id = id; } public String getName() { return name; } public void setName(String name) { this.name = name; } public Integer getAge() { return age; } public void setAge(Integer age) { this.age = age; } }
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
<groupId>org.apache.spark</groupId>
<artifactId>spark-mllib_2.12</artifactId>
<version>2.4.3</version>
</dependency>

画面2：
package cn.itcast.spark;
import org.apache.spark.mllib.linalg.Vector;
import org.apache.spark.mllib.linalg.Vectors;

画面3：
package cn.itcast.spark;
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
package cn.itcast.spark;
import org.apache.spark.mllib.recommendation.ALS;
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel;
import org.apache.spark.mllib.recommendation.Rating;
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
package cn.itcast.spark;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel;
import org.apache.spark.mllib.recommendation.Rating;
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
