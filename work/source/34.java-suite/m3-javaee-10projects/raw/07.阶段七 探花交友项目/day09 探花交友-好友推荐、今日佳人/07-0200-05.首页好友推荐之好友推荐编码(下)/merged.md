# 05.首页好友推荐之好友推荐编码（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\05.首页好友推荐之好友推荐编码（下）_【海量资源尽在 666java.com】.mp4
- 时长 17分9秒（音频 1029s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来去通过我们的一个什么的MLlib对吧进行计算它的一个最佳的一个这个模型推荐模型然后呢进行做一个推荐那么我们所以需要去调用我们的一个MLlib的一个recommend我们去new一个这个对象然后呢我们去调用这个MLlib中的点
[00:29] 这个best module把这个我们的这个ratients那就上面我们所得到的一个java pal的一个rdd给它传递进去好那么这样的话呢我们就通过它的一个这个计算这个呢我们就不重复了前面我们也讲过然后呢去得到我们最佳的这样的一个推荐模型那么就是拿到一个这个best一个module然后呢我们通过它就可以去做一个这个推荐了那我们先来做一个recommend
[00:58] recommend products那么比如说我们给这个1这个用户然后去推荐20个用户我们来看一下得到的结果会怎么样那么我们首先去拿到它的一个 ratings然后我们去做一个便利做一个便利我们去打印一下这个叫rating它的什么就是user再加一个什么再去加一个rating点
[01:27] 什么呢叫productor然后呢再去加他的一个这个得分加一个rating点这个方法好嘞好这样的话呢我们就能够把它打印出来了那我们来执行一下好那我们等待他的一个执行好那么我们来看一下他的一个计算结果那么是把这个数据都打印出来了那么为这个1这个用户呢去
[01:52] 推荐了有20个用户啊那么前面这个是我们的用户ID然后呢这个是所推荐的啊那个用户ID然后它的一个得分那我们可以看一下啊那么这个得分最高的一个呢是57这个用户那我们可以去来看一下这个数据啊那我们可以简单的去验证一下比如说我们把这个呢就复制出来吧然后呢我们来看一下啊那我们就丢到这儿然后呢这个是我们的这个数据我们找到57啊这个数据那么拷贝一下这个数据然后到这儿
[02:22] 来看一下它的一个这个结果那么这两个数据我们去做一个对比然后我们来看一下它的这两个用户相似不相似首先我们来看一下它的一个这个年龄对吧那么年龄是在这个位置对吧一个是30一个是29它俩这个年龄差的比较小然后它的性别一个是1一个是2那就说明他们是异性对吧还有他们是都在同城北京
[02:52] 然后呢他的学历呢也都是本科那么所以这两个用户是比较相似的那么有同学可能记得说前面我们这个数据啊可能是那么哎那么我们是应该是我们现在所连接的我们来看一下啊现在我们所连接的这个数据库啊那么是我们的这个碳花这个数据库啊碳花这个数据库那么就是我们的这个数据库了那么在这个数据库里面其实我是做了一些这个调整这个数据的就是说那么我的这个
[03:21] 所在的城市有北京有南京的所以说它会有一些差异化出来那么大家需要把这个数据也调一下那么包括它的一些已婚状态等等那么当然我们这块没有去做一个计算那么如果你要是和婚姻状态有关系的话那么就需要去改一下它的数据然后它的一些性别需要去调一下它的一些学历需要去调一下
[03:47] 那么这样的话我们可以看到刚才计算出的这两个用户是不是比较相似那么根据我们的规则去计算那么他的一个得分是96分这样的一个得分那么所以说他是最相似的一个用户肯定会推荐给他然后还有这个11这个用户那我们也可以来看一下那么找到这个用户ID为11的这个用户那我们来复制一下那么我们到下面这块来那我们来看一下他的一个
[04:16] 这个相关的一些内容啊然后呢我们可以看到他的这两个的这个性别啊是异性啊所以得分比较高那么再加上什么呢他的这个年龄啊相差呢是个四岁啊比他比这个57肯定要差的大一些然后呢还有他的本科他的这个学历呢一样然后呢也是在同层
[04:37] OK那么这样的话呢其实就也是基本上可以认识出来这个推荐结果呢是比较准确的这样的一个结果OK好那么接下来呢我们继续往下面去写啊那么下面的我们是其实是需要把我们的啊
[04:53] 把我们的这个结果不仅是打印了那么我们更需要的是让他能够去存储到我们的mongoDB里面去那么接下来我们就需要通过我们的一个mongo的一个Spark去做一个save操作我们还记得前面有这样的一个叫做mongo Spark他有一个save这样的一个操作但是要注意的是我们要想去操作我们这个mongo的一个Spark我们得先得到一个
[05:22] 叫做什么呢就是java的一个Spark contact的对象叫jsc你得有这个对象才能够去使用这个mongo Spark所以我们需要去new一个java的一个Spark contact但是要注意了这块你不能直接去这样去new比如说我们不能够
[05:41] 来看一下那么之前我们是不是通过这种方式就是上面这种方式直接去new一个通过一个convex去new那么这样的话你是不可以这么去玩的为什么我来简单的说一下那么这样去玩的话会有问题就是说在我们同一个应用中你相当于是已经创建了两个上下文了这个是不可以的莫言是不能够这样去玩的那么我们需要通过谁通过前面我们所得到的一个叫做Spark一个sessionspark
[06:12] Spark的一个session它呢我们去拿到一个Spark contact去构造出一个我们的一个GSC那么这样的话呢就可以就是说它和前面的这个Spark session使用的是同一个这个上下文下面呢我们就要去将这个数据将这个将这个数据写入到我们的一个MongoMongoDB中
[06:42] 那么我们需要得到一个这个gsc那么下面呢我们就需要去为每一个用户呢去做一个推荐那么我们肯定需要先得到我们的用户的一个列表那么我们就需要在上面这个位置拿到这个u的info.rdd的时候去拿到我们的用户的列表那么拿到这个u的info.rdd呢我们需要做一个map这个操作然后呢我们去写一个Lambda表达式我们就用这个v吧
[07:08] 然后呢我们去得到一个什么呢就是那么我们通过v.getLung1是不是得到我们这个ID了对吧然后呢我们去通过一个connect那么这个的话就可以得到我们的一个这个叫做userIDs那么这样的话就得到一个这个用户的一个列表了那么我们来看一下那么在这加一个注释这个叫用户列表
[07:37] 那么接下来呢我们在这个位置是不是就可以对我们的这个用户列表去做一个便利然后呢我们为每一个用户呢去做一个我们数据的一个推荐那么我们就通过刚才的这个best这个model然后呢点recommend去做一个推荐推荐给这个用户点应该拿到他的int value然后呢我们再去推荐比如说我们一个用户推荐50个这样的一个
[08:05] 那我们推荐就50个吧那么当然我们现在数据会相对比较少但是呢我们也可以去推荐这个50个那么我们去拿到我们的推荐的这样的一个这个ratings然后呢我们就需要把它呢去写入到写入到我们的这个mongo db中那么这个就是推荐的一个这个结果那么我们就需要通过这个mongo的一个spaq去做一个sale这个操作那么要注意的是呢我们做sale的时候我来看一下那么我们
[08:34] 提示一下啊那么我们需要去写的时候呢我们要去得到的是一个java的一个rdd啊去做一个写入所以说呢我们又需要去把它去转换一下并且是一个document这样的一种类型啊那我们怎么样去转换呢我们又需要这么来玩了那么我们要通过我们的jsc点什么呢点这个propel然后呢去得到一个list那我们通过一个这个arrivus
[09:04] 然后点 as list我们去把它丢进来这样的话就得到我们的一个RDD了然后我们并且需要把每一条数据去转成我们的一个document所以我们又需要做一个map这个操作那么拿到一个ve对吧然后这个里面操作我们就来实际的来操作一下那么我们定义一个documentdocument然后我们定义是一个document我们来找一下
[09:33] document应该是我们的这个然后呢去定义一个它然后去new一个document好那么最后return这个documentreturn这个document那么这样的话呢我们就可以给它去put一些内容了那么比如说我们put一个什么呢我们就需要参考我们之前的一个这个数据这个command user那么这个里面数据没了对吧那我们可以来参考一下我们之前的一个
[10:03] 这个结构就是我们double中的这个结构我们找一下找一下这个里面的这个podule然后找到这个recommend user那么有这么几个段对吧好我们就来看一下那么首先第一个是id那么这个id我们去给它设置应该是下滑线id那么我们去设置设一个object object id然后点get去得到一个值这第一个这个这个之段
[10:32] 那么第二个这个字段呢我们来看一下就是谁呢就是我们的UraID那么UraID是谁呢就是我们的这个当前所拿到的VE里面这个ID对不对那么我们来get一个我们来看一下啊那么我们这个VE呢是拿到它的一个什么呢就是我们所推荐的这个用户ID那就是这个product ID啊然后呢我们继续往下面写
[10:59] 那么还有一个是谁呢就是我们这个toUraID就推荐给谁呢推荐给我们这个用户推荐给就是这个Ura这个地方大家别写错就是说我们推荐给谁推荐给他然后呢还有的就是下面的就是一个score这个得分那么这个得分我们怎么来呢来看一下那么这个得分呢我们就要通过他的一个点一个rating这样的一个这个字段但是呢要注意了
[11:28] 那么这个rating我们需要给它去保留两位小数方便我们后面的一个计算那我们来看这个两位小数怎么计算那么我们就来拷贝一下这个我们就不写了把这个就拿过来得分去保留这个两位小数然后score就写到这来了那么我们去保留了这个两位小数之后那么我们需要对这个得分要乘以2
[11:54] 那么为什么要去乘以2呢要注意啊那我们现在的这个总分是50那我们为了去得到一个什么呢就是以100分去展现的这样一个原分值啊所以说呢我们要去呃乘以2就是我们的原分值是100分啊质啊呃质的所以说呢我们要去做一个乘以2的这个动作因为我们现在目前的满分可以去计算一下啊那目前这个满分的是100分你看30
[12:24] 30加30然后这个是60我们本身就是100对吧我们这个就不需要再去加了那么这可能是之前去之前的分数是50分需要加我们这块来写一下那么这块我们就不需要去乘了因为本身的分值就是百分之的我们就找一下下面的这块要把这个去掉我们就不需要再去乘以2了如果是
[12:51] 50分置的话那么就需要乘一下好那么这个就是一个得分了然后呢接下来呢我们还需要给它设置的是一个我们这个日期啊来看一下啊日期呢是date类型啊这个stream类型那么写一个这个document啊.put一个date那么要注意这个类型呢是一个我们的一个年月日的一些所以说我们需要new一个datetime然后呢to stream然后呢y y y然后呢
[13:21] mm然后呢dd啊这样的一个格式去做一个存储那么最后是不是就拿到了这个document啊然后呢我们就可以最后去返回我们的一个java rdd的这样的一个就是我们就写一个java rdd吧其实是我们那个document的一个java rdd那么这样来写吧document的一个java rdd然后呢我们就可以去调用谁呢
[13:47] 我们那个mongo的一个Spark然后呢点c5操作c5它就可以了这样的话呢就完成了我们数据的一个写入了这个代码大家能不能看懂啊就是说我们来总结一下啊就是说我们先去去new一个我们的一个jsc啊这样的一个容器啊就上下文然后呢我们去每为每一个用户呢去做推荐50个这个数据啊然后呢把它去转成一个加网RDD啊这样去转得到一个Docum的对象
[14:16] 然后我们最后做一个C5的这样的一个操作OK好那么接下来我们就把这个程序跑起来那么我们就完事之后来看一下我们这个表里面有没有数据好我们来执行一下走好那么我们看到我们的程序就已经跑完了那么接下来我们来看一下数据有没有写到mongoDB里面来走会发现数据是不是已经写住了那我们可以看一下这个是给用户ID1这个数据推荐了57跟我们刚刚
[14:44] 推荐结果呢是一样的对吧然后呢给这个用户ID1呢推荐了76啊然后呢一直给他去推荐那推荐呢会推荐50个下面来看一下这个还是用户ID1然后呢这个是不是本身就是50条数据啊那我们看下50条然后呢这个应该就是给用户ID为2的数据用户是不是做推荐了然后呢给他去再做推荐啊OK那么这样的话呢我们是不是就基本看到数据呢是就OK了对吧好那么接下来呢我们就来去
[15:13] 还是去访问一下我们这个接口来看他的数据返回那么他应该肯定不就是不是这几条数据了那我们现在肯定能够命中数据了然后呢我们还是需要去先去登录一下那么这个是已经超时了然后呢我们去发起这个请求获取一个验证码然后呢我们来去再去做一个登录好那么我们再去走请求一次我们这个请求啊那么可以看到
[15:43] 这个请求的用户是不是已经就变成谁呢变成57了那么也就是说我们这个推荐的用户已经就发生了改变了对吧就按照我们推荐的一个结果就完成了那么其实我们可以想一下我们的这个项目如果在最后上线的话那么是不是就是我们只需要把我们芒果这个就是Spark的应用跑起来那么我们让它可以比如说定时每天跑一次
[16:06] 然后我们就会把数据不断的去写入这张表里面来而我们之前的业务逻辑就从这个表里面直接去查数据这样的话是不是就完成了我们的一个业务系统跟我们的一个推荐系统这样的一个对接对吧这样的话就搞定了我们来看一下我们的讲义那么我们的实现跟我们的讲义中实现是基本上应该是一样的然后下面我们来看一下测试测试数据是不是也就搞定了
[16:34] 然后我们最终把我们的数据也写入到我们的mongoDB里面来了也OK没有问题通过接口访问是不是也是OK的没有任何问题我们来看一下它的一个响应的数据得分是96这个是OK的没有问题下面92这个是86按照一个得分做一个倒序的这样的一个排序OK好那么这样的话我们是不是就完成了我们的一个好友的一个推荐的这样的一个具体代码的一个编写OK
[17:04] 好那么关于这个好友这个推荐的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面10：在 Typora 中查看 day09 讲义，展示 Spark 与 MongoDB 的配置信息（包括 Spark.mongodb.input.uri、Spark.mongodb.output.uri、j dbc.driver-class-name 等）。
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
Spark.mongodb.input.uri = mongodb://192.168.31.11:27017/tanhuai.recommend.video_20191007
Spark.mongodb.output.uri = mongodb://192.168.31.11:27017/tanhuai.recommend_video_20191007
```

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

```java
package com.tanhuai.Spark.mongo;
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
画面10：PPT 标题为“day09 讲义”，内容包括 Spark 与 MongoDB 的配置信息（Spark.mongodb.input.uri、Spark.mongodb.output.uri、j dbc.driver-class-name 等）。
画面11：PPT 标题为“day09 讲义”，内容包括用户推荐的代码逻辑和流程图。
画面14：PPT 标题为“day09 讲义”，内容包括用户信息的 JSON 数据结构（包含 user_id, avatar, gender, tags, favoriteValue 等字段）。

5) 不要评价画面美观，不要输出与课程无关的内容。

