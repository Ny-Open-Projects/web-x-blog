# 16_数据迁移_业务代码编写_热点文章接口2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\16_数据迁移_业务代码编写_热点文章接口2【海量资源尽在 666java.com】.mp4
- 时长 20分58秒（音频 1258s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去完成当前这个同步的方法同步的方法该怎么去做呢我们可以写一个思路首先呢咱们是要去查询文章这样吧根据文章ID查询数据查询数据啊咱们主要的是分两块第一个呢是要从数据库中去查然后第二个呢如果说数据库中没有的话咱们要从HBase中去查因为这个咱们之前是做过同步的对吧
[00:35] 然后呢然后这样啊是同步热点数据到哪呢咱们的这个叫做一个是数据库第二个呢同步数据到芒果好那这样的话就思路就写完了啊下面的咱们就来先去写一下啊下面该怎么去写呢我来看一看啊首先咱们在这儿去打印日志吧报告应付
[01:09] 开始热数据同步好吧那个article id文章id文章id是多少呢好口号然后是article id好然后下面咱们可以去获取数据get hot然后是article rti rti cl1啊c le然后呢是6 u a nt i t y啊然后根据什么呢根据当前的什么
[01:43] 文章ID,AP,articleID叫AP,articleID吗我看看啊是它是吧叫articleID啊那最终返回的是啥呢咱们封装个方法这是啊返回的是啥呢返回的呢就是当前那个综合的实体类RTICLE,Quality或者返回它呢最终保存的时候啊咱们好保存非常好保存所以说呢咱们让它去返回那这个方法没有咱们可以创建出来好来看一下这是什么
[02:26] 获取热数据热数据的ArticleQuality好下面的咱们可以怎么写呢这个写法是比较简单咱们因为咱们已经入进来了当前的就叫ArticleService是吧那这个注意了我看看上面是不是已经注意了呢叫全点了省得写错点有一个叫做Select
[02:58] 什么呢get一个叫做article created by article id这个呢其实就是从哪从哪查的呀这个就是从当前的数据库中去查的好吧咱们可以把当前的article id放进去这里边咱们需要用一个叫做lang value设置完之后呢它就能返回某一个对象这个对象啊有可能未空有可能未空咱们可以判断一下数据库中查不着的话
[03:29] 等于等于他这时候呢咱们就可以干嘛呢可以从这个里边的另外一个方法去查询就是负还是当前的ArticleID然后呢他返回的复职还是他那这样的话就能保证啊你先从数据库中查看有没有说没有的话你再从HBase中查把这个数据拿到就可以啊最终咱们是返回当前这个
[04:02] 对象就可以了好吧行那这是获取当前的一个数据然后接着往下看啊这时候呢咱们就可以去判断了啊来嗯嗯正判断吧当前的他呢不等于浪不等于浪然后呢你就可以去做这两件事啊第一个是同步数据库然后第二个呢是同步到mongo中好那咱们可以再去写一个方法叫hot ap article
[04:40] 然后是P S Y C这时候呢传的东西呢就是当前的Article Quality这是一个啊第二个第二个是啥呢第二个就是当前的热点文章要投入到Mongo中Hot R P P啊AP Article A R T I C R E然后是MongoTo Mongo吧To MongoS YS Y
[05:15] 这个数据其实也是当前那个Article Quality最终我们可以在这去打印人质这两个码咱们就来写E-L-S-E-Log-Info咱们就可以说一下找不到对应的热数据Article ID-R-I-C-L-E-D网号然后是Article ID
[05:49] 那行那这样的话咱们就试转了当然了你这个同步完之后咱们也在这可以打印一个说数据叫热数据热数据同步完成好然后这时候你再把这个ID印一下就可以了这样方法咱们还要再去创建先去创建这个然后再去创建怎么还不好使呢抛起家回车不好使创建手动创建这样这么行拷贝是他
[06:29] 拷贝一下然后呢把这个方法名拷过来参数一样呢那这个是啥呢这是同步到数据库下面这个呢是同步到芒果好那下面呢那下面呢咱们就去写一下这个方法那这个同步该怎么去同步呢从数据库中首先呢是思路日量先去查询先通过文章ID查询
[07:13] 数据库是否存在好吧然后呢是怎么着存在不需要保存不需要保存因为已经有了是吧然后是怎么着呢不存在然后是新增热点数据这样就完了啊那这个ID怎么拿呢你可以通过当前的对象啊去拿到当前的IDgetArticleID好吧这个呢就是当前的ArticleID
[07:45] 拿到ID之后,咱们可以去打印制,点log点info,然后是开始将热数据从哪啊?
[08:00] 从当前的这种HBase应该不是HBase应该是从当前的这种数据库,比如从哪吧应该是从不到哪,从不到买Circle
[08:21] 因为数据有可能是从HBase中也有可能是从MySQL中查出来的是吗好同步到MySQL然后是JP article.ticle id可以打印一下是故事当前这个id然后下面咱们就可以再去判断当前这个none不等于当前的article id然后我可以去做这东西这个咱们就可以直接语信
[08:55] 让我先走好在这打印一句话log.info说呀AP article id不存在AP article id不存在无法进行重复然后下面呢如果说他没事的话呢下面呢咱们就可以去查询了啊那查询的时候你可以看一下AP hot article mypro有一个点
[09:27] slack的list这时候你就可以去传一个当前的什么呢叫做ap-articles你有一个它然后你往里边去设置个值ap-articles.setarticleid把当前那个articleid装进去这样的话就有条件了你把它装到这它这时候就能返回一个列表这列表来就查询了
[10:01] 来看一下啊首先是none不等于当前的hotarticlelist并且干嘛hotarticlelist.isempty然后当然这边是有一个叫做free是吧如果说查到了查到的话查到就干嘛呢不保存查不到的时候呢咱们再去保存也就是说咱们在这有个yes好这个怎么写啊查都不用写你直接在这打印一句话就可以啊说说my circle啊
[10:39] 数据同步数据啊已同步不需要再次重复好吧那可以把他年的AP article ID给出来AP article ID冒号他然后是他啊哦如果说他存在的话呢我们就可以干嘛呢就可以通过当前这个对象啊而有一个叫做get hotarticles就能拿到一个对象拿了对象之后呢咱们就可以去保存了啊
[11:14] AP-hot-my-pro,哪有一个insert就把AP-hot-articles1装进去,用K2把这个名改一下,改成temp,等我区分好吧这样就可以了那你说这里边还有一个叫get-hot-articles吗可以看一下啊那这个呢其实就是Nu了一个东西Nu了一下啊这个呢就是首先呢要去Nu一个东西Nu一个当前对象然后是往里边设了一个article-id
[11:43] 时间啊他的分值还有什么他个呃name还有他的创建时间好吧其实就是拗了一下方便些如果说你不想在这拗的话你也可以在这扭是吧也是也是可以的嗯那行那这个咱们从当前那个什么同步到数据库啊咱们就说完了啊然后下面呢咱们来去说一下同步到mongo中该怎么去设置同步到mongo中呢其实这样咱们可以看一下这个笔记中怎么写的啊咱说一说啊
[12:13] 首先也是拿到一个文章的ID然后这里边是把文章ID作为一个routingT其实就是作为了一个主件然后最终去保存的时候其实是一个对象叫做mongolstorageentity最终保存其实也是这个对象这个对象咱们之前大概去说过但是并没有细说咱们可以再去看一看咱们可以打开当前的它咱们可以去拷贝一下它找到这个对象
[12:42] 对象里边你看他是继承了一个叫做storage entity然后这个是id这就是主界叫rowkey然后接着往下看然后下面你又可以去看一下这里边的东西里边其实有一个列表叫datalist这个datalist其实就是storage data这个data里边又有一些东西是吧哪一个类是吧里边的属性是啥不就这意思吗
[13:09] 所以说你要去把这些东西都给他找全了最终就能去保存你可以看你看首先是查看看他是不是等于当如果说他要是不等于那的话说明已经有了有的话咱们就不需要再次去同步如果他没有的话你需要去把对象去重新去创建了重新去创建然后往里边去设置一个data list但rokey的话就是当前的主件是吧就是当前的ad然后最终去保存就可以了
[13:38] 好吧关键的是你怎么去拿谁呢关键是怎么拿当前的这个什么storage date list那这个很简单就是这里边其实已经拿到了好吧这边已经拿到了因为这个刚才说了就是从当前的my circle中或者是从当前的HBase中已经获取到了好吧那行那咱们下面呢就来去把这个单转写写好来看一看啊打开当前字好这个啊嗯
[14:04] 前面的方法都一样咱们也是要通过当前的it去查询所以说要去获取到前的AP article id这个代码我就考过了背过来了然后是这是不是my circle了是什么了mongo下面接着往下看下面的话咱们就是首先咱们要去做一个rokey stringrokey等于谁rokey就等于AP article id它是一个
[14:34] 所以说你要去转称stringdate convert utils.toString然后是把当前的一个data.id装进去好那这样就可以了这个准备完了准备完之后你还要去准备一个datalist是吧咱们可以用当前的mongo-template.有一个叫做fine-by-id先通过当年它去查看看有没有是吧有的话你就需要再去
[15:05] 再去插入了好吧这个呢装入的就是mongoStorageEntity是吧是他吧drclass好最终返回的就是一个叫做mongoStorageEntity然后您可以判断啊判断啥呢他到底是否等于none不等于他不等于他的话说明已经有了这时候你就可以来打印一下说什么呢说mongomongo数据
[15:41] 你同步不需要干嘛呢再次同步啊好article id ap rt s e r e d然后是article id好了然后下面呢咱们就可以去同步了啊这时候就是没有呗嗯好那这个时候你需要去干嘛呢你需要去判断啊嗯当然不用判断你直接去拿数据就可以了用当前的呃article quality然后点get一个storage
[16:16] 最终就能拿到一个这种storage.datelist这时候你就可以再去判断这个判断其实为了防止它为空不等于之前的storage.datelist并且非storage.datelist.isEmpty它不为空这时候你就可以去用出来一个它它不是为空吧
[16:45] 这时候呢就可以扭一个mongo他往里边去设值一个值就是setRookie其实已经设完了就是他好第二个呢就是当前的一个listdatalist就把这个datalist装进去好了那这样就可以了啊中段你就可以调用mongo的template.insert就把当前这个mongo storage entity装进去就完了这样就保存了啊
[17:16] 咱们就可以干嘛呢在这啊这个是这什么我们在这呢就可以去打一句话log.info将数据从布到mongo完成是aparticleid等于谁呢等于就是articleid那行那这个方法咱们就写完了啊写完之后咱们这里边还有一个方法咱们再去写写
[17:52] 这里边好像还有一个删除的方法没有写这个删除的话咱们要删除三块内容哪三块呢就是刚才说的那个什么mycircle还有什么mongoahbase咱们也要删好吧咱们就可以调用第一个data by id这是删除什么呢删除当前的id这个是删除出具户
[18:22] 下面咱们要去删除HBase删除HBase的话首先你得有一个什么东西我们可以看HBase storage client有一个叫做什么有一个叫做delete rowget有一个叫做HBase client有一个delete row根据删除某一行这个参数有两个第一个就是当前的表名这个表的话就是HBase instance
[18:55] 这个表,然后第二个是rokey,rokey怎么拿呢?
[19:01] rokey的话呢其实你有这个ID之后呢你就可以拿到这个rokey啊我们可以拿到什么?
[19:11] 嗯AP article这个是AP article.set一个叫做IDget ID应该是get hot ID,是吧?
[19:24] article ID啊好,好,好吧这个呢,行
[19:29] 它说不行呢这个是一个integer你需要去转成一个什么转成一个string就行了啊所以说咱们在这直接用当前的data.convert.cultiv.r有一个string后边东西装进去还是这样的话就是一个rowkeystringrowkeyrowkey就等于它那行那这个拿到之后啊这时就把当前那个rowkey装进去就可以了
[20:03] 行这样的话咱们就算是删除成功那mongo稍微麻烦一些咱们可以先去查find by id然后你可以根据当前的rowkey去查然后是根据当前的返回的是一个mongo storage entityclass你先去看一下它有没有是吧if none不等于当前这个storage entity然后咱们就可以去删除了
[20:41] 删除的方式呢就是mongo-applic.remove可以把这个对象放进去你查出来这个对象啊那这样的话就算是删除成功了啊那这个热点文章呢咱们这个方法咱们就写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现文章热度数据的同步与持久化，涉及 MySQL、MongoDB 和 HBase 三种数据源的读写操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `ApiHotArticleService` 类中 `hotArticleSync` 方法的定义，用于同步热点文章数据。
画面2：在 `hotArticleSync` 方法中，调用 `getHotArticleQuantity` 方法获取文章热度数据。
画面3：展示 `getHotArticleQuantity` 方法的实现，通过 `articleQuantityService` 获取数据。
画面4：在 `hotArticleSync` 方法中，根据获取到的 `articleQuantity` 对象决定是否同步数据。
画面5：在 `hotArticleSync` 方法中，使用 `mongoTemplate` 查询 MongoDB 中的 `articleQuantity` 数据。
画面6：在 `hotArticleSync` 方法中，使用 `mongoTemplate` 查询 MongoDB 中的 `articleQuantity` 数据。
画面7：在 `hotArticleSync` 方法中，根据查询结果决定是否插入数据。
画面8：展示 `StorageData` 类的定义，用于存储数据。
画面9：在 `hotArticleSync` 方法中，使用 `mongoTemplate` 查询 MongoDB 中的 `articleQuantity` 数据。
画面10：在 `hotArticleSync` 方法中，使用 `mongoTemplate` 查询 MongoDB 中的 `articleQuantity` 数据。
画面11：在 `hotArticleSync` 方法中，根据查询结果决定是否插入数据。
画面12：展示 `ApiHotArticleService` 类中 `deleteHotData` 方法的定义，用于删除热点数据。
画面13：在 `deleteHotData` 方法中，使用 `hBaseStorageClient` 删除 HBase 中的热点数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public void insert(ApiHotArticles apiHotArticles) {
    apiHotArticlesMapper.insert(apiHotArticles);
}

