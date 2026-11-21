# 18.查询好友动态（功能测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\18.查询好友动态（功能测试）_【海量资源尽在 666java.com】.mp4
- 时长 5分57秒（音频 357s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来测试一下那么我刚刚呢已经把这个服务呢重新启动好了那么接下来呢我们就把断点呢就打到我们的这个control这个里面来然后呢我们再去做一个这个测试啊然后呢下面呢我们先来做登录因为我们要去查询动态那么我们目前呢只有这个用户1是不是去发送了这个动态那我们就模拟这个用户2吧去做一个登录
[00:29] 然后呢我们去查看他的好友的动态然后呢我们先去发送我们这个那么先先去发送我们的这个短信验证码那么这个是不是就是这个是我们得刷新一下这样可能会有点问题然后呢我们去把它设置一下这个ID号这个手机号这个我们改成什么呢JSON这种方式去提交
[01:00] 好那么发送成功了然后我们再去做一个校验把手机号拷贝过来然后去走好那么就得到了这个token那么我们通过这个token去做一个查询然后我们再去来一个查询好那么我们去设置一个设置一个我们那个token然后去做一个get请求
[01:28] 当然了我们可以去传递两个参数对吧一个是配置一个是size那么我们去跟一个问号等于配置那这个我们其实可以这么来写就是可以给他个默认值那么我们改造一下吧然后default value设置为什么1然后如果下面的这个的话就设置为什么呢default value设置为10默认的查10条
[01:56] 那我们就重新再来启动一下吧好那我们来等待一下它的启动好那么现在呢就已经重启好了那么接下来呢我们就来测试一下那我们就可以不用去传递这个参数了因为有默认值了走那我们来看一下这个请求请求呢已经就进入到我们的这个还是在之前的我们这个token的intercept那我们直接通过吧好那么就进入到我们刚刚这个方法中了
[02:24] 那么可以看到这两个值其实就是1和10然后我们再去进入到我Service中这个方法然后走拿到这个User对象然后我们通过这个double去做查询看他能不能查到数据来看一下那么这个Page info是不是就拿到有7条数据对吧有7条数据那么都已经拿到了然后我们继续往下面走
[02:54] 走走那么这个就拿到给code死那么判断肯定是不为空的然后呢我们继续往下面走走走这个去每一个去做一个分装然后呢去这个是填充一些默认值然后呢去往下走走去做一个这样的一个填充那这样的话呢就是相同的这个逻辑了我们就直接跳过然后呢走走着再来然后呢走
[03:21] 那么这个UIS那就只有一个也就是我们用户ID唯一的这个只需要去查询一下它的用户信息那么去做查询是不是得到了然后我们去做循环去循环那么每一次其实都有拿到然后就可以通过了走那么最后的一个结果其实就是这样的一个结果那么我们可以来看一下它的一些数据那么可以看到有它的这个ID这个是我们动态的ID这个是
[03:51] 用户ID头像昵称性别年龄还有这个tag还有文字标签然后呢还有我们的图片地址然后它的距离时间呢等等那么这个呢都是按照我们的所设置的一些值呢进行做一个响应返回那么基本上呢是没有什么问题的那么到这里呢我们是不是就已经完成了一个这个测试呀对吧好那么接下来呢我们就来整合到我们的这个
[04:20] 我们的一个APP然后去做一个测试好那么我们把这个APP就跑起来来做一个测试好那么现在我们把模拟器就跑起来了那么下面我们来做一下测试那么首先检查一下我API地址这个是对的然后我们去做登录就是用我们的手机号就是我们第二个用户的手机号就是158008071988
[04:49] 然后呢我们来看一下啊008079887988然后呢点击这个获取验证码啊然后呢我们去输入这个验证码123456好那么登录成功了那么登录成功之后呢那么我们把这个之前我们所加的一个断点都去掉啊如果有断点的话一会儿请求会超时那我们就看不到这个效果了啊那我们点击这个圈子
[05:18] 那么推荐好友这块没有我们点击这个好友这个查询那么其实可以看到呢我们按照这个结构去做一个这个分装之后啊那么最终结果呢其实是已经啊就显示出来了啊这就是我们啊所看到啊所期望看到的这样的一个啊这个效果对吧哎OK好那么其实到这里呢我们是不是就已经完成了一个我们这个好友的这个就是动态的这样的一个查询那么最终就可以看到我们啊
[05:47] 跟我们讲一中啊类似的这样的一个效果了OK好那么关于我们的这个好友动态的一个查询的一个讲解那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过调试和 REST 客户端工具测试“动态发布列表”功能的实现，包括服务层逻辑、数据处理和前端展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- IDE 中展示 `MovementsService.java` 文件，其中 `queryPublishList` 方法调用 `this.quanZiApi.queryPublishList` 获取数据。
- 调试控制台显示应用启动成功。
- 代码片段：`public PageResult queryPublishList(Integer page, Integer pageSize) { PageResult pageResult = new PageResult(); User user = UserThreadLocal.get(); PageInfoPublish pageInfo = this.quanZiApi.queryPublishList(user.getId(), page, pageSize); pageResult.setCounts(0); pageResult.setPages(0); pageResult.setPageSize(pageSize); pageResult.setPage(page); if (CollectionUtils.isEmpty(records)) { // 没有查询到动态数据 return pageResult; }`

