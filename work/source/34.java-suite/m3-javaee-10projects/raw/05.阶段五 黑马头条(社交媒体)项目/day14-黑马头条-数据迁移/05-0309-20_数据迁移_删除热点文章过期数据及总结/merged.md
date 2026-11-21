# 20_数据迁移_删除热点文章过期数据及总结

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\20_数据迁移_删除热点文章过期数据及总结【海量资源尽在 666java.com】.mp4
- 时长 6分0秒（音频 361s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面咱们就来完成最后一块内容就是说定时删除过期的热点数据这个应该是比较简单的前面只需要去做一个定时去调一下Service方法就可以好吧首先咱们在这还得去创建一个这种定时的任务的类咱们在这去创建创建class然后让他去干嘛呢让他去继承当前的sobstract jobctrl i实现两个方法是吧
[00:32] 然后第一个呢咱们要去在这去加一个compound然后是加个log4阶度行再加一个这个注解也可以那行那这样就加完了加完之后呢这个时间咱们该怎么去设置呢这个咱们可以设置一个晚上的10点30分晚上10点30分啊10点30分怎么设呀首先是0然后是3020星星
[01:03] 那这样的话咱们就算是设置完了这是每天晚上的22点30分就会去执行一次去删除那删除什么呢删除当前的过期的数据可以在这再去加个东西比如说system先去记录时间好这是时间咱们在这去loginfo然后是开始删除数据库过期数据当然这个主要针对的是
[01:36] 热点的文章在这可以去封装一个方法deletexti这是过期hotdate没有参数这个方法咱们可以去创建出来就在下边这个咱们可以再去应用日志拷贝这是什么呢删除数据库过期数据完成结束吧
[02:11] 然后是耗时加上system它可以减去好了啊那这个加完之后呢下面咱们主要是写这个逻辑就可以了这是删除过期数据过期数据这时候呢你需要去注入一个Service这个Service是谁啊这个Service呢就是当前的什么jp hot article Service这里边呢其实有一个删除的方法啊好
[02:49] 那你删除之前呢你首先呢你得先查出来先查啊用当前的AP HALT Article Service点有一个叫做slack的过期的时间查询上个月的时间查询上个月的数据啊这时候呢就能拿到一个list是吧然后呢你就可以去建立当前的listif non不等于当前的这个HALT Article List并且非HALT
[03:19] ArticleList.isEmpty 它不为空那这时候呢你就可以去做循环HotArticleList.do拿到了对象之后呢你就可以去调用JP HotArticleService.有一个叫做delete什么deleteHotData就是这个对象装进去可以了好吧那这样的话咱们就算是删除了数据好吧那行那这个就不测了啊就是这东西比较简单啊你直接可以自己测一测主要呢是这个时间呢你可以自己设一个什么呢
[03:49] 设一个自己的时间比如说咱们要是设置每两分钟或者每三分钟我每一分钟都可以去执行一下然后呢你可以看一下这个效果是吧这个查询的是上个月的时间呃这个数据然后呢你把这个数据给删了就可以了好吧呃那行那这个查完之后啊那这个那种啊咱们这个整个的呃那种迁移的过程就做完了那做完之后啊这块并没有去应用是吧你看啊当前的这份内容当前的
[04:16] 比如说全量的数据我是从当前的数据库去查询查询完之后我是保存到了HBase是吧然后第二个就是咱们还会去做一个热点数据还有一个文章审核的数据这个热点数据咱们又去存储到了当前的什么当前的这种MongoDB中是吧那这时候你要在文章去查询的时候特别是热点文章查询的时候你要去查询就要去从哪从Mongo中去查因为现在Mongo中也有许多数据所以说你要从这里边去查
[04:45] 那这样查的话呢肯定要比买色口红要快一些所以说呢这个呢你需要去做一个改造那改造的方式呢其实都是通过谁啊通是通过当前的什么这个测试咱们之前是讲过这个mongo template是吧你通过它啊注入完之后呢你可以去查询那你怎么查呢就是最终的是能够查询当前那个封装的对象就可以最终把这个对象呢再去解析成你想要的对象其实都是跟这个有关系都是跟它有关系啊这里边其实已经
[05:16] 包含了当前的这四块内容看到了吧文章列表和文章详情所需要的所有的内容啊都已经在里边去包含了你主要是从这个文章啊从这个实体内容去解析成这四个对象就可以了好吧那行那这个你们只是提供提供一个思路但是迁移的过程咱们是讲完了啊大家的主要的是重点掌握的是哎在项目中为什么要迁移那迁移有什么好处是吧然后迁移完之后呢那这个有什么有有什么样的这种
[05:45] 问题是吧比如说你有类型是吧你怎么去组装怎么去组合是吧好这个效率上可能会提高是吧你怎么去再怎么去查询好吧那行那这个呢就是一个整体的一个迁移的过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.fs.FileStatus;
import org.apache.Hadoop.fs.FileUtil;
import org.apache.Hadoop.fs.FileSystem;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import

