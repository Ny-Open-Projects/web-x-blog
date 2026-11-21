# 画面线理解：20_数据迁移_删除热点文章过期数据及总结

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\20_数据迁移_删除热点文章过期数据及总结【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:29, 01:12, 01:42, 02:33, 02:44, 02:57, 03:13, 03:30, 03:56, 04:33, 05:01, 05:25, 05:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:13:18

1) 这一组画面整体在讲如何使用 Quartz 定时任务框架结合 Spring Boot 实现定期删除过期数据的功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程教材第8.2节“定期删除过期的数据”，代码中定义了 `MigrationDeleteHotDataQuartz` 类，其 `triggerCron` 方法返回的定时任务表达式为 `["0 30 22 * * ?"]`，表示每天22:30执行。
画面2：IDEA项目结构视图，显示 `MigrationDeleteHotDataQuartz.java` 文件位于 `src/main/java/com/heima/migration/job/` 路径下。
画面3：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法定义，方法签名 `protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException`。
画面4：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法内，开始添加 `deleteExpiredData()` 方法的代码。
画面5：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法内，添加了日志记录语句 `log.info("开始删除数据过期数据");` 和 `log.info("删除数据库过期数据结束，耗时：0");`。
画面6：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法内，光标位于 `deleteExpiredData()` 方法调用前，准备编写方法体。
画面7：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法内，开始编写 `deleteExpiredData()` 方法，调用 `apHotArticleService.selectExpireMonth()` 获取过期数据列表。
画面8：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法内，为 `deleteExpiredData()` 方法添加了 `if (null == hotArticleList || hotArticleList.isEmpty())` 的空值判断。
画面9：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法内，为 `deleteExpiredData()` 方法添加了 `deleteHotData(apHotArticles)` 的删除操作。
画面10：IDEA编辑器中，`MigrationDeleteHotDataQuartz` 类的 `executeInternal` 方法内，`deleteExpiredData()` 方法的完整代码已编写完成，包含日志和数据删除逻辑。
画面11：展示“数据迁移流程”PPT，流程图包含“定时任务”、“热点数据迁移”、“文章数据迁移”等模块，其中“热点数据迁移”模块包含“从数据库中读取文章数据”、“删除过期数据”等步骤。
画面12：IDEA编辑器中，`MongoTest.java` 文件，定义了 `@SpringBootTest` 注解的测试类，包含 `testSave()` 方法用于插入数据，`testGetOne()` 方法用于根据ID查询数据。
画面13：IDEA编辑器中，`ArticleQuantity.java` 文件，定义了 `private ApHotArticle apHotArticle;` 和 `private ApArticleContent apArticleContent;` 等字段。
画面14：再次展示“数据迁移流程”PPT，与画面11内容相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
/**
 * 定期删除过期的数据
 */
@Component
@Slf4j
public class MigrationDeleteHotDataQuartz extends AbstractJob {

    @Autowired
    private ApHotArticleService apHotArticleService;

    @Override
    public String[] triggerCron() {
        /*
         * 2019/8/9 22:30:00
         * 2019/8/10 22:30:00
         * 2019/8/11 22:30:00
         * 2019/8/13 22:30:00
         */
        return new String[]{"0 30 22 * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
    }
}
```

画面2：
```
package com.heima.migration.job;
```

画面3：
```java
import org.quartz.JobExecutionException;
import org.springframework.stereotype.Component;

@Slf4j
@DisallowConcurrentExecution
public class MigrationDeleteHotDataQuartz extends AbstractJob {

    @Override
    public String[] triggerCron() {
        return new String[]{"0 30 22 * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
    }
}
```

画面4：
```java
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import
