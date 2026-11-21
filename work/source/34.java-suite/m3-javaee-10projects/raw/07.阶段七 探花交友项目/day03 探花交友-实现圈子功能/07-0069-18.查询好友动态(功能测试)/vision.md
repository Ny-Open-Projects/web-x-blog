# 画面线理解：18.查询好友动态（功能测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\18.查询好友动态（功能测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:31, 01:02, 01:36, 02:05, 02:30, 02:49, 03:05, 03:19, 03:37, 04:30, 05:11, 05:32, 05:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:45:24

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