@Override
public void hotArticleSync(Integer articleId) {
}

@Override
public void deleteById(Integer id) {
    apiHotArticlesMapper.deleteById(id);
}

@Override
public List<ApiHotArticles> selectExpireMonth() {
    return apiHotArticlesMapper.selectExpireMonth();
}
```

画面2：
```java
//根据文章id查询数据
log.info("开始热点数据同步。文章id: {}", articleId);
ArticleQuantity articleQuantity = getHotArticleQuantity(articleId);
//同步热点数据到缓存
hotArticleIdToMongoSync(articleQuantity);
//同步数据到mongo
```

画面3：
```java
private ArticleQuantity getHotArticleQuantity(Integer articleId) {
    articleQuantityService.getArticleQuantityByArticleId(articleId);
}
```

画面4：
```java
//根据文章id查询数据
log.info("开始热点数据同步。文章id: {}", articleId);
ArticleQuantity articleQuantity = getHotArticleQuantity(articleId);
//同步热点数据到缓存
hotArticleIdToMongoSync(articleQuantity);
//同步数据到mongo
```

画面5：
```java
//根据文章id查询数据
log.info("开始热点数据同步。文章id: {}", articleId);
ArticleQuantity articleQuantity = getHotArticleQuantity(articleId);
//同步热点数据到缓存
hotArticleIdToMongoSync(articleQuantity);
//同步数据到mongo
```

画面6：
```java
//根据文章id查询数据
log.info("开始热点数据同步。文章id: {}", articleId);
ArticleQuantity articleQuantity = getHotArticleQuantity(articleId);
//同步热点数据到缓存
hotArticleIdToMongoSync(articleQuantity);
//同步数据到mongo
```

画面7：
```java
private void hotArticleIdToMongoSync(ArticleQuantity articleQuantity) {
    //通过文章id查询，数据是否存在
    Integer aparticleId = articleQuantity.getArticleId();
    log.info("开始将数据同步到mysql, articleId: {}", aparticleId);
    ApiHotArticles apiHotArticles = apiHotArticlesMapper.selectById(aparticleId);
    List<ApiHotArticles> hotArticles = apiHotArticlesMapper.selectList(null);
    if (null != hotArticles && hotArticles.size() > 0) {
        //存在，则不需要保存
        return;
    } else {
        //不存在，新增热点数据
        ApiHotArticles apiHotArticles = new ApiHotArticles();
        apiHotArticles.setArticleId(aparticleId);
        apiHotArticles.setArticleQuantity(articleQuantity.getArticleQuantity());
        apiHotArticles.setCreateTime(new Date());
        apiHotArticles.setUpdateTime(new Date());
        apiHotArticles.setIsDeleted(0);
        apiHotArticles.setIsHot(1);
        apiHotArticles.setIsSync(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.setIsSyncing(0);
        apiHotArticles.setIsSynced(0);
        apiHotArticles.set

