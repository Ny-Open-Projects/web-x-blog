# 画面线理解：12.圈子功能实现之动态信息评论（发表评论）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\12.圈子功能实现之动态信息评论（发表评论）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:29, 00:46, 01:06, 01:30, 01:53, 02:33, 03:24, 03:41, 04:05, 04:48, 05:10, 05:31, 06:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:56:00

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
