# 09.今日佳人功能实现之实现dubbo服务（查询推荐用户列表）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\09.今日佳人功能实现之实现dubbo服务（查询推荐用户列表）_【海量资源尽在 666java.com】.mp4
- 时长 9分46秒（音频 586s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们已经完成了这个今日家人这样的一个查询那么下面我们来看一下这个推荐用户的一个列表这样的一个查询那么应该怎么去做那么我们是需要通过这个mongo template.有一个fund这个方法去做一个查询那么它同样呢需要两个参数一个呢就是query对象一个就是我们的一个这个class
[00:29] 好,那我们就去调用这个分的这个方法那么两个参数第一个呢是呃这个query啊先设置为none那么第二个呢就是我们的啊recommend user.classok好,那么接下来我们要做的事情呢就是去呃去构建这个query对吧那么query呢就等于什么呢是不是等于这个query啊点query然后呢我们去构造我们的一个查询的一个
[00:58] 条件啊对吧那么这个条件呢跟我们上面这个条件是不是它呢是一样的对吧那肯定是查询的我当前的这个呃用户啊所以说这个条件呢是是这样的啊然后呢我们需要设置一个位置那么要注意了在这个位置呢既然你查询这个列表那么一定呢会有分页对不对啊所以它一定会对应到的是什么这个方法对不对那么pay to able啊这样的一个方法那么我们呃
[01:28] 来去电用它那么下面我们是不是需要在这个位置在这个位置我们需要提定一个配置什么配置我们来看一下那么我们来看一下它这个里面的一个类型来点一下那么配置able它是一个接口对吧那我们需要去查看一下它的一个实现类那我们来看一下它的一个实现类那么我们就go to吧
[01:56] 这一个go to然后呢看它的一个实现类那么在这个实现类中呢其中有一个叫做什么呢PageRequest这个对象那我们去使用这个Request这个对象那我们当然了我们定义的时候呢可以通过这个PageAble去做一个定义对吧那么我们来定义一下那么使用就它然后呢这个PageAble等于去干嘛呢我们去new一个这个
[02:24] 我们应该是去new一个new一个叫做page request这样的一个对象然后呢我们给它设置一些参数那么我们来看一下它的一个参数那么会发现呢它其实已经都过时了那么这个呢我们不能去直接去new那么我们通过它有一个off这个方法
[02:46] 那么有个off这个方法那么可以看到是不是一般我们用上面这个就可以了对吧符合我们的需求了一个是我们的page size还有一个排序我们就使用它那么我们要注意了设置一个page number然后off那么我们来看第一个参数就是page number那么第二个参数是page size那么第三个参数就是我们那个sort排序了
[03:14] 我们就来做一个排序点 desc然后根据谁根据我们scoreok好那么这个地方是不是少了一个off好那么来看一下这个是这个是pace size放到这来好那么这样的话是不是就ok了他说
[03:39] 是没有一个这个方法不能去转这个方法那么这个是里面我们传递错了吗一个是int还能有一个是这个sort应该是OK的那么这个位置呢是不是会有点问题就是我们这个sort点这个by对吧扫了一个他然后呢我们把它呢传递过来这样去做一个构建OK好那么配置able呢是不是就搞定了丢到这来那么
[04:09] 这样的话呢我们是不是就完成了这样的一个查询了我们把这query呢放到这个里面来OK然后呢他呢就会去得到一个我们这个list然后呢最后呢我们就可以去做一个return了那么return的是我们的一个叫做page info这样的一个对象那么page info呢我们来看一下它呢需要有三个参数第一个呢是数据的总条数
[04:36] 那么在这个位置呢我们数据总调数呢我们先给它设置什么呢0啊我们为什么要去哎它是一个int型的对吧我们不需要这个L了啊不是浪形的那就0那我们为什么要去设置这个0呢我们这儿去说明一下啊这个数据总调数那么这个呢我们暂时呢啊暂时啊不提供那么如果啊如果我们需要的话啊在
[05:05] 提供啊那么这个是什么意思就是说那么我们在前端做我们这种分页效果的时候呢也不一定啊必须要用到总条数那么我比方说像我们的一种这种就是
[05:20] 这种一支这种下拉去更新的这样的一种效果的话它其实是不需要我们的数据总条数的那么可以一直往下一页去查询那么什么时候我就不再查询了呢就是你返回的这个结果它的集合为空的时候那我就不再继续做查询了那么这样的话就没有必要去得到我数据的一个总条数了这个大家能够理解了吧所以这个位置我们暂时不做一个提供
[05:47] 那么这是第一个这个参数那么第二个这个参数呢它呢是一个叫PageNumber对吧那我们来给它设置一个这个PageNumber啊设置它然后呢第三个这个参数那就是一个List了那么把这个呢给它啊丢进去好那么这样的话是不是就OK了那么这个是不是少一个这个范形呢嗯来看一下啊那么哎我们来点过去来看一下啊这个是不是会有点问题啊第一第二
[06:14] 还有一个page size那么page size呢那就是我们之前那个page size少一个参数啊这样的话是不是就OK了这个范形可以不写好那么这样的话我们是不是就搞定了对吧那么接下来呢我们来写一个测试用例那我们来测试一下它那么下面呢我们就写一个public word然后test一个list吧我们去测试这个集合那么写一个test
[06:42] 然后呢就要用它里面的这个query这个list那么UID呢肯定还是1对吧那第二个这个参数那么是PageNumber我们查询第一页然后呢我们来看一下这个查询每页查询五条数据吧叫做这样的一个查询那么它的返回值呢就是一个PageInfo那么这样我们就直接做一个SystemAlt的一个输出吧那我们来这个是查询什么查询我们的第一页对吧
[07:11] 那么我们继续往下面去写那么我们来查询什么呢第二页和第三页那我们来看一下查询的结果啊对不对好那我们来执行一下好那我们来等待他的一个执行好那么现在呢就已经执行结束了啊那我们来看一下这个结果那么可以看到呢在这个位置是不是已经查询到有三个这个配置info的对象那么我们来看一下他的数据啊对不对那么上面这个呢是第一页的数据
[07:40] 那么我们来看一下啊那么他的第一条这个数据呢ID呢是18那个score得分的是96那么其实看到这样的我们会觉得这个数据肯定是有问题的为什么有问题呢那么在前面我们去查询他的这个最高的这个得分的时候我们会知道他的一个用户呢是最高分是98但是呢这个位置第一个所返回的竟然是96那么这个数据显然的是不对的
[08:08] 那么为什么呢来说明一下啊那么在我们的这个实现中啊要注意一下那么我们这个配置它呢是从零开始的所以呢我们这个呢需要什么呢减一啊就是在我们实际的这个分页的这个基础之上呢我们要去减一才是它真正的这个底层的所需要的这个分页数啊这一点要注意了好那我们再来执行一下看它的效果会怎么样走
[08:37] 好那么下面呢我们来看一下我们的这个结果那么其实可以看到第一条这个数据呢就是ID为13的这个用户然后它的一个得分的是98那么这回是不是就正确了对吧然后呢我们可以大致的来浏览一下它的一些数据那么第二条呢用户ID呢45得分的也是98然后98啊97可以看到97啊也是一个啊这样的一个倒序排序的这样的一个数据那么我们可以看到刚刚呢我们
[09:07] 这条数据是不是刚刚被放到了第一条里面啊所以说可以看到它其实是在第二页的啊第一条这样的一个数据了OK好那么呃那么到这里呢我们这个方法测试呢是不是就结束了对吧那么这个就是我们给大家所讲的这个怎么呢查询用户的这样的一个列表那我们一起来看一下我们的一个讲义啊那么讲义呢跟我们的实现呢啊是基本上是一样的啊基本上是一样的
[09:33] 那么下面的去做测试结果呢跟我们得到的结果呢肯定都是一样的OK好那么关于我们这个double的一个这个服务的一个实践呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Data MongoDB 中实现分页查询，包括编写分页接口、构造分页条件、以及编写测试用例验证分页功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 `RecommendUserApiImpl.java` 中 `queryWithMaxScore` 方法的代码，用于根据用户ID查询得分最高的推荐用户。
画面2: 展示了 `queryPageInfo` 方法的代码，该方法用于分页查询推荐用户列表，当前代码中返回 null。
画面3: 展示了 `queryPageInfo` 方法的代码，正在修改 `query` 对象以应用分页条件。
画面4: 展示了 `queryPageInfo` 方法的代码，已添加 `Pageable pageable` 参数并初始化。
画面5: 展示了 Spring Data Commons 中 `Pageable` 接口的源码，用于理解分页对象的定义。
画面6: 展示了在 `queryPageInfo` 方法中，通过 `Pageable pageable = new Pageable();` 初始化分页对象。
画面7: 展示了 `queryPageInfo` 方法中，使用 `PageRequest.of(...)` 构造分页对象。
画面8: 展示了 `queryPageInfo` 方法中，使用 `PageRequest.of(pageNum, pageSize, Sort.Order.desc("score"))` 构造分页对象。
画面9: 展示了 `PageInfo` 类的源码，该类用于封装分页查询结果，包含总条数、当前页、每页大小等字段。
画面10: 展示了 `PageInfo` 类的源码，光标位于 `pageSize` 字段上。
画面11: 展示了测试类 `TestRecommendUserApi` 的代码，包含 `testQueryWithMaxScore` 和 `testList` 两个测试方法。
画面12: 展示了 `testList` 方法的代码，调用 `queryPageInfo` 方法并打印结果。
画面13: 展示了 `testList` 方法的执行结果，打印了多条推荐用户数据，包含用户ID、得分、日期等信息。
画面14: 展示了项目文档 `day02.md` 的内容，其中包含了项目结构、配置文件、测试等章节的目录。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1:
```java
@Override
public RecommendUser queryWithMaxScore(Long userId) {
    Criteria criteria = Criteria.where("toUserId").is(userId);
    // 按照得分倒序查询，获取一条数据
    Query query = Query.query(criteria).with(Sort.by(Sort.Order.desc("score")));
    .limit(1);
    return this.mongoTemplate.findOne(query, RecommendUser.class);
}
```

