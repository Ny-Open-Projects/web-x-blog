# 04.圈子功能实现之动态信息点赞（编写接口服务-点赞测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\04.圈子功能实现之动态信息点赞（编写接口服务-点赞测试）_【海量资源尽在 666java.com】.mp4
- 时长 2分39秒（音频 159s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对我们刚刚所写的这个点赞的这样的一个服务呢我们去做一个测试啊那么现在呢我这个服务呢都已经跑起来了那么接下来呢我们先来找到一个我们的一个这个动态啊那么我们就比如说就第一个吧就它啊那我们把这个value呢来做一个拷贝然后呢我们去打开我们这个restclient工具做一个测试
[00:27] 那么我们把这个我们这个ID这个ID到这儿把这个ID拿过来然后呢后面我们有一个什么的like对吧来看一下对吧后面会有一个这个like那么就会请求到这个里面来那么我们还是呢去打一个断点然后呢我们去发起一个get请求走好那么来看一下断点呢就已经进入到了我们这个control然后呢我们就跟着断点呢去进入然后呢走拿到这个优劣对象
[00:56] 然后我们去通过我们的 API去做一个点赞操作那么其实可以看到已经设置为Bulls为True了对吧那就说明已经点赞成功了那么可以到里面来查看一下那么里面还没有刷新一下那么是不是有一个comment这张表那么这个表里面是不是就有了一个数据了对吧就是说那么这个用户就是说当前的用户对 Publis
[01:25] 然后呢做一个操作做什么呢type为1的这个操作就是点赞的这个操作啊好那么接下来呢我们继续往下面走走走走到这那么走到这呢我们来看一下啊它是不是包含了key呢ready失踪显然呢肯定是没有包含对吧没有包含呢就会走到这个里面来那我们去查询一下我们这个就是这个public id它所对应的这个点赞数啊然后呢往下面走
[01:54] 那么这个数量呢显然目前呢是1对吧给它设置为这个负值然后呢我们把它存到我们的这个ready使用然后呢往下面走标记为我已经点赞过了通过好那么这个逻辑是不是就已经OK了对吧然后呢我们再去点击一个如果我们再次去点赞会怎么样呢来看一下那么这个逻辑前面我们是不是已经处理过了然后走来看那么显然呢这个布尔值是不是就是false了对吧然后呢往下面走走走
[02:23] 走到下面就变成500了那么这样的话就可以保证点赞只能操作一次那么也就是说我们现在这个点赞这个是不是就已经搞定了OK好那么关于我们这个点赞的这样的一个这个接口服务的一个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个点赞功能的完整实现流程，包括前端调用、控制器处理、服务层逻辑、Redis缓存操作以及数据库交互，并通过调试器观察变量状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示服务层代码，用于处理点赞逻辑，包含Redis缓存操作和数据库查询。
画面2：展示控制器层代码，定义了点赞接口，调用服务层方法。
画面3：展示MongoDB数据库中“quanzi_publish”集合的文档内容，包含发布信息。
画面4：控制器层代码，高亮显示了调用服务层的语句。
画面5：调试器界面，显示了当前执行的代码行和变量值，包括publishId和movementsService。
画面6：MongoDB数据库中“quanzi_publish”集合的文档内容，高亮显示了某个文档的_id字段。
画面7：MongoDB数据库中“quanzi_comment”集合的文档内容，显示了评论信息。
画面8：调试器界面，显示了服务层代码执行时的变量状态，包括likeCount和redisTemplate。
画面9：调试器界面，继续展示服务层代码执行时的变量状态，包括likeCount和redisTemplate。
画面10：调试器界面，展示服务层代码中记录用户点赞的逻辑，设置了loveCommentKey。
画面11：调试器界面，继续展示服务层代码中记录用户点赞的逻辑，设置了loveCommentKey。
画面12：服务层代码，展示调用QuanZiApi保存点赞的逻辑。
画面13：控制器层代码，高亮显示了调用服务层的语句。
画面14：使用Advanced REST client工具向服务器发送POST请求，请求路径为/like，返回状态码500。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
String likeCommentKey = "QUANZI_COMMENT_LIKE_" + publishId;
if (this.redisTemplate.hasKey(likeCommentKey)) {
    Long count = this.quanZiApi.queryCommentCount(publishId, type: 1);
    likeCount = count;
    this.redisTemplate.opsForValue().set(likeCommentKey, String.valueOf(likeCount));
} else {
    likeCount = this.redisTemplate.opsForValue().increment(likeCommentKey);
}
```

画面2：
```java
@GetMapping("/{id}/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId) {
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

画面3：
```javascript
db.getCollection('quanzi_publish').find({})
```

画面4：
```java
@GetMapping("/{id}/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId) {
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

画面5：
```java
// 变量值
publishId = "5d7ceedb48ac9d14503f03ac"
this.movementsService = (MovementsService)@9277
```

画面6：
```javascript
db.getCollection('quanzi_publish').find({})
```

画面7：
```javascript
db.getCollection('quanzi_comment').find({})
```

画面8：
```java
// 变量值
publishId = "5d7ceedb48ac9d14503f03ac"
user = (User)@2060
bool = true
likeCount = (Long)@9310
likeCommentKey = "QUANZI COMMENT LIKE 5d7ceedb48ac9d14503f03ac"
this.redisTemplate = (StringRedisTemplate)@9307
```

画面9：
```java
// 变量值
publishId = "5d7ceedb48ac9d14503f03ac"
user = (User)@2060
bool = true
likeCount = (Long)@9310
likeCommentKey = "QUANZI COMMENT LIKE 5d7ceedb48ac9d14503f03ac"
this.redisTemplate = (StringRedisTemplate)@9307
```

画面10：
```java
// 变量值
publishId = "5d7ceedb48ac9d14503f03ac"
user = (User)@2060
bool = true
likeCount = (Long)@9310
likeCommentKey = "QUANZI COMMENT LIKE 5d7ceedb48ac9d14503f03ac"
this.redisTemplate = (StringRedisTemplate)@9307
```

画面11：
```java
// 变量值
publishId = "5d7ceedb48ac9d14503f03ac"
user = (User)@2060
bool = true
likeCount = (Long)@9310
likeCommentKey = "QUANZI COMMENT LIKE 5d7ceedb48ac9d14503f03ac"
this.redisTemplate = (StringRedisTemplate)@9307
```

画面12：
```java
public long likeComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.saveLikeComment(user.getId(), publishId);
    if (!bool) {
        return null;
    }
    return null;
}
```

画面13：
```java
@GetMapping("/{id}/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId) {
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

画面14：
```http
POST /movements/5d7ceedb48ac9d14503f03ac/like HTTP/1.1
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdWJ1c2VzIiwiZXhwIjoxNTc3NzYwNjMwLCJpYXQiOjE1NzczNjA2MjIsInN1YiI6ImFkbWluIiwiYXVkIjoiYXNkcm9pZCJ9.6mJ6Z0F1ZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJkZmJk

