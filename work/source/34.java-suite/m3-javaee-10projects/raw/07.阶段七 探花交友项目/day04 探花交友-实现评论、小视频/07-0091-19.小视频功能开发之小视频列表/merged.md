# 19.小视频功能开发之小视频列表

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\19.小视频功能开发之小视频列表_【海量资源尽在 666java.com】.mp4
- 时长 9分51秒（音频 591s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来呢我们来实现我们小视频的列表的查询那么首先呢我们还是去定义我们的double的服务然后呢我们在double服务中呢去定义一个方法叫做query video list然后呢去设置两个参数一个是page一个是page size好 那么我们去把这个来拷贝一下那么我们找到我们的这个API的定义叫做video API
[00:27] 然后呢我们去写到这个位置来好那么接下来呢我们就来实现我们的这个服务在这然后呢我们去嗯它啊然后呢我们来实现一下那么又需要去实现一个方法好那么这个方法怎么样去做实现呢我们来看一下讲义啊那我们就直接就把这一段逻辑就拷贝过来了其实是比较简单逻辑啊这个我们之前一直也在写这样的一些逻辑
[00:57] 好 那么把这个query也拷贝过来那么就是我们这个mongo这个code下面这个query这样的话就可以了那么我们可以来看一下就是说那么首先我们可以看到在这个位置是我们定义了一个pageable然后设置了page,page size以及我们的排序按照一个creator做一个排序然后下面这个是我们的query对象然后我们去做一个find查询拿到之后我们就设置
[01:25] 一个这个配置info对象最后返回就可以了非常简单这样的一个实现好那么接下来呢我们把这个double这个服务呢我们来重启一下重启之后呢这个服务呢就可用了好那么接下来呢我们就来实现我们的这个就是我们的这个接口的服务啊那我们需要根据我们的这个定义啊就是我们需要来找一下就是我们需要找一下啊就是mock找到我们那个地址啊
[01:53] 好,那么我们找到它吧然后呢我们来看一下这个里面呢会有一个我们的小视频然后呢这个里面呢有一个叫做什么呢就是我们来找一下叫做视频小视频的列表那么我们可以看到这个结构呢是我们非常熟悉的一个结构啊然后呢下面这个关键是在items这个里面的这个一些这个内容啊那我们要根据这些属性之段呢我们需要的是定义我们的一个对象啊所以我们来叫做video这样的一个对象
[02:22] 好那我们把这个对象呢我们拷贝到哪里呢就拷贝到啊我们的这个server这个工程下面有一个Vue这个包啊拷到这个里面来那么拷进来之后呢我们就可以去啊使用它了好那么接下来呢我们来定义我们的Controller那么在我们的Controller中啊我们定义一个这个query video list啊这样的一个方法那我们把这个呢也就直接啊拷贝过来了好那我们来找到我们的这个video Controller好那我们来拷贝一下
[02:51] 那么显然呢它呢是需要调用我们这个Service中的啊是不是这个方法那我们把这个方法呢给它去创建出来好那么来看一下这个方法啊这个方法其实也是去使用我们刚刚的所写的API呢去做一个查询那我们来看一下它具体的一个实现啊那么这个里面内容呢还是比较多的啊那么我们啊这样我们就一点一点来去看一下吧啊那么首先呢我们呃它是需要一个配置result这个对象那么这个代码我们就直接
[03:21] 就拷贝过来了OK好那么我们定义了一个什么呢定义了一个我们的配置result最后是不是其实反复就是我们这个配置result的对象然后呢接下来呢我们就需要通过我们这个video的apm的做一个查询得到一个这个配置info这个对象先把它拷贝过来去得到它那么得到它之后呢我们需要去做一些这个事情就是说我们需要对我们的这个
[03:48] 就是我们这个查询到的一个视频的做一些这个便利然后呢我们需要去分装成我们所需要的一个video vo这样的一个对象啊然后呢再去做一些分装啊那么咱们就这么来吧把这几个拿过来啊拿过来我们就丢到这啊丢到这这个大家应该能够看到什么意思啊一个呢就是我们的这个video的list一个就是我们那个vo的list一个就是我们的user id的list
[04:15] 那么显然我们是不是就需要去查询用户的相关的一些信息对吧我们接下来就对我们的去做一个便利了recodes那么我们来看一下这个里面需要去做什么是不是每一次便利都是去拿一个v6,vu这个对象这个我们就不去一点去写了相同代码非常的简单的代码
[04:36] 然后我们去set一个这个优势ID然后还有什么就是这个是我们的一个分面对吧然后还有视频的地址然后还有ID还有就是一个签名注意签名我们这一块并没有去设计这一块所以说我们就暂时我们就加个todo吧就是todo然后这个叫签名我们就签名我们暂时就先todo
[05:02] 然后我们后面如果要是去加这一块功能的话我们就把它加进去就好了我们就加一个签名叫做我就是我OK好那么下面我们来看一下下面还有这么一堆内容是干嘛的其实我们在设置我们那些评论数那么由于我们现在评论数我们还没有去存所以说我们就暂时给它设置为比如说10这个我们也可以加一个什么to do就是我们还没做完对吧
[05:28] 然后呢这个呢是设置我们是否这个关注了这个就是发表视频的这个用户那么我们就随便吧比如说0或者1都可以比如1吧或者0也可以啊那就是这个呢也是做一个突度那么具体后面我们再做一个实现啊先做一个突度了然后呢这一块呢是设置什么呢设置我们是否进行了点赞这个操作那么同样的我们也把它设置为什么呢设置为0啊那么同样的也是哎
[05:56] 同样的也是去怎么呢把它突度一下好那么这个呢就是是否点赞呢就是默认了否啊没有点赞然后呢下面呢还有这个呢是在获取他的一个点赞的一个数量啊那我们来看一下这个呢其实也是突度突度然后呢点赞数点赞数然后点赞数设置为多少比如设置为40啊随便啊这个数字随便
[06:22] 然后我们把它加到我们这个V6list中然后加一个按进去好那么这样的话我们其实就得到了我们这个list对吧然后把它丢到哪里丢到我们的这个release点set谁呢set我们这个set我们的items把那个就是V6 list丢进去
[06:46] 那这样的话呢就就OK了对吧好那么下面呢在这一段呢其实就是我们需要去查询我们的用户信息啊然后呢我们去需要呢给他去把一些用户信息相关的一些内容呢做一个填充啊在这去做一个做一个填充这个呢我们也就不去敲了啊这个之前代码也写过好多次然后呢我们去把这个叫做什么呢叫做user info这个Service啊我们去注进来
[07:15] 那么注进了之后呢下面这个方法呢就可用了对吧通过这个诶它是什么呢这个UserInfoService然后呢有一个叫做QueryList没有这个方法吗我们来看一下啊那么这个里面呢是UserInfoList这个方法名有点不太一样那我们就来把这个方法名呢给它改一下就说QueryUserInfoList好其实是它的这个表达的意思呢是一样的这个方法名呢有点不一样
[07:45] 然后我们对它去做两层循环然后就判断ID是否相同相同的话就break然后把它的昵称和它的头像就拿到塞进来那么最后就可以去做一个return了这个是一个相对比较基础的这样的一个代码的编写当然了在这个里面我们可以来看一下这个里面我们是不是缺少一个叫UIDs然后把这个UID给它丢进去是吧我们缺少这个逻辑
[08:13] 应该是缺少这个逻辑我看一下那么在这刚刚我们就说它是应该是缺少这个逻辑的对吧好那么我们加到这个位置来就是我们去把它需要加到我们的UIDs这个里面来对吧然后大家需要做个判断如果不包含的话那么就需要加入进来了好那么这样的话我们这个集合或者说我们查询这个列表是不是也就搞定了那么这个UID我们并没有使用看一下对不对那么我们通过它去拿到那其实是
[08:43] 检查一下这个周拿到Vue list那么这个里面的ID是从哪来的呢这个里面的ID这个里面这个ID是通过recode ID来拿到的那么也就是说我们和我们当前这个user就没什么关系所以说这个我们就可以先注释掉了那么在后面我们会使用到它但是我们不能把代码删除我们先注释掉它好然后接下来我们就可以来测试一下了
[09:09] 那么把我们这个服务呢就重新啊跑起来那我们来测试一下好那我们等待它的一个启动好那么现在呢我们就重启好了那么接下来呢我们就来测试一下好那么那么我们还是去点击一下这个请求那么我们对这个地址呢去发起各的请求然后呢我们去send一下那么可以看到呢结果呢就出来了那么这个是不是就是之前我们所
[09:36] 提交的这个视频这样的一个视频好那么其实现在呢我们这个查选一次吧也就搞定了对吧OK好那么关于我们这个小视频列表的一个这个接口的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
定义并实现一个用于查询小视频列表的 Dubbo 服务，包括接口、实现类、控制器和相关数据处理逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Dubbo 服务接口 VideoApi 的定义，包含 saveVideo 和 queryVideoList 两个方法。
画面 2: 展示了 VideoApiImpl 实现类，包含 saveVideo 和 queryVideoList 方法，使用了 @Service 注解和 MongoTemplate。
画面 3: 展示了一个浏览器页面，访问的是一个视频列表的 REST API，URL 为 http://192.168.31.81:8888/group1/M00/00/02/wKgtMk/AMVLA2AALngh/7kPcC161.jpg。
画面 4: 展示了 VideoVo 数据类的定义，包含 id、userId、avatar、nickname、cover、videoUrl、signature、likeCount、hasFocus、commentCount 等字段。
画面 5: 展示了 VideoController 中的 queryVideoList 方法，使用 @GetMapping 注解，接收 page 和 pageSize 参数，并调用 videoService。
画面 6: 展示了 VideoService 中的 queryVideoList 方法，获取当前用户，初始化 PageResult，并设置分页信息。
画面 7: 展示了 VideoService 中的 queryVideoList 方法，调用 videoApi 查询视频列表，处理评论数、关注状态、点赞状态等信息。
画面 8: 展示了 VideoService 中的 queryVideoList 方法，设置视频 Vo 的评论数、关注状态、点赞状态，并添加到视频列表。
画面 9: 展示了 VideoService 中的 queryVideoList 方法，查询用户信息并设置到视频 Vo 中。
画面 10: 展示了 VideoService 中的 queryVideoList 方法，初始化 PageResult 并设置分页信息。
画面 11: 展示了 VideoService 中的 queryVideoList 方法，查询用户信息并设置到视频 Vo 中。
画面 12: 展示了 VideoService 中的 queryVideoList 方法，设置视频 Vo 的评论数、点赞数、关注状态，并处理用户 ID。
画面 13: 展示了 VideoService 中的 queryVideoList 方法，设置视频 Vo 的评论数、点赞数、关注状态，并添加到视频列表。
画面 14: 展示了测试页面，请求 URL 为 http://192.168.31.81:8888/group1/M00/00/02/wKgtMk/AMVLA2AALngh/7kPcC161.jpg，返回的 JSON 数据包含 count、pageSize、page、items 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.dubbo.server.api;

