# 画面线理解：16.推荐系统之修改查询逻辑

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\16.推荐系统之修改查询逻辑_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:34, 02:06, 03:12, 04:58, 06:53, 08:05, 09:48, 10:58, 11:55, 12:57, 14:00, 14:58, 15:42, 16:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:02:11

1) 这一组画面整体在讲如何在 Java 服务中实现基于 Redis 的用户动态推荐功能，包括推荐结果的生成、存储、查询以及与 Dubbo 服务和 MongoDB 的集成。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 SparkQuanZi.java 中的代码，用于根据用户 ID 获取推荐商品列表，并将结果存储到 Redis 的特定 key 中（"QUANZI_PUBLISH_RECOMMEND_" + userId）。
画面 2: 展示了 MovementsService.java 中的 saveMovements 方法，用于保存用户发布的动态内容，包括文本、位置信息和图片上传。
画面 3: 展示了 MovementsService.java 中的 queryPublishList 方法，用于查询用户动态列表，其中包含从 Redis 获取推荐数据的逻辑。
画面 4: 展示了 MovementsService.java 中的 queryPublishList 方法，正在输入参数 page 和 pageSize 的类型。
画面 5: 展示了 MovementsService.java 中的 queryPublishList 方法，用于处理从 Redis 获取的推荐数据，将其按分页处理。
画面 6: 展示了 QuanzApi.java 中的接口定义，包括查询评论数量、根据 ID 查询动态、查询评论列表等方法。
画面 7: 展示了 QuanzApiImpl.java 中的 queryPublishByIds 方法，用于根据 ID 列表查询动态，使用了 MongoDB 的查询条件。
画面 8: 展示了 MovementsService.java 中的 queryPublishList 方法，用于将处理后的 ID 列表传递给 QuanzApi 查询动态。
画面 9: 展示了 MovementsService.java 中的 queryPublishList 方法，用于设置 PageResult 的分页信息和处理空结果。
画面 10: 展示了 SparkQuanZi.java 中的 Spark 任务日志，显示了推荐模型的训练和查询过程。
画面 11: 展示了 MovementsService.java 中的 queryRecommendPublishList 方法，用于查询推荐列表。
画面 12: 展示了 MovementsService.java 中的 queryPublishList 方法，用于处理分页和设置 PageInfo。
画面 13: 展示了 Advanced REST Client 中的 HTTP 请求响应，返回了查询到的动态数据，包括用户信息、图片、评论等。
画面 14: 展示了 Typora 中的 day08.md 文档，记录了推荐系统中“小视频推荐”部分的实现逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
JedisCluster jediCluster = new JedisCluster(nodes);
for (Long userId : userIdList) {
    Rating[] recommendProducts = bestModel.recommendProducts(userId.intValue(), num: 20);
    List<Integer> products = new ArrayList<>();
    for (Rating product : recommendProducts) {
        products.add(product.product());
    }
    String key = "QUANZI_PUBLISH_RECOMMEND_" + userId;
    jediCluster.set(key, StringUtils.join(products, separator: ','));
}
//关闭
jediCluster.close();
jsc.close();
```

画面 2:
```java
public String saveMovements(String textContent,
                            String location,
                            String longitude,
                            String latitude,
                            MultipartFile[] multipartFile) {
    User user = UserThreadLocal.get();
    Publish publish = new Publish();
    publish.setUserId(user.getId());
    publish.setTest(textContent);
    publish.setLocationName(location);
    publish.setLatitude(latitude);
    publish.setLongitude(longitude);
    //图片上传
    List<String> imageUrls = new ArrayList<>();
    for (MultipartFile file : multipartFile) {
        PicUploadResult uploadResult = this.picUploadService.upload(file);
        imageUrls.add(uploadResult.getName());
    }
}
```

画面 3:
```java
private PageResult queryPublishList(User user, Integer page, Integer pageSize) {
    PageResult pageResult = new PageResult();
    Long userId = null; //默认查询动态
    if (null == user) {
        //查询推荐动态
        String key = "QUANZI_PUBLISH_RECOMMEND_" + UserThreadLocal.get().getId();
        String value = this.redisTemplate.opsForValue().get(key);
        if (StringUtils.isEmpty(value)) {
        }
        if (user != null) {
            userId = user.getId();
        }
    }
    PageInfo<Publish> pageInfo = null;
    user = UserThreadLocal.get(); //查询完成后，依然还是需要获取到当前的登录用户
```

画面 4:
```java
private PageResult queryPublishList(User user, Integer page, Integer pageSize) {
    PageResult pageResult = new PageResult();
    Long userId = null; //默认查询动态
    if (null == user) {
        //查询推荐动态
        String key = "QUANZI_PUBLISH_RECOMMEND_" + UserThreadLocal.get().getId();
        String value = this.redisTemplate.opsForValue().get(key);
        if (StringUtils.isEmpty(value)) {
        }
        if (user != null) {
            userId = user.getId();
        }
    }
    PageInfo<Publish> pageInfo = null;
    user = UserThreadLocal.get(); //查询完成后，依然还是需要获取到当前的登录用户
```

画面 5:
```java
if (null == user) {
    //查询推荐动态
    String key = "QUANZI_PUBLISH_RECOMMEND_" + UserThreadLocal.get().getId();
    String value = this.redisTemplate.opsForValue().get(key);
    if (StringUtils.isEmpty(value)) {
    }
    if (user != null) {
        userId = user.getId();
    }
}
PageInfo<Publish> pageInfo = null;
user = UserThreadLocal.get(); //查询完成后，依然还是需要获取到当前的登录用户
```

画面 6:
```java
Long queryCommentCount(String publishId, Integer type);

/**
 * 根据id查询
 * @param publishId
 * @return
 */
Publish queryPublishById(String publishId);

/**
 * 查询评论
 * @return
 */
PageInfo<Comment> queryCommentList(String publishId, Integer page, Integer pageSize);
```

画面 7:
```java
jInfo.setPageSize(pageSize);
jInfo.setPageNum(page);
return pageInfo;
de
List<Long> queryPublishByIds(List<Long> pids) {
    Query query = Query.query(Criteria.where("publishId").is(new ObjectId(publishId))
        .and("commentType").is(2).with(pageRequest);
    return this.mongoTemplate.find(query, null, Publish.class);
}
```

画面 8:
```java
List<Long> pidList = new ArrayList<>();
for (int i = startIndex; i <= endIndex; i++) {
    pidList.add(Long.valueOf(pids[i]));
}
List<Publish> publishList = this.quanZiApi.queryPublishByPids(pidList);
```

画面 9:
```java
if (pageInfo == null) {
    //默认查询逻辑
}
user = UserThreadLocal.get(); //查询完成后，依然还是需要获取到当前的登录用户
pageResult.setCounts(0);
pageResult.setPages(0);
pageResult.setPageSize(pageSize);
pageResult.setPage(page);
List<Publish> records = pageInfo.getRecords();
if (CollectionUtils.isEmpty(records)) {
    //没有查询到动态数据
    return pageResult;
}
```

画面 10:
```text
19/10/09 23:49:22 INFO TaskSchedulerImpl: Submitting 1 missing tasks from resultStage 1473.0 with 1 tasks
19/10/09 23:49:22 INFO TaskSetManager: Starting task 0.0 in stage 1473.0 (TID 1072), localhost, executor
19/10/09 23:49:22 INFO Executor: Running task 0.0 in stage 1473.0 (TID 1072)
19/10/09 23:49:22 INFO BlockManager: Found block rdd_2068_0 locally
19/10/09 23:49:22 INFO Executor: 1 block locks were not released by TID = 1072
[rdl_2068_0]
19/10/09 23:49:22 INFO TaskSetManager: Finished task 0.0 in stage 1473.0, whose tasks have all completed, from p
19/10/09 23:49:22 INFO DAGScheduler: ResultStage 1473 (first at MatrixFactorizationModel.scala:67) finish
19/10/09 23:49:28 INFO SparkContext: Starting job: lookup at MatrixFactorizationModel.scala:173 with 1.0
```

画面 11:
```java
public PageResult queryRecommendPublishList(Integer page, Integer pageSize) {
    return this.queryPublishList(user, page, pageSize);
}
public PageResult queryUserPublishList(Integer page, Integer pageSize) {
    return this.queryPublishList(UserThreadLocal.get(), page, pageSize);
}
public Long likeComment(String publishId) {
    User user = UserThreadLocal.get();
```

画面 1
