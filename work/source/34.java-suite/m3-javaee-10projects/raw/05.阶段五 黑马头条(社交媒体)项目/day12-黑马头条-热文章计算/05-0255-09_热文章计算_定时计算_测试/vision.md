# 画面线理解：09_热文章计算_定时计算_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\09_热文章计算_定时计算_测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:22, 00:29, 00:35, 00:47, 01:08, 01:20, 01:54, 02:05, 02:16, 02:24, 02:40, 03:05, 03:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:37:04

1) 这一组画面整体在讲如何使用 Spring Boot + Quartz 实现文章热度分值的定时计算与持久化功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 `ApplHotArticleQuartz.java` 中的 `triggerCron` 方法，设置定时任务触发时间为 `0 0/2 * * * ?`，并展示 `executeInternal` 方法中调用 `apHotArticleService.computeHotArticle()` 计算分值。
画面2：展示项目结构，`ArticleApplication` 启动类，以及 `target` 目录下的 `heima-leadnews-article.ini` 配置文件。
画面3：展示 `ApplHotArticleQuartz.java` 中 `triggerCron` 方法的代码，高亮显示 `return new String[]{"0 0/2 * * * ?"}`。
画面4：展示 `ApplHotArticleServiceImpl.java` 中 `computeHotArticle` 方法，其中 `String lastDay = DateTime.now().minusDays(1).toString("%yyyy-MM-dd 00:00:00");`，并调用 `apArticleMapper.loadLastArticleForHot(lastDay, articleList)` 加载文章列表。
画面5：展示 `ApplHotArticleQuartz.java` 中 `executeInternal` 方法，高亮显示 `log.info("开始定时计算分值");` 和 `log.info("计算分值完成, 耗时: 0", System.currentTimeMillis()-currentTimeMillis);`。
画面6：展示 Navicat for MySQL 中 `ap_article` 表的数据，包含 `title`、`author_id`、`channel_id`、`layout`、`images`、`labels`、`likes`、`collection`、`comment`、`views`、`province_id`、`city_id`、`county_id`、`created_time`、`publish_time`、`sync_status` 等字段。
画面7：展示 Navicat for MySQL 中 `ap_article` 表的数据，包含 `title`、`author_id`、`channel_id`、`channel_name`、`layout`、`images`、`labels`、`likes`、`collection`、`comment`、`views`、`province_id`、`city_id`、`county_id`、`created_time`、`publish_time`、`sync_status` 等字段。
画面8：展示 Navicat for MySQL 中 `ap_article` 表的数据，包含 `channel_name`、`layout`、`images`、`labels`、`likes`、`collection`、`comment`、`views`、`province_id`、`city_id`、`county_id`、`created_time`、`publish_time`、`sync_status` 等字段。
画面9：展示 `ApplHotArticleServiceImpl.java` 中 `computeHotArticle` 方法，高亮显示 `List<ApHotArticles> hotArticlesList = computeHotArticle(articleList);`，并展示调试窗口中 `hotArticlesList` 的内容。
画面10：展示 `ApplHotArticleServiceImpl.java` 中 `computeHotArticle` 方法，高亮显示 `hotArticlesList` 的内容，其中 `articleId = 10160`。
画面11：展示 `ApplHotArticleServiceImpl.java` 中 `computeHotArticle` 方法，高亮显示 `List<ApBehaviorEntry> entryList = apBehaviorEntryMapper.selectEntryList();`，并展示调试窗口中 `entryList` 的内容。
画面12：展示 `ApplHotArticleServiceImpl.java` 中 `computeHotArticle` 方法，高亮显示 `apHotArticleMapper.insert(hot);`。
画面13：展示 `ApplHotArticleServiceImpl.java` 中 `computeHotArticle` 方法，高亮显示 `//保存文章中的图片（暂时不做）`。
画面14：展示 `ApplHotArticleQuartz.java` 中 `executeInternal` 方法，高亮显示 `log.info("计算分值完成, 耗时: 0", System.currentTimeMillis()-currentTimeMillis);`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
@Component
@Slf4j
public class ApplHotArticleQuartz extends AbstractJob {
    @Override
    public String[] triggerCron() {
        return new String[]{"0 0/2 * * * ?"};
    }

    @Autowired
    private ApHotArticleService apHotArticleService;

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
        long currentTimeMillis = System.currentTimeMillis();
        log.info("开始定时计算分值");
        apHotArticleService.computeHotArticle();
        log.info("计算分值完成, 耗时: 0", System.currentTimeMillis()-currentTimeMillis);
    }

    @Override
    public String destriger() {
        return null;
    }
}
```

画面4：
```java
@Override
public void computeHotArticle() {
    //查询一天的新发布的文章
    String lastDay = DateTime.now().minusDays(1).toString("%yyyy-MM-dd 00:00:00");
    List<ApArticle> articleList = apArticleMapper.loadLastArticleForHot(lastDay, articleList);
    //计算文章热度（阅读量、评论、点赞、收藏）
    List<ApHotArticles> hotArticlesList = computeHotArticle(articleList);
    //缓存到redis
    cacheApHotArticles(hotArticlesList);
}
```

画面9：
```java
List<ApHotArticles> hotArticlesList = computeHotArticle(articleList);
```

画面10：
```java
articleId = 10160
```

画面11：
```java
List<ApBehaviorEntry> entryList = apBehaviorEntryMapper.selectEntryList();
for (ApHotArticles hot : hotArticlesList) {
    //保存热点文章
    apHotArticleMapper.insert(hot);
    //保存文章中的图片（暂时不做）
}
```

画面12：
```java
apHotArticleMapper.insert(hot);
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
