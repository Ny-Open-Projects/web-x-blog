# 08_动态ip代理池管理_更新动态ip2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\08_动态ip代理池管理_更新动态ip2【海量资源尽在 666java.com】.mp4
- 时长 9分5秒（音频 545s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去获取抓取的动态IP这个方法咱们要去完成一下好吧那这块内容咱们要去使用谁呢使用当前的一个叫做什么也叫使用CNN这个东西咱们之前是用过的是吧YouTube这个的方式方式获取代理IP数据
[00:37] 所以说咱们在这先去把client先给注入进来咱们在这写一个叫privateprivate然后是有一个叫做seleniumclient就是它是咱们创建的最早的一个工具然后这里边有个方法咱们可以看一下点咱们要获取当前的什么$HTMLOK这里边需要几个参数你看
[01:07] 第一个是你要爬取的URL第二个是有一个HoloProxy然后第三个是一个CookieName那这三个参数怎么来呢?
[01:20] 目前的第一个参数其实你应有了哪个呢?
[01:25] 就是当前的这个那它怎么获取?
[01:28] 它获取的方式非常简单是吧怎么办呢?
[01:32] 咱们在这去直接用当前的private这个参数叫啥我看看我们可以把它给拿到
[01:40] 我在这先去注入吧Value怎么写啊?
[01:45] 高尔夫是吧?
[01:47] 好,按进去咱们这名称的叫PostronProwseAtUrl好吧,叫它,报错了吗?
[01:58] 这个是第一个参数第二个参数呢?
[02:02] 这样的参数里面你看啊这边需要有一个叫做ColorProwse那这个怎么拿呢?
[02:12] 其实咱们可以用钢琴的这种另外一个对象private然后这里边是有一个叫怎么poller ip不是ippoller咱们叫plussyplussy provider就它咱们也可以注入进来这个咱们也是刚刚创建的是吧好这里边其实你就可以去获取一个叫什么叫做random plussy这是第二个材数
[02:41] 第三个参数我可以直接告诉你第三个参数是一个固定的叫YD-Cookie你说这个值是固定的吗怎么来的呢你可以看一下刚前你去请求这东西的时候回来F12这里边是有一个applicationapplication里边是有一个cookie看到了吗cookie的时候这个NameYD
[03:08] -cookie这个名称就这么着好吧这名称你只能是这么去查看要不然的话你获取不到好吧最终咱们就是可以去获取到一个html这是caller的html内容这个就是已经已经算是下载下来了下载下来之后没有用是吧你还要去解析对吧好咱们去试一下说none不等于干嘛不等于当起那个callerhtml然后
[03:38] 你就可以去解析了当然你要是iPad的话这样你可以再去加一个&stream youtube.isnotempty然后是就是当起这个什么内容然后现在就可以去解析了解析的方式咱们主要用的那种方式咱们这块是有一个叫做plotiparty这边写的有问题吗这个
[04:07] 点get html咱们可以用正则表达式的方式正则表达式你可以看像笔记中其实这有一个对等型的发取IP的正则表达式的预编译模式咱们可以拷贝过来好这样这滴滴滴是啥意思这还有个点看到了吗还有个点咱们打个包没有好滴滴滴还有墨号杠杠滴这什么意思呢
[04:37] 其实D是包含数字的是不是数字然后是数字点数字点数字点前面有三个点然后冒号然后还有一个数字其实你可以看一下当前的右键查看网页原代码其实说的咱们要去用证则表的是抓取的其实就是这么一段是不是数字点点点冒号冒号其实咱们要抓取的是这么个数据咱们只是用证则的方式去抓取的
[05:06] 好吧行这是一个行这样的话咱们用证则既然已经拿到了拿到的话咱们在这时候咱们就可以去直接用了不用呢你可以用当前的保持IP点没有一个卖这谁呢不是当前的好了HTML点盖的HTML给他其实就是咱们获取的解析后的一个内容这当然他是一个对象然后想要想获取内容的话你还得干嘛
[05:36] 你还得去判断下这里边很有可能会有多条所以说只要是这里边有值,只要它有值的话咱们就可以去循环的获取出来想获取第一部分怎么办?
[05:54] get不是get叫groupgroup里边其实可以一的话就包含什么?
[06:04] 是哪一份内容?
[06:07] 其实就是当前当
[06:09] 不相当于啥呢看一下不相当于一部分是这个内容然后第二部分是当前的端口号明白了吧所以说你这样拿的话是可以的你Ctrl D一下这个是二的话是什么是奥是吧好这样的话咱们就拿到了拿到之后那就很容易了这时候咱们要去返回当前的这么一个集合OK还容易这去先用出来一个
[06:42] 等于new array然后咱们在这去创建对象CLIP.PORT等于new他然后咱们就可以去往上设置了.setIPIP的话就是host好下面CLIP.setPort就这样就当前的PORT这两个值咱们设置完了这个报错了是吧
[07:12] 这没有事啊,包吹的话咱们就在这用当前的integer去弄一下,integer.有一个pass int好,就把它进来,泡到装机去就可以了那这样就可以了啊下面咱们还要再去设一些其他的比如说CLIP点什么呢,点一个set create time,不用设啊设一个time就可以了create time,又一个date
[07:47] 这样的话咱们就算是设置完了当然你也可以去设置一下它的来源是吧来源是啥呢点set一个叫做这个呢就是谁呀89免费代理你可以看一下啊目前这个内容是谁是不是有一个供应商啊这是供应商啊好你可以供应商就是谁呀就是89免费代理好吧
[08:18] 行那这个设置完之后到最终咱们就可以把当前对象装到这个集合中点add然后是把当前对象装进去里边可能会有多个他只要发现了他一直会循环好最终你把这个对象把这个机那边就返回就可以了这样的话咱们就算是解决完了行那这个b代理管理其实咱们也已经写完了写完之后咱怎么去测一下就这个咱们也是到后来
[08:53] 会去用当前的一个定时任务去做刚才也说过了是吧好那现在呀咱们就先不测了咱们一会呢就来去完成什么呢完成咱们的定时任务的添加

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在Java项目中通过Selenium和正则表达式从代理IP网站动态抓取并解析代理IP地址，封装成代理池对象。

