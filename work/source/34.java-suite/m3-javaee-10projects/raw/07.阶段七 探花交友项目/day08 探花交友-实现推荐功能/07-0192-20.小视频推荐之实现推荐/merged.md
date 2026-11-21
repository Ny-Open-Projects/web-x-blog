# 20.小视频推荐之实现推荐

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\20.小视频推荐之实现推荐_【海量资源尽在 666java.com】.mp4
- 时长 4分34秒（音频 274s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就基于我们刚刚所构造的数据呢我们来实现这个推荐啊那么这个推荐呢和我们之前的这个圈子的这个推荐呢是非常的类似的那我们就直接来做一个拷贝了然后呢我们把它拷贝到我们的这个Spark这个工程中啊那我们来找一下找到Spark这个工程然后呢找到这个下面呢会有一个这个Mongo对吧那我们就来拷贝一下
[00:26] 那么我们把这个名字改一下吧同意一下就和我们上面我们就不要后面这个mongodb了那么就叫Spark一个video啊就可以了呃然后哎这个没改掉吗我们重新来改一下啊rename一下然后呢我们去把它去做一个修改呃然后呢他说这个里面是不是有有引用啊引用可能就修改不了对吧那我们就直接去把它去掉吧这个把它去掉
[00:58] 然后呢我们这个位置就改成它改成它然后呢我们再来修改一下这样的话就肯定就可以了对吧Rename Fail那么就把它MangoDB去掉好嘞这样的话就修改成功了然后呢我们来看一下这个里面的逻辑首先它也是去读取我们的外部的这个配置文件然后呢我们来看一下它呢是要读取的也是同样是我们的
[01:28] 这个就是这个URL但是呢要注意我们之前的这个URL它只是配置谁呢配置了我们的这个就是我们这个圈子的啊这样的一个库当然了我们现在要配置的是谁呢配置是我们这个小视频的对吧那我们需要把这个呢就拿过来啊这个拿过来那么要注意了那么前面这个是不变的啊这个是不变的啊这一定要搞清楚别搞错了然后呢拿过来
[01:56] 然后呢后面我们再去写这个位置啊那我们就来拷贝一下我们这个库的名字啊就是我们这个connection的名字拷贝一下然后呢我们放到这个位置来就是这个探花点就是我们这个库下面的这个表好那么然后呢这样的话呢我们就这个就搞定了然后呢我们再回到我们这个代码中啊那么它呢就完成这样的一个
[02:23] 配置啊那么这个名字也改一下把这个mongodb啊去掉然后呢我们来看一下那么下面的是构建上下文啊然后呢去加载mongodb中的这个数据然后呢我们对小视频呢做了不同的评价做合并啊这个你可以看到它的逻辑呢是完全一样的只是一些字段的不一样然后呢我们去得到用户的ID的集合然后呢我们按照这个
[02:49] 日期呢起于时起模的作为key这个rating这个对象的作为一个value去做一个数据的一个存储然后呢我们去定义我们的这个MLlib的Rickmond得到了一个这个就是best model这样的一个最优的一个模型然后呢下面我们去构造我们的redis的一个环境然后呢我们就可以去做推荐了为每一个这个用户推荐20条这个数据
[03:19] 然后呢我们把它最后保存到我们的ready中逻辑是不是完全一样啊当然这个里面是缺一个什么呢就是去缺一个这个点close对吧ok好那我们把这个呢也补充到我们的讲义中放到这个最下面来放到这好那么这样的话其实我们就已经完成了这个推荐了好那么我们就来执行一下来等待他的一个这个执行
[03:47] 好那么我们这个程序呢就跑完了跑完之后呢我们就来检查一下数据啊有没有那我们要进入到我们的redis中呢来查看一下然后呢设置一个1那么这个呢就是可以看到他所推荐的这个结果数据然后呢这个呢是2啊这个呢是3就是这样的话就完成了一些数据的推进啊然后呢我们其实可以看到呢是不是就
[04:13] 和我们之前的这个圈子一样啊那么也是有这样的一个这个数据那么下面我们其实只需要在我们这个查询逻辑中呢去做一下这个修改然后呢去查询我们的redis啊这样的话是不是就搞定了OK好那么关于我们这个推荐的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spark 和 MongoDB 实现视频推荐系统，并将推荐结果存储到 Redis 集群中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前章节为“4.6、实现推荐”，并显示了推荐系统代码中保存推荐结果到 MongoDB 的部分。
画面2：在 IntelliJ IDEA 中，右键点击 SparkVideoMongoDB.java 文件，弹出菜单，准备进行重构或操作。
画面3：在 IntelliJ IDEA 中，对代码进行重构操作，显示了“Refactoring Preview”窗口，提示“InputStream”在注释和非代码文件中出现1次。
画面4：在 IntelliJ IDEA 中，右键点击 SparkVideoMongoDB.java 文件，弹出菜单，准备进行重构或操作。
画面5：在 IntelliJ IDEA 中，展示 SparkVideoMongoDB.java 文件的代码，重点是加载外部配置文件并初始化 SparkConf。
画面6：在 IntelliJ IDEA 中，打开并显示了项目中的 app.properties 配置文件，其中包含 MongoDB 和 Redis 的连接配置。
画面7：在 IntelliJ IDEA 中，打开并显示了 app.properties 配置文件，其中包含 MongoDB 和 Redis 的连接配置。
画面8：在 IntelliJ IDEA 中，展示 SparkVideo.java 文件的代码，重点是加载配置、初始化 SparkContext 并从 MongoDB 加载数据。
画面9：在 IntelliJ IDEA 中，展示 SparkVideo.java 文件的代码，重点是处理数据，将用户-视频评分对转换为 Tuple2，然后按用户ID分组。
画面10：在 IntelliJ IDEA 中，展示 SparkVideo.java 文件的代码，重点是获取用户ID列表，并为每个用户生成评分数据。
画面11：在 IntelliJ IDEA 中，展示 SparkVideo.java 文件的代码，重点是初始化 MLlib 推荐模型并准备将推荐结果存储到 Redis。
画面12：在 IntelliJ IDEA 中，右键点击 SparkVideo.java 文件，弹出菜单，准备进行重构或操作。
画面13：在终端中，通过 Docker 进入 redis-node01 容器，并执行 redis-cli 命令连接到 Redis。
画面14：在终端中，执行 Redis 命令，获取名为 QUANZI_VIDEO_RECOMMEND_1 和 QUANZI_VIDEO_RECOMMEND_2 的键的值，显示推荐结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
this.mongoTemplate.save(recommendQuanzi, "recommend_video_20191007");
```

画面2：
```java
SparkVideoMongoDB {
    public static void main(String[] args) throws Exception{
        InputStream inputStream = SparkVideoMongoDB.class.getClassLoader().getResourceAsStream("app.properties");
        Properties properties = new Properties();
        properties.load(inputStream);
        SparkConf sparkConf = new SparkConf()
                .setAppName("SparkVideoMongoDB")
                .setMaster("local[*]")
                .set("Spark.mongodb.input.uri", properties.getProperty("Spark.video.mongodb.input.uri"));
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    }
}
```

画面3：
```java
InputStream inputStream = SparkVideoMongoDB.class.getClassLoader().getResourceAsStream("app.properties");
Properties properties = new Properties();
properties.load(inputStream);
```

画面4：
```java
SparkVideoMongoDB {
    public static void main(String[] args) throws Exception{
        InputStream inputStream = SparkVideoMongoDB.class.getClassLoader().getResourceAsStream("app.properties");
        Properties properties = new Properties();
        properties.load(inputStream);
        SparkConf sparkConf = new SparkConf()
                .setAppName("SparkVideoMongoDB")
                .setMaster("local[*]")
                .set("Spark.mongodb.input.uri", properties.getProperty("Spark.video.mongodb.input.uri"));
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    }
}
```

画面5：
```java
InputStream inputStream = SparkVideo.class.getClassLoader().getResourceAsStream("app.properties");
Properties properties = new Properties();
properties.load(inputStream);
SparkConf sparkConf = new SparkConf()
        .setAppName("SparkVideoMongoDB")
        .setMaster("local[*]")
        .set("Spark.mongodb.input.uri", properties.getProperty("Spark.video.mongodb.input.uri"));
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
```

画面6：
```properties
Spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua_recommend_quanzi
Spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua_recommend_quanzi
redis.cluster.nodes = 192.168.31.81:6379,192.168.31.81:6380,192.168.31.81:6381
```

画面7：
```properties
mongodb://192.168.31.81:27017/tanhua_recommend_quanzi_20191001?readPreference=primaryPreferred
```

画面8：
```java
//加载MongoDB中的数据
MongoRDD<Document> rdd = MongoSpark.load(jsc);
```

画面9：
```java
JavaRDD<Document> values = rdd.mapToPair(document -> {
    Integer user = document.getLong(key: "userId").intValue();
    Integer product = document.getLong(key: "videoId").intValue();
    Double score = document.getDouble(key: "score");
    Long date = document.getLong(key: "date");
    return new Tuple2<>(user + "_" + product, document);
});
```

画面10：
```java
List<Long> userIdList = rdd.map(v1 -> v1.getLong(key: "userId")).distinct().collect();
```

画面11：
```java
//通过MLlib模型进行推荐，获取到推荐的视频
MLlibRecommend mllibRecommend = new MLlibRecommend();
MatrixFactorizationModel bestModel = mllibRecommend.bestModel(ratings);
```

画面12：
```java
InputStream inputStream = SparkVideo.class.getClassLoader().getResourceAsStream("app.properties");
Properties properties = new Properties();
properties.load(inputStream);
SparkConf sparkConf = new SparkConf()
        .setAppName("SparkVideoMongoDB")
        .setMaster("local[*]")
        .set("Spark.mongodb.input.uri", properties.getProperty("Spark.video.mongodb.input.uri"));
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
```

画面13：
```bash
root@itcast:~# Docker exec -it redis-node01 /bin/bash
root@itcast:/data# redis-cli -c
127.0.0.1:6379>
```

画面14：
```bash
127.0.0.1:6379> get QUANZI_VIDEO_RECOMMEND_1
"1019,1041,1088,1023,1028,1065,1031,1086,1046,1046,1052,1053,1056,1063,1048,1061,1073"
127.0.0.1:6379> get QUANZI_VIDEO_RECOMMEND_2
"1046,1052,1053,1056,1063,1048,1061,1073,1046,1052,1053,1056,1063,1048,1061,1073"
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

