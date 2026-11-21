# 09.佳人信息的接口实现

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\09.佳人信息的接口实现_【海量资源尽在 666java.com】.mp4
- 时长 5分34秒（音频 335s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下家人信息哦那么在我们首页呢我们去显示了我们的今日家人但是呢我们知道啊在点击之后啊它其实是可以去查看我们这个家人的信息的啊就是我们点击这个位置啊那么所以我们还是需要去开发这样的一个接口那么这个接口呢我们来看一下这是一个就是我们那个家人信息啊这样的一个接口
[00:25] 那么它有一个ID叫做用户ID是在我们的URL里面传递的然后下面是一些返回的数据也是我们一些基本的一些用户的数据这个数据结构跟我们的一个今日家人的结构是一样的所以说我们是需要去再去开发这样的一个接口好,那我们来看一下如何去开发
[00:49] 那么首先呢我们在我们的todaybest Controller中呢去添加一个这个querytodaybest这样的一个方法那我们来看一下啊把它拷贝一下然后呢进入到我们的这个今日家人啊的这个Controller中啊就丢到这个下面来那么在这个里面啊在这个里面呢那么那我们来看一下它呢去呃传递啊传递我们的这个就是呃查询我们今日家人这样的一个
[01:16] 这个详情那么之前是不是我们已经是有这个方法了对吧那我们来看一下那么之前我们是通过这个去做一个这个查询那么我们来看一下那么是在Service中的去传递一个他还需要去写一个这个方法对吧以前的是我们是没有参数的那么现在我们需要去写一个有参数的这样的一个方法那么下面呢我们就把这个方法呢我们也拷贝过来那我们就直接
[01:45] 把它放到下面吧那么我们就来写一个好,那我们来看一下这个里面的一个实现那么根据我们的用户ID然后呢去做一个UseInfo的一个查询这个里面我们这个方法应该是有By ID去做一个查询把我们这个TodayBest这个对象呢去做一个填充那么关键的一点呢是在我们之前的这个查询中我们并没有去查询我们的一个得分
[02:14] 但是现在我们需要去查询这个得分了那我们来实现一下这个方法那么在我们这个叫做recommend user始终做一个实现那么接下来呢我们这样我们就把下面这个也拿过来吧那么当然了我们还是需要先在我们的double的这个就是接口中呢要定义这个方法那回到我们这个double的这个interface中那么找到我们的APIrecommend userAPI里面那么再来去添加这样的一个
[02:44] 方法那么一个是user id一个是to user id然后呢我们去编写它的一个实现啊那么实在照那我们去编写这样的一个实现那我们来看一下这个实现的方法啊那么我们有两个这个条件对吧一个呢是to user id那一个就是我们的这个user id啊这两个这个方法然后这两个参数然后呢去做一个查询最后呢去返回我们这个
[03:11] recommend user score这样的一个得分那么在我们的double接口中提供好之后那么接下来我们就可以去直接是不是去调用它了对吧那我们就这样我们就去直接来调用它吧那我们把这个方法就拷贝过来然后找到我们刚刚在我们的就是recommend找一下Service那么在recommend user Service中然后去把这个方法我们来替一下
[03:40] 就是我们去根据UID和ToUID去做一个这个查询那么这样的话呢我们就查询到我们这个详情了好那么接下来呢我们就把这个服务呢来重启一下然后呢我们来做一个测试OK那么现在我们这个服务呢就已经跑起来了那么接下来呢我们首先呢先来测试一下我们的这个接口那么我们找到我们这个家人信息的这一块那么我们去把它呢丢过来
[04:07] 这个前面有一个斜杠然后我们把这个ID我们换成我们的这个1这个用户走去做一个查询那么其实可以看到这个就是他的一个这个家人的信息对吧然后呢我们就来看一下不是我们不是应该看1应该我们看的是57因为我们的这个今日家人推荐的是57那么去做一个查询那么这个就是他的一个
[04:34] 这样的一个这个数据啊然后它的一个缘分值呢是96那我们就接下来点击一下这个金人佳人这一块点击它那么我就会进入到这个页面啊那么其实可以看到呢上面是显示它的一个这个logo啊图片然后呢下面呢是它的一些这个标签啊呃用户名呢年龄呢然后呢在这块呢是它的一个缘分值啊那么呃刚刚我们其实点击进来之后呢会有个报错大家应该注意到了那么我们来看一下点击它
[05:02] 那么会有一个这个错误这个错误是什么意思呢就是说那么下面其实注意在下面动态这个下面它还会有一些信息就是那么这个用户就是这个用户它发送的一些这个动态那么需要在这块给它显示出来那么这个是另外一个接口一会儿我们来实现这个接口好那么这样的话我们这个家人信息的一个展现那么我们是不是就已经搞定了OK好那么关于我们的这个就是家人信息的一个查询呢
[05:32] 我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

