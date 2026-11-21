# 13_爬虫系统初始化_下载准备_工具类介绍1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\13_爬虫系统初始化_下载准备_工具类介绍1【海量资源尽在 666java.com】.mp4
- 时长 8分12秒（音频 493s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好下面咱们就继续往下讲刚才咱们是把这个初始化的URL去获取了一下测试了也没有问题下面咱们就来去讲下载这个下载呢其实咱们需要准备的工作有很多这时候呢咱们呢还是得先去详细的去说一下咱们之前的导入的这个工程里边到底有啥其实里边代码代码都提供了
[00:28] 但是这个下载的过程呢咱们业务啊一会儿会再去细讲咱们主要是细讲业务啊关键这个工具类这些工具类呢咱们都已经提供了下面呢咱们就来去说一下这些类的作用好咱们可以参考着这个讲义啊首先呢第一块啊咱们需要去设立一个cookie的name那为什么要设立cookie name呢就这样啊因为咱们要访问的网站呢是csdn那csdn呢它是有一个反爬虫的技术
[00:58] 这时候呢你去比如你下载了在sensei上去下载了一个页面这时候如果说它没有cookie的话那这时候呢它可能呢给你返回的并不是正常的数据所以说呢所以说呢咱们有时候啊可能呢需要去经常的去重置cookie那这cookie的名称是啥呢ok这cookie的名称是固定的就叫做acw-sc-v2这个名称呢咱们需要去配置一下
[01:28] 目前的话咱们都是配到当前的这个地儿找一找啊就这个地儿这个名称我再强调一下这个名称不能随意改不能改好吧这个就是必须叫这个名称因为咱们后期呢再去做判断的时候要通过这个名称去判断到底是否有cookie这个名称是固定的啊行那这个咱们就说到这然后再往下看还有一些什么类啊还有呢就是一个color policy
[01:59] 那这个类呢其实比较简单啊咱们可以拷贝一下啊这个是在一个modal类中modal类中的啊modal中的一个类算是一个实体类吧这个呢其实就两个属性啊一个是host第二个是port那这个很好理解第一个是当前的什么你的IP地址这个是你的端口号对吧并且这是在这设的一个构造方法然后下面还有一个就是getplotinfo其实呢就是当前的post加port
[02:28] 就是就是拼接了一下下面两方法其实无所谓一个是EQOS一个是Hashcode还有一个ToStream好吧行那这个设计力比较简单这个呢其实就是来构建代理什么代理呢就是来去构建咱们访问的或者要请求的一个方式这个就是你时不时用代理后期咱们还会再去说因为这个目前的话呢咱们可以默认使用请求的方式啊请求的方式使用HTTPClient
[02:57] http client行那这个咱们就这个实体列你知道一下就说这里边有两个属性一个是host一个是hot然后下一次下面再往下看这里边还有一个类需要大家知道哪个类就是当前那个color proxy factory这个类其实已经提供了可以打开看一看这个类其实也很好理解来看一看首先在这去设置了一个当前的什么电量是吧是no
[03:28] not use privacy就是我干嘛呢我不使用代理是吧不使用代理啊然后下面呢他呢是又去介绍了几种代理的方式代理的方式啊首先咱们发请求第一种呢就是用http client的代理啊这个构建的方式呢是比较简单的直接去new就可以了new完之后呢你需要把当前的端口号和啊house和端口号
[03:54] 传进去就可以了就是通过当前那个ColorProxy获取的就可以了OK这是HTTP Client其实呢咱们在后期去下载的时候默认首先先去使用当前的就是爬虫框架WebMatic爬虫框架默认使用的HTTP Client咱们先去用它去下载但是呢但是有可能啊下载不下来有可能下载不下来那下载不下来的时候呢咱们可能呢要去用第二种或者第三种
[04:24] 当前的这种代理第二种其实就是当前框架提供的当前框架提供的一种代理方式其实这个其实跟当前的house跟当前http client其实是一种因为当前webmatic框架默认就是使用的什么http client好这是一种然后再往下再往下的话是不太一样这个你看这有个selenium proxy
[04:51] 那这个呢其实就不太一样了这个其实就是用当前的什么Celine这个Proxy那这个呢什么时候用呢刚才咱们说的这个Cookie如果说你去更新的时候啊如果说你要是去访问的时候这个Cookie没有更新那这时候呢你可能得需要干嘛呢你可能得需要用当前那个Celine去发送请求用它去发送请求这样的话页面就可以去下载下来好吧
[05:20] 行那这个啊这里边有三种方式刚才也说到了啊然后再往下呢就是有一个获取当前的get什么plotinfo其实你再不使用再去不使用当前的这个代理的情况下呢咱们直接去获取到当前这个plotinfo就可以了其实就是直接获取的谁啊直接获取的就是当前这个方法好吧把它返回就可以了好吧行那这个咱们就这两个类啊咱们就说到这啊
[05:50] 咱们也可以往下看再往下看看看看还有没有其他的类这里边还有一个叫cookiecolor cookie这是一个实体类给搜一下这里边其实也很好理解这个类其实就是一个cookie的实体是吧实体你需要干嘛后期咱们需要去设置cookie的值当然这个操作其实是框架帮你做的你不用去设置但是你需要提供这么一个类
[06:20] 需要提供这么一个类啊这类呢其实就是包含了一些cookie的信息比如说你看啊当前的名称是吧值域名啊还有什么路径过期时间是否必须还有什么检查咱们的是否过期的一种方法是吧像这些呢这个类呢咱们需要去提供好吧行那这个啊这个呢咱们就说到这咱们再往下看看看看还有没有
[06:51] 好这呢是还有一个严实的回调接口啊咱们可以先读一下这段话说为了判断下载硬币是否成功因为SysGN的cookie登录啊验证是需要GS实现的呃所以说呢需要Clinium去下载硬币后等待一会检测cookie是否登录成功那这时候呢咱们其实呢就是有一个回调的方法回调的方法啊呃这里边呢delayeddelayeddelayed是吧
[07:20] 这里边一个callback其实一个接口是吧接口里边呢是有几个方法啊你看首先第一个是延时对应的方法叫callback延时对应的方法然后还有是咱们判断是否存在呀是是否每次啊或许每次失眠时间呢还有超时时间咱们都要去设置吧都要去呃可以去设置啊行那这是一个接口那这接口到底怎么用啊到底怎么用一会儿呢咱们去下载一面的时候呢其实用到了当前这个接口这个接口呢你也可以看一下啊
[07:50] 这个接口呢其实呢它没有任何实现它没有实现啊那怎么办呢没有实现的话其实呢咱们在真正写代码的时候呢咱们可以使用匿名内部类去完成具体的一些这种逻辑好吧行那这个类啊咱们就先介绍到这然后下面还有一些咱们一会再说好吧先把视频断一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解爬虫项目中代理对象的实现、工厂模式创建代理、以及延迟工具类的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示CrawlerConfig类，其中定义了prefix和suffix属性，并实现getInitCrawlerUrlList方法，用于根据URL后缀生成爬取URL列表。
画面2：展示文档中“6.2.1前置工作”部分，提及crawler.properties配置文件和CrawlerProxy实体类。
画面3：展示CrawlerProxy.java文件，定义了host和port私有属性，并实现getProxyInfo方法。
画面4：展示CrawlerProxy.java文件，定义了构造函数，用于初始化host和port。
画面5：展示CrawlerProxyFactory.java文件，定义了NOT_USB_PROXY常量和getHttpHostProxy静态方法。
画面6：展示CrawlerProxyFactory.java文件，实现getHttpHostProxy方法，创建HttpHost代理对象。
画面7：展示CrawlerProxyFactory.java文件，实现getWebmagicProxy方法，创建Webmagic代理对象。
画面8：展示crawler.properties配置文件，包含webdriver、proxy、csdn.comment.url等配置项。
画面9：展示CrawlerProxy.java文件，实现equals和hashCode方法，用于比较代理对象。
画面10：展示CrawlerProxyFactory.java文件，实现getSeleniumProxy方法，创建Selenium代理对象。
画面11：展示CrawlerCookie.java文件，定义了isExpired方法，用于判断Cookie是否过期。
画面12：展示CrawlerCookie.java文件，定义了getName、setName、getValue、setValue等方法，用于操作Cookie的属性。
画面13：展示文档中“延迟调用工具类”部分，提及DelayedUtils类。
画面14：展示DelayedUtils.java文件，定义了delayed方法，用于延迟执行回调。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Configuration
@PropertySources({"classpath:crawler.properties"})
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {
    private String prefix;
    private String suffix;

    public List<String> getInitCrawlerUrlList() {
        List<String> initCrawlerUrlList = new ArrayList<>();
        if (StringUtils.isNotBlank(suffix)) {
            String[] urlArray = suffix.split(regexp);
            if (urlArray != null && urlArray.length > 0) {
                for (int i = 0; i < urlArray.length; i++) {
                    if (StringUtils.isNotBlank(urlArray[i])) {
                        initCrawlerUrlList.add(prefix + urlArray[i]);
                    }
                }
            }
        }
        return initCrawlerUrlList;
    }
}
```

画面2：
```java
// 6.2.1 前置工作
crawler.properties
判断页面下载后是否需要进行下载操作
页面下载完成后，js代码写入到cookie，用来验证人或机构访问，csdn网站反爬虫的一种方式
crux.cookie.name=acw_sc_v2
```

画面3：
```java
/**
 * 代理实体类
 */
