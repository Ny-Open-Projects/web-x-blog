# 11_文章首页接口改造_后端_文章列表展示service代码1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\11_文章首页接口改造_后端_文章列表展示service代码1【海量资源尽在 666java.com】.mp4
- 时长 11分36秒（音频 697s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就先从后端开始去写首先咱们这边是有一个mypro这个mypro的话其实咱们之前定义过了这个mypro咱们可以再去说一下这个就是根据当前的article id再去查询当前的什么文章的列表这个咱们是vr版本上用到了所以说咱们可以先把它给定义出来这个咱们还是去拷贝一下然后找到什么找到apt article
[00:31] RTICLE好像是没有是吧AP呢AP是有的啊然后呢在这去重新去添加一个方法这个MIPER文件没有是吧那就把它给也给拷过来这个呢就是比较简单啊这个相对来说呢是一个什么呢这就是一个根据循环是去查询对吧这里边应该是一个IN啊那这是个IN啊
[01:00] 好那这个呢咱们就说完了啊那说完之后呢咱们下面重点呢还是得先去干嘛呢先去定义当前的Service好吧并且是添加一个VR版本的Service好吧刚才说了咱们首先要去加载的是load就这个load的话呢就是要去加载文章的列表信息文章的列表信息啊好那咱们下面呢就在当前的Service再去加一个方法
[01:28] 在当前的这个Service这有一个app article Service在这咱们去重新定义一个他返回的其实还是response result然后是叫load v2那这个实际上咱们之前其实有一个方法叫load这个是咱们最早之前的那个就是第一版本的
[01:57] 这个咱们是第二版本的OK这个里边的参数一样吗差不多首先第一个咱们还是当前的这种short是当前的一个类型是吧然后第二个还是当年的article-home-dtu还是一个dtu但是咱们在这再去加一个参数叫boolean类型的什么咱们会去判断first看看它是不是首页如果是首页的话先说了
[02:27] 首页的时候呢咱们会去从缓存中去获取数据如果说不是首页的话咱们会从这种数据库中去查取数据他的思路是不太一样的好吧那行那这个咱们就说到这然后下面呢可以去说一下这是加载加载文章列表数据那这是一个然后下面呢咱们就来去写这个实现方法打开当前这个APP article Service
[02:58] 然后呢在这儿再去加一个叫什么load vv那就算是重写了啊那重写完之后呢下面呢咱们就具体写这种逻辑啊那你说该怎么去写就这个啊就是跟这个load呢是类似的啊我只能说类似啊因为呢它前边的处理的参数是都是一样的都是一样的啊所以说这时候呢你可以从之前的这种代码啊拷过来比如说从这儿
[03:32] 从这儿考到哪呢考到当前的这个我看看啊参数教验load more他他好那咱们就可以直接考到这从这啊从这直接考到这然后下面这个用户咱们也要啊也要啊然后这个用户不为难OK那咱们就考到这啊考到这好背一下方式挪到下边是之前写的代码咱们可以简单看一眼啊
[04:09] 首先这个是有一个参数的校验对吧下面是一个时间的判断这两个是都是时间一个最大一个最小然后分页咱们没有的话咱们就给一个给20是吧然后下面还有就是入书这个咱们可以给一个最大可以给个最大这两个去选一个选一个最大然后下面还有什么下面还有一个文章文章频道参数这是频道入书他没有的话咱们给一个默认
[04:38] 给个默认还有一个参数的校验这个到底是load more还是load new怎么一开始其实是load more然后最终你可以上拉或者下拉去加载不同的参数对吧那行那这是一个是吧然后下面还有什么我看看这个参数跟咱们之前是一样的一样的好这是一个用户好那到此我们就可以去获取数据了刚才咱们说了有一个
[05:07] 要重要的参数就是first page看看是否是首页是否是首页是首页怎么办呢从缓存中获取数据不是首页呢从mycircle中就是数据库中获取数据这是两个思路啊所以说咱们在这直接去判断就可以了first page如果说是first如果说是true的话它肯定会去走到里边
[05:45] 往下走这时候咱们就可以干嘛呢从缓存中去拿数据这个咱们就可以在这儿带一个cache然后是article然后是v2然后这里边的参数其实就是当前的DTODTO里边其实有一些数据咱们可以去获取然后它返回的就应该当前的是一个list
[06:19] 这个list就是articlelist应该是aparticle就它然后这个是一个叫做chche list就等于它好吧那这个方法没有是吧没有就创建一下好那这时候咱们首先你要从缓冰中去拿数据首先你得想一个事就是怎么着先去输入当前的striptease template是吧
[06:54] 好拿到这个template然后呢你就可以去获取数据咱们可以在这呢去加一个这种故事啊说啥呢查询缓存首页文章数据好那你该怎么去定义呢在这块啊咱们首先呢在这可以去打印日志啊loginfo然后是怎么着呢里边可以写下说查询缓存热文章数据然后简号bug
[07:27] 这个tag其实很重要啊然后是怎么着呢然后可以写个冒号啊这tag呢其实就是有一个cto的get tag它呢其实就是当前的频道的id频道的id啊那为什么你说频道的id那么重要呢其实呢你可以去打开咱们之前写的代码这是叫做aphot article Service mpl找到它之后呢你可以发现啊
[07:55] 这咱们在这其实是做了一个叫kitch tag to redis可以看一下最终咱们就会以当前i know id就是频道id作为t然后把数据是存到了redis中所以说你拿到这个tag之后就可以从缓存中去获取数据好吧这个咱们就可以直接去写了用redis template点有一个叫做ops
[08:25] 然后是点get,这个key是谁呢?
[08:28] key的话呢,其实首先咱们要去用一个article constants点有一个叫做out article first page然后呢,你直接加上dto.get那这个时候它返回的呢,就是一个字幕串字幕串咱们叫IT吧那个字幕串里边呢,其实它就是用什么热文章的数据呢,去阐了一下啊咱们呢,需要把它给转换回来
[08:54] 转换回来可以先去判断一下如果说呀striptease.isEmpty如果说它为空这时候呢就可以直接去return一个list还有一个叫做newRelease就这个就等于用了一个Release是一样的这只是一个谷歌的一个工具类所以说咱们在这用那个方式也是可以的如果说呢它不为空的话呢就会往下走是吧
[09:26] 这时候咱们就可以转换了用json-pass-free然后你就可以去把当前的RET装进去然后你可以去把它去转换为什么类型的AP-article-class最终它就会返回一个集合这个集合叫list好吧下面咱们就可以在这去打印日志-loginfo说查询文章搜据缓时
[10:02] 查询缓存文章热数据啊然后是加上一个顶号talk就等于等于什么呢还是当前这个东西啊然后你还可以去设立一个size然后第一个呢就是toto.gettalk然后第二个呢就是以前的list.size好那这样的话我们就说这完了啊最终的你别忘了把这个list给返回行那第一种方式啊就是
[10:35] 加载首页数据啊从缓存中去获取咱们这个就说完了啊那最终呢你可以在这啊去加一个东西啊那怎么加呢你在这去判断一下啊你看你也可以去啊这么着怎么着呢说是 cache.size是大于0的时候啊这时候呢就可以直接去written啊到个info咱们可以去先说一句话啊说使用缓存加载数据然后是简号tag
[11:08] 首先是啥咱们在这去写一个dto.get套装然后你就可以去retrace path without还有一个ok without然后你就可以把当前的hlist装进去OK那这样的话我们第一步就算是做完了这只是第一步刚才说了因为这个是首页那不是首页的时候其实这个逻辑咱们还得去往下继续写

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
改造文章首页接口，实现根据标签从缓存中获取热门文章数据，并处理分页、类型、用户信息等逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“2.1 需求分析”，说明要添加文章接口，首页优先从缓存获取数据，app端图片优先从缓存中读取。
画面2：展示 `ApArticleMapper.xml` 文件，其中定义了 `loadArticleListByIdListV2` 查询语句，用于根据文章ID列表查询文章详情。
画面3：展示 `ApArticleService.java` 文件，定义了 `loadArticle` 方法，用于加载文章数据。
画面4：展示 `ApArticleServiceImpl.java` 文件，开始编写 `loadArticle` 方法的实现，包括参数校验和默认值设置。
画面5：展示 `ApArticleServiceImpl.java` 文件，实现根据用户登录状态决定加载推荐文章或默认文章的逻辑。
画面6：展示 `ApArticleServiceImpl.java` 文件，处理分页参数和标签参数的校验。
画面7：展示 `ApArticleServiceImpl.java` 文件，处理文章类型参数，区分加载更多和加载新文章。
画面8：展示 `ApArticleServiceImpl.java` 文件，使用 `ArticleConstants` 类的常量，如 `LOADTYPE_LOAD_MORE` 和 `LOADTYPE_LOAD_NEW`。
画面9：展示 `ApArticleServiceImpl.java` 文件，使用 `ArticleHomeDto` 类的 `getTag` 方法获取标签。
画面10：展示 `ApArticleServiceImpl.java` 文件，定义 `redisTemplate.opsForValue().get(...)` 方法用于从Redis缓存中获取数据。
画面11：展示 `ApArticleServiceImpl.java` 文件，使用 `StringUtils` 工具类的 `isNotEmpty` 方法判断标签是否为空。
画面12：展示 `ApArticleServiceImpl.java` 文件，使用 `JSON.parseArray` 方法将JSON字符串解析为 `List<Article>` 对象。
画面13：展示 `ApArticleServiceImpl.java` 文件，完成 `getCacheArticleV2` 方法，返回从缓存中获取的文章列表。
画面14：展示 `ApArticleServiceImpl.java` 文件，使用 `ResponseResult.okResult(...)` 方法返回成功结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```markdown
2.1 需求分析
添加文章接口，首页优先从缓存获取数据，app端图片优先从缓存中读取
```

