# 02_爬虫系统完善_增加代理下载

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\02_爬虫系统完善_增加代理下载【海量资源尽在 666java.com】.mp4
- 时长 9分54秒（音频 594s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去做这个爬虫系统的完善啊首先呢第一个呢是增加代理下载其实在咱们爬虫系统之前呢之前做的开发呢其实呢都是本地去请求咱们的cstn并没有设置这种ip代理那下面呢咱们要去启用当前这个代理去下载啊然后这是一块内容啊还有第二个呢是设置一个逆向爬曲
[00:27] 这也是咱们完善的一部分咱们之前一直在做正向的爬曲文章现在咱们要去这种设置逆向的爬曲文章咱们还是说回来当前增加代理这一块其实在咱们之前你可以看一下在当前 caller 系统中这是有一个 properties有一个 color properties里面是有这么一项叫 proxy is used 什么possi ip它是一个 force
[00:55] 意思就是不使用代理不使用代理的话就用你本机的IP或本机的这种网络去请求好然后下面呢咱们就要去设置咱们的这个代理的方式啊那这个代理的方式呢其实这样啊咱们这段代表最主要的方式就是咱们要去从表中去读当前的什么呢当前的这种IP代理列表然后呢咱们要去检查一下到底哪些不可用啊咱们可以去设置为它不能用
[01:25] 好吧那这个表呢是这样啊这个表的话就是我刚我现在打开这边啊就是cr-ip-pro就这个ip代理池的这个表好吧嗯那行那下下面呢咱们就来去设置一下这个在哪配呢这个呢你看这个是就是在当前的colorconfig中去设置好咱们打开当前这个列啊在这有一个colorconfig啊啊你看啊那我这块呢是直接定位在这的啊
[01:55] 那这块呢是之前的是有这么一个方法啊就是让sprint去管理当前那个color proxy provider啊但是呢并没有去设置或者并没有去获取IP所以说呢这块咱们要去补充一下就可以了补充一下啊下面呢咱们可以去设置一个动态代理IP我写呢好设置动态代理好吧没有当前那个color
[02:24] plausiprovider.set一个叫做plausiprovidercallback里边咱们就扭出来一个叫plausiprovidercallback这里边有两个方法这里边有一个方法是吧是获取列表然后还有一个是让某一个IP去失效这里边没有的话咱们就这样我们就在这定义一个好吧public然后咱们是void
[02:53] 这样的话咱们就是让他呢去失效好这个参数呢就是一样参数就是caller那这样的话咱们就说完了啊那是完之后啊这还需要再去加一个方法那就是这两个方法分别的话咱们就来去使用这两个方法去完成这两个方法啊那第一个呢就是当干嘛获取当前的什么caller
[03:26] WareaPalsy这边Palsy List这是一个是吧这个方法没有没事咱们一会去创建然后第二个就是咱们要去这个P比如检查完之后的IP不能用不能用的话咱们要去设置怎么着他不能用可用现在咱们叫Palsy这你要传个参数传个参数就是当前的Color Palsy这里边因为是有当前的P和当前的口号
[03:58] 那行那咱们下面就来去实现一下啊是房间一个咱们就放在外边就可以了啊public然后返回值呢就是他这个是没有参数啊没有参数第二个呢就是这个方法这个方法啊再写一下public然后这是void因为这个咱们需要去设置某个IP为失效啊所以说那是void就可以了啊
[04:34] 猜数的就是他,猜数就是这个那行那咱们下面就来去就是这两个方法啊那这个呢主要呢还是得从数据库中去查询写下一下啊获取初始化的IP列表好那这个该怎么去做呢这个咱们首先呢还是得去先去注入一个东西啊private
[05:10] 这个咱们之前是叫什么了这钱的话咱们叫我看看啊这叫就他是吧叫callerip pro Service我们之前创建过这个Service啊把它给注入进来然后呢然后的话咱们就可以去写代码了啊这会儿呢就说该怎么去写呢你直接查就行了吗其实也不是啊这会儿呢咱们需要去做一些判断做一些判断啊那做哪些判断呢好来看一看啊
[05:42] 咱们去查的时候你看这里边有个方法非常简单就QA直接去查这种没有失效的或者可用的这种IP就可以了是他呢他是一个什么一个CLP是吧是一个这么个对象CLP就他这么个对象等于你有一个CL他那咱们到底设置是哪些条件呢这里边咱们要去设置一个条件就是当前的
[06:15] set有一个叫做UIA这个呢其实是响应的时间这时间呢是设置5的话就是小于等于5秒这样的话呢就是你的响应你的IP响应速度越快它的值越小那小于等于5秒的咱们就以为这个IP能用所以说咱们查的时候干嘛呢只查能用的数据就可以了听明白吧所以说呢在这直接按一下
[06:45] 就能去查到一个列表这个里边啊他那边之后啊怎么就可以在这啊直接去乱下如果说那不等于当前的啊s啊而且呢干嘛解非是吧怎么着啊而意思不得如他不为空那这时候呢咱们就可以去返回这么个里边那这么里边呢并不是这里边所以说咱们要去构建当前这个里边啊这样去创建一个他
[07:16] 叫color-policy-list等于new array下面你就可以去循环它了啊点复好 循环了啊循环完之后呢你这时候呢你就可以去往里边去设值怎么设值呢
[07:44] 你直接去new一个colorplussy就可以了这里边传两个参数第一个呢就是当前ipplussy的get一个ip这是ip啊第二个呢就是ipplussy.getout就是两个一个是什么一个是ip一个是口号那这样可以了最终呢你把这个列表返回不就完了吗
[08:13] 那这样的话就能去拿到一些可用的IP的列表行那这是一个方法那么下面继续就这个方法也给写一下那这是啥意思呢这是代理IP代理IP不可用处理方法直接让那个IP干嘛呢失效就可以了那这里边咱们也是去设置一下我说当前的
[08:46] 当前的他呢不等于那然后呢咱们就可以去调用Color IP Service讲什么呢有一个叫做Awareful Policy这里边呢有两个参数啊一个呢就是当前的Proxy其实你就把当前那个Color Proxy传进去就可以了因为这里边含了IP和端口第二个呢你就可以说有一个描述是吧说自动禁用
[09:15] 好那这样的话咱们这个方法呢就算是复利完了那你说现在写完之后能不能测一下呢这样啊咱们一会儿还会再去说当前的一个IP代理更新这样咱们更新完之后有可用的IP之后呢咱们可以再测好吧这边呢咱们先挤到这但是这个咱们一会儿测试的时候啊有个参数也必须要改哪个参数啊就是当前的这个参数因为目前的话呢是一个force咱们测的时候需要去设置回来
[09:45] 设置为出就可以了好吧行那这个啊增加代理增加代理这个下载呢咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在爬虫系统中配置和使用代理下载功能，包括配置文件、代理提供者类和代理池服务的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示CrawlerConfig类中定义的CrawlerProxyProvider bean，包含设置代理IP和回调方法的代码。
画面2：在CrawlerConfig类中，光标位于getProxyList()方法的return语句上，准备返回代理列表。
画面3：展示crawler.properties配置文件，其中包含webdriver、proxy、csdn.comment.url等配置项，以及proxy.isUsedProxy=false的设置。
画面4：在CrawlerConfig.java中，展示@Value("${proxy.isUsedProxy}")注解用于注入配置值，并显示了initCrawlerXPath的定义。
画面5：展示ProxyProviderCallBack接口，定义了getProxyList()和unavailable()两个方法。
画面6：在CrawlerConfig.java中，展示setProxyProviderCallBack方法的调用，以及unavailableProxy方法的实现。
画面7：在CrawlerConfig.java中，光标位于public void后，准备添加新方法。
画面8：展示CrawlerIpPoolService类的代码，包含queryAvailableList、unavailableProxy等方法。
画面9：在CrawlerConfig.java中，展示List<CrawlerProxy> crawlerProxyList的声明和初始化。
画面10：在CrawlerConfig.java中，展示创建ClipPool对象、设置超时时间、查询可用代理列表的代码。
画面11：在CrawlerConfig.java中，展示遍历可用代理池并添加到列表中的代码。
画面12：在CrawlerConfig.java中，展示unavailableProxy方法的实现，调用crawlerIpPoolService的unavailableProxy方法。
画面13：在CrawlerConfig.java中，展示unavailableProxy方法的完整实现，包含if判断和调用服务方法。
画面14：展示课程PPT页面，标题为“1 爬虫系统完善”，子标题“1.1 增加代理下载”，并显示了CrawlerConfig类的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Autowired
private CrawlerIpPoolService crawlerIpPoolService;

