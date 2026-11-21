# 画面线理解：13.探花功能实现之喜欢功能实现（APP接口服务开发）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\13.探花功能实现之喜欢功能实现（APP接口服务开发）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:18, 00:28, 00:55, 01:03, 01:10, 01:22, 01:29, 01:51, 02:19, 02:29, 02:36, 03:36, 03:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:31:44

1) 这一组画面整体在讲什么（一句话）：
演示一个点赞/不喜欢功能的后端实现，包括单元测试、Controller、Service 层代码以及相关配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示单元测试类 TestUserLikeApiImpl，包含三个测试方法：testSave、testIsMutualLike、testDeleteUserLike，用于验证点赞、判断互粉、取消点赞功能。
画面2：展示 TestUserLikeApiImpl 类中 testIsMutualLike 方法的测试用例，调用 isMutualLike 方法并打印结果。
画面3：展示 TodayBestController 类中的 likeUser 方法，用于处理点赞请求，调用 todayBestService.likeUser 方法。
画面4：展示 TodayBestService 类中的成员变量，包括 UserService、UserInfoService、RecommendUserService 等，以及默认用户ID、推荐用户列表、SSO URL 等配置。
画面5：展示 TodayBestService 类中的 likeUser 方法，用于处理点赞逻辑，调用 userLikeApi.saveUserLike 保存点赞记录，调用 isMutualLike 判断是否互粉，调用 imService.contactUser 发送好友关系通知。
画面6：展示 TodayBestService 类中的 queryTodayBest 方法，用于查询今日最佳用户，调用 recommendUserService.queryTodayBest 方法。
画面7：展示 TodayBestService 类中的 queryTodayBest 方法，用于查询今日最佳用户，调用 recommendUserService.queryTodayBest 方法。
画面8：展示 TodayBestService 类中的 queryTodayBest 方法，用于查询今日最佳用户，调用 recommendUserService.queryTodayBest 方法。
画面9：展示 TodayBestService 类中的 likeUser 方法，用于处理点赞逻辑，调用 userLikeApi.saveUserLike 保存点赞记录，调用 isMutualLike 判断是否互粉，调用 imService.contactUser 发送好友关系通知。
画面10：展示 TodayBestService 类中的 queryTodayBest 方法，用于查询今日最佳用户，调用 recommendUserService.queryTodayBest 方法。
画面11：展示 TodayBestService 类中的 likeUser 方法，用于处理点赞逻辑，调用 userLikeApi.saveUserLike 保存点赞记录，调用 isMutualLike 判断是否互粉，调用 imService.contactUser 发送好友关系通知。
画面12：展示 IMService 类中的 contactUser 方法，用于处理好友关系通知，调用 usersApi.saveUsers 保存用户数据，调用 restTemplate.postForEntity 发送 HTTP 请求。
画面13：展示 IMService 类中的 contactUser 方法，用于处理好友关系通知，调用 usersApi.saveUsers 保存用户数据，调用 restTemplate.postForEntity 发送 HTTP 请求。
画面14：展示 TodayBestService 类中的 likeUser 方法，用于处理点赞逻辑，调用 userLikeApi.saveUserLike 保存点赞记录，调用 isMutualLike 判断是否互粉，调用 imService.contactUser 发送好友关系通知。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
public class TestUserLikeApiImpl {

    @Autowired
    private UserLikeApi userLikeApi;

    @Test
    public void testSave(){
        this.userLikeApi.saveUserLike(1L,2L);
        this.userLikeApi.saveUserLike(2L,3L);
        this.userLikeApi.saveUserLike(2L,1L);
    }

    @Test
    public void testIsMutualLike(){
        System.out.println(this.userLikeApi.isMutualLike(1L,2L));
        System.out.println(this.userLikeApi.isMutualLike(2L,1L));
        System.out.println(this.userLikeApi.isMutualLike(1L,3L));
    }

    @Test
    public void testDeleteUserLike(){
        System.out.println(this.userLikeApi.deleteUserLike(1L,2L));
        System.out.println(this.userLikeApi.deleteUserLike(2L,1L));
    }
}
```

画面2：
```java
@Test
public void testIsMutualLike(){
    System.out.println(this.userLikeApi.isMutualLike(1L,2L));
    System.out.println(this.userLikeApi.isMutualLike(2L,1L));
    System.out.println(this.userLikeApi.isMutualLike(1L,3L));
}
```

画面3：
```java
@PostMapping("/like")
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