画面 2：
- Advanced REST Client 插件界面，显示历史请求记录，包括登录、获取动态列表、点赞、评论等接口。
- 画面中鼠标悬停在 GET 请求 `http://172.16.55.153:18081/movements?page=1` 上。

画面 3：
- Advanced REST Client 插件界面，正在加载历史记录。

画面 4：
- Advanced REST Client 插件界面，输入框中显示 `http://172.16.55.153:18081/movements`，下方弹出建议的分页 URL。

画面 5：
- Advanced REST Client 插件界面，输入框中显示 `http://172.16.55.153:18081/movements?page=1`，下方弹出建议的分页 URL。

画面 6：
- IDE 中展示 `MovementsService.java` 文件，调试器断点位于 `queryPublishList` 方法中，变量面板显示 `page=1`、`pageSize=10`。
- 代码片段：`public PageResult queryPublishList(Integer page, Integer pageSize) { PageResult pageResult = new PageResult(); User user = UserThreadLocal.get(); PageInfoPublish pageInfo = this.quanZiApi.queryPublishList(user.getId(), page, pageSize); pageResult.setCounts(0); pageResult.setPages(0); pageResult.setPageSize(pageSize); pageResult.setPage(page); if (CollectionUtils.isEmpty(records)) { // 没有查询到动态数据 return pageResult; }`

画面 7：
- IDE 中展示 `MovementsService.java` 文件，调试器断点位于 `queryPublishList` 方法中，变量面板显示 `records` 列表内容，包含多个 `Publish` 对象。
- 代码片段：`PageInfoPublish pageInfo = this.quanZiApi.queryPublishList(user.getId(), page, pageSize);`

画面 8：
- IDE 中展示 `MovementsService.java` 文件，调试器断点位于 `queryPublishList` 方法中，代码片段显示对 `movements` 对象设置属性，如点赞数、距离、是否点赞等。
- 代码片段：`movements.setLoveCount(100); // TODO 喜欢数 movements.setDistance("1.2公里"); // TODO 距离 movements.setHasLoved(1); // TODO 是否喜欢 movements.setIsLiked(0); // TODO 是否点赞 movements.setCommentCount(30); // TODO 评论数 movements.setCreateDate(RelativeDateFormat.format(new Date(record.getCreated()))); // 发布时间 movements.setTextContent(record.getText()); movements.setImageContent(record.getMedias()).toArray(new String[][]);`

画面 9：
- IDE 中展示 `MovementsService.java` 文件，调试器断点位于 `queryPublishList` 方法中，代码片段显示使用 `QueryWrapper` 查询用户信息并设置标签。
- 代码片段：`QueryWrapper<UserInfo> userInfoQueryWrapper = new QueryWrapper<>(); userInfoQueryWrapper.in("user_id", userIds); List<UserInfo> userInfoList = this.userInfoService.queryUserInfolist(userInfoQueryWrapper); for (Movements movements : movementsList) { if (userInfo.getuId().longValue() == userInfo.getuId().longValue()) { movements.setTags(StringUtils.split(userInfo.getTag(), ','); }`

画面 10：
- IDE 中展示 `MovementsService.java` 文件，调试器断点位于 `queryPublishList` 方法中，代码片段显示设置用户昵称、性别、头像、年龄等属性。
- 代码片段：`movements.setTags(StringUtils.split(userInfo.getTag(), ','); movements.setNickname(userInfo.getNickName()); movements.setGender(userInfo.getSex().name().toLowerCase()); movements.setAvatar(userInfo.getLogo()); movements.setAge(userInfo.getAge());`

画面 11：
- 桌面环境，显示 Genymotion 模拟器运行的手机界面，屏幕显示一张图片和文字“孤独無處安放”。

画面 12：
- IDE 中展示 `MovementsService.java` 文件，调试器断点位于 `queryPublishList` 方法中，变量面板显示“Frames are not available”。
- 代码片段：`if (userIds.contains(record.getUserId())) { userIds.add(record.getUserId()); }`

画面 13：
- IDE 中展示 `MovementsController.java` 文件，调试器断点位于 `queryPublishList` 方法中，右侧显示 Genymotion 模拟器界面，展示动态列表。
- 代码片段：`@RequestMapping("/queryPublishList") public ResponseEntity<PageResult> queryPublishList(@RequestParam("page") Integer page, @RequestParam("pageSize") Integer pageSize) { PageResult pageResult = this.movementsService.queryPublishList(page, pageSize); return ResponseEntity.ok(pageResult); }`

画面 14：
- Typora 编辑器界面，显示“day03 四子 - Typora”文档，内容为动态列表的展示，包含用户头像、文字、点赞、评论等信息。
- 文档结构：`2.5. 省略排序动态 2.5.1. 修改dubbo服务接口 2.5.2. 修改服务层用例 2.5.3. MovementsController 2.5.4. MovementsService 2.5.5. 验证测试 3. 评论 3.1. 增加 3.1.1. 增加dubbo接口 3.1.2. 增加服务层用例 3.1.3. 增加控制器层 3.1.4. 增加数据库表 3.1.5. 增加测试用例 3.1.6. 测试`

