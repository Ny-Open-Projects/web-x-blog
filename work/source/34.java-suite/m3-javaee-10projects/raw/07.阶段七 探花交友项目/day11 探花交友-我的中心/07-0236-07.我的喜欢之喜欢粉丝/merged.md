# 07.我的喜欢之喜欢粉丝

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\07.我的喜欢之喜欢粉丝_【海量资源尽在 666java.com】.mp4
- 时长 2分56秒（音频 176s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们这个关注粉丝啊那么在前面呢就是在我的这个粉丝中呢是不是有这样的一个操作喜欢这个操作就是粉丝呢喜欢我但是呢可能我还没有去关注这个粉丝那么就需要有这样的一个操作了那么接下来呢我们来看一下这个怎么做啊这个也是比较简单的那么我们只要去保存一条他的一个喜欢数据啊就可以了好那我们还是呢把这个来
[00:29] 拷贝到我们的这个Controller中那么找到我们这个us Controller那么我们拷到这个下面来那么同样的也是传递我们的一个这个user id然后呢我们去下面来看这个喜欢一个粉丝这个方法那我们把这个方法呢就创建出来那么这个怎么去做呢那么同样的也是需要先拿到我们的这个user对象然后呢我们去通过
[00:59] Ulike做一个save操作一个就是user.getid另外一个就是我们的urlidurlid啊好那么这样的话就完成了对吧这个就是什么这个就是我们的一个保存喜欢的这样的一个操作啊接下来呢我们把这个服务呢跑起来那我们重新来测试一下好那么接下来呢我们就来测试一下啊那我们直接进入到我们的这个主界面啊刚刚的这个登录呢应该还没有失效
[01:30] 那么我们就进入到我的这个里面呢我们找到这个粉丝啊这个然后呢我们比如说来看一下那么在相互喜欢中呢我们有这个245这个用户然后呢我们进入到粉丝呢这个我们去喜欢这个6啊然后呢去喜欢它然后呢我们就回到我们的这个就是相互喜欢这个列表中呢它应该就会有四个存在的因为我们又重新去插入了一条
[01:57] 我们这个喜欢就就是相当于什么呢就是粉丝喜欢我然后呢我也喜欢粉丝的话那么这样的话就会变成一个相互喜欢了然后呢我们在这个相互喜欢中呢也可以去比如说把这个二给他这个取消喜欢掉那么那么这个时候就会变成什么呢就是我不喜欢他但是粉他是不是喜欢我他变成这个粉丝这一块了对吧
[02:21] 然后我们可以再点击这个喜欢啊再回到相互喜欢里面是不是就可以看到这个二又回来了那么就是这样的一个操作啊那么其实可以看到呢我们到这里呢是不是就完成了我们关于我的喜欢的这个位置的一些数据的展现以及我们列表的这样的一个展现啊并且呢去实现了一些这个操作啊然后呢在前面这一块呢我们是不是也实现了一个我们这个谁看过我这个列表啊哎OK
[02:48] 好那么关于我们这个我的喜欢这一块的功能的一个讲解呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个社交应用中“关注粉丝”功能的后端实现，包括控制器、服务层代码编写与调试，以及前端界面交互效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中UsersController的代码，包含注释“关注粉丝”和@PostMapping("/fans/{uid}")方法，用于处理关注粉丝的HTTP请求。
画面2：展示手机端应用界面，显示“粉丝”列表，用户可点击“+ 关注”按钮关注用户。
画面3：展示IDE中测试接口的请求面板，准备对UsersController的“关注粉丝”接口进行测试。
画面4：展示IDE中UsersService.java文件，正在调试dislike方法，控制台输出了Spring Boot启动日志。
画面5：展示UsersController.java文件，高亮显示了@PostMapping("/fans/{uid}")方法的完整代码，包含try-catch块。
画面6：展示UsersService.java文件，光标位于likeFan方法的定义处，准备编写实现逻辑。
画面7：展示UsersService.java文件，光标位于this.userLikeApi.后，IDE提示了可选方法，如saveUserLike、deleteUserLike等。
画面8：展示UsersService.java文件，正在编写likeFan方法，调用this.userLikeApi.saveUserLike(user.getId())。
画面9：展示UsersService.java文件，完成likeFan方法的编写，控制台显示了Spring Boot启动日志。
画面10：展示电脑桌面，手机模拟器界面显示“探索交友 - 传智播客研究院”应用的主界面。
画面11：展示手机模拟器界面，用户点击“+ 关注”按钮后，弹出关注确认框，显示用户头像和昵称。
画面12：展示手机模拟器界面，用户点击“关注”按钮后，界面显示“关注成功”，并更新了粉丝数。
画面13：展示手机模拟器界面，用户滑动浏览“今日达人”列表，点击进入用户详情页。
画面14：展示手机模拟器界面，用户在“今日达人”列表中点击另一个用户，进入其个人主页。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 关注粉丝
 * @param userId
 * @return
 */
@PostMapping("/fans/{uid}")
public ResponseEntity<Void> likeFan(@PathVariable("uid") long userId) {
    try {
        this.userService.likeFan(userId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面4：
```java
public void dislike(Long userId) {
    User user = UserThreadLocal.get();
    this.userLikeApi.deleteUserLike(user.getId(), userId);
}
```

画面5：
```java
/**
 * 关注粉丝
 * @param userId
 * @return
 */
@PostMapping("/fans/{uid}")
public ResponseEntity<Void> likeFan(@PathVariable("uid") long userId) {
    try {
        this.userService.likeFan(userId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面6：
```java
public void likeFan(Long userId) {
    User user = UserThreadLocal.get();
    this.userLikeApi.saveUserLike(user.getId(), userId);
}
```

画面7：
```java
this.userLikeApi.
```
提示：
```java
queryBatchLikeList... PageInfo<UserLike>
queryEachLikeCount(Long userId) Long
saveUserLike(Long userId, Long) Long
isMutualLike(Long userId, Long, String)
queryFanCount(Long userId) Long
queryFanList(Long userId) Long
queryLikeCount(Long userId) Long
queryLikeList(Long... PageInfo<UserLike> Long
equals(Object obj) boolean
hashCode() int
```

画面8：
```java
public void likeFan(Long userId) {
    User user = UserThreadLocal.get();
    this.userLikeApi.saveUserLike(user.getId(), userId);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

