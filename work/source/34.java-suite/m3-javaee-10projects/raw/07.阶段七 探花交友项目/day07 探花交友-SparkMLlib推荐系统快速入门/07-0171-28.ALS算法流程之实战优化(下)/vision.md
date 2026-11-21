# 画面线理解：28.ALS算法流程之实战优化（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\28.ALS算法流程之实战优化（下）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:42, 01:05, 01:18, 01:34, 01:51, 02:11, 02:25, 02:44, 02:58, 03:07, 03:18, 03:38, 04:15, 04:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:50:42

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中使用 ALS 算法训练推荐模型，并评估其性能，最终输出推荐结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示代码中计算测试数据集与最佳模型预测值之间的均方根误差（RMSE）的函数 computeRmse，以及程序结束语句 jac.stop()。
画面2：展示计算测试数据集在最佳模型下的 RMSE、均值评分、基线 RMSE 和提升百分比的代码，以及最终输出“最佳训练模型的准确率提升了”。
画面3：展示在代码中调用 ALS.train 方法训练模型，同时显示了 IDE 的自动补全建议。
画面4：展示在代码中调用 ALS.train 方法训练模型，同时显示了 IDE 的自动补全建议。
画面5：展示对评分数据进行划分，创建训练集、校验集和测试集的代码，包括过滤条件和缓存操作。
画面6：展示 PPT 页面，标题为“SparkMLlib推荐系统入门1md - Typora”，内容为课程大纲，其中包含“4.1.2 ALS算法”等章节。
画面7：展示代码中使用最佳模型进行推荐的逻辑，包括调用 recommendProducts 方法和打印推荐结果。
画面8：展示程序运行后的终端输出，显示“Compilation completed successfully in 2 s 482 ms (moments ago)”。
画面9：展示代码中使用最佳模型进行推荐的逻辑，包括调用 recommendProducts 方法和打印推荐结果。
画面10：展示代码中使用嵌套循环遍历不同参数（rank、lambda、numIter）训练模型，并记录最佳模型参数的逻辑。
画面11：展示代码中计算测试数据集在最佳模型下的 RMSE、均值评分、基线 RMSE 和提升百分比的代码，以及最终输出“最佳训练模型的准确率提升了”。
画面12：展示代码中使用最佳模型进行推荐的逻辑，包括调用 recommendProducts 方法和打印推荐结果。
画面13：展示初始化参数（ranks、lambdas、numIter）和最佳模型变量的代码。
画面14：展示 PPT 页面，标题为“SparkMLlib推荐系统入门1md - Typora”，内容为运行效果，包括数据集划分、模型评估结果和参数优化过程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
jac.stop();
```

画面2：
```java
double testRmse = computeRmse(bestModel, test, numTest);
System.out.println("测试数据集在 最佳训练模型 rank = " + bestRank + ", lambda = " + bestLambda +
        ", numIter = " + bestNumIter + " 的 RMSE = " + testRmse);
// 计算均值
Double meanRating = training.union(validation).mapToDouble(v -> v.rating()).mean();
// 计算标准差
Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> v1 + v2) / numTest);
// 计算准确率提升了多少
double improvement = (baselineRmse - testRmse) / baselineRmse * 100;
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
```

画面3：
```java
// 计算标准差
Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> v1 + v2) / numTest);
// 计算准确率提升了多少
double improvement = (baselineRmse - testRmse) / baselineRmse * 100;
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
// 构建最佳训练模型
MatrixFactorizationModel model = ALS.train(ratings.values().rdd(), bestRank, bestNumIter, bestLambda);
```

画面4：
```java
// 计算标准差
Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> v1 + v2) / numTest);
// 计算准确率提升了多少
double improvement = (baselineRmse - testRmse) / baselineRmse * 100;
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
// 构建最佳训练模型
MatrixFactorizationModel model = ALS.train(ratings.values().rdd(), bestRank, bestNumIter, bestLambda);
```

画面5：
```java
// 将评分数据按key值切成3个部分，分别用于训练（60%）、校验（20%）和测试（20%）
Integer numPartitions = 4; // 分区数
// 训练集
JavaRDD<Rating> training = ratings.filter(v -> v._1 < 6)
        .values()
        .repartition(numPartitions).cache();
// 校验集
JavaRDD<Rating> validation = ratings
        .filter(v -> v._1 >= 6 && v._1 < 8)
        .values()
        .repartition(numPartitions).cache();
// 测试集
JavaRDD<Rating> test = ratings
        .filter(v -> v._1 >= 8)
        .values()
        .repartition(numPartitions).cache();
```

画面6：
```markdown
4.1.2 ALS算法
```

画面7：
```java
// 使用最佳的训练模型进行推荐
Rating[] recommendProducts = model.recommendProducts(user, 10);
// 打印推荐结果
for (Rating rating : recommendProducts) {
    System.out.println(rating.user() + "->" + rating.product() + ":" + rating.rating());
}
jac.stop();
```

画面8：
```text
Compilation completed successfully in 2 s 482 ms (moments ago)
```

画面9：
```java
// 使用最佳的训练模型进行推荐
Rating[] recommendProducts = model.recommendProducts(user, 10);
// 打印推荐结果
for (Rating rating : recommendProducts) {
    System.out.println(rating.user() + "->" + rating.product() + ":" + rating.rating());
}
jac.stop();
```

画面10：
```java
for (int rank : ranks) {
    for (double lambda : lambdas) {
        for (int numIter : numIters) {
            MatrixFactorizationModel model = ALS.train(training.rdd(), rank, numIter, lambda);
            Double rmse = computeRmse(model, validation, numValidation);
            System.out.println("RMSE(校验集) = " + rmse + ", rank = " + rank + ", lambda = " + lambda + ", numIter = " + numIter);
            if (rmse < bestValidationRmse) {
                bestValidationRmse = rmse;
                bestModel = model;
                bestRank = rank;
                bestLambda = lambda;
                bestNumIter = numIter;
            }
        }
    }
}
```

画面11：
```java
// 计算均值
Double meanRating = training.union(validation).mapToDouble(v -> v.rating()).mean();
// 计算标准差
Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> v1 + v2) / numTest);
// 计算准确率提升了多少
double improvement = (baselineRmse - testRmse) / baselineRmse * 100;
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
// 构建最佳训练模型
MatrixFactorizationModel model = ALS.train(ratings.values().rdd(), bestRank, bestNumIter, bestLambda);
// 使用最佳的训练模型进行推荐
Rating[] recommendProducts = model.recommendProducts(user, 10);
// 打印推荐结果
for (Rating rating : recommendProducts) {
    System.out.println(rating.user() + "->" + rating.product() + ":" + rating.rating());
}
jac.stop();
```

画面12：
```java
// 使用最佳的训练模型进行推荐
Rating[] recommendProducts = model.recommendProducts(user, 10);
// 打印推荐结果
for (Rating rating : recommendProducts) {
    System.out.println(rating.user() + "->" + rating.product() + ":" + rating.rating());
}
jac.stop();
```

画面13：
```java
// 训练集、校验集、测试集划分
Integer numPartitions = 4; // 分区数
// 训练集
JavaRDD<Rating> training = ratings.filter(v -> v._1 < 6)
        .values()
        .repartition(numPartitions).cache();
// 校验集
JavaRDD<Rating> validation = ratings
        .filter(v -> v._1 >= 6 && v._1 <