画面2:
```java
@Override
public PageInfo<RecommendUser> queryPageInfo(Long userId, Integer pageNum, Integer pageSize) {
    this.mongoTemplate.find(query, null, RecommendUser.class);
    return null;
}
```

画面3:
```java
@Override
public PageInfo<RecommendUser> queryPageInfo(Long userId, Integer pageNum, Integer pageSize) {
    Criteria criteria = Criteria.where("toUserId").is(userId);
    Query query = Query.query(criteria).with();
    this.mongoTemplate.find(query, null, RecommendUser.class);
    return null;
}
```

画面4:
```java
@Override
public PageInfo<RecommendUser> queryPageInfo(Long userId, Integer pageNum, Integer pageSize) {
    Criteria criteria = Criteria.where("toUserId").is(userId);
    Query query = Query.query(criteria).with();
    this.mongoTemplate.find(query, null, RecommendUser.class);
    return null;
}
```

画面5:
```java
/**
 * Abstract interface for pagination information.
 * @author Oliver Gierke
 */
public interface Pageable {
    /**
     * Returns a {@link Pageable} instance representing no pagination setup.
     * @return
     */
    static Pageable unpaged() { return Unpaged.INSTANCE; }
    /**
     * Returns whether the current {@link Pageable} contains pagination information.
     * @return
     */
    default boolean isPaged() { return true; }
}
```

