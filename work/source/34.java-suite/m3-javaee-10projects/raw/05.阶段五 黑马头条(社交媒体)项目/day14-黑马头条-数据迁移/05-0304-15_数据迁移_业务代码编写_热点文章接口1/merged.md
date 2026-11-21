# 15_数据迁移_业务代码编写_热点文章接口1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\15_数据迁移_业务代码编写_热点文章接口1【海量资源尽在 666java.com】.mp4
- 时长 6分56秒（音频 417s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们继续这里边还有一个接口就是热点文章的接口这是最后一个接口了咱们要去编写一下咱们可以看一下里边的方法首先第一个是要查询根据条件查询热点文章然后是要去插入文章热点文章还有什么就是要去热数据同步这个同步的话主要是查询
[00:23] 这个同步的时候咱们可以从当前的文章数据库或者是当前的哪HBase中去查询并且是插入到哪插入到Mango中还有一个就是删除文章还有是查询过期过期的话就主要是上个月还有一个是根据当前的这种删除就删除那行那这个咱们设置完之后咱们下面就来去写一下当前的结果拷贝一下
[00:53] 然后是没用的都可以先关掉一会再测怎么马上就要测试了这个接口好后在这去定义方法一个是public然后咱们要去查询list回头是一个AP-HOT-articles然后是什么是叫做select list好吧这里边参数就是AP-HOT
[01:25] ap hot articles然后下面接着往下看还有一个插入void insert就是谁呢ap hot articles好是一个插群一个插入然后下面还有一个同步public void hot然后是ap ti cli然后是sync好吧
[02:02] 这条件就是当前的什么article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里面的 article id, 里
[02:35] 是void,然后是deleteid,是有一个integer的id这是删除还有一个查询过期的过期的话是返回这个集合啊jp hot articles然后是select espire然后是没有参数当然这个查询过期的时候呢咱们可以
[03:12] 根据月份去查询这个呢他虽然没有没有参数但是咱们再去拼接circle的时候呢他是有参数的好吧然后接着我先看啊查询过期查询过期的数据过期的数据好吧还有一个是吧还有一个是删除数据根据之前的条件删除public void然后是deleteout
[03:46] 导演就是AP HOT ARTICLES好那这样的话我们就算是设置完了啊那就可以干嘛呢还可以继续啊这呢去加上它的实现类让它去实现当前的AP HOTHOT ARTICLE SERVICECtrl I然后是加一个SERVICE咱们还可以再去加一个啊加一个LOG4J2
[04:21] 那你说这里边需要注入那些东西呢来看啊首先呢咱们要去注入一个mypro这个是没啥可说的啊private然后呢是一个叫做AP hotarticles mypro是吧先把它给注入进来这个应该会报错是吧supra warning好加上之后啊那这里边还需要啥呢还需要一个mongo因为咱们需要去挖mongo种是吧
[04:52] 叫mongo templatemongo template 装进去还有呢那是不是还得去干嘛呢还得去那个从h base中去查询呢所以说咱们在这儿再去进一个就是h base storage client好 这之后呢 咱们注入一个啊里边其实还有一个还需要一个综合的接口是刚才咱们定义这个什么
[05:30] Article Quality Service这个咱们也要去注入也用得着PrivateArticle Quality Service这个注入完之后这时候咱们就算是注入完了注入完之后咱们下面就可以写方法首先是写第一个这个比较简单这个就是从以前的JP HOTArticles ServiceMapper 直接去查询就可以了这个就是当前的
[06:03] ap-out-articlesok完了下面还有一个东西咱们要再去设置一个比较简单的吧根据这个删除是吧删除怎么办呢比较简单的也是调用了ap-out点儿有一个deleteID装进去可以了这里边还有一个叫过期咱们也可以去设置一下也是通过ap-out-myper点儿有一个叫做select这个就是查询的是
[06:35] 上一月份的数据上一月份的数据咱们之前是讲过的那行这个讲完之后这里边还有没有简单的方法吗插入咱们也可以去设置一个插入jp hot mypro.insert我把当前这个语句插入进去完事了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现一个热点文章同步服务，包括定义接口、编写实现类并注入相关依赖。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口定义文件，包含热点文章接口的注释和方法签名。
画面2：在 IDE 中右键点击项目，弹出菜单，准备进行重构或分析。
画面3：在 IDE 中打开 `ApHotArticleService.java` 文件，显示接口定义。
画面4：在 IDE 中，光标位于接口定义的 `insert` 方法后，准备编写实现。
画面5：在 IDE 中，光标位于接口定义的 `hotApArticleSync` 方法后，准备编写实现。
画面6：在 IDE 中，光标位于接口定义的 `selectExpireMonth` 方法后，准备编写实现。
画面7：在 IDE 中打开 `ApHotArticleServiceImpl.java` 文件，准备编写实现类。
画面8：在 IDE 中，光标位于实现类的 `@Service` 注解后，准备编写类定义。
画面9：在 IDE 中，光标位于实现类的 `private` 关键字后，准备声明字段。
画面10：在 IDE 中，光标位于实现类的 `private` 关键字后，准备声明字段。
画面11：在 IDE 中，光标位于实现类的 `private` 关键字后，准备声明字段。
画面12：在 IDE 中，光标位于实现类的 `selectList` 方法后，准备编写实现。
画面13：在 IDE 中，光标位于实现类的 `hotApArticleSync` 方法后，准备编写实现。
画面14：在 IDE 中，光标位于实现类的 `insert` 方法后，准备编写实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
}
log.info("同步数据到HBASE失败，articleId: {}, 状态:{}", articleId,
System.currentTimeMillis() - currentTimeMillis);
}
```

画面3：
```java
package com.heima.migration.Service;

import com.heima.model.article.po.ApHotArticles;
import java.util.List;

public interface ApHotArticleService {
    List<ApHotArticles> selectList(ApHotArticles apHotArticles);
    void insert(ApHotArticles apHotArticles);
    /*
     * 热度级 HBase 同步
     * @param articleId
     */
    public void hotApArticleSync(Integer articleId);
    /*
     * 查询过期的频道
     * @return
     */
    public List<ApHotArticles> selectExpireMonth();
}
```

画面7：
```java
package com.heima.migration.Service.impl;

public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面8：
```java
@Service
public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面9：
```java
@Service
@Log4j2
public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面10：
```java
@Service
@Log4j2
@SuppressWarnings("all")
public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面11：
```java
@Service
@Log4j2
@SuppressWarnings("all")
public class ApHotArticleServiceImpl implements ApHotArticleService {
    @Autowired
    private ApHotArticlesMapper apHotArticlesMapper;
```

画面12：
```java
@Service
@Log4j2
@SuppressWarnings("all")
public class ApHotArticleServiceImpl implements ApHotArticleService {
    @Autowired
    private ApHotArticlesMapper apHotArticlesMapper;
    @Autowired
    private MongoTemplate mongoTemplate;
    @Autowired
    private HBaseStorageClient hBaseStorageClient;
    @Autowired
    private ArticleQuantityService quantityService;
```

画面13：
```java
@Override
public List<ApHotArticles> selectList(ApHotArticles apHotArticles) {
    return apHotArticlesMapper.selectList(apHotArticles);
}
```

画面14：
```java
@Override
public void insert(ApHotArticles apHotArticles) {
    apHotArticlesMapper.insert(apHotArticles);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

