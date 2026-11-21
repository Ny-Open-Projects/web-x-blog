# 16_爬虫系统初始化_下载准备_下载类介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\16_爬虫系统初始化_下载准备_下载类介绍【海量资源尽在 666java.com】.mp4
- 时长 9分24秒（音频 565s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就接着往下讲刚才呢咱们是讲了两个帮助类对吧然后下面还有一些类啊咱们就有一个类需要去熟悉就是下载代理相关的代理下载相关的代理那个代理呢其实就是说有一个代理IP就是咱们之前讲过这个概念啊现在呢咱们有一个中文的这种类这个类呢其实就是来去提供代理的中文代理的啊但是这一块呢咱们还需要设置一步
[00:29] 这个呢你需要先去设定一个force也就是说默认的话咱们呢先不使用它默认是一个force那这个值呢其实在min这已经设置完了啊可以打开当前那个caller properties这儿啊咱们可以设定一个force好那设置完之后呢这时候呢咱们有一个帮助类provider有一个什么代理的提供者搜一下啊好就是当前的这个类啊这个类啊
[01:02] 那这个类呢首先呢是有两个锁有个读写锁是吧然后还有一个随机数嗯然后呢是当前读取的当前的一个呃当前到底是否是请用代理在末日处啊当然这个你也可以默认为force啊目前咱们准备阶段其实无所谓是吧然后下面呢是有一个方法有一个方法啊哪个方法呢就是有一个当前的这个方法这个方法啊就是咱们要去更新咱们的代理
[01:30] 那这个那这个是什么意思呢其实呢就是说咱们再去使用的时候比如说啊比如说你去访问了某个页面访问某个页面但是呢这时候你访问的时候呢有几种有几种情况第一种呢就是你本地啊在这写写写啊有可能呢是你的本地IP是吧然后第二个呢就是代理好代理IP代理IP咱们之前讲过啊呃
[02:03] 但是代理的话有可能会出现这种情况这个代理有可能会失效本地的话有可能会被封所以说咱们最好使用代理这个代理的话刚才说了有可能被封也就是说会失效失效的话这会就不能正常访问你的页面所以说这块内容咱们是有一个更新代理的操作更新代理的操作如果说这个IP一旦不能用
[02:31] 咱们就可以直接更新一下当前 IP但是更新的时候咱们需要去干嘛需要去加速下面还有一个就是设置IP不可用咱们也可以给大家说把它从当前 IP池中IP在里池中给它移除就可以了它其实就是个集合集合里边其实已经包含了咱们所有的能用或者不能用的IP这个东西咱们需要去进行判断当前这个类就是一个帮助类好吧就是来
[03:01] 提供当前的什么提供当前的一个可用的IP当然这里边也包含了判断好吧嗯行那这个怎么去用呢其实呢咱们还是得让他呢嗯还是让这个类啊被Sprint去容器去管理所以说呢咱们在这直接去考过来啊考哪啊还是考到老地方还是要考到当前的dollar这个中好
[03:27] 这个是没有是吧没有的话没有没有问题啊咱们在这可以直接去怎么着直接在这在下边也行是吧在下边也行啊输入一个呗什么的y6吧那要怎么写呢咱们要还要在这去看一下其实就是当前的这个写法啊把它拷贝一下拷到这这样的话就算是输入进来了没问题吧那这为什么包错了呢说它是一个布尔类型是吧
[04:11] 是布尔类型吗老实说这是布尔类型的话其实你也可以在这去直接去设立一个布尔类型其实这样也行也是可以的好吧那行那这个咱们就先说到这咱们接下来可以继续往下看这里边其实还有一个plussy http client download这个类这个类是干啥的其实这个类其实是要去盘虫的组件之一这个其实就是下载的组件
[04:47] 下载的组件但是下载组件其实咱们不用特意去管理为啥因为这个是要去继承当前一个overstrike的downloader其实这个类是谁这个类其实就是谁提供的就是当前的webmagic去提供的然后这里边大部分的圆满大部分类或者方法特别是当中的方法都是从圆满中去拷贝的
[05:14] 原本能拷贝的所以说你把这个类直接拷过来就可以了那你说直接引用不就行了吗为什么还要自己写这么个类呢其实这里边咱们稍微做了一些改造咱们先拷过来拷过来之后我再给你说一下为什么要进行改造好吧从这儿去选一下这类还是比较多的好拷贝拷完之后拷到哪呢拷到当前那个processor从这儿去创建一个download的文件夹download然后直接把这个类拷到这就可以了
[05:51] 那这个类呢你看稍等啊嗯错了是吧稍等啊他应该是他打包啊需要把这个包倒一下啊这个包也可以把这个也倒入一下啊然后看看哪还抱错稍等这plosy倒一下啊刚前的外边magic没有问题然后往下走看看哪还抱错跑包跑包阿里的不是阿里的啊咱们找一找啊咱们用的默认的啊默认的都是谁啊
[06:39] 默认的都是当前的http client其实就是第二个好倒完之后咱们再往下看看看看哪还报错html也要倒一下这个就是外部好吧还有报错的吗没找当前这个包怎么要倒一下再看一下当前的这个东西他说加个overlay加上好然后的话然后就没有报错了是吧没有报错了
[07:16] 行 那咱们就去说一下当前这里边有一个非常重要的方法这个方法其实就是download的方法就是当前下载页面的方法那这个方法其实咱们这里边去加了或者改造了当前这个类这个类其实最主要改造什么地儿往下看这里边其实是有一个下载失败的东西为什么会下载失败呢来看一下这块内容其实会有一个叫什么http client
[07:44] 其实webmatrix当前的框架它会默认先去使用http client去下载去发请求如果说一旦失败的话这时候咱们做了改造改造啥呢咱们用canim当前这个东西去下载这个方法是咱们自己奉劳的因为当前webmatrix它是默认使用当前这个去下载刚才也说了
[08:10] 咱们的CSDN它是有一个特殊的情况他们需要去更新cookie这时候他们需要用到当前的Clinium然后去下载这时候才能保证cookie的或者cookie的正确性所以说这块你稍微去做了些改造好咱们可以点一下这个方法做法其实就是咱们之前封装的用的是调用了当前Clinium Client然后去发了请求最终是把这页面给反回过来
[08:39] 算是能够正常下载也就是说说白了啊又是说什么呢呃一圆满啊假如说你要是不是cst是吧有可能其他网站不需要呃这种更新cookie的地儿呢你正常下载其实用他的这种圆满其实就完全OK了但是现在cst呢他有要求就是说这个cookie呢你需要更新一下所以说呢咱们在这啊去设置了两块
[09:03] 默认可以如果说默认的是使用HTTP client下载如果说一旦下载不成功这时候咱们再用Clinium去下载一遍这样的话就可以了好吧行这个咱们就说完了也就是说咱们现在已经完成了download就是下载模块的一些所有的准备工作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个基于 Selenium 的爬虫项目中，代理IP的管理与使用机制，包括代理IP提供者、配置、下载器类的实现与测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 `CrawlerProxyProvider` 类的源码，其中包含 `private ReadWriteLock lock`、`private Lock readLock`、`private Lock writeLock` 和 `private Random random` 等成员变量。
- 代码注释说明了类的作用是“随机获取一个可用的代理IP”。
- 代码中显示 `proxy.isUsedProxyIp=False`，但注释中提到“是否启动代理IP”。
- 左侧导航栏显示当前在“5 导入 heima-leadnews-crawler 项目”下的“6.2.6 代理IP相关（富文本使用代理）”章节。

