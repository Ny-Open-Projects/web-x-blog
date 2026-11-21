# 13.今日佳人功能实现之编写业务代码（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\13.今日佳人功能实现之编写业务代码（中）_【海量资源尽在 666java.com】.mp4
- 时长 14分6秒（音频 847s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那么接下来呢我们就来查询我们的推荐的这个用户啊那么我们需要去创建一个我们的这个recommend user serviceuser Service去做一个查询那么这个呢我们把它标记为呢也是一个Service那么接下来呢在这个位置啊我们需要去注入一个什么呢叫做recommend userrecommendrecommend user API这样的一个
[00:30] API的一个实现这个是double的一个服务所以我们需要在这个位置去reface去把它去加载加载进来那么它的一个版本就是Wolfen这个版本是1.0.0这样的一个版本那么有了这个Service之后那么我们在我们这个Service中那么就可以把它就注入进来了把它注入进来
[00:57] 然后我们把它注入进来然后之后我们去做一个查询然后我们在这就可以去做一个查询了那么通过这个Service调用我们就调用queryquery today然后我们来一个best然后我们传递谁我们传递我们这个use点get什么id就是
[01:25] 查询这个用户的一个今日佳人是谁那么他的返回值呢我们来返回这个today besttoday best然后呢我们去创建这个方法把这个方法创建出来创建出来这个呢改成是一个叫做user id吧user id好嘞好那么有了它之后呢下面呢我们就需要调用啊上面的这个远程的这个实现类
[01:55] 然后呢去做一个查询了把这个UraID呢给他传递过去那么传递过去之后呢他将返回的是一个recommendUra这样的一个对象那么这个对象呢我们拿到之后啊首先我们需要去做一个判断对吧如果空等于他的话那我们就return什么呢return这个空那么如果不等于空的话啊如果不等于空的话那我们就需要去构造一个这个today best一个对象
[02:25] 那么我们接下来呢就来去new一个这个对象吧去new一个他等于什么呢等于去new一个today啊best然后today best点set谁呢我们设置我们这个我们先来设置我们的一个相关的一些这个参数比如说我们这个推荐的一个这个叫缘分值啊对吧缘分值那么我们就给他来做一个设置啊
[02:52] 一个是他那么这个缘分值怎么设置呢我们需要通过这个recommend yield中的这个score就是我们这个得分去获取到那么要注意的是在我们这个今日家人这个对象中啊他所要求的缘分值呢的类型呢是一个none类型那么也就是说呢如果说我们这个得分啊我们加一个注射啊那么如果假设啊
[03:20] 如果我们这个得分为98.2的10对吧那么我们需要显示的它的一个这个得分是什么98那么也就是说我们需要把这个小数给它去除掉对吧小数去除掉然后保留这个整数就可以了
[03:40] 那么我们也不做禁位啊也不做那个四轴五入直接去去除他的一个小数就可以了那么这个应该怎么去做呢那么我们应该呢通过这个mess这个操作里面有一个什么什么的follow然后呢去拿到他的一个就是直接把这个就是小数就去掉对吧然后呢他将拿到一个什么呢这个score然后呢我们去再去什么呢
[04:09] 通过一个这个double点什么的value of然后呢score然后呢点什么的long value这样呢才能拿到一个我们的一个这个long型啊这个呢就是我们的一个这个缘分缘分值OK好那么这个呢我们就搞定了那我们还需要给他设置一个什么呢设置一个这个ID啊ID呢就是什么呢用户的ID就是我们给张三推荐的李色
[04:37] 那么就是李四的这个ID那么李四这个ID从哪拿是不是通过我们的recommend user点get谁get userid这个大家能够理解不是那个to userid这个要搞清楚那么todaybest中还有没有其他的字段可以添加其实并没有了其他字段都是我们的一些这个user info中的一些字段对不对所以说在这个位置我们就不做添加了这个是我们的什么用户ID
[05:06] 那么最后呢我们是不是就可以return谁呢return我们这个today啊best这样的一个对象那么接下来呢我们在我们这个在这个today啊best这个中呢我们就可以去做一些下面逻辑处理了那么如果啊如果他等于空的话那么怎么样啊这个要注意啊就是说我们给张三去查询他的一个这个得分最高的一个用户会发现呢
[05:34] 这个没有对吧没有那么我们这个时候呢需要什么呢就是说未找到未找到这个最高得分的推荐用户推荐推荐用户用户那么我们一个这个应该怎么去处理呢我们应该给出一个什么呢默认推荐对吧默认推荐的一个用户了所以说呢这个位置如果
[06:04] 他等于none的话那我们就给他去做一个默认就好了去new一个todaybest然后呢我们把这个todaybest.set谁呢set这个IDset这个ID是谁呢就是我们给他去设置一个默认的一个值那么这个默认值呢我们不能印编码到我们的代码中我们需要写成web的一个配置文件所以呢在前面在这个位置就会有这样的一个配置了就是这个
[06:33] default这个user啊那我们把这个呢拷贝过来那么默认的就是推荐用户ID为2的这个用户那么我们来看一下那么我们就定义到上面来吧这个long类型的一个这个userID啊那我们去写一个value然后呢去写一个什么呢这个大括号啊然后呢我们应该应该写的叫什么呢default啊前面加个default吧叫default啊user啊userID
[07:03] 那么我们把这个default的UID啊就拿到然后呢就放到下面的这个位置来好那么这个是默认然后呢我们还需要给他set一个他的一个得分这个我们就给他默认吧我们就写一个比如说98分或者说就是写一个95分吧这样的一个啊这样的一个得分ok好那么接下来呢我们就需要去干嘛呢去补全我们这个对象中的一些其他的一些这个属性了
[07:33] 我们去就是什么呢补全啊补全这个用户信息啊补全这个用户信息那么我们来看一下怎么样去做一个补全呢这个用户信息呢他呢又是在我们的优质优质info中去做一个查询所以说呢在这个位置啊那么还需要去定义一个谁呢定义叫做优质info啊这样的一个Service
[08:01] 那么我们同样把它标记为这是一个Service然后我们去把这个Service去注入到todaybest中然后我们去做一个使用那么我们去把它就注入进来然后下面在这个位置我们调用 user info Service.queryuser info by什么by id对吧通过id去做一个查询
[08:32] 那么我们这个推荐的这个用户他的ID是多少呢是不是就点get谁呢get ID对吧拿到这个ID然后呢我们就可以拿到一个对象啊叫做user info这样的对象那么在前面呢我们就来定义一个叫做user info这个对象然后呢user info等于他啊然后呢我们在这个Service中呢去定义这个方法把这个方法呢就定义出来了然后呢user info这个怎么样去做一个
[09:02] 做一个查找呢我们就简单来实现啊就是直接去查询我们的数据库啊就可以了所以呢在这个位置我们需要一个UseInfo的一个这个Mapper那我们在这个里面嘛来写一个我们的一个这个接口啊叫Interface就叫UseInfoMapper写这样的一个接口那么它呢要去继承我们有个叫做BaseBaseMapper然后呢这个对象呢就叫Use
[09:32] UseInfoOK好那么这个呢是这样的一个这个Service这个Mapper那么我们就可以把这个Mapper呢在我们的这个UseInfo的Service中呢去注入进来了把它呢注入进来把它注入进来然后呢把它呢注入进来好那么这样的话呢我们就可以通过这个UseInfoMapper我们去加一个注释这个就是我们去怎么呢这个查询数据库查询数据库
[10:03] 然后呢就去什么呢查找查找查找用户的信息数据那么这个呢我们要说明一下说明就是说我们这里呢是为了这个为了这个简单处理为了这个简单处理简单处理就直接去查询数据库了那么如果我们去开发一个我们的一个这个
[10:31] 就是比较正规的啊这样的一个真实项目的话那我们建议啊给大家一个建议呢就是就去什么呢就编写这个什么呢double服务然后呢进行啊调用那么这个方式也可以啊当然我们这块呢为了简单处理呢我们就直接去查询数据库了那么我们去怎么样去做一个查询呢我们就会调用上面的这个this.yourinformappsleptbyid啊就可以了
[11:01] 那么直接返回这个有info就OK了这个就比较简单了直接电话他去做一个返回然后我们来看一下又回到我们的这个Service中那么在这个Service中那么就可以去做一些信息的补全了比如说我们这个中会有一些比如说年历那么有的info中他也会有年历去做一个设置
[11:29] 大概就是一些这样的一些字段我们去做一些这个补全点set所以比如说还有头像那么我们在我们对象中是一个get什么logo这样的一个头像然后还有什么set一个我们的一个性别对吧那么我们这个位置由info中我们get什么是一个美举对吧sex这样的一个美举点name
[11:55] 那么为什么点name呢原因是呢我们来看一下我们的这个接口啊那么这个他的性别啊就gander他的一个性别呢他是有这两个对吧一个man或者一个woman啊这样的一个这个字不错啊那么我们就需要拿到他这个name那么来看一下他的name是谁呢其实就是中的这个man和这个woman啊这两个对象啊这个他的一个name那么有了这个
[12:22] 当然了我们这块会有个小问题就是这个拿到他的一个这个枚举的一个name是一个大写我们需要把它转成一个小写那么应该怎么转呢就直接转小写吧就这么算就转转成一个小写就可以了这个大家应该能够理解吧那么然后呢我们还需要去设置一些比如说像他尼琛那么get什么呢那个name然后呢这个是set还有什么呢tax
[12:50] 啊tax那么这块呢我们也有get什么tax但是呢我们这个tax它是一个字符创需要去做一个这个分割所以呢我们在这个位置通过一个utils split去做一个分割了然后呢通过一个逗号啊去做一个分割那么这样的话呢我们信息呢是不是就基本上呢就补全了对吧我们看一下还有没有其他的一些这个信息点set啊这个ok了ok了okokokok好那么信息是不是都已经就ok了
[13:20] 那么接下来呢我们就往这一丢就可以了哎呀OK好嘞当然了在这个位置啊我们还需要去做一个非空的一个判断啊如果它不等于空的话有的info啊如果它不等于空的话那我们再去做这个处理那么如果它为空的话那我们就不能够这么去做了那我们就直接去返回它吧哎呀OK
[13:45] 好那么到这里我们逻辑是不是基本上就已经就搞定了我们来看一下我们的一个讲义基本上写的可能也差不多差不多这样的一个逻辑了OK好那么关于逻辑我们就先写到这那么一会我们来去做一个测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Java 服务中通过组合多个服务（用户服务、推荐服务、用户信息服务）来构建一个“今日最佳用户”推荐功能。