@Bean
public CrawlerProxyProvider getCrawlerProxyProvider() {
    CrawlerProxyProvider crawlerProxyProvider = new CrawlerProxyProvider();
    crawlerProxyProvider.setUsedProxyIp(isUsedProxyIp);
    //使用动态代理
    crawlerProxyProvider.setProxyProviderCallBack(new ProxyProviderCallBack() {
        @Override
        public List<CrawlerProxy> getProxyList() {
            return getCrawlerProxyList();
        }
        @Override
        public void unavailable(CrawlerProxy proxy) {
            unavailableProxy(proxy);
        }
    });
    return crawlerProxyProvider;
}
```

画面3：
```properties
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
# Timeout
proxy.get=http://www.89ip.cn/tqdl.html?api&num=1&port=&address=&type=&charset=&anonymity=&sort=1&protocol=&dist=&proxyType=&proxyList=
proxy.validate.url=http://wip.kkcha.com/
# 是否启用代理
proxy.isUsedProxy=false
csdn.comment.url=https://blog.csdn.net/author)/phoenix/comment/list/?page=1&size=100
crawler.init.url.prefix=https://www.csdn.net/nav/
crawler.init.url.suffix=java
crawler.init.url.suffix=java
crawler.help.nextPagingSize=0
#1次爬取时间
crawler.nextupdatetime=4,16,64,128,256
```

画面4：
```java
@Value("${proxy.isUsedProxy}")
private Boolean isUsedProxyIp;

