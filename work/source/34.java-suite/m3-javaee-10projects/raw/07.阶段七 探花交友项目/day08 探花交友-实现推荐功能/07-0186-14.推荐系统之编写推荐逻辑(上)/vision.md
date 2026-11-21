# 画面线理解：14.推荐系统之编写推荐逻辑（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\14.推荐系统之编写推荐逻辑（上）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:38, 02:46, 04:16, 05:49, 06:30, 09:40, 11:48, 12:51, 14:25, 15:12, 16:17, 17:35, 19:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:00:30

1) 这一组画面整体在讲如何使用 Spark Java API 从 MongoDB 加载数据、进行数据转换，并调用 MLlib 进行推荐模型训练。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 MLlibRecommend.java 文件中的代码，用于对评分数据进行分组和缓存，包括用户和电影数量统计、数据过滤和缓存操作。
画面 2: 展示了 SparkQunaZi.java 文件的 main 方法，开始加载外部配置文件 app.properties。
画面 3: 展示了 SparkQunaZi.java 文件中加载配置文件并创建 SparkConf 对象的代码，使用 setAll 方法设置配置。
画面 4: 展示了 SparkQunaZi.java 文件中设置 SparkConf 的 master 为 "local[*]"，并设置 MongoDB 输入 URI。
画面 5: 展示了 SparkQunaZi.java 文件中创建 JavaSparkContext，并加载 MongoDB 数据到 JavaMongoRDD。
画面 6: 展示了 SparkQunaZi.java 文件中打印 MongoDB 数据的 foreach 操作。
画面 7: 展示了 SparkQunaZi.java 文件中对数据进行 mapToPair 操作，准备进行聚合。
画面 8: 展示了 SparkQunaZi.java 文件中 mapToPair 的具体实现，提取用户ID和发布ID，并构造 Tuple2。
画面 9: 展示了 SparkQunaZi.java 文件中对数据进行 reduceByKey 操作，计算用户评分。
画面 10: 展示了 SparkQunaZi.java 文件中对数据进行 mapToPair 操作，提取用户ID和发布ID。
画面 11: 展示了 SparkQunaZi.java 文件中调用 MLlibRecommend.bestModel 方法进行模型训练。
画面 12: 展示了 SparkQunaZi.java 文件中对数据进行 map 操作，提取用户ID、发布ID和评分。
画面 13: 展示了 SparkQunaZi.java 文件中对数据进行 map 操作，提取日期和评分。
画面 14: 展示了 SparkQunaZi.java 文件中调用 MLlibRecommend.bestModel 方法进行模型训练。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
Long numUsers = ratings.map(v -> v._1()).distinct().count();
Long numMovies = ratings.map(v -> v._2()).distinct().count();
System.out.println("用户：" + numUsers + " 动态：" + numMovies + " ");

Integer numPartitions = 4; // 分区数

// 训练集
JavaRDD<Rating> training = ratings
        .filter(v -> v._1() < 6)
        .values()
        .repartition(numPartitions)
        .cache();

// 校验集
JavaRDD<Rating> validation = ratings
        .filter(v -> v._1() > 6 && v._1() < 8)
        .values()
        .repartition(numPartitions)
        .cache();

// 测试集
JavaRDD<Rating> test = ratings
```

画面 2:
```java
import java.io.InputStream;
import java.util.Properties;

public class SparkQunaZi {
    public static void main(String[] args) {
        //加载外部的配置文件 .app.properties
        InputStream inputStream = SparkQunaZi.class.getClassLoader().getResourceAsStream("app.properties");
```

画面 3:
```java
Properties properties = new Properties();
properties.load(inputStream);
```

画面 4:
```java
SparkConf sparkConf = new SparkConf()
        .setAppName("SparkQunaZi")
        .setMaster("local[*]")
        .set("spark.mongodb.input.uri", properties.getProperty("spark.mongodb.input.uri"));
```

画面 5:
```java
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
JavaMongoRDD<Document> rdd = MongoSpark.load(jsc);
```

画面 6:
```java
rdd.foreach(document -> System.out.println(document.toJson()));
```

画面 7:
```java
// 在数据中会存在，同一个用户对不同的动态（相同动态）进行操作，需要合并操作
rdd.mapToPair(document -> {
    Long userId = document.getLong(key: "userId");
    Long publishId = document.getLong(key: "publishId");
    return new Tuple2<>(userId + "_" + publishId, document);
});
```

画面 8:
```java
Function2<Document, Document, Document> func = document -> {
    Long userId = document.getLong(key: "userId");
    Long publishId = document.getLong(key: "publishId");
    double newScore = v1.getDouble(key: "score") + v2.getDouble(key: "score");
    return new Tuple2<>(userId, newScore);
};
```

画面 9:
```java
// 在数据中会存在，同一个用户对不同的动态（相同动态）进行操作，需要合并操作
rdd.mapToPair(document -> {
    Long userId = document.getLong(key: "userId");
    Long publishId = document.getLong(key: "publishId");
    return new Tuple2<>(userId + "_" + publishId, document);
});
```

画面 10:
```java
// 在数据中会存在，同一个用户对不同的动态（相同动态）进行操作，需要合并操作
rdd.mapToPair(document -> {
    Long userId = document.getLong(key: "userId");
    Long publishId = document.getLong(key: "publishId");
    return new Tuple2<>(userId + "_" + publishId, document);
});
```

画面 11:
```java
MLlibRecommend mLibRecommend = new MLlibRecommend();
mLibRecommend.bestModel(values);
```

画面 12:
```java
// 在数据中会存在，同一个用户对不同的动态（相同动态）进行操作，需要合并操作
rdd.mapToPair(document -> {
    Long userId = document.getLong(key: "userId");
    Long publishId = document.getLong(key: "publishId");
    return new Tuple2<>(userId + "_" + publishId, document);
});
```

画面 13:
```java
Long date = document.getLong(key: "date");
int userId = document.getLong(key: "userId").intValue();
int publishId = document.getLong(key: "publishId").intValue();
Double score = document.getDouble(key: "score");
Rating rating = new Rating(userId, publishId, score);
return new Tuple2<>(date % 10, rating);
```

画面 14:
```java
MLlibRecommend mllibRecommend = new MLlibRecommend();
MatrixFactorizationModel bestModel = mllibRecommend.bestModel(ratings);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