画面2：
```xml
<!-- 以及文章id列表获取文章详情V2 -->
<select id="loadArticleListByIdListV2" resultMap="resultMap">
    select * from ap_article where id in
    <foreach item="item" collection="list" separator=",">
        #{item}
    </foreach>
</select>
```

画面3：
```java
// type 1 加载更多 2 加载最新
@Param("type")
@Param("dto")
@Return
ResponseResult loadArticle(@Param("dto") ArticleHomeDto dto, @Param("type") Integer type);
```

画面4：
```java
@Override
public ResponseResult load(ArticleHomeDto dto, Short type) {
    //参数校验
    if(dto == null) {
        dto = new ArticleHomeDto();
    }
    //时间校验
    if(dto.getBehotTime() == null) {
        dto.setBehotTime(new Date());
    }
    if(dto.getWinHotTime() == null) {
        dto.setWinHotTime(new Date());
    }
    //分页参数校验
    Integer size = dto.getSize();
    if(size == null || size < 0) {
        size = 20;
    }
    size = Math.min(size, MAX_PAGE_SIZE);
    dto.setSize(size);
    //文章类型参数校验
    if(StringUtils.isEmpty(dto.getTag())) {
        dto.setTag(ArticleConstants.DEFAULT_TAG);
    }
    //类型参数校验
    if(type.equals(ArticleConstants.LOADTYPE_LOAD_MORE) && type.equals(ArticleConstants.LOADTYPE_LOAD_NEW)) {
        type = ArticleConstants.LOADTYPE_LOAD_MORE;
    }
    //获取用户的信息
    ApUser user = ApUserLocalUtils.getUser();
```