画面2：
- 展示了 `CrawlerProxyProvider` 类中关于代理IP配置的代码段。
- 代码包含：`private boolean isUsedProxyIp = true;`（是否启动代理IP）和 `private int proxyIpUpdateThreshold = 10;`（动态代理IP自动更新阈值）。
- 代码注释说明了“是否启动代理IP”和“动态代理IP自动更新阈值”。

画面3：
- 展示了 `CrawlerProxyProvider` 类中 `updateProxy()` 方法的代码段。
- 代码包含：`if (isUsedProxyIp && null != proxyProviderCallBack) { ... }`，用于判断是否使用代理IP并调用回调。
- 代码中包含 `readlock.unlock();`、`writeLock.lock();`、`writeLock.unlock();` 等锁操作。
- 画面中弹出一个“快捷方式”对话框，显示“大小：800 x 100，宽度：200，高度：250”。

画面4：
- 展示了 `CrawlerProxyProvider` 类的源码，与画面1内容基本一致，但光标位置不同。
- 代码中显示 `private boolean isUsedProxyIp = true;` 和 `private int proxyIpUpdateThreshold = 10;`。
- 左侧导航栏显示当前在“6.2.6 代理IP相关（富文本使用代理）”章节。

画面5：
- 展示了 `CrawlerConfig.java` 文件中的 `DataValidateCallBack` 类的实现。
- 代码包含：`public boolean validate(String content) { ... }`，用于验证内容是否包含特定字符串。
- 代码中包含 `if (StringUtils.isEmpty(content)) { flag = false; }` 和 `if (containsLocationReload) { flag = false; }` 等判断逻辑。
- 代码注释说明了“数据校验层名称类”和“Return”。

