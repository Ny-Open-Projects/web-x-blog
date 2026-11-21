# 06.谁看过我实现之dubbo接口服务

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\06.谁看过我实现之dubbo接口服务_【海量资源尽在 666java.com】.mp4
- 时长 19分25秒（音频 1166s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个谁看过我的这个实现啊那么首先呢我们来看一下这个功能啊这个其实主要是来记录别人来访问了我的主页的这样的一个信息那么是在我们的首页的这个位置啊我们把这个放大一点来看啊那么其实是在上面是在下面一张图在这里啊
[00:22] 就是说在我们这个今日家人的上面呢会有这样的一个显示就是我们这个最近有四人来访快去查看然后呢我们会去把这最近来访的人呢去给他去列出来那么我们需要说一下就是那么其实我们是用户在访问了我的这个首页之后呢那我会把这个记录下来对吧然后呢我们在这个位置会把它显示出来
[00:48] 那么需要注意的是呢当我们点击之后啊那么其实这个记录就不应该再再次提示了也就是说我们需要去记录一下他所点击的啊这样的一个这个时间啊这一点大家需要去注意一下那么接下来呢我们就来做这个实现啊那么首先呢我们来编解编写这个pojo那么这个pojo呢叫vist啊然后呢我们来看一下他呢有这么几个字段啊ID然后呢用户ID就是我的ID啊
[01:17] 还有vist uid就是这个来访的用户id还有from就是来源啊比如说呢我们有来源于首页啊或者来源于圈子啊等等有这个from然后呢还有一个是date就是来访的一个时间啊所记录的一个时间那么还有一个呢是这个得分要注意了这个得分呢并不会存储到我们这张表里面来而是在我们进行查询的时候呢我们是需要去
[01:44] 给它去返回啊这个得分的呃所以说呢我们是需要这个值的啊哎OK好那么呃我们来呃我们就把这个对象呢我们先啊创建出来把它拷贝一下然后呢找到我们的一个double下面的一个puzzle啊我们先拷贝到这个里面来那么接下来呢我们就来定义我们的这个接口啊那么呃我们就把这个接口呢也拷贝过来啊拷贝到我们这个API啊这个里面
[02:11] 那么是一个VSYSTO一个API那么接下来我们就来看一下我们API中所定义的一些方法首先第一个是做一个C5操作就是去保存我们的一个来访的记录第二个是做一个top查询那么就是按照时间的做一个倒序查询我们最近的一个访客信息那么我们需要传递两个参数一个就是UID一个就是number你要查询几条
[02:40] 然后还有是下面这个是根据时间排到去排去也去查询用户的访客信息但是这个方法的和上面方不同在于什么它的条件是根据一个时间就是前面我们所提到的这个就是
[02:56] 如果你点击查看过之后啊那么我下一次再去查看的话那么就要按照你上一次所查看那个时间往后再去查看这个访客信息了那么大家在我们使用这个比如说像我们这个微信啊微信里面朋友圈里面有一个那个就是
[03:14] 提醒几个用户进行点赞什么的这个是属于最新的消息那么以前我们在使用这种像比如说QQ空间里面也有我的访客有多少个那么也就是说你点过之后大家不会再提醒这么几个用户了如果再有新的一些访客进行访问你的话那么才会去做一个这样的提示所以说要注意了那么这个是按照一个时间去做一个查询那么也就是说我们需要去查询提供这两个
[03:43] 那么找到我们这个Service
[04:12] 然后呢下面呢我们找到我们的一个这个API下面呢我们去呃写一个这个API叫什么呢IMPL啊去做一个实现啊实现一个它好那么我们把这个呢导入进来呃然后呢我们去实现啊它呃所需要提供的有三个啊这个方法一个保存啊两个查询然后呢我们把它呢去注册到啊我们的一个double中啊注册中心里面去
[04:42] 写一个Wolfen然后呢版本呢是1.0.0啊这样的一个这个版本那么好嘞那么这样的话呢我们就这个接口的一个实现啊基本把这个架构呢就打进好了对吧那么下面呢我们就来编写具体逻辑那么首先呢我们肯定是需要去注入我们的一个MongoMongo的一个template啊把它需要注进来的
[05:06] 那么把它呢去注入进来那么我们肯定是需要跟他去做交互的对吧那么接下来呢我们首先来实现第一个这个方法就是我们做这个C5这个操作那么我们去设置这个VistosSet一个ID啊那么通过这个Object啊Get去Object ID啊Get去拿到一个ID然后呢我们再去设置它的一些这个参数那么
[05:32] 这个vist这个uid这个肯定不用设置啊外面肯定会传入进来那么这个也不需要from也不需要那么这个score这个肯定也不需要这个date我们需要去设置一下那我们就给他去设置一个当前的一个时间戳啊这样的话呢就可以了啊然后呢我们去做一个这个c5的这个操作那么就调用这个mongotemplate然后呢做一个c5那我们把这个就是vist4然后呢去导入进来哎传入进来就ok了
[06:01] 然后最后 return我们 return它的一个就是保存成功的一个 id然后好那么这样的话就成功了对吧好那么这个就是我们的save的一个操作那么接下来我们来看一下这个top这个查询那么这个top查询我们肯定是需要去根据我们这个us id这个条件然后我们再根据我们的一个时间date做一个倒序排序再去做一个查询了
[06:30] 那么我们肯定是需要通过什么是不是 race.mongo-template然后做一个faint的一个操作那么需要有两个参数对吧那么第一个参数那就是我们的query对象那第二个参数就是我们 vstor.class
[06:53] 好那我们来看一下query我们怎么样去做一个做了应该是query导错包了应该是query等于query点query然后在我们query中我们去设置一个crittercritter.vail设置一个条件那么这个条件肯定是我查询我当前的用户对吧那么是来访我的吗这肯定是我的 id作为一个条件一一支
[07:23] 这个 user id那么这个呢是我们的一个查询条件啊然后呢我们还是需要去做一个排序的对吧所以呢设置一个位置啊呃为着一个配置对吧那么上面呢我们又需要去定一个配置able了那么定一个哎写一个大写下配置able啊啊配置able那么还是使用它啊然后呢我们去定一个配置able等于什么呢
[07:49] 通过一个page request对象点然后我们设置一个off那么这个page我们肯定是0对吧然后我们设置一个要拿的一个page size就是我们这个number然后我们再去做一个sort的一个排序做一个order desc的一个排序然后通过我们data这个字段去做一个倒序的一个排序
[08:18] 那么其实可以看到上面是不是就是他递的这个字段然后呢我们把这个PageAble呢就丢到我们这个位置这个里面来好那么有query了那么就把它丢过来好那么这样的话呢是不是我们这个方法也就搞定了也是非常简单的这样的一个方法好那么接下来我们来看一下这个的一个实现那么它和这个上面是不是基本呢是一样的啊
[08:41] 只是说我们这个query这个条件呢有所不同那么接下来呢我们就把它呢就拷贝过来那我们来修改一下啊那么呃在我们这个方法那么他就肯定呢就不需要我们这个分页了对吧那我们就把它就去啊然后呢我们还需要去更一个我们的一个呃这个就是条件啊更一个这个条件那么首先第一个呢是usid然后呢依着他然后呢我们再来做一个设置吧我们把这个回测一下啊
[09:09] 把它呢也回车一下然后呢我们再来设置一个这个andand谁呢就是我们的一个这个什么呢date这个时间对吧做一个这个时间然后呢我们再给它去做一个什么呢就是lt就是这个大于这个以后的这个时间那么会作为我们的一个条件然后呢把这个date传进去来
[09:38] 好这样的话就会作为一个条件就是我们上一次所查询那个时间点啊去大于这个时间呢我们就去做这样的一个查询当然这个时间点呢我们肯定会在我们查询逻辑中啊去做一个记录对吧做一个记录然后呢只要去大于这个的时间那我们就把这个数据呢就给他去查询到了啊那么是这样的一个条件那么当然了我们肯定还是需要给他去做一个排序对不对啊做一个什么呢
[10:07] 做一个这个我们看啊这个里面啊但这个里面不能去我们来看一下啊在这个位置去做一个排序那么我们要通过一个什么呢位置啊sort去做一个排序那么sort by order然后desd然后呢去根据谁呢还是要根据这个date去做一个啊排序了那么就说我们这个是他条件那么同样的也是需要去根据这个date去做一个这个排序然后去
[10:33] 做一个这个查询啊那么大家其实我们这个并没有去做吧因为我们这个vistos我们前面说过这个score啊这个我们还没有去得到啊这个得分所以说呢我们还需要给他去修改一下逻辑啊其实上面和下面这个逻辑是一样的啊那么我所以说呢我们就去写一个我们通用的一个这个逻辑好了那么写一个私有方法吧那么这个方法呢返回值呢就是一个
[11:03] list list一个vsts然后呢我们去查询queryvsts list好那我们就去查询它吧然后呢我们把这个query呢作为一个参数呢给我们去传递过来然后呢我们在这个里面呢去做一个查询呢就可以了比如说我们暂时可以先把这个这个方法我们先把这个代码先拷贝过来然后呢上面这块呢我们就这个就不需要了对吧那我们就直接调用this点
[11:33] 这个query把这个query对象传递过去就OK了然后呢这个上面的这个逻辑是不是也是一样的这样的话就OK了那么关键我们是不是要来看这个里面的逻辑那么在我们这个逻辑中呢其实除了我们正常的一个这个数据查询之外呢我们还需要去给他去查询什么呢查询我们的一个score的一个得分呢那么这个其实是一个关键那我们还是把它return把它return它
[12:02] 那我们需要给他去做一个填充了对吧好那么接下来呢我们来看一下这个得分又该如何去做一个这个查询而我们这个得分呢其实就是他的缘分值那么这个缘分值呢是在哪个里面去存储呢是不是在我们的这个用户的一个推荐或者说推荐用户这个表里面来也就是说在我们的这个叫做CommandUse这个里面是不是才存在这个Score
[12:30] 那么其他地方是没有这个score的对不对所以说呢我们我们就只能通过这个位置啊去做一个啊这个查询了那么接下来呢我们就来写一下这个查询的这个逻辑那么我们呢是需要对它去做一个便利啊然后呢去做一个查询那么我们呢还是需要通过我们的这个mongodb的这个template然后我们去fund1去做一个查询
[13:00] 那么query呢我们先设置为num那么这个class呢就是我们的recommendUra这个.class去做一个查询那么我们来看一下它的一个条件啊那我们来构造一个这个query这个条件那么我们就叫query吧query然后呢叫做query啊叫recommend吧recommend query啊等于什么呢query.query做一个
[13:30] 构建然后呢credit点设置一个vail条件vail条件谁呢来看一下那么这个里面肯定是这两个对吧作为一个条件那么我们这个user iduser id是谁呢我们来看一下那么用户user id那这个应该是一只谁呢是我们这个中的谁大家可以想一下他是我们的访客id对吧就是说这个别人来访问我
[13:57] 对吧然后呢这个这个UID是指的对方的那个ID啊然后呢我们把这个回测一下把它呢然后呢我们去到这到这然后呢去回测一下啊and啊去添加一个谁呢就叫怎么呢我们来写一个叫toUID就是推荐给谁呢推荐给我对吧推荐给我然后呢点然后呢ease谁呢就是我的vistos里面的
[14:24] 所以get什么UraID这两个别搞混那么一个是这个UraID一个toUraID那么我们去设置一个query那么把它传递过来好那么这样的话其实我们就拿到了一个我们这个叫做叫做什么叫做recommendUra这样的一个对象那么接下来我们是需要去做一个判断那么如果空不等于recommendUra对象的话
[14:54] 那么接下来我们就需要给他设置score对吧我们需要给他去他设置点set一个score等于谁是不是就是这个recommend userrecommend user点get score做一个score这样的一个设置那么这个是他不等于空如果他等于空如果等于空怎么办我们就给他设置一个如果等于空
[15:22] 需要给他设置一个默认值默认值这个我需要和产品经理沟通一下我们这边暂时把它设置比如说设置为30或者40都可以那30设置为一个30这样的话就OK了对吧然后最后去做一个返回就OK了那么这样的话我们其实就已经完成了我们实现类的这样的一个编写那么接下来我们来看一下那么这个是我们接口的一个
[15:51] 实现啊结果这个实现下面呢我们去做一个测试啊那么这个测试用力呢我就不写了我就直接把它来拷贝过来那我们来看一下这个测试用力啊那我们拷贝到我们这个就是test这个下面来拷贝再来好那么在我们这个测试用力中啊那我们来看一下啊它是做了什么事情啊那我们做一个save这个操作保存100条数据啊进我们的这个库里面来当然我们需要先把我们这个double呢先停掉啊要不然是不能够运行的
[16:20] 好那么我们来执行一下那么可以看到它的用户ID呢设置的是1到10然后呢这个访客ID呢是11到50然后呢做一个save这个操作啊好那我们来执行一下好那么等待它的一个执行好那么现在呢我们这个呢就执行结束了啊下面我们来看一下我们的这个mongodb然后呢我们刷新一下那么可以看到呢在下面有个vistos哎这个是不是我们之前就有这个
[16:49] 我们这样吧我们把它再drop掉吧然后呢我们重新来测试一下那么我们刷新一下然后呢我们再次去做一个执行好那我们再等待一下好那么再次呢执行结束了那我们来刷新一下然后呢下面这个Vistos然后呢我们去打开来看一下那么这个里面呢就有应该是有100条数据吧后面就没了对吧100条这个数据然后呢我们可以打开来看一下比如说呢这一条数据呢就是UID为9
[17:19] 他的访客就是24这个用户给他来访问他然后来源的首页然后大概可以看这么多的一些数据那么我们也可以去查询一下比如说我们可以写一个测试用例我们来做一个查询好那么下面我们就来写一下public然后返回值word然后test一个query然后我们来看一下我们去设置一个
[17:48] 设置一个这个test好然后呢我们去调用什么呢就是我们的查询的方法啊race.vestapi.top去做一个查询那么比如说我们查询我1这个用户啊比如查询前10个然后呢我们来看一下它的一个返回的一个集合然后呢我们去做一个便利啊把它呢就打印出来了好那我们来看一下这个效果啊好走好那我们来等待它的一个执行
[18:17] 好 那我们这个执行呢报错了原因是呢刚刚我们在写这个位置的时候呢就是它报了一个空子针异常那么错误呢是在这儿我觉得我们刚刚这个判断的这个这个参数我们去引用错了应该是去判断它刚刚我们判断的是这个regmon的query这个对象这个是有点问题好 那我们再次来执行一下
[18:40] 好那么接下来呢我们来看一下我们这个访问的好那我们来看一下这个数据啊那么也就是说当前的为我们这个用户啊就是一这个用户我们去查看他的一个访客啊有这么多然后呢我们来看一下他的这个得分啊是不是也全部都拿到了对吧那么这样的话呢其实我们就已经完成了我们这个double接口的一个编写好那么下面我们来看一下我们的这个
[19:09] 讲义啊那么这个讲义呢这个应该跟我们刚刚的实现的基本上是一样的啊哎OK那么这个实现呢是跟我们那个基本上差不多的啊哎OK好那么关于我们这个谁看过我的一个double接口的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 MongoDB 的 MongoTemplate 实现访客记录的保存与按用户和时间维度查询的推荐服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示一个名为“桃花传情”的社交应用界面，包含“今日达人”和“推荐”板块，用于演示业务场景。
画面 2：展示 `VisitorsApi.java` 接口定义，包含 `saveVisitor` 和 `topVisitor` 两个方法，用于定义服务契约。
画面 3：展示 `VisitorsApiImpl.java` 实现类，包含对 `saveVisitor` 和 `topVisitor` 方法的空实现。
画面 4：在 `saveVisitor` 方法中，注入 `MongoTemplate`，并开始编写保存逻辑，使用 `save` 方法。
画面 5：完成 `saveVisitor` 方法，设置 ID 和日期，调用 `save` 保存对象，并返回 ID 的十六进制字符串。
画面 6：在 `topVisitor(Long userId, Integer num)` 方法中，使用 `Pageable` 和 `Sort` 构建分页和排序查询。
画面 7：在 `topVisitor(Long userId, Long date)` 方法中，构建查询条件，按日期降序排序。
画面 8：在 `queryVisitorsList` 方法中，遍历访客列表，并为每个访客查询推荐用户。
画面 9：在 `queryVisitorsList` 方法中，使用 `Criteria` 构建推荐用户查询，并设置访客的分数。
画面 10：在 `queryVisitorsList` 方法中，使用 `MongoTemplate` 的 `findOne` 方法查询推荐用户，并设置访客分数。
画面 11：展示项目目录结构，包含 `api`、`Service`、`test` 等模块，以及 `VisitorsApiImpl` 的完整代码。
画面 12：展示 MongoDB 数据库中的 `visitors` 集合，包含多个访客记录，用于验证数据持久化。
画面 13：展示测试类 `TestVisitors` 的运行结果，显示测试通过，日志中包含访客数据和推荐用户信息。
画面 14：展示测试文档 `day09 试写.md`，其中包含测试相关的代码和注释，用于记录和说明测试过程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
String saveVisitor(Visitors visitors);
/**
 * 按照时间倒序排序，查询最近的访客信息
 * @param userId
 * @param num
 * @return
 */
