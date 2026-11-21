# 17_数据迁移_定时同步全量数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\17_数据迁移_定时同步全量数据【海量资源尽在 666java.com】.mp4
- 时长 7分36秒（音频 457s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面咱们就来去完成哪一块内容就是完成这个内容首先咱们要去做一个定时同步全量的数据你看这个步骤首先咱们要去做一个定时任务然后去查询未同步的文章然后再去保存到HBase其实这两步咱们已经做完了咱们主要是做一个定时就可以然后让他去查询未同步的文章然后再去保存到HBase中就可以
[00:30] 好吧那下面呢咱们就来去写一下当前这个定时任务啊那个定时任务可以看一下啊咱们就是跟之前是一样啊首先呢你得让当前的这个迁移系统呢首先得去引入当前的哪个quad是吧你得去引入quad啊然后呢你就可以在这去创建一个job比如说咱们叫job然后咱们是名称是啥呢叫他然后呢咱们就可以在这啊
[01:04] 这列上的去弄一些东西让他去干嘛呢一场当前的opus track的照好有两个方法咱们需要去写一下啊但是当然在这去加注解compound然后是他哎是这个吗不是啊应该是当前的这个东西啊disable current的一个sup 人就他然后呢还有一个log4j怎么加上啊log4j2好加完之后啊那这个干嘛呢这个
[01:34] 这个是不是就是要去设置一个这种你的表达式比如说咱们是0我先这么写两分钟执行一次是星星星好吧咱们先测试测试的话你可以这么找可以这么找你要是正式环境的话你可以去设置为一个比如说每天晚上的十点半或者说每天凌晨的两点OK那这样的话都可以设置咱们测试方面咱们就先去设置一个
[02:03] 这种每两分钟执行一次好吧那下面呢咱们就可以直接去调用一个什么叫db to hbase并且是没有参数的因为这个要查询的就是什么未审核的所有的文章啊好咱们在这儿去加个东西log.info开始同步文章数据到哪儿啊hbase然后下面咱们可以再去做一个
[02:34] 同步文章HBase完成然后呢你就可以在这去注入一个serviceService是哪个serviceprivate一个叫做articlearticlequartity没有吗怎么叫articlequartity吗articlequartityservice然后呢是把它注进来注进来之后呢这里边有个方法就是这个方法点儿有一个to
[03:09] db2 space应该是第二个啊因为这个呢是没有参数的好吧那行那这个设置完之后啊下面呢咱们就可以干嘛呢就可以去启动项目啊让他呢去执行好在这呢打个断点啊当然了您得去在这去检查一下啊检查哪个呢就是检查你的表啊数据有没有找到当前的这个然后你找到谁呢找到当前的这个把这数据啊
[03:39] 就是当前的这个迁移数据里面的数据呢所有的要删掉清空啊不见清空啊当然这个还要再去检查一下检查哪个检查当前的这个照报底才有啊这里边还有数据啊应该删掉不要了好然后呢咱们就可以去启动当前的这个微服啊右键咱们直接debug当然你可以看一下当前的mycat必须启动啊好启动了好debug启动
[04:14] 稍等下好这项目启动完了启动完之后这个中间的是没有报错啊怎么等一等啊等一等等两分钟然后呢就能去走执行到这儿然后咱们再去看一下效果好吧看看下面没有报错啊但你也可以去刷新下当前数据库看看有没有创建数据刷新你看这数据是不是刚刚创建的呀这个呢就是刚刚咱们创建那个照片看到了吧有问题啊那等着等着他呢是吧到这之后呢咱们再去执行
[04:47] 好那这个断点来了啊你可以看一下咱们可以往下去执行但是你执行之前的你最好的是先去准备一些数据比如说我去找到当前的article表我把这个先关了啊找到当前的mycat连上然后是找到它你找到当前的AP article我这块就是去做了一些数据啊这个数据的话只剩了几条并且呢我让这几这几条啊都是00的话呢就是未同步的数据啊
[05:18] 好那这样的话呢咱们去保存再刷新一下的确是零然后呢咱们就可以去往下去执行比如说我在这打那点让他过来好来了啊之后呢那这一步啊其实呢就是去查询什么呢查询数据并组装成当前的这么一个集合是吧你可以点进去看一看啊打到这好啊往下走这一步呢就是去查询什么呢未同步的数据你看看能不能查出来好把鼠标放到这
[05:50] 你看是不是有五条数据啊OK没问题啊然后下面呢就是组装就是组装啊那组装呢咱们可以一步步去执行先去组装的是啊我先走啊然后再往下呢是去执行了啊然后这这个呢就是去组装了组装完之后呢你可以看一下这里边有没有数据呢哎看里边是不是有数据啊那有数据的话呢下面呢咱们就最终就能返回好往下走走好那这一步就能查到数据那查到数据之后啊
[06:18] 首先咱们做了一个事就是先把数据可以转换一下转换成当前的一个集合这个集合叫做HBase Storage的一个例子然后你再把所有数据存到哪存到当前的HBase中你可以看一下到底能不能执行成功先去转换好转换是没问题你可以看一下里边到底有什么数据把数据放到这这样在这看一下你看这里边是不是有五条数据
[06:50] 分别是什么Rookie是谁然后的Datalist里边他会告诉你这个是AP article的然后第二个是什么Config的然后第三个还有什么Content还有一个authorauthor在这好这里边分别对应了他还有他具体的数据明白了吗具体的数据都给你去封装了好吧这是他的column这是他的value好了最终咱们看他能不能保存成功就可以了往下走稍等
[07:23] 你看是不是正常过去了那正常过去之后呢就说明我这边干嘛呢已经把数据添加到哪啊Hbase中了OK那到此为止呢咱们这个同步呢就算是说完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

