# 画面线理解：13.圈子功能实现之动态信息评论（评论点赞）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\13.圈子功能实现之动态信息评论（评论点赞）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:29, 00:39, 00:46, 00:56, 01:04, 01:15, 01:35, 01:47, 01:57, 02:19, 02:39, 02:58, 03:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:56:35

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
