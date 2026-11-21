# 画面线理解：06.我的喜欢之取消喜欢

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\06.我的喜欢之取消喜欢_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:12, 00:20, 00:26, 00:31, 01:01, 01:07, 01:14, 01:41, 01:54, 02:03, 02:16, 02:30, 02:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:40:13

1) 这一组画面整体在讲什么（一句话）：
演示“取消喜欢”功能的前后端实现，包括前端界面交互、Controller 层的 @DeleteMapping 注解方法、Service 层的业务逻辑以及调用的 API。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示“谁看过我”页面，列出最近5人，其中2个是粉丝。界面底部有“取消喜欢”按钮。
画面 2：展示“关注喜欢”页面，列出多个用户，每个用户右侧有“取消喜欢”按钮。底部导航栏显示“关注喜欢”。
画面 3：展示 Typora 文档中“1.5. 取消喜欢”章节，包含 UsersController 和 UsersService 的代码片段。
画面 4：在 IntelliJ IDEA 中，展示 UsersController.java 文件中 queryLikeList 方法的代码，包含 @GetMapping 注解和 try-catch 块。
画面 5：在 IntelliJ IDEA 中，展示 UsersController.java 文件中 dislike 方法的代码，包含 @DeleteMapping 注解和 try-catch 块。
画面 6：在 IntelliJ IDEA 中，展示 UsersService.java 文件中 dislike 方法的代码，包含 queryScore 方法调用和 RandomUtils.nextDouble 方法。
画面 7：在 IntelliJ IDEA 中，展示 UsersService.java 文件中 dislike 方法的代码，包含 UserLikeListVo 的 setMatchRate 方法调用。
画面 8：在 IntelliJ IDEA 中，展示 UsersService.java 文件中 dislike 方法的代码，包含 UserThreadLocal.get() 方法调用和 User 类的 getMobile() 方法的自动补全。
画面 9：展示手机端“手机号登录注册”界面，包含输入框和“获取验证码”按钮。
画面 10：展示手机端“谁看过我”页面，点击用户头像后弹出用户信息卡片。
画面 11：展示手机端“关注喜欢”页面，列出多个用户，每个用户右侧有“取消喜欢”按钮。
画面 12：展示手机端底部导航栏，包含“消息”、“喜欢”、“发现”三个图标。
画面 13：展示 Typora 文档中“1.5. 取消喜欢”章节，包含 UsersController 和 UsersService 的代码片段。
画面 14：展示 Typora 文档中“1.5.3. 测试”章节，包含一个 HTTP 请求的截图，以及“1.6. 关注粉丝”章节的标题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
```java
/**
 * 取消喜欢
 * @param userId
 * @return
 */
@DeleteMapping("/like/{uid}")
public ResponseEntity<Void> dislike(@PathVariable("uid") Long userId) {
    try {
        this.userService.dislike(userId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```
```java
public void dislike(Long userId) {
    User user = UserThreadLocal.get();
    this.userLikeApi.deleteUserLike(user.getId(), userId);
}
```
画面 4：
```java
@GetMapping("/friends/{type}")
public ResponseEntity<PageResult> queryLikeList(@PathVariable("type") String type,
                                                @RequestParam(value = "page", defaultValue = "1") Integer page,
                                                @RequestParam(value = "nick", defaultValue = "") String nick) {
    try {
        page = Math.max(1, page);
        PageResult pageResult = this.usersService.queryLikeList(Integer.valueOf(page), type, nick);
        return ResponseEntity.ok(pageResult);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```
画面 5：
```java
@DeleteMapping("/like/{uid}")
public ResponseEntity<Void> dislike(@PathVariable("uid") Long userId) {
    try {
        this.userService.dislike(userId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```
画面 6：
```java
Double score = this.recommendUserService.queryScore(user.getId(), userInfo.getUserId());
if (score == 0) {
    score = RandomUtils.nextDouble(30, 90); // 特殊情况下的评分生成，一般情况下都会有值
    userLikeListVo.setMatchRate(score.intValue()); // 评分
}
```
画面 7：
```java
Double score = this.recommendUserService.queryScore(user.getId(), userInfo.getUserId());
if (score == 0) {
    score = RandomUtils.nextDouble(30, 90); // 特殊情况下的评分生成，一般情况下都会有值
    userLikeListVo.setMatchRate(score.intValue()); // 评分
}
userLikeListVos.add(userLikeListVo);
```
画面 8：
```java
public void dislike(Long userId) {
    User user = UserThreadLocal.get();
    this.userLikeApi.deleteUserLike(user.getId(), userId);
}
```
画面 14：
```java
public void dislike(Long userId) {
    User user = UserThreadLocal.get();
    this.userLikeApi.deleteUserLike(user.getId(), userId);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
