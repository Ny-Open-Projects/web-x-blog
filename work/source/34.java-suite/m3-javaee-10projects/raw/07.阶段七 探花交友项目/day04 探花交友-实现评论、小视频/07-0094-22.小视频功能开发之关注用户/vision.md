# 画面线理解：22.小视频功能开发之关注用户

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\22.小视频功能开发之关注用户_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:09, 01:57, 02:17, 02:57, 03:13, 03:39, 04:05, 05:01, 05:37, 06:11, 06:31, 07:11, 07:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:02:38

1) 这一组画面整体在讲什么（一句话）：
实现视频平台中“用户关注”功能的前后端代码逻辑与接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“8.4.1. 定义dubbo服务”章节，内容为视频点赞接口的注解和方法定义。
画面2：在 IntelliJ IDEA 中展示 VideoService.java 文件，代码实现视频评论数统计与点赞状态更新逻辑，使用了 Redis 的 hash 和 set 操作。
画面3：在 IntelliJ IDEA 中展示项目结构，选中了 pojo 包下的 FollowUser 类，该类用于定义关注用户的数据结构。
画面4：在 Typora 文档中展示 VideoApiImpl.java 文件，包含关注用户和取消关注的接口实现代码。
画面5：在 Typora 文档中展示 VideoController.java 文件，包含保存用户关注的接口定义。
画面6：在 Advanced Rest Client 中展示“评论点赞”接口的文档，包含请求路径和参数说明。
画面7：在 IntelliJ IDEA 中展示 VideoController.java 文件，代码实现保存用户关注的逻辑。
画面8：在 Typora 文档中展示 VideoService.java 文件，代码实现关注用户的核心逻辑，包括获取当前用户、设置 Redis 关注状态。
画面9：在 Advanced Rest Client 中展示“视频用户关注”接口的文档，包含请求路径和参数说明。
画面10：在 IntelliJ IDEA 中展示 Debug 控制台，显示服务启动日志，包括 Tomcat 启动和 Dubbo 服务调用失败的异常信息。
画面11：在 IntelliJ IDEA 中展示 VideoController.java 文件，代码中存在“Not found method 'followUser' in class com.tanhua.dubbo.server.api.VideoApiImpl”的编译错误。
画面12：在 Advanced Rest Client 中展示“视频用户关注”接口的请求与响应，状态码为 200，响应内容为空。
画面13：在 Robo 3T 中展示数据库操作，执行了“db.getCollection('follow_user').find({})”查询，返回结果为空。
画面14：展示视频平台的前端界面，包含用户头像、关注按钮、视频列表等元素。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@PostMapping("/comments/{id}/dislike")
@ApiOperation("取消点赞")
public ResponseEntity<Long> disCommentsLikeComment(@PathVariable("id") String publishId) {
    return this.movementsController.disLikeComment(publishId);
}
```

画面2：
```java
long commentCount = this.quanZiApi.queryCommentCount(videoVo.getId(), type: 2);
videoVo.setHasComment(commentCount == null ? 0 : commentCount.intValue()); // 评论数
videoVo.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0); // 是否点赞
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER" + videoVo.getUserId();
String value = this.redisTemplate.opsForSet().get(likeUserCommentKey);
if (StringUtils.isNotEmpty(value)) {
    videoVo.setLikeCount(Integer.valueOf(value)); // 点赞数
} else {
    videoVo.setLikeCount(0); // 点赞数
}
if (!userId.contains(record.getUserId())) {
    userIds.add(record.getUserId());
}
videoVoList.add(videoVo);
```

画面3：
```java
package com.tanhua.dubbo.server.pojo;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;
import java.io.Serializable;

public class FollowUser implements Serializable {
    private static final long serialVersionUID = 31490190724050L;
    private Object id; // 主键id
    private Long userId; // 用户id
    private Long followUserId; // 关注的用户id
    private Long created; // 关注时间
}
```

画面4：
```java
@Override
public Boolean followUser(Long userId, Long followUserId) {
    FollowUser followUser = new FollowUser();
    followUser.setId(ObjectId.get());
    followUser.setUserId(userId);
    followUser.setFollowUserId(followUserId);
    followUser.setCreatedAt(System.currentTimeMillis());
    this.mongoTemplate.save(followUser);
    return true;
}

@Override
public Boolean disFollowUser(Long userId, Long followUserId) {
    Query query = Query.query(Criteria.where("userId").is(userId).and("followUserId").is(followUserId));
    DeleteResult deleteResult = this.mongoTemplate.remove(query, FollowUser.class);
    return deleteResult.getDeletedCount() > 0;
}
```

画面5：
```java
@PostMapping("/id/userFocus")
public ResponseEntity<Void> saveUserFocusComments(@PathVariable("id") Long userId) {
    try {
        Boolean bool = this.videoService.followUser(userId);
        if (bool) {
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面7：
```java
@PostMapping("/id/userFocus")
public ResponseEntity<Void> saveUserFocusComments(@PathVariable("id") Long userId) {
    try {
        Boolean bool = this.videoService.followUser(userId);
        if (bool) {
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面8：
```java
// 关注用户
@ApiOperation("关注用户")
public Boolean followUser(Long userId) {
    User user = UserThreadLocal.get();
    this.videoApi.followUser(user.getId(), userId);
    return true;
}
```

画面10：
```java
INFO 2280 --- [io-18081-exec-1] o.s.web.servlet.DispatcherServlet : Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Failed to invoke the method followUser in the service com.tanhua.dubbo.server.api.VideoApiImpl] with root cause
```

画面11：
```java
@GetMapping("/page")
@ApiOperation("查询视频列表")
public ResponseEntity<PageResult> queryVideoList(@RequestParam("page") Integer page,
                                                @RequestParam("pageSize") Integer pageSize,
                                                @RequestParam("type") Integer type) {
    PageResult pageResult = this.videoService.queryVideoList(page, pageSize, type);
    return ResponseEntity.ok(pageResult);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“8.4.1. 定义dubbo服务”，内容为视频点赞接口的注解和方法定义。
画面6：表格数据包含“请求参数”和“Headers”两部分，请求参数包括“id”，Headers 包含“Content-Type: application/x-www-form-urlencoded”。
画面9：表格数据包含“请求参数”和“Headers”两部分，请求参数包括“uid”，Headers 包含“Content-Type: application/x-www-form-urlencoded”。
画面12：表格数据包含“请求参数”和“Headers”两部分，请求参数包括“Authorization”和“Content-Type: application/json”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
