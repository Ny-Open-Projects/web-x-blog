# 画面线理解：13.更新通知

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\13.更新通知_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:25, 00:39, 01:24, 01:51, 02:22, 02:45, 03:01, 03:20, 03:30, 03:56, 04:47, 05:23, 06:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:45:55

1) 这一组画面整体在讲什么（一句话）：
实现用户通知设置功能，包括前端接口定义、后端 Controller 层处理、Service 层业务逻辑以及数据库持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Typora 中的文档结构，当前章节为“2.8.3. BlackListService”和“2.9. 更新通知”。
- “2.9.1. mock接口”部分显示了 mock 服务的 URL：https://mock.tanhu.com/mock/7/Msww/notifications/setting。
- Headers 区域显示了请求头：Content-Type: application/json 和 Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

画面 2：
- 展示了 UsersController 中的 @PostMapping("/notifications/setting") 方法，用于处理更新通知设置的请求。
- 代码中提取了请求体中的 likeNotification、pinglunNotification、gonggaoNotification 三个布尔值。

画面 3：
- 展示了 UsersController 中的 updateNotification 方法，与画面 2 内容一致，用于处理通知设置更新。

画面 4：
- 展示了 UserService 中的 updateNotification 方法，其中调用了 this.settingsService.updateNotification(...)。
- 代码中设置了 blackListVo 的属性，如 setAvatar、setAge 等。

画面 5：
- 展示了 UserService 中的 updateNotification 方法，光标位于 this.settingsService.updateNotification(...) 处。
- 代码中设置了 user 的属性，如 setUserId、setCreated、setUpdated。

画面 6：
- 展示了 SettingsService 中的 updateNotification 方法，光标位于 this.settingsMapper.update(...) 处。
- 代码中使用了 QueryWrapper<Settings> 来构建查询条件。

画面 7：
- 展示了 SettingsService 中的 updateNotification 方法，光标位于 this.settingsMapper.update(...) 处。
- 代码中使用了 QueryWrapper<Settings> 来构建查询条件。

画面 8：
- 展示了 SettingsService 中的 updateNotification 方法，光标位于 settings.setPinglunNotification(...) 处。
- 代码中设置了 settings 的属性，如 setLikeNotification、setGonggaoNotification、setPinglunNotification。

画面 9：
- 展示了 SettingsService 中的 updateNotification 方法，光标位于 this.settingsMapper.update(settings, _) 处。
- 代码中使用了 QueryWrapper<Settings> 来构建查询条件。

画面 10：
- 展示了 SettingsService 中的 updateNotification 方法，光标位于 this.settingsMapper.update(settings, _) 处。
- 代码中使用了 QueryWrapper<Settings> 来构建查询条件。

画面 11：
- 展示了手机端 App 的界面，显示了“通知设置”页面，包含“允许我接收点赞通知”、“允许我接收评论通知”、“允许我接收公告通知”三个开关。

画面 12：
- 展示了手机端 App 的“通知设置”页面，三个开关均已打开。
- 同时显示了服务器端的控制台日志，记录了请求处理成功。

画面 13：
- 展示了 Navicat Premium 中的 tb_settings 表，显示了用户设置数据。
- 同时显示了手机端 App 的界面，显示了用户动态和通知设置。