画面6：
- 展示了 `CrawlerConfig.java` 文件中 `isUsedProxyIp` 的配置。
- 代码包含：`@Value("${proxy.isUsedProxyIp}") private boolean isUsedProxyIp;`，用于从配置文件中读取代理IP是否启用。
- 代码中包含 `@Bean` 注解和 `@Configuration` 注解，用于配置Bean。
- 代码中包含 `@Autowired` 注解和 `@Component` 注解，用于依赖注入。

画面7：
- 展示了 `ProxyHttpClientDownloader` 类的源码。
- 代码包含：`@Autowired private CookieHelper cookieHelper;`、`@Autowired private CrawlerHelper crawlerHelper;`、`@Autowired private CrawlerProxyProvider crawlerProxyProvider;`、`@Autowired private SeleniumClient seleniumClient;`。
- 代码中包含 `private final Map<String, CloseableHttpClient> httpClients = new HashMap<>();` 和 `private HttpClientGenerator httpClientGenerator = new HttpClientGenerator();`。
- 代码注释说明了“增加了下载失败后自动重用 selenium 的方式进行文件下载”。

画面8：
- 展示了 `SeleniumClientTest.java` 文件中的测试类。
- 代码包含：`@SpringBootTest` 注解和 `@RunWith(SpringRunner.class)` 注解。
- 代码中包含 `@Autowired private SeleniumClient seleniumClient;`。
- 代码中包含 `public void test() { ... }`，用于测试 Selenium 客户端。
- 代码中包含 `System.out.println(seleniumClient.getHtml());`，用于打印 HTML 内容。

画面9：
- 展示了 `ProxyHttpClientDownloader` 类中 `setProxyProvider` 方法的代码。
- 代码包含：`public void setProxyProvider(ProxyProvider proxyProvider) { this.proxyProvider = proxyProvider; }`。
- 代码中包含 `if (site == null) { return httpClientGenerator.getHttpClient(site: null); }`。
- 代码中包含 `String domain = site.getDomain();` 和 `if (httpClient == null) { synchronized (this) { ... } }`。

画面10：
- 展示了 `ProxyHttpClientDownloader` 类中 `setThread` 方法的代码。
- 代码包含：`public void setThread(int Thread) { httpClientGenerator.setPoolSize(Thread); }`。
- 代码中包含 `protected PageHttpResponse(Request request, String charset, HttpResponse httpResponse, Task task) { ... }`。
- 代码中包含 `import org.apache.http.client.methods.HttpResponse;` 和 `import org.apache.http.client.methods.HttpRequest;`。
- 代码中包含 `import org.apache.http.client.methods.HttpPost;` 和 `import org.apache.http.client.methods.HttpGet;`。
- 代码中包含 `import org.apache.http.client.methods.HttpPut;` 和 `import org.apache.http.client.methods.HttpDelete;`。
- 代码中包含 `import org.apache.http.client.methods.HttpHead;` 和 `import org.apache.http.client.methods.HttpOptions;`。
- 代码中包含 `import org.apache.http.client.methods.HttpTrace;` 和 `import org.apache.http.client.methods.HttpPatch;`。
- 代码中包含 `import org.apache.http.client.methods.HttpPurge;` 和 `import org.apache.http.client.methods.HttpMkcol;`。
- 代码中包含 `import org.apache.http.client.methods.HttpCopy;` 和 `import org.apache.http.client.methods.HttpMove;`。
- 代码中包含 `import org.apache.http.client.methods.HttpLink;` 和 `import org.apache.http.client.methods.HttpUnlink;`。
- 代码中包含 `import org.apache.http.client.methods.HttpPropfind;` 和 `import org.apache.http.client.methods.HttpProppatch;`。
- 代码中包含 `import org.apache.http.client.methods.HttpLock;` 和 `import org.apache.http.client.methods.HttpUnlock;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMerge;` 和 `import org.apache.http.client.methods.HttpMkactivity;`。
- 代码中包含 `import org.apache.http.client.methods.HttpReport;` 和 `import org.apache.http.client.methods.HttpSearch;`。
- 代码中包含 `import org.apache.http.client.methods.HttpNotify;` 和 `import org.apache.http.client.methods.HttpSubscribe;`。
- 代码中包含 `import org.apache.http.client.methods.HttpUnsubscribe;` 和 `import org.apache.http.client.methods.HttpMkcalendar;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkresource;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含 `import org.apache.http.client.methods.HttpMkworkspace;` 和 `import org.apache.http.client.methods.HttpMkworkspace;`。
- 代码中包含

