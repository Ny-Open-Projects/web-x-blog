# 16.推荐系统之修改查询逻辑

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\16.推荐系统之修改查询逻辑_【海量资源尽在 666java.com】.mp4
- 时长 16分46秒（音频 1006s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续那么前面呢我们已经把我们的Spark Mlib所推荐的结果数据呢我们已经写入到了我们的Redis中那么接下来呢我们就需要去修改一下我们之前的查询逻辑然后呢我们从Redis中呢去做一个查询命中那么要注意的是呢我们如果有一些用户啊在Redis中进行查询的时候如果没有命中的话
[00:27] 那我们就需要还是走我们之前的逻辑去走我们的mongoDB去做一个查询好那么接下来我们来找到我们代码那么是在我们的server里面我们来找到我们的先找到Controller那么就是我们momentscontroller然后我们来看一下查询列表是在这个位置对吧是在这里那么查询列表是在这个位置那么我们就需要在这个位置是不是做一些
[00:55] 这样的一些处理啊对吧哎OK那么我们之前那个逻辑呢是去判断什么呢我们这个优热是否为嫩然后呢去去做一个我们这个查询那么其实呢我们这个位置需要去把它去调一下啊现在去调一下那么如果这个传入的这个优热是为嫩的话那就说明它是需要什么呢
[01:21] 去不为难是拿到它如果为难那就是需要去做一个推进了对吧那我们把这个逻辑呢我们来调一下那么如果它不等于难那么拿到它那么我们把这个逻辑啊那我们先不管这个逻辑了那我们先来写这个逻辑吧如果空等于这个U
[01:42] 如果空等于优热的话代表着我们这个是不是就是查询我们的推荐推荐动态对吧推荐动态那么如果它等于空那就是要查询这个推荐动态了那么怎么查询呢就需要通过Redis是不是去做一个命中了对吧做一个命中那么这个我们应该怎么去做一个操作那我们在上面吧我们来看一下那么这块有那么Redis template有那我们就直接去查就好了
[02:10] 那我们通过我们这个readist template然后呢我们去ops for value然后呢去做一个get操作那么给它一个key给它一个key那么定义一个这个key等于等于什么呢这个key呢要和我们前面所写的这个key呢是一样的是它好那么我们回到这个里面来
[02:36] 那么我们需要跟一个什么呢跟一个这个user id那么我们这个user是为none对吧我们肯定拿不到但是我们可以通过saylocal去获取到我们当前的这个用户那我们就直接给get id这样的话我们是不是就拿到我们当前的这个用户这个id了对吧然后呢我们去通过这个key呢去做一个查询那么它的返回值呢将返回的是一个这个value
[03:03] 然后呢下面我们是不是就需要对value做一个判断那么如果如果我们这个emptynot empty如果这个value不为空的话那就代表着我们这个
[03:17] 数据啊就是我们已经命中了这个数据了对吧命中了数据之后呢接下来呢我们就需要对他呢去做一个处理了那么这个数据我们看呃之前我们所存储的数据是按照一个逗号是不是去做一个分割呀那么也就是说我们看到将是啊这样的一个这个数据啊这样的一个数据可以看到啊这样的一个数据那我们按照逗号呢去做一个这个分割哎回到这个里面来啊
[03:44] 那我们对它去做一个逗号的一个分割好那我们来看一下怎么分割呢我们就来一个分割之后呢是一个素组那么叫pids等于什么呢叫utils.split然后呢value然后呢通过一个逗号去做一个分割那么分割完成之后啊那我们就拿到了我们的这个就是我们的一个pids了对吧
[04:13] 然后呢接下来呢我们就需要对它呢要做一个分页处理因为在这个位置还需要去做分页的对吧那我们就需要去计算一下我们的这个startindex下标是多少它呢就会等于什么呢我们这个page-1然后呢乘以page-size乘以这个page-size那么这是这是我们的这个第一个啊然后呢我们来看一下
[04:41] 那么我们还有一个叫什么的under index等于什么呢我们来看一下配置-1去乘以它那么under index呢它呢就等于什么等于我们的这个start index加上一个配置size注意要-1为什么要-1呢是我们的这个我们是从0开始的对吧所以我们需要去做一个-1这样的一个操作
[05:09] 当然了我们这个位置为了我们避免呢这个就是我们传入的这个配置过大的话我们去做一个判断啊如果这个start index如果呢它呢要是去比如说我们去它呢如果是大于那我们就小于吧小于我们的这个叫做pids
[05:32] 然后我们再继续往下走如果大于的话我们就不做处理了对吧不做处理了大家应该能够去理解好那么接下来我们来看一下这个按的index那么我们同样的这个也需要去把它判断一下如果这个按的index如果它大于等于大于等于这个pids.learns的话
[05:59] 如果它比它大的话那我们这个andindex就应该等于什么呢pids.learns-1也就是说我们要保证我们的startindex和andindex都不要超出最大的这个长度的这个范围要不然肯定我们会报错了对不对好那么接下来呢我们就可以去做一个我们的一个便利了我们需要通过一个下标去做一个便利啊
[06:28] 便利谁呢便利就是我们那个pids.learns然后呢它呢就等于不是等于0而是等于我们的startindex然后呢这样的话呢我们就可以去拿到我们需要这个数据了当然了这个小于注意啊它也我们这个位置它不应该小于的是这个它应该小于的是我们的underindex
[06:52] 那么注意要有一个等于因为我们前面已经减过一了最后要有一个等于然后我们通过定义一个我们的一个让类型的一个数组叫pidlist等于new一个arrivlist去做一个收集就写一个pidlist点按的去添加一个上面的一个pids
[07:19] 然后呢通过这个下标去获取那么这样的话我们就拿到了我们所需要的一个数据把它转成一个浪类型好那么这样的话就拿到我们所需要的一个PID这样的一个集合了那么有了这个PID集合之后啊那我们就需要通过这个PID去做一个查询那么之前呢我们都是通过我们的一个这个ID去做一个查询而现在呢我们就需要通过我们的PID去做查询所以说呢我们是还需要
[07:48] 再去拓展我们之前的一个这个就是我们这个圈子中的API中的这个方法那么可以看到以前的是不是只有一个by ID所以说我们还需要去再进行扩展一个方法那我们来看一下怎么样去扩展这个方法那么我们需要扩展的是query publish然后呢by什么呢不能叫ID叫pidids
[08:18] 然后呢我们所传入的啊注意所传入的是一个浪类型的然后呢就叫pids这样的一个类型那么把它呢改一下啊这个不叫public id了那么返回值呢显然就是一个应该写一个什么呢叫做list对吧写一个list然后呢所存储的对象呢是这个public好那么我们来去改一下这个注释啊这个就是我们根据
[08:47] 根据我们的一个PID然后批量查询我们的数据注意是不是批量查询查询出来是多个那么接下来我们又回到我们double的Service中我们需要重新的把这个方法我们来实现一下好我们来实现我们的刚刚所定义的方法
[09:11] 那么这个应该怎么去查呢它其实还是什么呢要根据什么呢要根据我们的这个MongoDB是不是去做一个查询点Fend什么的Fend我们应该是就是第一个了就它对吧好那么我们第一个参数Query设置为None第二个参数呢就是这个Publish.class然后呢我们这个Query对象那么我们来怎么样定义
[09:40] 那我们上面来找一下吧找一个他我们来可以去改一下快遇这个对象那么快遇谁呢我们通过的是在我们这个中的什么pid对不对pid来回来pid他不是ease而是什么呢应该是什么呢叫我们把后面这个就给他去掉吧叫什么呢叫硬这个操作叫pids
[10:06] 那也就是说我们执行的是一个硬操作哎他是不是缺少了一个这个括号啊那么把这个query呢传递过来这个大家能够看懂了吧那么就是说我们是通过一个这个硬操作然后呢去做一个我们的一个查询然后呢我们再次回到我们的这个Service中啊那么我们在我们的Service中呢去做一个查询那么就调用我们刚刚所写的啊这个方法那么就
[10:35] by ids我们传入pid listpid list然后呢他所拿到的其实就是一个叫做什么呢publish list然后呢我们来看一下下面逻辑啊那么下面逻辑其实我们是需要通过这个配置info来做一个这个执行的那么也就是说我们在这个位置啊我们在这个位置的去定义一个什么的配置那我们应该是这样的啊就是我们在上面这个位置吧
[11:05] 那我们来定义一个PageInfo等于这个None等于None那么PageInfo那么在这个位置我们就把它设置为什么PageInfo去New一个New一个什么PageInfo然后我们把这个PageInfo.setRecord是不是就是这个PublishList对吧这样的话我们就拿到这个集合数据了然后我们来看一下那么如果这个不等于
[11:34] 我们来看一下那么下面其实我们只要判断这个配置info是不是就可以了那么如果说我们这个配置info注意配置info如果它还是等于空的话那么这块走的是不是就是我们的默认查询逻辑对不对默认查询逻辑的话那么我们就需要把我们之前这个逻辑就丢到这个里面来那么配置info这个把前面也去掉
[12:00] 然后我们就直接去给他设置值是不是OK了好我们来看一下那么如果配置info等于none的话那么我们再判断这个user不等于none
[12:12] 那不等于那呢就把ID设置为它如果等于那呢那就还是去走到什么呢我们之前的一个默认推荐列表中啊那么这个我们是之前逻辑不受任何的影响啊那么只是说只是说在我们之前的逻辑的基础之上啊我们再来去加入了一个readist这样的命中这样的一个逻辑啊那么原有的逻辑呢是不发生任何的一个这个变化
[12:36] 那么到这里呢我们这个逻辑呢我们基本上呢就已经OK了啊好那么接下来呢我们就来测试一下那么我们就打一个断点吧我们来做一个测试啊当然了我们需要先把我们这几个服务呢都跑起来那么首先第一个呢其实就是我们的这个double这个服务我们来看一下这个它已经啊跑起来了那么我们这个呢
[12:58] 这个是我们所执行的Spark的一个这样的一个推荐啊那我们找到之前的一个double这个服务那我们把这个double服务呢启动一下然后呢这个是SSO然后呢我们来看一下debug里面那么这个command这个我们其实不需要启动了因为我们现在不涉及到这块的一个测试啊好那么这个server呢需要重启呢我们先把它停掉一会儿我们来重启一下OK好那我们等待它的一个启动
[13:25] 好那么现在我们这个服务呢都已经跑起来了那么接下来呢我们就来测试一下啊那我们访问的呢就是我们这个movins recommend然后呢传递配置呢等于1发起一个这个post请求看一下是post请求吗这个比较错啊那么recommend应该是一个get请求啊get请求好那我们去发起它然后呢我们在这个位置啊去我们去打一个断点
[13:53] 然后呢走发起这个请求来看一下请求是不是已经啊进入了好那我们就跟踪进去走然后呢跟踪进去哎是不是就直行到我们刚刚所编写这个逻辑位置了然后呢我们来看一下首先判断u的等于呢说明我们要查询的是我们的推荐呃然后呢我们这个是我们的一个key啊我们来看一下这key呢就是我们的这后面跟的id呢是1呃然后呢继续往下面走我们去通过redis呢去做一个判断
[14:22] 发现了是不是已经有数据命中了对吧可以看到这个value的数据是这样的一条这个数据然后继续往下面走如果命中那么往下面走那么去做一个分割拿到了一个数组然后我们计算它的一个start index那么start index值就是0然后我们再去判断它是否小于这个length是那走到这个里面来然后相加减一
[14:49] 那么就是9那么我们每一页拿10条数据那是不是就是0到9对吧所以这个是OK的没有问题那么继续往下面走做循环做循环拿到每一个这个数据那我们在这个位置去打一个断点走通过然后我们通过我们刚刚所扩展的这个方法去查询我们的publish的一个集合走那么等待它的一个执行
[15:13] 那么我们可以看到这个publicist list是不是已经就拿到这个相关的一些这个数据了对吧然后呢我们继续往下面走走是不是拿到了然后呢到这个位置他判断配置info是不是等于呢如果不是等于那的话就不走这个逻辑了对不对那么我们前面已经命中了嘛然后走直接走到这拿到我们这个Ure走走走走走那么下面逻辑呢跟我们之前的就一样了好我们直接就通过了
[15:40] OK好那我们来看一下这个结果那么这个结果呢是不是就是会返回这样的一些这个数据那么跟我们之前的这个结构呢是完全一样的那么也就是说我们已经在原有的这个逻辑的基础之上呢我们添加了一个推荐的一个这个数据的一个命中如果命中的话那么走对地址查询那么如果没有命中的话那我们就直接走mongo dbOK好嘞好那么这样的话呢其实就我们已经就完成了去修改我们的这个查询逻辑
[16:09] 然后呢从而也就实现了什么呢我们这个推荐的一个数据的这样的一个查询啊OK好那我们来看一下我们这个修改这个查询逻辑啊那么这个方法实现的基本是差不多的那么唯一有一点这个区别的在于什么呢就是我们讲义中的这块是通传了一个布尔值来判断是否是一个推荐那么跟我们去判断UID是否为难那其实是一样的啊其实是一样的OK
[16:37] 好那么下面呢也就基本的都一样了好嘞好那么关于我们这个修改这个查询逻辑呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