import com.tanhua.dubbo.server.pojo.video;
import com.tanhua.dubbo.server.vo.PageInfo;

public interface VideoApi {
    /**
     * 保存小视频
     * @param video
     * @return
     */
    Boolean saveVideo(Video video);

    /**
     * 分页查询小视频列表，按时间倒序排列
     * @param page
     * @param pageSize
     * @return
     */
    PageInfo<Video> queryVideoList(Integer page, Integer pageSize);
}
```

画面 2:
```java
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;

import java.util.List;

@Service(version = "1.0.0")
public class VideoApiImpl implements VideoApi {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Override
    public Boolean saveVideo(Video video) {
        if (video.getUserId() == null) {
            return false;
        }
        video.setId(ObjectId.get());
        video.setCreated(System.currentTimeMillis());
        this.mongoTemplate.save(video);
        return null;
    }

    @Override
    public PageInfo<Video> queryVideoList(Integer page, Integer pageSize) {
        Pageable pageable = PageRequest.of(page - 1, pageSize);
    }
}
```

画面 4:
```java
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class VideoVo {
    private String id; //视频ID
    private Long userId; //用户ID
    private String avatar; //头像
    private String nickname; //昵称
    private String cover; //封面
    private String videoUrl; //视频URL
    private String signature; //签名
    private Integer likeCount; //点赞数量
    private Integer hasFocus; //是否已关注（1是，0否）
    private Integer commentCount; //评论数量
}
```

画面 5:
```java
@GetMapping
public ResponseEntity<PageResult> queryVideoList(@RequestParam(value = "page", required = false, defaultValue = "1") Integer page,
                                                 @RequestParam(value = "pageSize", required = false, defaultValue = "10") Integer pageSize) {
    try {
        if (page <= 0) {
            page = 1;
        }
        PageResult pageResult = this.videoService.queryVideoList(page, pageSize);
        if (null != pageResult) {
            return ResponseEntity.ok(pageResult);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 6:
```java
public PageResult queryVideoList(Integer page, Integer pageSize) {
    User user = UserThreadLocal.get();
    PageResult pageResult = new PageResult();
    pageResult.setPage(page);
    pageResult.setPageSize(pageSize);
    pageResult.setPages(0);
    pageResult.setCounts(0);
    return null;
}
```

画面 7:
```java
User user = UserThreadLocal.get();
PageResult pageResult = new PageResult();
pageResult.setPage(page);
pageResult.setPageSize(pageSize);
pageResult.setPages(0);
pageResult.setCounts(0);

PageInfo<Video> pageInfo = this.videoApi.queryVideoList(page, pageSize);
List<Video> records = pageInfo.getRecords();
List<VideoVo> videoVoList = new ArrayList<>();
List<Long> userIds = new ArrayList<>();

for (Video record : records) {
    VideoVo videoVo = new VideoVo();
    videoVo.setUserId(record.getUserId());
    videoVo.setCover(record.getPicUrl());
    videoVo.setVideoUrl(record.getVideoUrl());
    videoVo.setId(record.getId().toHexString());
    videoVo.setSignature("我就是我-"); //TODO 签名
    videoVo.setCommentCount(10); //TODO 评论数
    videoVo.setHasFocus(0); //TODO 是否关注（1是，0否）
    videoVo.setHasLiked(0); //TODO 是否点赞（1是，0否）
    videoVo.setLikeCount(40); //TODO 点赞数
    if (userIds.contains(record.getUserId())) {
        userIds.add(record.getUserId());
    }
    videoVoList.add(videoVo);
}
```

画面 8:
```java
videoVo.setCommentCount(10); //TODO 评论数
videoVo.setHasFocus(0); //TODO 是否关注（1是，0否）
videoVo.setHasLiked(0); //TODO 是否点赞（1是，0否）
videoVo.setLikeCount(40); //TODO 点赞数
if (userIds.contains(record.getUserId())) {
    userIds.add(record.getUserId());
}
videoVoList.add(videoVo);
```

画面 9:
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper();
queryWrapper.in("user_id", userIds);
List<UserInfo> userInfos = this.userInfoService.queryUserInfoList(queryWrapper);
for (VideoVo videoVo : videoVoList) {
    for (UserInfo userInfo : userInfos) {
        if (videoVo.getUserId().longValue() == userInfo.getUserId().longValue()) {
            videoVo.setNickname(userInfo.getNickName());
            videoVo.setAvatar(userInfo.getLogo());
            break;
        }
    }
}
pageResult.setItems(videoVoList);
return pageResult;
```

画面 10:
```java
public PageResult queryVideoList(Integer page, Integer pageSize) {
    User user = UserThreadLocal.get();
    PageResult pageResult = new PageResult();
    pageResult.setPage(page);
    pageResult.setPageSize(pageSize);
    pageResult.setPages(0);
    pageResult.setCounts(0);
    return null;
}
```

画面 11:
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper();
queryWrapper.in("user_id", userIds);
List<UserInfo> userInfos = this.userInfoService.queryUserInfoList(queryWrapper);
for (VideoVo videoVo : videoVoList) {
    for (UserInfo userInfo : userInfos) {
        if (videoVo.getUserId().longValue() == userInfo.getUserId().longValue()) {
            videoVo.setNickname(userInfo.getNickName());
            videoVo.setAvatar(userInfo.getLogo());
            break;
        }
    }
}
pageResult.setItems(videoVoList);
return pageResult;
```

画面 12:
```java
String followUserKey = "VIDEO_FOLLOW_USER_" +

