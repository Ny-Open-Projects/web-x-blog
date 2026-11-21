# 画面线理解：25.ALS算法流程之编码实战

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\25.ALS算法流程之编码实战_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:52, 01:26, 02:09, 02:38, 04:15, 04:54, 06:04, 07:03, 07:56, 09:07, 09:59, 10:34, 10:49, 11:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:48:19

1) 这一组画面整体在讲如何使用 Spark Java API 实现基于 ALS 算法的电影推荐系统。

2) 按时间顺序列出每张画面的要点：
画面1：展示 TestMLib.java 文件，其中包含创建 DataFrame 并进行数据转换的代码，用于学生对象的构建。
画面2：展示 MyRecommend.java 文件，开始编写 SparkConf 配置，设置应用名称和 Master 为本地模式。
画面3：在 MyRecommend.java 中，创建 JavaSparkContext 对象。
画面4：在 MyRecommend.java 中，设置数据文件路径为 "F:\ml-100k\u.data"。
画面5：在 MyRecommend.java 中，对数据文件进行分割处理，使用 map 操作将每行按制表符分割。
画面6：在 MyRecommend.java 中，将分割后的数据转换为 Rating 对象。
画面7：在 MyRecommend.java 中，使用 ALS 算法训练模型，设置 rank 为 8，iterations 为 10。
画面8：在 MyRecommend.java 中，调用模型的 recommendProducts 方法，为用户 301 推荐 10 个商品。
画面9：在 MyRecommend.java 中，使用 for 循环遍历推荐结果，并打印输出。
画面10：在 MyRecommend.java 中，运行程序，终端显示 Spark 任务执行日志。
画面11：在 MyRecommend.java 中，程序运行完成，终端显示成功信息。
画面12：在 MyRecommend.java 中，展示最终的推荐结果，包括用户 ID 和商品 ID。
画面13：在 MyRecommend.java 中，展示最终的推荐结果，包括用户 ID 和商品 ID。
画面14：切换到 Typora 文档，展示 SparkMLlib 系统推荐算法的实战部分，包含 ALS 算法的代码示例。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```java
student.setAge(Integer.valueOf(as[2]));
return student;
});
Dataset<Row> dataSet = sparkSession.createDataFrame(rdd2, Student.class);
// dataSet.show();
dataSet.select(col("id"), cols("name")).orderBy(dataSet.col(colName: "id")).
```

画面2：
```java
package cn.itcast.spark;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaSparkContext;
public class MyRecommend {
    public static void main(String[] args) {
        SparkConf sparkConf = new SparkConf()
```

画面3：
```java
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
```

画面4：
```java
jsc.textFile(path: "F:\\ml-100k\\u.data");
```

画面5：
```java
JavaRDD<String> sourceRDD = jsc.textFile(path: "F:\\ml-100k\\u.data");
JavaRDD<String[]> lineRdd = sourceRDD.map(v -> v.split(regex: "\t"));
```

画面6：
```java
JavaRDD<String[]> lineRdd = sourceRDD.map(v -> v.split(regex: "\t"));
lineRdd.map(v -> new Rating());
```

画面7：
```java
lineRdd.map(v -> new Rating(Integer.valueOf(v[0]), Integer.valueOf(v[1]), Double.valueOf(v[2])));
```

画面8：
```java
ALS.train(ratingRDD, rank: 8, iterations: 10);
```

画面9：
```java
MatrixFactorizationModel model = ALS.train(ratingRDD, rank: 8, iterations: 10);
```

画面10：
```java
Rating[] products = model.recommendProducts(user: 301, num: 10);
```

画面11：
```java
for (Rating product : products) {
    System.out.println("user" + user + " - " + product.product + " - " + product.rating);
}
```

画面12：
```text
19/08/24 20:38:36 INFO BlockManager: Found block rdd_210_1 locally
userId = 301, product = 915
userId = 301, product = 933
userId = 301, product = 1106
userId = 301, product = 918
userId = 301, product = 912
userId = 301, product = 1645
userId = 301, product = 914
```

画面13：
```java
MatrixFactorizationModel model = ALS.train(ratingRDD, rank: 8, iterations: 10);
Rating[] products = model.recommendProducts(user: 301, num: 10);
```

画面14：
```text
7.4.3. 实战
...
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面14：PPT 标题为“SparkMLlib推荐系统实战”，内容包含 ALS 算法的代码示例。

5) 无。
