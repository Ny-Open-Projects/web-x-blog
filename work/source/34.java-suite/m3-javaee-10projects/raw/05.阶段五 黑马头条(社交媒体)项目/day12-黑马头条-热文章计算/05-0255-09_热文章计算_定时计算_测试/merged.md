# 09_热文章计算_定时计算_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\09_热文章计算_定时计算_测试【海量资源尽在 666java.com】.mp4
- 时长 3分45秒（音频 225s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去测试一下测试之前呢你首先呢得先去把当前这个redis给开启还要把minecat给重启一下好吧因为你刚才呢干嘛呢因为你刚才呢是修改了当前的这种scammer的文件是吧那行那这个重启完之后那非常简单了就啊你想测试你直接去右键当前的debug这个项目就可以了好吧让这个项目启动起来它就会每两分钟去执行一次当前这个东西
[00:30] 咱们在这咱们在这打断点好吧咱们在这边的也打断点啊咱们一会去debug一遍如果说有不熟的话咱们可以再看一看啊好那现在已经过来了啊咱们可以往下看啊往下走这时候呢他就是开始计算分值是吧好往下走这时候呢你直接跳过他就能到这那到这之后啊你看啊首先呢他是要根据那个昨天的时间是吧你可以看啊当前的last day
[00:55] 其实就是昨天的时间是吧然后呢去根据这个条件呢去查询当前的article list好往下查那这时候这个数据啊有可能会没有我在这儿是准备了三条数据你看根据当前的时间啊我是10月30号啊好这是根据当前的时间去查询的然后呢你看啊然后怎么办呢然后我在这儿啊这块的分值它也是没有的分值啊
[01:26] 分别是阅读这种评论还有收藏还有点赞前面这三项都一样只是点赞的数不一样一个是2一个是1一个是3那肯定是当前的这条排在第一这个是排在第二这个是排在第三是吧这分数是多少3加25加38加19分别是8分别是7好吧
[01:53] 那行那咱们下面就来去看一下这个分值的计算好吧好往下走一下行那这个分值其实已经计算完了那计算完之后你可以看一下当下那个hot article list看看它有没有排序应该存在的第一条的值是不是9没问题那第二条呢可以看看第二条是不是8第三条那就是7是吧没问题行那这个数据咱们就算是
[02:20] OK啊这块是没有问题的啊然后下面呢他就会去进行保存啊当然不是啊先去缓存当前的频道啊往下走好没有包错了没有包错就没有问题啊然后你可以再往下问一下看啊这会这个是为每一个用户去保存一份热点文章然后往下走先去保存的是文章的一般信息啊那有同学说那这个保存了一次那下边怎么又保存了一次呢保存两次原因是这样啊那第一次保存的是通用的一些数据
[02:50] 比如说这个用户是第一次登录那你说不太推荐吗也推荐也推荐所以说这是通用的一些文章然后下面是给咱们每一个用户再去设置文章的信息做一个关联而已好 我先走好 这个说完了说完之后你可以打开这个表去给他看一下刚才我这是空的好 刷新一下他就会去插入那么多数据刚才说了
[03:18] 因为有的呀它是没有什么的没有entry ID的啊是0的0干嘛呢0的都是一些默认的0都是默认的值啊然后像这些1234的都是什么呢都是当前的每一个什么根据当前的entry ID去设置你看entry ID你看这个是不是设置了好多条数据啊OK啊那行那这样的话咱们就算是设置完了啊哎把这个停了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

