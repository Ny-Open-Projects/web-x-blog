# 画面线理解：17_数据迁移_定时同步全量数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\17_数据迁移_定时同步全量数据【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:52, 01:15, 02:20, 02:59, 03:35, 04:06, 04:23, 04:55, 05:40, 05:59, 06:35, 07:08, 07:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:10:43

1) 这一组画面整体在讲一个基于 Quartz 定时任务的数据库迁移系统，具体实现文章数据从 MySQL 同步到 HBase 的功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示系统整体迁移流程图，包含“定时任务”、“文章数据迁移”、“文章详情迁移”等模块，中间有“MQ”和“定时任务”等节点。
画面2：在 IntelliJ IDEA 中，右键点击项目模块“heima-leadmin-migration”，选择“Build Module 'heima.migration'”。
画面3：在 IntelliJ IDEA 中，打开并查看 `MigratorDbToBaseQuartz.java` 文件，显示类定义和 `triggerCron` 方法。
画面4：在 IntelliJ IDEA 中，查看 `MigratorDbToBaseQuartz.java` 文件，显示 `executeInternal` 方法的定义。
画面5：在 IntelliJ IDEA 中，查看 `MigratorDbToBaseQuartz.java` 文件，显示 `articleQuantityService` 字段的定义。
画面6：在 Navicat for MySQL 中，查看 `MIGRATION_ORTZ_JOB_DETAILS` 表，显示定时任务配置信息。
画面7：在 IntelliJ IDEA 中，查看 `MigratorDbToBaseQuartz.java` 文件，显示 `@Autowired` 注解和 `articleQuantityService` 字段。
画面8：在 IntelliJ IDEA 中，查看 `MigratorDbToBaseQuartz.java` 文件，显示 `triggerCron` 方法的返回值和 `executeInternal` 方法的实现。
画面9：在 Navicat for MySQL 中，查看 `MIGRATION_ORTZ_JOB_DETAILS` 表，显示定时任务配置信息。
画面10：在 IntelliJ IDEA 中，查看 `ArticleQuantityServiceImp.java` 文件，显示 `getArticleQuantityList` 方法的实现。
画面11：在 IntelliJ IDEA 中，查看 `ArticleQuantityServiceImp.java` 文件，显示 `getArticleQuantityList` 方法的实现。
画面12：在 IntelliJ IDEA 中，查看 `ArticleQuantityServiceImp.java` 文件，显示 `doTdbase` 方法的实现。
画面13：在 IntelliJ IDEA 中，查看 `ArticleQuantityServiceImp.java` 文件，显示 `doTdbase` 方法中 `storageClient.addBaseStorage` 的调用。
画面14：在 IntelliJ IDEA 中，查看 `MigratorDbToBaseQuartz.java` 文件，显示 `executeInternal` 方法的实现。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```
Build Module 'heima.migration'
```

画面3：
```java
@Component
public class MigrationDbToBaseQuartz extends AbstractJob {
    @Override
    public String[] triggerCron() {
        return new String[]{"0 0/2 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
    }
}
```

画面4：
```java
import org.quartz.JobExecutionException;
import org.springframework.stereotype.Component;

@Component
public class MigrationDbToBaseQuartz extends AbstractJob {
    @Override
    public String[] triggerCron() {
        return new String[]{"0 0/2 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
    }
}
```

画面5：
```java
@Component
public class MigrationDbToBaseQuartz extends AbstractJob {
    @Override
    public String[] triggerCron() {
        return new String[]{"0 0/2 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
        log.info("开始同步文章数据到hbase");
        articleQuantityService.doTdbase();
        log.info("同步文章数据到hbase完成");
    }
}
```

画面7：
```java
@Component
public class MigrationDbToBaseQuartz extends AbstractJob {
    @Autowired
    private ArticleQuantityService articleQuantityService;

    @Override
    public String[] triggerCron() {
        return new String[]{"0 0/2 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
        log.info("开始同步文章数据到hbase");
        articleQuantityService.doTdbase();
        log.info("同步文章数据到hbase完成");
    }
}
```

画面10：
```java
@Override
public List<ArticleQuantity> getArticleQuantityList() {
    Log.info("生成ArticleQuantity列表");
    List<Article> unSyncArticleList = apArticleService.getSyncArticleList();
    List<String> apArticleIdList = unSyncArticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
    List<ArticleConfig> apArticleConfigList = apArticleConfigService.queryArticleConfigs(apArticleIdList);
    List<ArticleContent> apArticleContentList = apArticleContentService.queryArticleContents(apArticleIdList);
    List<Author> apAuthorList = apAuthorService.queryByIds(apArticleIdList);
    List<ArticleQuantity> articleQuantityList = unSyncArticleList.stream().map(article -> {
        return new ArticleQuantity({
            setArticle(article),
            setAuthorId(apAuthorList.get(article.getAuthorId())),
            setArticleConfig(apArticleConfigList.get(article.getArticleConfigId())),
            setArticleContent(apArticleContentList.get(article.getArticleContentId()))
        });
    }).collect(Collectors.toList());
    return articleQuantityList;
}
```

画面12：
```java
@Override
public void doTdbase() {
    long currentTimeMillis = System.currentTimeMillis(); // currentMillis: 1572685503137
    List<ArticleQuantity> articleQuantityList = getArticleQuantityList(); // articleQuantityList: size = 5
    if (null != articleQuantityList && !articleQuantityList.isEmpty()) {
        Log.info("开始进行定时数据库到hbase同步，筛选出未同步的数据量：" + articleQuantityList.size());
        List<BaseStorage> baseStorageList = articleQuantityList.stream().map(ArticleQuantity::getBaseStorage).collect(Collectors.toList());
        storageClient.addBaseStorage(BaseConstants.ARTICLE_QUANTITY_TABLE_NAME, baseStorageList);
    } else {
        Log.info("定时数据同步到hbase中，没有找到数据");
    }
}
```

画面13：
```java
List<BaseStorage> baseStorageList = articleQuantityList.stream().map(ArticleQuantity::getBaseStorage).collect(Collectors.toList());
storageClient.addBaseStorage(BaseConstants.ARTICLE_QUANTITY_TABLE_NAME, baseStorageList);
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：流程图结构：
- “定时任务” → “文章数据迁移” → “文章详情迁移”
- “文章数据迁移” → “MQ”
- “文章详情迁移” → “MQ”
- “MQ” → “定时任务”
- “定时任务” → “文章数据迁移”
- “定时任务” → “文章详情迁移”

5) 无