画面4：
```java
@Autowired
private UserService userService;

@Autowired
private UserInfoService userInfoService;

@Autowired
private RecommendUserService recommendUserService;

@Value("2")
private Long defaultUserId;

@Value("http://127.0.1:18080")
private String ssoUrl;

@Value("2,3,4,5,6,7,8,9,10,11,12,13")
private String defaultRecommendUsers;

@Autowired
QuestionService questionService;

private static final ObjectMapper MAPPER = new ObjectMapper();
```

画面5：
```java
public Boolean likeUser(Long likeUserId) {
    User user = UserThreadLocal.get();
    String id = this.userLikeApi.saveUserLike(user.getId(), likeUserId);
    if (StringUtils.isEmpty(id)) {
        return false;
    }
    if (this.userLikeApi.isMutualLike(user.getId(), likeUserId)) {
        //相互喜欢成为好友
        this.imService.contactUser(likeUserId);
    }
    return true;
}
```

画面6：
```java
@Reference(version = "2.0.0") //2.0.0是ES版本的实现，1.0.0是MongoDB版本的实现
private UserLocationApi userLocationApi;

public TodayBest queryTodayBest() {
    //根据token查询当前登录的用户信息
    User user = UserThreadLocal.get();
    TodayBest todayBest = this.recommendUserService.queryTodayBest(user.getId());
    if (todayBest == null) {
        //未找到最高赞的推荐用户，给出一个默认推荐用户
        todayBest = new TodayBest();
        todayBest.setUserId(DefaultUserId);
        todayBest.setFavValue(55L);
    }
    return todayBest;
}
```

画面7：
```java
@Reference(version = "2.0.0") //2.0.0是ES版本的实现，1.0.0是MongoDB版本的实现
private UserLocationApi userLocationApi;
```

画面8：
```java
@Reference(version = "2.0.0") //2.0.0是ES版本的实现，1.0.0是MongoDB版本的实现
private UserLocationApi userLocationApi;
```

画面9：
```java
public Boolean likeUser(Long likeUserId) {
    User user = UserThreadLocal.get();
    String id = this.userLikeApi.saveUserLike(user.getId(), likeUserId);
    if (StringUtils.isEmpty(id)) {
        return false;
    }
    if (this.userLikeApi.isMutualLike(user.getId(), likeUserId)) {
        //相互喜欢成为好友
        this.imService.contactUser(likeUserId);
    }
    return true;
}
```

画面10：
```java
public TodayBest queryTodayBest() {
    //根据token查询当前登录的用户信息
    User user = UserThreadLocal.get();
    TodayBest todayBest = this.recommendUserService.queryTodayBest(user.getId());
    if (todayBest == null) {
        //未找到最高赞的推荐用户，给出一个默认推荐用户
        todayBest = new TodayBest();
        todayBest.setUserId(DefaultUserId);
        todayBest.setFavValue(55L);
    }
    return todayBest;
}
```

画面11：
```java
public Boolean likeUser(Long likeUserId) {
    User user = UserThreadLocal.get();
    String id = this.userLikeApi.saveUserLike(user.getId(), likeUserId);
    if (StringUtils.isEmpty(id)) {
        return false;
    }
    if (this.userLikeApi.isMutualLike(user.getId(), likeUserId)) {
        //相互喜欢成为好友
        this.imService.contactUser(likeUserId);
    }
    return true;
}
```

画面12：
```java
private AnnouncementService announcementService;

public Boolean contactUser(Long userId) {
    //需要做2件事：1、保存数据到MongoDB；2、好友关系注册到环信
    Users users = new Users();
    users.setUserId(UserThreadLocal.get().getId());
    users.setFriendId(userId);
    // 1、保存数据到MongoDB
    this.usersApi.saveUsers(users);
    // 2、好友关系注册到环信
    String url = ssoUrl + "/user/huanxin/contacts/" + users.getUserId() + "/" + users.getFriendId();
    ResponseEntity<Void> responseEntity = this.restTemplate.postForEntity(url, request, Void.class);
    if (responseEntity.getStatusCodeValue() == 200) {
        return true;
    }
    return false;
}
```

画面13：
```java
private AnnouncementService announcementService
