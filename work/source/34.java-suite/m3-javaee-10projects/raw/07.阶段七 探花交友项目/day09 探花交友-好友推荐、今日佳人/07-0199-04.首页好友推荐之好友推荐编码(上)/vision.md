# 画面线理解：04.首页好友推荐之好友推荐编码（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\04.首页好友推荐之好友推荐编码（上）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 02:32, 04:43, 06:38, 08:49, 09:40, 10:31, 12:25, 14:55, 17:34, 20:22, 22:12, 24:06, 25:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:10:41

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spark 中读取 MongoDB 和 MySQL 数据，并基于用户属性计算用户相似度，用于推荐系统。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程大纲，当前章节为“1.2.1. 编写Spark程序”，并显示配置文件中 Spark 连接 MongoDB 和 MySQL 的配置项。
画面 2：展示 Spark 程序入口，加载外部配置文件 app.properties，构建 SparkConf 并创建 JavaSparkContext。
画面 3：展示项目目录结构，重点在 src/main/java/com/tanhua/spark/mongo/SparkUserRecommend.java 文件。
画面 4：展示 SparkUserRecommend.java 中加载 MySQL 数据的代码，使用 SparkSession 读取数据库。
画面 5：展示设置数据库连接属性的代码，包括驱动、用户名、密码等。
画面 6：展示 EditPlus 编辑器中用户数据文件（u_data）的内容，包含用户 ID、年龄、性别、城市、学历等字段。
画面 7：展示 EditPlus 中用户数据文件的详细内容，包含用户 ID、年龄、性别、城市、学历等字段。
画面 8：展示 SparkUserRecommend.java 中计算用户相似度的代码，使用 cartesian 方法生成笛卡尔积。
画面 9：展示计算用户相似度的代码，过滤掉用户自己与自己的对比。
画面 10：展示计算用户相似度的代码，提取用户 ID。
画面 11：展示计算用户相似度的代码，计算年龄差。
画面 12：展示计算用户相似度的代码，计算用户年龄差。
画面 13：展示计算用户相似度的代码，计算用户城市是否相同。
画面 14：展示计算用户相似度的代码，计算用户学历是否相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
spark.mongodb.input.uri = mongodb://192.168.31.81:27017/tanhua_recommend_uanti_20191009
roadReferencePrimaryPreferred
spark.mongodb.output.uri = mongodb://192.168.31.81:27017/tanhua_recommend_uanti_20191009
roadReferencePrimaryPreferred
jdbc.url = jdbc:mysql://192.168.31.81:3306/tanhua_recommend_user?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
jdbc.username = root
jdbc.password = 0194907
jdbc.driverClassName = com.mysql.cj.jdbc.Driver

画面 2：
public static void main(String[] args) throws Exception {
    InputStream inputStream = SparkQuaZi.class.getClassLoader().getResourceAsStream(name: "app.properties");
    Properties properties = new Properties();
    properties.load(inputStream);
    // 构建Spark配置
    SparkConf sparkConf = new SparkConf()
        .setAppName("SparkQuaZi")
        .setMaster("Local[*]")
        .set("spark.mongodb.input.uri", properties.getProperty("spark.mongodb.input.uri"));
    // 构建Spark上下文
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 加载MongoDB中的数据
    JavaMongoRDD<Document> rdd = MongoSpark.load(jsc);
    // 打印测试数据
    rdd.foreach(document -> System.out.println(document.toJson()));
    // 在数据中会存在，同一个用户对不同的动作（相同动作）进行操作，需要合并操作
}

画面 3：
SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();
String url = properties.getProperty("jdbc.url");
// 设置数据库连接信息
Properties connectionProperties = new Properties();
connectionProperties.put("driver", properties.getProperty("jdbc.driver-class-name"));
connectionProperties.put("user", properties.getProperty("jdbc.username"));
connectionProperties.put("password", properties.getProperty("jdbc.password"));
JavaRDD<Row> userInfoRdd = sparkSession.read().format("jdbc").option("url", url).option("dbtable", "tb_user_info", connectionProperties).load();

