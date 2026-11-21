# 13.探花功能实现之喜欢功能实现（APP接口服务开发）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\13.探花功能实现之喜欢功能实现（APP接口服务开发）_【海量资源尽在 666java.com】.mp4
- 时长 3分55秒（音频 236s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来编写我们的这个APP所需要的这个服务那么我们在我们的这个today best中呢去添加一个喜欢的这个方法当然这个呢我们也会去参考我们的这个mock接口呢去做一个实现然后呢下面呢我们找到我们这个server这一端然后呢我们找到下面有一个today best Controller然后呢在下面这个位置啊去把它呢拷贝过来
[00:28] 然后我们去来看一下他的一个地址就是传递了一个ID一个log然后ID就是我们的用户的一个ID就是你喜欢那个用户ID就比如说张三登录之后去点击喜欢李四然后like user ID就是李四的那个ID然后我们来看一下这个方法肯定现在没有对吧我们来创建一下
[00:53] 那么这样吧我们就直接点进去吧点进去之后呢我们在我们的讲义中啊直接把它拷贝过来啊就可以了放到下面来然后呢这个是我们的一个Service啊实现起来非常简单那么就是我们调用我们的这个API的这个方法呢就可以了那么下面呢我们把这个API的注进来啊就是叫做Urelec API把它注进来Urelec API然后呢refresh
[01:22] 我们去引入一下引入一下它那应该是这个对吧然后呢我们定一个这个版本Wolfen是1.0.0去做一个引入然后呢下面呢我们就再使用我们的这个就是我们这个UderLike去做一个去做一个这个保存然后呢去传递两个参数一个是UderID一个就是我们LikeUderID
[01:48] 然后呢如果发现了这个ID为空的话那就代表着我们这个保存失败了那我们就return false就可以了那么如果我们的这个去如果它是相互之间保存完成之后啊如果他们互为好友的话那我们就需要去做一个这个注册了对吧那么这个呢我们就需要去使用我们的IM的一个Service然后呢去注册我们的一个这个好友然后呢把它去注册为一个好友了
[02:17] 然后我们就在下面这个位置然后去注我们的imservice把他注进来好然后我们去调用imservice这个方法就可以了那么在这个里面需要做两件事情一个是保存数据到mongoDB
[02:36] 那么另外一个呢就是注册我们的这个好友数据呢到环信啊那么大家在做测试的时候要注意一下这一块呢经常会发生一个404的一个错误原因是什么呢原因是我们可能在测试的时候有一些用户呢并没有去注册到我们的这个环信上面那么他们之间去
[02:57] 注册这个好友关系的时候呢就会报错啊所以说呢这个其实也属于一个正常的一种这个错误大家看到这个404之后的也不要着急那么你可以在环信那个平台呢把这个你要去添加好友的这个对方这个好友啊先添加到这个环信里面那么再去添加就OK了
[03:18] 那么当然了如果是我们去按照正常的流程去先去做一个我们应用的一个注册的话然后呢再去做一个登录的话那么这个时候呢他肯定就会把我们的好友去注册到环境了这个时候就没有问题了只是我们在做测试的时候呢可能会发生这个问题啊好那么呃接下来呢我们就来看一下我们这块的Service啊这块是不是就没有问题了那么其实到这里呢我们这个呃喜欢的这个功能的这个接口呢就搞定了好
[03:48] 那么关于我们这个就是喜欢的一个APP这样应用的一个服务的开发呢那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

