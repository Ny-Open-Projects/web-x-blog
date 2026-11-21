# 21.小视频功能开发之评论

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\21.小视频功能开发之评论_【海量资源尽在 666java.com】.mp4
- 时长 8分19秒（音频 499s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下小视频的评论啊那么其实这个评论呢和我们前面这个点赞一样它和之前的圈子中的这种逻辑呢也都是一样的所以我们可以使用同一套逻辑来做啊那么我们首先来看一下评论的列表那我们就直接把这个就拷贝过来了然后呢我们来找到我们这个video Controller然后呢我们往下面去写这个方法然后呢当然这个呢我们是需要去根据我们的一些这个
[00:29] 接口服务呢去做一些这个使用啊那么我来看一下啊就是我们的一个叫做评论的一个列表评论列表那么就是这样的一些这个数据了那么结构跟我们之前也都是一样的一个结构啊OK好那么我们来看一下这个里面有没有报错呢这个comments这个Controller没有那我们就来注入一下private然后呢commentscontroller把它呢注入进来
[00:59] 这个呢也是我们之前写过的这个Controller好注入进来呢直接使用Controller中的一些这个方法啊就ok了好那么这个是评论列表然后呢还有就是什么呢发布评论也就是我们的提交这个评论好来看一下那么这个里面呢我们需要把一些相关的一些这个包呢来导入一下好那么这样的话呢就搞定了那么也是使用它啊当然在这个点需要大家注意一下就是那么在我们之前这个
[01:26] 这个保存这个comment中啊只需要去接收一个map这俩就可以了但是呢我们现在呢它呢是通过一个我们的url做一个数据的一个传递所以在这个位置需要通过这个pass variable来拿到我这个id把它丢进来才能够使用啊那么这样的话就可以去直接调用它了啊那么接下来呢我们就把这个服务呢就跑起来那我们再来测试一下好那我们来测试这个提交评论和我们的这个评论列表
[01:56] 好那么我们这个服务呢它就跑起来了接下来我们来看一下我们的这个Mock的接口那我们来看一下这个评论发布啊那么我们来看它的一个一些API一些参数那么首先呢我们来URL是这样的URL我们来拷贝一下然后呢进入到前面我们这个测试那么就那我们就这样来写吧来拷贝一下前面的它那么基本上是一样的然后呢comments然后发起的是一个
[02:23] Post这样的一个请求下面还有Comment的一个这样的一个数据那么这个数据我们是需要通过一个这个JSON去做一个传递对吧好那么我们就在这个位置去发起Post请求然后去添加一个这个JSON那么就是这个Comment然后叫什么呢比方说写个Good然后我们去提交的是一个ObligationJSON这样的一个类型
[02:51] 然后呢我们去做一个提交那么这样的话呢我们就提交成功了那么下面呢我们可以来看一下我们的数据啊那么找到我们这个comment那么第11条这个数据那么可以看到是不是有一个good啊这样的一个这个提交的一个评论类型呢是为2的这样的一个评论好那么接下来呢我们来看一下我们的查询列表
[03:16] 那么我们呢对它去发起一个get请求啊就可以了好那我们往上面走改成get请求走那么它将返回的就是我们评论的这样的一个列表了那么可以看到是不是我们已经就能够去把它查询到了并且呢就显示出来了
[03:34] OK好那么这个其实就是我们啊所讲这个评论的这个发布和这个列表那么下面呢我们把这个评论点赞呢我们一起来把它做完啊那么就是把这两个拷贝过来那么跟我们之前逻辑呢是一致的啊那就直接来使用这个Controller好那我们把它丢到呢丢到我们这个最下面来在这那么一个呢就是评论啊点赞一个就是我们评论取消点赞
[04:00] 那么其实他传递的呢也都是什么呢都是我们这个就是我们视频的这个ID啊好那么我们就直接来做一个重新启动好那么服务呢就跑起来了那么接下来呢我们来测试一下评论点赞那么我们来看一下他的一个这个地址啊那么这个地址呢我们就来拷贝一下吧就是我们去评论一下他对吧然后呢我们来看一下那么就到这儿在这个位置啊
[04:30] 然后呢我们这个ID啊那么要注意它并不是视频ID而是谁呢而是我们的这个评论ID就是说我们发表了一个评论叫good它的一个ID呢是这个值啊那我们就来拷贝一下吧就它这个呢是ID那么对它呢再去做一个评论做一个评论然后呢我们去发启示一个什么呢post请求然后呢来看一下
[04:56] 那么还有什么内容啊那么我们就去来看一下这个我们的接口下面呢会有评论啊点赞那么点赞的就没有内容了对吧那么就直接去把这个内容呢就去掉啊就可以了做一个点赞走来看一下他的一个结果的返回那么是不是又返回数量是为一了然后呢我们再去啊再去查询一下那么来看一下这个位置呢是不是就
[05:21] 可以看到那么对前面的这个是不是做了一个评价对吧他的ID是这个40要注意你看这个和前面他是不是这两个是不是相等啊然后呢他的这个就是评论类型呢就是唯一就是做了一个点赞了好嘞好那么到这里呢我们就这个功能是不是就完成了但是呢我们要注意了在我们这个前面啊查询这个列表中啊那么查询列表中呢我们还有tutu没做来看一下那么这个评论数
[05:51] 和这个是否关注啊是否关注我们一会儿再说然后呢下面我们来看一下这个评论数那么评论数呢其实我们是可以直接去做一个查询的对不对好那我们来看前面的一个这个实现啊就是我们的这个往上面走啊就是我们的一个视频一个列表那么关于这个评论数啊那我们就可以直接调用我们圈子去做一个查询了那我们就把这个就拷贝过来好那来拷贝一下然后呢我们就丢到这来
[06:20] 那么把这个圈子我们去注进来private圈子API好那么把它呢通过reface来获取到这个Wolfen1.0.0这样的一个这个版本好然后呢我们拿了它之后啊然后在下面呢就可以去做一个评论数的一个这个查询对吧把这个呢就
[06:45] 拿掉了那我们查询的这个它的type呢是为2就是我当前的这个评论数就是我这个视频的这个评论数为2的这个数量有几个那么查询到如果它等于0呢就设置为0不是的话就拿它的值OK好那么我们再来测试一下把它重启一下
[07:04] 好 那我们等待它的一个启动那我们就来测试一下服务跑起来了那测试一下什么呢就是我们去测试一下我们这个查询我们的列表因为我们刚刚呢对我们的这个视频是不是做了评论对吧它的评论数应该是唯一OK 那么这个时候是不是就对了对吧评论数呢是唯一的好 那么到这里呢我们是不是就已经完成了我们的评论的列表的查询那么以及我们这个评论的一个发布
[07:34] 以及我们评论的点赞和这个取消点赞这个我们都已经做了但我们刚刚是不是没有测试这个取消点赞我们可以来测试一下那么就是这个对吧那么其实测试的非常简单加一个什么我们再去做一个点赞肯定是500了因为不能重复点赞所以在这个位置我们再来一个dislike走那么是不是就取消了然后我们再来去执行一下
[08:03] 这样的话呢就OK那么这样的话就点赞又成功了好嘞好那么这样的话我们就已经完成了我们评论的一个点赞和以及这个取消点赞也OK好那么关于这个评论相关的一操作呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现小视频评论功能，包括评论列表、发布评论、点赞和取消点赞、关注用户等接口的代码编写与测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程笔记中“8.1 评论列表”部分，包含mock地址：https://mock.boxuegu.com/project/164/interface/api/72177，以及VideoController中@GetMapping("/id/comments")方法的代码。
画面2：展示VideoController中@GetMapping("/id/comments")方法的完整代码，包含分页参数page和pagesize。
画面3：展示VideoController中@PostMapping("/id/comments")方法的代码，用于保存评论，接收Map<String, String>参数和videoId。
画面4：展示VideoController中@PostMapping("/id/comments")方法的代码，光标位于方法体内部，下方是调试控制台，显示Java执行路径。
画面5：展示Mock服务页面，项目名称为“评论发布”，接口路径为POST /smallVideos/{id}/comments，mock地址为https://mock.boxuegu.com/project/164/smallVideo/{id}/comments。
画面6：展示Advanced REST Client工具，设置POST请求，请求地址为http://172.16.55.153:18080/smallVideos/5dc432a45459672c7492cad/comments，请求头包含Authorization。
画面7：展示VideoController中@PostMapping("/comments/{id}/like")和@PostMapping("/comments/{id}/dislike")方法的代码，用于点赞和取消点赞。
画面8：展示Robo 3T数据库工具，查询comment集合，显示多条评论记录，其中一条记录的commentType为“good”，content为“2”。
画面9：展示Robo 3T数据库工具，查询comment集合，光标选中一条记录，显示其id、publishedId、commentType、content等字段。
画面10：展示VideoService中设置评论焦点、点赞数、是否关注等逻辑的代码，包含Redis操作和判断用户是否点赞。
画面11：展示VideoService中@Autowired注解的字段，包括VideoApi、picUploadService、FastFileStorageClient等，光标位于@Autowired注解上方。
画面12：展示VideoService中查询评论数的代码，使用quanziApi.queryCommentCount方法，并在控制台输出日志。
画面13：展示课程笔记中“8.3 评论点赞”部分，包含代码片段和注释。
画面14：展示课程笔记中“8.4 关注用户”部分，说明关注用户对小视频发布者的影响。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@GetMapping("/id/comments")
public ResponseEntity<PageResult> queryCommentsList(@PathVariable("id") String videoId,
        @RequestParam(value = "page", defaultValue = "1") Integer page,
        @RequestParam(value = "pagesize", defaultValue = "10") Integer pagesize) {
    return this.commentsController.queryCommentsList(videoId, page, pagesize);
}
```
画面2：
```java
@GetMapping("/id/comments")
public ResponseEntity<PageResult> queryCommentsList(@PathVariable("id") String videoId,
        @RequestParam(value = "page", defaultValue = "1") Integer page,
        @RequestParam(value = "pagesize", defaultValue = "10") Integer pagesize) {
    return this.commentsController.queryCommentsList(videoId, page, pagesize);
}
```
画面3：
```java
@PostMapping("/id/comments")
public ResponseEntity<Void> saveComments(@RequestBody Map<String, String> param,
        @PathVariable("id") String videoId) {
    param.put("movementId", videoId);
    return this.commentsController.saveComments(param);
}
```
画面7：
```java
@PostMapping("/comments/{id}/like")
public ResponseEntity<Long> commentsLikeComment(@PathVariable("id") String publishId) {
    return this.movementsController.likeComment(publishId);
}

