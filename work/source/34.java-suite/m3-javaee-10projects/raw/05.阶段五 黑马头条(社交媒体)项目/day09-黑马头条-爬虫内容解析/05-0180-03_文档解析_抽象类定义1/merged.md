# 03_文档解析_抽象类定义1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\03_文档解析_抽象类定义1【海量资源尽在 666java.com】.mp4
- 时长 8分59秒（音频 540s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲啊刚才呢咱们是把这个类啊把这个类把这个类的方法呢给去拷贝了一下啊那这个呢其实都是一些通用的这些方法啊然后下面呢咱们去真正的去解析当前的文档啊那解析文档呢其实呢咱们在这儿可以再去创建一个包这个包叫Processor啊来打开创建一个包Processor
[00:30] C S O R 叫S S O R看一看叫S S O R 是吧好嘞 跑过来然后这个呢这个包下边是去解析当前页面用的咱们可以在这去创建类首先呢咱们还是需要有一些模板比如说咱们还是需要去创建一个这种模类这种抽象类好 它是一个抽象类
[01:00] 然后让他去继承谁让他去继承当前的这个类这样的话他通的方法咱们就用了同时不要忘了这里边还要去设一个processor我看看processor page没有配置吗我看看配置processor是吧配置processor写错了这个配置processor其实就是谁其实就是当前那个
[01:40] 就是当前那个webmatik它的一个类啊它的一个接口这个接口那这里边咱们需要去用到两个方法一个是processor啊能拿到当前配置对象然后呢还有一个站点还有站点啊那这个咱们定义完之后呢咱们下面呢就来去实现一些方法Ctrl-A我们需要实现哪个呢首先呢咱们是需要去实现当前的东西
[02:09] 这两个咱们要实现啊两个实现之后呢还有一个就是当前的handler咱们要去做啊handler你要在这块去实现好这两个好这个呢两个咱们就好这个啊这最后一个呢咱们都让那个他的一个子类让子类去实现因为这个呢知道吧当前这个什么啊poritypority是吧这个呢其实就是呀就是当前的什么优先级是吧
[02:36] OK那这几个方法咱们就算是实现完了这个方法咱们可以先控制过期咱们用到的时候呢可以再去定义那这个呢咱们需要去处理一下一会再处理这个方法呢其实咱们也可以控制它干嘛呢它呢就是processor是定制啥呢定制爬虫逻辑叫什么核心接口方法方法
[03:07] 然后在这里边写抽象逻辑因为这个毕竟是一个前面的一个Observate是一个抽象类可以把一些公用的东西可以放到这然后再往下看这个呢这个站点的话其实咱们可以去写一下这点目前的话其实它的代码是固定的代码是固定的这时候你需要干嘛你需要去用一个这种set
[03:38] 这个sit其实就是webmatic它提供的然后再往下你可以去创建set重视的什么时间重视的时间然后下面还有啥下面可以看set重视的睡眠时间是吧好再往下看还有啥还有一个就是set它的睡眠时间sleep好其实这东西不用记
[04:06] 工具机你直接拷贝过来其实也行没有问题再去设一个timeout同时时间东西咱们工具机中我们会用到这个东西好他就会去拿到一个站点这个站点后你就可以往这个站点里边干嘛往这站点里边去设置一些hiderhider的pitchhider其实刚才咱们说了这个hider的话咱们都是在哪定义的在当前
[04:35] ObservableProcessorFloat 是吧这里面是不是有啊所以说啊咱们在这可以直接去去过去getHeadmap里边其实有一个Headmap你可以看一下其实呢就跳到了前面里面好吧先拿到它之后呢咱们就可以去设置了啊嗯这时候咱们就可以去先去做一个判断啊说NUM不等于前面的什么
[05:05] heider map并且呢并且是heider map.isempty如果说它不会空这时候咱们就可以去复活循环了复活循环可以跟我写吧首先呢它是有一个map.entryentry里边其实就是两个范型第一个是sleuth第二个也是sleuth咱们叫entry
[05:37] 帽号是谁呢帽号就是header-map.entryset这时候你就可以往前的站点去设置他的header.get好这样的话就往
[06:03] 前这个站点的去设置了当然这个值啊咱们也可以写一些固定的值写一些固定的值啊你可以写在这写没有问题咱们也可以去抽出来是吧你可以抽出来比如说咱们在这去定义比如说public int getRetrieved times d i m e s我们可以直接return一个3
[06:35] 这时候你可以直接去调用这个方法其实也可以的好没问题这个其实就是谁就是当前的从事次数从事次数然后再往下看还有啥呢是public咱们还会返回一个int是从事间隔时间从事间隔时间咱们要去设get time然后是sleep time
[07:09] 这个呢咱们重拾间隔时间呢可以给它设置一个一秒一秒一千好吧这是毫秒啊可以设置一下要重拾间隔时间好吧没问题然后再往下还有啥呢还有一个抓取时间抓取的间隔时间get sleep time这个呢咱们可以也可以给个一秒好吧return一千好吧什么叫抓取
[07:47] 间隔时间好往下看啊然后还有一个叫超时时间不是时间啊publicint timeout就这么写吧好吧这是什么从事间隔时间啊超时时间啊超时时间啊这个呢咱们可以给长一下啊给长一下啊这个呢咱们就可以给给一个1万
[08:19] 十秒钟好吧这个咱们就算设置完了这样的话你就分别的就可以在这儿比如说咱们的这个同时间隔时间可以放到这儿是一个括号然后是抓取不是住区抓取换取间隔时间的咱们可以把它给考一下下面还有一个是吧叫get timeout这是什么
[08:54] 超时时间好吧行那就站点呢咱们就算是设置完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在爬虫框架中实现一个抽象的页面处理器（AbstractCrawlerPageProcessor），包括继承结构、核心方法实现以及如何配置请求头和站点参数。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前位于“6.3.3 抽象页面处理器AbstractCrawlerPageProcessor”章节，介绍该处理器的作用是处理页面并解析数据。
画面2：展示AbstractProcessFlow类的源码，定义了UserAgent数组，用于模拟浏览器访问。
画面3：在IDE中创建新的Java类文件，准备编写AbstractCrawlerPageProcessor。
画面4：在类定义中，继承AbstractProcessFlow并实现PageProcessor接口。
画面5：展示AbstractCrawlerPageProcessor类中需要重写的抽象方法，包括handle、process、getSite等。
画面6：在getSite方法中，开始定义返回的Site对象，并初始化其属性。
画面7：在getSite方法中，调用setRetryTimes、setRetrySleepTime、setSleepTime、setTimeout等方法设置站点参数。
画面8：在getSite方法中，定义了getHeaderMap方法，用于获取请求头，并返回一个包含Accept参数的Map。
画面9：在getSite方法中，使用for循环遍历请求头Map，准备将请求头添加到Site对象中。
画面10：在getSite方法中，使用Map.Entry遍历请求头Map，并调用addHeader方法添加请求头。
画面11：在getSite方法中，完成请求头的添加逻辑。
画面12：在getSite方法中，定义了getRetryTimes方法，用于获取重试次数。
画面13：在getSite方法中，使用try-catch块处理可能的异常。
画面14：在getSite方法中，完成所有参数设置并返回Site对象。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
6.3.3 抽象页面处理器AbstractCrawlerPageProcessor
com.heima.crawler.process.processor.AbstractCrawlerPageProcessor
/*
页面处理器抽象类，将通过 ProxyHttpClientDownloader 下载的数据进行解析处理。
从CrawlerConfigProperty配置中拿到解析类去进行数据的解析
*/
<>
<>

