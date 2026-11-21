# 画面线理解：10_爬虫系统初始化_初始化URL的获取1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\10_爬虫系统初始化_初始化URL的获取1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 02:00, 02:29, 03:04, 03:24, 03:45, 04:13, 04:46, 05:25, 05:52, 06:11, 06:50, 07:29, 08:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:34:45

1) 这一组画面整体在讲如何通过 Spring Boot 的 @ConfigurationProperties 注解，从配置文件 crawler.properties 中读取 URL 前缀和后缀，并编写 Java 方法将它们组合成一个 URL 列表。

2) 按时间顺序列出每张画面的要点：
画面1：显示 CSDN 网站的“JavaScript 简介”页面，浏览器标签页中包含多个技术相关网站，如 CSDN、GitHub、PyCharm、IntelliJ IDEA 等，表明课程环境准备就绪。
画面2：IntelliJ IDEA 中打开项目 heima-leadnews-crawler，编辑器显示 crawler.properties 配置文件，其中包含 webdriver、proxy、crawler.init.url.prefix 等配置项。
画面3：在项目结构中选中 CrawlerConfig.java 文件，准备编写配置类。
画面4：在 crawler.properties 文件中，光标位于 crawler.init.url.prefix 配置项上，该配置项值为 https://www.csdn.net/nav/。
画面5：在 CrawlerConfig.java 中，使用 @ConfigurationProperties(prefix = "crawler.init.url") 注解，并定义 private String prefix 字段。
画面6：在 CrawlerConfig.java 中，添加 import org.springframework.boot.context.properties.ConfigurationProperties; 导入语句。
画面7：在 CrawlerConfig.java 中，添加 import org.springframework.context.annotation.Configuration; 导入语句。
画面8：在 CrawlerConfig.java 中，添加 import org.springframework.context.annotation.PropertySource; 导入语句。
画面9：在 CrawlerConfig.java 中，定义 private String suffix 字段，并注释说明其值为 /java, web, arch, do, mobile, ops, sec, cloud, engineering, iot, fund, career。
画面10：在 CrawlerConfig.java 中，编写 getInitCrawlerUrlList 方法，初始化一个 ArrayList，并将 suffix 字符串按分号分割。
画面11：在 CrawlerConfig.java 中，使用 String[] urlArray = suffix.split(";"); 将 suffix 按分号分割成数组。
画面12：在 CrawlerConfig.java 中，使用 if (urlArray != null && urlArray.length > 0) 判断数组是否非空。
画面13：在 CrawlerConfig.java 中，使用 for (int i = 0; i < urlArray.length; i++) 循环遍历数组。
画面14：在 CrawlerConfig.java 中，使用 if (StringUtils.isEmpty(urlArray[i])) 判断数组元素是否为空，并在非空时将 prefix + urlArray[i] 添加到初始化列表中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2 中的 crawler.properties 内容：
```
# windows
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
# linux
webdriver.chrome.driver=/usr/local/bin/chromedriver
proxy.get.url=http://www.89sp.cn/tqdl.html/api?l=linux&port=508&address=Bisp=
proxy.validate.url=http://www.89sp.cn/tqdl.html/api?l=linux&port=508&address=Bisp=
# 是否使用代理
proxy.isUsedProxy=true
proxy.comment.url=https://blog.csdn.net/author/Phoenix/comment/list/{id}/{page}/{size}
proxy.cookie.name=taoc_sc_v2
crawler.init.url.prefix=https://www.csdn.net/nav/
crawler.init.url.suffix=java,web,arch,do,mobile,ops,sec,cloud,engineering,iot,fund,career
crawler.help.nextPagingSize=10
# 1次更新时间
crawler.nextupdatehours=4,16,64,128,256
```

画面5 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class CrawlerConfig {

}
```

画面6 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

}
```

画面8 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:crawler.properties")
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

}
```

画面9 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:crawler.properties")
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

    private String prefix;
    private String suffix; //java, web, arch, do, mobile, ops, sec, cloud, engineering, iot, fund, career

}
```

画面10 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:crawler.properties")
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

    private String prefix;
    private String suffix; //java, web, arch, do, mobile, ops, sec, cloud, engineering, iot, fund, career

    public List<String> getInitCrawlerUrlList() {
        List<String> initCrawlerUrlList = new ArrayList<>();
        String[] urlArray = suffix.split(";");
        return initCrawlerUrlList;
    }
}
```

画面11 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:crawler.properties")
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

    private String prefix;
    private String suffix; //java, web, arch, do, mobile, ops, sec, cloud, engineering, iot, fund, career

    public List<String> getInitCrawlerUrlList() {
        List<String> initCrawlerUrlList = new ArrayList<>();
        String[] urlArray = suffix.split(";");
        if (urlArray != null && urlArray.length > 0) {
            for (int i = 0; i < urlArray.length; i++) {
                String url = urlArray[i];
                if (StringUtils.isEmpty(url)) {
                    continue;
                }
                initCrawlerUrlList.add(prefix + url);
            }
        }
        return initCrawlerUrlList;
    }
}
```

画面12 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:crawler.properties")
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

    private String prefix;
    private String suffix; //java, web, arch, do, mobile, ops, sec, cloud, engineering, iot, fund, career

    public List<String> getInitCrawlerUrlList() {
        List<String> initCrawlerUrlList = new ArrayList<>();
        String[] urlArray = suffix.split(";");
        if (urlArray != null && urlArray.length > 0) {
            for (int i = 0; i < urlArray.length; i++) {
                String url = urlArray[i];
                if (StringUtils.isEmpty(url)) {
                    continue;
                }
                initCrawlerUrlList.add(prefix + url);
            }
        }
        return initCrawlerUrlList;
    }
}
```

画面13 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:crawler.properties")
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

    private String prefix;
    private String suffix; //java, web, arch, do, mobile, ops, sec, cloud, engineering, iot, fund, career

    public List<String> getInitCrawlerUrlList() {
        List<String> initCrawlerUrlList = new ArrayList<>();
        String[] urlArray = suffix.split(";");
        if (urlArray != null && urlArray.length > 0) {
            for (int i = 0; i < urlArray.length; i++) {
                String url = urlArray[i];
                if (StringUtils.isEmpty(url)) {
                    continue;
                }
                initCrawlerUrlList.add(prefix + url);
            }
        }
        return initCrawlerUrlList;
    }
}
```

画面14 中的 CrawlerConfig.java 内容：
```java
package com.heima.crawler.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Configuration
@PropertySource("classpath:crawler.properties")
@ConfigurationProperties(prefix = "crawler.init.url")
public class CrawlerConfig {

    private String prefix;