画面 4：
SparkSession sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();
String url = properties.getProperty("jdbc.url");
// 设置数据库连接信息
Properties connectionProperties = new Properties();
connectionProperties.put("driver", properties.getProperty("jdbc.driver-class-name"));
connectionProperties.put("user", properties.getProperty("jdbc.username"));
connectionProperties.put("password", properties.getProperty("jdbc.password"));
JavaRDD<Row> userInfoRdd = sparkSession.read().format("jdbc").option("url", url).option("dbtable", "tb_user_info", connectionProperties).load();

画面 5：
// 设置数据库连接信息
Properties connectionProperties = new Properties();
connectionProperties.put("driver", properties.getProperty("jdbc.driver-class-name"));
connectionProperties.put("user", properties.getProperty("jdbc.username"));
connectionProperties.put("password", properties.getProperty("jdbc.password"));
JavaRDD<Row> userInfoRdd = sparkSession.read().format("jdbc").option("url", url).option("dbtable", "tb_user_info", connectionProperties).load();

画面 6：
无代码内容。

画面 7：
无代码内容。

画面 8：
cartesian.mapToPair(row -> {
    Row row1 = row._1();
    Row row2 = row._2();
    Long userId1 = row1.getLong(1);
    Long userId2 = row2.getLong(1);
    // 自己与自己对比
    if (userId1.longValue() == userId2.longValue()) {
        return new Tuple2<>(null,_);
    }
    return new Tuple2<>(null,_);
});

画面 9：
cartesian.mapToPair(row -> {
    Row row1 = row._1();
    Row row2 = row._2();
    Long userId1 = row1.getLong(1);
    Long userId2 = row2.getLong(1);
    // 自己与自己对比
    if (userId1.longValue() == userId2.longValue()) {
        return new Tuple2<>(null,_);
    }
    return new Tuple2<>(null,_);
});

画面 10：
cartesian.mapToPair(row -> {
    Row row1 = row._1();
    Row row2 = row._2();
    Long userId1 = row1.getLong(1);
    Long userId2 = row2.getLong(1);
    // 自己与自己对比
    if (userId1.longValue() == userId2.longValue()) {
        return new Tuple2<>(null,_);
    }
    return new Tuple2<>(null,_);
});

画面 11：
cartesian.mapToPair(row -> {
    Row row1 = row._1();
    Row row2 = row._2();
    Long userId1 = row1.getLong(1);
    Long userId2 = row2.getLong(1);
    // 自己与自己对比
    if (userId1.longValue() == userId2.longValue()) {
        return new Tuple2<>(null,_);
    }
    return new Tuple2<>(null,_);
});

画面 12：
cartesian.mapToPair(row -> {
    Row row1 = row._1();
    Row row2 = row._2();
    Long userId1 = row1.getLong(1);
    Long userId2 = row2.getLong(1);
    // 自己与自己对比
    if (userId1.longValue() == userId2.longValue()) {
        return new Tuple2<>(null,_);
    }
    return new Tuple2<>(null,_);
});

画面 13：
cartesian.mapToPair(row -> {
    Row row1 = row._1();
    Row row2 = row._2();
    Long userId1 = row1.getLong(1);
    Long userId2 = row2.getLong(1);
    // 自己与自己对比
    if (userId1.longValue() == userId2.longValue()) {
        return new Tuple2<>(null,_);
    }
    return new Tuple2<>(null,_);
});

画面 14：
cartesian.mapToPair(row -> {
    Row row1 = row._1();
    Row row2 = row._2();
    Long userId1 = row1.getLong(1);
    Long userId2 = row2.getLong(1);
    // 自己与自己对比
    if (userId1.longValue() == userId2.longValue()) {
        return new Tuple2<>(null,_);
    }
    return new Tuple2<>(null,_);
});

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
