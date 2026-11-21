# 画面线理解：11.圈子功能实现之动态信息评论（查询评论列表-测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\11.圈子功能实现之动态信息评论（查询评论列表-测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:17, 00:37, 00:40, 00:45, 00:58, 01:04, 01:16, 01:24, 01:30, 01:52, 01:54, 01:59, 02:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:55:27

1) 这一组画面整体在讲什么（一句话）：
演示一个评论点赞功能的后端 Java 代码实现、数据在 MongoDB 中的存储结构，以及通过 REST API 调用和 Android 模拟器展示前端效果的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 IntelliJ IDEA 中 CommentsService.java 文件的代码，实现根据用户 ID 查询评论列表并关联用户信息的逻辑。
画面 2：展示 Robo 3T 数据库客户端，显示名为 "quanzi_publish" 的集合，其中包含一个文档，其 _id 为 ObjectId("5d70cedb68ac5d1450303ac"), user_id 为 5, text 为 "今天天气不错"，locationName 为 "上海市"。
画面 3：展示 Robo 3T 中 "quanzi_publish" 集合的文档详情，显示 media 字段包含一个 URL：http://licost-tanhus.css-cn-shanghai.aliyuncs.com/images/quanzi/1.jpg。
画面 4：展示 Advanced REST Client 浏览器插件，准备发送一个 GET 请求，但响应内容为空。
画面 5：展示 Advanced REST Client 浏览器插件，成功发送 GET 请求后，响应内容为一个 JSON 数组，包含两个对象，每个对象有 _id、user_id、text、created、seeType、latitude、longitude、locationName 字段。
画面 6：展示 Windows 文件资源管理器，打开一个名为 "day04" 的文件夹，其中包含多个视频文件，如 "05.基于功能实现之点赞功能（点赞逻辑）.avi"。
画面 7：展示 Genymotion 应用启动界面，显示 "GENY MOTION Version 3.0.2"，正在启动。
画面 8：展示 Genymotion 界面，显示 "Initializing virtual device..."，正在初始化虚拟设备。
画面 9：展示 Genymotion 中一个 Android 应用的界面，显示 "推荐" 和 "好友" 标签页，内容为用户 "heima" 的动态。
画面 10：展示 Genymotion 中 Android 应用的界面，显示 "好友" 标签页，内容为用户 "heima" 的动态。
画面 11：展示 Genymotion 中 Android 应用的界面，点击 "动态评论" 后，弹出一个评论输入框，下方显示一个 Typora 文档窗口。
画面 12：展示 Typora 文档，内容为 day04 评论模块的代码，显示点赞逻辑，其中有一行注释 "点数（赞，0）"，以及代码片段：
```java
comments.setLikeCount(0);
string userKey = "QUANZI_COMMENT_LIKE_USER" + user.getId() + "_";
comments.setHasLiked(this.redisTemplate.hasKey(userKey) ? 1 : 0); //是否点赞
result.add(comments);
PageResult pageResult = new PageResult();
pageResult.setItems(result);
pageResult.setPage(page);
pageResult.setPageSize(pagesize);
pageResult.setPages(0);
pageResult.setCounts(0);
return pageResult;
```
画面 13：展示 Typora 文档，内容为 day04 评论模块的代码，显示保存评论的逻辑，其中有一行注释 "保存评论"，以及代码片段：
```java
/**
 * 保存评论
 * @param publishId
 * @param content
 * @return
 */
public Boolean saveComments(String publishId, String content) {
    User user = UserThreadLocal.get();
    return this.quanziApi.saveComment(user.getId(), publishId, 2, content);
}
```
画面 14：展示 Typora 文档，内容为 day04 评论模块的代码，显示保存评论的逻辑，其中有一行注释 "保存评论"，以及代码片段：
```java
/**
 * 保存评论
 * @param publishId
 * @param content
 * @return
 */
public Boolean saveComments(String publishId, String content) {
    User user = UserThreadLocal.get();
    return this.quanziApi.saveComment(user.getId(), publishId, 2, content);
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
if (!userIds.contains(record.getUserId())) {
    userIds.add(record.getUserId());
}

QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds);
List<UserInfo> userInfoList = this.userInfoService.queryUserInfolist(queryWrapper);

List<Comments> commentsList = new ArrayList<>();
for (Comment record : records) {
    Comments comments = new Comments();
    comments.setId(record.getId().toString());
    comments.setCreateDate(new Date(record.getCreated()).toString("yyyy-MM-dd HH:mm"));
    comments.setContent(record.getContent());
    for (UserInfo userInfo : userInfoList) {
        if (record.getUserId().longValue() == userInfo.getUserId().longValue()) {
```

画面 2：
```json
{
  "_id": ObjectId("5d70cedb68ac5d1450303ac"),
  "user_id": 5,
  "text": "今天天气不错",
  "medias": [
    "http://licost-tanhus.css-cn-shanghai.aliyuncs.com/images/quanzi/1.jpg"
  ],
  "seeType": 1,
  "locationName": "上海市",
  "_class": "com.tanhus.dubbo.server.pojo.Publish"
}
```

画面 5：
```json
[
  {
    "_id": "5d70cedb68ac5d1450303ac",
    "user_id": 5,
    "text": "今天天气不错",
    "created": 1568467006477,
    "seeType": 1,
    "latitude": 31.234567,
    "longitude": 121.456789,
    "locationName": "上海市"
  },
  {
    "_id": "5d70cedb68ac5d1450303ad",
    "user_id": 5,
    "text": "今天天气不错",
    "created": 1568467006477,
    "seeType": 1,
    "latitude": 31.234567,
    "longitude": 121.456789,
    "locationName": "上海市"
  }
]
```

画面 12：
```java
comments.setLikeCount(0);
string userKey = "QUANZI_COMMENT_LIKE_USER" + user.getId() + "_";
comments.setHasLiked(this.redisTemplate.hasKey(userKey) ? 1 : 0); //是否点赞
result.add(comments);
PageResult pageResult = new PageResult();
pageResult.setItems(result);
pageResult.setPage(page);
pageResult.setPageSize(pagesize);
pageResult.setPages(0);
pageResult.setCounts(0);
return pageResult;
```

画面 13：
```java
/**
 * 保存评论
 * @param publishId
 * @param content
 * @return
 */
public Boolean saveComments(String publishId, String content) {
    User user = UserThreadLocal.get();
    return this.quanziApi.saveComment(user.getId(), publishId, 2, content);
}
```

画面 14：
```java
/**
 * 保存评论
 * @param publishId
 * @param content
 * @return
 */
public Boolean saveComments(String publishId, String content) {
    User user = UserThreadLocal.get();
    return this.quanziApi.saveComment(user.getId(), publishId, 2, content);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
