# 10_文档解析_目标页解析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\10_文档解析_目标页解析【海量资源尽在 666java.com】.mp4
- 时长 9分54秒（音频 595s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续啊下面呢咱们就来去说一下这个模板文档的解析啊这是应该是关于文档解析的最后一个这种啊算是类啊那这类呢咱们还是要再去重新定义一下啊咱们先去写一下啊是在当前的这个安排中然后是创建一个类然后这个类呢还是跟之前的是一样你需要去继承当前的什么他考虑一下他吧好吧好考完之后呢咱们打
[00:30] 是实现方法这方法还是有四个是吧是咱们的核心处理的方法下面还有两个是吧这两个其实咱们不用再去写了直接去设置就可以了那这个怎么写啊直接写的就是咱们是enumer是吧不是enumer叫colorcolor enumer.handletype.getforwardforward点什么呢name然后呢是点什么呢ecos
[01:01] 不是end with, 谁呀好这是一个这个呢这个其实跟上面差不多是吧, dollar enumerate.dll这是document type, 这是什么呢, 前面的是哪一块前面的话应该是前面的page, 是不是page啊page.name.eco好这是document
[01:33] 还有一个啊下面还有一个叫是是优先级是吧我们设置一个120因为刚之前是设置过百百一和二和一百二啊这是一百二这是一个优先级是靠后的啊当然这个优先级呢咱们一会呢会去单独去排序啊当然排序的时候越小的值呢咱们可以让让他呢排到前边目前这个就是排到最前边然后这是其次啊最后是当前这个doc好吧
[02:01] 行那这个设置完之后啊那么下面呢就来去写一下当前的核心的代码啊我们在这去加一个comp1然后再去加一个log4j2啊后呢咱们需要去注入一些东西啊注入哪个呢首先呢咱们要去做colorconfig property然后这里边咱们有一些属性咱们还是要拿到的啊然后呢嗯诸啊下面还要再注入另外一个叫什么叫colorcolor
[02:35] 这个hyper也需要啊行拿了之后呢咱们也去注入做完之后呢下面呢咱们就来去写这个逻辑这个逻辑呢其实还是写个注释也行啊就是这样呢复理页面数据页面数据啊那还是跟之前的是一样啊首先呢咱们还是要拿到当前的一个时间好就是记录一下时间啊好下面呢咱们可以去拿到它的类型咱们也可以去记录一下它的类型
[03:05] 什么, caller helper, get, handle type谁呀, h.get request行,这个呢就是handle type然后呢咱们下面呢就可以去设置log.info我给你写句话啊开始解析目标依然数据URL是谁呢是一个啊然后第二个呢,第二个是handle type
[03:40] handle type 冒号口号好吧这是第一个就是谁呀是配置点get url这是一个啊然后第二个呢就是handle下面呢咱们就可以去获取它的抓取规则因为呢最终呢咱们是要获取目标页其实目标页刚才说了就是这个一面是吧那你获取目标页的数据或者说咱们要抓取规则怎么办呢就是获取目标第二个抓取规则
[04:11] 规则这边还是得用当前这个属性点erget这个get应该是一个集合叫target pass ruler这个集合这个呢其实就是当前的规则拿到规则之后啊这时候呢咱们首先呢得去验证一下这个规则的这种有效性就是抽取有效的数据
[04:43] 这个其实咱们有一个工具类叫passrulerutils有一个叫做pass那参数第一个是配置.html第二个其实就是当前的这个ruler拿到它之后是rules
[05:13] 当然这个呢你可以重新给它复样值也行啊怎么就不会再用再去重新去定义一个什么呢一个变量了啊好下面呢咱们就可以去做循环了啊做循环之前呢还是在干嘛呢哎还是得去做一个那啊如果说那不等于目前的target bus ruler list并且呢并且非是吧还是这个啊target bus ruler list is empty说它不为空
[05:44] 它不会空的话呢外面呢咱们就可以往当前配置中去加速自断这里边呢因为它有多个是吧每一个像每一个类别里边是不是都有多个自断呢你可以点进去看一看啊点进去是不是自断呢还有当前的一个内容啊咱们都要去放到哪啊放到哪都要放到咱们的这个配置里边啊好咱们往下写啊那这个时候往下写的时候呢就是比较容易啊你可以直接这么写
[06:15] 做一个循环第一个就是 passRuler冒号就是 target.rulerlist然后这时候就可以去 变成 .rfueled然后第一个值就是 passRuler.getFueled第二个的话其实你要去换值了叫 passRuler.
[06:45] at一个mod content就是当前的一个内容好吧行那这个设置完之后咱们呢也可以在这啊在上面去加一个什么呢加一个注释好吧注释之后咱们也可以打印个日志啊将数据干嘛呢将数据啊将数据添加到配置中那配置交给谁啊交给后续的peoplepickling那这个呢其实就是一个
[07:22] 外包magic的一个处理流程现在咱们解析完解析完之后后面是应该他交由他去进行干嘛保存在保存之前咱们其实还有些事咱们一会再说好吧那这个咱们先去先去处理到这一步然后咱们下面刚才说了咱们在这去加一个什么loginfo去记录一个日志那点啥呢说添加数据字段field配置的field
[07:55] 配置中的field好然后这个field呢是咱们可以是url是啥一个啊url是啥然后第二个呢咱们有一个handle typeyp啊好第三个呢咱们可以去设立一个field是谁目号好好第一个参数就是page.at.url是吧然后第二个呢是handle type第三个呢
[08:32] 第三个的话就是前面的什么可以这么写叫passcooler.getfield这个咱们就设置完了可以看一下这个设置完之后最后咱们可以干嘛可以在这下面可以再去打进去你到底是花了多长时间咱们也可以在这去设置loginfo不要烦这东西咱们在实际开发的时候
[09:00] 像这些日志呢咱们还是记录还是挺多的啊所以说呢大家呢一定要是耐心去写解析目标year数据完成然后下面的是url啊然后是码号咱们也可以从上面拷过来啊比如说是handle啥啥好最后一个呢是号时号时是多少然后说姐妹还是配着点get url然后是handle type然后第三个呢
[09:38] 是system.orbit.com.mavis.mavis.是吧点去谁呀是吧那这个我们就算是设置完了啊那这个类啊咱们也设置完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在爬虫项目中实现一个处理文档页面的处理器，包括配置解析规则、处理页面数据并提取字段。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1: 展示项目结构，聚焦于 `CrawlerDocPageProcessor.java` 文件，其中定义了 `@Component` 注解的类，继承自 `AbstractCrawlerPageProcessor`，并声明了 `@Autowired` 的 `CrawlerConfigProperty` 和 `CrawlerHelper` 字段。
画面2: 展示 `CrawlerDocPageProcessor` 类中 `isHandledType` 方法的实现，返回 `false`。
画面3: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `isHandledType` 方法的调用。
画面4: 展示 `CrawlerDocPageProcessor` 类中 `getPriority` 方法的实现，返回 `10`。
画面5: 展示 `CrawlerDocPageProcessor` 类中 `@Component` 注解的定义，以及 `@Autowired` 注解的使用。
画面6: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `crawlerHelper` 的调用。
画面7: 展示 CSDN 网站上一篇关于 Java 数组知识的文章，内容涉及数组的定义、初始化和遍历。
画面8: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `crawlerConfigProperty.getTargetParseRuleList()` 的调用。
画面9: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `targetParseRuleList` 的初始化和 `if (null != targetParseRuleList && !targetParseRuleList.isEmpty())` 的条件判断。
画面10: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `for (ParseRule parseRule : targetParseRuleList)` 的循环。
画面11: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `page.putField(parseRule.getField(), parseRule.getContent());` 的代码。
画面12: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `log.info("添加数据字段到page中的field,url: {},handleType: {},field: {},content: {}", url, handleType, field, content);` 的日志输出。
画面13: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `log.info("添加数据字段到page中的field,url: {},handleType: {},field: {},content: {}", url, handleType, field, content);` 的日志输出。
画面14: 展示 `CrawlerDocPageProcessor` 类中 `handlePage` 方法的实现，其中包含 `log.info("添加数据字段到page中的field,url: {},handleType: {},field: {},content: {}", url, handleType, field, content);` 的日志输出。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1:
```java
package com.heima.crawler.process.processor.impl;
import com.heima.crawler.helper.CrawlerHelper;
import com.heima.crawler.process.entity.CrawlerConfigProperty;
import com.heima.crawler.process.processor.AbstractCrawlerPageProcessor;
import lombok.extern.log4j.Log4j2;
import org.springframework.stereotype.Component;
import org.springframework.beans.factory.annotation.Autowired;
import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.selector.Html;
import java.util.ArrayList;
import java.util.List;
@Component
public class CrawlerHelpPageProcessor extends AbstractCrawlerPageProcessor {
    @Autowired
    private CrawlerConfigProperty crawlerConfigProperty;
    @Autowired
    private CrawlerHelper crawlerHelper;
```

