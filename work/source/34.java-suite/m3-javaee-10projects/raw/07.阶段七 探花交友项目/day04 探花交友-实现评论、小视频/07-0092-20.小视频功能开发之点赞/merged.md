# 20.小视频功能开发之点赞

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\20.小视频功能开发之点赞_【海量资源尽在 666java.com】.mp4
- 时长 7分42秒（音频 462s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下视频的点赞啊那么这个点赞的这个逻辑啊其实它和我们之前所做的这个圈子的这个点赞是一样的所以说它的实现呢也是一样的所以我们就不再重复这个实现了那我们就直接来使用它就OK了好那么我们下面来看一下它的一个MOOC接口的一个地址那么是在我们来找一下就是这个视频点赞啊在这一块我刷新一下
[00:29] 好那么这个呢就是视频点赞啊那么跟我们之前一样只是这个路径呢不一样所以说我们可以这么来玩一下那我们就直接把我们前面这个MovementsController直接注目进来那么就OK了好那我们来看一下啊那么这样我们先把这两个方法就是一个是点赞啊一个是取消点赞那我们来拷贝到我们的这个Video这个Controller中那么我们拷贝到这个位置来
[00:58] 好那么下面我们把这个moment啊Controller我们来注入一下我们就直接注入这个Controller就可以了momentmomentcontroller把它呢注入进来好那么好那么把它注入进来然后呢我们去使用它那么在我们之前的这个就是我们这个动态中啊它是不是已经有这个点赞啊相关的一些这个方法了那我们直接调用它就OK了
[01:26] 好那么下面呢我们就来看一下啊在这个video这个Controller中啊那么是不是也就实现了我们这个点赞了对吧那么可以看到点赞直接使用它就可以了只是说我们在传递的时候啊那么以前呢是我们传递的是一个就是我们动态的一个ID而我们现在就改成什么呢是我们视频的ID啊这样的话就可以了那这个呢是点赞啊这个就是我们的一个取消点赞好那么接下来呢我们来测试一下好那我们把这个服务呢来重新启动一下
[01:55] 好,那么现在我们这个服务呢就已经跑起来了那么接下来我们来测试一下那么首先我们来测试我们这个视频点赞那么视频点赞呢发起的是一个post请求那么我们来看一下啊它呢发起的是一个post请求那么只是我们不需要下面的两个这个文件啊那么我们呢可以看一下后面我们需要跟一个谁呢是不是跟一个我们的一个视频的ID那么视频ID呢其实就是它了把它拿过来
[02:23] 然后后面我们再去更一个什么呢这个like这个操作好那么做一个这个like操作然后做一个发起请求走好那我们来看一下它的一个效果那么它的这个数量呢就是为1啊好那么接下来呢我们来看一下我们的这个mongodb那我们找到我们这个圈子下面一个comment然后呢我们来打开最后一条数据啊
[02:47] 那么它的这个ID来看一下是不是这个CACD啊尾号是CACD那么也就是说对这个的这个动态可以把它理解为是一个动态了啊那么就是什么呢就是做一次这个comment type就是评论的类型就是11就是点赞啊这样的一个操作好那么这个点赞其实是不是就已经搞定了那么这个取消点赞就非常简单了在原有的这个like改为什么呢dislike啊就可以了
[03:17] 好走好那么这样的话呢它的这个数量就为0了那么接下来呢我们就来看一下我们这个点赞的一个这个它的一个这个就是我们那个数据啊那么可以看到在最后一条数据是不是就没有了对吧那么同我们也可以再次去做一个点赞再次去做一个点赞了那么我们来找一下啊那么就是它了然后走发起请求数量是不是就为1了那我们再来看一下
[03:46] 对吧这样的话呢就OK了没有问题好那么接下来呢我们就需要把我们之前在查询我们小视频列表中的一个这个todo是不是要去改一下了比如说呢我们下面在去哪了我们下面在这个位置啊在这个位置中呢我们其实是有一个叫做点赞数啊点赞数和一个是否点赞的这样的啊这两个字段需要我们去填充一下那么这两个怎么去填充呢其实我们可以
[04:13] 找到我们之前的这个Controller对吧那我们前面刚讲的这个Controller就是我们这个什么呢moments Controller下面呢它有一个这个点赞和取消点赞那么具体其实在这个Controller中去做一个Service做一个完成那么在下面这个就是在下面我们不是有一个叫做填充那个方法吗还记得吧就是我们有一个这个这个for value这个to moments
[04:42] 这个里面那么点赞数和这个点赞数这个处理点赞数上面这个是否点赞那我们就把这个逻辑拷贝过来就可以了他逻辑呢都是相通的这个逻辑啊那我们找到我们这个就是我们找那个Service control了啊然后呢找这个Service啊那我们来点一下吧到这那么在这个里面怎么样去做那么就把它就拷贝过来了好那么这个肯定不能不能变化对吧
[05:12] 那么我们来看一下啊那么当前用户是否有点赞了呢就是我们还是需要这个当前这个用户优惠了把这个优惠门就打开啊有了这个优惠对象然后呢我们来看一下这个moment id其实就是我们的什么呢就是我们的哎就是我们的视频的id那就是get什么呢get id啊就可以了好那么这个moment呢我们就会设置什么呢我们这个呃叫video然后呢
[05:40] 设置它是否点赞然后呢我们还缺少一个readist的一个template那我们上面呢就把这个readist的template呢就注入进来了叫做readist的一个templatereadist的一个template死去然后呢死去然后呢有一个叫readist的template好把它呢就注入进来那么注入进来之后呢就可以去使用它了那么其实我们这个是否点赞就已经搞定了
[06:08] 那么下面这个就可以把它去掉了是不是好那么下面我们来看来看这个点赞数啊那么其实也是一样直接改一下啊把这个呢就去掉这是我们的点赞数那么这个moment id我们要改成什么呢我们视频的id啊视频的id好这个逻辑是不是就ok了对吧那么这个呢是跟我们之前其实写这个逻辑呢是一样的啊那么这个stream util啊把这个就去掉吧那我们就来导入一下啊这样的话就ok了没有问题好嘞
[06:37] 好那么接下来呢我们把这个服务呢我们来重启一下那我们来测试一下好那么我们这个服务呢就重新启动起来了那么我们可以再来测试一下那么这个是点赞那么点赞之后呢肯定就不能够重复点赞了对吧所以说呢我们可以把它叫dislike好这回就OK了然后呢我们再去呃咨询一下点赞肯定是没有问题的那么下面我们再来看一下我们的查询我们的
[07:07] 这个列表那么我们去发起一个get请求那么看一下它是否能够去显示出我们的点赞数啊那么可以看到在这个位置是不是就点赞啊点赞数为1当前这个用户是否点赞了呢也是点赞了啊因为我这个是自己去上传着啊这样的一个这个视频好嘞好那么这样的话呢我们其实又完成了我们这个点赞啊以及这个取消点赞啊大家在做的过程中啊千万别忘记了把那个前面我们todo呢要
[07:36] 把它做完OK好那么关于我们视频的一个点赞我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