/*
对于博客页，HelperList是列表页，TargetList是文章页。
对于论坛页，HelperList是帖子列表，TargetList是帖子详情。
对于电商网站，HelperList是分类列表，TargetList是商品详情。
*/
```

画面2：
```java
public abstract class AbstractProcessFlow implements ProcessFlow {

    private CrawlerConfig crawlerConfig;
    @Autowired
    private CrawlerHelper crawlerHelper;

    // user agent 意思是用户代理，用户代理是一种才对数据打标，制造分段头，以及标识、传递消息的组件。
    // 用户代理是指浏览器，它的操作系统、它的软件、它的硬件、它的版本号，用户代理，它还包括它自己。
    private final String UserAgent[] = {
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Chrome/10.0.0.0 Safari/534.50",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Chrome/10.0.0.0 Safari/534.50",
            "Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Chrome/10.0.0.0 Safari/534.50"
    };
```

画面3：
```
package com.heima.crawler.process.processor;
```

画面4：
```java
import com.heima.crawler.process.AbstractProcessFlow;
public abstract class AbstractCrawlerPageProcessor extends AbstractProcessFlow implements PageProcessor {
```

画面5：
```java
@Override
public void handle(ProcessFlowData processFlowData) {

}
@Override
public CrawlerEnum ComponentType getComponentType() {
    return null;
}
@Override
public void process(Page page) {

}
@Override
public Site getSite() {
    return null;
}
```

画面6：
```java
@Override
public Site getSite() {
    class Site {
        // ...
    }
    return Site;
}
```

画面7：
```java
@Override
public Site getSite() {
    Site site = Site.m().setRetryTimes().setRetrySleepTime().setSleepTime().setTimeout();
    return site;
}
```

画面8：
```java
public Map<String, String> getHeaderMap() {
    Map<String, String> headerMap = new HashMap<String, String>();
    headerMap.put(UserAgentParameterName, getUserAgent());
    headerMap.put(AcceptParameterName, getAccept());
    return headerMap;
}
```

画面9：
```java
for (Map.Entry<String, String> entry : headerMap.entrySet()) {
    // ...
}
```

画面10：
```java
for (Map.Entry<String, String> entry : headerMap.entrySet()) {
    site.addHeader(entry.getKey(), entry.getValue());
}
```

画面11：
```java
site.addHeader(entry.getKey(), entry.getValue());
```

画面12：
```java
public int getRetryTimes() {
```

画面13：
```java
try {
    // ...
} catch (Exception e) {
    // ...
}
```

画面14：
```java
RetryTimes().setRetrySleepTime(getRetrySleepTime()).setSleepTime(getSleepTime()).setTimeout(getTimeout());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

