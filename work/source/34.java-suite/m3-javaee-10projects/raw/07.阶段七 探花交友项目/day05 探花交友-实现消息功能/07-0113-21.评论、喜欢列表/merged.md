# 21.评论、喜欢列表

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\21.评论、喜欢列表_【海量资源尽在 666java.com】.mp4
- 时长 3分48秒（音频 229s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现我们的评论列表和我们的喜欢列表因为这两个呢和我们前面的点赞列表呢它的实现逻辑呢是非常的小小啊所以说我们就两个一可以一起可以把它就做完了好那么下面呢我们来看一下我们的Controller那么我们去增加了两个这个方法啊那我们来拷贝一下然后呢我们去找到我们的
[00:26] 这个IM的这个Controller然后呢我们丢到下面来好那么一个呢是我们的查询评论的啊一个是查询我们的这个喜欢列表那么我们来看一下那么我们需要去创建这两个方法对吧那我们就进入到IM这个Service中去创建这两个方法那么我们把这个下面这个方法呢就拷贝过来了
[00:54] 拷贝过来然后呢我们直接丢到这来那么我们做了一个什么事情呢是这样的就是那么我们把之前的这个呢我们去做了一个抽取啊因为这个type呢是点赞评论和喜欢type是不一样的所以说我们这个原来写这个方法呢我们就不需要了啊把它去掉然后呢我们就写了一个叫做message contact list这样的一个方法然后呢去传递这个type进来
[01:22] 那么我们可以看到当我们去查询这个点赞列表的时候呢我们就传入1那么查询这个评论的话就是2那么喜欢的就是3啊这样的一个实现然后呢我们这个这个还是那个查询方法名的定义的问题啊好那么这样的话就OK了就没有问了没有问题了啊那么我们基本都使用的这个messagelike这样的一个对象啊那么因为在我们的这个接口中啊那么无论你是这个喜欢列表
[01:50] 还是评论列表它的这个结构呢都是一样的所以说我们就使用一个对象啊就可以了好那么接下来呢我们就来把我们的服务呢重启一下然后呢我们去做一个测试啊那我们找到我们的这个就是serve这个服务然后呢我们重启一下好那么来等待它的一个启动好那我们这个服务呢就跑起来了那么接下来呢我们就来测试一下啊那么我们呢来看一下刚刚的这个测试
[02:18] 那么这个呢查询的是我们这个点赞的一个列表那么下面我们来看一下喜欢的这个列表那么我们把后面改成这个likes改成这个likes发起请求那么这个呢就是喜欢的这个操作然后呢我们来看一下这个评论列表那么我们使用这个comments那么看一下他的评论那么他有这么多的一些这个数据啊
[02:47] 好嘞好那么接下来呢我们就还是整合到我们的APP里面来测试一下那么我们去这个APP可能挂了所以我们需要重启一下那么稍微等待一下我这边来重启一下好那么我们把我们这个应用的跑起来那我们来直接进入这个组界面我们来看一下我们的刚才刚才那个登录是否有失效如果失效的话重新登录一下就可以了
[03:13] 等我们点击这个消息然后点击这个点赞是不是拿到这个数据了对吧然后我们来看一下评论列表只有这么多的一些这个数据然后呢还有喜欢这个数据啊好那么这样的话呢其实我们就已经完成了那么我们这个操作对吧那么我们已经就实现了我们的一个这个点赞列表和评论列表以及我们喜欢列表的这样的一个功能的一个实现
[03:41] 好那么关于在评论和喜欢的一个列表的实现我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 后端通过控制器和 Service 层实现“喜欢列表”接口，并通过 Mock 服务和 Android 模拟器验证接口功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Mock 服务中“喜欢列表”接口的基本信息，包括接口路径 /messages/loves、HTTP 方法 GET、Mac 地址和请求头（Content-Type: application/json, Authorization: 令牌）。
画面 2: 展示 IntelliJ IDEA 中 IMController.java 文件，其中定义了 @GetMapping("/likes") 接口，接收 page 和 pageSize 参数，调用 imService.queryMessageLikeList 方法。
画面 3: 展示 IMController.java 文件中 @GetMapping("/comments") 和 @GetMapping("/loves") 方法，分别用于查询评论列表和喜欢列表，均接收 page 和 pageSize 参数。
画面 4: 展示 Typora 中的 day05.md 文档，其中包含 IMService 的代码片段，定义了 queryMessageLikeList、queryMessageCommentList 和 queryMessageLoveList 方法。
画面 5: 展示 IMService.java 文件中 queryMessageLikeList 方法的实现，通过循环遍历记录，根据用户 ID 匹配用户信息，构造 MessageLike 对象并添加到列表中。
画面 6: 展示 IMService.java 文件中 queryMessageLikeList 方法的实现，其中调用 queryMessageCommentList 和 queryMessageLoveList 方法。
画面 7: 展示 IMService.java 文件中 queryMessageCommentList 方法的实现，通过 QueryWrapper 查询用户信息列表，并遍历记录构造 MessageLike 对象。
画面 8: 展示 Mock 服务中“喜欢列表”接口的响应数据结构，包含 id、avatar、nickname、createDate 字段及其类型、是否必填、示例值和校验规则。
画面 9: 展示 IMService.java 文件中 queryMessageCommentList 方法的实现，其中使用 QueryWrapper 查询用户信息列表，并遍历记录构造 MessageLike 对象。
画面 10: 展示 IntelliJ IDEA 的运行日志，显示 Spring Boot 应用启动成功，包含多个 INFO 日志，如 ReferenceBeanBuilder、ThreadPoolTaskExecutor、TomcatWebServer 等。
画面 11: 展示 Advanced REST Client 中发送 GET 请求到 http://192.168.31.90/messages/likes，请求头包含 Authorization 令牌。
画面 12: 展示 Advanced REST Client 中发送 GET 请求后，响应状态码为 200，响应体为空。
画面 13: 展示 Genymotion 模拟器界面，显示“孤独无处安放”应用的主界面，包含“点赞”、“评论”、“喜欢”、“公告”等选项。
画面 14: 展示 Genymotion 模拟器界面，显示“消息”页面，包含“点赞”、“评论”、“喜欢”、“公告”等选项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@GetMapping("/likes")
public ResponseEntity<PageResult> queryMessageLikeList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                       @RequestParam(value = "pageSize", defaultValue = "10") Integer pageSize) {
    PageResult pageResult = this.imService.queryMessageLikeList(page, pageSize);
    return ResponseEntity.ok(pageResult);
}
```

画面 3:
```java
@GetMapping("/comments")
public ResponseEntity<PageResult> queryMessageCommentList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                       @RequestParam(value = "pageSize", defaultValue = "10") Integer pageSize) {
    PageResult pageResult = this.imService.queryMessageCommentList(page, pageSize);
    return ResponseEntity.ok(pageResult);
}

