# 17.推荐用户列表功能实现之编写业务代码（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\17.推荐用户列表功能实现之编写业务代码（上）_【海量资源尽在 666java.com】.mp4
- 时长 18分30秒（音频 1110s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下推荐列表那么推荐列表呢是指下面的这一块这个内容啊那么列表呢显然是会有一个分页的一个效果啊那么其实我们可以来分析一下这个数据啊就是其实它和我们这个今日佳人的这个数据的来源是一样的只是呢我们今日佳人中呢是选用了它这个就是缘分值最高的这个用户而我们下面呢是需要把
[00:29] 所有推荐的一些用户的列表呢给它去展现出来那么这样的话其实就比较容易去实现了那么接下来呢我们首先呢来看一下我们这个Mock的一个接口那么我们来打开这个地址我们来看一下啊那么这个我们需要登录一下然后呢我们来找到啊找到我们的这个项目然后呢在这个下面呢有一个叫做这个交友下面的是在啊
[00:57] 那么默克地址呢是这样的一个地址啊就是recommendation然后呢请求参数呢除了这个请求头之外啊也会有一些请求的一些这个参数那么包括有这个page啊当前页page size这个就返回多少条数据还有gender还有性别还有他的近期登录的时间呢还有年龄呢居住地呢
[01:25] 学历等等这样的一些查询条件为什么会有这么多些条件呢原因是在我们的这一块会有一个筛选但是目前还暂时没有做实现只是告诉大家我们可以这样去做那么这个就是我们的一个MOOC这样的一个接口然后它所响应的一个数据是有这样的一个数据这个Counts是总记录数还有Page Size页面大小
[01:54] 然后还有pages还有items就是我们的列表的数据了这个里面其实就是前面我们的今日佳人的这样的一些数据结构OK好那么接下来我们就来做一个具体的实现好嘞那么下面首先我们需要对我们的查询的参数去构建它的一个对象就是前面我们所看到的查询的参数
[02:22] 那我们来构建一个对象那我们把这个对象呢来拷贝一下那么我们把它丢到哪里呢丢到我们的这个VO里面来丢到这儿那么这个呢是一个recommend user query那么这个是不是要跟我们的这个接口的要对应起来对吧一一做一个对应啊这个呢我们就补一个给去写了然后呢我们就直接把它拷贝过来了
[02:48] 然后下面我们来看一下结果对象那么结果对象就是刚才所看到的这一段所以我们去来定义一个结果对象那么同样我们也把它拷过来那么这个结果对象叫做PageResult有Counts,PageSize,PageItems这样的一个对象然后Items中所存放的就是谁其实就是我们
[03:13] today best这样的一个对象存储它OK好那么接下来呢我们就可以来开发它的一个业务功能了那么接下来呢我们就来编写具体的这个代码逻辑啊那我们同样呢是把它写到这个Controller中或者我们去单独再写一个也可以啊只要我们去符合这个URL规则啊就可以了那么我们就直接写到这个里面来吧
[03:39] 那么我们就下面写一个public返回值呢叫做page什么呢result啊这样的一个对象啊然后呢我们写一个叫做query什么呢recommend对吧recommend your list啊list那么这样的一个列表啊呃那么我们首先呢把它标记为这是一个get mapping然后呢呃它的一个这个路径的规则呢我们来拷贝一下啊那么就在这个位置啊
[04:09] 它也是这个探花啊下面的它然后呢我们需要呢有两个参数那么第一个参数呢叫做什么呢叫做recommendrecommend我们这个叫query param我们的查询参数啊那么还有一个呢就是我们的这个token啊这个呢也是需要的好嘞好那么哎少了一个少了一个我们这个参数啊好那么这样的话呢我们是不是就勾到完成了
[04:36] 那么接下来我们就可以通过我们这个Service然后去做一个query查询然后我们把这两个参数给它传递过去一个是query param还有一个就是token那么它的返回值那就返回这个就是pay走的route就可以了那么接下来我们去在Service中的去创建我们这个方法就ok好那么我们来看一下这个怎么去做
[05:04] 那么首先第一呢它呢也是需要通过我们这个token是不是去查询我们当前的一个登录信息啊对吧啊查询登录信息这是第一个啊我们要做的这个事情那么接下来呢我们就需要去查询我们的一个这个列表那我们调用什么呢我们这个recommend user Service点那么我们还得去写一个啊就叫什么呢呃我们就写一个query吧
[05:33] query这个recommendrecommend your list那么我们就写它然后呢我们去传递一个谁呢叫做不能用list应该就your.get什么id一个是id还有谁呢就是我们的query param中的什么呢get page和谁呢点get page size
[06:00] 那么把这两个传递过去因为我们肯定要去做分页对不对啊那么它的返回值呢我们来看一下啊那么我们这样我们先把这个方法创建出来啊创建出来那么我们来看一下它的返回值先返回呢啊后面我们再去做一个修改那么这个里面怎么做呢我们将调用我们这个就是double中的这个服务然后呢去做一个query啊query page info
[06:26] 然后需要有三个参数对吧第一个参数就是 id那第二个参数是配置配置那第三个参数就是配置size那么这三个参数那么它就不需要做一些其他逻辑的处理了那我们直接返回是不是就可以了对吧我们做一个做一个return做一个return做一个returnreturn它
[06:52] 那么return它的返回值是一个叫做page info对吧所以我们这个位置要写一个page什么infook好那么这样的话我们在这个中的逻辑就处理完成了那么接下来我们就在我们这个里面去处理当然了我们在这个位置也可以去把它跟上面这个一样可以去完善一下就是说我们可以这样来做那我们我们
[07:21] 还是把它返回吧返回可能处理会比较方便一点那么我们这个方法就直接就返回PageInfo了把其他的一些处理逻辑啊我们就丢到在我们的这个Today这个Service中的去做一个处理那我们来找一下我们这个Service啊在这个里面去做处理了那么我们就不到那个Service中做处理了因为不属于它的一个范畴嘛那么这个是我们的一个PageInfo啊那么有了PageInfo之外呢我们就可以去拿到这里面的一些
[07:51] 这个内容了你比如说呢我们可以拿到这个records那么它呢是我们的一个推荐的一个这个用户啊用户这样的一个列表那么我们要知道的是呢这个用户中啊它只有什么呢这个ID啊只有这个ID那么我们其实呢还是需要去查询一些其他的一些这个信息信息的对不对所以说呢我们要明白一点就是说
[08:19] 我们需要查询用户的一些这个信息啊并且呢我们要按照我们的一些条件啊去做一些这个查询那么什么意思啊就是说我们有可能在这个位置啊查询到有10条数据啊10条数据但是呢这10条数据它符合我们这个查询条件的可能只有什么呢三条啊只有三条那我们最终响应的是三条数据
[08:47] 而不是这10条这个大家能够理解了吧所以说呢在这个位置我们需要构造我们的一个查询条件那么这个查询条件那么我们应该怎么样去做呢那我们还是需要通过我们的这个mybatties去做一个查询了那么我们去写一个叫做什么呢就叫user info这样的一个Service去做一个这个queryqueryuser info什么呢
[09:17] infoinfo什么呢list我们需要去查询这样的一个list那么这个list怎么去写呢我们来看一下那么它的这个返回值我们就期望它所返回的就是一个谁呢我们这个listlist谁呢就叫userinfo这样的一个对象就叫userinfo死吧
[09:41] 那就他啊那么他的一个查询呢我们其实是需要他去根据一个什么呢我们的一个参数吧去做一个查询那么这样我们先把这个方法呢我们先定义出来吧那么来看一下那我们把这个方法呢先定义出来
[10:00] 那么我们来看一下它的参数啊应该是一个什么样的一个参数啊那么在这个位置呢我们应该调用的是谁呢就是this.map.selectlist所以它是需要一个什么呢query loop或者说loop对象啊所以说呢在这个位置啊我们定义一个叫做query loop这样的一个对象那么我们把它定义出来然后呢我们把这个query loop传给它
[10:26] 那就可以做一个这样的一个查询了那么这个查询呢就是在查询什么呢我们的查询我们的推荐用户的一个哎这个叫什么查询我们的这个就是用户信息啊列表这样的一个查询那么有了这个查询之后呢我们在这个Service中啊那么就可以去把传递我们这个query的一个wrap对象啊所以我们可以去定义一个什么呢query啊wrap对象
[10:56] 那么这个t呢就是我们的user info啊在哪个对象那么我们写一个query啊rop对象等于new一个queryrop对象好那么我们把这个queryrop给它传递过去那么接下来呢我们需要给它去设置我们的查询条件啊那么首先呢是需要去印一个谁呢就是我们的一个这个呃我们来看一下表啊那么在我们的user info中啊有一个什么的user id啊user id这个字段
[11:25] 那么首先稍微等一下这个有点卡了那么这个user id他应该是应一个谁应该是有一个集合对不对所以在上面这个位置我们要拿到推荐用户中的一个用户的一个id的一个列表那么我们所以需要去定义一个这个lang类型的一个什么的user iduser id s等于new一个array list
[11:53] 然后呢我们对它去做一个便利便利records然后呢我们把这个url urlids.and去添加一个record.get什么get这个urlid那么拿到这个urlid之后呢我们就可以把它呢传递到这儿来这个呢就是我们的一个条件对吧就是我们的一个这个id就是
[12:19] 我们的一个用户ID啊用户ID这样的一个条件那么这个是我们的必须的一个条件对吧那么其实呢我们还需要有一个就是我们前面说过在在我们这个位置啊就是在前面这个位置呢可能会有一些其他的一些查询的条件比如说像年龄呢呃城市呢啊等等那么所以这个位置还可以去构造啊那我们就简单的来写这么几个吧比如说啊我们去写一个这个年龄啊那么我们去做一个判断
[12:49] 那么如果我们这个叫做query param点get什么a者然后呢如果它不等于none的话不等于none就代表着它是不是已经是有这个传入值了对吧你看它的这个a者默认应该是none那么我们就在这个位置去判断那么如果它不等于none的话那我们就需要给queryquery wrap去做一个什么呢
[13:19] lt对吧就是小于对吧那么那么就小于吧直接来写他就是比如说age然后呢去写一个谁呢就是我们这个叫做queryapparum.getage这就是一个条件了这个就是我们的一个年龄啊这样的一个条件那么当然了比如说其他也可以啊就是我们就写两个吧能够代表这个意思啊大家就能够理解了点什么呢is notnotempty一个叫做
[13:47] query param.get city就是我们的一个程式那么如果说这个不为空的话那我们还是需要给它去应该是wrap对象然后去EQ去等于我们的一个city然后它EQ谁就是我们这个query param.get city这样的话就OK了对吧好那么我们来看一下我们的表结构对吧
[14:16] 就是我们这个居住这个城市啊只要相等就可以了当然这个我们肯定是需要去做这样的一个判断啊做这样的判断那么接下来呢我们就需要来处理我们这个集合了那么我们去写一个这个去做一个循环啊然后呢我们需要去每循环一个就需要去构造一个我们的一个today best这样的一个对象那我们就需要在上面呢先定义这样的一个集合了那么叫做today
[14:45] today bests等于new一个reve list然后我们就需要在这个里面去定义我们的对象然后today bests等于new一个对象好那么接下来我们就把它去加进去点按的去加一个today bests那么接下来在这个中我们就需要去给它分装一些
[15:10] 它的一些这个数据了那么分装数据呢就和我们这面是一样的了我们就把这个就拷过来了来看一下啊那么这个UraInfo那么当然了这个today中呢还有一个点哎少一个谁呢set一个ID啊这个ID那其实就是我们的用户ID那就是UraInfoUraInfo.get什么呢UraID啊把它设置进去那么这样的话呢我们这个today best这个对象呢
[15:39] 就已经设置完成了把一些这个内容都已经设置好了那么就最后是不是就可以去做一个返回了对吧那么最后返回呢我们最后应该是去new一个所以呢我们的page result一个对象那么要注意啊这个page result是不是有这么几个这个参数啊对吧那我们来一起来设置一下啊那么首先第一个呢是数据总条数那么要说明的一点是我们数据总条数呢我们不需要去做一个这个设置啊
[16:08] 那我们就直接给他去什么呢就设置一个0啊就可以了为什么不需要设置呢原因是在我们前端呢我们不需要这个总条数的一个计算但是呢我们这个这个支段呢还需要去做一个响应这个返回那么第二个这个参数呢哎第二我们来看一下啊第二个这个参数啊我们来打开看一下啊那么第二个这个参数呢是page size那么page size呢那就是我们这个叫做什么呢queryquery payment
[16:37] 中的这个配置赛对吧那第三个参数我们来看一下啊第三个参数那就是什么呢配置是我们的一个总页数对吧那么总页数呢我们给他来设置一下那么哎我们来看一下啊这个是配置result啊result中我们看有没有这个是一个总页数啊
[16:59] 那么总页数其实我们也是不需要的对吧那我们就直接给它返回0吧然后呢因为我们没有总条数我们也计算不出这个总页数所以就设置为0那么还有什么呢还有一个就是Pager当前页那我们就设置一个当前页那么就是一个QueryParam.get什么Pager那第三个这个参数呢就是我们TodayBest这个集合了那这样的话呢是不是就设置完整了对吧
[17:26] OK好那么接下来呢我们可以来测试一下这个方法看是否能够达到我们这个预期然后呢我们来看一下结果啊那么我们在我们的测试用力中呢来测一下那我们把这个测试用力呢就拷贝一下来修改一下啊好那么我们去查询它的一个这个叫list对吧然后呢我们去做这样的一个查询点queryquery一个它
[17:54] 首先这个参数呢我们可以去new一个就是我们可以不设置参数对吧然后去new一个它然后呢我们去传递这个token进去这样的话呢就可以去做一个查询了OK好那么我们把这个结果呢稍微来处理一下那么我们去有一个叫做page result然后呢我们就把这个page result打印出来吧这样的话也可以看到这个结果对不对OK好那么
[18:23] 这样的话我们就完成了一个测试了好我们来执行一下来等待它的一个执行

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

