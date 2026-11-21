# 画面线理解：21.小视频功能开发之评论

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\21.小视频功能开发之评论_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:46, 01:13, 01:53, 02:23, 03:21, 03:54, 04:35, 05:16, 05:55, 06:26, 07:03, 07:34, 08:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:01:56

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
