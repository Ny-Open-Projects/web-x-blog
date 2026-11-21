# 画面线理解：26.ALS算法流程之实战优化（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\26.ALS算法流程之实战优化（上）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:44, 03:11, 03:58, 04:55, 06:02, 06:57, 07:42, 08:33, 09:31, 10:07, 12:38, 13:19, 14:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:48:59

1) 这一组画面整体在讲如何使用 Spark Java API 实现基于 ALS 算法的电影推荐系统，包括数据读取、转换、模型训练和结果输出。

2) 按时间顺序列出每张画面的要点：
画面1: 显示程序运行结果，包含用户ID和产品ID的推荐对，以及程序成功退出。
画面2: 展示代码中创建 SparkConf、JavaSparkContext，并加载数据文件。
画面3: 展示代码中对数据进行分割处理，转换为 Rating 对象，并进行模型训练和推荐。
画面4: 展示代码中对数据进行分割处理，转换为 Rating 对象，并进行模型训练和推荐。
画面5: 展示代码中对数据进行分割处理，转换为 Rating 对象，并进行模型训练和推荐。
画面6: 展示代码中对数据进行分割处理，转换为 Rating 对象，并进行模型训练和推荐。
画面7: 展示代码中加载电影目录映射关系。
画面8: 展示 PPT 标题“SparkMLlib推荐系统入门1md - Typora”，并显示代码中统计用户和电影数量。
画面9: 展示代码中对 Rating 对象的属性进行操作。
画面10: 展示代码中对数据进行分割处理，转换为 Rating 对象，并进行模型训练和推荐。
画面11: 展示代码中对数据进行分割处理，转换为 Rating 对象，并进行模型训练和推荐。
画面12: 展示代码中对数据进行分割处理，转换为 Rating 对象，并进行模型训练和推荐。
画面13: 展示程序运行结果，包含训练集、校验集和测试集的数量。
画面14: 展示程序运行结果，包含训练集、校验集和测试集的数量。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面2:
```java
SparkConf sparkConf = new SparkConf()
    .setAppName("MyRecommend")
    .setMaster("local[*]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
jsc.setLogLevel("WARN"); //设置日志级别
JavaRDD<String> sourceRDD = jsc.textFile(path: "F:\ml-100k\u.data");
JavaRDD<String[]> lineRdd = sourceRDD.map(v -> v.split(regex: "\t"));
```

画面3:
```java
MatrixFactorizationModel model1 = ALS.train(ratingRDD, rank: 0, iterations: 10);
Rating[] products = model.recommendProducts(user: 301, num: 10);
for (Rating product : products) {
    System.out.println("userId = " + product.user() + ", product = " + product.product());
}
jsc.stop();
```

画面4:
```java
Rating rating = new Rating(Integer.valueOf(v[0]), Integer.valueOf(v[1]), Double.valueOf(v[2]));
Integer key = Integer.valueOf(v[3]) % 10;
return new Tuple2(key, rating);
```

画面5:
```java
Rating rating = new Rating(Integer.valueOf(v[0]), Integer.valueOf(v[1]), Double.valueOf(v[2]));
Integer key = Integer.valueOf(v[3]) % 10;
return new Tuple2(key, rating);
```

画面6:
```java
Rating rating = new Rating(Integer.valueOf(v[0]), Integer.valueOf(v[1]), Double.valueOf(v[2]));
Integer key = Integer.valueOf(v[3]) % 10;
return new Tuple2(key, rating);
```

画面7:
```java
List<Tuple2> movies = jsc.textFile(path: "F:\ml-100k\u.item").map(v -> {
    String[] ss = v.split(regex: "\t");
    return new Tuple2(ss[0], ss[1]);
}).collect();
```

画面8:
```java
Long numRatings = ratings.count();
Long numUsers = ratings.map(v -> (Rating) v._2).distinct().count();
Long numMovies = ratings.map(v -> (Rating) v._2).distinct().count();
System.out.println("用户：" + numUsers + " 电影：" + numMovies + " 评论：" + numRatings);
Integer numPartitions = 4; // 分区数
```

画面9:
```java
Rating rating = new Rating(Integer.valueOf(v[0]), Integer.valueOf(v[1]), Double.valueOf(v[2]));
Integer key = Integer.valueOf(v[3]) % 10;
return new Tuple2(key, rating);
```

画面10:
```java
List<Tuple2> movies = jsc.textFile(path: "F:\ml-100k\u.item").map(v -> {
    String[] ss = v.split(regex: "\t");
    return new Tuple2(ss[0], ss[1]);
}).collect();
```

画面11:
```java
Integer numPartitions = 4; // 分区数
JavaRDD<Rating> training = ratings
    .filter(v -> v._1() < 6)
    .values()
    .repartition(numPartitions)
    .cache();
```

画面12:
```java
Integer numPartitions = 4; // 分区数
JavaRDD<Rating> training = ratings
    .filter(v -> v._1() < 6)
    .values()
    .repartition(numPartitions)
    .cache();
```

画面13:
```java
JavaRDD<Rating> test = ratings
    .filter(v -> v._1() >= 6 && v._1() < 8)
    .values()
    .repartition(numPartitions)
    .cache();
```

画面14:
```java
JavaRDD<Rating> test = ratings
    .filter(v -> v._1() >= 6 && v._1() < 8)
    .values()
    .repartition(numPartitions)
    .cache();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面8: PPT 标题“SparkMLlib推荐系统入门1md - Typora”，并显示代码中统计用户和电影数量。

5) 不要评价画面美观，不要输出与课程无关的内容。
