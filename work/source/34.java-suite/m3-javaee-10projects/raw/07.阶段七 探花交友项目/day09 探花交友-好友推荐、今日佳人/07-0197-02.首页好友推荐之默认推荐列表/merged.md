# 02.首页好友推荐之默认推荐列表

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\02.首页好友推荐之默认推荐列表_【海量资源尽在 666java.com】.mp4
- 时长 7分36秒（音频 456s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来看一下我们的首页的好友推荐那么首先第一呢我们先来做的是他的默认一个推荐的一个列表那么就是说无论我们是去查询我们之前所造的数据还是我们去在后面将要去实现了我们真正的推荐的这个数据
[00:21] 那我们都需要呢去做出这样的一个准备就是说如果查询不到我们的推荐列表的话那我们应该怎么办那我们就应该给出一个默认的一个推荐列表这个呢在我们之前呢是没有做的啊所以说我们来做一下这个功能
[00:37] 那么首先我们在我们的配置文件中我们去配置一下这个叫做default command-use那么这个你可以自己去配我就大概配置了这么多然后我们把它来拷贝一下找到我们这个server这个工程然后找到resource然后下面obligation然后我们就把它加到
[00:57] 再加到这吧因为这个是不是在我们之前是不是我们也添加过一个默认的一个这个今日佳人的一个推荐啊然后呢我们再回到我们的这个代码中啊那么下面呢我们就可以来实现它了那我们把这个呢来拷贝一下
[01:13] 然后找到我们的controllercontroller是叫做todaybest这样的一个Controller然后我们进入它的一个recommend那么就是进用Service去做一个实现那么这个断点就去掉不需要它然后在下面我们就来去注入一下private然后来一个street然后我们就写一个叫什么写一个叫做把它去掉
[01:44] 就写default recommend us然后呢我们写一个这个value然后呢我们就写一个这个dollar打括号写一个它好那么这样的话呢我们是不是就把它呢就注入进来了那么注入进来之后啊那么下面我们就需要在我们的推进的啊这个方法中呢去做一个实现那么可以看到啊就是这个方法了那么我们可以看到之前的逻辑是这样写的那么先去做查询
[02:14] 那么查询到之后呢去拿到recode然后呢去便利这个recode拿到我们所需要的userids这样的一个集合然后呢我们在这个位置就需要去做一个判断了判断什么呢如果未查询到那么需要需要什么呢需要使用我们的一个默认的一个推荐列表那么做这样的一个事情所以说在这个位置啊我们先去做一个判断那么
[02:44] 应该是什么呢用connection utils.isempty那么如果这个record如果是为空的话如果是为空的话那么我们就来去做这样的一个推荐
[03:02] 那么如果为空那么也就是说它是为空的那我们就需要干什么呢去拿到我们上面的一个这个default的一个recommend的us去做一个什么呢这个分割对吧然后呢我们去分割一下吧拿了utils.split它然后呢去做一个逗号的一个分割那么拿到它就比较叫ss吧
[03:30] 然后我们对它去做一个便利做一个这个便利然后我们来看一下那么这个recode它我们来看一下它是一个空的一个集合注意它不是none所以说我们直接往这里面去添加就可以了我们去每循环一次我们就去new一个recommend user这样的一个对象然后我们把它ss加到什么加到recode
[04:00] 哎呀Recon呢点按的去添加一个什么呢Recommend user对象啊去做这样的一个添加啊这样的话就可以了对吧那么接下来呢我们就去来分装我们这个对象首先我们来看一下set一个这个user id啊这个user id那么user id呢就是谁呢就是我们所推荐的这个id对吧那我们就
[04:27] 就是这个s了啊就是这个s那么大家呢要把它转成一个啊none类型按照它这是第一个这个参数那么第二个呢我们需要给它去set一个谁呢set一个to user id推荐给谁那么推荐给是不是就是我们当前这个用户啊那么我们来写一下这个user.getid啊
[04:48] 这是第二个这个参数那么第三个呢我们来看一下它呢是需要给它设置一个这个score就是这个得分那么这个得分呢我们现在肯定是没有的对吧所以说呢我们就可以给它去随机去产生这样的一个得分那么我们就使用这个random有tools然后呢去写一个它所需要的是什么呢是一个double类型对吧那我们就需要给它
[05:16] 点next这个double那么我们就随意设置吧比如说是70到90或者是98之间这样的一个得分那么这样的话是不是基本上就OK了对吧其他资本我们就不需要去做一个添加了可以看一下set什么的ID和date这两个其实我们后面的没有去使用的所以说我们就不需要去做一个这个设置了
[05:42] 那么这个呢其实就是我们默认列表的这样的一个查询啊好那么接下来呢我们就把我们的一个服务呢都跑起来那我们来测试一下啊那么我们还是呢先找到我们的这个double啊这个服务先把它呢先跑起来哎找到它呃然后呢我们去做一个这个启动啊做一个启动呃然后呢把sso呢也跑起来上面是不是有啊啊把sso跑起来
[06:12] 稍等一下把SSO也跑起来然后我们再把我们这个server就debug就跑起来好那我们来等待它的一个启动好那么现在我们这个服务就已经都跑起来了那么接下来我们先把之前的这个common的user这张表我们先给它清空就代表着我们就现在没有数据了然后我们刷新看一下就没有数据了
[06:35] 然后呢我们去需要登录一下那么这个呢我都已经登录好了发送验证码然后登录然后呢我们直接去做一个查询那么其实可以看到呢是不是他已经拿到这个数据了对吧然后呢他是随机去产生了一些这个就是缘分值啊那么是95啊95 94啊等等啊就是我们刚刚所设置的一些
[06:59] 这个数据啊然后呢其实可以看到跟我们之前所返回的这个结构呢是一样的只是说我们给他添加了一个这个默认的这样的一个推荐列表的一个逻辑啊OK好那么下面我们来看一下这个讲义的一个实现那么这个实现逻辑跟我们是一样的其实主要逻辑呢是在这啊添加了一个他然后呢下面做测试那么可以看到这样的一个结果啊是OK的啊没有问题
[07:24] 好嘞好那么这个呢其实就是啊我们所讲的这个什么呢我们默认的一个推荐列表好那么关于我们这个默认的一个推荐列表的一个讲解那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 IntelliJ IDEA 中开发一个推荐系统服务，包括在服务层构建推荐用户列表、处理空结果的默认推荐逻辑、以及使用 Dubbo 接口定义和测试接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示项目结构，选中了 `my-tanhua-server` 模块，准备进入服务层代码。
画面 2: 在 `TodayBestService.java` 中，展示 `queryRecommendUserList` 方法的实现，其中包含根据用户 ID 查询推荐用户列表的逻辑。
画面 3: 在 `TodayBestService.java` 中，展示 `queryTodayBest` 方法，用于查询当天最佳用户，并在无结果时创建默认用户对象。
画面 4: 在 `TodayBestService.java` 中，展示 `queryRecommendUserList` 方法，其中包含处理空推荐列表的逻辑，使用 `ArrayList` 存储用户 ID。
画面 5: 在 `TodayBestService.java` 中，展示 `queryRecommendUserList` 方法，光标位于 `if (CollectionUtils.isEmpty(records))` 语句，准备添加默认推荐用户逻辑。
画面 6: 在 `TodayBestService.java` 中，展示 `queryRecommendUserList` 方法，光标位于 `for (String s : ss)` 循环，准备创建 `RecommendUser` 对象。
画面 7: 在 `TodayBestService.java` 中，展示 `queryRecommendUserList` 方法，光标位于 `for (String s : ss)` 循环，弹出 `RecommendUser` 类的自动补全建议。
画面 8: 在 `TodayBestService.java` 中，展示 `queryRecommendUserList` 方法，光标位于 `for (String s : ss)` 循环，弹出 `RecommendUser` 类的自动补全建议，显示 `setToUserId` 方法。
画面 9: 在 `RecommendUser.java` 文件中，展示 `RecommendUser` 类的定义，包含 `setUserId`、`setScore` 等方法。
画面 10: 在 `my-tanhua-dubbo-interface` 模块中，展示 `RecommendUser` 类的定义，包含 `setUserId`、`setScore` 等方法。
画面 11: 在 `DubboApplication.java` 文件中，展示 Spring Boot 启动类，包含 `@SpringBootApplication` 注解。
画面 12: 在 Advanced REST Client 中，展示发送 GET 请求，请求头包含 `Authorization`，响应状态为 200。
画面 13: 在 Typora 编辑器中，展示 `day09 详义.md` 文件，内容为 `queryRecommendUserList` 方法的伪代码，包含 `setScore` 方法的调用。
画面 14: 在 Typora 编辑器中，展示 `day09 详义.md` 文件，内容为 `queryRecommendUserList` 方法的伪代码，包含 `setScore` 方法的调用，显示 `RecommendUser` 对象的 JSON 格式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getId());
if (null != userInfo) {
    todayBest.setAge(userInfo.getAge());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setNickname(userInfo.getNickName());
    todayBest.setTags(StringUtils.split(userInfo.getTags(), separatorChar, ','));
}
return todayBest;

