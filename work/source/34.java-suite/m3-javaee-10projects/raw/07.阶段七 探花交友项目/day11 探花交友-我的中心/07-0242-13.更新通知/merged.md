# 13.更新通知

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\13.更新通知_【海量资源尽在 666java.com】.mp4
- 时长 6分39秒（音频 399s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们的更新啊我们这个通知的这样的一些这个数据啊那么首先呢我们来看一下我们的mock接口那我们来找一下那么是在我们的这个位置啊就是去设置我们的一些通知的一些相关的一些设置啊主要呢是这三个布尔值然后呢我们接下来呢就来实现一下啊那么首先呢我们来拷贝一下我们的这个Controller
[00:27] 然后呢找到我们的Service就是在我们的这个位置啊就是在us里面的这个这个Controller啊这个位置好那么我们来看一下我们的这Controller的一个代码啊然后呢我们在这个位置呢去接收一个我们的一个json然后呢把它转成是一个我们的map啊然后呢去获取这三个这个布尔值然后呢我们将它呢去传递到我们这个方法中
[00:56] 然后呢我们来看一下这个方法那么就直接来创建吧就是我们去修改我们通知的这个方法那我们来看一下这个应该怎么样去做实现那么首先呢肯定我们需要先拿到我们的user对吧等于user.get然后拿到之后啊接下来呢我们就去做一个更新那么我们呢就去调用啊调用我们的这个叫settings
[01:25] settings这个Service然后呢去做一个update啊现在还没有这个方法那我们来新建啊这样的一个方法啊那么我们把这三个参数啊加我们的一个用户ID呢我们传递过去点get ID啊然后呢我们再去拿到这三个啊就是一个是喜欢的一个通知啊一个是评论那一个呢就是我们的一个公告啊把这三个呢给他啊传递过去
[01:55] 然后我们去调用这个方法这个Service中是没有这个方法的那么我们就给它去创建我们的这个方法把这挤给A那么前面应该这个用的是user id那我们来改一下user id那么我们来看一下这个里面怎么样去做实现呢那我们是需要去更新我们的书记库对吧那我们要通过this.settings.map.update去做一个更新
[02:25] 那么需要传递的是两个参数那么一个就是settings一个就是我们的条件对吧那我们这样我们就先来给他设置我们的settings那么settings然后settings等于等于什么new一个settings然后我们去给他设置点set一个like的一个通知那就like他然后我们再去set一个公告然后这个就是谁
[02:56] 是不是就是公告然后呢我们再来set一个评论那么这个就是评论评论好那么这样的话呢我们就设置完成了那么这就是我们的一个这个第一个这个参数setis然后第二个呢就是我们的条件那我们同样呢需要去来构造一个querywrap这样的一个对象然后呢叫user in
[03:23] U的info叫什么呢setting啊我们的settings好然后呢叫query drop等于new一个query drop然后呢我们把它呢就传递过去好那么接下来呢给它设置条件那么这个条件呢那就是谁呢我们的这个EQ啊等于谁呢U然后呢下滑线ID然后呢来一个叫做U的ID啊好那么这样的话呢就可以完成一个更新了
[03:51] 好那么接下来呢我们就实际的来测试一下把我们的服务呢启动一下好那么接下来呢我们就来演示一下测试一下我们这个功能那么我们服务呢都已经跑起来了那么检查一下地址没有问题然后呢我们做一次登录02026868然后呢我们获取我们的这个验证码然后呢输入验证码123456
[04:18] 好,那么它就会登录到我们的这个主页然后呢,登录到主页之后呢我们就进入到我们的这个我的这个模块中啊然后呢,我们去选择这个通用设置那么在通用设置里面呢有一个叫做通知设置啊那么就可以看到目前呢我们呢,这三个开关呢都打开的一个状态那么所对应到我们的数据库里面的这个数据呢都是三个这个1啊,对吧
[04:47] 然后呢接下来呢假设我们把第二个给它关掉把这关掉然后呢我们再来刷新一下看我们的数据库里面啊那么这个是不是就变成零了那么当我们在退出我们的这个设置的时候啊那么比如说我回到首页啊然后呢我再进入到我的这个通用设置中啊再点击我这个里面的一个通知设置我会发现第二个是不是就处于关闭状态啊那我把第一个也关掉啊第三个也关掉
[05:15] 那么来看一下我们的数据那是不是就是都是零啊然后呢我再退出啊再退出然后呢再进入到我的这个首页然后呢再进入到那么我的这个我的页面再来查看一下是不是都是为关闭状态那么打开第一个那么可以来测试一下它是不是就是一了那么这样的话呢我们是不是就已经实现了我们的这个通知的这个设置啊那么大家要注意的是
[05:45] 那么我们虽然目前呢已经啊实现了我们这个通知这个设置但是呢我们并没有把这个开关呢去应用到我们的真正的这个通知的这个位置比如说呢这个有人喜欢我啊去发出这个通知啊等等并没有去做这样的事情啊那么大家呢在后续呢可以自行去完成这样的功能啊那我们目前呢只是去
[06:08] 完成了我们这个就是用户设置的一个保存而这个设置的开关呢并没有真正的去应用到我们的系统中啊这一点大家需要去注意一下啊那我相信这个呢其实我们做起来呢并不复杂啊也别不麻烦啊好那么呃这样的话呢我们就已经啊完成了我们这个呃更新我们通知的这样的一个服务的一个编写了哎OK
[06:32] 好那么关于我们这个通知的一个这个开关的更新了那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

