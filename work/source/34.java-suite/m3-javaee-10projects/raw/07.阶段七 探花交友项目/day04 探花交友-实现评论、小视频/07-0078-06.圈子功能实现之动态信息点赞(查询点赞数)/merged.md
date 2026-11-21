# 06.圈子功能实现之动态信息点赞（查询点赞数）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\06.圈子功能实现之动态信息点赞（查询点赞数）_【海量资源尽在 666java.com】.mp4
- 时长 6分33秒（音频 393s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么前面呢我们已经完成了我们的点赞和取消点赞的一个逻辑那么前面呢我们的所写的to do现在就需要去实现它了那么在我们查询我们这个好友列表的时候就是这个动态信息列表的时候呢我们来看一下在这个里面呢是我们有一堆这个to do内容的对吧
[00:24] 那么我们来看一下这个涂度内容是在哪里呢在上面是吧在这个位置对吧那么我们这个喜欢数和点赞数这个我们需要给它设置一下还有这个是否点赞这两个需要去处理一下那么这样我们把它放到一起吧放到一起去把它拎到上面来我们去做一个处理好那么下面呢我们展示韩式去涂度
[00:50] 那么我们来看一下这个是否点赞啊这个怎么去去拿到这个值呢其实我们下面是不是就在这个位置啊对吧有一个这个标记对吧那我们来看一下那么怎么样去实现它呢那我们可以来定义一个它那么这个public id啊public id呢呃大家这个要注意一下这个user呢是谁呢是我们啊当前的这个就是呃当前这个用户是否对这个
[01:19] 动态信息的点赞了对吧那么这个就是我当前这个ID那么Public ID呢其实就是这个Recall的这个ID啊那我们来看一下那么就是那就拿到它吧那么拿到它或者是拿到这个什么呢就是我们这个Movins的ID啊是一样的那我们就直接拿这个Movins ID吧这样呢我们省得再去转对吧那么Get ID拿到它那么拿到这个之后呢我们就可以去设置
[01:49] 它是1还是0那么如果已经有点在那就是1那么没有呢那就是0那么我们其实只需要做一个判断就可以了对吧那我们就可以来一个this.readisttemplate是不是去包含了这个那么我们把它呢就拿过来当然我们这个名字可能起了会有点问题这个不应该叫那我应该叫什么呢like对吧like
[02:15] 那么我们就写到下面这个来那么下面这个呢也会有点问题那我们就把这个去设置一下吧那么我们这个应该叫什么呢叫like然后呢可以加一个url这样的话和上面做一个区分了那我的话是我们下面的一个喜欢了这个点赞呢都使用这个like就可以了那么我们就使用它这样的话就重复了把这个名字的我们去改一下
[02:42] 好然后呢上面我们来看一下如果它包含我们就把它设置为1如果不包含就设置为0这样的话是不是就OK了然后呢下面还有这个点站数啊点站数那么点站数这个怎么来呢那么同样的也是需要下面的这个去获取对吧那我们就拿到它吧然后呢去丢到这来然后呢这个是public id那么我就通过这个moments.getid那么拿到它然后呢
[03:11] 拿到它之后上面我们这个应该叫这个应该加一个user和用户是不是相关的那么这个写到这来然后呢它呢这个值呢我们就直接去获取了然后呢去readisttemplate.ops对吧然后opsvalue.get那么把这个likecommentkey去丢进去就可以了
[03:37] 那么这样的话呢我们是不是就搞定了对吧当然它是这个呢要求呢是一个int类型的那我们就去转一下吧好那么这样的话是不是就OK了对吧但是呢我们这样去写呢它会有一个问题就是说如果我们的这个这个readist都没有这个值的话它肯定会抛异常的对吧因为我们直接用一个去转的话那么我们最好是这样来拿一下就是拿这个value等于
[04:07] 我们去做一个判断啊这样的话就不会出现我们的异常了空子人异常了对吧呃然后呢我们去判断一下如果是trim有tils点一日啊如果是not empty那么如果这个不为空的话那我们就可以去放心的啊去做一个转化了如果为空的话那我们给它设置为0啊就ok了我把这个value就拿过来啊放这然后呢这个to do我们就去掉了已经做完了对吧那这个我们也把它去掉
[04:36] OK好然后呢我们去做一个加一个else的一个操作那么如果是如果是else的话那么就是如果为空那么就直接设置为这个0啊就可以了好那么这个关于这个点单数呢我们是不是就搞定了那么接下来呢我们来测试一下啊那么我们去然后把我们这个server呢做一个重新做一个启动啊好那我们来等待它的一个启动
[05:02] 好那么我们这个服务呢就重新启动起来了那么这样我们还是来查询一下我们的这个列表对吧moments那么去做一个查询走好那我们来等待他的一个这个知行啊他应该就能够查到这个列表数据了对吧那我们来看一下那么其实我们刚刚呢所测试的是最后一条这个数据啊最后一条数据那么会发现呢他的这个点赞数啊就是
[05:30] 就是这个like count依然是零那么因为我们刚刚是不是已经把它去做了一个取消点赞了对吧那我们来点赞一下然后呢把这个断点我们就去掉吧走然后呢点赞成功了然后呢我们再去做一次查询那么来看一下它的一个数量那么在最后一个是不是可以看到这个就是这个like这个数量就是我们这个
[05:55] like count已经变成了什么呢变成了这个1了对吧然后呢我当前这个用户是否点击过这个like呢就是点赞呢也设置为1了那么也就是说我们刚刚所修改的这个逻辑啊它已经是OK了生效了对吧没有问题了好那么这个呢其实就是我们所讲的我们这个修改什么呢修改我们这个查询的这样的一个点赞数啊
[06:19] 大了后面我们也会去修改它的一个这个喜欢数那么最后是不是就得到这样的一个测试了OK好那么关于我们这个修改这个点赞数的这样的一个逻辑呢我们先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个点赞/取消点赞功能的后端实现，包括控制器层和业务服务层的代码逻辑，以及通过 REST 客户端测试接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 MovementsController.java 中的 dislikeComment 方法，用于处理取消点赞请求，调用 movementsService.disLikeComment 方法，并处理异常。
画面 2: 展示 MovementsService.java 中的 disLikeComment 方法，通过 QuanZiApi 查询点赞数，然后使用 RedisTemplate 设置或递减点赞数。
画面 3: 展示 MovementsService.java 中的 queryPublishList 方法，用于查询发布列表，设置用户点赞、距离、评论数等属性。
画面 4: 展示 MovementsService.java 中的 queryPublishList 方法，设置点赞数和是否点赞的逻辑，使用 RedisTemplate 操作点赞数据。
画面 5: 展示 MovementsService.java 中的 queryPublishList 方法，设置点赞数和是否点赞的逻辑，使用 RedisTemplate 操作点赞数据。
画面 6: 展示 MovementsService.java 中的 queryPublishList 方法，设置点赞数和是否点赞的逻辑，使用 RedisTemplate 操作点赞数据。
画面 7: 展示 MovementsService.java 中的 queryPublishList 方法，设置点赞数和是否点赞的逻辑，使用 RedisTemplate 操作点赞数据。
画面 8: 展示 MovementsService.java 中的 queryPublishList 方法，设置点赞数和是否点赞的逻辑，使用 RedisTemplate 操作点赞数据。
画面 9: 展示 MovementsService.java 中的 queryPublishList 方法，设置点赞数和是否点赞的逻辑，使用 RedisTemplate 操作点赞数据。
画面 10: 展示 MovementsService.java 中的 queryPublishList 方法，设置点赞数和是否点赞的逻辑，使用 RedisTemplate 操作点赞数据。
画面 11: 展示 Advanced REST Client 中的点赞请求，请求体包含点赞数、评论数、距离等字段。
画面 12: 展示 Advanced REST Client 的历史请求列表，包含点赞、取消点赞、登录等接口。
画面 13: 展示 MovementsController.java 中的 likeComment 方法，用于处理点赞请求，调用 movementsService.likeComment 方法。
画面 14: 展示 Typora 中的文档，内容为点赞功能的接口定义和测试数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@GetMapping("/like/dislike")
public ResponseEntity<Long> dislikeComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.disLikeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 2:
```java
Boolean bool = this.quanZiApi.disLikeComment(user.getId(), publishId);
if (!bool) {
    return null;
}

// 保存成功，获取点赞数
Long likeCommentKey = "QUANZI_COMMENT_LIKE" + publishId;
if (this.redisTemplate.hasKey(likeCommentKey)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, type);
    this.redisTemplate.opsForValue().set(likeCommentKey, String.valueOf(count));
} else {
    likeCount = this.redisTemplate.opsForValue().increment(likeCommentKey);
}

// 记录当前用户已经点赞
String loveCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + publishId;
this.redisTemplate.opsForValue().set(loveCommentKey, "1");
return likeCount;
```

