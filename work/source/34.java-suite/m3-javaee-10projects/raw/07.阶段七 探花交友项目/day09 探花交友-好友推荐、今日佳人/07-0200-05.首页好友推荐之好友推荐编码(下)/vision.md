# 画面线理解：05.首页好友推荐之好友推荐编码（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\05.首页好友推荐之好友推荐编码（下）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:18, 02:10, 03:36, 05:09, 06:21, 07:54, 09:29, 10:18, 11:34, 12:52, 14:26, 15:36, 16:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:11:26

1) 这一组画面整体在讲如何使用 Spark MLlib 构建用户推荐系统，并将推荐结果写入 MongoDB 数据库。

2) 按时间顺序列出每张画面的要点：
画面1：展示 SparkUserRecommend.java 中的代码，用于计算用户间相似度（基于城市和学历），生成 Rating 对象并返回 Tuple2。
画面2：在代码中调用 MLlib 的 MatrixFactorizationModel，准备进行推荐计算。
画面3：在 Navicat Premium 中查看 tb_user_info 表的数据，展示用户信息（如 user_id, nick_name, city, age, edu 等字段）。
画面4：在 Navicat Premium 中继续查看 tb_user_info 表的数据，聚焦于部分用户记录。
画面5：在代码中调用 MLlib 的 bestModel 方法，准备进行推荐计算。
画面6：在代码中创建 JavaSparkContext，并调用 bestModel.recommendProducts 方法。
画面7：在代码中使用 for 循环遍历用户 ID，调用 bestModel.recommendProducts 方法。
画面8：在代码中使用 Document 对象封装推荐结果。
画面9：在代码中使用 MongoSpark.save() 方法将推荐结果写入 MongoDB。
画面10：在 Typora 中查看 day09 讲义，展示 Spark 与 MongoDB 的配置信息（包括 spark.mongodb.input.uri、spark.mongodb.output.uri、j dbc.driver-class-name 等）。
画面11：在 Typora 中查看 day09 讲义，展示用户推荐的代码逻辑和流程图。
画面12：在代码中使用 MongoSpark.save(documentJavaRDD) 方法将推荐结果写入 MongoDB。
画面13：在 Advanced REST Client 中发送 POST 请求，用于用户登录验证。
画面14：在 Typora 中查看 day09 讲义，展示用户信息的 JSON 数据结构（包含 user_id, avatar, gender, tags, favoriteValue 等字段）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
if (StringUtils.equals(city1, city2)) {
    score += 20;
}
// 计算学历
String edu1 = row1.getString(i7);
String edu2 = row2.getString(i7);
if (StringUtils.equals(edu1, edu2)) {
    score += 20;
}
Rating rating = new Rating(userId1.intValue(), userId2.intValue(), score);
return new Tuple2<>(key % 10, rating);
```

画面2：
```java
Rating rating = new Rating(userId1.intValue(), userId2.intValue(), score);
return new Tuple2<>(key % 10, rating);
```

画面5：
```java
// MLlib进行计算最佳的推荐模型
MLlibRecommend mLibRecommend = new MLlibRecommend();
MatrixFactorizationModel bestModel = mLibRecommend.bestModel(javaPairRDD);
```

画面6：
```java
// MLlib进行计算最佳的推荐模型
MLlibRecommend mLibRecommend = new MLlibRecommend();
MatrixFactorizationModel bestModel = mLibRecommend.bestModel(javaPairRDD);

// 将数据写入MongoDB中
JavaSparkContext jsc = new JavaSparkContext(sparkSession.sparkContext());
```

画面7：
```java
// MLlib进行计算最佳的推荐模型
MLlibRecommend mLibRecommend = new MLlibRecommend();
MatrixFactorizationModel bestModel = mLibRecommend.bestModel(javaPairRDD);

// 将数据写入MongoDB中
JavaSparkContext jsc = new JavaSparkContext(sparkSession.sparkContext());

for (Long userId : userIds) {
    bestModel.recommendProducts(userId.intValue(), num: 0);
}
```

画面8：
```java
Document document = new Document();
```

画面9：
```java
// 将数据写入MongoDB中
JavaSparkContext jsc = new JavaSparkContext(sparkSession.sparkContext());

for (Long userId : userIds) {
    Rating[] ratings = bestModel.recommendProducts(userId.intValue(), num: 0);
    jsc.parallelize(Arrays.asList(ratings)).map(v1 -> {
        Document document = new Document();
        return document;
    });
}
MongoSpark.save();
```

画面10：
```yaml
spark.mongodb.input.uri = mongodb://192.168.31.11:27017/tanhuai.recommend.video_20191007
spark.mongodb.output.uri = mongodb://192.168.31.11:27017/tanhuai.recommend_video_20191007
```

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

```java
package com.tanhuai.spark.mongo;
import org.apache.commons.lang.StringUtils;
import org.apache.commons.lang3.StringUtils;
```

画面11：
```java
// 用户MongoDB的写入
JavaSparkContext jsc = new JavaSparkContext(sparkSession.sparkContext());
for (Long userId : userIds) {
    // 为用户推荐50个相似用户
    Rating[] recommendProducts = bestModel.recommendProducts(userId.intValue(), 50);
    JavaRDD<Document> docs = jsc.parallelize(Arrays.asList(recommendProducts)).map(v1 -> {
        Document document = new Document();
        return document;
    });
}
MongoSpark.save(docs);
```

画面12：
```java
Document document = new Document();
document.put("_id", ObjectId.get());
document.put("userId", v1.product());
document.put("toUserId", v1.user());
// 评分
double score = new BigDecimal(v1.rating()).setScale(newScale, BigDecimal.ROUND_DOWN);
document.put("score", score);
document.put("date", new DateTime().toString("yyyy/MM/dd"));
return document;
```

画面13：
```json
{
  "phone": "1800226895",
  "verificationCode": "123456"
}
```

画面14：
```json
{
  "user_id": 97,
  "avatar": "https://img.tanhuai.see.on-shanghai.aliyuncs.com/images/logo/10.jpg",
  "gender": "woman",
  "tags": [
    "运营",
    "求职",
    "好物推荐"
  ],
  "favoriteValue": 62
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面10：PPT 标题为“day09 讲义”，内容包括 Spark 与 MongoDB 的配置信息（spark.mongodb.input.uri、spark.mongodb.output.uri、j dbc.driver-class-name 等）。
画面11：PPT 标题为“day09 讲义”，内容包括用户推荐的代码逻辑和流程图。
画面14：PPT 标题为“day09 讲义”，内容包括用户信息的 JSON 数据结构（包含 user_id, avatar, gender, tags, favoriteValue 等字段）。

5) 不要评价画面美观，不要输出与课程无关的内容。
