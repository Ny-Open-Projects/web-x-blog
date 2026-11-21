# 画面线理解：13_爬虫系统初始化_下载准备_工具类介绍1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\13_爬虫系统初始化_下载准备_工具类介绍1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:23, 01:53, 02:09, 03:01, 03:18, 04:16, 04:45, 05:09, 05:43, 05:52, 06:35, 06:47, 07:31, 08:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:36:50

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
