# 08.圈子功能实现之动态信息评论（查询单条动态信息）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\08.圈子功能实现之动态信息评论（查询单条动态信息）_【海量资源尽在 666java.com】.mp4
- 时长 11分27秒（音频 687s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们的查询单条动态啊这个是干嘛用的呢那么我们来回到我们的这个APP我们来看一下那么这个是我们的Mock的这个数据啊然后呢我们现在是不是已经实现了我们这个好友动态的一个展现以及呢我们的这个点赞和这个喜欢这两个操作那么接下来呢我们将要实现的是这个评论的一个功能那么评论这个功能呢我们需要点进去点这个
[00:29] 评论那么才可以去实现的这样的一个功能那么这个可能会网络有点问题这样就OK了然后呢这个呢其实点击评论呢首先会打开我们这个单条这个动态的一个这个详情这个详情大概有这么多些内容然后呢在这个下面呢再去做一些
[00:50] 这个评论那么当我们去打开这个单条动态的时候呢主要有两个查询那么一个呢是查询我们的这个动态信息那么下面呢还有就是另外一个呢就是查询我们评论的一个列表所以说我们要提供这两个这个接口那么才能够去完成这个打开这个单条动态啊那我们来看一下我们的这个接口那么一个呢是我的这个叫做什么呢就是叫做
[01:19] 单条动态啊再有一个刷新一下那么这里呢会有一个叫做单条动态然后呢下面呢还有一个叫做评论列表那么有了这两个接口之后呢才能够去实现我们这样的一个效果啊所以接下来呢我们就分别呢来实现这两个这个接口那么首先第一个呢是单条动态那么我们先来做这个然后呢我们接下来呢就需要在我们的这个
[01:50] 就是Ctrl中的我们去定义一个我们的一个这个接口那么我们来看一下这个接口的一个格式那么它就是一个Moments然后后面跟一个ID就可以了然后下面就返回我们这个就是Moments的这个结构就对象就可以了好嘞接下来我们就来编写这个代码首先定义public返回值
[02:15] response.add.t呢就是这个moments然后写个query这个moments然后呢有个by什么呢id对吧好那么我们接下来呢这个也是一个get请求那么它呢也需要有一个占位服务就是我们的publish id那么我们把这个呢就拿过来这个呢就是占位服务获取到这个id
[02:43] 然后呢这个里面怎么样去实现呢那么我们这个逻辑呢跟上面这个也差不多啊那我们就先去调用这个Movins这个Service然后呢点一个什么呢就是query它by id然后呢我们把这个publish id呢传递过来那么它呢将会返回一个Movins这样的一个对象啊等于它好那么然后呢我们就然后呢我们就
[03:12] 然后我们就在哪呢下面这个位置是不是需要做一个判断如果空不等于这个movins的话那么就代表着我们是不是查询到了那我们就return一个response.ok然后把这个movins丢进来那么如果是说给它去还是去做一个try catch的一个包裹吧那么如果出异常的话那最后响应的还是这个500这样的一个错误
[03:41] 好那么我们来加一个主事这个呢就是怎么呢我们去查询单条单条我们的动态信息好嘞好那么接下来呢我们就来实现这个方法然后呢我们去实现这个方法好那么这个方法呢我们来看一下那么通过public ID呢去做一个
[04:08] 这个查询啊去做一个查询那么这个应该怎么去做查询呢我们是通过我们的这个圈子的这个API那么是不是可以去做一个这个查询啊但是呢我们在之前的这个API中是不是并没有去并没有去实现啊这样的一个方法所以说呢我们还是需要在我们Double的这个服务中啊先去提供这样的一个方法那么才能够去使用对吧
[04:36] 好那我们先来编写啊double的这样的一个接口那么下面我们就啊返回值呢那就写这个呢写这个就是我们的publist啊publist然后写个query啊然后呢publist by什么呢id呃by by这个id那么通过id呢去做一个查询那么哎这样来写那么这个呢就是呃根据什么呢
[05:04] 根据ID去做查询那么要注意的是那么我们这个根据ID去做查询那么就最终返回的是我们这个publish这样的一个对象好那么我们接下来呢我们就来实现这个所定义的这个接口那么在这个Service这个工程中呢我们去做一个具体的一个实现那么就是在下面这个位置那么去做一个具体的一个实现在这那么我们去实现一个它然后呢去
[05:34] 然后在这我们就直接去调用类似点这个mongo-template.这个叫fender-by-id那么id我们就给它new一个objector-id然后把这个publish-id传递过去那么第一个参数是它第二个参数就是我们的publish.class这样的话就OK了比较简单的一个实现然后下面在这个Service中就是我们刚刚所写的Service直接调用
[06:03] 我刚刚所提供的一个方法那么叫做querypublishById把这个publishId传递过去那么我们将会得到一个publish对象那么有了这个对象之后我们可以去判断一下如果它等于空的话如果它等于空那我们就return当就可以了如果不等于空那么到这儿是不是我们就查询查询查询到了我们的一个动态动态数据那么接下来需要做什么做一些
[06:33] 我们数据的接下来做什么呢数据的填充填充这样的一个动作那么数据的填充呢其实在前面我们已经做过了对吧那么其实就是在我们查询这个列表中我们已经做过这种数据的填充了那么我们可以把这个方法和我们下面那个方法的一些逻辑部分去做一些这个抽取比如说像我们这一段逻辑就是可以去共用的这样的逻辑那我们就把这个
[07:02] 这一段这个方法那么就这一段吧这一段我们去去做一个抽取出来抽取出来一个方法那么我们就定一个方法吧定一个方法定一个什么呢叫私有定一个私有的一个方法那么word比如说我们叫for填充这个value对吧填充这个valueto谁呢to我们这个moments
[07:31] E-N-T-S好,那么我们去做这样的一个填充那么这个会有点问题E-N-T-S好,那么我们来看一下这个里面需要怎么去做填充那么我们去来看一下首先第一个是它需要这个records那么我们来定一下比如说我们这个就是一个就是它了那我们往这一丢这是一个那么还需要谁呢还需要的是我们这个user还需要的是这个user
[08:01] 那么我们来看一下这个useruser的话我们就直接可以去获取那就是user然后呢user等于等于谁呢user谁的local.get做一个获取好这样的话就能够获取到user这个问题是不是解决了然后呢其实我们在最后我们重点呢要是返回谁的是不是返回这个mowenslist因为我们做了一个填充对吧returnreturn
[08:32] return一个return一个他那么当然呢我们可以看到呢我们现在所定义的方法呢是一个word返回空对吧那我们定义一个他就ok了然后呢我们在这个位置是不是就需要去做这个操作了对吧race.for去做一个填充那么传递一个recode4然后呢他呢就会返回一个这个集合那么我们直接这样来调用吧直接丢到这这样的话是不是就ok了
[09:01] 好嘞好那么接下来我们来看一下我们单条评论啊这个怎么去玩呢那我们同样的也是希望去调用这个方法那么他呢需要一个集合呢我们就给他去设置一个集合吧revis.aslist那我们就把这个publist给他传递过去然后呢他呢将会就得到一个我们这个moments的一个list那其实我们肯定只有一个对吧因为你传入的是不是只有一条这个数据啊
[09:30] 对吧那我们直接就return谁呢return这个movin at list.get0这样的话就OK了那么这个是不是就实现了我们的这个单条动态的这个查询啊OK好那么接下来呢我们就把一些相关的服务呢就跑起来好先把这个double这个服务跑起来然后呢我看一下啊正在启动了对吧然后呢接下来呢我们再把我们这个server这个服务跑起来我们接下来做一个测试啊
[09:59] 好那么现在我们这个服务呢都已经跑起来了然后呢我们就通过这个接口呢去做一个测试那么传递我们Publist的ID然后呢设置我们的这个token然后呢去做一个Send的发送那么就可以看到这样的一个结果那么就完成了我们这个一个数据的一条就是我们单条这个动态的一个查询那么我们接下来看一下我们的奖励那么我们定义一个
[10:27] double的一个接口然后呢接口的实现然后呢定义我们的这种服务的接口然后呢去服务的实现当然了我们讲义中的这个分装逻辑啊跟我们刚刚写的呢有一点点小的区别那么就在于它是单个去做一个分装而我们呢刚刚呢是直接把这个整体的分装这个逻辑呢全部都抽取到这样的一个方法中了
[10:53] 那么跟我们上面的查询我们的列表呢去共用这一套逻辑那么这个其实是一样的没有本质的一个区别那么大家可以根据这个讲义或者说我刚刚所写的一个代码来或者说你如果有其他的写法也都可以的只要能够实现相同的一些这种效果就可以了然后呢下面的这个就是一些这个测试了那么测试呢我们是不是也测试这个结果是不是也能够拿到我们这样的一个数据了OK好那么关于这个单条
[11:23] 动态信息的一个查询呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现一个社交应用中“动态”功能的后端服务，包括定义 Dubbo 接口、实现接口、服务接口定义以及相关业务逻辑代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档，内容为“1.3. 查询单条动态”章节，其中包含“1.3.1. 定义 dubbo接口”和“1.3.2. dubbo接口实现”部分，代码片段为：
```java
// 根据id查询
@Param id
@Return
```
和
```java
@Override
public publish queryPublishById(String id) {
    return this.mongoTemplate.findBysId(new ObjectId(id), Publish.class);
}
```
画面 2: 显示一个空白的网页，页面中央有加载动画，URL 为 https://mock.boxuegu.com/project/164/interface/api/67249。

