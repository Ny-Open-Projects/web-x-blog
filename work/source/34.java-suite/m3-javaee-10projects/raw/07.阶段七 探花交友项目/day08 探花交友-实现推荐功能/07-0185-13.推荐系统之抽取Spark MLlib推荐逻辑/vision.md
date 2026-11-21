# 画面线理解：13.推荐系统之抽取Spark MLlib推荐逻辑

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\13.推荐系统之抽取Spark MLlib推荐逻辑_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:44, 01:17, 02:07, 02:32, 02:57, 03:18, 03:34, 03:43, 04:04, 04:15, 04:26, 04:46, 05:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:59:46

1) 这一组画面整体在讲如何使用 Spark MLlib 实现基于矩阵分解的电影推荐系统，包括数据预处理、模型训练与评估。

2) 按时间顺序列出每张画面的要点：
画面1：
- 显示 IntelliJ IDEA 中的 Java 代码，正在处理评分数据，将每行数据按制表符分割，提取用户ID、电影ID和评分。
- 代码片段：`JavaRDD<String> rawData = jsc.textFile(path: "F:/ml-100k/u.data"); //设置数据集文件`
- 代码片段：`JavaRDD<String[]> rawRatings = rawData.map(v1 -> v1.split(regex: "\t")); //将数据按照\t分割`
- 代码片段：`JavaPairRDD<Long, Rating> ratings = rawRatings.mapToPair(v1 -> { Rating rating = new Rating(Integer.valueOf(vl[0]), Integer.valueOf(vl[1]), Double.valueOf(vl[2])); return new Tuple2<>(Long.valueOf(vl[3]) % 10, rating); });`

画面2：
- 显示文件资源管理器，展示项目目录结构，包含 `ml-100k` 文件夹，其中包含 `u.data`、`u.item`、`u.user` 等数据文件。

画面3：
- 显示 IntelliJ IDEA 中的 Java 代码，继续处理电影数据，将电影ID和电影标题映射为 `Tuple2`。
- 代码片段：`List<Tuple2> movies = jsc.textFile(path: "F:/ml-100k/u.item").map(v1 -> { String[] ss = v1.split(regex: "\\|"); return new Tuple2<>(ss[0], ss[1]); }).collect();`

画面4：
- 显示 IntelliJ IDEA 中的 Java 代码，统计用户数量、电影数量和评分总数，并将数据集按比例划分为训练集、校验集和测试集。
- 代码片段：`Long numUsers = ratings.map(v1 -> (Rating) v1._2().user()).distinct().count();`
- 代码片段：`Long numMovies = ratings.map(v1 -> (Rating) v1._2().product()).distinct().count();`
- 代码片段：`System.out.println("用户：" + numUsers + " 电影：" + numMovies + " 评论：" + numRatings);`
- 代码片段：`Integer numPartitions = 4; // 分区数`
- 代码片段：`JavaRDD<Rating> training = ratings.filter(v -> v._1() < 6).values().repartition(numPartitions).cache();`

画面5：
- 显示 IntelliJ IDEA 中的 Java 代码，定义模型参数，包括模型秩、学习率、迭代次数等。
- 代码片段：`int[] ranks = new int[]{10, 11, 12};`
- 代码片段：`double[] lambdas = new double[]{0.02, 0.03, 0.2, 0.3, 1, 3};`
- 代码片段：`int[] numIters = new int[]{8, 9, 10, 11, 12, 13, 14, 15};`
- 代码片段：`int[] numRaters = new int[]{0, 5, 10};`

画面6：
- 显示 IntelliJ IDEA 中的 Java 代码，计算模型的均值、标准差和准确率提升，并构建最佳模型。
- 代码片段：`Double meanRating = training.union(validation).mapToDouble(v -> v.rating()).mean();`
- 代码片段：`Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> v1 + v2) / numTest);`
- 代码片段：`double improvement = (baselineRmse - testRmse) / baselineRmse * 100;`
- 代码片段：`System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");`
- 代码片段：`bestModel = ALS.train(ratings.values().rdd(), bestRank, bestNumIter, bestLambda);`

