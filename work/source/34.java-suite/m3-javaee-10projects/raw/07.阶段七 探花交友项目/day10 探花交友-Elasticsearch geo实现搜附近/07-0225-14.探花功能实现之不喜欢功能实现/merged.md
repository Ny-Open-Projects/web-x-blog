# 14.探花功能实现之不喜欢功能实现

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\14.探花功能实现之不喜欢功能实现_【海量资源尽在 666java.com】.mp4
- 时长 2分58秒（音频 179s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来开发这个不喜欢这个功能啊那么不喜欢这个功能呢我们现在就做一个简单的一个实现那么就是我们直接去把这个呃呃前面我们去添加的这个喜欢的这个数据呢给他去删除啊就可以了好那么我们就把这个方法我们拷贝过来然后呢我们找到我们today best下面呢有一个呃在最下面的位置啊然后呢我们放到这个位置来就是不喜欢
[00:28] 然后呢我们去实现这个方法那么就回到这个Service吧那我们就把这个方法直接也来啊拷贝过来然后呢我们就来看一下那么这个就是我们的一个dislike然后呢做一个删除啊就可以了好那么其实我们这个方法呢就搞定了那么接下来呢我们就把我们的所有的服务呢重新启动一下然后呢我们再把模拟器呢跑起来让我们来测试一下这两个这个接口好嘞好那么我们就来启动一下
[00:58] 好那么接下来呢我们就把我们这个模拟器呢就跑起来啊然后呢我们来测试一下那么我们还是输我们这个手机号啊6868然后呢我们去获取验证码输验证码好嘞那么这样的话呢就登录成功了然后呢我们进入到我们的这个探花我们来看一下啊那么在这个里面呢数据呢肯定是能够显示出来的对吧那我们来看一下左滑右滑这个效果
[01:27] 那我们去选择这个图片去滑动它那么要我们这个往这边滑滑动要大一点那么这样的话就喜欢了那么我们来看一下我们的数据有没有那么我们来刷新一下那么Urelike里面是不是已经就有了三条这个数据了对吧那么刚才是不是我们又滑了这个三条对吧然后呢喜欢然后呢比如说这个49喜欢那么我们
[01:56] 来看一下这里面应该是有49这条数据吧49有然后我们再进入我们来看一下还能不能有49这个用户那么26我们看一下有没有这个好像是没有因为我们要演示一下这个把它删除那么2627我们这个里面27里面本身就有对吧好那我们来看一下第一条就第二条是27
[02:21] 来看一下这个是27最后就是26然后我们把这个去往左滑给它删除掉然后我们再来看一下现在总共是6条数据那就变成了5条数据了那说明我们刚刚所写的这个接口是OK的没有问题然后这个去滑动这个去左滑右滑这样的一个效果那么这个就是我们这个探花这样的一个功能那么到这里我们是不是就已经
[02:48] 实现了我们这个碳花的这个展现包括它的一个左滑右滑这个功能好那么关于我们这个碳花这个功能的一个讲解呢那我们就讲到这里了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示“不喜欢”功能的后端代码实现与数据库操作，包括控制器、服务层代码及 MongoDB 数据库中的点赞记录查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档中 TodayBestController 的“不喜欢”功能代码，包含 @GetMapping 注解和异常处理。
画面 2: 显示 IntelliJ IDEA 中 TodayBestController 的“不喜欢”方法代码，与画面 1 内容一致。
画面 3: 显示 Typora 文档中 TodayBestService 的“不喜欢”方法代码，以及一个包含多个开发工具界面的缩略图。
画面 4: 显示 Genymotion 模拟器上的“手机号登录注册”页面。
画面 5: 显示 Genymotion 模拟器上的“探花”应用界面，展示用户头像和“喜欢”按钮。
画面 6: 显示 Genymotion 模拟器上的“探花”应用界面，用户点击了“喜欢”按钮。
画面 7: 显示 Robo 3T 数据库工具，展示 user_like 集合的文档结构，包含用户 ID、点赞用户 ID、创建时间等字段。
画面 8: 显示 Robo 3T 数据库工具，查询 user_like 集合，返回 5 条记录。
画面 9: 显示 Robo 3T 数据库工具，选中并展开第二条记录，显示详细字段值。
画面 10: 显示 Genymotion 模拟器上的“探花”应用界面，展示用户头像和“喜欢”按钮。
画面 11: 显示 Robo 3T 数据库工具，查询 user_like 集合，返回 5 条记录。
画面 12: 显示 Robo 3T 数据库工具，查询 user_like 集合，返回 5 条记录。
画面 13: 显示 Genymotion 模拟器上的“探花”应用界面，展示用户头像和“喜欢”按钮。
画面 14: 显示 Typora 文档中 TodayBestController 的“喜欢”功能代码，以及 TodayBestService 的“喜欢”方法代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 不喜欢
 *
 * @param likeUserId
 * @return
 */
@GetMapping("({id}/unlove")
public ResponseEntity<Void> dislikeUser(@PathVariable("id") Long likeUserId) {
    try {
        this.todayBestService.dislikeUser(likeUserId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 2:
```java
/**
 * 不喜欢
 *
 * @param likeUserId
 * @return
 */
@GetMapping("({id}/unlove")
public ResponseEntity<Void> dislikeUser(@PathVariable("id") Long likeUserId) {
    try {
        this.todayBestService.dislikeUser(likeUserId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 3:
```java
public Boolean dislikeUser(Long likeUserId) {
    User user = UserThreadLocal.get();
    return this.userLikeApi.deleteUserLike(user.getId(), likeUserId);
}
```

画面 14:
```java
/**
 * 喜欢
 *
 * @param likeUserId
 * @return
 */
@GetMapping("({id}/love")
public ResponseEntity<Void> likeUser(@PathVariable("id") Long likeUserId) {
    try {
        this.todayBestService.likeUser(likeUserId);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

```java
public Boolean likeUser(Long likeUserId) {
    User user = UserThreadLocal.get();
    String id = this.userLikeApi.saveUserLike(user.getId(), likeUserId);
    if (StringUtils.isEmpty(id)) {
        return false;
    }
    return true;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