List<Visitors> topVisitor(Long userId, Integer num);

/**
 * 按照时间倒序排序，查询最近的访客信息
 * @param userId
 * @param date
 * @return
 */
List<Visitors> topVisitor(Long userId, Long date);
```

画面 3：
```java
@Service(version = "1.0.0")
public class VisitorsApiImpl implements VisitorsApi {

    @Override
    public String saveVisitor(Visitors visitors) {
        return null;
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Integer num) {
        return null;
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Long date) {
        return null;
    }
}
```

画面 4：
```java
@Autowired
private MongoTemplate mongoTemplate;

@Override
public String saveVisitor(Visitors visitors) {
    visitors.setId(ObjectId.get());
    visitors.setDate(System.currentTimeMillis());
    this.mongoTemplate.
        save(T objectToSave, String collectionName)
        scriptOps()
        setApplicationContext(ApplicationContext applicationContext)
        setReadPreference(ReadPreference readPreference)
        setSessionSynchronization(SessionSynchronization sessionSynchronization)
        setWriteConcern(WriteConcern writeConcern)
        setWriteResultChecker(WriteResultChecking writeResultChecking)
        stream(Query query, Class<T> entityType, String collectionNam, CloseableIterator<T> closeableIterator)
        ...
```

画面 5：
```java
@Override
public String saveVisitor(Visitors visitors) {
    visitors.setId(ObjectId.get());
    visitors.setDate(System.currentTimeMillis());
    this.mongoTemplate.save(visitors);
    return visitors.getId().toHexString();
}
```

画面 6：
```java
@Override
public List<Visitors> topVisitor(Long userId, Integer num) {
    Pageable pageable = PageRequest.of(page: 0, num, Sort.by(Sort.Order.desc("")));
    Query query = Query.query(Criteria.where("userId").is(userId)).with(pageable);
    return this.mongoTemplate.find(query, Visitors.class);
}
```

画面 7：
```java
@Override
public List<Visitors> topVisitor(Long userId, Long date) {
    Query query = Query.query(Criteria
        .where("userId").is(userId)
        .and("date").lt(date)
        .with(Sort.by(Sort.Order.desc("date")));
    return this.mongoTemplate.find(query, Visitors.class);
}
```

画面 8：
```java
@Override
public List<Visitors> queryVisitorsList(Query query) {
    List<Visitors> visitorsList = this.mongoTemplate.find(query, Visitors.class);
    for (Visitors visitors : visitorsList) {
        Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId()));
        this.mongoTemplate.findOne(query, RecommendUser.class);
    }
    return visitorsList;
}
```

画面 9：
```java
@Override
public List<Visitors> queryVisitorsList(Query query) {
    List<Visitors> visitorsList = this.mongoTemplate.find(query, Visitors.class);
    for (Visitors visitors : visitorsList) {
        Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId())
            .and("toUserId").is(visitors.getUserId()));
        RecommendUser recommendUser = this.mongoTemplate.findOne(recommendQuery, RecommendUser.class);
        if (null != recommendUser) {
            visitors.setScore(recommendUser.getScore());
        } else {
            visitors.setScore(300);
        }
    }
    return visitorsList;
}
```

画面 10：
```java
@Override
public List<Visitors> queryVisitorsList(Query query) {
    List<Visitors> visitorsList = this.mongoTemplate.find(query, Visitors.class);
    for (Visitors visitors : visitorsList) {
        Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId())
            .and("toUserId").is(visitors.getUserId()));
        RecommendUser recommendUser = this.mongoTemplate.findOne(recommendQuery, RecommendUser.class);
        if (null != recommendUser) {
            visitors.setScore(recommendUser.getScore());
        } else {
            visitors.setScore(300);
        }
    }
    return visitorsList;
}
```

画面 11：
```java
@Service(version = "1.0.0")
public class VisitorsApiImpl implements VisitorsApi {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Override
    public String saveVisitor(Visitors visitors) {
        visitors.setId(ObjectId.get());
        visitors.setDate(System.currentTimeMillis());
        this.mongoTemplate.save(visitors);
        return visitors.getId().toHexString();
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Integer num) {
        Pageable pageable = PageRequest.of(page: 0, num, Sort.by(Sort.Order.desc("")));
        Query query = Query.query(Criteria.where("userId").is(userId)).with(pageable);
        return this.mongoTemplate.find(query, Visitors.class);
    }