//设置动态代理
private String initCrawlerXPath="//ul[@class='feedlist_mod']//li[@class='clearfix']/div[@class='article-item-box']//div[@class='article-item-title']//a[@class='article-title']";
```

画面5：
```java
package com.heima.crawler.model.crawler.core.callback;

import ...

public interface ProxyProviderCallBack {
    public List<CrawlerProxy> getProxyList();
    public void unavailable(CrawlerProxy proxy);
}
```

画面6：
```java
public CrawlerProxyProvider getCrawlerProxyProvider() {
    CrawlerProxyProvider crawlerProxyProvider = new CrawlerProxyProvider();
    crawlerProxyProvider.setUsedProxyIp(isUsedProxyIp);
    //设置动态代理
    crawlerProxyProvider.setProxyProviderCallBack(new ProxyProviderCallBack() {
        @Override
        public List<CrawlerProxy> getProxyList() {
            return getCrawlerProxyList();
        }
        @Override
        public void unavailable(CrawlerProxy crawlerProxy) {
            unavailableProxy(crawlerProxy);
        }
    });
    return crawlerProxyProvider;
}
```

画面8：
```java
public List<CrawlerProxy> getCrawlerProxyList() {
    List<CrawlerProxy> crawlerProxyList = new ArrayList<>();
    ClipPool clipPool = new ClipPool();
    clipPool.setDuration(5);
    List<ClipPool> clipPools = crawlerIpPoolService.queryAvailableList(clipPool);
    if (null != clipPools && !clipPools.isEmpty()) {
        for (ClipPool clipPool : clipPools) {
            crawlerProxyList.add(new CrawlerProxy(clipPool));
        }
    }
    return crawlerProxyList;
}
```

画面12：
```java
public void unavailableProxy(CrawlerProxy crawlerProxy) {
    if (crawlerProxy != null) {
        crawlerIpPoolService.unavailableProxy(crawlerProxy);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
标题：1 爬虫系统完善
子标题：1.1 增加代理下载
内容：展示CrawlerConfig类的代码，包括@Autowired、@Bean注解和代理提供者配置。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