画面 14：
- 展示了 Typora 中的文档结构，当前章节为“2.9.3. UsersService”和“2.9.4. SettingsService”。
- “2.9.4. SettingsService”部分显示了 updateNotification 方法的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
public Boolean doBlackList(Long userId, Long blackUserId) {
    QueryWrapper<BlackList> wrapper = new QueryWrapper<BlackList>();
    wrapper.eq("user_id", userId).eq("black_user_id", blackUserId);
    return this.blackListMapper.delete(wrapper) > 0;
}
```

画面 2：
```java
@PostMapping("/notifications/setting")
public ResponseEntity<Void> updateNotification(@RequestBody Map<String, Boolean> param) {
    try {
        Boolean likeNotification = param.get("likeNotification");
        Boolean pinglunNotification = param.get("pinglunNotification");
        Boolean gonggaoNotification = param.get("gonggaoNotification");
        this.userService.updateNotification(likeNotification, pinglunNotification, gonggaoNotification);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 3：
```java
@PostMapping("/notifications/setting")
public ResponseEntity<Void> updateNotification(@RequestBody Map<String, Boolean> param) {
    try {
        Boolean likeNotification = param.get("likeNotification");
        Boolean pinglunNotification = param.get("pinglunNotification");
        Boolean gonggaoNotification = param.get("gonggaoNotification");
        this.userService.updateNotification(likeNotification, pinglunNotification, gonggaoNotification);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 4：
```java
blackListVo.setAvatar(userInfo.getLogo());
blackListVo.setAge(userInfo.getAge());
blackListVoList.add(blackListVo);
pageResult.setItems(blackListVoList);
return pageResult;
```

画面 5：
```java
public void updateNotification(Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    User user = UserThreadLocal.get();
    this.settingsService.updateNotification(user.getId(), likeNotification, pinglunNotification, gonggaoNotification);
}
```

画面 6：
```java
public void updateNotification(Long userId, Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    this.settingsMapper.update(userId, likeNotification, pinglunNotification, gonggaoNotification);
}
```

画面 7：
```java
public void updateNotification(Long userId, Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    this.settingsMapper.update(userId, likeNotification, pinglunNotification, gonggaoNotification);
}
```

画面 8：
```java
public void updateNotification(Long userId, Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    Settings settings = new Settings();
    settings.setLikeNotification(likeNotification);
    settings.setGonggaoNotification(gonggaoNotification);
    settings.setPinglunNotification(pinglunNotification);
    settings.setUserId(userId);
    settings.setCreated(new Date());
    settings.setUpdated(new Date());
    this.settingsMapper.update(settings);
}
```

画面 9：
```java
public void updateNotification(Long userId, Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    Settings settings = new Settings();
    settings.setLikeNotification(likeNotification);
    settings.setGonggaoNotification(gonggaoNotification);
    settings.setPinglunNotification(pinglunNotification);
    settings.setUserId(userId);
    settings.setCreated(new Date());
    settings.setUpdated(new Date());
    QueryWrapper<Settings> queryWrapper = new QueryWrapper<Settings>();
    queryWrapper.eq("user_id", userId);
    this.settingsMapper.update(settings, queryWrapper);
}
```

画面 10：
```java
public void updateNotification(Long userId, Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    Settings settings = new Settings();
    settings.setLikeNotification(likeNotification);
    settings.setGonggaoNotification(gonggaoNotification);
    settings.setPinglunNotification(pinglunNotification);
    settings.setUserId(userId);
    settings.setCreated(new Date());
    settings.setUpdated(new Date());
    QueryWrapper<Settings> queryWrapper = new QueryWrapper<Settings>();
    queryWrapper.eq("user_id", userId);
    this.settingsMapper.update(settings, queryWrapper);
}
```

画面 11：
```java
public void updateNotification(Long userId, Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    Settings settings = new Settings();
    settings.setLikeNotification(likeNotification);
    settings.setGonggaoNotification(gonggaoNotification);
    settings.setPinglunNotification(pinglunNotification);
    settings.setUserId(userId);
    settings.setCreated(new Date());
    settings.setUpdated(new Date());
    QueryWrapper<Settings> queryWrapper = new QueryWrapper<Settings>();
    queryWrapper.eq("user_id", userId);
    this.settingsMapper.update(settings, queryWrapper);
}
```

画面 12：
```java
public void updateNotification(Long userId, Boolean likeNotification, Boolean pinglunNotification, Boolean gonggaoNotification) {
    Settings settings = new Settings();
    settings.setLikeNotification(likeNotification);
    settings.setGonggaoNotification(gonggaoNotification);
    settings.setPinglunNotification(pinglunNotification);
    settings.setUserId(userId);
    settings.setCreated(new Date());
    settings.setUpdated(new Date());
    QueryWrapper<Settings> queryWrapper = new QueryWrapper<Settings>();
    queryWrapper.eq("user_id", userId);
    this.settingsMapper.update(settings, queryWrapper);
}
```
