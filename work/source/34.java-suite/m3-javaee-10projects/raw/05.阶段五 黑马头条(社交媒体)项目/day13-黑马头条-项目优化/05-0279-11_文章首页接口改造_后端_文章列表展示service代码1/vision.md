# 画面线理解：11_文章首页接口改造_后端_文章列表展示service代码1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\11_文章首页接口改造_后端_文章列表展示service代码1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:55, 02:10, 03:33, 03:57, 04:17, 05:06, 06:26, 07:37, 08:24, 09:05, 09:42, 10:35, 11:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:52:38

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