2) 按时间顺序列出每张画面的要点：
画面1：在ProxyIpManager.java中，光标位于getGrabClipPoolList()方法的开始处，准备编写代码。
画面2：在方法内声明了一个私有变量seleniumClient，用于后续操作浏览器。
画面3：使用IDEA的代码提示功能，为seleniumClient添加@Autowired注解，表明其由Spring容器管理。
画面4：在方法内声明了crawlerProxyProvider和proxyGetUrl变量，用于获取代理URL。
画面5：切换到浏览器，查看代理IP网站的Cookie信息，其中包含一个名为yd_cookie的会话Cookie。
画面6：在代码中调用seleniumClient.getCrawlerHtml()方法获取网页内容，并使用正则表达式匹配IP。
画面7：在浏览器中查看网页源码，发现IP地址被嵌入在JavaScript代码中，通过弹窗显示。
画面8：在代码中使用WeakHashMap和相关类进行数据处理，准备解析IP。
画面9：再次查看浏览器源码，确认IP地址的存储位置。
画面10：在代码中使用Pattern.compile()编译正则表达式，用于匹配IP地址。
画面11：使用IDEA的代码提示功能，为变量选择合适的类型。
画面12：在代码中使用Matcher对象匹配IP地址，并提取IP和端口。
画面13：在代码中使用if语句判断匹配结果，并将匹配到的IP地址封装到ClipPool对象中。
画面14：在文档中查看ProxyIpManager类的结构，确认其包含@Autowired注解的字段和方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
log.info("插入代理ip,ip: {},port: {}",clipPool.getIp(),clipPool.getPort());
```

画面2：
```java
@Autowired
private SeleniumClient seleniumClient;
```

画面3：
```java
@Autowired
private SeleniumClient seleniumClient;
```

画面4：
```java
@Autowired
private CrawlerProxyProvider crawlerProxyProvider;
@Value("${proxy.get.url}")
private String proxyGetUrl;
```

画面6：
```java
CrawlerHtml crawlerHtml = seleniumClient.getCrawlerHtml(proxyGetUrl);
if (null != crawlerHtml && StringUtils.isNotBlank(crawlerHtml.getHtml())) {
```

画面10：
```java
Pattern proxyIpPattern = Pattern.compile("((\\d{1,3})\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}):(\\d{1,5})");
```

画面12：
```java
Matcher matcher = proxyIpPattern.matcher(crawlerHtml.getHtml());
while (matcher.find()) {
    String ip = matcher.group(1);
    String port = matcher.group(3);
    ClipPool clipPool = new ClipPool();
    clipPool.setIp(ip);
    clipPool.setPort(port);
    clipPoolList.add(clipPool);
}
```

画面14：
```java
/**
 * 动态代理管理服务
 */
@Component
@Logj2
public class ProxyIpManager {

    private static final ResourceBundle resourceBundle =
            ResourceBundle.getBundle("crawler");

    // 获取代理ip配置的URL
    private static final String proxyGetUrl = resourceBundle.getString("proxy.get.url");

    // 获取代理ip的正则表达式，预编译模式
    Pattern proxyIpPattern = Pattern.compile("((\\d{1,3})\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}):(\\d{1,5})");

    @Autowired
    private CrawlerProxyProvider crawlerProxyProvider;

    @Autowired
    private CrawlerIpPoolService crawlerIpPoolService;

    @Autowired
    private SeleniumClient seleniumClient;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：PPT标题为“day1_自动更新ip定时抓取ip自动更新文章”，其中包含“1.1 增加代理ip文件”、“2.1 ProxyIpManager类”、“4.1 代理ip自动更新”等子标题。

5) 不要评价画面美观，不要输出与课程无关的内容。

