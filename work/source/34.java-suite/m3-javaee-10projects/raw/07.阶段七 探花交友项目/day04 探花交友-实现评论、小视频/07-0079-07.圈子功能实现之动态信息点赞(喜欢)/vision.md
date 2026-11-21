# 画面线理解：07.圈子功能实现之动态信息点赞（喜欢）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\07.圈子功能实现之动态信息点赞（喜欢）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:49, 01:31, 02:41, 03:27, 04:04, 05:45, 06:39, 07:25, 08:04, 08:38, 10:01, 11:02, 11:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:52:38

1) 这一组画面整体在讲什么（一句话）：
演示一个社交应用中点赞和取消点赞功能的后端实现，包括控制器层、服务层的代码逻辑以及Redis缓存操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个JSON格式的评论数据结构，包含字段如distance、createAt、commentCount等，以及一个imageContent数组。
画面2：展示MovementsController.java中的loveComment方法，用于处理点赞请求，返回点赞数。
画面3：展示MovementsService.java中的loveComment方法，使用RedisTemplate操作Redis，记录点赞数和用户点赞状态。
画面4：展示MovementsService.java中loveComment方法的代码，用于记录用户点赞状态。
画面5：展示MovementsService.java中unLoveComment方法，用于取消点赞，减少Redis中的点赞数并删除用户点赞记录。
画面6：展示MovementsService.java中queryPublishList方法，用于查询用户动态列表，设置分页信息。
画面7：展示MovementsService.java中loveComment方法，用于保存点赞记录并获取点赞数。
画面8：展示桌面环境，弹出Navicat Premium软件窗口，背景为Genymotion虚拟机界面。
画面9：展示MovementsService.java中queryPublishList方法，调试日志显示Dubbo调用失败。
画面10：展示MovementsService.java中queryPublishList方法，调试日志显示Redis操作成功。
画面11：展示MovementsService.java中queryPublishList方法，调试日志显示查询用户动态列表。
画面12：展示MovementsService.java中queryPublishList方法，设置用户ID并查询动态列表。
画面13：展示MovementsController.java中的disLikeComment方法，用于处理取消点赞请求。
画面14：展示Typora编辑器中的课程笔记，内容为“1.2.3. 测试”，包含一个用户动态示例图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```json
{
  "id": "d0fced4c8c9d91ab6b101c2c",
  "userId": 1,
  "url": "https://img1.tianhuo.com/.../images/1.jpg",
  "username": "tianhuo",
  "gender": "man",
  "age": 30,
  "text": "今天天气不错",
  "imageContent": [
    {
      "url": "https://img1.tianhuo.com/.../images/1.jpg",
      "distance": "1.2公里",
      "createAt": "今天",
      "commentCount": 30,
      "loveCount": 0,
      "isLiked": 1
    }
  ]
}
```

画面2：
```java
@GetMapping("/{id}/love")
public ResponseEntity<Long> loveComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.loveComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面3：
```java
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + publishId;
if (!this.redisTemplate.hasKey(likeCommentKey)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(likeCommentKey, String.valueOf(likeCount));
} else {
    likeCount = this.redisTemplate.opsForValue().increment(likeCommentKey);
}
// 记录当前用户已经点赞
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + publishId;
this.redisTemplate.opsForValue().set(likeUserCommentKey, "1");
return likeCount;
```

画面4：
```java
// 保存成功，获取喜欢数
Long loveCount = 0L;
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(likeCommentKey)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    loveCount = count;
    this.redisTemplate.opsForValue().set(likeCommentKey, String.valueOf(loveCount));
} else {
    this.redisTemplate.opsForValue().increment(likeCommentKey);
}
// 记录当前用户已经点赞
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + publishId;
this.redisTemplate.opsForValue().set(likeUserCommentKey, "1");
return loveCount;
```

画面5：
```java
public Long unLoveComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.removeComment(user.getId(), publishId, commentType);
    if (!bool) {
        return null;
    }
    // redis中的喜欢数需要减少1
    String likeCommentKey = "QUANZI_COMMENT_LIKE_" + publishId;
    Long count = this.redisTemplate.opsForValue().decrement(likeCommentKey);
    // 删除该用户的标记喜欢
    String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + publishId;
    this.redisTemplate.delete(likeUserCommentKey);
    return count;
}
```

画面6：
```java
movements.setId(record.getId().toHexString());
movements.setUserId(record.getUserId());
if (userIds.contains(record.getUserId())) {
    userIds.add(record.getUserId());
}
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + movements.getId();
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + movements.getId();
String value = this.redisTemplate.opsForValue().get(likeCommentKey);
if (StringUtils.isNotEmpty(value)) {
    movements.setLikeCount(integer.valueOf(value)); //点赞数
} else {
    movements.setLikeCount(0); //点赞数
}
movements.setLoveCount(100); //TODO 喜欢数
movements.setLoveLoved(1); //TODO 是否喜欢
```

画面7：
```java
public Long loveComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.saveLoveComment(user.getId(), publishId);
    if (!bool) {
        return null;
    }
    // 保存成功，获取喜欢数
    Long loveCount = 0L;
    String likeCommentKey = "QUANZI_COMMENT_LIKE_" + publishId;
```

画面9：
```java
com.alibaba.dubbo.rpc.RpcException: Failed to invoke the method queryPublishList in the service com.tanhua.server.service.MovementsService
at com.alibaba.dubbo.rpc.cluster.support.FailoverClusterInvoker.invoke(FailoverClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.AbstractClusterInvoker.invoke(AbstractClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.FailoverClusterInvoker.invoke(FailoverClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.AbstractClusterInvoker.invoke(AbstractClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.FailoverClusterInvoker.invoke(FailoverClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.AbstractClusterInvoker.invoke(AbstractClusterInvoker.java:2)
at com.tanhua.server.service.MovementsService.queryPublishList(MovementsService.java:89)
```

画面10：
```java
// 保存成功，获取喜欢数
Long loveCount = 0L;
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(likeCommentKey)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    loveCount = count;
    this.redisTemplate.opsForValue().set(likeCommentKey, String.valueOf(loveCount));
} else {
    this.redisTemplate.opsForValue().increment(likeCommentKey);
}
// 记录当前用户已经点赞
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + publishId;
this.redisTemplate.opsForValue().set(likeUserCommentKey, "1");
return loveCount;
```

画面11：
```java
public PageResult queryPublishList(User user, Integer page, Integer pageSize) {
    PageResult pageResult = new PageResult();
    Long userId = null; // 默认好友动态
    if (user != null) {
        userId = user.getId();
    }
    PageInfo<Publish> pageInfo = this.quanZiApi.queryPublishList(userId, page, pageSize);
    pageResult.setCounts(0);
    pageResult.setPages(0);
    pageResult.setPageSize(pageSize);
    pageResult.setPage(page);
    return pageResult;
}
```

画面12：
```java
// 查询好友动态
userId = user.getId();
PageInfo<Publish> pageInfo = this.quanZiApi.queryPublishList(userId, page, pageSize);
user = UserThreadLocal.get(); // 查询完成后，依然还是需要获取到当前的登录用户
pageResult.setCounts(0);
pageResult.setPages(0);
```

画面13：
```java
