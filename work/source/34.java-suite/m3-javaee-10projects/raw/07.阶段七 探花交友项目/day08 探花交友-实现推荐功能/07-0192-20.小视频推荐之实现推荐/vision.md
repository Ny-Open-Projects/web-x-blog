# 画面线理解：20.小视频推荐之实现推荐

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\20.小视频推荐之实现推荐_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:27, 00:46, 01:07, 01:21, 01:43, 02:02, 02:21, 02:44, 03:10, 03:34, 03:43, 03:54, 04:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:05:41

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
                .set("spark.mongodb.input.uri", properties.getProperty("spark.video.mongodb.input.uri"));
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
                .set("spark.mongodb.input.uri", properties.getProperty("spark.video.mongodb.input.uri"));
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
        .set("spark.mongodb.input.uri", properties.getProperty("spark.video.mongodb.input.uri"));
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
```

画面6：
```properties
spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua_recommend_quanzi
spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua_recommend_quanzi
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
        .set("spark.mongodb.input.uri", properties.getProperty("spark.video.mongodb.input.uri"));
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
```

画面13：
```bash
root@itcast:~# docker exec -it redis-node01 /bin/bash
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
