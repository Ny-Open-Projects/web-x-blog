# 画面线理解：23.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\23.课程总结_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:12, 01:24, 01:53, 02:30, 02:50, 03:03, 03:19, 03:35, 04:03, 04:10, 04:17, 04:30, 04:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:08:02

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何实现圈子推荐功能，包括动态增加自增id、搭建推荐系统、使用Spark MLlib实现推荐、将结果存入Redis，并实现小视频的推荐逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：课程说明，列出“圈子推荐功能说明”、“圈子推荐功能流程”、“圈子推荐功能的实现”、“搭建推荐系统”、“使用Spark实现推荐逻辑”、“小视频推荐功能的实现”等章节。
画面2：展示“Publish”对象的Java类定义，包含id、pid、userId、text、medias、seeType、longitude、latitude、locationName等字段。
画面3：展示“创建icast-tanhua-recommend工程”的pom.xml文件，包含父模块和spring-boot-starter-web依赖。
画面4：展示“搭建系统”章节下的pom.xml，包含spark-mllib依赖和exclusions排除。
画面5：展示MLlibRecommend类中MatrixFactorizationModel的bestModel方法，用于计算用户和商品的评分矩阵。
画面6：展示SparkMongoDB类的main方法，用于实现MongoDB的推荐功能。
画面7：展示SparkMongoDB类的代码，包含导入的包和main方法。
画面8：展示测试结果，Redis中已存入推荐数据，并说明需要从Redis读取数据。
画面9：展示测试页面，包含“Raw”、“JSON”、“Response”选项卡，以及测试数据。
画面10：展示“增加自增id”章节，包含Video类的定义。
画面11：展示VideoMsgConsumer类的代码，用于处理视频消息。
画面12：展示TestVideoApi类的testSaveVideo方法，用于测试视频保存。
画面13：展示SparkVideoMongoDB类的代码，用于加载配置、创建Spark上下文、读取MongoDB数据并计算评分。
画面14：展示Video类的代码，包含设置用户ID、视频ID、评分、创建时间、评论数、关注数、点赞数等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@Data
@AllArgsConstructor
public class Publish implements java.io.Serializable {
    private static final long serialVersionUID = 8732108321082804771L;
    private ObjectId id; //主键
    private Long pid; //long类型id，用于推荐能使用
    private Long userId;
    private String text; //文字
    private List<String> medias; //媒体url
    private Integer seeType; //谁可以看，1-公开，2-私密，3-部分可见，4-不给谁看
    private List<Long> seeList; //不给谁看的列表
    private String longitude; //经度
    private String latitude; //纬度
    private String locationName; //位置名称
}
```

画面3：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>icast-tanhua</artifactId>
        <groupId>cn.ictast.tanhua</groupId>
        <version>1.0-SNAPSHOT</version>
        <modelVersion>4.0.0</modelVersion>
    </parent>
    <artifactId>icast-tanhua-recommend</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

画面4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>icast-tanhua</artifactId>
        <groupId>cn.ictast.tanhua</groupId>
        <version>1.0-SNAPSHOT</version>
        <modelVersion>4.0.0</modelVersion>
    </parent>
    <artifactId>icast-tanhua-spark</artifactId>
    <packaging>jar</packaging>
    <dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-mllib_2.12</artifactId>
            <version>2.4.3</version>
            <scope>runtime</scope>
        </dependency>
        <exclusions>
```

画面5：
```java
public class MLlibRecommend {
    public MatrixFactorizationModel bestModel(JavaPairRDD<Long, Ratings> ratings) {
        Long numRatings = ratings.count();
        Long numUsers = ratings.map(v -> v._1).distinct().count();
        Long numMovies = ratings.map(v -> v._2).distinct().count();
        System.out.println("用户：" + numUsers + " 电影：" + numMovies + " 评分：" + numRatings);
        Integer numPartitions = 4; // 分区数
        // 训练集
        JavaRDD<Ratings> training = ratings
                .filter(v -> v._1 < 0)
                .repartition(numPartitions)
                .cache();
        // 测试集
        JavaRDD<Ratings> validation = ratings
                .filter(v -> v._1 >= 0)
                .cache();
```

画面6：
```java
package com.tanhua.spark.mongo;
import com.mongodb.spark.MongoSpark;
import org.apache.commons.lang3.StringUtils;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.types.StructType;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.DataTypes;
import scala.Tuple2;
import java.io.InputStream;
public class SparkMongoDB {
    public static void main(String[] args) throws Exception{
        //读取外部的配置文件
        InputStream inputStream =
```

画面7：
```java
package com.tanhua.spark.mongo;
import com.mongodb.spark.MongoSpark;
import org.apache.commons.lang3.StringUtils;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.types.StructType;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.DataTypes;
import scala.Tuple2;
import java.io.InputStream;
```

画面8：
```java
//关闭连接
jedisCluster.close();
```

画面9：
```java
//测试
@GetMapping("/movements")
public PageResult movements(@RequestParam("page") Integer page,
                            @RequestParam("size") Integer size) {
    PageResult pageResult = new PageResult();
    //查询数据库
    List<Movements> movementsList = movementsService.movements(page, size);
    pageResult.setTrans(movementsList);
    return pageResult;
}
```

画面10：
```java
package com.tanhua.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
@Data
@AllArgsConstructor
public class Video implements java.io.Serializable {
    private static final long serialVersionUID = -3116312836848493387L;
    private ObjectId id; //主键
    private Long vid; //视频id
    private Long userId; //用户id
    private Double score; //评分
    private Long created; //创建时间
}
```

画面11：
```java
package com.tanhua.recommend.msg;
import com.fasterxml.jackson.databind.JsonNode;
import com.tanhua.recommend.pojo.Publish;
import com.tanhua.recommend.pojo.RecommendVideo;
import org.apache.commons.lang3.StringUtils;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
```

画面12：
```java
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestVideoApi {
    @Autowired
    private VideoApi videoApi;
    @Autowired
    private MongoTemplate mongoTemplate;
    @Test
    public void testSaveVideo() {
        for (int i = 0; i < 100; i++) {
            Video video = new Video();
            video.setId(ObjectId.get());
            video.setUserId(RandomUtils.nextLong(1,10));
            video.setVid(Long.valueOf(1000 + i));
            video.setLocationName("上海");
            video.setPicUrl("http://itcast-tanhua.oss-cn
