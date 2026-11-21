# 07.谁看过我实现之app接口服务

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\07.谁看过我实现之app接口服务_【海量资源尽在 666java.com】.mp4
- 时长 10分58秒（音频 658s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来实现我们的谁看过我的这个接口首先呢我们来看一下我们的这个Mock接口那么打开我们来看一下啊就是这样的一个这个接口在Movements下面有一个Vistos然后呢下面它的请求参数啊是没有的就是根据我们Token啊去查询就可以了然后下面是我们的返回的数据啊就是我们的一些基本的一些这个数据了
[00:25] 好那么接下来呢我们就来去实现一下它啊那么首先呢在我们的这个movements Controller中去编写啊这样的一个这个Controller的一个方法那么我们来拷贝一下然后呢我们找到我们的这个就是server哎找到在下面啊serverserver下面呢找到我们那个Controller啊就是movements Controller那么在这movements Controller然后呢我们就把它加到最下面来啊加到这个位置来
[00:56] 好嘞那么它这个位置呢是需要一个vist这个VO这个对象是吧那么我们来给它去去找一下这个对象啊那我们来看一下讲义中啊有没有没有这个对象那么我们来找一下好那么我呢去给大家找了一下这个VO这个对象把这个对象呢我们来拷贝一下啊拷贝到这个里面来这个对象呢就是按照我们的这个接口的一个响应的一个数据结构啊所定义的这样的一个对象
[01:24] 好嘞那么这个呢就ok啊然后呢我们在这个里面呢肯定他这个啊把这个包导入定来也ok然后呢我们接下来呢在我们这个Service中啊那我们来实现我们这个方法好那我们来把这个放大一下呃然后呢我们来点中它然后呢去create这样的一个方法啊好那么在这个里面我们来看一下怎么去做啊那么首先呢我们肯定是需要这个user的对吧那么user等于这个usersadeloca.get
[01:54] 去获取到我们当前这个U的对象那么接下来呢我们就来做一个具体的一个这个实现那么首先呢我们是需要把我们的那个Vist然后呢API呢注入进来那么我们先来做这件事情那我们写到这个上面吧那么我们叫VistVist然后呢我们有一个叫做API然后呢我们把它呢就注入进来
[02:22] 注入进来那么reface然后这个版本同样也是1.0.0这样的一个版本那么下面我们就通过我们Vist API然后去做一个查询让我们来看一下我们就要用vist.api.top
[02:44] 那么注意了那么在这个位置是不是有两个啊这个方法一个呢是根据number一个呢是根据这个date做查询所以说呢我们必然这个位置啊是需要去做一个判断那么前面呢我们也说过啊那么我们这个查询时间点呢我们是需要把它去存储起来的是不是啊所以说我们应该先做什么事情啊就是说那我们先应该通过我们的一个readies的一个template然后呢我们去做一个查询对吧
[03:13] 比如说呢我们去先去查询那么如果有这个时间那我们就按照这个时间去做一个查询如果没有的话那我们就按照数量去做一个查询好的我们写一个这个注释啊那么接下来我们要实现的就是什么呢就是那么如果我们的redis中存在我们上一次查询的时间时间点的话对吧那么就这么按照时间查询
[03:44] 否则呢就按照什么按照我们的一个数量啊查询好大概是这样的一个这个情况啊然后呢接下来呢我们定义我们的一个redis的一个key啊它呢等于什么呢我们就把它等于叫这个我们叫这个vist吧it然后呢然后呢vist然后呢我们下滑线去跟一个所以呢我们的一个usr id因为每一个用户肯定都需要去
[04:13] 记录自己的一个这样的一个信息对吧然后呢我们去做一个get杀群那么他拿到了这个值那么我们就要date吧那么我们去对这个date呢去做一个判断啊如果我们的有tils然后呢我们去使用它点那么我们这个之前这个有tils是不是用的有问题啊那我们应该是用apache下面的这个啊那我们把上面那个去调一下
[04:42] 那么在上面的这个里面来那么把它就去掉我不使用它然后我们就直接来导入我们Apache里面的包如果它为空那么我们就需要去查询什么按照我们的一个按照数量查询我们就叫ris.vistoapi.top是不是根据第一个来
[05:10] 那么这个UID呢就是U的点getID那么第二个参数呢是number那么查几条呢我们可以查五条查十条都可以那么随便吧我查六条啊这个我们可以随意去写啊当然了这个我们需要和产品经理是不是确认一下对吧那么如果要是不为空的话那我们就按照什么就需要按照我们的一个时间啊进行查询
[05:34] vist.top然后呢去这个做这个时间啊u的点get id然后呢这个时间呢就是我们所拿到的这个时间那我把它去转一下啊哎那个叫对等把它去转一下好那么这样的话呢我们就会得到我们的这个集合对吧那么我们就来定义一下吧这个集合那么就要就叫vist或者vist这个list都可以啊那么我们就把它定义到上面来
[06:06] 然后呢这个Vistos等于它然后呢或者等于下面的它好那么这样的话呢我们是不是就完成了这个查询那么下面呢我们需要做一个判断就是我们通过一个Connects UtilsEasyAperture那么如果我们这个Utils是不是也是导致有点问题那么把这个呢我们不要使用这个double里面的那我们呢去使用的是就是我们这个Apache下面的它
[06:36] 如果我们这个vsts为空的话那我们就什么呢直接return一个我们空的一个集合就可以了用connections.util.connections.connections.然后呢empty一个list
[06:54] 返回一个空的一个集合这样的话就保证我们不会前端就不会去报错好那么接下来我们最终需要返回的是vist这个VO那么这个VO里面有一些关于用户的信息所以我们还需要去查询用户的信息了那我还是先要去拿到用户的一个ID所以说我们在这块写一个叫UO的IDS等于new一个revealist然后我们去做一个便利便利我们的vist
[07:22] 然后我们用的ids.and添加一个vist点get什么呢get我们这个就是vist id就是访客的 id我们是要拿到访客的一些信息那么下面我们就调用list.usinfo servicequeryusinfo by list我们需要传递一个叫做queryqueryrop
[07:51] queryrop对象然后它是一个叫做什么呢userinfo这样的一个对象那么queryrop然后我们去new一个它然后设置queryrop点然后我们去设置我们的一个查询条件就是user就user下滑线ID应该我们是什么呢应该是in这个操作不是eq
[08:21] 然后呢, your ID 印谁呢印我们这个 your ID s好嘞,那么这样的话呢我们这个条件是不是就构造好了然后呢我们去查询到一个 your info list那么接下来呢我们就要去做一个两层的一个这个复循环啊,便利啊然后呢我们首先便利的是我们的这个 VSTOS然后呢我们再去便利我们的 your info
[08:51] 然后我们去做一个判断如果这个vist.getvistid.longvalue如果等于youtuainfo里面的id.getyoutuid叫什么我们这个拿错了叫youtuainfo.getyoutuid.longvalue如果这两个要相等的话那我们就应该break一下然后我们接下来是不是就去分装我们的这个
[09:20] 对象对吧Vist这个VO这个对象那么我们去分装一个它然后呢定一个等于new一个VistVistVO这样的一个对象然后呢我们去做还需要定一个集合对吧那就定一个集合那么叫list然后呢存的是这个VO这个对象这个要写成什么呢打写好然后呢我们设置一个result等于new一个revealist
[09:50] 然后我们去把它return一下好到这个里面去做一个按的添加那么vst vo做一个添加好那么这个里面就做一些数据的一些分装了那么分装我们就不去做了我们就直接把这个就call过来那么这个就是非常简单代码就做一些set设置那么最后可以看到有个年龄他的头像姓名 id以及他的尼称还有标签还有他的一个原分值
[10:19] 那么这样的话最后做一个return啊就可以了好那么接下来呢我们就可以来测试一下啊那么接下来我们先把这个服务呢都跑起来好那么现在我们这个服务呢都已经跑起来了那么下面呢我们就来测试一下啊点击它呃然后呢我们可以看到是不是就查询到我们的这个数据了那么这样的话呢我们是不是这个就已经搞定了对吧ok好那么我们来看一下啊那么呃到这测试的结束啊好那么这样的话呢我们这个谁看过我的这样一个
[10:49] 接口服务的一个编写呢那我们是不是已经做完了OK好那么关于我们这个谁看过我的一个功能这个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

