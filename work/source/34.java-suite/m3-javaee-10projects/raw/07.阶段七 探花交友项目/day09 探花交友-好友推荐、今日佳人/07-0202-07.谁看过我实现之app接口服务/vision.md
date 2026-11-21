# 画面线理解：07.谁看过我实现之app接口服务

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\07.谁看过我实现之app接口服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:43, 01:17, 02:05, 02:52, 04:33, 05:12, 06:16, 06:50, 07:28, 08:09, 09:10, 10:01, 10:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:13:26

1) 这一组画面整体在讲如何在 Java 服务端实现一个根据用户 ID 查询访客列表的接口，涉及 Redis 缓存、MongoDB 查询、以及与用户服务的联动。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了接口管理平台中一个名为“游客访问”的 GET 接口，其 Mock 地址为 https://mock.boxuegu.com/mock/164/movements/Visitors。
画面 2: 展示了 `VisitorsApiImpl.java` 中的 `queryRecommendList` 方法，用于根据用户 ID 查询推荐访客列表。
画面 3: 展示了 `VisitorsVo` 类的定义，包含 id、avatar、nickname、gender、tags、fateValue 等字段。
画面 4: 展示了 `MovementsService` 中的 `saveMovements` 方法，用于保存访客动态，包括文本内容、经纬度和上传的图片。
画面 5: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，开始编写逻辑，调用 `this.visitorsApi.top` 方法。
画面 6: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，引入 `StringUtils` 工具类进行字符串判断。
画面 7: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，调用 `this.visitorsApi.topVisitor(user.getId(), num: 6)` 查询访客。
画面 8: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，引入 `IfNode`、`IfClosure` 等条件判断类。
画面 9: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，使用 `StringUtils.isEmpty(data)` 判断数据是否为空。
画面 10: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，使用 `visitor.getVisitorUserId()` 获取访客用户 ID。
画面 11: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，使用 `QueryWrapper<UserInfo>` 构建查询条件。
画面 12: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，使用 `for` 循环遍历访客列表，匹配用户 ID。
画面 13: 展示了 `MovementsController` 中的 `VisitorsVo` 类定义，与画面 3 内容一致。
画面 14: 展示了 `MovementsService` 中的 `queryVisitorsList` 方法，最终逻辑：如果 Redis 缓存存在则直接返回，否则调用 `topVisitor` 查询并缓存。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2:
```java
Query recommendQuery = Query.query(Criteria
        .where("UserId").is(visitors.getUserId())
        .and("toUserId").is(visitors.getUserId()));
RecommendUser recommendUser = this.mongoTemplate.findOne(
        recommendQuery, RecommendUser.class);
if (null != recommendUser) {
    visitors.setScore(recommendUser.getScore());
} else {
    //设置默认值
    visitors.setScore(300);
}
return visitorsList;
```

画面 3:
```java
package com.tanhu.server.vo;
import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
public class VisitorsVo {
    private Long id;
    private String avatar;
    private String nickname;
    private String gender;
    private String[] tags;
    private Integer fateValue;
}
```

画面 4:
```java
public String saveMovements(String textContent,
        String location,
        String longitude,
        String latitude,
        MultipartFile[] multipartFile) {
    User user = UserThreadLocal.get();
    Publish publish = new Publish();
    publish.setUserId(user.getId());
    publish.setText(textContent);
    publish.setLocationName(location);
    publish.setLatitude(latitude);
    publish.setLongitude(longitude);
    //图片上传
    List<String> imageUrls = new ArrayList<>();
    for (MultipartFile file : multipartFile) {
        PicUploadResult uploadResult = this.nightloadService.upload(file);
```

画面 5:
```java
public List<VisitorsVo> queryVisitorsList() {
    User user = UserThreadLocal.get();
    //如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
    String redisKey = "visitors_" + user.getUserId();
    String data = this.redisTemplate.opsForValue().get(redisKey);
    if (StringUtils.isEmpty(data)) {
        //按照数量查询
        this.visitorsApi.top
        return null;
    }
```

画面 6:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

画面 7:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

画面 8:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

画面 9:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

画面 10:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

画面 11:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

画面 12:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

画面 13:
```java
package com.tanhu.server.vo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
@Data
@NoArgsConstructor
@AllArgsConstructor
public class VisitorsVo {
    private Long id;
    private String avatar;
    private String nickname;
    private String gender;
    private String[] tags;
    private Integer fateValue;
}
```

画面 14:
```java
//如果redis中存在上一次查询的时间点的话就按照时间查询，否则就按照数量查询
String redisKey = "visitors_" + user.getUserId();
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    //按照数量查询
    this.visitorsApi.topVisitor(user.getId(), num: 6);
    return null;
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 13: PPT 标题为“2.6. MovementsController”，内容为 `VisitorsVo` 类定义。
画面 14: PPT 标题为“2.6. MovementsController”，内容为 `queryVisitorsList` 方法的完整逻辑。

5) 无。