2) 按时间顺序列出每张画面的要点：
画面1: 在 IntelliJ IDEA 中，右键点击 `TodayBestService.java` 文件，弹出菜单，准备创建或修改运行配置。
画面2: 展示 `TodayBestService.java` 文件内容，其中包含 `@Autowired` 注解的 `userService` 字段和 `queryTodayBest` 方法的初始骨架。
画面3: 展示 `RecommendUserService.java` 文件，其中定义了 `@Reference` 注解的 `recommendUserApi` 字段和 `queryTodayBest` 方法。
画面4: 在 `RecommendUserService.java` 中，光标位于 `queryWithMaxScore` 方法调用处，准备输入参数。
画面5: 在 `RecommendUserService.java` 中，光标位于 `setFateValue` 方法调用处，准备输入参数。
画面6: 在 `TodayBestService.java` 中，光标位于 `queryTodayBest` 方法内，准备输入 `recommendUserService` 的调用。
画面7: 在 `TodayBestService.java` 中，光标位于 `setFateValue` 方法调用处，准备输入参数。
画面8: 在 `TodayBestService.java` 中，光标位于 `queryUserInfoById` 方法调用处，准备输入参数。
画面9: 展示 `UserInfoService.java` 文件，其中包含 `@Service` 注解和 `@Value` 注解的字段。
画面10: 在 `TodayBestService.java` 中，光标位于 `queryUserInfoById` 方法调用处，准备输入参数。
画面11: 在 `TodayBestService.java` 中，光标位于 `setGender` 方法调用处，准备输入参数。
画面12: 在 `TodayBestService.java` 中，光标位于 `setTags` 方法调用处，准备输入参数。
画面13: 在 `TodayBestService.java` 中，光标位于 `queryUserInfoById` 方法调用处，准备输入参数。
画面14: 在 `TodayBestService.java` 中，光标位于 `return todayBest;` 语句处，准备完成方法。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2:
```java
public class TodayBestService {
    @Autowired
    private UserService userService;

    public TodayBest queryTodayBest(String token) {
        //根据token查询当前登录的用户信息
        User user = this.userService.queryUserByToken(token);
        if (user == null) {
            return null;
        }
        return null;
    }
}
```

