# 画面线理解：12_文章首页接口改造_后端_文章列表展示service代码2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\12_文章首页接口改造_后端_文章列表展示service代码2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:58, 02:56, 04:05, 04:38, 06:03, 06:46, 07:24, 08:44, 09:35, 10:22, 11:27, 12:33, 13:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:53:31

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
