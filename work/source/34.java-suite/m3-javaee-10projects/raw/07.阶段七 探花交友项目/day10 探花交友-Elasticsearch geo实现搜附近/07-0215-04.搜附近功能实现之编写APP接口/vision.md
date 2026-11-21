# 画面线理解：04.搜附近功能实现之编写APP接口

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\04.搜附近功能实现之编写APP接口_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:14, 02:25, 03:31, 04:07, 05:10, 06:21, 07:38, 08:33, 09:40, 11:07, 12:23, 13:03, 13:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:23:15

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的“附近好友”功能的后端实现，包括控制器、服务层代码编写、API 调用调试及前端效果展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：浏览器打开 MockBox 网站，页面为空白，可能用于演示接口测试环境。
画面2：IntelliJ IDEA 中显示 `TodayBestController.java` 代码，定义了 `@GetMapping("/search")` 接口，用于查询附近用户，返回 `ResponseEntity.ok(list)`。
画面3：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，包含 `queryRecommendUserList` 方法，用于查询推荐用户列表。
画面4：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中调用 `this.userLocationApi.queryUserFromLocation` 查询附近用户。
画面5：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中对查询到的用户列表进行空值判断，若为空则返回 `Collections.emptyList()`。
画面6：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中使用 `QueryWrapper` 构建查询条件，根据性别筛选用户。
画面7：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中遍历用户列表，排除自己。
画面8：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中创建 `NearUserVo` 对象，准备返回数据。
画面9：Advanced REST Client 发送 POST 请求到 `http://192.168.31.90/tanhu/search`，请求头包含 `Authorization`，响应状态码为 200，响应体为 JSON 格式数据。
画面10：Genymotion 模拟器显示“附近”功能界面，用户点击“筛选”按钮。
画面11：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中调用 `this.userLocationApi.queryUserFromLocation` 获取用户位置信息。
画面12：IntelliJ IDEA 中显示 `TodayBestService.java` 代码，`queryNearUser` 方法中使用 `restTemplate.postForEntity` 发起 HTTP 请求。
画面13：Typora 编辑器显示“day10 讲义.md”文档，内容为“2. Elasticsearch 实现位置查询”，并附带一张“附近好友”功能的 UI 截图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@GetMapping("/search")
public ResponseEntity<List<NearUserVo>> queryNearUser(@RequestParam(value = "gender", required = false) String gender,
        @RequestParam(value = "distance", required = false) String distance) {
    try {
        List<NearUserVo> list = this.todayBeatService.queryNearUser(gender, distance);
        return ResponseEntity.ok(list);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面3：
```java
// 为当前用户生成一个默认推荐用户
todayBest = new TodayBest();
todayBest.setUserId(defaultUserId);
todayBest.setFateValue(99L);

// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getUserId());
if (null != userInfo) {
    todayBest.setAge(userInfo.getAge());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setNickname(userInfo.getNickName());
    todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar));
}

return todayBest;

public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam) {
    User user = UserThreadLocal.get();
```

画面4：
```java
this.userLocationApi.queryUserFromLocation(longitude, latitude, 10)
```

画面5：
```java
if (CollectionUtils.isEmpty(userLocationVoList)) {
    return Collections.emptyList();
}
```

画面6：
```java
List<Long> userIds = new ArrayList<>();
for (UserLocationVo locationVo : userLocationVoList) {
    userIds.add(locationVo.getUserId());
}
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in("user_id", userIds);
if (StringUtils.isNotBlank(gender)) {
    if (StringUtils.equalsIgnoreCase(gender, "man")) {
        queryWrapper.eq("sex", SexEnum.MAN);
    } else if (StringUtils.equalsIgnoreCase(gender, "woman")) {
        queryWrapper.eq("sex", SexEnum.WOMAN);
    }
}
```

画面7：
```java
for (UserLocationVo locationVo : userLocationVoList) {
    if (locationVo.getUserId().longValue() == user.getUserId().longValue()) {
        continue;
    }
    for (UserInfo userInfo : userInfoList) {
        if (locationVo.getUserId().longValue() == userInfo.getUserId().longValue()) {
            NearUserVo nearUserVo = new
```

画面8：
```java
NearUserVo (com.tanhu.server.vo)
double[]
int[]
boolean[]
char[]
float[]
long[]
short[]
void[]
```

画面9：
```json
{
  "code": 12,
  "userList": [
    {
      "userId": 25,
      "avatar": "https://itcast-tanhu.oss-cn-shanghai.aliyuncs.com/avatar_25.jpg",
      "nickname": "helma_25"
    },
    {
      "userId": 27,
      "avatar": "https://itcast-tanhu.oss-cn-shanghai.aliyuncs.com/avatar_27.jpg",
      "nickname": "helma_27"
    },
    {
      "userId": 10,
      "avatar": "https://itcast-tanhu.oss-cn-shanghai.aliyuncs.com/avatar_10.jpg",
      "nickname": "helma_10"
    }
  ]
}
```

画面12：
```java
HttpEntity<MultiValueMap<String, String>> httpEntity = new HttpEntity<>(params, headers);
ResponseEntity<Void> responseEntity = this.restTemplate.postForEntity(targetUrl, httpEntity, Void.class);
return responseEntity.getStatusCodeValue() == 200;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：Typora 文档标题为“day10 讲义.md”，二级标题“2. Elasticsearch 实现位置查询”，下方附带一张“附近好友”功能的 UI 截图，截图中显示“您附近有6个好友，选择他们聊聊吧！”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
