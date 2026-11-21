# 画面线理解：15_app搜索_文章搜索接口_代码完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\15_app搜索_文章搜索接口_代码完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:28, 02:38, 03:51, 04:52, 06:11, 07:38, 08:46, 10:38, 11:53, 12:54, 14:16, 15:14, 16:15, 17:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:37:38

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Jest 客户端实现文章搜索功能，包括保存记录、构建查询条件、执行搜索并处理结果。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，用于保存用户搜索记录，调用 `apUserSearchMapper.insert` 插入数据并返回响应结果。
画面2: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，添加了条件判断，如果 `fromIndex` 为 0 则返回 `getEntryId` 的响应结果。
画面3: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，添加了 `jestClient.execute` 用于构建和执行搜索条件。
画面4: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面5: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面6: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面7: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索。
画面8: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索，并处理返回的 `SearchResult`。
画面9: 展示了 `ApArticleSearchServiceImpl` 中的 `articleSearch` 方法，使用 `SearchSourceBuilder` 构建搜索条件，调用 `jestClient.execute` 执行搜索，并处理返回的 `SearchResult`。
画面10: 展示了 `ArticleSearchController` 中的 `article_search` 方法，用于调用 `aparticleSearchService.articleSearch`。
画面11: 展示了 `ArticleSearchController` 中的 `article_search` 方法，用于调用 `aparticleSearchService.articleSearch`。
画面12: 展示了 `ArticleSearchControllerTest` 中的测试代码，使用 `MockMvc` 模拟请求并验证响应。
画面13: 展示了 Kibana 的 Console 页面，显示了 Elasticsearch 的索引映射配置。
画面14: 展示了 `ArticleSearchControllerTest` 中的测试代码，使用 `MockMvc` 模拟请求并验证响应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
ApUserSearch apUserSearch = new ApUserSearch();
apUserSearch.setEntryId(entryId);
apUserSearch.setKeyword(searchWords);
apUserSearch.settStatus(1);
apUserSearch.setCreatedTime(new Date());
int insert = apUserSearchMapper.insert(apUserSearch);
return ResponseResult.okResult(insert);
```

画面2:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    jestClient.execute(
```

画面3:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    jestClient.execute(
```

画面4:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    Search search = new Search.Builder(
        searchSourceBuilder.toString()).addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    jestClient.execute(search);
    return null;
}
```

画面5:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    jestClient.execute(search);
    return null;
}
```

画面6:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    try {
        jestClient.execute(search);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面7:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    try {
        jestClient.execute(search);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面8:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSourceBuilder.toString())
        .addIndex(ESIndexConstants.ARTICLE_INDEX)
        .addType(ESIndexConstants.DEFAULT_DOC).build();
    try {
        SearchResult searchResult = jestClient.execute(search);
        List<Article> articles = searchResult.getHitsList(Article.class);
        for (Article aparticle : articles) {
            //处理结果
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```

画面9:
```java
@Override
public ResponseResult cArticleSearch(UserSearchDto dto) {
    if (dto.getFromIndex() == 0) {
        ResponseResult ret = getEntryId(dto);
        if (ret.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
            return ret;
        }
    }
    saveUserSearch(int ret.getData(), dto.getSearchWords());
    //构建查询条件  jestClient
    SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
    searchSourceBuilder.query(QueryBuilders.matchQuery("name", dto.getSearchWords()));
    searchSourceBuilder.from(dto.getFromIndex());
    searchSourceBuilder.size(dto.getPageSize());
    Search search = new Search.Builder(searchSource
