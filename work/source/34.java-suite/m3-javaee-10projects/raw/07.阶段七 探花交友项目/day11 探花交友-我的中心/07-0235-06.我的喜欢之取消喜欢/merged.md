# 06.我的喜欢之取消喜欢

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\06.我的喜欢之取消喜欢_【海量资源尽在 666java.com】.mp4
- 时长 2分44秒（音频 165s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们这个取消喜欢那么这个取消喜欢呢它呢是在我们的这个列表中啊可以有这样的一个操作啊那么接下来呢我们就来实现这个功能那么首先呢来看一下我们这个us Controller那么我们先把它呢就拷贝过来那么加入到我们的这个us Controller中然后呢我们就加到这个最下面来啊在这个位置
[00:29] 这就是我们这个取消喜欢那我们接收的是一个我们的一个UID啊UID那么这个呢是我们要取消哪个用户呃然后呢我们去调用这个Service中的啊这个dislike这个方法那么就可以了好那我们把这个方法呢就写出来那么实际我们去实现我们这个取消喜欢呢是啊非常啊简单的啊就是我们去直接去调用之前的delete方法就可以了
[01:00] 然后呢去通过这个usd local.get拿到一个usd项然后呢我们去调用我们这个usd like然后呢有一个delete啊传递一个叫做get id另外一个呢就是这个usd id啊这样的话就ok了那么做删除啊就可以了好那么接下来呢我们就把这个服务呢我们就跑起来我们来测试一下
[01:27] 好那么接下来呢我们就来测试一下啊那么现在呢我们已经把服务呢都跑起来了那么下面呢我们还是去修改一下服务地址那还是我们这个我们的本地地址啊然后呢我们去登录一下然后我们去做一个这个取消喜欢这样的一个测试啊好然后呢我们就会进入到我们的主页啊然后呢我们进入到我的这个模块中那么这个里面呢会有一些
[01:57] 这个相互喜欢啊等等那么点击这个喜欢那么这个里面就会有一些这个取消喜欢比如说呢我们就把这个11吧就是这个第三个啊这个用户我们去给他去做一个取消喜欢啊这样的话就没了之前是有13个那我们这个还没有刷新啊那么我们再点击首页然后我们再点到这个我的里面来看一下它是不是就变成12了对吧那就说明我们这个取消喜欢的功能是不是就OK了对吧
[02:26] 好那么下面我们来看一下我们的讲义在某讲义中这个就是我们的Controller然后下面这个就是Service是比较简单的一个实现然后下面这个是一个测试刚刚我们是直接整合到我们的APP里面去做了一个测试好那么关于我们这个取消喜欢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

