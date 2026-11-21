# 15_爬虫系统初始化_下载准备_帮助类介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\15_爬虫系统初始化_下载准备_帮助类介绍【海量资源尽在 666java.com】.mp4
- 时长 7分45秒（音频 466s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就接着往下讲然后下面呢是有一个爬虫相关的一些帮助类这些帮助类呢大家呢也要熟悉一下咱们呢可以打开代码不是这个把这个关掉这里边呢是有一个叫helper这个包其实已经提供好了咱们可以把其他的没用的先关掉关掉然后你首先呢可以打开第一个叫cookie helper然后这里边内容呢其实呢就是来去更新cookie
[00:31] 咱们也可以去读一下这段话说Cookie helper主要是用于管理爬取过程中使用对应代理Cookie的管理CSDN的网站的关键是与Cookie与IP做了绑定这时候要不是CSDN的话比如说你要是爬取其他文章的其他网站有可能不会出现这个问题但是CSDN它现在是跟IP是绑定了所以说咱们现在
[01:00] 有的时候需要去更新一下cookie这时候你才能获取到你想要的那种好吧那行咱们可以往下看这里边的方法这里边的方法其实没有几个主要是有一个方法就是当前的update cookie那这个你看首先是通过了当前的plot就是plot其实咱们之前讲过这里边其实就是在里是吧就是里的一个什么house和pot
[01:31] 通过这个呢去获取它的cookie列表然后呢看看有没有如果说必须要是有或者没有如果说它不等于那啊不等于那这时候呢咱们直接干嘛呢直接就是清空清空之后呢重新去获取获取完之后重新往里边设置就可以重新往里边设置啊那这是强制更新下面还有一个更新更新的话咱们就是它为空的时候呢咱们再去往里边去怎么着再去往里边设置
[02:00] 就这么个操作行这个其实就是sysdn的一些特点或者网站的特点所以说咱们需要去更新cookie这一步所以说有了这么当前一个cookie helper好除了这个类之外其实下面还有一个类咱们可以看一下文档这里边其实还有一个这有一个color什么呢config不对下面应该是当前这个帮助类但是帮助类之前
[02:30] 说这个之前呢咱们还要再去在这去配置一下用一样说了这块呢你这个类你这个类想在本项目中去使用的话你得去干嘛呢你得让他呢呃被Spring容器去管理那这时候怎么办呢这时候你可以非常简单啊咱们呢可以直接去在这在这呢去配置一步就可以啊咱们可以看一下文档这里边呢只是去扭了一下就可以扭了一下啊再把呢我就直接考过来了
[03:05] 这里边其实还少个东西看到了吗有一个什么c-r-u-c cookie namecookie name那这cookie name是谁其实呢这个cookie name呢刚才说了咱们其实咱们在一开始讲那个cookie的时候就说了这里边呢其实有一个cookie的名称看到了吧其实呢就是这个名称其实就这个名称那这个名称你要想拿到容易吗很容易是吧怎么拿呀咱们呢只需要在这儿
[03:35] 这样吧咱们就定义一个变量private string比如说就是他好吧然后下面加什么这个value是吧然后怎么着说服他然后就是你前面的这一段前面的这一段好因为这么拿是完全可以的好吧问题这样的话咱们就拿到了当前的值拿到这个值
[04:11] 行这个咱们设置完之后咱们以后再去用的时候直接是注入当前 cookie helper就可以了因为我已经让他被Spring去管理了对吧行咱往下看除这个类之外其实还有一个帮助类叫什么caller helper咱们可以看这个类这里其实就是也是在当前helper这个包下面还有一个叫caller helper打开
[04:39] 这里面其实有一个抓取辅助类里边是有一个非常重要的方法大家需要知道就是这一块这一块这一块会用是啥呢其实我要中间去讲的是有一个request那这个request是谁呢我可以告诉你这个request其实就是谁其实就是当前的就是webmagic它提供的一个request其实咱们之前说流程的时候说了其实咱们是有一个下载是吧
[05:08] 下载之前是不是还有一个访问URL对吧那访问URL你访问的URL或者是说你怎么去解析呢这时候咱们的中间的操作的对象其实都是request其实都是request咱们可以从request中去拿到你想要的什么想要的这种数据而且这个方法是本身提供的
[05:32] 这是request也就是说外包matic这个包本身就已经给你提供好了当前的一个方法或者说或者说当前那个request他已经给你封装好了你只要从这里边去获取你想要的数据就可以了但这个数据怎么怎么拿呢咱们都咱们呢也可以去存可以去可以去存这边只是说了一下获取就存的方式其实差不多啊嗯行啊那这个呢其实就是一些东西嗯就可以咱们的这样咱们可以继续往下看啊
[06:02] 其实这个就是设置啊这个设置啊刚才是少说了一步啊这一块内容呢其实就是往里边去put这是key是吧这是就是你的path item这个path item其实咱们之前说过啊其实就是什么呢就是你当前要解析的内容啊给的内容啊ok他还有一个这个类还有一个当前的color path item其实这个呢就是具体要解析的某一个字段某一些字段就是这里边的封装类东西啊
[06:30] 行这个咱们说完之后下面还有一些咱们需要知道再往下其实还有一个验证还有一个验证这验证就是说咱们的数据也可以进行验证OK行这个咱们就说到这这个也可以去看一看用到的时候咱们还会再拿出来去说你现在要知道当下的caller hyper咱们可以用这个quest中从哪从URL中去获取内容从配置中去获取内容然后去解析然后第二个就是去
[06:58] 解析不是要解析应该要验证验证当前的一些东西那这块呢其实呢咱们还是要去封装到哪是不是还是在封装到caller config呢所以说咱们还是要去再做一步好咱们可以直接去把它拷过来这时候呢咱们呢其他类中想要去使用的时候呢直接去注入当前的caller helper咱们就可以用了那你说上面还有东西啊上面的其实就是些验证的规则
[07:31] 认识规则这个是默认的大家一定要去考过来就可以了其实你考过来就可以了行行行OK那这个咱们就说完了后期咱们用到的时候直接注入当前这两个还有跑累就可以好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解爬虫项目中 CookieHelper 辅助类的实现细节，包括代理管理、Cookie 缓存、配置读取和数据校验等功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程目录结构，当前位于“6.2.4 爬虫相关类”章节，聚焦于“cookie操作的辅助类”。
画面 2: 在 IntelliJ IDEA 中展示 CookieHelper.java 文件，显示类的构造函数和成员变量，包括 proxyCookieCacheMap 和 seleniumClient。
画面 3: 展示 CrawlerProxy.java 文件，定义了代理服务器的构造函数和 getProxyInfo 方法。
画面 4: 展示 CookieHelper.java 文件，聚焦于构造函数和成员变量的定义。
画面 5: 展示 CookieHelper.java 文件，高亮了 getCookieList 方法，该方法根据 URL 和代理获取并更新 Cookie 列表。
画面 6: 展示 crawler.properties 配置文件，包含 WebDriver、代理、Cookie 等配置项。
画面 7: 展示 CrawlerConfig.java 文件，定义了 prefix 和 suffix，并实现了一个获取 Cookie 名称的公共方法。
画面 8: 展示 CrawlerConfig.java 文件，高亮了 getCookieHelper 方法，该方法通过 CRUX_COOKIE_NAME 获取 CookieHelper 实例。
画面 9: 展示 CrawlerHelper.java 文件，高亮了 setParseItem 方法，用于设置解析数据。
画面 10: 展示 CrawlerParseItem.java 文件，定义了解析项的属性，如 id、summary、url、spatialUrl、tag。
画面 11: 展示 CrawlerHelper.java 文件，高亮了 requestValidation 方法，用于校验下载数据。
画面 12: 展示 CrawlerHelper.java 文件，高亮了 requestValidation 方法，显示了日志输出“校验下载数据完成”。
画面 13: 展示 CrawlerConfig.java 文件，高亮了 getCrwalerHelper 方法，该方法创建并配置了 CookieHelper 和 DataValidateCallBack。
画面 14: 展示 CrawlerConfig.java 文件，高亮了 getCrwalerHelper 方法，显示了完整的配置逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
6.2.4 爬虫相关类
爬虫Cookie帮助类
cookie操作的辅助类
com.heima.crawler.helper.CookieHelper
```

画面 2:
```java
public class CookieHelper {

