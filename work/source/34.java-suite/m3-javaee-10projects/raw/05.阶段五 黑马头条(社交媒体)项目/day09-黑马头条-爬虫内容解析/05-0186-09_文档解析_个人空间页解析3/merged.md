# 09_文档解析_个人空间页解析3

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\09_文档解析_个人空间页解析3【海量资源尽在 666java.com】.mp4
- 时长 20分57秒（音频 1258s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续啊那咱们现在就把这个分页处理的逻辑啊给去写一下啊那这时候呢咱们可以再去抽出来一个方法比如要get doc要get然后url然后加上呢叫list然后咱们需要去传两个参数进去啊第一个参数呢就是一个request url那为什么要去传这个request url呢比如再说这个呢其实就是呀就是个人空间的url啊然后再往下呢
[00:28] 再往下的话咱们需要去传一个当前这种页码是吧你要到底是要去多少页去分页啊你要去获取多少页呢这时候咱们要去拿到啊然后最终呢咱们呢返回过来的呢返回过来的就是一个什么这个历史记号里边是一个死证啊咱们可以在这写个变量docpageurlist就等于它好吧咱们再往下如果说呢如果说这里边有值啊有值
[00:59] 它不等于NoneNone不等于当前DOCPage并且呢DOC DOCPageURL List打什么呢Lens那应该是叫Ease吧Ease EmptyEase Empty这时候咱们在前面去加一个什么飞空如果说你要是贵空这时候咱们就可以直接去加到当前的Hyper Add直接就把它加到当前上面的Hyper URL
[01:30] 而历史里边就可以了啊说了这个是第一页是吧再往下这里边的咱们都是处理第一页以后的啊从第二页开始啊所以说你可以把它直接装进去就可以了好吧那装进去之后呢下面呢就还是往当前这个轨筷子中去装轨筷子中装啊然后他就会去执行下一步了进行下一步啊那行那这个这个咱们说到这之后呢咱们再往下啊再往下写因为这个方法没有是吧没有把东西出现出来啊好绑紧给注释啊过去
[02:05] 分页后的数据好吧然后下面的这个这个咱们就简写一下叫URL好吧然后这个呢叫page size这样好写这个改一个URL啊是page size行拿了之后呢咱们下面那你说这里边该怎么去写首先呢咱们要去做一个判断做什么判断呢还用做什么判断吗那这里边咱们其实还有一个逻辑这时候呢
[02:37] 从判断呢咱们还是得去打开张铁这个东西啊比如说我让你看一个效果啊比如说咱们按F12啊咱们要去从初始化URL里边去是不是要获取到某一个文章的什么文章塑造的用户空间是吧就这个东西所以你可以看一下它你看这个这个是一个你看下边这个呢再点一下这个这个啊你看它这个呢其实都有一个特点什么特点呢都是以它结尾这是它
[03:07] 在SDN空间里边有一个默认的情况都是以这个结尾你可以再点一个啊再往下看你看是不是都是以它结尾都是以它结尾的话这时候呢那你说它有用吗其实它分页的时候其实没啥用啊为什么说没什么用呢你可以看啊比如说啊这个找一个有找一个多多多条的啊你看点你看它的后边啥呢它的后边是article list3article list3是吧所以说啊
[03:38] 所以说呢你这时候你可以再往下点啊他就是把这个变成4所以说那个刚才那个后缀啊刚才这个后缀其实是没有用的刚才这个后缀有用吗没用啊他咱们只需要查查只需要前面这一段所以说呢咱们一会儿啊还会去替换因为分页的时候不需要他加上他反而就分不了页了所以说呢咱们一会儿要去单独去处理一下好那咱们写的时候啊就就这样写啊如果说url点什么呢
[04:12] close with,end with吧如果说以谁结尾啊以刚才那个结尾刚才怎么写呢咱们可以看一下啊就是什么拷贝一下吧好拷贝一下它啊如果说以它结尾的话咱们再去处理去处理啊当然这个处理的话呢咱们一会儿再去处理啊咱们先这么写的话可能不太好这时候呢咱们可以把它抽到上面啊抽到上面啊抽到上面的话其实也比较简单咱们在这直接去private
[04:48] 然后呢就叫叫他叫什么叫HelperURL我们叫前缀吧好吧后缀啊好就是当刚才的这个值那个值啊这个问号也加上啊问号也加上啊好这是一个当然如果说你要不想让别人改的话你可以加一个什么final加个final啊意思在这里边咱们还会用到二个第二个第二个呢其实就是刚才说的
[05:22] 咱们分页的时候其实要分页要要要拼什么东西要拼一个article list要一个拼一个article list所以说咱们把这个啊也要加上因为咱们后期分页的时候拿前面这个后边的给你组装就可以了好吧所以说咱们这个要去把它给分一下private final还是final啊不不允许让人动好吧然后呢接着呢咱们叫help page怎么叫paging吧就page得了
[05:54] pitch Service这个定义完之后啊定义完之后呢咱们这时候啊这去写的时候呢就可以直接去写它了啊往下走走走往这的这一块呢咱们要去分两步走啊分两步那第一步要干嘛呢第一步咱们首先呢要去获取到所有的分页后的URL分页的URL然后第二个呢这个是获取
[06:37] 分页数据中的什么目标URL这个就比较懵了啊你看啊首先呢咱们要获取的什么呢你看啊要获取的是比如说123比如咱们获取第四第五第六像是我说的是第一个URL是这个URL说你要是点到第六页然后点下回车咱们要获取目标的话其实就是当前某一条文章的URL你明白吧
[07:05] 所以说呢这块咱们要去做两件事啊做两件事啊首先咱们要拿到分页的URL那这个呢简单咱们直接去手动拼装就可以刚才说了这时候呢咱们要从第二页开始啊因为第一页第一页你已经在这去拿到了咱们只需要从第二页获取就可以好吧那这时候咱们也可以去干嘛呢也可以去在这去写一个东西
[07:33] 怎么写呢再去出个方法吧好吧再出个方法获取生成吧然后是叫hyper hyperpadingurl然后咱们传的一个值呢其实就是这样第一个呢是url然后第二个呢是咱们的page size反回的呢反回的其实就是个例子集合此顿我们要手动拼接嘛然后怎么叫page
[08:08] URList这么写不行啊paging URL list好吧这是第一个然后第二个呢第二个的话呢其实就比较简单了啊第二个不是比较简单第二个比较麻烦一些啊这个咱们只需要通过它上面这个参数啊paging什么docurl那这时候呢参数就是它参数就是它
[08:39] 你返回的数据呢它其实也是一个集合这个集合咱们再进到上面好吧叫list split然后呢咱们叫什么呢叫doc page billing url list等于none好吧然后然后呢让它去上传让它去等于它咱们把这个doc给它返回就可以了return doc page billing url list好吧
[09:08] 行那这个方法这两个方法呢咱们还是要分别去实现啊这个比较简单这个还是很麻烦的啊因为这个为什么麻烦呢因为呢你拿到某一个URL的时候你是不是还在发请求是吧也就是说你需要去发请求得到这个页面然后呢从这个页面里边去获取到什么呢具体的URL好吧行拿到它之后啊那咱们就继续往下讲啊来我在这啊先去把它给剪一下啊生成
[09:38] 这个相对来说比较简单什么来着叫生成分页的URL好往下写这个其实就是一个运接的过程这个过程咱们这是这样URL点先去替换一下replace然后是第一个什么alpha URL这个前缀然后下面就是咱们要分页的前缀错了应该是前面这个URL
[10:11] 这是URLURL替换成啥呢要替换成前的位置的后缀也就是说啊前面这个咱们一开始去爬取的时候是不是要获取了这个内容但是咱们要去分页的时候呢后边这段咱们不要是吧不要啊那不要替换成啥呢替换成当前什么哪个呢article-list是吧所以说呢这块呢这个这个啊主要就是来去替换的最终呢你把它呢
[10:42] 再去复给谁复给一个string的配置URL这是就算替换完了替换完之后我们要去做一个做一个这种循环首先的inti等于OK一定要注意这是个1因为第一页干嘛一页已经上面是不是已经解析完了这时候咱们要去从第二页开始小于pagesize然后是
[11:14] 可以加加哦就可以拼接了啊这已经拼接完了是吧我配置这个好像没有集合是吧怎么在这再去创建个集合吧最终把它给返回就可以了说怎么叫什么呢还是list的返回的一个stream然后呢怎么叫配置list当我unit一个readlist好吧我把它呢装进去就可以了啊一个一个的url装进去
[11:49] 这个呢就是当前的配置URL加上什么呢加上配就可以了因为这个是一个分页这是一个分页啊好最终呢是把当前这个给它返回就可以了叫配置配定配置配定R list这个就算是设置完了啊设置完之后啊那下面呢还有一个方法咱们需要去写是吧来把这个方法也去生成一下啊好生成那完之后呢这个方法是干嘛的方法
[12:24] 是获取分页后的什么URL这个啊是目标URL目标其实就是文章的文章的URL列表那这个这个方法呢咱们就来往下写啊还是一样啊咱们在这还是得去先去记录个时间吧好吧先记录时间那记录时间是什么system.currenttime.minus
[12:58] 然后最终是拿到一个当前的这种他吧好吧无所谓啊下面都行下面呢咱们也可以去记录一个东西loginfo记录啥呢比如说咱们是开始运行分页获取抓取吧抓取doc页面其实就是文档页面是吧然后呢没有了啊
[13:27] 然后下面咱们就可以干嘛呢就可以去最终是去解析解析成之后反复一个list咱们可以先把它定义一下stri怎么叫什么呢ocurlist等于new一个relist好吧下面咱们就可以去解析了解析之前咱们为了防止出错咱们也可以在这去先去干嘛先去做一个count
[13:56] 要是出错的话咱们往哪边去加1下面咱们就去那首先如果说他pidding varlist就是前传的这个参数那是等于空的前面是非等于空的时候咱们这时候咱们就可以去做循环了怎么可以这么写pidding.foo
[14:28] 这个呢其实就是URL是吧然后下面呢咱们就可以去进行发问发送请求那发送请求之前呢咱们也可以在这去设置一个login for记录一下这个词叫啥呢叫什么开始Helper什么呢页面开始进行Helper页面分页处理咱们这个URL是谁呀URL是啥那咱们就是咱们的URL
[15:10] 下面咱们就可以真正的处理真正处理的时候你首先得去干嘛你去发请求getOriginalRequestHTML这个其实第一个传输就是Url然后第二个咱们可以尝尝好吧这个其实就拿到了当前的HTML吗那这个方法是在哪呢方法其实咱们在刚开始去讲这个的时候已经考完了其实就在这
[15:38] 其实就这个方法好吧刚才说了他就是发请求如果说他是用http client请求不到的话他就可以使用谁呀叫Celine去请求数据OK啊最终的这个数据就能请求到了请到之后呢其实就是谁呀其实就是某一个这种文档数据是吧那文档数据不行啊他要干嘛呢你是不是还得去获取某一个一碗碗里边所以说呢咱们在这儿
[16:08] 你光拿到它其实没有用啊咱们现在还是一样啊还是得再去解析再去解析啊好那解析的方式呢其实跟上面是一样的啊你首先拿到这个html date然后呢咱们可以先去验证一下啊验证完之后呢咱们可以再去做那验证怎么验证啊验证完之后咱们再去解析啊验证啊就是咱们有一个color helpcolor help.我们有一个叫做dat date然后呢你就可以去valid
[16:38] 然后咱们就是html返回一个board比如说就叫validate如果说是validate没问题就说了如果说它没有问题的话这时候咱们就可以去解析可以去解析怎么解析咱们之前的方式是一样的这时候咱们可以new一个html当然了这个是谁
[17:11] 这个就是当前webmatic提供的好传的参数是啥参数就是当前的html date它是一个45串是吧然后下面你就可以去设置s passs pass是这样跟上面这个是一样吗一样跟上面这个是一模一样所以说还是它怎么可以直接拷贝拷贝也行直接写也行好这是一个然后下面是什么links pass
[17:47] 这个呢其实就是一个方法这个呢其实就拿到谁呀拿到了当前的一个当前的一个这种数据啊这叫URList好吧然后咱们再往下啊如果说如果说什么呢如果说这URList.Empty如果说它为空如果说它不为空啊如果说它不为空的话呢这时候呢咱们就可以把它给放到哪啊UCURL.什么
[18:25] 把他装入当前天要返回的这个集合中就可以了好吧如果说他不成功的话呢我们这时候呢就可以去设置一个参数就说你要是失败的话咱们就也可以记住一下然后是看了加加好吧然后呢咱们下面呢就可以去说如果说大于二的话呢咱们直接去直接去停止当前这个循环就可以好吧
[18:59] 直接趁着循环那这个怎么办咱们就是说2与几2的时候我们就可以直接去break停止当前的循环好吧行这个其实就写的差不多了写差不多之后咱们在这可以去回谁return咱们的什么doc file list好吧当然咱们在这也可以再去记录一下多记录一步
[19:29] 防止后期出错的时候咱们调试这样记录完之后你能一眼看出来到底是哪个方法或者哪一块业务出现的问题说咱们是分页分页抓取分页抓取DOC页面页面完成然后号10也可以设个号10好吧设成英文的符号吧好吧方式加什么呢加上systemsys
[20:10] System.ArenderedTimeMinutes选取谁呀选取一个叫做ArenderedTimeMinutes这样的话咱们就可以了这边怎么还报错了呢我看看啊这不是加号啊这应该是一个逗号好,forEU的逗号啊那这个咱们目前这个方法就算是写完了这个类呢其实所有的业务呢咱们也算是处理完了这是第二步啊就是Hyper就是个人空间那个
[20:46] 那这时候咱们这个所有的URL基本上都拿到了比如说我现在也拿到了具体的URL那这时候咱们下一步就应该去解析具体的什么文章的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 爬虫项目中实现对帮助页（Help Page）的分页抓取逻辑，包括 URL 生成、分页数据提取和有效性校验。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 `CrawlerHelpPageProcessor.java` 中，展示 `addSpiderRequest` 方法用于添加爬虫请求，日志记录解析帮助页数据完成，参数包括 url、handleType、耗时、page 等。
画面 2: 展示 `getDocPageUrlList` 方法的定义，用于获取帮助页的 URL 列表，方法接收 requestUrl 和 crawlerHelpPagingSize 参数。
画面 3: 浏览器显示 CSDN 网站的搜索结果页面，包含多个关于 Java 编程和算法的文章链接。
画面 4: 在代码中，`getDocPageUrlList` 方法的实现部分，检查 URL 是否以 “utm_source=feed” 结尾。
画面 5: 浏览器显示 FreeSpider 网站的个人主页，包含多个文章列表，如“爬虫篇”、“影虫篇”等。
画面 6: 在代码中，`getDocPageUrlList` 方法的实现部分，定义了 `helpPageSuffix` 为 “/article/list”，并检查 URL 是否以该后缀结尾。
画面 7: 浏览器开发者工具中，查看 CSDN 网站的 HTML 结构，定位到帮助页的链接元素。
画面 8: 在代码中，`generateHelpPagingUrlList` 方法的实现部分，生成分页 URL 列表，通过循环构造 URL 并添加到列表中。
画面 9: 在代码中，`getHelpPagingDocUrl` 方法的实现部分，开始进行分页抓取，记录开始时间，初始化 docList。
画面 10: 在代码中，`getHelpPagingDocUrl` 方法的实现部分，检查 pagePagingUrlList 是否为空，若为空则返回空列表。
画面 11: 在代码中，`getHelpPagingDocUrl` 方法的实现部分，调用 `crawlerHelper.getDataValidateCallBack().validate(UrlData)` 进行数据校验。
画面 12: 在代码中，`getHelpPagingDocUrl` 方法的实现部分，校验通过后，使用 `HtmlUtil` 的 `xpath` 方法提取链接。
画面 13: 在代码中，`getHelpPagingDocUrl` 方法的实现部分，校验失败时，增加失败计数器 `failCount`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
addSpiderRequest(thePlyList, page.getRequest(), CrawlerBrun.DocumentType.PAGE);
log.info("解析帮助页数据完成。url: {}, handleType: {}, 耗时: {}ms, page: {}, handleType: {}",
        url, handleType, System.currentTimeMillis() - startTime, page, handleType);
