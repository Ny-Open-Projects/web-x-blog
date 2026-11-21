# 15_爬虫文章审核_定时任务调用方法编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\15_爬虫文章审核_定时任务调用方法编写【海量资源尽在 666java.com】.mp4
- 时长 5分41秒（音频 341s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去完成这三个方法啊去审核啊那最主要审核的呢其实是咱们下面这个东西啊下面这个那你说上面这两个是干嘛的呢来我给你说一下啊首先呢那这个呢是在去咱们呢会去设置一些什么呢设置一些定时任务去自动审核那这个呢是在爬虫的文爬虫爬虫的时候啊爬去的文章
[00:26] 每爬出一条咱们要去选用这个方法去接收消息啊去审核但是呢以防万一啊万一你有的东西没有审核咱们再用这个方法去低声重入去跑一遍那再去跑一遍啊再去查看一下当前状态唯一的咱们再去审核一遍这都听明白吧好了啊那这个呢咱们就说明白了啊然后下面咱们就依次来去写列方法啊首先呢只需要去查一下什么状态唯一的就可以
[00:55] 好吧呃这样咱们又咱们首先呢在这去注入一个mypro叫crnewsmypro好注入他然后呢是他然后在这你可以直接去调用点儿有一个叫做flagged list这个猜数啊其实是一个crnews但是这个不是是吧加一个东西呗一个什么fuel per warning啊在这再加一个log4j2好吧行那这个
[01:26] 这个其实是一个空的,CLnews,是空的,叫CLnews你看它应该是只有一个状态状态是1,CLnews.setStatus没有Status吗?
[01:43] type吗?
[01:44] 应该是有Status,稍等,我先找一找.set,干什么,有Status嘛这样你设置为1,当然它是一个byte你直接是强转一下就可以了,好吧
[02:01] 那这样的话你就可以把当前的clnews作为条件去查询那这样他查询出来的东西是啥查询出来的东西所有的东西都是啥都是状态唯一的数据对吧这时候咱们就可以去审核了那啥呢说none不等于当前的clnews list并且呢并且是它不为空clnews list.is empty然后咱们就可以去做一个循环
[02:33] 但你也可以先在这打印日是吧提示一下定时任务自动审核检索检索未审核数量绕是吧数量数量是多少呢看一下当前的clnewslist.size最终咱们就可以去复尔循环一下clnewslist.size
[03:08] 点负好拿到它之后呢是吧咱们就可以调用auto就把当前这个news装进去就可以了让它去进行审核那这是一个啊那个要是为空的话呢咱们也可以去在这去设置一下说log.info定时任务自动审核会检索出数据会检索出数据
[03:43] 好了那这样的话这个方法咱们就设置完了啊然后呢咱们下面再去写第二个方法好吧这个方法也是比较简单的啊他呢也是会调用下面这个方法啊其实最核心的方法应该是下面这个啊然后呢咱们接着往下写这个怎么写呢Pace呢也是要去封装条件封装条件啊怎么封装呢其实还是要去创建一个CL News然后呢CL News等于Nu一个CL News然后呢然后你要去查询
[04:13] 查询一个就可以了clnews.setidid其实就是当前clnewsid就是你传过来的clnewsid好第二个它必须是什么必须是setstatus必须状态是1这样的话我才去审核我们还是要好吧好这时候你就可以去查询了
[04:44] CLnews.mypr.dr我们有一个slack的byid and status一个参数呢没有这个参数就直接对象传进去就可以了这样就能拿到一个对象叫CLnewsCLnews1吧CLnews吧也行这个行不了吧其实无所谓是吧最终的你也可以去照用前线这个方法
[05:15] 它不会空我们在这去判断一下说None不等于当前的当前的CL News 1然后呢我就可以让它去调用下边这个方法当前这个CL News 1装进去可以了那行这两个方法其实都已经写完了其实重点出来了重点的话就是下边这个方法

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 的 Mapper 接口，实现对新闻文章的自动审核功能，包括创建实体、配置 Mapper、编写 Service 逻辑和调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，选中 ReviewCrawlerArticleServiceImpl.java 文件，准备编写自动审核逻辑。
画面 2: 选中方法 autoReivewArticleByCrawler，准备编写具体实现。
画面 3: 在方法中声明私有成员变量 @Autowired CNewsMapper cNewsMapper。
画面 4: 在方法中调用 cNewsMapper.selectList() 方法，准备查询未审核文章。
画面 5: 在方法中调用 cNews.setXXX() 方法，准备设置新闻实体属性。
画面 6: 在方法中调用 cNewsMapper.selectByIdAndStatus() 方法，准备根据 ID 和状态查询。
画面 7: 在方法中声明并初始化日志对象 log。
画面 8: 在方法中创建 CNews 对象，设置状态，调用 selectList 查询未审核文章，打印日志。
画面 9: 在方法中使用 for 循环遍历未审核文章列表，调用 autoReivewArticleByCrawler 方法进行审核。
画面 10: 在方法中调用 autoReivewArticleByCrawler 方法，准备传入 CNews 对象。
画面 11: 在方法中调用 cNewsMapper.selectByIdAndStatus() 方法，准备根据 ID 和状态查询。
画面 12: 在方法中调用 cNewsMapper.selectByIdAndStatus() 方法，准备根据 ID 和状态查询。
画面 13: 在方法中调用 cNewsMapper.selectByIdAndStatus() 方法，准备根据 ID 和状态查询。
画面 14: 在方法中调用 cNewsMapper.selectByIdAndStatus() 方法，准备根据 ID 和状态查询。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Service
public class ReviewCrawlerArticleServiceImpl implements ReviewCrawlerArticleService {
    @Override
    public void autoReivewArticleByCrawler() throws Exception {

    }

