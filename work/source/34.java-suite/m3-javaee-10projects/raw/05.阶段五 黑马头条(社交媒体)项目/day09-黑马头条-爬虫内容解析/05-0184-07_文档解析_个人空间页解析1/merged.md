# 07_文档解析_个人空间页解析1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\07_文档解析_个人空间页解析1【海量资源尽在 666java.com】.mp4
- 时长 7分21秒（音频 441s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲刚才咱们是把初始化的URL给获取了并且也去解析了是吧然后下面咱们就来去打开帮助页也去解析一下帮助页这个帮助页其实就是谁就是咱们在去解析某一个分类的时候这是初始化的是吧你找到它的一个用户的空间说的找到用户的空间其实就是去解析这个URL
[00:30] 当然这里边其实你还要去考虑一个问题哪个问题呢好来看一看然后咱们再去点其他的一个东西你看这个文章多的时候这个文章少的话其实没有分页是吧它不需要分页因为就一条文章不需要分页如果说文章过于多的话这时候它会自动分页这个也没有分页是吧咱们找一个分页的好再找一个你看这个是有分页的那你说我这些数据我是不是也要获取到
[00:59] 是吧所以说呢咱们这块也要获取到分页的数据也要获取到分页的数据行那这个呢咱们就先说到这一会呢咱们就来去解析里边的应该是叫获取里边的各个的URL好吧行那这个就是就是要去获取帮助页的或者个人空间里边的文章的URL
[01:25] 好那下面呢这有一个工具啊有一个应该是有一个公用的方法咱们需要定义到哪啊定义到咱们的当前的这个负类中那考到哪个负类中呢你看啊这里边呢其实我先考过来啊咱们呢需要去考到当前的这个obspect process flow考到这里边啊因为呢它是一个更大的负类这时候呢它所有的子类呢都能去用啊咱们首先呢去拷贝一下
[01:55] 拷贝完之后我再去说一下这里边到底有什么方法好拷贝然后是找到最大的负类好拷到这就可以了拷到最后边拷完之后其实里边没有几个方法你看首先是获取的啥呢获取的是一个什么HNL date怎么去获取HNL date其实就是去发请求就是一发请求这里边有两步比较关键第一个就是它你可以点进去
[02:27] 就是通过什么呢通过这种http的方式http client的方式呢去获取的数据http client的数据啊的请求方式如果说啊如果说他的是这个数据没有啊他拿到数据之后说验证啊这个数据是有问题那有问题怎么办呢有问题的话呢咱们就干嘛呢就去通过这种什么slinimslinim啊slinim这种方式去请求下载咱们的
[02:56] HTML那种OK啊比如说呢它是有两个方法啊主要是两个方法主要是这两个啊比如说有两种方式第一种咱们要用http client去请求如果说数据拿不到咱们再用Clinim这种方式去请求数据OK啊那为什么要请求呢你看啊比如说比如说啊你现在啊已经拿到了某一个UR比如说就是这个什么加温练习2的UR
[03:23] 那这个URL你是不是得去拿到这个源码对吧也就是说拿到咱们最终的内容拿到这个内容之后呢咱们才能去解析这个没问题吧所以说呢这个呢咱们最终是要拿到这个HTML的内容其实刚才说的那个HTML date其实就是刚才我打开的这个源码好吧行那这个咱们就说到这咱们就继续往下讲
[03:51] 然后下面呢咱们就可以定义这么一个类去解析但这个类里面呢主要就是去在帮助业里边去获取它的这种URL但是获取URL刚才说了咱们要去考虑一个问题就是一个是非业的情况一个是不非业的情况好吧来把它呢给拷贝一下在这去创建一个类让这个类呢也去立成当前的谁呀当前的给我看啊是不是
[04:27] 是这没错目前的这个类这个好那这个链没有这个没有这个没有的话咱们就先删了这个类咱们还没有定义好先删了好咱们把这个方法给实现一下这几个方法我们主要是还是去写这几个方法首先它事实上是让the brain去管理咱们在这因为后边就要去加一些这种日志所以说在这去加一个log4j2好吧
[05:07] 然后咱们下面就来去写这些方法最合一的方法肯定就是handle page是吧咱们这样先去把这几个方法给补充完整补充完整之后咱们一会再去编写当前这个方法好吧这个方法是干嘛的我们之前说初始化URL的时候应该是写的是吧是处理爬虫类型咱们都是正向目前都是正向
[05:37] 然后的话那那这块怎么写啊他既然给你传了一个那就去直接返回一个比如说叫caller new more好点儿那是handle bit什么呢啊而咱们的forward name点name 点ecoeco如果说他跟你传回来的是一样的话那这时候呢咱们就返回出啊要不然那就返回force好吧这个呢这个其实跟那上面差不多是吧啊前面也是当前这个范形
[06:08] 也是这个饭鞋啊也是这个眼睛木啊什么呢是DAOQ门的太保点咱们的是一个什么还有现在目前是空间一啊比如说咱们在这儿去还是他就把这当前那个OAuth门的太保进去就可以了好吧那当然这个这个当前的优先级写下注射啊就是保持保持这样的好好习惯处理什么玻璃文档
[06:39] 这里的文档类型嘛,好不好然后呢,这个呢这个是,稍等啊这个呢是优先级是吧那优先级我想问一下目前你说先是初始化这个先执行还是这个空间先执行那肯定,肯定是呀肯定是当前这个初始化先执行是吧那初始化先执行的话你看它这个值多少,100是吧,那你说这边是多少90,对,应该是比这个100要大啊咱们切成110就可以了,好吧
[07:11] 那目前这个优先级啊咱们就算是说完了啊一会儿还有一个目标页需要去设置其实优先级要比这个更大因为那个是最后处理好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在爬虫项目中实现帮助页面的处理器，包括继承抽象处理器、重写处理方法和设置优先级。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中CrawlerHelpPageProcessor类的代码，其中包含getPriority()方法返回100。
画面2：切换到CSDN博客页面，浏览Java异常处理和Tomcat安装相关文章。
画面3：在CSDN博客中浏览关于Mac使用tesseract-ocr、json dump中文问题和Python3的帖子。
画面4：展示getHttpClientRequestData方法的代码，包含日志记录和异常处理。
画面5：展示AbstractProcessFlow类的代码，包含@Autowired注解的SeleniumClient和CrawlerProxyProvider。
画面6：展示AbstractProcessFlow类中getOriginalRequestData方法的代码，包含获取代理和Cookie的逻辑。
画面7：查看CSDN文章的源代码，包含meta标签和脚本标签。
画面8：展示CrawlerHelpPageProcessor类的代码，包含@Component和@Logj2注解。
画面9：在IDE中右键CrawlerHelpPageProcessor类，选择“Local History”查看历史版本。
画面10：在IDE中导入us.codecraft.webmagic.Page包。
画面11：展示CrawlerHelpPageProcessor类中重写的isNeedHandleType和isNeedDocumentType方法。
画面12：展示CrawlerHelpPageProcessor类中isNeedHandleType方法的实现，返回CrawlerEnum.HandleType.HTML。
画面13：展示CrawlerHelpPageProcessor类中isNeedDocumentType方法的实现，返回CrawlerEnum.DocumentType.HTML。
画面14：展示CrawlerHelpPageProcessor类中getPriority方法的实现，返回100。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
@Override
public int getPriority() {
    return 100;
}
```

画面4：
```java
public String getHttpClientRequestData(String url, Map<String, String> parameterMap,
        List<CrawlerCookie> cookieList, CrawlerProxy proxy) {
    CookieStore cookieStore = getCookieStore(cookieList);
    String jsonDate = null;
    if (null != crawlerProxy) {
        proxy = CrawlerProxyFactory.getHttpProxy(crawlerProxy);
    }
    try {
        long currentTime = System.currentTimeMillis();
        log.info("HttpClient 请求数据: url:{}, parameter:{}, cookies:{}, proxy:{}", url, parameterMap, cookieList, proxy);
        jsonDate = HttpClientUtils.get(url, parameterMap, getHeaderMap(), cookieStore, proxy, "utf-8");
        log.info("HttpClient 请求数据完毕: url:{}, parameter:{}, cookies:{}, proxy:{}", url, parameterMap, cookieList, proxy);
        System.currentTimeMillis() - currentTime;
        return jsonDate;
    } catch (URISyntaxException e) {
        log_error("HttpClient 请求数据异常: url:{}, parameter:{}, cookies:{}, proxy:{}", url, parameterMap, cookieList, proxy, e.getMessage());
    } catch (IOException e) {
        log_error("HttpClient 请求数据异常: url:{}, parameter:{}, cookies:{}, proxy:{}", url, parameterMap, cookieList, proxy, e.getMessage());
    }
    return jsonDate;
}
```

画面5：
```java
@Autowired
private SeleniumClient seleniumClient;

