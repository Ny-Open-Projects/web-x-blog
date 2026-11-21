# 02_文档解析_前置准备工作

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\02_文档解析_前置准备工作【海量资源尽在 666java.com】.mp4
- 时长 4分30秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就接着往下讲啊来继续看啊然后这边呢是有一个工具类呢那需要大家去熟悉啊这工具类呢是就在当前这个U2C包下边有一个叫PathRulerU2C啊这个东西而这个东西呢其实呢就是又有一些教验的规则啊关于内容的一些合并什么的啊这个咱们到具体用的时候呢咱们再去可以再去详细去说好吧
[00:27] 这东西的你就知道一下目前的话有一个解析规则的工具类然后再往下看再往下看这一块内容的其实有一个speeder是吧这东西咱们需要去配置到color config那为什么配它呢因为咱们下面要去真正的去解析当前的页面解析页面的时候咱们需要用到当前这个speed它是谁提供的是当前的这种
[00:54] webmagic提供的一个对象这个对象咱们需要用着所以说咱们把它统一的让当前这个color config去管理所以说咱们在这我已经考虑过来了其实你直接考过来就可以好吧这个对象再去说一遍这个对象呢就是谁呀是webmagic提供的一个对象好吧就是爬虫对象那这个说完之后下面还有一个类那这个类呢其实需要添加一些方法那这个方法是谁呢
[01:23] 你看把这个方法都给你考过来了好老板呢考到当前那个Obspect然后是Process Flow啊考到这个里边好考过来考过来之后啊应该会有包错吗看看啊嗯有包错是吧那为什么要考到这呢其实呢咱们现在啊都是大家也能够发现啊其实咱们之前也大概就说过
[01:50] 目前的话咱们是有一个流程的就是爬虫呢它是有一个流程的首先呢咱们会去获取初始化的URL是吧然后下面呢咱们会去下载有那个URL咱们就下载然后呢咱们再去解析解析之后呢再去下载但是这个解析咱们还没有写咱们马上就会去写但是这些啊刚才我说的这个下载解析还有后期的排虫和具体的这种内容的解析咱们统一的
[02:19] 都会去用到当下什么都会用到当前这个模板类都用到这个模板类它是一个overstrike这种它是一个什么这种什么抽象的类咱们这些所有的功能的类比如说下载初始化咱们一会儿会去解析都要去继承当前这个overstrike的这个process flowOK那这里边有什么功能呢那这里边其实就是抽取了一些抽取了什么东西一些
[02:49] 通用的数据或通用的方法或通用的一些参数OK啊OK咱们咱们可以看一下刚才考过来的这些东西啊其实考过来这些东西呢其实并不难啊主要呢这些东西呢你也不用说特意去去要用非要去手写其实没有必要啊你看啊那首先呢这是注入两个东西一个是caller config一个是caller helper
[03:15] 当然这里边是主要的最主要咱们考虑过来就是能够为了设置请求头设置请求头这个是user agent是吧然后下面是有一个exec当然在这里边咱们还有获取的方法获取当前请求的方法这时候方便让子类去调用方便让子类去调用当然这里边还去封装了一个requestrequest的话咱们有两种方式第一个就是
[03:44] 通过URL去获取第二个是通过当前那个passitem去获取都是获取request都是获取request行那这个request得说一下这个request其实不是你们之前立的request它是webmatic包下边的一个请求对象webmatic的行那这两个咱们就设置完了设置完之后这里边还有一个添加往request中去添加数据这个也有
[04:11] 然后其他的话就没有太多东西了好吧一会咱们去用到的时候咱们可以再去讲再去讲啊行那目前的话咱们这个解析的准备工作啊咱们先说到这儿啊一会呢其实咱们再去创建具体的解析的这种解析器

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个爬虫项目中 AbstractProcessFlow 类的实现细节，包括 UserAgent 和 Accept 头部的配置、请求封装方法以及如何获取随机的 UserAgent 和 Accept。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，当前选中的是 src/main/java/com/heima/crawler/process/AbstractProcessFlow.java。
画面2：展示 ParseRuleUtils.java 文件中的 parseRuleList 方法，用于解析规则列表。
画面3：展示 PPT 内容，讲解“抽取页面处理器”的相关概念，包括 AbstractCrawlerPageProcessor 等类。
画面4：展示 CrawlerConfig.java 文件，定义了 parseRuleList 方法和 Spider 对象。
画面5：展示 PPT 内容，讲解 UserAgent 的定义和作用。
画面6：展示 AbstractProcessFlow.java 文件，定义了抽象类。
画面7：展示 AbstractProcessFlow.java 文件，定义了 CrawlerConfig 和 CrawlerHelper 字段。
画面8：展示 AbstractProcessFlow.java 文件，定义了 UserAgent 字段。
画面9：展示 AbstractProcessFlow.java 文件，定义了 UserAgent 字段。
画面10：展示 AbstractProcessFlow.java 文件，定义了 UserAgent 字段。
画面11：展示 AbstractProcessFlow.java 文件，定义了 getHeadersMap 方法。
画面12：展示 AbstractProcessFlow.java 文件，定义了 getRequest 方法。
画面13：展示 AbstractProcessFlow.java 文件，定义了 getAccept 方法。
画面14：展示 PPT 内容，讲解 AbstractCrawlerPageProcessor 类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public static List<ParseRule> parseRuleList(Html html, List<ParseRule> parseRuleList) {
    List<ParseRule> ruleList = parseContent(html, parseRuleList);
    effectiveParseRuleList = getEffectiveParseRuleList(ruleList);
    return effectiveParseRuleList;
}

/**
 * 获取有效的抓取规则
 */
private static List<ParseRule> getEffectiveParseRuleList(List<ParseRule> parseRuleList) {
    return parseRuleList;
}
```

画面4：
```java
// 重复次数
add(new ParseRule("commentCount", CrawlerEnum.ParseRuleType.XPATH, "//div[@class='tool-bar']//span[@class='comment-count']");
add(new ParseRule("content", CrawlerEnum.ParseRuleType.XPATH, "//div[@class='content_rich']");
return parseRules;
```

画面5：
```java
/**
 * UA
 * user agent 是意思用户代理，用户代理是一种对数据打包、创建分组、以及编辑、传递信息的邮件。
 * 用户代理是指浏览器，它的信息包括硬件平台、系统软件、应用软件和用户个人偏好。用户代理，它还包括搜索引擎。
 */
private final String UserAgent[] = {
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Chrome/10.0.0.0 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/6.0.1250.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490