画面5：
```java
    //判断用户是否登录
    if(user == null) {
        return ResponseResult.okDefaultArticleList();
    } else {
        //不显示，加载默认的文章
        List<Article> articles = getDefaultArticle(dto.type);
    }
```

画面6：
```java
    //分页参数校验
    Integer size = dto.getSize();
    if(size == null || size < 0) {
        size = 20;
    }
    size = Math.min(size, MAX_PAGE_SIZE);
    dto.setSize(size);
    //文章类型参数校验
    if(StringUtils.isEmpty(dto.getTag())) {
        dto.setTag(ArticleConstants.DEFAULT_TAG);
    }
    //类型参数校验
    if(type.equals(ArticleConstants.LOADTYPE_LOAD_MORE) && type.equals(ArticleConstants.LOADTYPE_LOAD_NEW)) {
        type = ArticleConstants.LOADTYPE_LOAD_MORE;
    }
```

画面7：
```java
    //类型参数校验
    if(type.equals(ArticleConstants.LOADTYPE_LOAD_MORE) && type.equals(ArticleConstants.LOADTYPE_LOAD_NEW)) {
        type = ArticleConstants.LOADTYPE_LOAD_MORE;
    }
```

画面8：
```java
    if(type.equals(ArticleConstants.LOADTYPE_LOAD_MORE) && type.equals(ArticleConstants.LOADTYPE_LOAD_NEW)) {
        type = ArticleConstants.LOADTYPE_LOAD_MORE;
    }
```

画面9：
```java
    if(firstPage) {
        List<Article> cacheList = getCacheArticleV2(dto);
        return null;
    }
```

画面10：
```java
    private StringRedisTemplate redisTemplate;
    //查询缓存中的文章数据
    private List<Article> getCacheArticleV2(ArticleHomeDto dto) {
        Log.info("查询缓存中热门文章数据tag:{}", dto.getTag());
        redisTemplate.opsForValue().get(...)
    }
```

画面11：
```java
    if(StringUtils.isEmpty(dto.getTag())) {
        dto.setTag(ArticleConstants.DEFAULT_TAG);
    }
```

画面12：
```java
    List<Article> list = JSON.parseArray(ret, ApArticle.class);
```

画面13：
```java
    private List<Article> getCacheArticleV2(ArticleHomeDto dto) {
        Log.info("查询缓存中热门文章数据tag:{}", dto.getTag());
        String ret = redisTemplate.opsForValue().get(ArticleConstants.HOT_ARTICLE_FIRST_PAGE + dto.getTag());
        if(StringUtils.isEmpty(ret)) {
            return Lists.newArrayList();
        }
        List<Article> list = JSON.parseArray(ret, ApArticle.class);
        Log.info("查询缓存中热门文章数据tag:{}", dto.getTag());
        return list;
    }
```

画面14：
```java
    if(cacheList.size() > 0) {
        log.info("使用缓存加载文章");
        return ResponseResult.okResult(cacheList);
    }
    return null;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

