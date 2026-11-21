# 07.圈子功能实现之动态信息点赞（喜欢）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\07.圈子功能实现之动态信息点赞（喜欢）_【海量资源尽在 666java.com】.mp4
- 时长 11分49秒（音频 710s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来实现这个喜欢那么其实喜欢呢和前面点赞的逻辑呢非常的类似啊非常的相像那我们来看一下这个喜欢的一个API那么只是把这个什么呢之前的like改成什么呢law然后呢取消呢也是这个叫unlaw所以说呢我们就来直接来编写吧这个也是和那个基本上是一样的那我们可以把这两个呢来拷贝一下
[00:27] 好 那么我们去做一下这个修改那么首先第一个呢是这个点赞我们改成这个喜欢喜欢然后呢这个改成什么呢love然后呢这个改成love其实我们这个逻辑都是一样的那么我们改成这个love好 然后呢这个是不是就搞定了然后呢这个改成什么呢不是diss了改成什么呢on 是吧这个叫什么呢看一下on
[00:58] 然后下面这个就改成什么叫然后把这个改成好那么这样的话我们这个是不是就OK了对吧这个叫取消喜欢好那么接下来我们就来编写这个Service把这个Service我们去来写一下那么其实这个逻辑跟我们之前的点赞的逻辑是非常的
[01:28] 这一次的好我们就直接来拷贝过来拷贝过来我们来修改一下那么首先来看一下那么这个是肯定是没有问题的然后我们这个应该调用的是sale什么的烙sale烙然后我们去如果保存如果是false的话那就保存失败了那么下面是保存成功然后获取什么不是点赞而是什么喜欢喜欢素
[01:54] 那我这个K呢要改一下那我们把这个like跟什么呢然后呢这个去做判断然后呢这个都没有问题然后呢这个也没有问题这个我们还是把名字改一下吧都改成什么呢我们都把它改成那我们都把它改一下改成这个然后呢这个我们就直接改吧那就叫什么呢叫Low
[02:23] 好,那么这个烙舞呢是到这儿啊到这儿好,那么这个在这儿这样的话就没有问题了最后返回它我们来看一下啊这块还有没有其他问题呢这个我们也要改一下是吧这个呢是改成烙舞这样的话就没有问题了吧OK好,那么这个呢是
[02:46] 这个是喜欢的这个操作那么还有下面还有一个取消喜欢的这个操作那么同样呢我们把它呢也创建出来那么取消喜欢呢跟前面的取消点赞呢也是非常的类似啊所以说就直接来做拷贝然后做一个修改就可以了那么同样呢在这个位置呢我们传递的这个type呢就要改成3啊改成3然后呢下面这个like呢我们要改成什么呢love
[03:15] 然后呢这个点赞啊改成喜欢然后呢这个是标记这个喜欢好那么上面这个是不是也没改把它改一下喜欢好那么这个搞定那这个把这个like改成什么呢好这样的话呢就都已经改完了那么这块就OK了搞定了对吧那么这块是这个名字我们刚才没改吗那么我们把它改一下好那么这样的话呢就OK了
[03:45] 这个喜欢和取消喜欢的都已经搞定了那么接下来呢我们还是需要把上面的这两个给它来处理一下就是这个漏数和这个是否是否这个喜欢是否喜欢好那么把其他的呢我们还是先丢到下面去然后呢我们就把这个逻辑吧来直接拷贝过来改一下就可以了对吧那么首先呢这个我们改成漏然后呢这个like呢我们改成漏
[04:16] 然后这个set什么呢set hash这个什么呢这个LOW好 那么这样的话就OK了把这个设置为它这个是否喜欢然后下面的这个呢这个同样的也是去把like改成LOW然后这个放到这然后这个是我们就写个LOW吧LOW valueLOW value好 那么LOW value也丢到这来
[04:48] 然后呢我们去set这个law的一个count好那么这个就是一个点赞数那么就改成喜欢然后呢这个是喜欢数好那么把这两个就去掉了来我们检查一下还有没有问题啊那么这个是喜欢没有问题这个是喜欢的数量这个是law这个呢这个有问题了那么自不改成这个law这样的话呢我们是不是基本上呢就没有问题了
[05:16] 然后呢这个K也没有问题那这个也没有问题这个没有问题没有问题哎OK好那么到这里呢我们是不是就把这两个都已经测试完了对吧好那么接下来呢我们就来实际的来测试一下那我们把我们这个服务呢重新来启动一下重新启动一下那我们接下来呢就直接整合到我们的APP吧去做一个测试那么我们先把我们的模拟器呢先打开然后呢把我们之前的一些
[05:45] 这个断点什么都去掉现在没有断点了ok好那么我们就稍微等待一下我们把我我这边把模拟器先跑起来好那么现在我们模拟器就跑起来了那么接下来我们就来测试一下我们等待它的一个打开然后我们先去修改一下我们 API 的地址然后我们去改一下就写一个 a
[06:12] 然后呢我们去拷贝一下这个我的IP地址往这一扣然后呢去粘贴一下把前面这个A呢去掉没有那个A呢是粘贴不了的然后呢我们去登录一下那么你比如说呢我还是用这个158的这个00280然后呢这个尾号我得看一下然后是别搞错了然后呢去找一下我们的数据库
[06:41] 数据库里面来找一下这个用户就是叫麦炭花这个里面用户这个是7988那么是7988然后我们获取验证码获取到了然后输入123456那么登录成功然后到这个里面去看我们这个圈子的内容
[07:07] 然后呢现在应该没有断点吧那么来查看好友的这个好友的一些这个内容那么发现是没有数据的对不对那么为什么会没有数据呢原因是我们这一块是不是在包错了那么哪里包错了呢我们来看一下那么我们这个是空指针异常刚刚去排查了一下问题呢是在这个位置就是刚刚我们在
[07:35] 修改这个代码的时候呢会有点问题就是我们使用了这个low value但是这个位置判断的时候呢并没有使用导致这个位置呢去对这个none的做这个硬头转换的时候呢就出错了所以说呢我们刚刚在修改的时候呢没有把这个修改掉然后呢我们重新来启动一下那我们再来看效果好那我们等待它的一个启动好那么现在呢我们就跑起来了那么我们再来测试一下我点击这个推荐然后再点击这个好友
[08:03] 那么还是有点问题啊那我们来看一下这个是什么错误好那么这个问题呢经过了一个排查呢会发现有个问题就是我们点击这个推荐的时候它会出现一个空指认异常那么我们点击这个好友的时候它其实是没有异常的是可以正常去加载数据的那么为什么去点击这个推荐这个位置会有异常呢原因呢是在这个位置就是我们在这呢要拿到一个User ID但是呢
[08:31] 我们这个Ura是不是已经被我们之前啊设置为这个None传入这个None了对吧那么呃之前呢我们在这个位置去判断是等于None呢我们要查询的是推荐呃然后呢呃关键我们要设置这个UID是否为None来决定我们是查询好友还是推荐呃所以说呢我们查询完成之后啊那我们还是应该去给到这个Ura一个值就是我们当前的这个用户啊
[08:57] 那么就是我只要用完这个判断之后那我就可以拿到我这个user那么其实我这个user就是我当前登录的这个用户那么我们来加一个注释说明这个一定就是我们就是什么就是在查询完成后依然还是需要去去获取到当前的当前的这个登录登录用户的这是一个小bug那么会导致这个话会有个问题
[09:26] 那么这样的话呢我肯定就没有问题了因为我们是拿到当前这个登录用户啊然后呢我们重新来启动一下再来看一下它的一个效果好那么重新启动起来之后呢我们再来去做一个测试那么我们还是点击这个好友然后我们再点击这个推荐第一次访问呢会有一点慢然后呢我们可以再来去点一下其他地方啊然后呢我们去测试一下这个推荐啊然后呢
[09:57] 这个有点慢啊稍微我们需要等待一下好那么现在呢就没有问题了刚刚呢我们在测试的时候啊呃他没有完全跑起来那么我们就去测试了那么点击没有反应啊那我们点击他好那么接下来我们点这个呃测试个点赞啊然后点击他那么哎发现呃点赞是不是已经就成功了有这样的一个效果啊那我们可以点击这个喜欢然后呢我可以再次点击就取消了把这个
[10:26] 有个断点那么把断点去掉然后呢我们再去点击它去取消了那么接下来呢我们可以我们还是来点一下吧点一下它然后点一下它然后呢下面一个这个呢我们就只点赞我们不去点这个喜欢那么下面呢我们去重新进入我们的这个APP应用我们来看一下它能不能够读取到我们
[10:55] 这个正确的这个数据啊那我们来试一下好那么我们来等待它的一个这个加载那么我们还是直接去这个主界面因为已经有登录信息了就不需要重新登录了我们点击这个圈子然后呢我们进入到这个里面可以看一下效果是不是已经出来了你看这个呢已经显示已经点赞过了下面这个呢是已经点了这个喜欢了然后下面这个呢是已经是点了我们这个喜欢OK这个是点赞啊
[11:24] 然后往下面走其他都没有好嘞好那么这样的话我们是不是就整合到我们的APP做了这样的一个测试我们也把我们喜欢是不是也就讲完了对吧包括喜欢和取消喜欢这个操作OK那么最后测试就可以整合我们的APP去测试了发现是没有问题的好嘞好那么关于我们喜欢的操作我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
com.alibaba.dubbo.rpc.RpcException: Failed to invoke the method queryPublishList in the Service com.tanhua.server.Service.MovementsService
at com.alibaba.dubbo.rpc.cluster.support.FailoverClusterInvoker.invoke(FailoverClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.AbstractClusterInvoker.invoke(AbstractClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.FailoverClusterInvoker.invoke(FailoverClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.AbstractClusterInvoker.invoke(AbstractClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.FailoverClusterInvoker.invoke(FailoverClusterInvoker.java:2)
at com.alibaba.dubbo.rpc.cluster.support.AbstractClusterInvoker.invoke(AbstractClusterInvoker.java:2)
at com.tanhua.server.Service.MovementsService.queryPublishList(MovementsService.java:89)
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

