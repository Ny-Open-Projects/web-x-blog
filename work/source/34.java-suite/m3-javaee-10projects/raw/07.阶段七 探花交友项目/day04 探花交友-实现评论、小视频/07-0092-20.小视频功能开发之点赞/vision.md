# 画面线理解：20.小视频功能开发之点赞

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\20.小视频功能开发之点赞_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:55, 01:17, 01:33, 02:09, 02:39, 03:32, 03:58, 04:28, 04:50, 05:30, 06:00, 06:45, 07:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:01:20

1) 这一组画面整体在讲一个视频评论点赞/踩功能的前后端实现，包括前端 REST API 调用、后端 Java 控制器与服务层代码、Redis 缓存操作以及数据库查询。

2) 按时间顺序列出每张画面的要点：
画面1：展示 REST API 返回的视频列表数据，包含分页信息、视频对象（id、userId、cover、videoUrl、likeCount、dislikeCount、commentCount）。
画面2：展示 VideoController 中的 queryVideoList 方法，用于分页查询视频列表，包含对 page 参数的校验和调用 videoService。
画面3：展示 VideoController 中的 saveVideo 方法，用于上传视频，调用 videoService.saveVideo。
画面4：展示 VideoController 中的 likeComment 和 dislikeComment 方法，用于处理视频评论的点赞和踩功能，调用 movementsController。
画面5：展示使用 Advanced REST Client 发起 POST 请求上传视频，包含 avatar_2.png 和 videoFile 两个文件字段。
画面6：展示 Robo 3T 数据库客户端，显示 video 集合中的一条文档，包含 id、userId、picUrl、videoUrl、created、userType、_class 字段。
画面7：展示 Advanced REST Client 发送 POST 请求后返回的空响应。
画面8：展示 VideoService 中的 queryVideoList 方法，创建 PageResult 对象并设置分页信息，查询视频记录并转换为 VideoVo 对象。
画面9：展示 MovementsService 中的 likeComment 方法，调用 quanziApi.saveLikeComment 保存点赞，使用 redisTemplate 查询和更新点赞数。
画面10：展示 MovementsService 中的 likeComment 方法，处理点赞逻辑，设置点赞状态和点赞数，使用 Redis 的 hash 和 opsForValue 操作。
画面11：展示 VideoService 中的 queryVideoList 方法，设置 VideoVo 的属性，包括 userId、cover、videoUrl、videoId、signature、commentCount、isFocus，以及点赞和踩的 Redis 操作。
画面12：展示 VideoService 中的 saveVideo 方法，声明了多个 @Autowired 注入的依赖，包括 videoApi、picUploadService、storageClient、fdsWebServer、userInfoService、redisTemplate。
画面13：展示 Advanced REST Client 发送 POST 请求后返回的空响应。
画面14：展示 Typora 编辑器中的 day04 评论、小视频评论相关文档，包含 VideoController 中的 likeComment 和 dislikeComment 方法的注释和代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```java
@GetMapping
public ResponseEntity<PageResult> queryVideoList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                 @RequestParam(value = "pageSize", defaultValue = "10") Integer pageSize) {
    try {
        if (page <= 0) {
            page = 1;
        }
        PageResult pageResult = this.videoService.queryVideoList(page,
                pageSize);
        if (null != pageResult) {
            return ResponseEntity.ok(pageResult);
        }
    } catch (Exception e) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面3：
```java
@RestController
@RequestMapping("smallVideos")
public class VideoController {

    @Autowired
    private VideoService videoService;

    @Autowired
    private MovementsController movementsController;

