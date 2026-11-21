# 画面线理解：18_mycat_mycat连接测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\18_mycat_mycat连接测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:17, 00:25, 01:10, 01:20, 01:44, 02:06, 02:16, 02:42, 03:30, 04:06, 04:35, 04:43, 04:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:59:22

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