画面6:
```java
Pageable pageable = new Pageable();
```

画面7:
```java
Pageable pageable = PageRequest.of(pageNum, pageSize, Sort.Order.desc("score"));
```

画面8:
```java
Pageable pageable = PageRequest.of(pageNum, pageSize, Sort.Order.desc("score"));
```

画面9:
```java
@Data
@AllArgsConstructor
public class PageInfo<T> implements java.io.Serializable {
    private static final long serialVersionUID = -2105385689859184204L;
    /**
     * 总条数
     */
    private Integer total;
    /**
     * 当前页
     */
    private Integer pageNum;
    /**
     * 一页显示的大小
     */
    private Integer pageSize;
    /**
     * 数据列表
     */
    private List<T> list;
}
```

画面11:
```java
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestRecommendUserApi {
    @Autowired
    private RecommendUserApi recommendUserApi;

    @Test
    public void testQueryWithMaxScore() {
        RecommendUser recommendUser = this.recommendUserApi.queryWithMaxScore(userId: 1L);
        System.out.println(recommendUser);
    }

    @Test
    public void testList() {
        this.recommendUserApi.queryPageInfo(userId: 1L, pageNum: 1, pageSize: 5);
    }
}
```

画面12:
```java
@Test
public void testList() {
    System.out.println(this.recommendUserApi.queryPageInfo(userId: 1L, pageNum: 1, pageSize: 5));
    System.out.println(this.recommendUserApi.queryPageInfo(userId: 1L, pageNum: 2, pageSize: 5));
    System.out.println(this.recommendUserApi.queryPageInfo(userId: 1L, pageNum: 3, pageSize: 5));
}
```

画面13:
```java
List<RecommendUser> recommendUsers = this.mongoTemplate.find(query, RecommendUser.class);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面14:
- 标题：day02.md
- 内容：
  1. 首页
  2. 今日任务
     2.1. 部署MongoDB
     2.2. 搭建工程
     2.3. 搭建dubbo服务
        2.3.1. 搭建接口
        2.3.2. 搭建服务
        2.3.3. 测试
           2.3.3.1. pom.xml
           2.3.3.2. application.properties
           2.3.3.3. ServerApplication
           2.3.3.4. RestTemplateConfig
  2.5. 实现今日任务
     2.5.1. mod服务
     2.5.2. User
     2.5.3. Userinfo
     2.5.4. TodayBest

5) 无。