@PostMapping("/comments/{id}/dislike")
public ResponseEntity<Long> disCommentsLikeComment(@PathVariable("id") String publishId) {
    return this.movementsController.dislikeComment(publishId);
}
```
画面10：
```java
videoVo.setCommentFocus(10); // TODO 评论数
videoVo.setHasFocus(0); // TODO 是否关注
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER" + user.getId() + "_" + videoVo.getId();
videoVo.setHasLiked(this.redisTemplate.hasKey(likeUserCommentKey) ? 1 : 0); // 是否点赞
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + videoVo.getId();
if (StringUtils.isNotEmpty(value)) {
    videoVo.setLikeCount(Integer.valueOf(value)); // 点赞数
} else {
    videoVo.setLikeCount(0); // 点赞数
}
if (userIds.contains(record.getUserId())) {
    videoVo.setHasFocus(1); // TODO 是否关注
}
```
画面12：
```java
long commentCount = this.quanziApi.queryCommentCount(videoVo.getId(), type); // 评论数
videoVo.setCommentCount(commentCount == null ? 0 : commentCount.intValue());
videoVo.setHasFocus(0); // TODO 是否关注
String likeUserCommentKey = "QUANZI_COMMENT_LIKE_USER" + user.getId() + "_" + videoVo.getId();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“8. 小视频评论”，子标题“8.1 评论列表”，内容包含mock地址。
画面5：Mock服务页面标题为“基本信息”，包含项目名称、接口路径、mock地址等。
画面14：PPT标题为“8.4 关注用户”，内容说明关注用户对小视频发布者的影响。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