    @Override
    public void autoReivewArticleByCrawler(Integer cNewsId) throws Exception {

    }

    @Override
    public void autoReivewArticleByCrawler(CNews cNews) throws Exception {

    }
}
```

画面 3:
```java
@Service
public class ReviewCrawlerArticleServiceImpl implements ReviewCrawlerArticleService {
    @Autowired
    private CNewsMapper cNewsMapper;

    @Override
    public void autoReivewArticleByCrawler() throws Exception {

    }

    @Override
    public void autoReivewArticleByCrawler(Integer cNewsId) throws Exception {

    }

    @Override
    public void autoReivewArticleByCrawler(CNews cNews) throws Exception {

    }
}
```

画面 8:
```java
@Service
@SuppressWarrings("all")
public class ReviewCrawlerArticleServiceImpl implements ReviewCrawlerArticleService {
    @Autowired
    private CNewsMapper cNewsMapper;

    @Override
    public void autoReivewArticleByCrawler() throws Exception {
        CNews cNews = new CNews();
        cNews.setStatus((byte)1);
        List<CNews> cNewsList = cNewsMapper.selectList(cNews);
        if(null != cNewsList && !cNewsList.isEmpty()){
            log.info("定时任务自动审核剩余未审核数量：0",cNewsList.size());
            for (CNews news : cNewsList) {
                autoReivewArticleByCrawler(news);
            }
        }else{
            log.info("定时任务自动审核剩余未审核数量：0");
        }
    }
```

画面 9:
```java
@Service
@SuppressWarrings("all")
public class ReviewCrawlerArticleServiceImpl implements ReviewCrawlerArticleService {
    @Autowired
    private CNewsMapper cNewsMapper;

    @Override
    public void autoReivewArticleByCrawler() throws Exception {
        CNews cNews = new CNews();
        cNews.setStatus((byte)1);
        List<CNews> cNewsList = cNewsMapper.selectList(cNews);
        if(null != cNewsList && !cNewsList.isEmpty()){
            log.info("定时任务自动审核剩余未审核数量：0",cNewsList.size());
            for (CNews news : cNewsList) {
                autoReivewArticleByCrawler(news);
            }
        }else{
            log.info("定时任务自动审核剩余未审核数量：0");
        }
    }
```

画面 10:
```java
@Service
@SuppressWarrings("all")
public class ReviewCrawlerArticleServiceImpl implements ReviewCrawlerArticleService {
    @Autowired
    private CNewsMapper cNewsMapper;

    @Override
    public void autoReivewArticleByCrawler() throws Exception {
        CNews cNews = new CNews();
        cNews.setStatus((byte)1);
        List<CNews> cNewsList = cNewsMapper.selectList(cNews);
        if(null != cNewsList && !cNewsList.isEmpty()){
            log.info("定时任务自动审核剩余未审核数量：0",cNewsList.size());
            for (CNews news : cNewsList) {
                autoReivewArticleByCrawler(news);
            }
        }else{
            log.info("定时任务自动审核剩余未审核数量：0");
        }
    }
```

画面 13:
```java
@Service
@SuppressWarrings("all")
public class ReviewCrawlerArticleServiceImpl implements ReviewCrawlerArticleService {
    @Autowired
    private CNewsMapper cNewsMapper;

    @Override
    public void autoReivewArticleByCrawler() throws Exception {
        CNews cNews = new CNews();
        cNews.setStatus((byte)1);
        List<CNews> cNewsList = cNewsMapper.selectList(cNews);
        if(null != cNewsList && !cNewsList.isEmpty()){
            log.info("定时任务自动审核剩余未审核数量：0",cNewsList.size());
            for (CNews news : cNewsList) {
                autoReivewArticleByCrawler(news);
            }
        }else{
            log.info("定时任务自动审核剩余未审核数量：0");
        }
    }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