画面7：
- 显示 IntelliJ IDEA 中的 Java 代码，继续处理数据，统计用户和电影数量。
- 代码片段：`Long numUsers = ratings.map(v1 -> (Rating) v1._2().user()).distinct().count();`
- 代码片段：`Long numMovies = ratings.map(v1 -> (Rating) v1._2().product()).distinct().count();`
- 代码片段：`System.out.println("用户：" + numUsers + " 电影：" + numMovies + " 评论：" + numRatings);`

画面8：
- 显示 Typora 编辑器中的 Markdown 文件 `day08.md`，内容为课程大纲，包含章节标题和子标题。
- PPT 标题结构：
  1.4. 我的分组规则
  1.5. 项目架构
  1.5.1. QuanzMQService
  1.5.2. 修改
  1.5.3. MovementsController
  1.5.4. 接收消息
  1.5.5. 识别Last-tanhua-recommend工程
  1.5.6. 配置文件
  1.5.7. 测试
  1.7. 测试
  1.7.1. 发布动态
  1.7.2. 浏览动态
  1.7.3. 点赞
  1.7.4. 知晓动态
  1.7.5. 喜欢
  1.7.6. 知晓喜欢
  1.7.7. 评论
  2. 播放系统
  2.1. 乐播系统
  2.2. 重置app.properties
  2.3. MLlibRecommend
  2.4. SparkMongoDB
  2.5. 测试

画面9：
- 显示 IntelliJ IDEA 中的 Java 代码，与画面1类似，处理评分数据。
- 代码片段：`JavaRDD<String> rawData = jsc.textFile(path: "F:/ml-100k/u.data"); //设置数据集文件`
- 代码片段：`JavaRDD<String[]> rawRatings = rawData.map(v1 -> v1.split(regex: "\t")); //将数据按照\t分割`
- 代码片段：`JavaPairRDD<Long, Rating> ratings = rawRatings.mapToPair(v1 -> { Rating rating = new Rating(Integer.valueOf(vl[0]), Integer.valueOf(vl[1]), Double.valueOf(vl[2])); return new Tuple2<>(Long.valueOf(vl[3]) % 10, rating); });`

画面10：
- 显示 Typora 编辑器中的 Markdown 文件 `day08.md`，内容为课程大纲，包含章节标题和子标题。
- PPT 标题结构：
  1.4. 我的分组规则
  1.5. 项目架构
  1.5.1. QuanzMQService
  1.5.2. 修改
  1.5.3. MovementsController
  1.5.4. 接收消息
  1.5.5. 识别Last-tanhua-recommend工程
  1.5.6. 配置文件
  1.5.7. 测试
  1.7. 测试
  1.7.1. 发布动态
  1.7.2. 浏览动态
  1.7.3. 点赞
  1.7.4. 知晓动态
  1.7.5. 喜欢
  1.7.6. 知晓喜欢
  1.7.7. 评论
  2. 播放系统
  2.1. 乐播系统
  2.2. 重置app.properties
  2.3. MLlibRecommend
  2.4. SparkMongoDB
  2.5. 测试

画面11：
- 显示 IntelliJ IDEA 中的 Java 代码，与画面1类似，处理评分数据。
- 代码片段：`JavaRDD<String> rawData = jsc.textFile(path: "F:/ml-100k/u.data"); //设置数据集文件`
- 代码片段：`JavaRDD<String[]> rawRatings = rawData.map(v1 -> v1.split(regex: "\t")); //将数据按照\t分割`
- 代码片段：`JavaPairRDD<Long, Rating> ratings = rawRatings.mapToPair(v1 -> { Rating rating = new Rating(Integer.valueOf(vl[0]), Integer.valueOf(vl[1]), Double.valueOf(vl[2])); return new Tuple2<>(Long.valueOf(vl[3]) % 10, rating); });`

画面12：
- 显示 IntelliJ IDEA 中的 Java 代码，展示 `MLlibRecommend` 类的结构。
- 代码片段：`package com.tanhua.spark.mongo;`
