# 12_文章首页接口改造_后端_文章列表展示service代码2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\12_文章首页接口改造_后端_文章列表展示service代码2【海量资源尽在 666java.com】.mp4
- 时长 13分25秒（音频 805s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续啊刚才说了这个呢只是从什么呢从当前缓存中去加载数据但是缓存中如果说没有数据或者说当前缓存的不是首页那不是首页的时候呢咱们不可能是直接从缓存中去拿数据的然后下面咱们还要再去继续判断那这个呢不可能是加载更多或者是加载咱们的最新更新是吧那这个咱们该怎么去设置呢首先呢咱们还得去做一个判断啊
[00:29] 那啥呢就是用户是否为难是否为空那为空怎么办呢为空就加载默认默认的然后不为空呢为空就是先去找推荐的热文章找不到推荐的再去查找什么再去查找当前的默认默认出现的吧默认出现的热文章
[01:05] 好这个能看明白吧就这么几种情况啊首先呢咱们看一下用户当年是否为空如果为空的话呢咱们就直接加在默认的就行了如果不为空咱们先去找推荐的热文章那为什么那你能找着吗能找着为啥呢因为咱们之前呢在咱们这一块去做这个热文章计算的时候呢其实呢咱们为每一个用户都去保存了一份热文章当然咱们也去保存了默认的热文章好吧
[01:32] 行那这个呢其实咱们都能找得着啊所以说咱们在这儿先去找推荐的这文章然后是找不着的话咱们再去找默认的默认推荐的这文章就可以了好吧所以说在这儿先去判断那当前这个啊当前这个用户当前这个用户user云浪是一种情况啊然后呢然后是elsc啊是另外一种情况他等云浪的时候呢
[02:02] 那就是那时候那就是去加载什么推荐的热文章啊要不然的话咱们就设置这种默认的文章啊咱们可以把它给删了啊这里边咱们咱们可以去委屈一些东西啊当然咱们可以先去封装一个方法封装一个方法啊这个咱们可以去加一个叫get什么呢get user article v2好吧
[02:29] 然后参数就是当前的第一个就是user然后第二个是dto第三个是type这个返回的其实也是一个热文章什么意思list这叫什么叫做ip article怎么叫user article list好吧叫它你把它给返回return现在response result.ok
[03:00] 好就把当前那个user article list放进去完了然后下面还有一个是默认的这是默认的咱们去atdefund article vticle v然后这个参数其实也是一样是吧也是第一个是dto然后第二个是type因为这个没有用户没有用户好那么下面就可以去这样还是用它去接收这个咱们叫做defund好吧
[03:34] 第一,FuLT然后最终的你也可以去把它去装进去就完事了啊把这个装进去行那这两个方法咱们要去写写好吧先写下边这个一会儿再去写上面这个好吧因为下边这个比较容易啊好那就是去去加载加载默认的热文章出去但你要想去加载热文章出去的话你首先呢首先呢得先去输入当前的什么呢
[04:12] private有一个叫做 ap hothot有一个article.map就它然后你先把它注进来你看这里边有没有方法来默认的来找点有一个叫做load hot list location其实这个就是咱们之前用过的方法然后第二个是咱们的type
[04:42] 就是type这样的话就能去找着当前的这种热文章的数据我们叫hotlist好吧hotlist行下面怎么着呢拿到了这个热文章之后呢那你说你光拿热文章其实没有用因为最终咱们要返回的是list里边包含的是AP article所以说你要通过当前的热点文章去查找它的什么文章数据
[05:12] 文章数据啊但是这里边已经包含了什么呢包含了当前的article id是吧所以说呢这样找其实就容易了啊那这时候呢你就可以去再做一个做一个判断吧说hotlist这写啊non不等于他并且呢并且呢hotlist.isample在前面去加一个什么一个非是吧这时候呢你就可以去循环它了啊
[05:44] list.for然后这时候呢就是hotarticles这时候你就可以去查找了那查找的话你这时候你还得去用谁呀这里边应该是有的哪个呢叫apaparticlemapper有它吧点有一个selectid这时候呢你可以把hot.getarticleid这样
[06:13] 那这个好像报错了是吧你用一个浪类型去转换一下volume off把后边这串你去好他返回的呢其实就是一个一个的对象吧叫一批article查找完查到我查到之后呢这时候呢你需要去把它装到一个集合中所以说咱们在这啊再去创建一个集合叫listaparticleok然后呢咱们是叫做article list
[06:50] 等于一个list4,等于有一个new,一个list好吧然后呢咱们就可以去把这个对象啊一个一个装进去就完事了啊等于有一个add然后你把它你的AAP article装进去把这个list返回,那就可以了好吧咱们在这最终是把它给返回,为tun当前者
[07:17] 好那这个咱们就算是做完了啊这是加载默认的文章数据写完默认之后呢咱们可以干嘛呢可以继续啊继续写当前的一个根据用户去查询的热点文章的数据啊我们可以再次去创建一个方法有方法呢就是根据这是先从用户推荐的点中点中查找什么热文章如果没有哎如果没有啊
[07:50] 再从大文章那边查询数据好那完了啊那这个其实代表咱们之前也写过啊写过也就是说你那你先干嘛呢你得先去从这种用户或者是用户用户行为实体中去查查到他的这种这种行为实体然后呢通过行为实体呢咱们再去干嘛呢咱们再去查询他的热点文章就可以了好吧那这个代表咱们之前是写过的我可以咱们咱们在这直接考过来就走了啊
[08:22] 没有多少东西我把这个熟悉的版本去拷过来就这个东西看到了吧首先去判断用户然后是拿到当前的设备ID是吧拿到设备ID好往下看这个没有是吧没有的话咱们就先去注入进来这个是行为实体的MAPprivate然后是有一个叫做什么来着叫AP叫什么来着hyper是吧hyper entry Mapper就它好了注入进来之后你看这个就没错了
[08:59] 有没有问题没问题啊行那这个加上之后呢这个intraday啊那你还不能保证它一定有值不能保证啊那这时候应该怎么办呢该怎么办呢其实呢咱们就可以干嘛呢就可以去再去判断一下多做判断一下你看这里边其实做了一个判断如果说呀文章没查到我查询全局的这文章那全局的这文章是啥呢就咱们之前做
[09:28] 这点我们这样的时候呢其实给这块去设置的时候默认设置的是什么默认设置的是一个0默认设置是0看到了吗当前的entryID是0啊这时候呢他0就是啥呢就是默认的啊所以说你在这在这去加一个东西啊if如果说entryID啊还是等于等于呢这时候怎么办呢这时候呢你就可以去把它呢重新复加值它就等于谁呀0
[09:59] 当然它不等于那的话那就根据当前的行为尸体去查询就可以了好吧那行那咱们下面就来去查询的话用app-article-myper.有一个叫做load-article-identry-id这个其实咱们需要去穿这三数第一个就是当前的entry-id第二个就是dto第三个是type好那这样的话咱们就能去获取到当前的一个什么
[10:29] 这个list的话其实就是热点文章数据热点文章数据你不能保证它一定有值是吧不能保证嘛好在这去加默认热文章你查找好在这就可以去判断一下list.mp我说它呢是不为空那这时候呢咱们就可以通过它去查找文章数据
[11:08] 不说他未空呢要fc啊那就可以去用下边的方法哎要用下边的方法啊那这个方法的话咱们直接累积就可以了好吧首先呢传第一个呢是dto然后第二个呢是type好那这样的话咱们就说完了啊重点呢咱们还是去写那一段啊既然不为空的话你首先呢你得去干嘛呢你得先去循环他啊去循环他啊
[11:41] 那循环的方式呢咱们可以这样啊咱们可以这么写list里边呢是有一个int然后呢怎么办呢又是叫article listarticle啊v r t i c l e好吧就等于那前的list.stream点什么呢有一个叫做map我们可以去找值什么呢找里边的p.get有一个叫做article id
[12:15] 然后咱们可以最终的是让他干嘛呢让他去match好像写的有问题是吧我看看这么写不用加这个括号写错了这个咱们可以删了就这么写就可以了然后把它给放到这放的是点有一个to一个叫做collect是吧可以拿这样就可以了意思就是从这里边去找当前的RGBD并且是装到了当前的集合中OK有这个集合之后你就可以干嘛呢
[12:47] 你就可以去查询了从哪查呢从当前的AP article myper中咱们其实刚刚定义了一个这种什么方法其实就是最后一个叫VR你就是把当前那个article id 例子装进去它返回的就是文章的那边好吧这时候呢你就可以直接去把它给返回就可以好吧回tun当前的AP article 4OK那这样的话咱们就
[13:16] 那这个整个的Service咱们已经写完了咱们一会儿咱们就来去写control然后咱们再去测试好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 服务中实现文章分页加载功能，包括根据用户偏好、热门文章和默认文章三种情况获取数据，并处理分页和类型校验。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 代码位置：`AppArticleServiceImpl.java`，方法 `loadV2()`。
- 代码内容：
```java
type = ArticleConstants.LOADTYPE_LOAD_MORE;
//获取用户的信息
ApUser user = ApUserLocalUtils.getUser();
//是否是首页 是首页，从缓存中获取数据 不是首页，从数据库中获取数据
if(firstPage) {
    List<Article> cacheList = getCachedArticleV2(dto);
    if(cacheList.size() > 0) {
        log.info("使用缓存加载数据tag: {}", dto.getTag());
        return ResponseResult.okResult(cacheList);
    }
}
return null;
```

