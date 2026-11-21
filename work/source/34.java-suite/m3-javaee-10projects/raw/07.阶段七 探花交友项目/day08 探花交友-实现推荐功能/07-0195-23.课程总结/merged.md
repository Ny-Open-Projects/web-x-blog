# 23.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\23.课程总结_【海量资源尽在 666java.com】.mp4
- 时长 4分59秒（音频 300s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢我们做一个总结那么今天呢我们主要呢是在做推荐功能那么完成了两个推荐功能第一个呢就是圈子中的推荐那第二个呢就是小视频的推荐那么我们来看一下圈子的推荐啊那么它的功能呢其实就是在我们用户在针对于我们的一些所发布的一些动态信息呢可以有一些这个交互的一些操作比如说
[00:30] 点赞呢浏览呢啊等等这样的一操作然后呢我们根据这些信息呢呃然后呢去为一些用户呢去推荐不同的一些这个高质量的一些啊这个动态信息啊那么大概就是这样的一个功能呃然后呢他这个流程呢就是我们这样的一个流程就用户操作然后呢发消息到我们ROCK的MQ然后呢我们推荐系统呢去接收这个消息然后呢写入mongodp
[00:55] 由我们的Spark去拉取数据做计算基本结果呢写到Release然后用户进行做一个查询那么基本的一个流程就是这样的一个流程啊然后呢我们下面呢又去做的具体的一些实现包括我们去增加了一些自增长的ID然后呢我们定义了它的一些动态的这个计分的规则然后呢我们又去实现它的消息的发送啊以及这个消息的接收然后呢我们
[01:22] 又去做了什么呢做了一些我们推荐系统那么基于前面我们所得到的一些这种数据呢就可以去做一个推荐了当然了这个数据呢我们肯定是需要自己去构造一下因为我们就是拿几条数据测试这个是没有意义的我们需要去测试一堆数据啊那么我们是不是构造了有一千条这个数据那么这一千条数据呢是针对于那么一百条的动态信息所生成的一千条这个
[01:50] 然后呢进行做推荐的啊然后呢下面呢我们就搭建了我们的这个推荐系统那么就是我们这个SPARK系统啊做一个具体的一个推荐算法的一个编写在这个里面来做一个完成啊那么同样的我们也是使用了SPARK的MLib来做一个具体的一个推荐的一个
[02:11] 这个实现啊那么使用它的是一个它固有的一个这样的一个模型然后呢我们套用这个模型呢就可以了完成这样的一个推荐了然后呢我们把之前的这个mlib的相关的一些这个代码呢我们基本呢没有做什么改动啊就是我们去分装了这样的一个方法然后就会得到我们最优的一个推荐的模型基于这个模型呢那我们就可以去做一些这个推荐了啊
[02:39] 然后呢我们基于他呢我们就去编写了我们的对于圈子中数据的一些这个推荐啊那么希望大家能够自己呢把这一块代码的完成那么前面这个代码其实可以大家呢
[02:52] 不需要去能够掌握它的一个完成编写那么只要我们能够保证能够看懂那么因为之前前面我们已经写过这样的代码了对吧那我们能够去完成下面这个代码的一个编写那么就可以基于这个MLib来做一个功能的一个实现这样的话就OK了好那么这样的话呢我们就完成了数据的一个推荐并且把结果呢
[03:16] 存储到Redis中然后呢我们就需要去查询修改我们的查询的逻辑然后呢就可以通过这个Redis去做一个数据的一个命中那么这样的话呢我们是不是就和前面的这个就整个关联起来了然后呢这个就具体的就不说了最后的结果呢肯定就是跟我们之前的一样可以查到我们的数据如果没有命中还是走之前的逻辑如果命中的话那就按照这个推荐的一个结果进行展现
[03:46] 然后呢最后呢我们实现了我们的这个小视频的推荐它和我们圈子的这个推荐呢是一致的啊逻辑也是一样的所以说呢我们呢也就是能够快速的去把它就这个做出来了然后呢同样呢也是包含了有这个增加自征来地然后呢它的评分的规则啊然后呢还有什么呢就是我们的发送消息啊然后呢去接收消息然后呢对于消息的这种处理
[04:14] 然后呢我们同样的也是去做了这个构造啊做了数据的构造也是一千个这个视频的数据然后呢我们再去有这个啊一百个视频的数据然后呢有一千个这个推荐的这样的一个数据啊哎OK
[04:30] 好那么最后呢我们也是去修改了一下我们的查询的逻辑啊那么就可以去实现我们的一个数据的一个查询了那么最后呢其实我们就需要整合到我们的这个APP中呢去做一个实现那么刚刚呢我们已经整合完成了那么发现这个结果呢跟之前是一样的但是它的数据的来源其实就已经发生了变化啊OK好那么关于我们今天的这个课程的这个总结呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何实现圈子推荐功能，包括动态增加自增id、搭建推荐系统、使用Spark MLlib实现推荐、将结果存入Redis，并实现小视频的推荐逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：课程说明，列出“圈子推荐功能说明”、“圈子推荐功能流程”、“圈子推荐功能的实现”、“搭建推荐系统”、“使用Spark实现推荐逻辑”、“小视频推荐功能的实现”等章节。
画面2：展示“Publish”对象的Java类定义，包含id、pid、userId、text、medias、seeType、longitude、latitude、locationName等字段。
画面3：展示“创建icast-tanhua-recommend工程”的pom.xml文件，包含父模块和spring-boot-starter-web依赖。
画面4：展示“搭建系统”章节下的pom.xml，包含Spark-mllib依赖和exclusions排除。
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
    <artifactId>icast-tanhua-Spark</artifactId>
    <packaging>jar</packaging>
    <dependencies>
        <dependency>
            <groupId>org.apache.Spark</groupId>
            <artifactId>Spark-mllib_2.12</artifactId>
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
package com.tanhua.Spark.mongo;
import com.mongodb.Spark.MongoSpark;
import org.apache.commons.lang3.StringUtils;
import org.apache.Spark.api.java.JavaSparkContext;
import org.apache.Spark.api.java.JavaRDD;
import org.apache.Spark.sql.SparkSession;
import org.apache.Spark.sql.Dataset;
import org.apache.Spark.sql.Row;
import org.apache.Spark.sql.types.StructType;
import org.apache.Spark.sql.types.StructField;
import org.apache.Spark.sql.types.DataTypes;
import scala.Tuple2;
import java.io.InputStream;
public class SparkMongoDB {
    public static void main(String[] args) throws Exception{
        //读取外部的配置文件
        InputStream inputStream =
```

画面7：
```java
package com.tanhua.Spark.mongo;
import com.mongodb.Spark.MongoSpark;
import org.apache.commons.lang3.StringUtils;
import org.apache.Spark.api.java.JavaSparkContext;
import org.apache.Spark.api.java.JavaRDD;
import org.apache.Spark.sql.SparkSession;
import org.apache.Spark.sql.Dataset;
import org.apache.Spark.sql.Row;
import org.apache.Spark.sql.types.StructType;
import org.apache.Spark.sql.types.StructField;
import org.apache.Spark.sql.types.DataTypes;
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
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
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

