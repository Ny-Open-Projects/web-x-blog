# 13.推荐系统之抽取Spark MLlib推荐逻辑

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\13.推荐系统之抽取Spark MLlib推荐逻辑_【海量资源尽在 666java.com】.mp4
- 时长 5分18秒（音频 318s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现我们的推荐那么我们主要呢也是使用Spark的MLlib来做一个具体的一个实现那么下面呢我们首先呢来回顾一下之前我们的所写的这个Magicon这样的一个程序那么这个代码大家应该还有印象那么就是那么我们大致的来
[00:25] 回顾一下就是那么首先呢我们去读取我们的这个文件啊那么这个是我们的数据文件那么在数据文件中呢会有一些相关的一些数据就是我们的用户啊对我们这个某些这个商品的这个评价啊那我们来找一下那么这个里面呢找到它然后呢这个下面呢会有一个叫U.DATE那我们来找一下叫什么呢U.DATE好打开这个EditPlus
[00:54] 然后我们去拖载过来那么是不是可以看到这个就是用户对吧用户对商品或者说电影它的一个评价是三星的这样的一个评价那么后面的这个是时间出那么大概是有这四个字段
[01:14] 那么我们去读到这个数据之后啊那么我们就需要对这个原数据呢去做一个处理那么我们对这个数据呢做一个map的一个操作那么首先呢对它去通过一个杠点的做一个这个分割然后呢我们得到一个这个rentins这样的一个加入RDD然后呢我们需要对它去
[01:39] 生成一个KV这样的一个结构那么K呢就是我们按照一个时间戳取余时取模这样的一个值作为我们的K那么值呢就是我们这个Rating这样的一个对象那么就是标准的一个就是用户评级的这样的一个数据模型那么就是用户然后呢就是商品或者说电影然后呢这个是评分这样的一个模型那么下面呢就是去
[02:09] 装载我们的一些电影的目录的数据啊以及统计用户和电影数量的一些这个统计的一些数目啊这样的一些相关的数据然后呢我们就去把我们的数据呢去做一个这个切分啊60%用于训练那么20%呢用于教验啊20%用于测试啊这样的一个处理然后呢在这个位置我们会去训练不同的一些这个模型
[02:37] 那么我们去取得这个最佳的一个这个模型那么然后呢就使用这个参数去得到一些这个模型啊最后呢就可以去拿到我们这个最优的这样的一个模型去做一个推荐了那么下面这个我们就不详细去说了前面我们都已经讲过了啊然后呢在最后啊其实在这个位置就会拿到什么呢拿到我们最优的一个这个模型
[03:04] 那么拿到模型的就可以去做一个推荐了那么其实就是我们这个方法主要呢其实就是我们要反拿到我们的最优的这样的一个模型那么就需要我们去传入什么呢传入我们的这个数据然后呢通过我们这个代码的一个计算啊然后呢得到最优的一个这个模型就可以进行做一个推荐了那么接下来呢我们来看一下我们的讲义啊那么在我们讲义中呢我们写了一个叫做什么呢叫MNLibRickMund
[03:32] 那么这个就是对我们前面代码做了一些抽取那么就说把前面的一些相关的一些代码把代码我们就去掉这个就去掉然后我们就直接的去把这个抽取出来然后我们只要传入我们java RDD的一个retins
[03:53] 然后呢我们去返回我们的一个最优的一个这个模型啊就可以了那我们就可以调用这个最优这个模型呢去做一个这个推荐了就这样的一个逻辑啊其实代码跟前面写的是一样的啊那么接下来呢我们就把这个类呢我们就来啊拷贝过来好拷贝一下然后呢我们进入到这个啊工程中好来看一下这个是我们Spark我们去我们去还需要把这个我们来看一下啊
[04:22] 这个包包呢它没有创建好对吧那我们需要去创建这样的一个包那我们就来创建一下吧创建一个这个哎错了那我们需要创建一个是一个package包好把它创建出来然后呢把它呢丢进来哎OK好那么这样的话呢我们这个第一个这个类呢我们就已经啊搞定了好那么这个呢我们就不需要再去看了其实就是做了一个分装
[04:51] 然后得到我们最优的这样的一个模型那么接下来重点我们是需要去编写英文逻辑然后去读取mongodb的数据然后调用我们这个方法得到我们的一个最优的一个模型然后我们再去做一个推荐ok好那么关于我们mlib的一个recommend这样的一个推荐模型的一个抽取我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
- 代码片段：`package com.tanhua.Spark.mongo;`