    @PostMapping("/upload")
    public ResponseEntity<Void> saveVideo(@RequestParam(value = "videoThumb") MultipartFile picFile,
                                         @RequestParam(value = "videoFile") MultipartFile videoFile) {
        try {
            Boolean bool = this.videoService.saveVideo(picFile, videoFile);
            if (bool) {
                return ResponseEntity.ok(null);
            }
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面4：
```java
@PostMapping("/({id})/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String videoId) {
    return this.movementsController.likeComment(videoId);
}

@PostMapping("/({id})/dislike")
public ResponseEntity<Long> dislikeComment(@PathVariable("id") String videoId) {
    return this.movementsController.dislikeComment(videoId);
}
```

画面8：
```java
public PageResult queryVideoList(Integer page, Integer pageSize) {
    User user = UserThreadLocal.get();
    PageResult pageResult = new PageResult();
    pageResult.setPage(page);
    pageResult.setPages(pageSize);
    pageResult.setComts(0);
    PageInfo<Video> pageInfo = this.videoApi.queryVideoList(page, pageSize);
    List<Video> videoList = new ArrayList<>();
    List<Long> userIds = new ArrayList<>();
    for (Video record : pageInfo.getRecords()) {
        VideoVo videoVo = new VideoVo();
        videoVo.setUserId(record.getUserId());
        videoVo.setCover(record.getPicUrl());
        videoVo.setVideoUrl(record.getVideoUrl());
        videoVo.setId(record.getId().toHexString());
        videoVo.setSignature("我就是我");
        videoVo.setCommentCount(10);
        videoVo.setIsFocus(0);
        String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + record.getId();
        videoVo.setLikeCount(this.redisTemplate.opsForValue().get(likeUserCommentKey));
        String dislikeUserCommentKey = "QUANZI_COMMENT_DISLIKE_USER_" + user.getId() + "_" + record.getId();
        videoVo.setDislikeCount(this.redisTemplate.opsForValue().get(dislikeUserCommentKey));
        videoList.add(videoVo);
        userIds.add(record.getUserId());
    }
    pageResult.setRecords(videoList);
    pageResult.setUserIdList(userIds);
    return pageResult;
}
```

画面9：
```java
public Long likeComment(String published) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanziApi.saveLikeComment(user.getId(), published);
    if (!bool) {
        return null;
    }
    // 保存成功，获取点赞数
    Long likeCount = 0L;
    String likeCommentKey = "QUANZI_COMMENT_LIKE_" + published;
    if (this.redisTemplate.hasKey(likeCommentKey)) {
        Long count = this.quanziApi.queryCommentCount(published, type: 1);
        likeCount = count;
        this.redisTemplate.opsForValue().set(likeCommentKey, String.valueOf(likeCount));
    } else {
        likeCount = this.redisTemplate.opsForValue().increment(likeCommentKey);
    }
    return likeCount;
}
```

画面10：
```java
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER_" + user.getId() + "_" + movements.getId();
movements.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0); // 是否点赞
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + movements.getId();
String value = this.redisTemplate.opsForValue().get(likeCommentKey);
if (StringUtils.isNotEmpty(value)) {
    movements.setLikeCount(Integer.valueOf(value)); // 点赞数
} else {
    movements.setLikeCount(0); // 点赞数
}
String loveCommentKey = "QUANZI_COMMENT_LOVE_" + movements.getId();
String loveValue = this.redisTemplate.opsForValue().get(loveCommentKey);
if (StringUtils.isNotEmpty(loveValue)) {
    movements.setLoveCount(Integer.valueOf(loveValue)); // 点赞数
} else {
    movements.setLoveCount(0); // 点赞数
}
```

画面12：
```java
@Reference(version = "1.0.0")
private VideoApi videoApi;

@Autowired
private PicUploadService picUploadService;

@Autowired
protected FastFileStorageClient storageClient;

@Autowired
private FdsWebServer fdsWebServer;

@Autowired
private UserInfoService userInfoService;

private RedisTemplate<String, String> redisTemplate;

public Boolean saveVideo(MultipartFile picFile, MultipartFile videoFile) {
    User user = UserThreadLocal.get();
    // 保存视频到本地
    String picPath = this.picUploadService.upload(picFile);
    String videoPath = this.picUploadService.upload(videoFile);
    // 保存到数据库
    Video video = new Video();
    video.setUserId(user.getId());
    video.setPicUrl(picPath);
    video.setVideoUrl(videoPath);
    video.setCreated(System.currentTimeMillis());
    video.setIsFocus(0);
    video.setLikeCount(0);
    video.setDislikeCount(0);
    video.setCommentCount(0);
    video.setIsDeleted(0);
    video.setIsPublic(1);
    video.setIsRecommend(0);
    video.setIsHot(0);
    video.setIsTop(0);
    video.setIsNew(1);
    video.setIsNewest(1);
    video.setIsNewestTime(System.currentTimeMillis());
    video.setIsNewestUser(user.getId());
    video.setIsNewestUserNickName(user.getNickName());
    video.setIsNewestUserAvatar(user.getAvatar());
    video.setIsNewestUserFollowCount(user.getFollowCount());
    video.setIsNewestUserFansCount(user.getFansCount());
    video.setIsNewestUserLikeCount(user.getLikeCount());
    video.setIsNewestUserDislikeCount(user.getDislikeCount());
    video.setIsNewestUserCommentCount(user.getCommentCount());
    video.setIsNewestUserVideo
