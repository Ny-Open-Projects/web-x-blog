# 15.推荐系统之编写推荐逻辑（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\15.推荐系统之编写推荐逻辑（下）_【海量资源尽在 666java.com】.mp4
- 时长 11分53秒（音频 714s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来先获取到我们的用户的列表啊那么这个怎么获取呢其实前面的我们在我们的这个values啊这个里面呢其实在我们啊就在这个位置啊那其实我们已经可以去拿到我们的这个用户啊这样的一个列表了那么怎么样拿呢或者我们通过这个rdd拿也可以啊那我们就这么来做一个操作吧通过这个rdd
[00:28] 点做一个map操作然后呢我们去拿到的是一个我们这个是一个document对吧然后呢我们拿到v1里面的谁呢点get什么呢get longget long我们拿到就是这个user id然后呢我们对他呢去做一个什么呢做一个distinct去筹然后呢我们再去调用一个什么呢
[00:58] connect好这样的话其实我们就拿到我们用户ID的这样的一个列表了那么就叫userID叫list好这个就是我们的一个什么用户列表那么接下来我们就对我们的用户列表去做一个去做一个便利去做一个便利叫userID好
[01:28] 那么我们这个UserID拿到之后就可以去做一个推荐了对吧那我们就要用这个Best这个Module点做一个Recommend做一个推荐那么第一个参数呢就是这个UserID对吧第二个参数呢就是推荐的一个数量比如说推荐10个这样的一个动态的信息然后呢这个是参数类型的问题那我们就去转一下把它转成一个Int点什么呢Int Value
[01:58] 好那么我们就会拿到我们的一个这个叫什么呢我们来重新写一个名字啊给他那么就叫啊叫他吧啊就叫Command啊Product然后呢我们对他呢其实就可以再去做一个便利了对吧那么把它呢就打印出来啊就OK了Product好那么这样的话呢就OK了那么我们可以拿到他的比如说我们可以拿到他的什么呢点
[02:27] 点这个user然后呢加一个比如说去推荐谁呢去加一个product点点什么呢点product好那么这样的话就可以做一个推荐了对吧好那我们来执行一下看一下它最终执行的一个效果好那么执行呢结束了那我们来看一下这个结果啊那么可以看到呢是不是我们对这个比如说我这个用户呢推荐这么几个这个动态的信息
[02:56] 对不对二呢去推荐这么多啊那么其实这个呢就是我们已经就完成了我们数据的一个这个推荐对吧但是我们不能够只是这样去做一个推荐那我们最终是需要把这个数据啊我们去保存到我们的redis的所以下面这个位置啊就需要去我们去连接随着连接我们的redis啊连接我们的redis然后呢做什么呢做这个存储
[03:21] 好那么下面我们来看一下这个release应该怎么样去做一个连接呢那么首先呢我们需要定义的是一个我们叫做jadis啊jadis cluster然后呢jadis cluster因为我们用的是集群嘛去new一个这个jadis cluster那么new这个jadis cluster之后呢我们需要传递一个我们的一个nodes也就是我们需要传递一个这个set
[03:48] set中所存储的是一个叫做host and port那么就叫什么呢叫nodes等于new一个什么呢hashset好那我们来看这个里面我们存什么内容那我们就需要去读取到我们的这个配置文件对吧那么配置文件我们又该如何去做一个读取呢在前面是不是我们已经读到了那我们就拿到我们的
[04:17] properties.getget property那么拿到谁呢我们来看一下那么在这个里面呢我们就拿到拿到他拿到他然后呢拿到这个配置之后啊那我们就来看一下啊那么拿到他其实是一个其实是一个这不错对吧拿到是一个这不错那我们就是叫叫什么呢我们就叫比如说我们叫readiesreadies nodes
[04:48] 然后呢str这只是一个支付串对吧好然后呢我们需要对它去做一个处理那么这个处理呢显然呢可以看到呢是我们需要按照一个逗号去做一个分割然后呢按照分号分割才可以拿到它的一个IP地址和一个我们的一个这个端口那么这个应该怎么去做一个操作呢那我们是不是就需要呢去对它去做一个分割那我们通过这个有tools.split
[05:17] 对这个redis str做一个什么呢做一个逗号的一个分割那么他呢就会拿到的是一个叫什么呢redis那我们就加一个s吧加一个s然后呢我们接下来呢我们就需要对我们的这个呢去做一个迭代啊做一个迭代那么我们拿到每一个nodes str的时候呢我们对他呢再次去做一个
[05:46] 这个分割再次去做分割那就通过什么呢utils.split然后这个nodes.str通过一个分号我们可以写这个分号通过一个分号去做一个分割那么他就拿到我们的一个ss好那么其中的ss0那就是我们的host然后我们的ss1其实就是port所以说我们把这个
[06:15] 把这个我们应该丢到应该把它写到上面来写到这然后我们去node死node死and去我们看一下这应该叫我们刚才拼错了对吧node死node死然后我们去做一个and操作然后另有一个host and pod这样的一个对象
[06:44] 那么第一个这个参数呢那就是这个SS0然后呢第二个这个参数就是SS1那么这样的话呢我们是不是就得到它了那么当然了这个呢会有一个问题就是它的一个类型的问题啊那么它需要得到一个int类型呢我们就转一下好这样的话呢我们就得到了这个notes这个对象然后呢我们就把这个notes这个对象传递给它那么这样的话其实就完成了一个redis的一个连接啊
[07:14] 这块大家应该能够看懂就是我们去把配置文件的做一个两次分割第一次根据逗号第二次根据这个封号去做一个根据这个冒号去做一个分割拿到他的host和pod就构造完成了一个redis的一个cluster那么接下来我们就可以去做
[07:35] 这个推荐了对吧那我们来看一下怎么样去做推荐那么上面这个其实我们已经完成了推荐啊只是说我们需要最后呢把这个推荐的数据的写入到我们的这个redis中那么我们在这个位置吧在这个位置呢我们去写一个集合它所存储的呢其实就是我们的这个什么呢我们的这个叫产品ID对吧那我们就写这个product
[08:05] 然后呢去new一个我们的一个arriv list我们这个是不是拼错了少了一个ook好然后呢我们来看一下每一次便利呢我们就拿到它的一个这个产品点按的添加一个product点什么呢productproduct
[08:31] 好那么这样的话就拿到了拿到我们这个产品了那么接下来呢我们就需要呢去写入到我们的redis中那么通过这个jedis的一个cluster点做一个set这个操作那么set呢key啊那我们定义一个这个key等于什么呢啊key等于那我们就可以写一下比如说我们叫圈子啊圈子啊然后呢叫publishpublish
[08:59] 然后呢我们再写一个recmondrecmond然后呢下滑线再加一个叫做user id就是我们为这个用户啊去推荐一个这个值那key呢就是它了那么value呢那我们就去把我们的这个呢去用一个逗号去做一个分割啊就可以转成一个字符刷那就通过一个street有tels.join操作然后呢把它传把它传递过去跟一个什么呢
[09:30] 逗号去做一个分割那么这样的话呢就已经完成了一个存储了对吧OK好那么接下来呢我们就来执行一下看最后是否能够把这个数据写到我们的Ready中呢我们来再次去做一个执行好那么现在呢我们这个程序呢就执行结束了啊那么接下来呢我们来登录进到Ready中我们来测试一下那么我们来看一下我们这个key啊我们来拷贝一下啊
[09:58] 那么找到这个key那么就是它了那么比如说我们给这个应该是找到get给这个1这个用户呢去做一个推荐那么可以看到有这么多一些数据啊那么我们可以去
[10:12] 查看二的这个数据推荐那么当然了我们刚刚推荐的是十条那么可以改多一点比如说改成二十条这样也是可以的效果其实是一样的那么我们可以再来测一下比如说给六这个用户去做推荐推荐了有这么多那么可以看到每个人推荐的它是不一样的就根据它的一个内部的一个推荐算法去做一个这样的一个推荐了其实我们就是在套用它的一个这样的一个模型然后去做这样的一个推荐了OK
[10:42] 好那么到这里呢我们这个基本的这个推荐的一个逻辑呢就已经编写完成了啊当然我们最后呢别忘记啊把这个我们这个也关闭掉对吧然后呢我们这个readist的cluster也关掉啊我们用完之后呢记得啊要把它啊关闭一下好那么这样的话呢就OK了好那么下面我们来看一下我们的讲义啊讲义应该跟我们写的差不多啊然后呢读取配置文件然后呢去构建Spark的一个配置
[11:10] 上下文然后读起mongodb的数据然后去数据这合并然后拿到我们的用户的ID的数据
[11:18] 然后呢对我们的日期对模实进行取模的一个操作啊然后呢我们去拿到我们的M6中的一个推荐模型然后呢做推荐之后呢把Redis呢初始化完成之后啊然后呢去做一个存储啊基本上呢是非常啊类似的这样的一个过程了那么最终的一个结果呢其实我们可以看到啊就是我们在Redis中是不是已经就写入了相关的一些这个数据了对吧
[11:46] OK好那么关于我们这个推荐系统的一个业务逻辑的一个编写的那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
- 命令：`Docker exec -it redis-node01 /bin/bash`
- 命令：`redis-cli -c`

画面 13：
- 展示了 Markdown 文档 `day08.md` 的内容，其中包含 Spark 配置和 MongoDB 数据读取逻辑。
- 代码片段：`SparkConf sparkConf = new SparkConf().setAppName("SparkMongoDB").setMaster("local[2]").set("Spark.mongodb.input.uri", "mongodb://localhost:27017/my-tanhu-Spark");`

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
root@litcast:~# Docker exec -it redis-node01 /bin/bash
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
        .set("Spark.mongodb.input.uri", "mongodb://localhost:27017/my-tanhu-Spark");
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