@GetMapping("/loves")
public ResponseEntity<PageResult> queryMessageLoveList(@RequestParam(value = "page", defaultValue = "1") Integer page,
                                                      @RequestParam(value = "pageSize", defaultValue = "10") Integer pageSize) {
    PageResult pageResult = this.imService.queryMessageLoveList(page, pageSize);
    return ResponseEntity.ok(pageResult);
}
```

画面 4:
```java
public PageResult queryMessageLikeList(Integer page, Integer pageSize) {
    return this.messageCommentList(type: 1, page, pageSize);
}

public PageResult queryMessageCommentList(Integer page, Integer pageSize) {
    return this.messageCommentList(type: 2, page, pageSize);
}

public PageResult queryMessageLoveList(Integer page, Integer pageSize) {
    return this.messageCommentList(type: 3, page, pageSize);
}
```

画面 5:
```java
List<MessageLike> messageLikeList = new ArrayList<>();
for (Comment record : records) {
    for (UserInfo userInfo : userInfoList) {
        if (userInfo.getUserId().longValue() == record.getUserId().longValue()) {
            MessageLike messageLike = new MessageLike();
            messageLike.setID(record.getID().toHexString());
            messageLike.setAvatar(userInfo.getLogo());
            messageLike.setNickname(userInfo.getNickName());
            messageLike.setCreateDate(new DateTime(record.getCreated()).toString(s: "yyyy-MM-dd HH:mm:ss"));
            messageLikeList.add(messageLike);
            break;
        }
    }
}
pageResult.setItems(messageLikeList);
return pageResult;
```

画面 6:
```java
public PageResult queryMessageLikeList(Integer page, Integer pageSize) {
    return this.messageCommentList(type: 1, page, pageSize);
}

public PageResult queryMessageCommentList(Integer page, Integer pageSize) {
    return this.messageCommentList(type: 2, page, pageSize);
}

public PageResult queryMessageLoveList(Integer page, Integer pageSize) {
    return this.messageCommentList(type: 3, page, pageSize);
}
```

画面 7:
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds);
List<UserInfo> userInfoList = this.userInfoService.queryUserInfoList(queryWrapper);
List<MessageLike> messageLikeList = new ArrayList<>();
for (Comment record : records) {
    for (UserInfo userInfo : userInfoList) {
        if (userInfo.getUserId().longValue() == record.getUserId().longValue()) {
            MessageLike messageLike = new MessageLike();
            messageLike.setID(record.getID().toHexString());
            messageLike.setAvatar(userInfo.getLogo());
            messageLike.setNickname(userInfo.getNickName());
            messageLike.setCreateDate(new DateTime(record.getCreated()).toString(s: "yyyy-MM-dd HH:mm:ss"));
            messageLikeList.add(messageLike);
            break;
        }
    }
}
pageResult.setItems(messageLikeList);
return pageResult;
```

画面 9:
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds);
List<UserInfo> userInfoList = this.userInfoService.queryUserInfoList(queryWrapper);
List<MessageLike> messageLikeList = new ArrayList<>();
for (Comment record : records) {
    for (UserInfo userInfo : userInfoList) {
        if (userInfo.getUserId().longValue() == record.getUserId().longValue()) {
            MessageLike messageLike = new MessageLike();
            messageLike.setID(record.getID().toHexString());
            messageLike.setAvatar(userInfo.getLogo());
            messageLike.setNickname(userInfo.getNickName());
            messageLike.setCreateDate(new DateTime(record.getCreated()).toString(s: "yyyy-MM-dd HH:mm:ss"));
            messageLikeList.add(messageLike);
            break;
        }
    }
}
pageResult.setItems(messageLikeList);
return pageResult;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: PPT 标题为“8.2. IMService”，内容包含 IMService 的代码片段，定义了 queryMessageLikeList、queryMessageCommentList 和 queryMessageLoveList 方法。
画面 8: 展示 Mock 服务中“喜欢列表”接口的响应数据结构，包含 id、avatar、nickname、createDate 字段及其类型、是否必填、示例值和校验规则。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