    @Override
    public List<Visitors> topVisitor(Long userId, Long date) {
        Query query = Query.query(Criteria
            .where("userId").is(userId)
            .and("date").lt(date)
            .with(Sort.by(Sort.Order.desc("date")));
        return this.mongoTemplate.find(query, Visitors.class);
    }
}
```

画面 12：
```json
{
  "id": "5daf10177da931a6c4d8593",
  "userId": 32,
  "from": "首页",
  "date": 1571724010111,
  "score": 300
}
```

画面 13：
```java
Query recommendQuery = Query.query(Criteria.where("userId").is(visitors.getUserId())
    .and("toUserId").is(visitors.getUserId()));
RecommendUser recommendUser = this.mongoTemplate.findOne(recommendQuery, RecommendUser.class);
if (null != recommendUser) {
    visitors.setScore(recommendUser.getScore());
} else {
    visitors.setScore(300);
}
```

画面 14：
```markdown
2.4. 测试

package com.tanhua.dubbo.server.api;
import org.apache.commons.lang3.RandomUtils;
import org.bson.types.ObjectId;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestVisitors {

    @Autowired
    private VisitorsApi visitorsApi;

    @Test
    public void testSaveVisitor() {
        Visitors visitor = new Visitors();
        visitor.setUserId(32);
        visitor.setFrom("首页");
        visitor