```

画面 2:
```java
private List<String> getDocPageUrlList(String requestUrl, Integer crawlerHelpPagingSize) {
    // 处理帮助页类型
    // 正则
    // Return
}
```

画面 4:
```java
private List<String> getDocPageUrlList(String url, Integer pageSize) {
    if (url.endsWith("utm_source=feed")) {
    }
}
```

画面 6:
```java
private final String helpPageSuffix = "/article/list";

private List<String> getDocPageUrlList(String url, Integer pageSize) {
    if (url.endsWith(helpPageSuffix)) {
        List<String> pagePagingUrlList = generateHelpPagingUrlList(url, pageSize);
        docPageUrlList = getHelpPagingDocUrl(pagePagingUrlList);
        return docPageUrlList;
    }
}
```

画面 8:
```java
private List<String> generateHelpPagingUrlList(String url, Integer pageSize) {
    String pageUrl = url.replace(helpPageSuffix, helpPageSuffix);
    List<String> pagePagingUrlList = new ArrayList<>();
    for (int i = 1; pageSize > i; i++) {
        pagePagingUrlList.add(pageUrl);
    }
    return pagePagingUrlList;
}
```

画面 9:
```java
private List<String> getHelpPagingDocUrl(String pagePagingUrlList) {
    long currentTimMillis = System.currentTimeMillis();
    log.info("开始进行分页抓取{}个页面", pagePagingUrlList.size());
    List<String> docList = new ArrayList<>();
    for (String url : pagePagingUrlList) {
        log.info("开始进行help页抓取");
        String htmlData = getOriginalRequestHtmlData();
        crawlerHelper.getDataValidateCallBack().validate(htmlData);
    }
}
```

画面 11:
```java
private List<String> getHelpPagingDocUrl(String pagePagingUrlList) {
    long currentTimMillis = System.currentTimeMillis();
    log.info("开始进行分页抓取{}个页面", pagePagingUrlList.size());
    List<String> docList = new ArrayList<>();
    for (String url : pagePagingUrlList) {
        log.info("开始进行help页抓取");
        String htmlData = getOriginalRequestHtmlData();
        crawlerHelper.getDataValidateCallBack().validate(htmlData);
    }
}
```

画面 12:
```java
boolean validate = crawlerHelper.getDataValidateCallBack().validate(htmlData);
if (validate) {
    List<String> urlList = new HtmlUtil(htmlData).xpath(crawlerConfigProperty.getHelpCrawlerXPath().links, 0);
    if (urlList.isEmpty()) {
        docList.add(urlList);
    } else {
        failCount++;
        if (failCount > 2) {
            // 处理失败情况
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

