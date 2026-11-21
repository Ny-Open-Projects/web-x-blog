# 画面线理解：17.推荐用户列表功能实现之编写业务代码（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\17.推荐用户列表功能实现之编写业务代码（上）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 02:11, 03:23, 04:48, 05:55, 07:04, 09:38, 11:24, 12:35, 13:50, 14:59, 16:28, 17:33, 18:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:28:58

1) 这一组画面整体在讲如何实现一个推荐系统中“今日最佳”功能的后端代码，包括接口定义、服务层逻辑、数据查询和单元测试。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档（Typora）中“3.1、mock接口”部分，包含一个推荐列表的UI截图和mock接口地址：https://mock.boxuegu.com/project/164/interface/api/64561。
画面2：展示mock接口返回的JSON数据示例，包含用户信息如gender、age、tags、faceValue等字段。
画面3：展示IDE中PageResult.java的类定义，包含counts、pagesize、page、list等字段。
画面4：展示TodayBestController.java中@GetMapping("/queryTodayBest")方法，调用todayBestService.queryRecommendUserList。
画面5：展示TodayBestService.java中queryRecommendUserList方法，调用recommendUserService.queryRecommendUserList。
画面6：展示RecommendUserApi接口定义，包含@Reference注解和queryTodayBest方法。
画面7：展示RecommendUserApi接口定义，包含queryTodayBest方法。
画面8：展示Navicat中tb_user_info表结构，包含字段如city、birthday、cover_pic、income、marriage、created、updated等。
画面9：展示课程文档中“3. 推荐列表”部分，包含推荐列表的UI截图。
画面10：展示TodayBestService.java中构建QueryWrapper并根据city、age等条件查询用户信息。
画面11：展示TodayBestService.java中构建QueryWrapper并根据city、age等条件查询用户信息。
画面12：展示TodayBestService.java中将UserInfo转换为TodayBest对象并添加到todayBests列表。
画面13：展示TodayBestService.java中如果未找到推荐用户则创建默认推荐用户。
画面14：展示TestTodayBest.java中测试queryTodayBest和queryRecommendUserList方法。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```json
{
  "gender": "man",
  "age": 24,
  "tags": [
    "单身",
    "本科",
    "颜值担当"
  ],
  "faceValue": 94
}
```

画面3：
```java
package com.tanhua.server.vo;

import ...

@Data
@AllArgConstructor
@NoArgsConstructor
public class PageResult {
    private Integer counts; // 总记录数
    private Integer pagesize; // 页大小
    private Integer pages; // 总页数
    private Integer page; // 当前页码
    private List<?> list; // 列表
}
```

画面4：
```java
@RequestMapping("/queryTodayBest")
@Autowired
private TodayBestService todayBestService;

@GetMapping("/queryTodayBest")
public PageResult queryTodayBest(String token) {
    return this.todayBestService.queryRecommendUserList(queryParam, token);
}
```

画面5：
```java
public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam, String token) {
    User user = this.userService.queryUserByToken(token);
    if (user == null) {
        return null;
    }
    PageInfo<RecommendUser> pageInfo = this.recommendUserService.queryRecommendUserList(user.getId(), queryParam.getPage(), queryParam.getSize());
    List<RecommendUser> records = pageInfo.getRecords();
    return null;
}
```

画面6：
```java
@Service
public class RecommendUserApi {
    @Reference(version = "1.0.0")
    private RecommendUserApi recommendUserApi;

    public TodayBest queryTodayBest(Long userId) {
        RecommendUser recommendUser = this.recommendUserApi.queryWithMaxScore(userId);
        if (null == recommendUser) {
            return null;
        }
        TodayBest todayBest = new TodayBest();
        // 如果分为98.2分，需要显示的分数是98
        double score = Math.floor(recommendUser.getScore());
        todayBest.setFateValue(Double.valueOf(score).longValue()); // 综分值
        return todayBest;
    }
}
```

画面7：
```java
public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam, String token) {
    // 根据token查询当前登录的用户信息
    User user = this.userService.queryUserByToken(token);
    if (user == null) {
        return null;
    }
    PageInfo<RecommendUser> pageInfo = this.recommendUserService.queryRecommendUserList(user.getId(), queryParam.getPage(), queryParam.getSize());
    List<RecommendUser> records = pageInfo.getRecords();
    // 需要查询用户的信息，并且按照条件查询
    List<UserInfo> userInfos = this.userInfoService.queryUserInfolist();
    return null;
}
```

画面8：
```sql
city varchar(10) DEFAULT NULL COMMENT '居住城市',
birthday varchar(10) DEFAULT NULL COMMENT '生日',
cover_pic varchar(10) DEFAULT NULL COMMENT '封面图',
income varchar(10) DEFAULT NULL COMMENT '收入',
marriage varchar(10) DEFAULT NULL COMMENT '婚姻状态',
created datetime DEFAULT NULL,
updated datetime DEFAULT NULL,
KEY `user_id` (`user_id`),
PRIMARY KEY (`id`)
```

画面10：
```java
for (RecommendUser record : records) {
    userIds.add(record.getUserId());
}
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in(column: "user_id", userIds); // 用户id
if (queryParam.getAge() != null) {
    queryWrapper.lt(column: "age", queryParam.getAge()); // 年龄
}
if (StringUtils.isNotEmpty(queryParam.getCity())) {
    queryWrapper.eq(column: "city", queryParam.getCity()); // 城市
}
// 需要查询用户的信息，并且按照条件查询
List<UserInfo> userInfos = this.userInfoService.queryUserInfolist(queryWrapper);
return null;
```

画面11：
```java
queryWrapper.in(column: "user_id", userIds); // 用户id
if (queryParam.getAge() != null) {
    queryWrapper.lt(column: "age", queryParam.getAge()); // 年龄
}
if (StringUtils.isNotEmpty(queryParam.getCity())) {
    queryWrapper.eq(column: "city", queryParam.getCity()); // 城市
}
// 需要查询用户的信息，并且按照条件查询
List<UserInfo> userInfos = this.userInfoService.queryUserInfolist(queryWrapper);
List<TodayBest> todayBests = new ArrayList<>();
for (UserInfo userInfo : userInfos) {
    TodayBest todayBest = new TodayBest();
    todayBest.setUserId(userInfo.getUserId());
    todayBest.setAge(userInfo.getAge());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setNickname(userInfo.getNickName());
    todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar: ','));
    todayBests.add(todayBest);
}
return new PageResult(0, );
```

画面13：
```java
public TodayBest queryTodayBest(String token) {
    // 根据token查询当前登录的用户信息
    User user = this.userService.queryUserByToken(token);
    if (user == null) {
        return null;
    }
    TodayBest todayBest = this.recommendUserService.queryTodayBest(user.getId());
    if (todayBest == null) {
        // 未找到最高分的推荐用户，给出一个默认推荐用户
        todayBest = new TodayBest();
        todayBest.setFateValue(951);
    }
    // 补全用户信息
    UserInfo userInfo = this.userInfoService.queryUserById(todayBest.getUserId());
    if (null != userInfo) {
        todayBest.setAge(userInfo.getAge());
        todayBest.setAvatar(userInfo.getLogo());
        todayBest.setGender(userInfo.getSex().name().toLowerCase());
        todayBest.setNickname(userInfo.getNickName());
        todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar: ','));
    }
    return todayBest;
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT标题为“3.1、mock接口”，下方有推荐列表的UI截图。
画面9：PPT标题为“3. 推荐列表”，下方有推荐列表的UI截图。
画面8：Navicat中显示了tb_user_info表结构，包含字段和注释。

5) 无。