@Setter
@Getter
public class CrawlerProxy implements Serializable {
    public CrawlerProxy(String host, Integer port) {
        this.host = host;
        this.port = port;
    }
}
```

画面4：
```java
/**
 * 代理实体类
 */
@Setter
@Getter
public class CrawlerProxy implements Serializable {
    public CrawlerProxy(String host, Integer port) {
        this.host = host;
        this.port = port;
    }
    private String host;
    private Integer port
}
```

画面5：
```java
package com.heima.crawler_factory;

import ...

/**
 * 代理工厂
 */
public class CrawlerProxyFactory {
    /**
     * 不使用代理
     */
    private static final String NOT_USB_PROXY = "NOT_USB_PROXY";

    /**
     * 代理对象httpclient的代理
     * @param crawlerProxy
     * @return
     */
    public static HttpHost getHttpHostProxy(CrawlerProxy crawlerProxy) {
```

画面6：
```java
public static HttpHost getHttpHostProxy(CrawlerProxy crawlerProxy) {
    if (null != crawlerProxy && StringUtils.isNotBlank(crawlerProxy.getHost()) && null != crawlerProxy.getPort()) {
        return new HttpHost(crawlerProxy.getHost(), crawlerProxy.getPort());
    }
    return null;
}
```

画面7：
```java
public static us.codercraft.webmagic.proxy.Proxy getWebmagicProxy(CrawlerProxy crawlerProxy) {
    if (null != crawlerProxy && StringUtils.isNotBlank(crawlerProxy.getHost()) && null != crawlerProxy.getPort()) {
        return new us.codercraft.webmagic.proxy.Proxy(crawlerProxy.getHost(), crawlerProxy.getPort());
    }
    return null;
}
```

画面8：
```properties
# windows
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
# linux
webdriver.chrome.driver=/usr/local/bin/chromedriver
proxy.set.url=http://www.89ip.cn/tqdl.html?api=1&num=500&port=80&address=isp
proxy.validate.url=http://myip.kkcha.com/
# 是否使用代理
proxy.isUsedProxyIp=true
csdn.comment.url=https://blog.csdn.net/${author}/phoenix/comment/list/${id}/page=1&size=100&tree_type=2
crux.cookie.name=acw_sc_v2
crawler.init.url.prefix=https://www.csdn.net/nav/
crawler.init.url.suffix=java,web,arch,db,mobile,ops,sec,cloud,engineering,iot,fund,career
crawler.help.nextPagingSize=10
# 下次爬取时间
crawler.nextupdatehours=4,16,64,128,256
```

画面9：
```java
@Override
public boolean equals(Object o) {
    if (o == null) return true;
    if (o.getClass() != getClass()) return false;
    CrawlerProxy that = (CrawlerProxy) o;
    return host.equals(that.host) && port.equals(that.port);
}

@Override
public int hashCode() {
    return Objects.hash(host, port);
}
```

画面10：
```java
public static org.openqa.selenium.Proxy getSeleniumProxy(CrawlerProxy crawlerProxy) {
    if (null != crawlerProxy && StringUtils.isNotBlank(crawlerProxy.getHost()) && null != crawlerProxy.getPort()) {
        org.openqa.selenium.Proxy proxy = new org.openqa.selenium.Proxy();
        proxy.setProxyType(CrawlerProxy.getProxyType());
        return proxy;
    }
    return null;
}
```

画面11：
```java
private boolean isRequired;

/**
 * 校验是否过期
 */
public boolean isExpired() {
    boolean flag = false;
    if (null != expire) {
        flag = expire.getTime() <= (new Date()).getTime();
    }
    return flag;
}
```

画面12：
```java
public String getName() {
    return name;
}

public void setName(String name) {
    this.name = name;
}

public String getValue() {
    return value;
}

public void setValue(String value) {
    this.value = value;
}

public String getDomain() {
    return domain;
}

public void setDomain(String domain) {
    this.domain = domain;
}

public String getPath() {
    return path;
}

public void setPath(String path) {
    this.path = path;
}

public Date getExpire() {
    return expire;
}

public void setExpire(Date expire) {
    this.expire = expire;
}
```

画面13：
```java
/**
 * 延迟调用工具类
 */
public class DelayedUtils {
    public static void delayed(long delayedTime) {
        try {
            Thread.sleep(delayedTime);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

画面14：
```java
/**
 * 延迟调用工具类
 */
public class DelayedUtils {
    public static void delayed(long delayedTime) {
        try {
            Thread.sleep(delayedTime);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    /**
     * 延迟方法
     * @param callback
     */
    public static Object delayed(DelayedCallback callback) {
        long sleepTime = callback.sleepTime();
        Thread.sleep(sleepTime);
        return callback.callBack();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“6.2 下载”，子标题“6.2.1 前置工作”，内容包括“crawler.properties”和“CrawlerProxy”。
画面10：PPT标题为“6.2.1 前置工作”，子标题“获取Selenium Cookie”，内容包括“getSeleniumProxy”方法。
画面13：PPT标题为“延迟调用工具类”，内容包括“DelayedUtils”类。
画面14：PPT标题为“延迟调用工具类”，内容包括“DelayedUtils”类。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

