# 18_mycat_mycat连接测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\18_mycat_mycat连接测试【海量资源尽在 666java.com】.mp4
- 时长 4分56秒（音频 297s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位刚才呢咱们是把所有的配置都已经配置完了啊那配置完之后呢这块内容呢咱们也也已经启动了那启动完之后呢咱们现在呀就来用咱们自己的程序呢去连接一下当前的这种mycat那首先呢咱们要做两次链接啊第一个链接呢就是在当前的nevercat中去连接当前的mycat好打开啊而这个其实我就是啊把它给删了啊删之后呢你连接一下怎么连呢比如说mycircle
[00:33] 比如说我就叫mycat,叫local这个端口号大家注意叫什么?
[00:39] 8066我可以注意这是8066不是3306,密码是多少?
[00:45] 密码是root吗?
[00:46] 还是123456?
[00:48] 123456因为我在这这文件里边是不是已经说了这是不是就是123456所以说你这就是123456你测试一下,OK,连接成功,好点确定
[01:02] 好双击打开打开你看啊当前这个库啊就是逻辑库那这个itk码-news其实就是对应的谁啊就是对应的当前scammer中有一个当前的这个库并且呢它是有那么多表这个表呢其实你在这也能打开看到了吗这个就是它的一张它的一些表就是一共有多少吧117张表但这个表啊是分布在不同的数据库上的这个大家一定要注意啊
[01:33] 虽然你看着连接跟之前的库没啥区别其实呢你查询的时候它是不一样的咱们可以做个测试啊比如说啊咱们可以打开本地的库咱们就打开谁呢比如说当前的一个叫做APInfo0里边啊有一个APArticle你看这里边啊这里边是一共是有153条数据对吧没问题吧153条啊那这时候呢咱们可以去查一下查谁呢就是查询当前的MyCat
[02:05] 咱们在这啊直接去slide新一下啊这样吧直接找到这个表啊打开你看这是多少条共1000条记录再往下走再往下走是不是一共有2000多条记录啊不对这是7是吧应该是有6000多条记录刚才咱们打开的一个库里边呢是只有100多条是吧所以说呢当前这个表呢是存在多少个表中看这啊
[02:34] 这个是不是已经存到了40个库中是吧咱们是在这查询的时候呢其实它是收集了40个库总共查询的是一共是有6000多条记录咱们可以这样啊看个星一下比如说看个星好就行是不是6123条吧OK啊那这样的话咱们在Narrowcase中怎么去连接咱们就说完了啊
[03:04] 那说完之后啊最终呢咱们是要在程序中也要连上那连接数据库这个咱们之前是不是讲过怎么怎么三者连呢是不是有common里边有当前的一个配置文件其实都是在当前的maven-test-properties里边去设置的对吧行那这个东西咱们消息改一改啊首先呢当前他他不是他啊就跟当前的数据库是一样的咱们数据库叫啥呀ID黑马-news是吧
[03:34] 所以说你要改叫什么IT黑马news并且这是8066是吧8066啊8066密码是654321密码反转大家千万不要忘了好吧那这设置完之后啊咱们就来可以测一下咱们还是查询当前的这种文章信息好吧咱们之前写过一个测试啊只要是他能查出来数据说明呢
[04:08] 就能连上是吧我可以执行稍等关于的配置呢其实在这也有说啊说你在这你要连上当年的数据库啊密码那个端口要改了密码要改了对吧最终的你再去测试这样就可以了啊好稍等一下吧他下面正在编译啊好编译完了来看一下看看这执行的效果啊我先走好正在往下走看看到底能不能连上好原亮色是吧
[04:48] 那这个就没有问题你看这个数据是不是就查到了呀好那这个关于这个连接和测试啊咱们就说到这里啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 MyCAT 的分库分表架构，通过配置文件和测试代码验证文章服务的读写分离与数据分片功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 MyCAT 配置目录，选中并高亮 `schema.xml` 文件，准备查看分库分表配置。
画面2：在 IntelliJ IDEA 中浏览项目结构，选中 `heima-leadnews-common` 模块，准备查看其代码。
画面3：在 IntelliJ IDEA 中浏览项目结构，选中 `heima-leadnews-article` 模块，准备查看其代码。
画面4：在文件资源管理器中，选中并高亮 `schema.xml` 文件，准备查看分库分表配置。
画面5：在 Notepad++ 中打开并展示 `schema.xml` 文件内容，包含多个分片表的定义。
画面6：在 Navicat for MySQL 中连接到本地 MySQL，显示数据库列表，准备查看表结构。
画面7：在 Navicat for MySQL 中展开 `mycat_local` 数据库，显示多个分片表，准备查看数据。
画面8：在 Navicat for MySQL 中查看 `ap_article` 表的数据，展示文章列表。
画面9：在 Navicat for MySQL 中查看 `ap_article` 表的数据，展示文章列表。
画面10：在 Navicat for MySQL 中执行 SQL 查询 `SELECT count(*) FROM ap_articles;`，返回结果 6123。
画面11：在 IntelliJ IDEA 中打开 `ArticleTest.java` 测试类，准备执行测试。
画面12：在 IntelliJ IDEA 中执行 `ArticleTest` 测试，控制台输出 Spring Boot 启动日志。
画面13：在 IntelliJ IDEA 中执行 `ArticleTest` 测试，控制台输出 Hibernate 和 Spring Framework 初始化日志。
画面14：在 IntelliJ IDEA 中执行 `ArticleTest` 测试，控制台输出测试通过日志，显示测试成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```xml
<?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<schema name="liheima-news" checkSQLSchema="true" sqlMaxLimit="100">
    <!-- 通用调度器quartz服务的调度表 -->
    <table name="QUARTZ_QRTZ_CALENDARS" dataNode="DNSQ" type="global"/>
    <table name="QUARTZ_QRTZ_CRON_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="QUARTZ_QRTZ_FIRED_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="QUARTZ_QRTZ_JOB_DETAILS" dataNode="DNSQ" type="global"/>
    <table name="QUARTZ_QRTZ_LOCKS" dataNode="DNSQ" type="global"/>
    <table name="QUARTZ_QRTZ_SIMPLE_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="QUARTZ_QRTZ_TRIGGERS" dataNode="DNSQ" type="global"/>
    <!-- 通用调度器crawler服务的调度表 -->
    <table name="CRAWLER_QRTZ_CALENDARS" dataNode="DNSQ" type="global"/>
    <table name="CRAWLER_QRTZ_CRON_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="CRAWLER_QRTZ_FIRED_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="CRAWLER_QRTZ_JOB_DETAILS" dataNode="DNSQ" type="global"/>
    <table name="CRAWLER_QRTZ_LOCKS" dataNode="DNSQ" type="global"/>
    <table name="CRAWLER_QRTZ_SIMPLE_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="CRAWLER_QRTZ_TRIGGERS" dataNode="DNSQ" type="global"/>
    <!-- 通用调度器migration服务的调度表 -->
    <table name="MIGRATION_QRTZ_CALENDARS" dataNode="DNSQ" type="global"/>
    <table name="MIGRATION_QRTZ_CRON_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="MIGRATION_QRTZ_FIRED_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="MIGRATION_QRTZ_JOB_DETAILS" dataNode="DNSQ" type="global"/>
    <table name="MIGRATION_QRTZ_LOCKS" dataNode="DNSQ" type="global"/>
    <table name="MIGRATION_QRTZ_SIMPLE_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="MIGRATION_QRTZ_TRIGGERS" dataNode="DNSQ" type="global"/>
</schema>
```

