# 22.小视频功能开发之关注用户

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\22.小视频功能开发之关注用户_【海量资源尽在 666java.com】.mp4
- 时长 7分39秒（音频 459s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来看一下关注用户那么这个关注用户呢,在前面我们讲这个功能的时候其实我们也提到过,就是在这个位置啊它呢有一个对用户的一个关注就是这个视频的一个发布者对它做一个关注那么我们呢是对人关注啊,并不是对视频做关注所以说这个要搞清楚啊那么这个关注呢是可以在我们后期做我们推荐的时候呢可以用到这个数据的
[00:28] 关注的用户呢他肯定他的这个权重就会更重一些啊这个我相信大家都能够想通好那么接下来我们就来看一下实现这个关注啊那么之前呢我们是实现了有点赞评论但是我没有做关注关注呢就不太适合在使用我们那个comment的一张表那我们需要重新去去定一张表去做一个实现了那么下面我们来定义我们的一个double这样的一个服务
[00:54] 好 那么我们先把这个服务呢我们先定义出来那么首先呢我们需要定义我们的一个实体叫follow user那么就是一个我们的这样的一个关注啊关注这个用户或者是跟随这个用户好 那我们把这个先创建出来那我们找到这个double interface下面呢会有一个叫做podio拷贝过来那么就是有这么几个制度我们一起来看一下
[01:20] 那么首先第一个呢是用户ID啊也就是我们的这个是主件ID啊那么第二个是用户ID那第三个呢就是这个follow user ID那就是关注的用户比如说张三关注李四那么上面user ID就是张三的ID那么李四呢就是下面这个follow user的这个ID啊还有就是他的creator时间那么就是他的关注的时间那么非常简单的这样的一张表好那么接下来呢我们就来
[01:46] 定义这个接口那么我们在我们这个Value API中去定义两个接口一个就是关注用户一个就是取消关注用户那么找到它来定义这么两个这个方法然后我们再去做一个实现好那么接下来我们在我们的这个Service中去做一个具体的实现那么来看一下对吧是它我们把这两个方法那么我们就直接来拷贝也是非常简单的这两个实现
[02:15] 那么我们就把它还有下面这个就拷贝过来那么拷贝过来之后那我们就来看一下它的逻辑的一个编写那么首先第一个是关注这个用户传入两个参数一个是用户ID一个就是这个follow然后UID我们定义这样的一个对象然后设置一些相关的一些属性然后最后做一个保存这样的话就OK了
[02:38] 这是第一个那么第二个呢是取消关注那么其实就是对我们这个数据呢做一个deleteremote做这样的一个删除那么这样的话就OK了好那么这个呢我们就不去细讲了因为这个呢大家都会写相关的一些代码那么下面呢我们就来实现我们的一些这个服务了对吧那么服务呢就会进入到我们这个server这个工程好那我们来进入这个server工程在我们这个video这个里面卡托了钟啊那我们在
[03:06] 继续在下面这去编写那么同样的我们是需要去根据什么呢根据我们的这个就是Mock的API那么来找一下在这个位置有一个叫做视频用户的一个关注和这个取消关注有两个这个API那么我们就参考这个API去做一个实现所以就可以把这个Controller中的方法定义出来那么我就直接来做一个拷贝了好那么就拷贝到这个位置来
[03:34] 好那么这个呢其实就是呃关注啊这个就下面就是取消关注啊都是发起的post请求哎ok好那么传递都是什么呢我们的这个id就是user id啊注意这个user id呢是你的那个目标用户比如说我要张三关注李四那么这个传送的是李四啊这一定要搞清楚然后呢我们就需要在我们这个Service中啊再去实现啊这么两个方法那这两个方法那么我们也直接来做一个拷贝了那我们就
[04:02] 把它拷贝一下那么我们来讲解一下好这个是一个是关注一个是取消关注那我们来看一下关注就非常简单了那么拿到我当前这个用户ID然后呢我调用我的这个API中的这个方法然后呢把当前用户ID传递过去再加一个什么呢就是传入的这个UID那么我们把这个以关注的这个标记呢我们传到REDIS中做这样的一个保存然后最后return true然后取消关注呢就是
[04:32] 什么呢我们调用我的这个什么呢dcfollower然后呢user然后呢就做一个取消然后呢再把我存储到ready使用这条数据呢给它delete掉那么这样的话呢就实现了我们这个取消关注啊那么所以说还是非常简单的两个操作啊好那么接下来呢我们需要呢把我们这个double这个服务啊以及我们的这个服务呢跑起来好那么我们来等待它的一个启动
[04:59] 好,那么现在服务就跑起来了那么接下来我们就来测试一下那么首先我们先来看用户的关注这个用户视频那个用户那么我们把这个ID注意这个ID是传入了User ID那么我们就需要在这来看一下
[05:17] 那比如说我当前登录这个用户ID是100对吧那么我们就给他去传入这个1我就是这个用户去关注这个1这个用户了那么我们去发起一个post请求走那么等待他的一个执行那么现在呢是出错了是吧来看一下什么错误啊那么往上面走他呢应该是怎么呢是执行这个方法执行这个方法出错了我们来看一下这个里面有没有报错
[05:47] 他呢并没有报错啊那么可能是我们来看一下啊那么我们往后面看一下能不能看到一些这个具体的错误的一些这个内容呢他说这个找不到这个方法啊找不到这个方法那就说明什么呢说明我们这个服务是不是刚刚没有重启啊他导致这个找不到这个服务对吧找不到这个服务那我们可以来看一下啊那么在我们刚刚所写的这个
[06:15] 这个API里面我们是不是有这个方法对吧是有这个方法的没有问题那么是不是没有完成一个注册呢我们重新来启动一下测试一下好那我们这个服务呢就已经重新启动起来了那么我刚刚呢也点过这个Send发送了发现是响应的是200没有问题那么接下来呢我们就来看一下我们的这个表是不是有一个Follow User这张表那么显然会有一条数据对吧
[06:41] 那么当前这个用户ID这个是为2就当前的这个用户ID是为2他去关注于我的这个用户ID为1的这个用户那么这样的话我们就实现了用户的一个关注那么下面我们来看一下取消关注那么取消关注就是去加一个这个on focus就可以了那么之前是user focus那么加一个什么user unfocus这样的话就OK走
[07:08] 好,那么我们再来看一下这个表里面的数据就会被删除了那么这样的话呢就没有这个关注的这个用户了好,那么到这里呢其实我们这个关注是不是也就搞定了对吧,OK好,那么关于我们这个小视频评论中的这个也不是评论了就是我们在我们这个详情这个页面就是来看一下就是我们在这个位置就是在我们这个位置的这个关注呢我们就已经搞定了
[07:36] 好,那么关于它呢,我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
INFO 2280 --- [io-18081-exec-1] o.s.web.servlet.DispatcherServlet : Servlet.Service() for servlet [dispatcherServlet] in context with path [] threw exception [Failed to invoke the method followUser in the Service com.tanhua.dubbo.server.api.VideoApiImpl] with root cause
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

