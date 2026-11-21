# 14.推荐系统之编写推荐逻辑（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\14.推荐系统之编写推荐逻辑（上）_【海量资源尽在 666java.com】.mp4
- 时长 19分47秒（音频 1187s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来编写我们的业务逻辑啊那么首先呢我们在这个下面去创建一个类啊这个类的名字呢我们就叫SparkSpark就叫圈子啊我们在处理这个圈子相关的一些这个推荐啊那么就写一个Spark这个圈子然后呢接下来呢我们在这里面啊就写我们的这个man方法啊然后呢
[00:26] 首先其实我们是需要去加载我们的一些外部的配置文件啊那么我们外部的配置文件就是这个app.public文件那我们来考一下这个名字啊那就它了好那么我们来看一下怎么样去做一个加载呢那么我们呢是需要通过我们的这个类加载器是不是去做一个加载啊那么就通过这个Spark圈子然后点class点
[00:55] get classloader然后点get resource as stream然后我们去指定一个名字那么其实这个名字就是我们 app properties那么在我们的app properties中它其实去就是记录了我们两个配置第一个就是我们 MongoDB的一个配置那么第二个就是我们redis的这样的一个配置然后在这个里面我们是不是就
[01:23] 可以拿到我们的一个这个什么叫做input stream这个呢就是我们的一个输入流那么然后呢我们就需要定义一个什么呢properties对象去解析我们这个配置文件等于new一个properties然后呢我们通过一个properties点load去做一个这个加载input stream
[01:53] 那么这个呢它显然会有一个这个异常对吧那么这个异常呢我们就直接啊去做一个抛出吧抛出一个exception啊做这样的一个抛出那么走到这里呢我们这个配置文件呢是不是就已经啊加载完成了那么加载完成之后啊那么下面我们就需要来干嘛呢去干嘛构建我们Spark啊
[02:18] Spark的一个配置那么我们还是要通过Spark去运行对吧那么通过这个Spark的一个配置那么这个Spark的配置怎么样去作为构建呢我们定义一个叫做Spark然后呢configconfig一个对象然后呢定义一个Spark config它等于什么呢我们去new一个sparkconfig一个对象然后呢我们去给它去做一系列的一些这个set
[02:45] 比如说第一个呢是app name那么我们这个就用我们这个类的名称吧就它把它拷贝过来然后呢我们继续去set谁呢比如说我们设置还有这个master那么我们这个主呢那就是本地对吧local然后呢这个新
[03:05] OK好然后呢这个是两个啊还有其他的配置你比如说呢我们需要去set去设置一些这个参数那么就是我们现在Spark呢需要去连接到我们的MongoDB那我们就需要给他去设置一个参数啊这个参数名呢就是在我们配置文件中所配置的这个参数名那我们来拷贝一下那么就是他然后呢要注意了这个值呢我们就通过
[03:35] properties然后点getproperty然后我们去把这个拷贝过来那么去读取这个配置项那么这样的话我们其实就完成了我们一个Spark的一个配置然后有了我们这个Spark配置之后那么接下来我们就需要去干嘛去构建构建什么我们的sparkspark的一个上下
[04:02] 文啊上下文那么 Spark 的这个上下文怎么样去构建呢我们是通过这个 java sparksparkcontact然后定一个什么 jsc jsc 呃然后呢我们去做一个 new 一个 java 的一个 Spark contact我们把这个 sparkconfig 对象呢传递进去这样的话呢我们这个 Spark 的一个上下文对象呢就
[04:31] 构建好了那么这个是我们前面啊所写过的一些代码那么接下来呢我们来看一下我们就需要去加载我们的一个MongoDB的数据啊那么如何去加载MongoDB的数据呢在前面的我们是不是已经引入了这个就是叫做MongoSpark的Connector这样的一个依赖包那么我们就需要通过这个依赖包中所提供的一个对象啊叫做什么呢Mongo
[05:01] mongo Spark然后呢点load去做一个加载那我们把这个jsc呢传递给他啊传递给他然后呢他呢就会得到一个什么呢我们的一个叫做java的一个来看一下叫做java的一个mongo的一个rdd啊这样的一个数据那我们就把它叫做什么呢rdd然后呢这个叫什么呢这个就是叫做我们去加载我们的mongo
[05:30] db中的这个数据啊去做一个这个加载那么加载到之后是不是就可以来做一个处理了那么其实我们可以先干嘛呢我们可以打印一下对吧我们先这个打印啊测试一下我们的这个数据啊怎么样去打印呢通过这个rdd啊点什么呢点这个有个叫for each啊这个前面我们是不是写过啊那我们写一个lam的表达式
[05:56] 然后我们去通过一个setmode把它的打印出来document.tojson然后去做这样的一个打印最后我们就可以把我们的这个jsc做一个什么做一个close关闭好嘞好那么这个就是我们去做一个关闭了好那么接下来我们先来执行一下看一下它是否能够正常的去读取到配置文件并且去加载我们mongoDB中的数据
[06:25] 然后呢最后呢能够把它正确的打印出来好那我们来执行一下ok好那我们来等待它的一个执行那么ok现在呢就执行结束了我们来看一下数据啊那么这个是不是可以看到是不是已经加载到我们mongo db的啊这个数据了对吧ok这个呢是没有问题的呃然后呢我们可以大致的来浏览一下数据啊这个是不是可以看到有这个呢public id啊这个浪类型score一些得分
[06:53] 包括我们这个Data的数据啊一切是没有问题的那么接下来呢我们这个打印呢我们其实就不需要了可以把它注释掉啊那么如果需要的话也可以再次把它打开啊那么接下来呢我们就需要去对我们的这个数据呢做一些这个处理那么大家要明确的一点是我们其实拿到这个数据啊它其实有点类似于什么呢就是我们的日志数据就是说那么只要用户
[07:22] 对我们这个圈子中的一个动态做操作那么他就会去做一个记录那么就可能会有这样的一种情况就是同一个用户那么对于不同的一些动态数据那么都有进行做一些评价那我们是必须去按照这个用户和我们这个动态信息呢去做一个这个合并就是合并成一个啊什么意思啊就是说之前我们这个数据啊
[07:50] 那么之前这个数据模型是一个用户对一个电影的评分它其实只是有一条数据并不会说一个用户对于一个电影的评分可能会有多条数据这种情况是没有的所以说我们需要对它做一个合并处理那我们来写一下这个注释我们要做的事情就是在我们的这个数据中那么会存在会存在什么呢
[08:19] 同一个用户用户对什么呢对这个不同的对不同的这个动态或者说这个或者是这个相同的动态相同这个动态相同一个动态然后呢去进行这个操作然后呢我们是不是就都记录下来了对不对那我们就其实我们需要做的是做一个合并
[08:49] 这样的一个操作那么怎么样去做一个合并呢那我们就需要去我们需要去做对我们这个数据就是RDD这个数据做一个什么呢Map to pair这样的一个操作那么为什么是Map to pair操作那么我们就需要按照一个用户再加一个他的一个这个就是我们的一个这个动态的ID
[09:16] 作为一个key去做一个存储那么就是说我们呢会把它如果说是同一个用户对于相同的这个动态做操作的时候那么是不是就会有一些相同的key所存在啊所以说呢我们要把它转成一个KV这样的一个结构啊方便我们去做一个
[09:37] 处理那么我们来看一下那我们就会拿到一个document那么这个里面应该怎么去写呢我们依然呢是通过Lamb的表达式去做一个编写那么我们最终我们return所返回的是一个什么呢叫做trap对吧trap2这个对象那么它呢是有什么呢kv是不是来组成的key那我们肯定是需要去去写一个这样的key对吧然后的v呢其实就是还是我们这个document
[10:06] 对吧那么这个key我们怎么样去定义它呢那么我们是不是应该去拿到我们的用户和我们这个产品对吧那么我们怎么样去拿到它呢就通过这个document对吧document.get什么呢get一个num谁呢是不是我们叫useriduserid然后呢我们去拿到它的一个这个intvalue那么拿到这个id当然我们拿到这个num也可以啊那我们就直接拿到这个
[10:36] 让去做一个这个处理吧哎哎OK那么我们就拿到这个浪浪和印度都可以去做一个处理啊那么这个叫优的ID啊等于他好那么这是第一个啊这个操作那第二个操作呢我们就需要拿到谁啊是不是拿到我们的一个public ID啊public ID那么public ID呢他也是这个浪类型的对吧那我们就可以把谁呢哎
[11:04] 把这个空行去一下啊那么我们就通过这个U的ID去加一个下滑线再加一个public ID那么这样的话呢我们就会把同一个用户对于相同这个动态是不是就会有同样的一个key去做这样的一个存储啊对吧然后呢我们这样的处理完成之后啊并不能够去把这个做合并我们只是去找出
[11:30] 这样的一些这个数据还没有做合并那么怎么样做合并呢大家应该还记得我们是不是学过这样的一个方法叫做什么呢叫做ReduceByKey是不是按照相同的key去做一个Reduce这样的一个操作啊对吧我们来看一下啊叫做V1V2这个操作那么这个操作怎么玩呢那么我们最终其实返回的对吧最终返回的还是我们的一个这个数据啊最终返回的还是一个数据那我们来看一下啊
[12:00] 那我们看一下这个是怎么样去做一个这个操作啊那么把这个来关一下那么我们其实就需要拿到这个v1它的一个这个我们的score对吧score这个值然后呢去加我们的v2啊v2.get一个double然后呢score啊score然后呢它拿到之后啊就会得到我们的一个新的一个
[12:30] 新的一个这个比如说叫new一个scorenew一个score等于它这是我们新的一个score这个值然后呢我们就把这个我们这个新的这个score这个值我们给它回写到任何一个我们的对象中那我们做一个什么put不是set而应该做一个put操作叫一个score然后呢我们把这个new一个score把它丢进去
[12:59] 好那么这样的话呢我们就相当于把这个累加之后就是相同k的这个数据的这个score我们做了一个相加那么相加之后呢会得到一个new score把它回写到一个ve里面来那么这样的话呢我们就需要需要什么呢做一个return谁呢return这个ve那么这样的话是不是就会得到我们这个相同的相同的这个k的数据只会保留一条对吧
[13:27] 只会保留一条并且呢我们去做了这样数据的一个这样的一个累加得到最终的一个总的一个分数啊那么我们拿到它之后啊那么其实我们这样的话呢我们其实可以直接通过谁呢通过它的一个点啊点有一个叫做value的一个操作那么就会拿到我们那个加尔滴滴的一个数据啊那么这个其实就是我们的一个叫做
[13:51] 比如就叫values吧那么这个就是一个JavaRDD啊这样的一个数据了好那么接下来呢我们是不是就可以去做一个这个调用了对吧ok当然了我们也可以什么呢也可以去先去跟我们刚才一样做一个我们的一个数据的一个打印吧这个呢是做一个测试啊那我们就通过一个values啊通过一个这个valuesvalues然后呢点for each
[14:20] for each做一个操作那么拿到它然后呢set mode然后呢document.to jsonok好那么我们来执行一下看它执行的一个结果啊会怎么样好那么执行结束了我们来看一下这个结果啊那么现在呢就会对我们的这个score呢其实做了一个什么呢做了一个这个累加啊这样的一个操作了那么其实也就是说我们现在相当于对我们这个数据做了一些这个清洗
[14:48] 那么接下来呢我们就可以去正式的去使用我们这个数据了那么把它呢我们就注释掉了那么接下来呢我们就需要什么呢我们就需要去做什么呢去推荐了对吧那么我们前面是不是写了一个叫做MLlibRecommend对象那我们去new一个这个对象出来new一个它然后呢我们通过一个MLlib这个Recommend对象然后呢去得到一个best module
[15:17] 然后呢我们把这个我们上面那个values啊传递进去啊那么啊这个还啊传递不了对不对那我们来看一下他所需要的是什么呢需要我们这样的一个类型啊那我们现在是不是还没有得到这样的一个rating这样的一个类型啊那我们还需要给他去转换一下啊好那么我们在这来做一个这个转那么我们还是呢通过这个values啊然后呢我们去做一个map to啊pair这样的一个
[15:47] 操作那这个跟我们之前的这个逻辑呢啊是一样的啊好那么我们来看一下这个里面的一个这个玩法那么最终呢其实我们嘴唾还是去new一个我们这个trip这个对象啊然后呢这个key那么我们要拿到我们这个时间呢去和这个时是不是取模啊对吧好那我们来看一下这个应该怎么去拿呢那么这个时间呢我们就应该定一个这个date等于
[16:15] document.getluck对吧然后呢我们拿到一个这个date那么这样就拿到我们这个时间了那么就是这个date与谁呢与我们的这个时取模去作为它的一个key而这个value呢那就是我们这个rating这个对象对吧那我们来看一下啊那我们定义一个rating这个对象啊它呢等于new一个这个rating
[16:43] 那么我们来看一下我们把这个rating呢就拿过来那么这个rating对象拿到之后啊那么其实它是需要有三个构造参数的对不对那么第一个呢是这个我们来点击去看一下啊那么第一个呢其实是这个什么叫做user还有product然后呢还有rating也就是我们这个叫评论对吧新级然后呢我们来看一下第一个这个参数那么是我们的这个user
[17:10] 那么user呢其实是int类型的那我们就需要来拿一下通过这个documentdocument然后呢点get什么呢getgetint那我们还得先拿到这个run因为我们这个document它是run类型那我们拿到这个叫做user叫做user id拿到它然后呢拿到它int值这样去转一下
[17:38] 那么这样的话呢我们拿到的才是谁呢才是我们这个U的ID啊第一个这个参数拿到它往那一丢那么第二个这个参数那么我们和它就类似了那么第二个这个参数呢还有什么呢还有叫Publish ID啊Publish ID然后呢拿到它那么第二个参数那就是我们这个相当于产品啊
[18:03] 然后呢第三个参数那就是需要拿到这个什么呢这个double对吧就是我们的一个这个得分那么来看怎么去拿呢那么我们依然通过这个document点get什么呢get一个double然后呢score然后呢就会拿到一个这个score对吧好嘞好那么这个score呢我们就啊我们就丢到啊这个位置来
[18:30] 好那么这样的话我们是不是构建完成我们一个rating这样的一个对象然后呢丢到这个里面来最后呢我们通过这个map to pair去得到我们这样的一个对象啊然后呢我们来看一下最终的一个它的一个返回值那么其实就会变成什么呢我们叫做就叫ratings吧那么我们来看一下啊这个就叫ratings吧叫ratings这样的一个对象
[19:02] 那么我们就会把它呢是不是就可以传递进来这样的话呢是不是就OK了对吧传递过来那么然后呢我们通过它呢就会去得到一个谁呢得到我们的一个这个best一个module那么通过它是不是就可以去做一下这个推荐了对不对那么这个推荐呢我们肯定是需要为一些用户
[19:23] 是不是去做一些推荐啊所以说我们还需要去得到一个这个用户的一个列表也OK好那我们先把这个视频呢我们先停一下那么下个视频呢我们来做的事情呢就是我们去呃拿到我们用户列表然后呢我们去推荐的结果去写到我们的Ribbon之中那我们做这个事情啊OK好那么关于这个推荐呢我们先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
        .set("Spark.mongodb.input.uri", properties.getProperty("Spark.mongodb.input.uri"));
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