画面3:
```java
import com.alibaba.dubbo.config.annotation.Reference;
import com.tanhua.dubbo.server.api.RecommendUserApi;
import com.tanhua.server.vo.TodayBest;
import org.springframework.stereotype.Service;

@Service
public class RecommendUserService {
    @Reference(version = "1.0.0")
    private RecommendUserApi recommendUserApi;

    public TodayBest queryTodayBest(Long userId) {
        RecommendUser recommendUser = this.recommendUserApi.queryWithMaxScore(userId);
        return null;
    }
}
```

画面6:
```java
public TodayBest queryTodayBest(String token) {
    //根据token查询当前登录的用户信息
    User user = this.userService.queryUserByToken(token);
    if (user == null) {
        return null;
    }
    TodayBest todayBest = this.recommendUserService.queryTodayBest(user.getId());
    if (todayBest == null) {
        //未找到最高得分的推荐用户，给出一个默认推荐用户
        todayBest = new TodayBest();
        todayBest.setId(defaultUserId);
        todayBest.setFateValue(951);
    }
    return null;
}
```

画面7:
```java
public TodayBest queryTodayBest(String token) {
    //根据token查询当前登录的用户信息
    User user = this.userService.queryUserByToken(token);
    if (user == null) {
        return null;
    }
    TodayBest todayBest = this.recommendUserService.queryTodayBest(user.getId());
    if (todayBest == null) {
        //未找到最高得分的推荐用户，给出一个默认推荐用户
        todayBest = new TodayBest();
        todayBest.setId(defaultUserId);
        todayBest.setFateValue(951);
    }
    return null;
}
```

画面8:
```java
// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getId());
```

画面10:
```java
// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getId());
```

画面11:
```java
// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getId());
todayBest.setAge(userInfo.getAge());
todayBest.setAvatar(userInfo.getLogo());
todayBest.setGender(userInfo.getSex().name().toLowerCase());
todayBest.setNickname(userInfo.getNickName());
todayBest.setTags(StringUtils.split(userInfo.getTags(), separator));
```

画面12:
```java
// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getId());
todayBest.setAge(userInfo.getAge());
todayBest.setAvatar(userInfo.getLogo());
todayBest.setGender(userInfo.getSex().name().toLowerCase());
todayBest.setNickname(userInfo.getNickName());
todayBest.setTags(StringUtils.split(userInfo.getTags(), separator));
```

画面14:
```java
// 补全用户信息
UserInfo userInfo = this.userInfoService.queryUserInfoById(todayBest.getId());
if (null != userInfo) {
    todayBest.setAge(userInfo.getAge());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setNickname(userInfo.getNickName());
    todayBest.setTags(StringUtils.split(userInfo.getTags(), separator));
}
return todayBest;
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。

