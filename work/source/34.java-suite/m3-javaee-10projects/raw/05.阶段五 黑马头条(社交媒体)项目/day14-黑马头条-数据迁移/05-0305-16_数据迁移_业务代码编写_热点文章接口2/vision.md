# 画面线理解：16_数据迁移_业务代码编写_热点文章接口2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\16_数据迁移_业务代码编写_热点文章接口2【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:02, 03:03, 04:15, 05:48, 09:00, 10:00, 11:19, 13:05, 15:08, 16:24, 17:25, 18:41, 20:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:10:02

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
