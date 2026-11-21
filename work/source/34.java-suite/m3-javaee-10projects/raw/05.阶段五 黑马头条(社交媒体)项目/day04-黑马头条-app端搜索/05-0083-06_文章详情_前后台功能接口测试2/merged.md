# 06_文章详情_前后台功能接口测试2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\06_文章详情_前后台功能接口测试2【海量资源尽在 666java.com】.mp4
- 时长 3分47秒（音频 227s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好这里有了数据之后呢咱们下面呢就来去看一下前面的效果啊前面的效果呢就是说在这儿是已经是点了啊展示了当前的是取消关注比如说你已经关注完了啊那关注完之后呢比如说我现在我现在想去取消点下取消你看啊取消那取消之后呢你可以可以再看下效果它就会自动的去把这条数据给干嘛呢给删掉给删掉啊行啊那没问题啊那这个功能咱们就测完了然后再往下看还有什么功能啊
[00:34] 往下走走走这里边还有一个点赞和不喜欢看到了吗这两个按钮当然这个评论转发跟收藏咱们并没有做所以咱们现在来去测一下当前点赞和不喜欢就可以了比如我点一下当前这个比如我点一下点赞当点一下点赞之后他就会去往当前的LagsBehaviour里边去加一条数据目前这不是有数据吗咱们先来删掉好吧看的效果明显一些
[01:04] 好上完之后呢咱们可以点一下点赞来看一看刷新一下这个数据是不是进来了啊没有问题啊这个数据其实就能哎插入进去嗯那再往下看吧好吧这里边还有一个不喜欢其实不喜欢的其实也是往当前的一个表中去存数据哪个表啊当前的unlike behavior是吧这里边数据比较多是吧咱们就我看看啊把这个9月份都在删掉好吧好然后这时候呢咱们再来去测一下啊
[01:40] 点刷新是不是这一块也进了数据了啊没问题啊说明咱们写的接口都没问题啊但是这个接口咱们之前写过之前也测过啊其实这些都没有事那行那这里边其实还隐藏了一个接口就是说我的阅读的时长就是阅读的行为这个呢咱们也会存当前的行为那这个呢其实咱们在阅读的时候它就会不停的往当前的一个表中去存数据哪个表知道吧叫read behavior都是它
[02:11] 咱们可以拉到最后可以看一下这里边应该有九月份今天是9月19号看有没有没有是吗刷新一下没有那这没有它可能还没有加进来我要去点一下再重新进一下好吧往下走走走走走走走走然后咱们再来看一下看一下这个效果9月19号的有没有呢
[02:56] 来找一找啊这块好像没有数据是吧那这样啊咱们就把这个9月份也给它删掉好吧删掉之后咱们再来看一下能不能去插入点数据就可以了因为这个数据可能它有可能会更新啊有可能会更新来咱们就来再去刷一下啊再去刷一下啊我刚才是退出了啊再重新登录一下啊还找到这条数据然后往下点点点点点好然后呢然后咱们就退出这条数据啊退出那退出完之后咱们再点去啊
[03:26] 这样的话咱们就算是阅读了啊阅读完之后看看他看看他到底有没有记录啊来刷新刷新刷新刷新你看这点数据啊看这点数据哎哪呢就是最后一条数据看到了吗就这个呢其实就是刚刚加入的这点数据好吧那这个数据其实这个阅读行为这个接口其实是没有问题的好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个基于 MySQL 数据库的新闻应用的用户行为数据（如关注、阅读）的存储与展示，以及前端页面的开发与调试。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Navicat for MySQL 中 `ap_user` 表的数据，选中了 id 为 18 的记录，字段包括 user_id, fans_id, fans_name, level, created_time, is_display, is_ shield_letter, is_shield_comment, burst。
画面2：展示一个手机端网页预览，标题为“游戏制作之路-unity捕鱼达人（一开始以及加载界面的制作）”，右侧有二维码提示使用 Weex playground app 扫描。
画面3：展示 Navicat for MySQL 中 `ap_user_follow` 表的数据，选中了 id 为 6 的记录，字段包括 user_id, follow_id, follow_name, level, is_notice, created_time, burst。
画面4：展示 IntelliJ IDEA 中 `AppFollowBehaviorServiceImpl.java` 文件的代码，其中包含 `saveFollowBehavior` 方法，有对 `ApUser` 对象的非空校验和 `userId` 的赋值逻辑。
画面5：展示 Navicat for MySQL 中 `ap_user` 表的结构，以及右侧的 `migration` 文件夹下的多个 SQL 文件，如 `migration.qrtz_blob_triggers.sql`、`migration.qrtz_simple_triggers.sql` 等。
画面6：展示 Navicat for MySQL 中 `ap_unlikes` 表的数据，选中了 id 为 2 的记录，字段包括 entry_id, article_id, count, read_duration, percentage, load_duration, created_time, updated_time, burst。
画面7：展示手机端网页预览，内容为“游戏制作之路-unity捕鱼达人（一开始以及加载界面的制作）”的第二部分，描述了使用 Unity 中的 Slider UI 组件。
画面8：展示 Navicat for MySQL 中 `ap_read_behavior` 表的数据，选中了 id 为 36 的记录，字段包括 entry_id, article_id, count, read_duration, percentage, load_duration, created_time, updated_time, burst。
画面9：展示手机端网页预览，内容为“游戏制作之路-unity捕鱼达人（一开始以及加载界面的制作）”的第二部分，描述了使用 Unity 中的 Slider UI 组件。
画面10：展示 Navicat for MySQL 中 `ap_read_behavior` 表的数据为空。
画面11：展示 Navicat for MySQL 中 `ap_read_behavior` 表的数据，选中了 id 为 32 的记录，字段包括 entry_id, article_id, count, read_duration, percentage, load_duration, created_time, updated_time, burst。
画面12：展示浏览器开发者工具中的 Network 面板，显示了对 `load_article_behavior/` 等接口的请求，包括 200 和 403 状态码。
画面13：展示浏览器开发者工具中的 Network 面板，显示了对 `show_article_behavior/` 等接口的请求，包括 200 和 403 状态码。
画面14：展示 Navicat for MySQL 中 `ap_read_behavior` 表的数据，选中了 id 为 37 的记录，字段包括 entry_id, article_id, count, read_duration, percentage, load_duration, created_time, updated_time, burst。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面4：
```java
public ResponseResult saveFollowBehavior(FollowBehaviorDto dto) {
    ApUser user = ApUserLocalContextUtil.get();
    if (user == null && dto.getEquipmentId() == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_REQUIRED);
    }
    Long userId = null;
    if (user != null) {
        userId = user.getId();
    }
```

画面5：
```
migration.qrtz_blob_triggers.sql
migration.qrtz_calendars.sql
migration.qrtz_cron_triggers.sql
migration.qrtz_dml_triggers.sql
migration.qrtz_fired_triggers.sql
migration.qrtz_job_details.sql
migration.qrtz_paused_trigger_grps.sql
migration.qrtz_simple_triggers.sql
migration.qrtz_simprop_triggers.sql
migration.qrtz_triggers.sql
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2、7、9：PPT 标题为“游戏制作之路-unity捕鱼达人（一开始以及加载界面的制作）”，内容包含“一、创建开始界面”、“二、游戏加载场景”等章节。
画面12、13：Network 面板中显示了请求的 URL、状态码、响应时间等数据，如：
- `load_article_behavior/` 请求状态码为 200，响应时间为 32 ms。
- `show_article_behavior/` 请求状态码为 403，响应时间为 11 ms。

5) 无。