public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam) {
    User user = UserThreadLocal.get();
    PageInfo<RecommendUser> pageInfo = this.recommendUserService.queryRecommendUserList(user.getId());
    List<RecommendUser> records = pageInfo.getRecords();
```

画面 3:
```java
TodayBest todayBest = this.recommendUserService.queryTodayBest(user.getId());
if (todayBest == null) {
    todayBest = new TodayBest();
    todayBest.setId(defaultUserId);
    todayBest.setFateValue(95L);
}
```

画面 4:
```java
public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam) {
    User user = UserThreadLocal.get();
    PageInfo<RecommendUser> pageInfo = this.recommendUserService.queryRecommendUserList(user.getId());
    List<RecommendUser> records = pageInfo.getRecords();
    if (records.isEmpty()) {
        List<Long> userIds = new ArrayList<>();
        for (RecommendUser record : records) {
            userIds.add(record.getUserId());
        }
    }
```

画面 5:
```java
public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam) {
    User user = UserThreadLocal.get();
    PageInfo<RecommendUser> pageInfo = this.recommendUserService.queryRecommendUserList(user.getId());
    List<RecommendUser> records = pageInfo.getRecords();
    if (CollectionUtils.isEmpty(records)) {
```

画面 6:
```java
if (CollectionUtils.isEmpty(records)) {
    String[] ss = StringUtils.split(defaultRecommendUsers, separatorChar, ',');
    for (String s : ss) {
        RecommendUser recommendUser = new RecommendUser();
```

画面 7:
```java
if (CollectionUtils.isEmpty(records)) {
    String[] ss = StringUtils.split(defaultRecommendUsers, separatorChar, ',');
    for (String s : ss) {
        RecommendUser recommendUser = new RecommendUser();
```

画面 8:
```java
if (CollectionUtils.isEmpty(records)) {
    String[] ss = StringUtils.split(defaultRecommendUsers, separatorChar, ',');
    for (String s : ss) {
        RecommendUser recommendUser = new RecommendUser();
        recommendUser.setUserId(user.getId());
        recommendUser.setScore(RandomUtils.nextDouble(70, 99));
        records.add(recommendUser);
    }
}
```

画面 9:
```java
public class RecommendUser {
    private Long id;
    private Long userId;
    private Double score;
    private String avatar;
    private String nickname;
    private Integer age;
    private List<String> tags;
    private Integer fateValue;
    private Date updatedAt;
    private Date createdAt;
    private String gender;
    private String mobile;
    private String password;
    private String email;
    private String description;
    private String location;
    private String job;
    private String education;
    private String company;
    private String department;
    private String position;
    private String title;
    private String website;
    private String blog;
    private String wechat;
    private String qq;
    private String weibo;
    private String zhihu;
    private String github;
    private String twitter;
    private String linkedin;
    private String facebook;
    private String instagram;
    private String snapchat;
    private String tiktok;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String dailymotion;
    private String twitch;
    private String youtube;
    private String vimeo;
    private String d

