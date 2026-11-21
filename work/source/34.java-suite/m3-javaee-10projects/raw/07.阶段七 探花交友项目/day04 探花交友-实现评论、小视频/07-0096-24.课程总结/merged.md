# 24.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\24.课程总结_【海量资源尽在 666java.com】.mp4
- 时长 3分13秒（音频 194s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢我们做一个总结那么今天呢我们主要呢是实现了我们圈子中的一些交互的一些操作比如说点赞呢喜欢呢这样的一些操作啊还有评论然后呢还有就是我们的一些小视频的一些这种功能那么包括我们搭建了小视频的一些所需要的这个fastDFS的环境然后呢以及呢小视频的一些功能的实现点赞呢还有一些加载列表
[00:29] 然后呢去关注啊然后呢评论呢啊等等一些这样的一些功能啊好那么下面我们来看一下那么这个评论呢我们是主要呢是针对于那么我们的这个圈子中的一些动态呢去做一些评论那么我们把这个点赞和喜欢以及评论呢都理解为是一个评论那么这样的话呢我们在设计我们表结构的时候是不是就可以统一的把它设计起来啊对吧OK
[00:57] 好那么下面我们来首先这个是实现了什么我们点赞啊然后呢下面我们又实现了这个喜欢这个操作然后呢还有查询我们的单条动态的信息然后呢还有我们是单条动态信息的一些这个评论啊然后呢我们呃是不是就基本上就已经完成了我们圈子的一些这个功能那么实现完我们这个圈子功能之后啊那么我们将去实现我们的小视频这个功能
[01:25] 那这个呢就非常类似于我们的一些这个抖音呢或者是快手啊这样的一些小视频的一些平台那么我们大致的功能呢是可以看到是这样的就可以把它展现出来啊然后呢去查看详情然后呢可以做一些关注呢还是评论呢点赞了这样一些相关的一些这种操作啊那么我们针对于小视频的这个功能呢我们做了一些分析那么主要是针对于它的技术方案的分析主要是三个
[01:53] 一个是存储还有推荐还有就是我们的加载速度这三个这个方面然后我们存储采用的是FastDFS去做一个存储所以我们去搭建了一个FastDFS这样的一个环境然后我们还去学习了它的一些client的一些使用然后我们就去实现我们小视频的一些功能包括有发布小视频然后还有是我们查看小视频的一个列表
[02:20] 然后我们可以对小视频的做点赞那么需要注意的是我们这个视频的点赞跟我们前面的圈子中的一些动态的信息的点赞的逻辑是一样的所以我们采用了同一套的实现来做一个实现然后我们针对于小视频的去做一些评论那么也是和前面一样圈子中的一些评论逻辑也是一样的所以也是可以使用同一套的逻辑去做一个实现
[02:49] 那么最后呢是我们还做了一个这个关注啊就是我们可以关注这个用户然后呢呃关注用户之后呢主要是针对于我们后面去做推荐的时候呢可以去加大他的一些这个权重啊哎OK好那么这个就是小视频的一些功能啊那么今天呢我们主要呢就实现了这两个功能哎OK好那么关于今天的一个课程的一个总结呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解小视频功能的实现，包括评论、点赞、视频存储与分发等模块的技术方案与代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 课程说明：点 赞、喜欢功能；圈子实现评论、点赞；小视频功能说明；FastDFS环境搭建；小视频的功能实现。
- 当前章节：1.1.1. 定义dubbo接口。
- 代码：package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Publish;
import com.tanhua.dubbo.server.vo.PageInfo;
public interface QuanziApi {
    //发布动态
    @Param publish
    @Return
    boolean savePublish(Publish publish);

画面2：
- 代码：package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Publish;
import com.tanhua.dubbo.server.vo.PageInfo;
public interface QuanziApi {
    //发布动态
    @Param publish
    @Return
    boolean savePublish(Publish publish);
    //查询动态列表
    PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize);
    //点赞
    @Param userId
    @Param publishId
    @Return
    boolean saveLikeComment(Long userId, String publishId);
    //取消点赞、喜欢等
    @Param userId
    @Param publishId
    @Return
    boolean removeComment(Long userId, String publishId, Integer commentType);
    //喜欢
    @Param userId
    @Param publishId
    @Return
    boolean saveLikeComment(Long userId, String publishId);

画面3：
- 当前章节：1.2. 喜欢。
- 代码：package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.pojo.Publish;
import com.tanhua.dubbo.server.vo.PageInfo;
public interface QuanziApi {
    //发布动态
    @Param publish
    @Return
    boolean savePublish(Publish publish);
    //查询动态列表
    PageInfo<Publish> queryPublishList(Long userId, Integer page, Integer pageSize);
    //点赞
    @Param userId
    @Param publishId
    @Return
    boolean saveLikeComment(Long userId, String publishId);
    //取消点赞、喜欢等
    @Param userId
    @Param publishId
    @Return
    boolean removeComment(Long userId, String publishId, Integer commentType);
    //喜欢
    @Param userId
    @Param publishId
    @Return
    boolean saveLikeComment(Long userId, String publishId);

画面4：
- 当前章节：1.4. 单条动态评论。
- 代码：package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.vo.PageInfo;
public interface QuanziApi {
    //查询评论列表
    PageInfo<Comment> queryCommentList(String publishId, Integer page, Integer pageSize);
    //点赞
    @Param userId
    @Param publishId
    @Return
    boolean saveLikeComment(Long userId, String publishId);
    //取消点赞、喜欢等
    @Param userId
    @Param publishId
    @Return
    boolean removeComment(Long userId, String publishId, Integer commentType);
    //喜欢
    @Param userId
    @Param publishId
    @Return
    boolean saveLikeComment(Long userId, String publishId);

画面5：
- 当前章节：2. 小视频功能说明。
- 内容：小视频功能类似于抖音、快手小视频的应用，用户可以上传视频进行分享，也可以浏览查看别人分享的视频，并且可以对视频评论和点赞操作。
- 效果：展示小视频应用界面截图。

画面6：
- 内容：展示小视频应用界面截图，包含多个视频缩略图和“发布”按钮。
- 底部：查看详情：展示视频播放界面。

画面7：
- 内容：展示视频播放界面，包含视频画面、用户头像、点赞数、评论数等信息。
- 视频画面：森林溪流场景。

画面8：
- 当前章节：3. 技术方案。
- 内容：对于小视频的功能的开发，核心点就是：存储 + 推荐 + 加载速度。
- 存储：小视频的存储量以及容量都是非常巨大的，所以我们选择自己搭建分布式存储系统 FastDFS 进行存储。
- 推荐：我们将采用多种权重的计算方式进行计算。
- 加载速度：除了提升服务器带宽外可以通过CDN的方式进行加速，当然了这需要额外购买CDN服务。

画面9：
- 当前章节：4.1. 搭建服务。
- 代码：#拉取镜像
Docker pull delron/fastdfs
#搭建tracker容器
Docker run -d --network=host --name tracker -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker
#搭建storage容器
Docker run -d --network=host --name storage -e TRACKER_SERVER=192.168.31.81:22122 delron/fastdfs storage

画面10：
- 当前章节：4.2. java client。
- 代码：#导入依赖
<dependency>
    <groupId>com.github.tobato</groupId>
    <artifactId>fastdfs-client</artifactId>
    <version>1.26.7</version>
    <exclusions>
        <exclusion>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
        </exclusion>
    </exclusions>
</dependency>
#4.2.1. application.properties
#分布式文件系统FDFS配置
fdfs.so-timeout = 1501
fdfs.connect-timeout = 601
fdfs.thumb-image.width = 150
fdfs.thumb-image.height = 150
#tracker-list参数，实现多个
fdfs.tracker-list=192.168.31.81:22122

画面11：
- 当前章节：5. 发布小视频。
- 代码：import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.List;
@Data
@org.springframework.data.mongodb.core.mapping.Document(collection = "video")
public class Video implements java.io.Serializable {
    private static final long serialVersionUID = 313673283684933873L;
    private ObjectId id; //主键id
    private Long userId; //用户id
    private String title; //标题
    private String picUrl; //封面图片地址
    private String videoUrl; //视频地址
    private Long created; //创建时间
    private Integer seatType; //谁可以看，1-公开，2-私密，3-部分可见，4-不活性者
    private List<Long> sealList; //可访问的用户
    private String longitude; //经度
    private String latitude; //纬度
    private String locationName; //位置名称

画面12：
- 当前章节：7. 视频点赞。
- 内容：点 赞逻辑与之前的圈子点赞一样，所以实现也是一样的。
- Mock地址：https://mock.boxuegu.com/project/164/interface/api/77987
- 接口描述：/smallVideo/id/dlike
- Mock地址：https://mock.boxuegu.com/mock/164/smallVideo/id/dlike
- 请求参数：id（视频id）；Headers：Content-Type application/x-www-form-urlencoded（必填）。

画面13：
- 当前章节：8.2. 发布评论。
- Mock地址：https://mock.boxuegu.com/project/164/interface/api/72919
- 代码：@RequestMapping("/video/comments")
public ResponseEntity<PageResult> queryCommentsList(@PathVariable("id") String videoId,
    @RequestParam(value = "page", defaultValue = "1") Integer page,
    @RequestParam(value = "pagesize", defaultValue = "10") Integer pagesize) {
    return this.commentsController.queryCommentsList(videoId, page, pagesize);
}

画面14：
- 当前章节：8.2. 发布评论。
- 代码：@RequestMapping("/video/comments")
public ResponseEntity<PageResult> queryCommentsList(@PathVariable("id") String videoId,
    @RequestParam(value = "page", defaultValue = "1") Integer page,
    @RequestParam(value = "pagesize", defaultValue = "10") Integer pagesize) {
    return this.commentsController.queryCommentsList(videoId, page, pagesize);
}
@PostMapping("/video/comments")
public ResponseEntity<Void> saveComments(@RequestBody Map<String, String> param,
    @PathVariable("id") String videoId) {
    param.put("movementId", videoId);
    return this.commentsController.saveComments(param);
}

