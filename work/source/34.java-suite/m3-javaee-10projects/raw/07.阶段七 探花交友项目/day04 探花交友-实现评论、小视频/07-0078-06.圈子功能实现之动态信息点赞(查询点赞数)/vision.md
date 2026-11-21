# 画面线理解：06.圈子功能实现之动态信息点赞（查询点赞数）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\06.圈子功能实现之动态信息点赞（查询点赞数）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:21, 00:46, 01:14, 02:01, 02:42, 03:20, 03:47, 04:21, 05:03, 05:23, 05:45, 06:07, 06:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:51:45

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
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.zookeeper.ZooKeeper
INFO 10232 --- [clientConnector] org.apache.z
