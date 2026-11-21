# 28.ALS算法流程之实战优化（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\28.ALS算法流程之实战优化（下）_【海量资源尽在 666java.com】.mp4
- 时长 5分51秒（音频 352s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们来看一下我们的运行的结果那么我们其实需要重点关注的是在下面的这两个输出那么我们最优的三个参数其实已经就拿到了对不对然后呢它的这个run可能是12这个lambda是0.01这个迭代数是9然后呢我们这个通过我们的一个最佳训练模型呢在测试我们的测试数据的时候
[00:29] 它的一个误差值呢是这个值啊2.00这个值啊然后呢我们的最佳的一个训练模型的准确度呢提升了97.49%所以看到这个提升的还是比较多的啊那么OK那么接下来呢我们将去根据我们啊所得到的一些这个三个最优的参数来构建啊构建我们的一个最佳训练模型
[00:56] 构建最佳训练模型那么要注意在这个位置呢我们去构建我们最佳训练模型的时候呢哎我们要使用谁呢呃要使用我们这个全部的这个数据啊全部的一个数据来看一下啊那么第一个呢就是我们的这个软体啊点什么呢rdd哎
[01:19] 对吧就是我们并不是用训练这个数据了就是我们全量的这个数据因为我们要做推荐嘛那么第一个参数它第二个呢是然后呢然后呢runc对吧第二个参数呢是迭代数迭代数第三个呢就是我们的一个lambda数量这样的话呢它是说这个是不是这个是参数是有问题的
[01:47] 那么前面的我们runting是一个java pair那么这样的话我们需要得到它的value对吧那么需要点一个什么呢拿到它的一个value再做一个rdd这样的话就可以了好那么我们这个时候拿到的才是我们真正的什么最佳的一个训练模型了那么接下来呢通过这个最佳训练模型那么就可以给我们去做一个推荐了那我们来看一下对不对那我们就做推荐那么这个代码就跟我们刚刚的代码呢是一样了
[02:17] 那我们就来使用一下我们就直接来拷贝过来吧那么我们就用这个最佳的这个训练模型这个来我们来写一下使用最佳的训练模型模型进行推荐进行推荐我们给这个789这个用户来推荐10个这个商品来我们来执行一下走好那我们来等待他的一个执行
[02:44] 好那我们来看一下这个结果这个结果呢其实就是为我们的这个789去推荐啊这么几个这个电影啊那么这样的话就推荐出来了OK好那么其实这样的话呢我们就得到我们最终的一个结果其实我们需要把这个代码给大家去
[03:03] 总结一下其实我们写这么多代码的一个意义所在的就是我们需要去不断的去计算得到我们这三个关键的参数然后得到一个最优的参数然后使用我们最优的参数来给我们去做最终的一个推荐也就是说
[03:23] 我们最终的API的使用还是使用最核心的这一块就是做一个推荐只是说它的一些model的设置需要它的参数它的model参数的设置是需要我们去做一些计算
[03:39] 才能够得到的这样的一些这个参数这样的一个训练的一个模型的那么这一点啊大家应该要掌握啊那么我们呢在后面的项目中呢也会去使用这样的方法来得到我们的一个最佳的一个model使用这个model呢再去做我们的一个推荐啊OK
[03:58] 好那么关于我们这个实战的一个优化呢那我们就先讲到这里那么希望大家能够去把它呢去实际的来动手去写一遍啊然后呢去运行一下看一下这个结果那么大家呢也可以按照我所说的刚才呢把这个注释呢打开就是说把这个
[04:20] 打开然后呢把下面这个注视掉然后呢去寻找啊最优的这个Lambda最终结果可能又不一样了啊OK好那我还是把它注视掉吧好那么接下来呢我们来看一下下面的一个运行结果吧运行结果跟我们刚刚的是一样的啊然后呢呃最后的一个总结我们可以看一下啊就是我们总共呢有943个用户然后呢1682个店已经去从了有10万条呃用户的这个评价
[04:50] 然后我们把数据分成三部分60%用于训练20%用于教研20%用于测试那么这个事我们是不是也做到了对吧然后模型在不同的参数下面去计算它的一个这个什么的RMS一值就是标准误差值然后我们去找到最小的一个值就是它最优的一个参数的一个建模
[05:17] 目的是不是就是通过这个最小误差值来找到最优的一个参数来建模这个是我们的一个目的我们使用20%的一个测试模型来测试我们这个模型的一个好坏也就是还是去计算它的一个这个标准误差那么在这个我们最优的这个参数上面提升了多少那么这个准确率可能和你每次执行可能会有些不一样OK这个大家注意一下
[05:45] 好嘞好那么关于我们这个优化改进呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

