# 画面线理解：27.ALS算法流程之实战优化（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\27.ALS算法流程之实战优化（中）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 02:21, 02:44, 03:20, 04:08, 05:08, 05:48, 06:00, 06:35, 07:00, 07:48, 08:14, 08:41, 09:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:49:51

1) 这一组画面整体在讲如何使用 Spark MLlib 的 ALS（交替最小二乘法）算法进行推荐系统模型训练，并通过三层嵌套循环遍历不同参数组合，选择在验证集上表现最优的模型用于测试集评估。

2) 按时间顺序列出每张画面的要点：
画面1: 显示代码中对评分数据集进行过滤、分组和缓存，计算训练集、验证集和测试集的样本数量，并打印统计信息。
画面2: 定义了用于参数调优的三个数组：ranks、lambdas、numIters，以及用于记录最优模型参数的变量。
画面3: 在三层嵌套循环中，使用 ALS.train 方法训练模型，并通过代码补全提示选择 ALS 类。
画面4: 在三层嵌套循环中，使用 ALS.train 方法训练模型，并通过代码补全提示选择 ALS 类。
画面5: 显示了 computeRmse 方法的实现，用于计算模型在数据集上的均方根误差（RMSE）。
画面6: 显示了 computeRmse 方法的实现，用于计算模型在数据集上的均方根误差（RMSE）。
画面7: 显示了 computeRmse 方法的实现，用于计算模型在数据集上的均方根误差（RMSE）。
画面8: 在三层嵌套循环中，训练模型并计算验证集的 RMSE。
画面9: 在三层嵌套循环中，如果当前模型的 RMSE 小于当前最优 RMSE，则更新最优模型和参数。
画面10: 在三层嵌套循环中，如果当前模型的 RMSE 小于当前最优 RMSE，则更新最优模型和参数。
画面11: 显示了 computeRmse 方法的实现，用于计算模型在数据集上的均方根误差（RMSE）。
画面12: 显示了使用最优模型计算测试集的 RMSE，并打印结果。
画面13: 显示了计算训练集、验证集和测试集样本数量的代码，并打印统计信息。
画面14: 显示了计算测试集 RMSE、均值、基线 RMSE 和改进率的代码，并打印结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
// 测试集
JavaRDD<Rating> test = ratings
.filter(v -> v._1() >= 8)
.values()
.repartition(numPartitions).cache();

Long numTraining = training.count();
Long numValidation = validation.count();
Long numTest = test.count();
System.out.println("训练集：" + numTraining + " 校验集：" + numValidation + " 测试集：" + numTest);
```

画面2:
```java
// 对上面的三个参数做循环，这里使用三层嵌套循环来测试
for (int rank : ranks) {
    for (double lambda : lambdas) {
        for (int numIter : numIters) {
            ALS.train(training.rdd(), rank, numIter, lambda);
        }
    }
}
jac.stop();
```

画面3:
```java
// 对上面的三个参数做循环，这里使用三层嵌套循环来测试
for (int rank : ranks) {
    for (double lambda : lambdas) {
        for (int numIter : numIters) {
            ALS.train(training.rdd(), rank, numIter, lambda);
        }
    }
}
jac.stop();
```

画面4:
```java
// 对上面的三个参数做循环，这里使用三层嵌套循环来测试
for (int rank : ranks) {
    for (double lambda : lambdas) {
        for (int numIter : numIters) {
            ALS.train(training.rdd(), rank, numIter, lambda);
        }
    }
}
jac.stop();
```

画面5:
```java
if (validationRmse < bestValidationRmse) {
    bestModel = model;
    bestValidationRmse = validationRmse;
    bestRank = rank;
    bestLambda = lambda;
    bestNumIter = numIter;
}

double testRmse = computeRmse(bestModel, test, numTest);
System.out.println("测试数据集在 最佳训练模型 rank = " + bestRank + ", lambda = " + bestLambda + ", numIter = " + bestNumIter + " 上的 RMSE = " + testRmse);