画面 3: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsController.java，光标位于 @GetMapping 注解处，代码片段为：
```java
@GetMapping("/id/unlove")
public ResponseEntity<Long> unloveComment(@PathVariable("id") String publishId) {
    try {
        NullPointerExce...
    } catch (Exception e) {
        return ResponseEntity.badRequest().body(0L);
    }
}
```
画面 4: 显示 IntelliJ IDEA 编辑器，光标位于 if (nt) 语句处，代码片段为：
```java
if (nt) {
    // 代码被模糊处理
}
```
画面 5: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于 public 语句处，代码片段为：
```java
public PageResult queryPublishList(User user, Integer page, Integer pageSize) {
    return this.queryPublishList(user, page, pageSize);
}
```
画面 6: 显示 IntelliJ IDEA 编辑器，打开文件 QuanzApi.java，光标位于方法定义处，代码片段为：
```java
Long queryCommentCount(String publishId, Integer type);
// 根据id查询
@Param publishId
@Return
Publish queryPublishById(String publishId);
```
画面 7: 显示 IntelliJ IDEA 编辑器，打开文件 QuanzApiImpl.java，光标位于方法实现处，代码片段为：
```java
@Override
public Long queryCommentCount(String publishId, Integer type) {
    Criteria criteria = Criteria.where("publishId").is(new ObjectId(publishId))
            .and("commentType").is(type);
    Query query = Query.query(criteria);
    return this.mongoTemplate.count(query, Comment.class);
}

@Override
public Publish queryPublishById(String publishId) {
    return this.mongoTemplate.findById(new ObjectId(publishId), Publish.class);
}
```
画面 8: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER" + user.getId() + movements.getId();
String value = this.redisTemplate.opsForValue().get(likeUserCommentKey);
if (value != null) {
    movements.setHasLiked(1);
} else {
    movements.setHasLiked(0);
}
```
画面 9: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
pageResult.setCounts(0);
pageResult.setPage(0);
pageResult.setPage(page);
List<Publish> records = pageInfo.getRecords();
if (CollectionUtils.isEmpty(records)) {
    return pageResult;
}
pageResult.setItems(movementList);
return pageResult;
```
画面 10: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
private void fillValueToMovements(List<Publish> records) {
    User user = UserThreadLocal.get();
    List<Movements> movementsList = new ArrayList<>();
    List<Long> userIds = new ArrayList<>();
    for (Publish record : records) {
        Movements movements = new Movements();
        movements.setId(record.getId().toHexString());
        movements.setUserId(record.getUserId());
        if (userIds.contains(record.getUserId())) {
            continue;
        }
        userIds.add(record.getUserId());
        movements.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0);
        movementsList.add(movements);
    }
    return movementsList;
}
```
画面 11: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
if (CollectionUtils.isEmpty(records)) {
    return pageResult;
}
pageResult.setItems(this.fillValueToMovements(records));
return pageResult;
```
画面 12: 显示 IntelliJ IDEA 编辑器，打开文件 MovementsService.java，光标位于代码片段处，代码片段为：
```java
public Movements queryMovementById(String publishId) {
    Publish publish = this.quanzApi.queryPublishById(publishId);
    if (null == publish) {
        return null;
    }
    // 查询到动态数据，数据的请求
    List<Movements> movementsList = this.fillValueToMovements(Arrays.asList(publish));
    return movementsList.get(0);
}
```
画面 13: 显示 Typora 文档，内容为“1.3.2. dubbo接口实现”和“1.3.3. 定义服务接口”部分，代码片段为：
```java
@Override
public publish queryPublishById(String id) {
    return this.mongoTemplate.findBysId(new ObjectId(id), Publish.class);
}
```
和
```java
@GetMapping("/id")
public ResponseEntity<Movements> queryById(@PathVariable("id") String publishId) {
    Movements movements = this.movementsService.queryById(publishId);
    if (movements == null) {
        return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(movements);
}
```
画面 14: 显示 Typora 文档，内容为“1.3.2. dubbo接口实现”和“1.3.3. 定义服务接口”部分，代码片段为：
```java
@GetMapping("/id")
public ResponseEntity<Movements> queryById(@PathVariable("id") String publishId) {
    Movements movements = this.movementsService.queryById(publishId);
    if (movements == null) {
        return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(movements);
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文第 2 点中完整列出所有代码片段）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

