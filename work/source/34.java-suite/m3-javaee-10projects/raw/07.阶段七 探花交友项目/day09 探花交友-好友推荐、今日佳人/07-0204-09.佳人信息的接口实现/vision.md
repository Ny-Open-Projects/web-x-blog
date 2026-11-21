# 画面线理解：09.佳人信息的接口实现

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\09.佳人信息的接口实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:32, 00:57, 01:17, 01:31, 01:49, 02:08, 02:32, 02:52, 03:25, 04:00, 04:24, 04:56, 05:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:14:36

1) 这一组画面整体在讲如何通过模拟接口、服务层代码和 Dubbo 接口实现“今日佳人”功能的前后端数据交互与业务逻辑。

2) 按时间顺序列出每张画面的要点：
画面 1：展示 Typora 文档中“佳人信息”模块的 mock 接口文档，包含接口地址 https://mock.boxuegu.com/project/164/tanhuai/id/personalInfo，以及返回数据示例。
画面 2：在 Advanced REST Client 中查看 mock 接口的请求参数，路径参数 id 示例值为 1，Headers 中包含 Content-Type: application/json 和 Authorization 令牌。
画面 3：继续查看 mock 接口的返回数据部分，但未显示具体内容。
画面 4：在 IntelliJ IDEA 中查看 TodayBestController.java 代码，其中包含 @Value 注解设置默认用户 ID 和推荐用户数，以及 queryTodayBest 方法的业务逻辑。
画面 5：在 Typora 文档中展示 TodayBestService 的代码，包含 queryTodayBest 方法的实现逻辑。
画面 6：在 IntelliJ IDEA 中查看 TodayBestService.java 代码，展示补全用户信息和计算分数的逻辑。
画面 7：在 IntelliJ IDEA 中查看 TodayBestService.java 代码，展示设置分数和返回对象的逻辑。
画面 8：在 IntelliJ IDEA 中查看 RecommendUserService.java 代码，展示 queryRecommendUserList 和 queryScore 方法的实现。
画面 9：在 IntelliJ IDEA 中查看 Dubbo 接口项目结构，展示 RecommendUserApiImpl 类的代码，包含 @Override 注解的 queryWithMaxScore 方法。
画面 10：在 IntelliJ IDEA 中查看 RecommendUserApiImpl.java 代码，展示 queryScore 方法的实现，包含查询推荐用户并返回分数的逻辑。
画面 11：在 Advanced REST Client 中发起对 /movements/visitors 接口的 GET 请求，响应状态为 200。
画面 12：在 Advanced REST Client 中发起对 /tanhuai/personalInfo 接口的 GET 请求，响应状态为 200。
画面 13：在 Genymotion 模拟器中展示“今日佳人”页面，显示用户信息和点赞按钮。
画面 14：在 Typora 文档中展示 recommendUserApi 和 RecommendUserApiImpl 的代码结构，以及 RecommendUserService 的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 4：
```java
@Value("2")
private Long defaultUserId;
@Value("${tanhua.sso.default.recommend.users}")
private String defaultRecommendUsers;

public TodayBest queryTodayBest() {
    //根据token查询当前登录的用户信息
    User user = UserThreadlocal.get();
    TodayBest todayBeat = this.recommendUserService.queryTodayBest(user.getId());
    if (todayBeat == null) {
        todayBeat = new TodayBest();
        todayBeat.setId(defaultUserId);
        todayBeat.setFateValue(95L);
    }
    //补全用户信息
    UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBeat.getId());
```

画面 5：
```java
@GetMapping("/{id}/personalInfo")
public ResponseEntity<TodayBest> queryTodayBest(@PathVariable("id") Long userId) {
    try {
        TodayBest todayBest = this.todayBestService.queryTodayBest(userId);
        return ResponseEntity.ok(todayBest);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 6：
```java
User user = UserThreadlocal.get();
TodayBest todayBest = new TodayBest();
//补全信息
UserInfo userInfo = this.userInfoService.queryById(userId);
todayBest.setId(userId);
todayBest.setAge(userInfo.getAge());
todayBest.setAvatar(userInfo.getLogo());
todayBest.setGender(userInfo.getSex().name().toLowerCase());
todayBest.setNickname(userInfo.getNickName());
todayBest.setTags(StringUtils.split(userInfo.getTags(), ','));
```

画面 7：
```java
double score = this.recommendUserService.queryScore(userId, user.getId());
if (score == 0) {
    score = 98; //默认分值
}
todayBest.setFateValue(Double.valueOf(score).longValue());
return todayBest;
```

画面 8：
```java
public TodayBest queryTodayBest() {
    //如果得分98.2时，需要显示的得分为98
    double score = Math.floor(recommendUser.getScore());
    todayBest.setFateValue(Double.valueOf(score).longValue()); //分值
    todayBest.setId(recommendUser.getUserId()); //UserId
    return todayBest;
}

public double queryScore(Long id, Integer page, Integer pagesize) {
    return this.recommendUserApi.queryPageInfo(id, page, pagesize);
}
```

画面 9：
```java
package com.tanhuai.dubbo.server.api;
import ...
@Service(version = "1.0.0")
public class RecommendUserApiImpl implements RecommendUserApi {
    @Autowired
    private MongoTemplate mongoTemplate;

    @Override
    public RecommendUser queryWithMaxScore(Long userId) {
        Criteria criteria = Criteria.where("toUserId").is(userId);
        Query query = Query.query(criteria).with(Sort.by(Sort.Order.desc("score")));
        return this.mongoTemplate.findOne(query, RecommendUser.class);
    }
}
```

画面 10：
```java
@Override
public double queryScore(Long userId, Long toUserId) {
    Query query = Query.query(Criteria
            .where("toUserId").is(toUserId)
            .and("userId").is(userId));
    RecommendUser recommendUser = this.mongoTemplate.findOne(query, RecommendUser.class);
    if (null == recommendUser) {
        return 0;
    }
    return recommendUser.getScore();
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 1：PPT 标题为“3、佳人信息”，子标题“3.1、mock接口”，包含接口地址和返回数据示例。
画面 5：PPT 标题为“3.3、TodayBestService”，展示 TodayBestService 的代码。
画面 14：PPT 标题为“3.4.1、recommendUserApi”和“3.4.2、RecommendUserApiImpl”，展示接口定义和实现代码。

5) 无。