@Autowired
private CrawlerProxyProvider crawlerProxyProvider;
```

画面6：
```java
public String getOriginalRequestData(String url, Map<String, String> parameterMap) {
    //获取代理
    CrawlerProxy proxy = crawlerProxyProvider.getRandomProxy();
    //获取cookie列表
    List<CrawlerCookie> cookieList = cookieHelper.getCrawlerCookieList(url, proxy);
    //获取cookieStore
    CookieStore cookieStore = getCookieStore(cookieList);
    //构建url
    String buildUrl = HttpClientUtils.buildUrl(url, parameterMap, HttpClientUtils.UTF_8);
    //获取请求头
    String cookieHeader = cookieHelper.getCookieHeader(buildUrl, proxy, cookieStore);
    //获取请求体
    String body = cookieHelper.getBody(buildUrl, proxy, cookieStore);
    //获取请求头
    String header = cookieHelper.getHeader(buildUrl, proxy, cookieStore);
    //获取请求体
    String request = cookieHelper.getRequest(buildUrl, proxy, cookieStore);
    //获取请求头
    String response = cookieHelper.getResponse(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentType = cookieHelper.getContentType(buildUrl, proxy, cookieStore);
    //获取请求头
    String accept = cookieHelper.getAccept(buildUrl, proxy, cookieStore);
    //获取请求头
    String userAgent = cookieHelper.getUserAgent(buildUrl, proxy, cookieStore);
    //获取请求头
    String referer = cookieHelper.getReferer(buildUrl, proxy, cookieStore);
    //获取请求头
    String connection = cookieHelper.getConnection(buildUrl, proxy, cookieStore);
    //获取请求头
    String cacheControl = cookieHelper.getCacheControl(buildUrl, proxy, cookieStore);
    //获取请求头
    String pragma = cookieHelper.getPragma(buildUrl, proxy, cookieStore);
    //获取请求头
    String expires = cookieHelper.getExpires(buildUrl, proxy, cookieStore);
    //获取请求头
    String date = cookieHelper.getDate(buildUrl, proxy, cookieStore);
    //获取请求头
    String authorization = cookieHelper.getAuthorization(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentLength = cookieHelper.getContentLength(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentEncoding = cookieHelper.getContentEncoding(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentLanguage = cookieHelper.getContentLanguage(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentLocation = cookieHelper.getContentLocation(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentRange = cookieHelper.getContentRange(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentDisposition = cookieHelper.getContentDisposition(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentMD5 = cookieHelper.getContentMD5(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentTransferEncoding = cookieHelper.getContentTransferEncoding(buildUrl, proxy, cookieStore);
    //获取请求头
    String contentSecurityPolicy = cookieHelper.getContentSecurityPolicy(buildUrl, proxy, cookieStore);
    //获取请求头
    String expect = cookieHelper.getExpect(buildUrl, proxy, cookieStore);
    //获取请求头
    String ifModifiedSince = cookieHelper.getIfModifiedSince(buildUrl, proxy, cookieStore);
    //获取请求头
    String ifNoneMatch = cookieHelper.getIfNoneMatch(buildUrl, proxy, cookieStore);
    //获取请求头
    String ifRange = cookieHelper.getIfRange(buildUrl, proxy, cookieStore);
    //获取请求头
    String lastModified = cookieHelper.getLastModified(buildUrl, proxy, cookieStore);
    //获取请求头
    String maxForwards = cookieHelper.getMaxForwards(buildUrl, proxy, cookieStore);
    //获取请求头
    String origin = cookieHelper.getOrigin(buildUrl, proxy, cookieStore);
    //获取请求头
    String referer = cookieHelper.getReferer(buildUrl, proxy, cookieStore);
    //获取请求头
    String server = cookieHelper.getServer(buildUrl, proxy, cookieStore);
    //获取请求头
    String transferEncoding = cookieHelper.getTransferEncoding(buildUrl, proxy, cookieStore);
    //获取请求头
    String upgrade = cookieHelper.getUpgrade(buildUrl, proxy, cookieStore);
    //获取请求头
    String vary = cookieHelper.getVary(buildUrl, proxy, cookieStore);
    //获取请求头
    String via = cookieHelper.getVia(buildUrl, proxy, cookieStore);
    //获取请求头
    String warning = cookieHelper.getWarning(buildUrl, proxy, cookieStore);
    //获取请求头
    String wwwAuthenticate = cookieHelper.getWWWAuthenticate(buildUrl, proxy, cookieStore);
    //获取请求头
    String xRequestedWith = cookieHelper.getXRequestedWith(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedFor = cookieHelper.getXForwardedFor(buildUrl, proxy, cookieStore);
    //获取请求头
    String xRealIP = cookieHelper.getXRealIP(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedProto = cookieHelper.getXForwardedProto(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedHost = cookieHelper.getXForwardedHost(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedPort = cookieHelper.getXForwardedPort(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedProto = cookieHelper.getXForwardedProto(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedHost = cookieHelper.getXForwardedHost(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedPort = cookieHelper.getXForwardedPort(buildUrl, proxy, cookieStore);
    //获取请求头
    String xForwardedProto = cookieHelper.getXForwardedProto(buildUrl, proxy, cookieStore);
    //获取

