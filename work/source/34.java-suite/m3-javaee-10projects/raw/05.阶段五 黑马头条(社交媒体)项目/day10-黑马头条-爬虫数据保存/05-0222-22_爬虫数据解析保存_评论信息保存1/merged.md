# 22_爬虫数据解析保存_评论信息保存1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\22_爬虫数据解析保存_评论信息保存1【海量资源尽在 666java.com】.mp4
- 时长 14分13秒（音频 853s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去完成当前这个评论数据的添加首先呢咱们在这还是要去做啊那这个评论啊跟咱们之前做的这种附加信息啊还有是那些的文章啊都稍微有点不一样那有哪些不一样呢就大家想一想咱们之前去抓文章的时候有没有去抓取评论数据呢想一想是不是没有啊
[00:26] OK啊那没有的话怎么办呢咱们还得需要去重新去抓取重新抓取啊你首先是要获取到当前的评论的链接拿到链接之后呢再去重新抓取获取内容然后呢咱们再去解析内容然后是存储就这么些步骤好吧那行那咱们下面呢就来去先去写一下咱们下面呢就怎么着呢还是跟之前一样system.2
[00:56] 拿到一个时间然后是记录一下呗我说呢说是开始获取文章评论数据然后下面咱们就可以去封装一个方法比如叫get command就mm然后是date参数是谁参数的话呢实际上参数是就是就他就可以了没有必要呢再把这个salesnews再装进去
[01:28] 它的只是封装当前一个列表因为这个屏幕有可能会有多个所以说这里边有这里边是有一个什么CL NewsCommand就是它然后这是Command List然后拿到之后它这里边还需要去关联当前的文章数据所以说咱们在这再去做一个循环再去做循环循环的作用主要就是把它重新设立一个ID
[02:01] 比如说none等于当前的comment list并且呢fee是吧不等于空comment list is empty如果说它不等于空的话呢这时候呢咱们就可以去循环了啊循环的方式就是comment list.foo拿到它之后呢咱们就可以条一条的进行去添加Zeronews command
[02:33] 那这个呢就是好那就设置完了啊设置完之后呢你就可以去添加数据了啊那这时候呢咱们可以去再去注入一个这种Service哪个呢有一个command Service没有什么什么叫color吗我看看啊
[03:05] command serviceuse command Service就它啊行拿到之后呢咱们在这去注注入完之后啊这你就可以去干嘛你就可以去保存了啊点有一个save colorcommand use command啊直接去把当前这个放进去就可以了这样就保存了啊保存完之后呢你在这去打一个日志说你已经完成了啊说获取
[03:37] 文章评论数据完成耗时多长时间我们要去设置一下耗时然后呢在这去写一个system他点去他行那这个设置完之后下面这个方法咱们要去创建一下那这个方法里边咱们就要去设置两大步对吧两大步其实你也可以设置成三步三步咱们要获取
[04:11] 获取评论列表啊应该是三步啊第一步呢第一步是构建评论的URL对是构建评论URL啊然后是拿到URL之后呢是发送请求发送请求获取数据好还有第三步啊第三步三步呢其实就是解析获取的JSON数据为什么说JSON数据呢因为这次啊
[04:42] 获取完之后是让它转成阶层然后等拿到阶层数据之后咱们再进行保存最终你直接去把这个列表给return就可以了好吧咱们就下面去写一下首先构建评论URL这个怎么构建这个怎么建你看评论URL是这样咱们在这有一个这东西这条数据其实就是一个评论的URL但是
[05:12] 但是这一块呢是需要去设置两个值一个值呢就是当前的host就是你的什么就是你的这个作者名称是吧然后第二个呢是ID那这个ID是谁呢这个ID啊其实呢就是一个文章的这种ID算是文章的ID因为你爬取的文章的ID但我想问一下那目前的这两个值有没有呢想一想这两个值是不是咱们之前是爬取过的对吧咱们现在一个事呢就是要去拼接当前的源拿到
[05:42] 拿到当前的他和他然后最终跟这个串一拼接就能去获取到某一条文章的这种评论数据咱们可以这样咱们可以这样比如说你找到当前的某一个比如说这里边你看里边的这种文章你看这个有评论数1这评论数2这是2这是2是吧这有评论数你找一个有评论数的好咱们点一下那点一下之后你看这个好像也看不出来是吧咱们可以这样咱们可以把当前的这一条
[06:14] 拷贝过来拷贝改一改第一个是他的这个Authored就是他我们把它给替换了第二个是他你回车回车回车完之后其实这个数据就是咱们需要这样先去拿到这URL是吧URL之后咱们去发了一条邮获取到了当前的这个数据这数据的话不能直接保存的要干嘛需要去解析这个数据可以看一下我们最终的
[06:50] 不能去拿到里边的一些数据比如说这里边info里边这是第一个评论有一个好多余这就是content当前是谁评论的评论的时间是哪个咱们主要是拿到这几个看到了吧OK咱们是要再次发抢求是拿到获取到这个内容OK下面有两条的话咱们要去获取多个有可能是有多个评论所以说咱们这获取的是一个什么是一个列表
[07:17] 首先咱们第一步要构建URL这样咱们就去stripturl就等于谁呢等于一个bo的url然后是command的url猜数是谁说了猜数是哪个猜数是不是就是passatm因为里边是不是我们已经把取了刚才说的那两项刚才说的这两项
[07:50] 行到这这个好像是怎么着没有吗本来就没有啊咱们就要去创建一下啊好先创建到这一会咱们再去运营然后呢拿到URL之后呢你需要去干嘛呢你需要去获取数据这时候呢咱们可以直接去调用附内的一个什么at orange一个是jason8发送请求是jason8他的URL呢就是当前的
[08:22] 旧的有R,第二个实在实难这个是没有值的好,这个返回的就是一个json.json数据,就相当于这么一大串这么大串不行啊,你要去解析所以说咱们在这儿再去设置一个解析我们要解析怎么写呢SIS,就它,analysis然后是command然后是json.json
[08:53] 好这个参数呢就是当前的json好它返回的就应该是我的我要返回的这个列表好它之后呢最终呢你就可以去return了啊return当前的错了怎么写的common的list好吧把这个返回就可以了好那这样的话咱们步骤算设置完了方法没有咱们要去放键一下好那下面呢就来去写这两个方法
[09:28] 那这个呢咱们先去说这个啊说是生成评论访问链接好吧那这个该怎么去写呢想一想首先呢你要够取到当前的这个创然后呢是干嘛呢解析它然后就替换啊找到找到当前的这个跟这个把这里边的东西给替换了就可以了是吧所以说啊咱们在这啊先去获取到当前这个创怎么获取啊
[10:01] 还是要在上面去加个东西叫private-string的比如叫他好吧行那上面上面先不改一会儿再说怎么叫然后在这去设置一个it他然后把它给拷贝一下这东西咱们可以设置成大写好吧那这样的话咱们就算是设置完了设置完之后这个值咱们已经获取到了
[10:33] 获取到之后呢咱们在下边就可以直接去用了直接去用啊那这里边怎么去用呢那你要去解析这里边的数据对吧是不是要解析这里边的数据啊OK没问题啊但是有可能会有多个那你怎么去怎么去那啥呢怎么去那个怎么去获取到里边具体的有可能会有多个呀所以说呢咱们还是要把它干嘛呢把它呢转成一个map转成一个map叫retifrefact然后是utils
[11:03] refact, rec, mutils.r, 咱们有一个叫做toMap, ok把当前这个passAtom管成一个map好,这个呢其实就是一个map啊map里边呢咱们就可以去循环了啊map.tset, 这样不行是吧咱们写一个for循环啊然后第一个值呢是map.entry然后这个qvalue呢就是
[11:35] 来设置一下key是一个spin,value是一个object这个只能叫entry,冒号就是myp.tset写错了拿到它之后写错了吗写错了然后就可以去循环循环完之后你可以拿到它的
[12:08] 比如说这一点这个呢其实就是一个下面还有一个就是要不然要我们要构建这个屁啊不见你最终啊要去计划一说呢你最好是跟当前这个符号是一样的也就是说你要去拼接当前的DAO了服大括号和后边这个大括号好吧那这就比较容易了怎么办呢咱们咱们可以再去进行这个叫b又等于什么呢等于一个括号然后是老师他
[12:39] 然后是加上谁呀加上key然后是再加上是一个框ok这样的话咱们就算是运营完成你可以再拿他的value谁呀叫intra.getvalue这个value是一个什么objok没问题下面咱们就可以去判断判断之后咱们就可以去替换说value那么num不等于value然后你就可以去
[13:09] 可以去替换了当然这个value你必须的是干嘛呢必须的是to split一下然后怎么办str value vlue就可以了然后最终的你就要去替换用谁替换用cst command url有一个叫做replace第一个值就是他们的yield key
[13:43] 然后第二个呢就是start value啊最终呢咱们就要去重新给它付下值就可以了然后最终呢你就可以去认为正向前的哪个那这样的话咱们就算是设置完了啊现在这个设置完成之后啊然后下面呢咱们就来去来写写哪个方法写这个方法好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中通过 IDE 自动补全功能编写处理文章评论数据的代码，包括构建评论 URL、发送请求、解析 JSON 数据并分析评论信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 `CrawlerNewsParsePipeline.java` 文件中，光标位于 `private void sendSubmitArticleAutoMessage(Integer id) {` 方法内，IDE 显示了 `cNews` 类型的自动补全建议，用户选择 `cNews`。
画面 2: 在 `sendSubmitArticleAutoMessage` 方法内，IDE 显示了 `CrawlerNewsAdditionalService` 类型的自动补全建议，用户选择 `crawlerNewsAdditionalService`。
画面 3: 在 `sendSubmitArticleAutoMessage` 方法内，IDE 显示了 `CrawlerNewsCommentService` 类型的自动补全建议，用户选择 `crawlerNewsCommentService`。
画面 4: 在 `CrawlerNewsParsePipeline.java` 文件中，光标位于 `private void addCommentData(CrawlerParseItem parseItem, CNews cNews) {` 方法内，显示了 `Log.info("开始获取文章评论数据")` 语句。
画面 5: 在 `addCommentData` 方法内，光标位于 `Log.info("获取文章评论数据完成，耗时：0" + System.currentTimeMillis());` 语句后，显示了 `Log` 类的自动补全建议。
画面 6: 浏览器打开 CSDN 博客页面，显示了“Java算法基础2”等文章列表。
画面 7: 浏览器页面显示了 CSDN 博客的评论区数据，包含多个评论的 JSON 数据。
画面 8: 在 `CrawlerNewsParsePipeline.java` 文件中，光标位于 `private String buildCommentUrl(CrawlerParseItem parseItem) {` 方法内，显示了 `//解析获取的json数据` 注释。
画面 9: 在 `CrawlerNewsParsePipeline.java` 文件中，光标位于 `private List<CNewsComment> getCommentData(CrawlerParseItem parseItem) {` 方法内，显示了 `String jsonData = getOriginalRequestJsonData(buildCommentUrl, parameterMap: null);` 语句。
画面 10: 在 `getCommentData` 方法内，光标位于 `List<CNewsComment> commentList = analysisCommentJsonData(jsonData);` 语句后，显示了 `analysisCommentJsonData` 方法的自动补全建议。
画面 11: 在 `analysisCommentJsonData` 方法内，光标位于 `private List<CNewsComment> analysisCommentJsonData(String jsonData) {` 方法内，显示了 `private` 关键字的自动补全建议。
画面 12: 在 `analysisCommentJsonData` 方法内，光标位于 `@Value("${csdn.comment.url}")` 注解后，显示了 `@Value` 注解的自动补全建议。
画面 13: 在 `analysisCommentJsonData` 方法内，光标位于 `@Value("${csdn.comment.url}")` 注解后，显示了 `@Value` 注解的自动补全建议。
画面 14: 在 `analysisCommentJsonData` 方法内，光标位于 `@Value("${csdn.comment.url}")` 注解后，显示了 `@Value` 注解的自动补全建议。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private void sendSubmitArticleAutoMessage(Integer id) {
    // 添加评论数据
    @param parseItem
    @param cNews
    // 保存附件信息
    @param parseItem
    @param cNews
}
```

画面 2:
```java
private void sendSubmitArticleAutoMessage(Integer id) {
    // 添加评论数据
    @param parseItem
    @param cNews
    // 保存附件信息
    @param parseItem
    @param cNews
}
```

画面 3:
```java
private void sendSubmitArticleAutoMessage(Integer id) {
    // 添加评论数据
    @param parseItem
    @param cNews
    // 保存附件信息
    @param parseItem
    @param cNews
}
```

画面 4:
```java
private void addCommentData(CrawlerParseItem parseItem, CNews cNews) {
    long currentTimeMillis = System.currentTimeMillis();
    Log.info("开始获取文章评论数据");
    if (null != commentList && !commentList.isEmpty()) {
        for (CNewsComment cNewsComment : commentList) {
            cNewsComment.setNewsId(cNews.getNewsId());
        }
    }
}
```

画面 5:
```java
Log.info("获取文章评论数据完成，耗时：0" + System.currentTimeMillis());
```

画面 6:
无代码。

画面 7:
无代码。

画面 8:
```java
private String buildCommentUrl(CrawlerParseItem parseItem) {
    // 保存附件信息
    @param parseItem
    @param cNews
}
```

画面 9:
```java
private List<CNewsComment> getCommentData(CrawlerParseItem parseItem) {
    String buildCommentUrl = buildCommentUrl(parseItem);
    String jsonData = getOriginalRequestJsonData(buildCommentUrl, parameterMap: null);
    List<CNewsComment> commentList = analysisCommentJsonData(jsonData);
    return commentList;
}
```

画面 10:
```java
private List<CNewsComment> analysisCommentJsonData(String jsonData) {
    @Value("${csdn.comment.url}")
    private String csdnCommentUrl;
    // 生成评论访问链接
    @param parseItem
    @return
}
```

画面 11:
```java
private List<CNewsComment> analysisCommentJsonData(String jsonData) {
    @Value("${csdn.comment.url}")
    private String csdnCommentUrl;
    // 生成评论访问链接
    @param parseItem
    @return
}
```

画面 12:
```java
@Value("${csdn.comment.url}")
private String csdnCommentUrl;
```

画面 13:
```java
@Value("${csdn.comment.url}")
private String csdnCommentUrl;
```

画面 14:
```java
@Value("${csdn.comment.url}")
private String csdnCommentUrl;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

