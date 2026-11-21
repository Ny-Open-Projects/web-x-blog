# 画面线理解：15.推荐系统之编写推荐逻辑（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\15.推荐系统之编写推荐逻辑（下）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:58, 02:09, 02:38, 03:11, 03:57, 05:08, 05:47, 06:41, 07:56, 09:13, 09:47, 11:07, 11:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:01:16

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 项目中使用 MLlib 构建推荐模型，并将推荐结果缓存到 Redis 集群中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Spark 项目结构，当前编辑的是 `SparkQunZi.java` 文件。
- 代码片段：将 MongoDB 中的评分数据转换为 `Rating` 对象并返回 `Tuple2`。
- 代码片段：初始化 `MLlibRecommend` 和 `MatrixFactorizationModel`。

画面 2：
- 展示了 Spark RDD 的常用转换操作（如 `cache`, `collect`, `coalesce` 等）。
- 代码片段：对 `user` 字段进行去重操作。

画面 3：
- 展示了推荐算法的核心逻辑：对每个用户调用 `recommendProducts` 方法获取推荐结果。
- 代码片段：`recommendProducts` 方法返回一个 `Rating` 数组。

画面 4：
- 展示了推荐结果的打印逻辑：遍历推荐结果并输出用户ID和商品ID。
- 代码片段：`System.out.println(product.user() + ":" + product.product());`

画面 5：
- 与画面 4 几乎相同，只是代码行号略有不同，强调了循环体内的打印逻辑。

画面 6：
- 开始编写 Redis 缓存逻辑，注释为“//连接redis，做存储”。
- 代码片段：`Set<HostAndPort> nodes = new HashSet<>();`

画面 7：
- 从 `app.properties` 文件中读取 Redis 集群节点配置。
- 代码片段：`String redisNodesStr = properties.getProperty("redis.cluster.nodes");`

画面 8：
- 将 Redis 集群节点字符串按逗号分隔，然后按冒号分割成 `HostAndPort` 对象。
- 代码片段：`String[] ss = StringUtils.split(nodesStr, separatorChar:':');`

画面 9：
- 继续构建 `JedisCluster` 对象，将 `HostAndPort` 对象添加到集合中。
- 代码片段：`nodes.add(new HostAndPort(ss[0], Integer.valueOf(ss[1])));`

画面 10：
- 完成 `JedisCluster` 对象的初始化。
- 代码片段：`JedisCluster jedisCluster = new JedisCluster(nodes);`

画面 11：
- 开始编写将推荐结果写入 Redis 的逻辑。
- 代码片段：`jedisCluster.set(key, value);`

画面 12：
- 切换到终端，执行 Docker 命令进入 Redis 容器并启动 Redis CLI。
- 命令：`docker exec -it redis-node01 /bin/bash`
- 命令：`redis-cli -c`

画面 13：
- 展示了 Markdown 文档 `day08.md` 的内容，其中包含 Spark 配置和 MongoDB 数据读取逻辑。
- 代码片段：`SparkConf sparkConf = new SparkConf().setAppName("SparkMongoDB").setMaster("local[2]").set("spark.mongodb.input.uri", "mongodb://localhost:27017/my-tanhu-spark");`

画面 14：
- 展示了测试结果，Redis 中已成功写入推荐数据。
- 文本内容：`192.168.31.6380: get QUAZI_PUBLISH_RECOMMEND_2 ...`
- 文本内容：`可以看到已经有推荐数据写入到了Redis中。`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
JavaPairRDD<Long, Rating> ratings = values.mapToPair(document -> {
    Long date = document.getLong(key: "date");
    int userId = document.getLong(key: "userId").intValue();
    int publishId = document.getLong(key: "publishId").intValue();
    Double score = document.getDouble(key: "score");
    Rating rating = new Rating(userId, publishId, score);
    return new Tuple2<>(date % 10, rating);
});
```

画面 2：
```java
// 打印的武氏
cache()
.collect()
.classTag()
.coalesce(int numPartitions, boolean shuffle)
.cartesian(JavaRDDLike<U, V> other)
.checkpoint()
.collectAsync()
.collectedPartitions(int[] partitionIds)
.context()
.count()
```

画面 3：
```java
d mLibRecommend = new MLlibRecommend();
MatrixFactorizationModel bestModel = mLibRecommend.bestModel(ratings);
rid : userIdList {
    recommendProducts = bestModel.recommendProducts(userId.intValue(), 10);
}
```

画面 4：
```java
for (Long userId : userIdList) {
    Rating[] recommendProducts = bestModel.recommendProducts(userId.intValue(), 10);
    for (Rating product : recommendProducts) {
        System.out.println(product.user() + ":" + product.product());
    }
}
```

画面 5：
```java
for (Long userId : userIdList) {
    Rating[] recommendProducts = bestModel.recommendProducts(userId.intValue(), 10);
    for (Rating product : recommendProducts) {
        System.out.println(product.user() + ":" + product.product());
    }
}
```

画面 6：
```java
//连接redis，做存储
Set<HostAndPort> nodes = new HashSet<>();
```

画面 7：
```java
String redisNodesStr = properties.getProperty("redis.cluster.nodes");
JedisCluster jedisCluster = new JedisCluster();
```

画面 8：
```java
String redisNodesStr = properties.getProperty("redis.cluster.nodes");
Set<HostAndPort> nodes = new HashSet<>();
for (String nodesStr : redisNodesStrs) {
    String[] ss = StringUtils.split(nodesStr, separatorChar:':');
    nodes.add(new HostAndPort(ss[0], Integer.valueOf(ss[1])));
}
```

画面 9：
```java
Set<HostAndPort> nodes = new HashSet<>();
for (String nodesStr : redisNodesStrs) {
    String[] ss = StringUtils.split(nodesStr, separatorChar:':');
    nodes.add(new HostAndPort(ss[0], Integer.valueOf(ss[1])));
}
```

画面 10：
```java
JedisCluster jedisCluster = new JedisCluster(nodes);
```

画面 11：
```java
jedisCluster.set(key, value);
```

画面 12：
```bash
root@litcast:~# docker exec -it redis-node01 /bin/bash
root@litcast:/data# redis-cli -c
```

画面 13：
```java
public static void main(String[] args) throws Exception{
    //读取配置文件
    InputStream inputStream = SparkMongoDB.class.getClassLoader().getResourceAsStream("app.properties");
    Properties properties = new Properties();
    properties.load(inputStream);

    //传递Spark配置
    SparkConf sparkConf = new SparkConf()
        .setAppName("SparkMongoDB")
        .setMaster("local[2]")
        .set("spark.mongodb.input.uri", "mongodb://localhost:27017/my-tanhu-spark");
```

画面 14：
```markdown
192.168.31.6380: get QUAZI_PUBLISH_RECOMMEND_2 ... 
192.168.31.6380: get QUAZI_PUBLISH_RECOMMEND_2 ... 
可以看到已经有推荐数据写入到了Redis中。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