画面 2：
- 代码位置：`AppArticleServiceImpl.java`，方法 `loadV2()`。
- 代码内容：
```java
// 弹出自动补全建议
```

画面 3：
- 代码位置：`AppArticleServiceImpl.java`，方法 `loadV2()`。
- 代码内容：
```java
// 弹出自动补全建议
```

画面 4：
- 代码位置：`AppArticleServiceImpl.java`，方法 `loadV2()`。
- 代码内容：
```java
if(user != null) {
    List<Article> userArticleList = getUserArticleV2(user, dto, type);
    return ResponseResult.okResult(userArticleList);
} else {
    List<Article> defaultArticleList = getDefaultArticleV2(dto, type);
    return ResponseResult.okResult(defaultArticleList);
}
```

画面 5：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getDefaultArticleV2()`。
- 代码内容：
```java
private List<Article> getDefaultArticleV2(ArticleHomeDto dto, Short type) {
    // 加载默认的热文数据
    @Param dto
    @Param type
    @Return
    private List<Article> getDefaultArticleV2(ArticleHomeDto dto, Short type) {
```

画面 6：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getDefaultArticleV2()`。
- 代码内容：
```java
private List<Article> getDefaultArticleV2(ArticleHomeDto dto, Short type) {
    // 加载默认的热文数据
    @Param dto
    @Param type
    @Return
    private List<Article> getDefaultArticleV2(ArticleHomeDto dto, Short type) {
```

画面 7：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getDefaultArticleV2()`。
- 代码内容：
```java
private List<Article> getDefaultArticleV2(ArticleHomeDto dto, Short type) {
    List<Article> hotlist = apHotArticlesMapper.loadHotListByLocation(dto, type);
    List<Article> articleList = Lists.newArrayList();
    if(null != hotlist && !hotlist.isEmpty()) {
        for (ApHotArticles hotarticles : hotlist) {
            Article aparticle = apArticleMapper.selectById(Long.valueOf(hotarticles.getArticleId()));
            articleList.add(aparticle);
        }
    }
    return articleList;
}
```

画面 8：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getDefaultArticleV2()`。
- 代码内容：
```java
private List<Article> getDefaultArticleV2(ArticleHomeDto dto, Short type) {
    List<Article> hotlist = apHotArticlesMapper.loadHotListByLocation(dto, type);
    List<Article> articleList = Lists.newArrayList();
    if(null != hotlist && !hotlist.isEmpty()) {
        for (ApHotArticles hotarticles : hotlist) {
            Article aparticle = apArticleMapper.selectById(Long.valueOf(hotarticles.getArticleId()));
            articleList.add(aparticle);
        }
    }
    return articleList;
}
```

画面 9：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getUserArticleV2()`。
- 代码内容：
```java
private List<Article> getUserArticleV2(ApUser user, ArticleHomeDto dto, Short type) {
    // 先从用户推荐的列表中找热文章，如果没有再从大文类别表中查询数据
    @Param user
    @Param dto
    @Param type
    @Return
    private List<Article> getUserArticleV2(ApUser user, ArticleHomeDto dto, Short type) {
```

画面 10：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getUserArticleV2()`。
- 代码内容：
```java
// 对热文章列表进行排序
hotArticlesList.sort(Comparator.<ApHotArticles>comparing(ApHotArticles::getScore).reversed());
// 如果热文章数量大于1000，只取前1000条
if(hotArticlesList.size() > 1000) {
    return hotArticlesList.subList(0, 1000);
}
return hotArticlesList;
```

画面 11：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getUserArticleV2()`。
- 代码内容：
```java
private List<Article> getUserArticleV2(ApUser user, ArticleHomeDto dto, Short type) {
    // 用户行为实体
    ApBehaviorEntry apBehaviorEntry = apBehaviorEntryMapper.selectById(dto.getEntryId());
    if(apBehaviorEntry == null) {
        return Lists.newArrayList();
    }
    Integer entryId = apBehaviorEntry.getEntryId();
    if(entryId == null) {
        entryId = 0;
    }
    apHotArticlesMapper.loadArticleIdListByEntryId(entryId);
}
```

画面 12：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getUserArticleV2()`。
- 代码内容：
```java
List<Article> list = apHotArticlesMapper.loadArticleIdListByEntryId(dto.getEntryId(), dto, type);
if(!list.isEmpty()) {
    List<Integer> articleIdList = list.stream().map(Article::getArticleId).collect(Collectors.toList());
    // 过滤并排序
    List<Integer> finalList = articleIdList.stream()
        .filter(id -> id > 0)
        .sorted(Comparator.reverseOrder())
        .collect(Collectors.toList());
    // 取前1000条
    if(finalList.size() > 1000) {
        finalList = finalList.subList(0, 1000);
    }
    // 查询文章
    List<Article> articleList = apArticleMapper.selectBatchIds(finalList);
    return articleList;
} else {
    return getDefaultArticleV2(dto, type);
}
```

画面 13：
- 代码位置：`AppArticleServiceImpl.java`，方法 `getUserArticleV2()`。
- 代码内容：
```java
List<Article> list = apHotArticlesMapper.loadArticleIdListByEntryId(dto.getEntryId(), dto, type);
if(!list.isEmpty()) {
    List<Integer> articleIdList = list.stream().map(Article::getArticleId).collect(Collectors.toList());
    // 过滤并排序
    List<Integer> finalList = articleIdList.stream()
        .filter(id -> id > 0)
        .sorted(Comparator.reverseOrder())
        .collect(Collectors.toList());
    // 取前1000条
    if(finalList.size() > 1000) {
        finalList = finalList.subList(0, 1000);
    }
    // 查询文章
    List<Article> articleList = apArticleMapper.selectBatchIds(finalList);
    return articleList;
} else {
    return getDefaultArticleV2(dto, type);
}
```

画面 14：
- 代码位置：`AppArticleServiceImpl.java`，方法 `loadV2()`。
- 代码内容：
```java
if(firstPage) {
    List<Article> cacheList = getCachedArticleV2(dto);
    if(cacheList.size() > 0) {
        log.info("使用缓存加载数据tag: {}", dto.getTag());
        return ResponseResult.okResult(cacheList);
    }
}
// 分页参数处理
if(size == null || size <= 0) {
    size = 20;
}
// 设置分页大小
dto.setPageSize(size);
// 标签处理
if(StringUtils.isNotBlank(dto.getTag())) {
    dto.setTag(ArticleConstants.DEFAULT_TAG);
}
// 类型参数校验
if(type.equals(ArticleConstants.LOADTYPE_LOAD_MORE) && type.equals(ArticleConstants.LOADTYPE_LOAD_NEW)) {
    type = ArticleConstants.LOADTYPE_LOAD_MORE;
}
// 获取用户信息
ApUser user = ApUserLocalUtils.getUser();
// 是否是首页
if(firstPage) {
    // 从缓存获取数据
    List<Article> cacheList = getCachedArticleV2(dto);
    if(cacheList.size() > 0) {
        log.info("使用缓存加载数据tag: {}", dto.getTag());
        return ResponseResult.okResult(cacheList);
    }
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上述要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程

