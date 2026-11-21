# 19_爬虫文章审核_文章等信息保存

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\19_爬虫文章审核_文章等信息保存【海量资源尽在 666java.com】.mp4
- 时长 16分36秒（音频 997s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就把这个文章的信息给保存一下那这个文章信息呢咱们首先呢不能直接保存应该先去查一查查完之后呢如果说没有的话咱们再去保存操作啊是这么个思路咱们现在在这先去注入一个当前的AP author myper拿到myper之后呢咱们再去做操作啊接着呢咱们在这直接去查就可以了.er有一个slack的author nameclnews
[00:29] 这样的话就是一个文章的名文章的作者名称啊我去拿到了当年一个AP author然后这时候呢你又可以去计算啊看啥呢AP author不等于num并且呢嗯他写吧看的是等于等于num啊等于等于num或者是什么呢AP author.getid他等于等于num这两个等于等于num的时候呢就说明他是真为num啊这时候呢咱们就可以去
[01:01] new出来一个他那new出来为啥呢就是为了能够要保存备ap author.set什么set一个corridor time他们就是有一个new一个date然后下面还有ap author.set name就是servernews.get name好吧然后再往下ap author.set一个什么type这个type是0啊这个0啊0的话就说明是爬虫
[01:32] 还有什么吗我可以看一下里边就这三项是吧这时候咱们就可以直接去保存了保存的话就用ap-author-my-pro.insert就把当前这个ap-author放进去就可以了最终你把它给返回给punap-author好这个我要在这去多说一句话这份内容咱们一开始写的时候mypro
[02:03] 这块是有一个主件因为我文章保存的时候需要用到文章的当前作者的ID所以说这会是有一个主件返回大家一定要别忘了行这个是拿到了拿到完之后下面咱们就来去设置文章的内容文章的话咱们也可以在这去直接去先在这去注入一个mypr
[02:33] 然后是aparticlemypro好好注进来之后呢在这儿你就可以去new一个aparticle等于new一个ap他然后下面呢就往里边去设置就可以了aparticle.set我们有一个channel id先把这channel id给设置进去好吧然后再往下aparticle.setchannel name把这channel name也设置进去然后呢下面还有什么呢
[03:08] article.set有一个叫做authoridauthorid的话其实这份内容里边咱们传了一个authorid所以说你在这直接去把authorid装进去就可以了integer一个lang这样你new一下new一个lang就可以了new一个lang然后把这个
[03:36] 你开个重新构造一下就是个量子型好吧然后再往下看aparticle.set什么呢set一个叫做author name知道吗这时候咱们就可以通过谁拿叫clnews.getname这个其实就是作者的名称好再往下看aparticle.set这个就是clnews里边的gettypegettype好吧
[04:05] 接着往下看,这一块是int,是一个short,我们用这个强转一下,好,就可以了啊那下面接着往下看,aparticle.setPublishName,咱们用clnews.getPublish接着往下看,set什么呢,set什么呢,autonym,authored
[04:34] Channel ID, image 4, image 4没有啊咱们用u数去设置,title设置一下title是clnews.gettitle接着往下看,然后aparticle.set还有啥这些好像都不用怎么去设置了是吧这个呢是有一个orange咱们设置一下这是来源,来源的话咱们可以给一个force接着往下看aparticle.set
[05:10] 还有啥呢?
[05:11] 来看一看啊一个createTime是不是没创建呢?
[05:16] 好,我们就在这去设置一个new date好,最后一个咱们再去设置一个aparticle.setImage这个必须要设这个是谁呢?
[05:29] 其实这个呢并不是你传过来的images它是一个集合它是一个string所以说呢咱们在这要去处理一下
[05:40] 怎么处理呢就是要去从当前这个图片中去截取几张图片放到这里边就可以了那你该怎么去拿呢你看啊这样拿啊咱们在这去循环一下吧好吧比如说咱们要image先判断一下吧说呀none不等于当前的image然后并且呢image.isEmpty这时候呢咱们就可以去循环for别for了好吧
[06:13] 我们就要去取三张怎么办呢直接用for情况去取啊in i 等于0i 小于谁啊imageS 以 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告 广告
[06:40] 这时候咱们可以用一个容器去装一下std builder sb 等于他new一个std然后这个图片多个图片之间咱们需要用逗号分割所以说咱们在这先去处理一下说等于0然后下面咱们就可以去设置一个sb.append然后先去加一个逗号然后最后再去把sb.append什么
[07:11] 把当前的image.geti放进去就可以了那这样的话咱们就算是设置完了最终呢你把这个数据sp.tools这个内容就算是放进去了好了最后呢就可以用aparticlemypro.insert把它进了aparticle放进去就可以了那到目前的话咱们这个算是这个文章内容咱们就算是保存完了
[07:43] 那咱们就继续啊继续啊这个lib咱们一会儿再保存用这个稍稍微比较复杂一些啊咱们先把这两个给保存一下好吧那这个呢就是当前的一个配置这个还是比较简单的啊咱们可以直接在这扭一个ap article.tsleconfig然后呢是扭出来一个他好之后呢你就可以往里面去设置呗好吧ap articleconfig.set一个什么叫做
[08:15] article id这个呢就是aparticle.getid好吧然后接着往下看啊aparticleconfig.aparticleconfig点什么呢点一个叫做不是咱们的功能是吧是否转发是吧我们可以设置为转发的话咱们就可以设置为可以转发啊都是aparticleconfig点什么呢有一个叫做isdelete
[08:48] 能删除吗?
[08:48] 不能,可以是这个force然后再往下,aparticleconfig.set一个command是否收藏呢?
[08:52] 可以,可以收藏然后再往下看,aparticleconfig.set一个mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
[09:18] private ap article config mypro好 发出来之后呢这时候你就可以在这去直接去这家insert就可以了好吧就把当前那个ap article config装进去好最终呢你把当前这个ap article返回就可以了好吧那就是完之后啊那么下面呢咱们继续往下看啊还有一个contentcontent的话其实也比较简单啊ap article content
[09:51] 有啊好好于你有一个他然后这里边授职比较简单啊有两个职第一个一批article content的article id要去顺便上前的文章然后第二个呢就是内容了啊那一批article content这个呢就是那种啊嗯行那这个试完之后啊试完之后呢咱们下面呢就可以去保存了啊那保存的话呢
[10:23] 这块呢同样也需要去输入一个mypl是什么AP article content mypl找一找这时候呢就可以去保存点一个什么点有一个叫做insert就把当前的数据保存就可以了那咱们下面呢也拔了一个标签呢也可以保存了啊那表保存标签呢其实呢咱们要去解析当前的AP article里边的一些labels
[11:01] 因为目前的话这个AP article已经保存了它这个里边是有值的在这先去判断一下咱们主要的是拿到什么呢拿到AP article它不等于none并且呢string.youtube.isnotamplied是AP article的什么get labels它不等于none的时候我们要去解析这里边的数据
[11:29] 他这个存的是当前label的ID值你可以看一下当前label是一个是AP article另外一个是label ID然后第三个是count只是没有什么太大的意义只是一个排序好吧咱们每次要去增一就可以然后下面咱们就来去写那这时候既然他知道他存的时候是有什么看一下他存的时候labels找一找
[11:58] 当这里边是没有是吧没有数据啊我可以告诉你啊里边存的是一个二个三个四个啊是这样的一个地址所以说你要怎么怎么办呢得先去你得先去截取先去截取啊用前的ap article.dat labels.split就用当前的作坏去分割分割完之后啊就能去拿到一个label好
[12:28] 拿到这个array之后呢,我们就可以去循环了label array,label array,R4拿到这个呢,就是label的什么label的ID拿到label的ID之后呢,咱们就可以去查询查询的话,咱们需要通过两个条件查询一个是AP article,另外一个是一个是AP article的ID另外一个是label ID,怎么办呢这时候你要去构建一个对象
[12:59] 你先这样先去在这先去注入一个private然后是有一个ap articleap article 没有吗ap article 拿到这个mypr之后你可以去直接去有一个叫做select
[13:31] slack的list那这里边传的就是一个AP article label这样啊咱们在这去构建一下叫AP article label等于你用一个AP article label其实里边有一个构造的函数你直接用这个构造函数传值也行D然后第二个呢就是label ID这一块有问题是吧咱们用当前的一个integer点pass
[14:01] 就把后边这个值啊放到这里边这样就可以了啊装里边之后呢你把这个这个东西啊放这它就能返回一个集合其实那里边就一条数据好吧再再再咱们在这啊再去判断一下我说none啊不等于当前的它并且呢它呢是不等于空是吧点意思empty然后呢然后去干嘛呢
[14:33] 然后咱们就可以去更新说明这里边有值是吧有值啊如果否则的话呢否则的话咱们要去新增否则就去新增那这个时候怎么办呢我们就可以通过目前的labels.get0其实里边刚才说了就一条数据嘛能拿到一个AP article1是吧然后呢就可以往这个里边AP article1.set一个comp
[15:03] 我把这conn干嘛呢conn是AP article label.get.cont.j1也就是说也又是去做了一个j1操作好吧conn要去更新吧AP article label.mypl.err咱们有一个叫做update就把当前这个AP article label1放进去就可以了好吧这是一步吧然后下面这一步呢
[15:34] 这一步的话咱们就要去设置了怎么办咱们这次如果说他一查没有的话怎么办咱们要去保存了保存的话就是当前AP article这东西aparticle.set一个count默认是s就是1好咱们就可以直接去保存AP articlelabel myport.insert就把AP article label放进去
[16:05] 那这样的话咱们就算是设置完了这个是1注意点这是1然后这个是label那这样的话咱们这个label也算是设置完了那这个还报错是吧来看看这个需要去返回所以说你在这return一个return jp article那这样的话咱们就算是设置完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中编写和调试一个用于保存文章信息的 Service 层方法，涉及作者、文章、标签和图片等实体的持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 编辑器中显示 `ReviewCrawlerArticleService.java` 文件，正在定义 `saveArticleByCrawler` 方法的开头部分，光标位于 `private` 关键字后，准备输入方法体。
画面 2: 方法体中，使用 `@Autowired` 注入 `ApAuthorMapper`，并开始编写获取作者信息的逻辑，包含 `if (authorId == null || apAuthor.getId() == null)` 判断。
画面 3: 光标位于 `private void saveArticleLabel(ApArticle aparticle) {` 方法定义处，准备编写标签保存逻辑。
画面 4: 方法体中，使用 `@Autowired` 注入 `ApArticleMapper`，并开始编写设置文章属性的代码，包括 `apArticle.setAuthorId(new AuthorId(...))`。
画面 5: 继续编写 `saveArticleByCrawler` 方法，设置文章的 `channelId`, `channelName`, `id`, `cNews` 等属性。
画面 6: 编写 `if (null != images && images.size() > 0)` 条件判断，用于处理图片列表。
画面 7: 在 `if` 条件内，使用 `StringBuilder` 拼接图片 URL，并调用 `apArticle.setImages(sb.toString())`。
画面 8: 光标位于 `private void saveArticleContent(String content, ApArticle aparticle) {` 方法定义处，准备编写内容保存逻辑。
画面 9: 方法体中，使用 `@Autowired` 注入 `ApArticleConfigMapper`，并开始编写配置保存逻辑。
画面 10: 光标位于 `private void saveArticleLabel(ApArticle aparticle) {` 方法定义处，准备编写标签保存逻辑。
画面 11: 方法体中，使用 `@Autowired` 注入 `ApArticleLabelMapper`，并开始编写标签保存逻辑。
画面 12: 在 `for` 循环中，创建 `ApArticleLabel` 对象并调用 `apArticleLabelMapper.selectList()`。
画面 13: 在 `for` 循环中，调用 `apArticleLabel.setCount(apArticleLabel.getCount())`。
画面 14: 方法体中，调用 `apArticleMapper.insert(apArticle)` 并返回 `apArticle`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private ApArticle saveArticleByCrawler(List<String> images, Integer channelId, String ch
```

画面 2:
```java
@Autowired
private ApAuthorMapper apAuthorMapper;

private ApAuthor saveAuthor(Clickers cNews) {
    if (authorId == null || apAuthor.getId() == null) {
        apAuthor = new ApAuthor();
        apAuthor.setCreatedTime(new Date());
        apAuthor.setAuthorName(cNews);
    }
}
```

画面 3:
```java
private void saveArticleLabel(ApArticle aparticle) {
```

画面 4:
```java
@Autowired
private ApArticleMapper apArticleMapper;

private ApArticle saveArticleByCrawler(List<String> images, Integer channelId, String ch
```

画面 5:
```java
private ApArticle saveArticleByCrawler(List<String> images, Integer channelId, String ch
    ApArticle apArticle = new ApArticle();
    apArticle.setChannelId(channelId);
    apArticle.setChannelName(channelName);
    apArticle.setAuthorId(new Long(authorId));
    apArticle.setAuthorName(cNews.getNews());
    apArticle.setOrigin(cNews.getOrigin());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());
    apArticle.setPublishTime(cNews.getPubTime());