画面 3:
```java
movements.setId(record.getId().toString());
movements.setUserId(record.getUserId());
if (userIds.contains(record.getUserId())) {
    userIds.add(record.getUserId());
}

movements.setLoveCount(100); // TODO 喜欢数
movements.setDistance("1.2公里"); // TODO 距离
movements.setHasLoved(1); // TODO 是否喜欢
movements.setCommentCount(30); // TODO 评论数
movements.setCreateDate(RelativeDateFormat.format(new Date(record.getCreated())));
movements.setTextContent(record.getText());
movements.setImageContent(record.getMedias().toArray(new String[]{}));
movementsList.add(movements);
```

画面 4:
```java
String loveCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + publishId;
movements.setHasLiked(0); // TODO 是否点赞
movements.setLikeCount(80); // TODO 点赞数
```

画面 5:
```java
movements.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0); // TODO 是否点赞
movements.setLikeCount(80); // TODO 点赞数
```

画面 6:
```java
public PageResult queryRecommendPublishList(Integer page, Integer pageSize) {
    return this.queryPublishList(null, page, pageSize);
}

public PageResult queryPublishList(Integer page, Integer pageSize) {
    return this.queryPublishList(null, page, pageSize);
}

public Long likeComment(String publishId) {
    // 逻辑省略
    return null;
}
```

画面 7:
```java
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + movements.getId();
movements.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0); // TODO 是否点赞
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + movements.getId();
movements.setLikeCount(Integer.valueOf(this.redisTemplate.opsForValue().get(likeCommentKey))); // TODO 点赞数
```

画面 8:
```java
movements.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0); // TODO 是否点赞
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + movements.getId();
movements.setLikeCount(Integer.valueOf(this.redisTemplate.opsForValue().get(likeCommentKey))); // TODO 点赞数
```

画面 9:
```java
if (StringUtils.isNotEmpty(value)) {
    movements.setLikeCount(Integer.valueOf(value)); // 点赞数
} else {
    movements.setLikeCount(0); // 点赞数
}
```

画面 10:
```java
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.ZooKeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.z

