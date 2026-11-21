# 25.ALS算法流程之编码实战

- 阶段：07.阶段七 探花交友项目
- 章节：day07 探花交友-SparkMLlib推荐系统快速入门
- 源文件：07.阶段七 探花交友项目\day07 探花交友-SparkMLlib推荐系统快速入门\25.ALS算法流程之编码实战_【海量资源尽在 666java.com】.mp4
- 时长 12分0秒（音频 720s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续那么接下来呢我们来看一下我们具体的一个动手的一个实战那么前面呢我们已经讲过了数据的一个说明以及我们建模的一个这样的一个说明了那么接下来呢我们就实际的通过代码呢我们来看一下在Spark中呢使用这个Spark MLib所提供的一个ALS呢来实现一个电影的一个推荐
[00:27] 那么我们要实现的一个功能呢是给定一个用户的ID那么我们为这个用户呢去推荐几部啊感兴趣的这个电影那么推荐的依据呢就是我们前面的这个数据啊他的一些用户的评价的数据OK好那么接下来呢我们就动手呢来去呃写一下这个代码那我们来看一下那么首先呢我们来创建这个类啊叫做什么呢呃my啊recommend
[00:57] 那么我们来写一个这个类好然后呢在这个类里面呢我们去写一些相关的一些这个推荐的代码那么前面的还是呢我们需要定义一个叫做java Spark的contactorgsc然后呢去new一个java的contactorsparkcontactor然后呢我们上面呢要定义一个sparkspark怎么呢config
[01:25] 等于new一个sparkconfig然后呢去设置有两个参数对吧一个是appname那么一个呢就是master然后呢master呢就是叫local然后呢来一个新哎OK那么appname呢我们把这个呢就拿过来放到这儿然后呢把这个sparkconfig呢去丢到这里来对吧
[01:49] 然后呢我们这个是不是就已经定义好了最后呢就来一个JSC点什么呢stop哎呦ok好那么具体的代码逻辑呢在我们中间这个位置呢去完成首先第一步呢我们来读取我们的一个文件啊或者说我们的数据文件那么这个JSC呢点通过一个什么呢text fill去做一个读取那么文件的一个地址呢我把它放在哪里呢
[02:18] 放在我的这个F盘下面的有一个叫做code下面在F盘下面在这个位置有这样的一个数据那我们来考一下然后呢它下面的数据是谁呢是不是就这个u.date这样的一个文件那么我们来读取一下就它然后呢这个呢所读取到的就是我们最原始的一个这个数据了那我们就它叫source吧
[02:49] source RDDsource RDD就是我们原始的一个数据那么接下来呢我们是不是需要对这个文件呢做一个处理做什么处理呢是不是要做一个数据的一个这样的一个分割呀对吧那么中间这个呢它是什么呢通过这个table键那么也就是-t这样的一个分割那我们在这个位置呢需要对这个文件啊做一个分割啊分割的一个处理
[03:18] 那么通过什么呢-t啊对吧-t啊这样的一个分割处理那么我们通过这个source.rdd然后呢做一个map的一个操作然后呢我们去写一个lam的表达式然后呢v呢就等于什么呢去返回的就是一个v.split啊split所以呢-t啊-t哎ok那么这个呢就得到我们的一个
[03:44] 具体的一个我们的一个这个RDD对吧那我们就叫什么呢就叫这个具体的这个一行一行这个数据吧对吧那就LINE吧RDD好那么有了这个数据之后呢我们就需要对它做一些这个处理了那么我们最终呢是需要把我们这个数据中的这个这么几个数据然后呢去分装成一个Rating这样的一个对象
[04:13] 那么所以在这个位置呢我们这个line.rdd然后呢去做一个map这样的一个操作然后呢我们写一个还是写一个这个v啊v这个操作然后呢我们去给它new一个返回谁呢就是这个ratingrating这个对象啊返回一个这个对象那我们来看一下这个对象的一个定义啊那么它呢是由三个这个构造呃构造参数来组成
[04:43] 那么第一个呢是用户int型那么第二个呢是我们的商品啊是也是int型然后第三个呢就是评价是一个double类型的那么接下来呢我们就需要呢在这个位置啊来给他去哎看一下他提示啊是不是也是这个int型的对吧那我们就给他来这样的一个int型的一个啊这样的一个值啊那么我们呃那就这样来写吧我们还需要来一个大括号啊在大括号里面去来写一下
[05:13] 那把它剪切一下到这个位置呢我们通过这个V点我们拿到的V本身就已经split之后的对吧那我们就直接来使用吧那我们来看一下啊那么首先第一个这个参数啊那我们就不需要这个大括号了吧那就这样来写吧然后呢第一个这个参数啊第一个这个参数那么是int类型的对吧那么我们就value of然后呢V什么呢0对不对
[05:42] 那么第二个参数它是商品的ID对吧然后value of然后来一个V什么呢1对吧然后这个就对了再往后然后第三个参数第三个是double类型的我们就来一个double.value of然后V什么呢是不是3对吧这样的话是不是就OK了
[06:12] 那么现在是不是有一些这个哎这个怎么会多了一个中括号呢把这个中括号去掉好那么这样的话呢我们是不是就分装啊分装完成了我们这个数据啊对吧那么它的一个返回值呢我们是不是就会得到一个这个什么呢啊rating的一个rdd对吧啊rating这样的一个rdd这个大家应该能看懂吧我们去分装rating这样的一个对象那么我们来写一下啊这个就是我们去
[06:41] 转化啊得到得到这个对象集得到一个对象集好那么这个我们就不要紧加了RDD就写一个RatingRDD吧那么接下来呢我们就需要通过什么呢ALS所提供的这个Trend这个方法然后呢我们给他去做一个这个提供啊那么呃构造啊第一个呢就是我们需要给他的一个Ratings
[07:08] 那么是不是就是上面我们这个rating这个RDD对吧第一个这个对吧他需要的是一个RDD这个对象那我们是一个java RDD所以给他需要点一个RDD得到一个RDD对象那么第二个呢是这个rank这个参数这个参数呢我们前面说过是不是一般我们是设置什么呢设置我们的这个来看一下啊一般我们设置这个8到20之间就可以了那么比方说我们就设置8吧
[07:37] 然后呢第三个参数呢是它迭代的一个次数啊那么我们一般设置10就可以了OK那么这样的话我们将会得到一个我们的一个什么呢模型啊训练级或者模型这是我们的一个训练的一个模型啊得到它得到它之后呢我们就可以去我们去做一个推荐了通过这个什么呢module然后呢有一个recommendrecommend
[08:07] Podux去做这样的一个推荐那么我们可以看到是不是有两个参数一个呢就是Ura一个呢就是这个Number那么Ura呢就是用户啊然后呢就是推荐几个这样的一个产品那我们来看一下那么第一个呢比方说我们给一个用户啊我们随便来找一个这个用户吧这个里面有很多的用户比如说就谁呢301吧就他吧
[08:32] 我们为这个301这个用户去推荐10个啊这样的一个商品那么这个就是一个什么呢这就是我们的一个商品的一个推荐了那么我们来看一下它的返回值那是不是就得到这个推荐的一个啊这样的一个产品了对吧好那么接下来呢我们就就可以把我们的这个产品呢是不是就打印出来我们来看一下啊
[09:01] 那么我们去做一个for循环啊这样的一个操作然后呢我们就去做一个打印了比如说我们在这个prodact中呢就可以去拿到他的一些拿到一些他的一些属性我们可以看一下啊比如说他的一些这个user和这个这个就是什么呢就是prodact就是他的产品的这个ID啊那我们来看一下啊这个我们就写吧这个user
[09:30] 那么这个呢就是叫做user id啊等于谁呢加一个product点什么呢user然后呢再加一个谁呢这个product它呢就等于啊等于谁呢加一个这个product点好那么这个呢就是我们这个打印这个结果集啊打印这个结果集了哎OK
[10:01] 好那么我们尝试的来执行一下看他的一个这个结果怎么样好那么我们来稍微等待一下他的一个执行好那么我们来看一下这个结果结果呢其实就在这个位置打印出来了对吧为这个301的这个用户呢推荐了有这么多的一些这个商品对吧推荐了这么多商品那么在前面呢我们其实可以看到他反复的进行做了一些这个迭代的
[10:29] 迭代的一个交互输出然后去得到了这样的一个结果那么我们其实会发现了这个在做测试的时候这个打印的日志太多了我们其实希望的去把这个日日信息的我们来精简一下那我们可以是在这个位置去设置它的一个日志的一个级别比如说我们来设置一个什么的就是log的一个级别
[10:58] 那么我们比如说把它设置为什么呢这个警告这个级别对吧WRAN对吧然后呢这个就是一个设置日志的一个级别那么这个是应该是什么呢ARN对吧这样去设置日志的一个级别那我们再来执行一下来看一下它的一个结果好那么现在呢我们可以看到它的日志输出呢就今年很多了那么这样的话会方便我们去做一个测试
[11:28] 那么这个结果是其实跟我们刚才结果呢是一样但是可能推荐的商品呢会有所不同因为他去去得计算的时候都会有一个随机的一个矩阵啊在里面所以这个结果呢会有所不同啊哎呦OK好那么这个呢就是我们最基本的一个来使用MLlib中的一个这个ALS的一个推荐啊那么基本的一个API的使用呢那就是这样的哎呦OK
[11:56] 好那么关于这个实战呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.Spark;
import org.apache.Spark.SparkConf;
import org.apache.Spark.api.java.JavaSparkContext;
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