画面11：
```java
@SpringBootTest(classes = ArticleJarApplication.class)
@RunWith(SpringRunner.class)
public class ArticleTest {

    @Autowired
    private AppArticleService appArticleService;

    @Test
    public void testArticle() {
        AppUser appUser = new AppUser();
        appUser.setId(1104);
        AppThreadLocalUtils.setThread(appUser);
        ResponseResult result = appArticleService.load(null, ArticleConstants.LOADTYPE_LOAD_MORE);
        System.out.println(result.getData());
    }
}
```

画面12：
```
2019-09-11 11:00:39,246 [INFO] main [com.heima.article.test.ArticleTest] [logStarting] [Starting ArticleTest on LAPTOP-C3PJD3ES with PTD 10140 (start
2019-09-11 11:00:39,246 [INFO] main [com.heima.article.test.ArticleTest] [logStarting] [Starting ArticleTest on LAPTOP-C3PJD3ES with PTD 10140 (start
2019-09-11 11:00:39,248 [INFO] main [com.heima.article.test.ArticleTest] [logStartupProfile] [The following profiles are active: class org.apache.ibatis.logging.LogFactory] [Logging initialized using 'class org.apache.ibatis.logging.log4j2.Log4j2Impl' as impl]
```

画面13：
```
2019-09-11 11:00:42,584 [DEBUG] [com.zaxxer.hikari.pool.HikariPool-1] [After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After adding stats] [HikariPool-1 - After

