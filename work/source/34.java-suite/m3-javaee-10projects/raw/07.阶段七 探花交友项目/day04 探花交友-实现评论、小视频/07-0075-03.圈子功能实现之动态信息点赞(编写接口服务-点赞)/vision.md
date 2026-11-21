# 画面线理解：03.圈子功能实现之动态信息点赞（编写接口服务-点赞）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\03.圈子功能实现之动态信息点赞（编写接口服务-点赞）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:39, 01:22, 02:40, 03:25, 04:05, 04:43, 06:54, 07:32, 08:14, 09:01, 09:41, 10:36, 11:54, 12:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:49:31

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现点赞功能，包括定义接口、编写控制器、服务层逻辑以及与 Redis 和第三方 API 的交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了接口文档页面，接口路径为 GET /movement/{id}/like，请求头包含 Content-Type: application/json 和 Authorization: Bearer <token>。
画面 2: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，其中定义了 @Param 注解的 page 和 pageSize 参数，以及 @GetMapping("/like") 方法的开始部分。
画面 3: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，正在编写 @GetMapping("/like") 方法，参数为 @PathVariable("id") String publishId。
画面 4: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，@GetMapping("/like") 方法已定义为返回 ResponseEntity<Long>，并开始编写业务逻辑。
画面 5: 在 IntelliJ IDEA 中，显示了 MovementsController.java 文件，@GetMapping("/like") 方法中添加了 try-catch 块，用于处理异常并返回 ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build()。
画面 6: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 likeComment 方法，其中调用了 quanZiApi.saveLikeComment。
画面 7: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，定义了 @Reference 注解的 quanZiApi、@Autowired 注解的 picUploadService 和 userInfoService。
画面 8: 在 Typora 编辑器中，显示了 day04 评论.md 文件，其中包含点赞功能的伪代码和注释，如“保存点赞到 redis”、“获取点赞数”等。
画面 9: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 redisTemplate 的相关代码，用于操作 Redis。
画面 10: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 Redis 操作逻辑，包括判断 key 是否存在并设置值。
画面 11: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 Redis 操作逻辑，包括判断 key 是否存在并设置值。
画面 12: 在 IntelliJ IDEA 中，显示了 MovementsService.java 文件，正在编写 Redis 操作逻辑，包括判断 key 是否存在并设置值。
画面 13: 在 Typora 编辑器中，显示了 day04 评论.md 文件，其中包含点赞功能的伪代码和注释，如“保存点赞到 redis”、“获取点赞数”等。
画面 14: 在 Typora 编辑器中，显示了 day04 评论.md 文件，其中包含点赞功能的伪代码和注释，如“保存点赞到 redis”、“获取点赞数”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@Param page
@Param pageSize
@Return
```
画面 3:
```java
@GetMapping("/id/like")
public Long likeComment(@PathVariable("id") String publishId {
```
画面 4:
```java
@GetMapping("/id/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId {
```
画面 5:
```java
@GetMapping("/id/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId {
    try {
        Long count = this.movementsService.likeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```
画面 6:
```java
public Long likeComment(String publishId) {
    User user = UserThreadLocal.get();
    this.quanZiApi.saveLikeComment(user.getId(), publishId);
    return null;
}
```
画面 7:
```java
@Service
public class MovementsService {
    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;
    @Autowired
    private PicUploadService picUploadService;
    @Autowired
    private UserInfoService userInfoService;
    private RedisTemplate<String, String> redisTemplate;
```
画面 8:
```java
public Long likeComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.saveLikeComment(user.getId(), publishId);
    if (!bool) {
        return null;
    }
    Long likeCount = 0L;
    //保存点赞到redis
    String key = "QUANZI_COMMENT_LIKE_" + publishId;
    if (this.redisTemplate.hasKey(key)) {
        Long count = this.quanZiApi.queryCommentCount(publishId, 1);
        likeCount = count;
        this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
    } else {
        likeCount = this.redisTemplate.opsForValue().increment(key);
    }
    return null;
}
```
画面 9:
```java
private RedisTemplate<String, String> redisTemplate;
```
画面 10:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```
画面 11:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```
画面 12:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```
画面 13:
```java
public Long likeComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.saveLikeComment(user.getId(), publishId);
    if (!bool) {
        return null;
    }
    Long likeCount = 0L;
    //保存点赞到redis
    String key = "QUANZI_COMMENT_LIKE_" + publishId;
    if (this.redisTemplate.hasKey(key)) {
        Long count = this.quanZiApi.queryCommentCount(publishId, 1);
        likeCount = count;
        this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
    } else {
        likeCount = this.redisTemplate.opsForValue().increment(key);
    }
    return null;
}
```
画面 14:
```java
//保存点赞到redis
String key = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(key)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(key, String.valueOf(likeCount));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8 和 13: PPT 标题为“day04 评论.md”，内容包括“点赞功能”、“保存点赞到 redis”、“获取点赞数”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