画面2:
```java
@Override
public boolean isHandledType(String documentType) {
    return false;
}
```

画面3:
```java
@Override
public void handlePage(Page page) {
}
@Override
public boolean isHandledType(String handleType) {
    return CrawlerEnum.HandleType.FORWARD.name().equals(handleType);
}
@Override
public boolean isHandledDocumentType(String documentType) {
    return false;
}
```

画面4:
```java
@Override
public int getPriority() {
    return 10;
}
```

画面5:
```java
import lombok.extern.log4j.Log4j2;
import org.springframework.stereotype.Component;
@Component
public class CrawlerDocPageProcessor extends AbstractCrawlerPageProcessor {
```

画面6:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handleType);
}
@Override
public boolean isHandledType(String handleType) {
    return CrawlerEnum.HandleType.FORWARD.name().equals(handleType);
}
```

画面8:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handleType);
    List<ParseRule> targetParseRuleList = crawlerConfigProperty.getTargetParseRuleList();
    targetParseRuleList = ParseRuleUtils.parseHtmlRuleList(targetParseRuleList);
```

画面9:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handleType);
    List<ParseRule> targetParseRuleList = crawlerConfigProperty.getTargetParseRuleList();
    targetParseRuleList = ParseRuleUtils.parseHtmlRuleList(targetParseRuleList);
    if (null != targetParseRuleList && !targetParseRuleList.isEmpty()) {
```

画面10:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handleType);
    List<ParseRule> targetParseRuleList = crawlerConfigProperty.getTargetParseRuleList();
    targetParseRuleList = ParseRuleUtils.parseHtmlRuleList(targetParseRuleList);
    if (null != targetParseRuleList && !targetParseRuleList.isEmpty()) {
        for (ParseRule parseRule : targetParseRuleList) {
```

画面11:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handleType);
    List<ParseRule> targetParseRuleList = crawlerConfigProperty.getTargetParseRuleList();
    targetParseRuleList = ParseRuleUtils.parseHtmlRuleList(targetParseRuleList);
    if (null != targetParseRuleList && !targetParseRuleList.isEmpty()) {
        for (ParseRule parseRule : targetParseRuleList) {
            page.putField(parseRule.getField(), parseRule.getContent());
        }
    }
}
```

画面12:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handleType);
    List<ParseRule> targetParseRuleList = crawlerConfigProperty.getTargetParseRuleList();
    targetParseRuleList = ParseRuleUtils.parseHtmlRuleList(targetParseRuleList);
    if (null != targetParseRuleList && !targetParseRuleList.isEmpty()) {
        for (ParseRule parseRule : targetParseRuleList) {
            log.info("添加数据字段到page中的field,url: {},handleType: {},field: {},content: {}", url, handleType, parseRule.getField(), parseRule.getContent());
            page.putField(parseRule.getField(), parseRule.getContent());
        }
    }
}
```

画面13:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handleType);
    List<ParseRule> targetParseRuleList = crawlerConfigProperty.getTargetParseRuleList();
    targetParseRuleList = ParseRuleUtils.parseHtmlRuleList(targetParseRuleList);
    if (null != targetParseRuleList && !targetParseRuleList.isEmpty()) {
        for (ParseRule parseRule : targetParseRuleList) {
            log.info("添加数据字段到page中的field,url: {},handleType: {},field: {},content: {}", url, handleType, parseRule.getField(), parseRule.getContent());
            page.putField(parseRule.getField(), parseRule.getContent());
        }
    }
}
```

画面14:
```java
@Override
public void handlePage(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析目标页, url: {}, handleType: {}", url, handle

