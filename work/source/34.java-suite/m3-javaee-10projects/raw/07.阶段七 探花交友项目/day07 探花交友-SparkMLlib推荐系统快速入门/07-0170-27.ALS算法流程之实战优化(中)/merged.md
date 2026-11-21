# 27.ALS算法流程之实战优化（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\27.ALS算法流程之实战优化（中）_【海量资源尽在 666java.com】.mp4
- 时长 9分43秒（音频 583s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们将训练不同的这个参数下面的这个模型啊那么我们就先把这个就拷贝过来吧这个就是我们需要去做一个训练的啊这样的一些这个参数啊那么来看一下那么我们需要呢有设置有这个runc这个参数那么有10 11 12对吧还有lambda呢有这个0.0.1 0.0.3 0.1 0.3 1和3
[00:29] 那么这个呢其实是一个经验之谈啊就是Lambda呢我们最好设置为是3的这样的一个倍数去做一个设置啊所以我默认的给它设置为就是0.01但它的默认值就是0.01啊然后呢还有迭代的一个次数呢是8 90那么也可以设置这么多因为这个是由于我们测试的一个关系啊就是你设置的这个参数越多那么我们测试的时间需要花费的越长啊为了我们一会演示的快速得到一个
[00:57] 结果的话我们就按照这么简单的去做一些这个测试啊那么如果大家在做学习的时候呢可以把这几个去改一下就是我可以使用这个去做一个测试啊哎呀OK好那么下面呢我们把这几个也拿过来吧就是这几个这个定义的一些变量啊那我们来给大家来解释一下啊就是我们先定义一个我们最优的一个这个model设置为一个null然后呢我们定义我们的
[01:27] 最就是我们去做一个校验的一个它的一个误差值的先设置为是一个double的一个最大值然后因为这个值我们一会有用然后我们去设置它的最优的一个run格lambda number还叠代数等等然后我们先把它设置为一个给它一个初始值那么接下来要注意了那么在这个位置我们需要对上面的三个上面的三个
[01:57] 这个参数做什么呢循环做循环这里呢使用什么呢使用这个三层嵌套嵌套循环来测试好什么意思呢就是我们需要去对上面的去做一个循环了比如说我们就先循环这个runc对吧然后呢我们再去循环谁呢循环这个lambda
[02:22] 然后呢我们再去循环我们的这个迭代的一个数量通过这三个值我们去不断的去拿到我们的一个这个model拿到一个model那我们就需要去给它去设置我们的这个als去设置我们的训练级的一个模型了对吧那么我们就设置应该用这个吧那么首先第一个呢是我们需要去训练的一个集合
[02:52] 那我们所需要需要使用训练的集合呢并不是之前的rating而是我们被分割出来60%的这个数据叫做我们的训练集放到这然后呢第二个这个参数呢就是我随着我们的这个runc这个参数对不对把它呢丢过来那么第三个这个参数那就是谁呢看一下啊那么第三个就是我们的一个这个就是便利啊便利数量那么最后一个啊最后哎
[03:22] 最后一个的设置就是lambda这个参数大家也可以把那个就是我们的这个循环的这个顺序调一下也可以不调也行这样都可以一样的那么来看一下他所需要的是一个rdd而我们现在是一个java的rdd那就得到一个什么的rdd这样的话呢就ok了那我们通过他呢就会得到我们的一个这个模型model
[03:50] 那么通过它呢就会得到我们的一个这个模型那么这个模型我们怎么样去对比它是最优的呢我们需要通过一个算法来做一个实践那我们一起来看一下啊那么这个算法呢是在这儿就是说我们需要去定义下面的这样的一个这个方法那么这个算法呢我就不去编写了啊我就直接来拷贝过来了
[04:15] 那么放到这里来看一下这个算法的一个它的一个意思就是我们去计算我们的一个这个预测的一个数据跟我们实际数据之间的一个什么呢这个均方根的一个这样的一个误差那么就是说我们去传入我们的一个这个模型然后再传入我们的一个这个数据传入一个预测的一个数据
[04:44] 然后呢跟我们实际的一个结果呢去做一个这个差值可以看到在这个位置去做一个差值然后呢去做一个平方根去得到一个他们之间的一个标准的一个误差然后呢计算这个误差的一个大小按照最小的这个误差就会找到什么呢最优的一个模型所以我们的一个方法呢是这样的一个方法好那么我们在上面呢我们就会去
[05:11] 调用这个方法呢我们去啊我们去做一个这个计算对吧那么他需要呢有三个参数那么第一个呢是model那么把这个model呢啊传递给他那么第二个参数呢是一个date要注意这个date呢我们需要做随着做我们教验的啊这个data那么我们把这个data呢就给他传递过去了那么valid data而这个数量呢我们就是这个哎这个valid data的这个数量啊也传递过去哎ok
[05:41] 那么它呢将得到一个什么呢得到我们的一个误差这个值那么我们可以把这个误差呢打印出来啊那我就直接来做一个拷贝这个打印的内容吧那把它呢就拿过来了然后呢放到这哎哎丢到这好那么我们来看一下打印的这个误差这个值呢其实就是在这啊打印出来然后呢我们去做一个判断判断什么呢
[06:10] 如果我们这个误差小于谁呢小于我们上面所定义的这个误差那么如果小于他我们就认为这个是最优的当然也不是最优了就是比较优化的一个我们就可以把它记录下来了对不对那么这个model我们就应该来这个best这个model那么就等于这个model了我们记录一下这个就是我最优的一个model
[06:37] 我们分别呢把这三个值呢都给它记录下来哎这个叫什么呢runc那我们要记录这么几个值了这个这个best lambda对于lambda哎哎错了然后呢还有一个是我们的一个迭代数对吧等于我们看一下是它好那我们把它就记录下来了这个大家能不能够理解啊就是说
[07:06] 我们当然了还有这个数量我们也需要去调一下对吧那么这个数量我们记录就是刚才的这个标准的这个误差值那么等到他下一次循环的时候每一次是不是都会去做一个记录对吧那么记录他的一个这个值那么最终我们是不是就会得到一个误差最小的一个这个model那么也就是说最终我们就能够得到误差最小的model然后其中的这三个参数那么就可以得到谁呢
[07:36] 得到我们最佳的一个训练级这个大家理解了吗那么关键点其实就在这里OK好那我们来看一下我们的讲义是不是跟我们写的这个是一样的对吧好那么接下来我们就需要去根据我们的一个最佳的一个训练模型去做一个计算那我们就把这个来计算一下吧计算谁呢计算我们的测试模型来看一下那么我们在这吧来看一下
[08:05] 那么我们是不是这样吧我们先不做这个计算了我们先来运行一次吧看一下他的一个这个输出啊看一下结果啊然后呢我们先执行一下好那我们来等待他的一个执行好那么我们来看一下这个运行的一个结果啊那么大致的我们会运行这么多那么其实我们现在已经就得到最佳的这样的一个训练级了对吧好那么接下来呢我们将使用我们最佳的这个训练级模型呢
[08:34] 我们来做一个测试就是来测试谁呢测试我们的一个test那就是我们前面所拿到的一个20%的数据的一个测试集的这样的一个数据然后呢我们来看他的一个这个测试的一个这个结果那么并且呢我们需要去计算一下什么他的一个这个相关的一个这个差值那我们把这个也拿过来吧拿过来我们来看一下
[09:03] 好那我们就放到这吧来我们来看一下这么几个代码是什么意思啊就是我们去计算它的一个平均的一个值然后呢计算一个它的标准这样的一个误差然后呢我们重点呢是要去计算它的计算准确率提升了多少啊那么用这个标准的这个误差去减去我们平均的这个误差然后呢去再除以啊再除以我们的这个
[09:32] 标准的这个误差值然后呢就可以看到他已经是提升了多少了那我们可以来看一下这个结果啊我来运行一下走

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