    /**
     * 代理ip存储的地方
     * <p>ip端口、cookie列表
     */
    private Map<String, List<CrawlerCookie>> proxyCookieCacheMap = new ConcurrentHashMap<String, List<CrawlerCookie>>();

    /**
     * 数据锁
     */
    private final String SYNCHRONIZED_TAG = "SYNCHRONIZED_TAG";

    private SeleniumClient seleniumClient = new SeleniumClient();

    public CookieHelper() {

    }
```

画面 3:
```java
public class CrawlerProxy implements Serializable {

    public CrawlerProxy(String host, Integer port) {
        this.host = host;
        this.port = port;
    }

    private String host;
    private Integer port;

    /**
     * 获取代理信息
     */
    public String getProxyInfo() {
        return host + ":" + port;
    }
```

画面 4:
```java
public class CookieHelper {

    /**
     * 代理ip存储的地方
     * <p>ip端口、cookie列表
     */
    private Map<String, List<CrawlerCookie>> proxyCookieCacheMap = new ConcurrentHashMap<String, List<CrawlerCookie>>();

    /**
     * 数据锁
     */
    private final String SYNCHRONIZED_TAG = "SYNCHRONIZED_TAG";

    private SeleniumClient seleniumClient = new SeleniumClient();

    public CookieHelper() {

    }
```

画面 5:
```java
public List<CrawlerCookie> getCookieList(String url, CrawlerProxy proxy) {
    List<CrawlerCookie> cookieList = getProxyCookieListGroup();
    if (null != cookieList && !cookieList.isEmpty()) {
        return cookieList;
    } else {
        List<CrawlerCookie> implList = getNewCookieInitList(url, cookieName, proxy);
        updateCookie(implList, proxy);
        return cookieList;
    }
}
```

画面 6:
```
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
# linux
webdriver.chrome.driver=/usr/bin/chromedriver

proxy.get.url=http://www.89ip.cn/tqdl.html?api=1&num=50&port=80&address=isp&
proxy.validate.url=http://http://www.ip138.com/ips138888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

