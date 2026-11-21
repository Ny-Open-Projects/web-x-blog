# 12.圈子功能实现之动态信息评论（发表评论）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\12.圈子功能实现之动态信息评论（发表评论）_【海量资源尽在 666java.com】.mp4
- 时长 6分18秒（音频 379s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们去发表这个评论啊那么他的这个API呢是在这个位置就是评论提交啊这个API那我们来点击一下哎刷新一下啊那我们等待一下可能会网络有点慢好那么这个呢就是我们的评论提交的这个接口啊那么发起的是一个post请求那么下面呢是一些这个参数啊
[00:26] 当然了那么要注意的一点是我们这个参数啊来看一下啊那么其实我们这个参数呢它呢是一种啊json类型的这个之前我们也用过啊所以我们需要通过json来做一个接收了好那么然后呢最后的响应呢就没有内容了返回状态码就可以了好那么接下来呢我们就来实现一下好那么下面我们来写这个评论
[00:49] 那么public我们返回值呢就返回还是这个responseEdit然后呢这个就没有返回值那就写一个word然后呢我们做一个save comments然后呢我们去写一个这个叫做什么post mapping然后呢加一个我们先把这个写出来吧那么它需要有一个请求的一个这个json对吧那我们通过什么呢request
[01:18] request body设置是一个map然后呢stream来一个stream好那么我们来看一下这个叫paramount那么拿到这个我们去写一个这个注释这个叫什么呢就是我们去发表发表评论发表评论然后有了这个方法之后呢我们就调用这个Service点Service中的这个C5 comments好那我们把这个
[01:49] Param可以去拿到这个值也可以去传递那我们就直接拿到吧拿到这个Movement ID我们来获取一下那么这个叫Publish Publish ID等于这个Param.get好那么这是第一个参数那么第二个参数就是Comment就是我们的评论那么这个我们把它称之为叫Contact吧
[02:19] 好,那么应该叫什么con对吧con contact好,那么我们把这两个传递过去就是一个是public id一个就是contact内容那么就是我们给这个去这个动态我们去做一个评论当然我们这个不应该叫public id了对吧,那我们应该叫我们就叫这个moment id吧就叫它吧好
[02:47] 然后呢我们传递到我们这个里面来对吧然后呢我们就去做一个做一个保存了那么它的返回值呢我们就去接收是一个布尔类型吧布尔类型那么这样的话处理起来也比较方便那么我们去判断一下如果这个布尔布尔如果是去如果是去的话那代表就成功了那么我们就returnreturn它呢设置一个ok
[03:17] 就好了然后呢我们设置一个脑然后呢如果一旦出现什么异常的话那我们就给他来写一下如果出现异常的话那我们就return这个上面这个500了跟这个是一样好考虑一下好那么接下来呢我们去实现这个方法就可以了这个方法实现就比较简单了那么我们来看一下然后呢我们直接就去通过谁呢通过我们的这个
[03:47] 就是叫圈子API点有一个叫做savecomment这个对象那么传递四个参数那UIDpublic ID和我们的这个contact还有我们的这个type和contact那么就OK了那么首先第一个呢就是我们这个movement这个ID就是我们这个我们把它设置为就是我们的一个这个就是动态的ID那么其实这个还是应该去使用这个public对吧
[04:16] 我们一直使用它嘛用publics吧其实这个名字啊无所谓大家能够理解这个意思啊就可以了那么我们就把它改一下吧这个publics id好那还使用它吧然后呢还有就是第一个参数呢这个错了啊第一个参数应该是url那我们还是应该拿到url对象url等于叫做url url local.get
[04:43] 好那么拿到之后呢那我们就通过这个user.getid第一个参数是它那么第一个参数是userid第二个参数是publicid第三个呢是type那么要注意type呢这个我们变成2对吧评论是2然后呢还有什么呢就是contact内容那就是我们这个内容了传递过去那么这个方法它的返回值我们来看一下
[05:08] 它的返回值本身就是一个布尔那么我们就直接可以把这个是不是就往这一丢就好了这个大家应该能够理解了吧好那么这个就是做一个save这个操作了好那么接下来呢我们把我们这个服务呢就重新来启动一下然后我们去做一个这个测试好那么现在呢我们就启动起来了接下来呢我们来测试一下点击这个评论
[05:34] 然后呢我们下面去发表这个评论比如说我们写一个OK然后呢我们点击这个发送走就发布成功了然后呢我们再次点击一下看一下它能不能够查到这个列表那么发现下面这个位置是不是已经就有这个列表了对吧然后呢我们还可以去再输入一些这个看表情可以吗然后走评论成功了
[05:59] 然后呢我们再去点开来看一下啊也是OK的啊没有问题这个呢就是我们的这个保存这个评论的这个功能接下来呢我们就可以去做这个点赞的这个操作了啊OK好那么关于我们这个保存这个发表这个评论呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现评论功能的前后端交互，包括定义接口、编写控制器、服务层逻辑以及调用第三方 API。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了在 Typora 中的文档结构，当前章节为“1.1.4.3. 能够评论”，并显示了在 Postman 中测试接口的响应结果，响应体为 {"message": "发表评论成功"}。
画面 2: 在 MockBox 平台上配置一个 POST 接口，接口路径为 /comments，请求方法为 POST，Tag 为“评论”，状态为“已集成”。
画面 3: 在 IntelliJ IDEA 中查看 CommentsController.java 文件，展示了 @GetMapping 注解的 queryCommentsList 方法，参数为 @RequestParam("movementId") String publishId, @RequestParam(value = "page", defaultValue = "1") int page, @RequestParam(value = "pagesize", defaultValue = "10") int pageSize。
画面 4: 在 IntelliJ IDEA 中查看 CommentsController.java 文件，展示了 @PostMapping 注解的 saveComments 方法，方法签名为空。
画面 5: 在 IntelliJ IDEA 中查看 CommentsController.java 文件，展示了 @PostMapping 注解的 saveComments 方法，方法签名为空。
画面 6: 在 MockBox 平台上查看接口的 Body 参数，包括 movementId (string, 必填) 和 comment (string, 必填)。
画面 7: 在 IntelliJ IDEA 中查看 CommentsController.java 文件，展示了 @PostMapping 注解的 saveComments 方法，方法签名为空。
画面 8: 在 IntelliJ IDEA 中查看 CommentsController.java 文件，展示了 @PostMapping 注解的 saveComments 方法，方法签名为空。
画面 9: 在 IntelliJ IDEA 中查看 CommentsService.java 文件，展示了 saveComments 方法的参数类型为 String movementId, String content。
画面 10: 在 IntelliJ IDEA 中查看 CommentsService.java 文件，展示了 saveComments 方法的参数类型为 String movementId, String content。
画面 11: 在 IntelliJ IDEA 中查看 CommentsService.java 文件，展示了 saveComments 方法的参数类型为 String movementId, String content。
画面 12: 在 IntelliJ IDEA 中查看 CommentsService.java 文件，展示了 saveComments 方法的参数类型为 String movementId, String content。
画面 13: 在 IntelliJ IDEA 中查看 CommentsController.java 文件，展示了 @PostMapping 注解的 saveComments 方法，方法签名为空。
画面 14: 在 Typora 中的文档结构，当前章节为“1.4.4. 测试”，并显示了在 Genymotion 模拟器上运行的“动态评论”界面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
@GetMapping
public ResponseEntity<PageResult> queryCommentsList(@RequestParam("movementId") String publishId,
                                                   @RequestParam(value = "page", defaultValue = "1") int page,
                                                   @RequestParam(value = "pagesize", defaultValue = "10") int pageSize) {
    try {
        PageResult pageResult = this.commentsService.queryCommentsList(publishId, page, pageSize);
        if (null != pageResult) {
            return ResponseEntity.ok(pageResult);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 4:
```java
@PostMapping
public ResponseEntity<Void> saveComments() {
}
```

画面 5:
```java
/**
 * 发表评论
 * @param param
 * @return
 */
@PostMapping
public ResponseEntity<Void> saveComments(@RequestBody Map<String, String> param) {
    String publishId = param.get("movementId");
    String content = param.get("comment");
    Boolean bool = this.commentsService.saveComments(publishId, content);
    if (bool) {
        return ResponseEntity.ok(null);
    }
}
```

画面 9:
```java
public Boolean saveComments(String movementId, String content) {
```

画面 10:
```java
this.quanziApi.saveComment(movementId, content);
```

画面 11:
```java
this.quanziApi.saveComment(user.getId(), publishId, type, content);
```

画面 12:
```java
this.quanziApi.saveComment(user.getId(), publishId, type, content);
```

画面 13:
```java
/**
 * 发表评论
 * @param param
 * @return
 */
@PostMapping
public ResponseEntity<Void> saveComments(@RequestBody Map<String, String> param) {
    String publishId = param.get("movementId");
    String content = param.get("comment");
    Boolean bool = this.commentsService.saveComments(publishId, content);
    if (bool) {
        return ResponseEntity.ok(null);
    }
}
```

画面 14:
```java
/**
 * 发表评论
 * @param publishId
 * @param content
 * @return
 */
public Boolean saveComments(String publishId, String content) {
    User user = UserThreadLocal.get();
    this.quanziApi.saveComment(user.getId(), publishId, 2, content);
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

