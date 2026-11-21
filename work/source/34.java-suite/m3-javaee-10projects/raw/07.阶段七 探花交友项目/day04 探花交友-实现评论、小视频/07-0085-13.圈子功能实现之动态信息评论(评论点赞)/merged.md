# 13.圈子功能实现之动态信息评论（评论点赞）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\13.圈子功能实现之动态信息评论（评论点赞）_【海量资源尽在 666java.com】.mp4
- 时长 3分18秒（音频 199s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下评论点赞啊那么评论点赞呢是在下面的这个位置那么也就是说我们刚刚所看到的这个评论后面有个小的按钮啊这个点赞这个功能
[00:13] 那么评论点赞其实跟我们之前的对于我们动态点赞它是一样的也是所有保存的数据都一样只是它的点赞的或者评论目标是不一样所以说这个其实我们可以看到API也基本都是一样的所以说我们可以直接照搬之前的逻辑了但是要注意的是它的请求路径是不一样的
[00:37] 所以我们只能是这么来玩就是在我们之前的这个movements这个Controller中这个点赞和取消点赞的这两个逻辑我们需要来拷贝一下然后把它放到我们这个commons Controller中也就是我们需要往这一丢然后我们需要把这个movements的一个Service注进来注进来那么我们去注进叫movements
[01:07] 然后呢moments这个叫Service啊Service把它呢注入进来我们共用一个Service然后呢去使用下面这个逻辑就可以了那么我们这个Controller的我们代码呢就是相当于两边代码是一样的这样的代码但是呢它的路径呢又是不一样的所以说呢我们只能是去这样去做一个这个处理了所以说呢我们这个就不用去
[01:36] 关注这个他的这个就是idea工具的这个提示了对吧好的我们这样去写就这个点赞这个功能呢其实就搞定了好的我们来把这个服务呢来重启一下那我们来看一下这个效果好那么现在呢我们就重新启动好了然后呢我们再来测试一下就是我们点击这个就是评论对吧然后呢去后台需要去查询一下然后我们点击这个点赞
[02:03] 哎走哎发现这个点赞是不是也是OK了啊那么我们再来去点击一下看他会怎么样的哎你发现呃这个是不是已经就标记为已经点赞了对吧那我们呃可以哎那么呃再退出一下那么我点击他啊然后呢我再去点击他好嘞然后呢取消然后呢我再进入你会发现他是不是已经就取消了啊这个
[02:29] 因为这个逻辑跟我们前面是一样的所以说呢我们就直接照搬过来它肯定也是功能是OK的对吧好那我们点击一下哎没有问题再测试一下好再来测一下OK没有问题的好那么其实这个呢就是我们对于评论就是这个动态中的这个评论的一个点赞它和前面这个逻辑是一样的逻辑啊只是说在评论中的只有点赞没有喜欢了如果有喜欢的话他们也可以直接把这个拿过来也是可以去使用的啊
[02:57] OK好那么这样的话呢我们其实对于我们的这个评论功能呢基本呢也就搞定了对吧那么对于我们这个点赞呢喜欢呢还有评论呢都已经搞定了对吧包括这个评论中的点赞也搞定了好嘞好那么关于我们这个评论的一些相关的功能呢那我们就讲到这里了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个社交应用中“评论”和“点赞/取消点赞”功能的前后端实现，包括接口定义、代码编写和移动端交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了接口管理平台中“评论-提交”接口的详情，包括接口路径 /api/comments、请求头 Content-Type: application/json、Authorization 认证信息，以及返回数据类型为 integer。
画面 2: 展示了接口管理平台中“点赞”接口的返回数据定义，返回值为 integer 类型，最大值 100，最小值 0。
画面 3: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，其中定义了 @PostMapping("/comments") 方法，用于保存评论，调用 commentsService.saveComments 方法。
画面 4: 展示了 IntelliJ IDEA 中 MovementsController.java 文件，其中定义了 @GetMapping("/{id}/love") 方法，用于点赞，调用 movementsService.likeComment 方法。
画面 5: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，其中定义了 @GetMapping("/{id}/dislike") 方法，用于取消点赞，调用 movementsService.disLikeComment 方法。
画面 6: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，其中定义了 @GetMapping("/comments") 方法，用于查询评论列表，调用 commentsService.queryCommentsList 方法。
画面 7: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，其中在 CommentsController 类中添加了 @Autowired MovementsService movementsService; 字段。
画面 8: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，其中定义了 @GetMapping("/{id}/like") 方法，用于点赞，调用 movementsService.likeComment 方法。
画面 9: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，其中定义了 @GetMapping("/{id}/dislike") 方法，用于取消点赞，调用 movementsService.disLikeComment 方法。
画面 10: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，同时在右侧弹出 Genymotion 模拟器，显示了“动态评论”界面，服务器日志显示应用已启动。
画面 11: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，同时在右侧 Genymotion 模拟器中，用户点击了“点赞”按钮，界面显示点赞数。
画面 12: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，同时在右侧 Genymotion 模拟器中，用户点击了“取消点赞”按钮，界面显示点赞数变化。
画面 13: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，同时在右侧 Genymotion 模拟器中，用户点击了“取消点赞”按钮，界面显示点赞数变化。
画面 14: 展示了 IntelliJ IDEA 中 CommentsController.java 文件，同时在右侧 Genymotion 模拟器中，用户点击了“取消点赞”按钮，界面显示点赞数变化。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
@PostMapping("/comments")
public ResponseEntity<Void> saveComments(@RequestBody Map<String, String> param) {
    try {
        String publishId = param.get("movementId");
        String content = param.get("comment");
        Boolean bool = this.commentsService.saveComments(publishId, content);
        if (bool) {
            return ResponseEntity.ok(null);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 4:
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

画面 5:
```java
@GetMapping("/{id}/dislike")
public ResponseEntity<Long> dislikeComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.disLikeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 6:
```java
@GetMapping("/comments")
public ResponseEntity<PageResult> queryCommentsList(@RequestParam("movementId") String publishId,
        @RequestParam(value = "page", defaultValue = "1") Integer page,
        @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
    try {
        PageResult pageResult = this.commentsService.queryCommentsList(publishId, page, pageSize);
        if (null != pageResult) {
```

画面 7:
```java
@Autowired
private MovementsService movementsService;
```

画面 8:
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

画面 9:
```java
@GetMapping("/{id}/dislike")
public ResponseEntity<Long> dislikeComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.disLikeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