// 计算均值
Double meanRating = training.union(validation).mapToDouble(v -> v.rating()).mean();

// 计算基线误差
Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> (v1 + v2) / numTest));

// 计算准确率提升了多少
double improvement = (baselineRmse - testRmse) / baselineRmse * 100;
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
```

画面6:
```java
// 计算均值
Double meanRating = training.union(validation).mapToDouble(v -> v.rating()).mean();

// 计算基线误差
Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> (v1 + v2) / numTest));

// 计算准确率提升了多少
double improvement = (baselineRmse - testRmse) / baselineRmse * 100;
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
```

画面7:
```java
// 计算均值
Double meanRating = training.union(validation).mapToDouble(v -> v.rating()).mean();

// 计算基线误差
Double baselineRmse = Math.sqrt(test.map(v -> (meanRating - v.rating()) * (meanRating - v.rating())).reduce((v1, v2) -> (v1 + v2) / numTest));

// 计算准确率提升了多少
double improvement = (baselineRmse - testRmse) / baselineRmse * 100;
System.out.println("最佳训练模型的准确率提升了：" + String.format("%.2f", improvement) + "%");
```

画面8:
```java
// 对上面的三个参数做循环，这里使用三层嵌套循环来测试
for (int rank : ranks) {
    for (double lambda : lambdas) {
        for (int numIter : numIters) {
            MatrixFactorizationModel model = ALS.train(training.rdd(), rank, numIter, lambda);
            Double rmse = computeRmse(model, validation, numValidation);
            System.out.println("RMSE(校验集) = " + rmse + ", rank = " + rank + ", lambda = " + lambda + ", numIter = " + numIter);
        }
    }
}
jac.stop();
```

画面9:
```java
// 对上面的三个参数做循环，这里使用三层嵌套循环来测试
for (int rank : ranks) {
    for (double lambda : lambdas) {
        for (int numIter : numIters) {
            MatrixFactorizationModel model = ALS.train(training.rdd(), rank, numIter, lambda);
            Double rmse = computeRmse(model, validation, numValidation);
            System.out.println("RMSE(校验集) = " + rmse + ", rank = " + rank + ", lambda = " + lambda + ", numIter = " + numIter);
            if (rmse < bestValidationRmse) {
                bestModel = model;
                bestValidationRmse = rmse;
                bestRank = rank;
                bestLambda = lambda;
                bestNumIter = numIter;
            }
        }
    }
}
jac.stop();
```

画面10:
```java
// 对上面的三个参数做循环，这里使用三层嵌套循环来测试
for (int rank : ranks) {
    for (double lambda : lambdas) {
        for (int numIter : numIters) {
            MatrixFactorizationModel model = ALS.train(training.rdd(), rank, numIter, lambda);
            Double rmse = computeRmse(model, validation, numValidation);
            System.out.println("RMSE(校验集) = " + rmse + ", rank = " + rank + ", lambda = " + lambda + ", numIter = " + numIter);
            if (rmse < bestValidationRmse) {
                bestModel = model;
                bestValidationRmse = rmse;
                bestRank = rank;
                bestLambda = lambda;
                bestNumIter = numIter;
            }
        }
    }
}
jac.stop();
```

画面11:
```java
if (validationRmse < bestValidationRmse) {
    bestModel = model;
    bestValidationRmse = validationRmse;
    bestRank = rank;
    bestLambda = lambda;
    bestNumIter = numIter;
}

double testRmse = computeRmse(bestModel, test, numTest);
System.out.println("测试数据集在 最佳训练模型 rank = " + bestRank + ", lambda = " + bestLambda + ", numIter = " + bestNumIter + " 上的 RMSE = " + testRmse);

// 计算均值
Double meanRating = training.union(validation).mapToDouble(v -> v.rating()).mean();

// 计算基线误差
