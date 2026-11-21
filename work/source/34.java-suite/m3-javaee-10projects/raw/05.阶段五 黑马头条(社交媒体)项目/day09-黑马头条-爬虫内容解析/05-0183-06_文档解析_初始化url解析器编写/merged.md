# 06_文档解析_初始化url解析器编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\06_文档解析_初始化url解析器编写【海量资源尽在 666java.com】.mp4
- 时长 4分54秒（音频 294s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那刚才呢咱们是把当前这个负类啊抽取的这个抽象的负类给写完了下面咱们就来分别去写它的什么子类MPL它子类呢是有三个啊为什么会有三个呢我们先写第一个一会咱们再去解释好吧第一个叫啥呢叫ColorColorInitPage就是Processor这是一个类
[00:31] 让它去继承当前的图像类拷贝过来吧好吧长了跑过来跑下包这时候咱们需要去实验方法就是这四个没问题先把这四个给加上就可以了它是一个compound让Spring去管理它加完之后咱们最核心的方法其实就是中间的这个中间这个这三个咱们一会再写好吧
[01:03] 先把这个给写出来然后这时候这里边是有一个配置对象刚才说这个配置对象呢就是啥就是当前的这种外部Matic的一个对象那这时候呢咱们需要用到不是要初始化你看这名字就是初始化当前的页面是吧说页面啊这时候咱们需要拿到值这个值呢我们需要去输入一个东西就是要caller
[01:32] 然后是config property就是这个咱们在之前config中其实已经让sprint去管理了咱们也去干嘛也去往里边去设值了所以说你直接往里边去拿值就可以了啊拿哪个呢init color url list咱们首先拿的东西当然这个咱们这个不拿这个啊不拿这个咱们应该是拿的这个东西是解析的url解析的url怎么去解析
[02:00] 拿到它之后其实这个就是一个unit s pass好拿到它之后下面咱们就可以去用对子.r get html然后再一发请求咱们有一个s passs pass其实就是当前的这个s pass获取ur的s pass然后下面是link 4.0
[02:31] 但是啊就这代码是固定的咱们以后再去写的时候只是去不同的路径去请求不同的url这个你要知道吧最终他返回的呢他返回的呢其实就是helper的url啊helperurl哎然后要干嘛呢啊因为呢咱们要通过这个路径啊通过这个路径呢去获取的其实是具体的url去具体的什么
[03:01] Helper就是用户空间的一网然后呢这时候呢咱们就可以去交由下一级去处理我们可以调用ad这个方法这个方法一个呢就是前的Helper list第二个呢就是刚写那个request.getrequest然后第三个呢类似这个东西咱们要去交给下一级去处理下一级呢写下就下集啊咱们现在出实话下一级在哪
[03:31] 下一集是不是到空间了是吧document type是什么呢help那这个咱们就算是设置完了那这个设置完之后咱们下面咱们再去写下面的方法那下面的方法该怎么去写呢首先第一个咱们直接去返回当前这个类型就可以了直接还是用当前的caller numeral
[04:01] handletype.nim.forword.nim直接去.ecoshandletype就可以了判断到底是否是一样的因为是ecos行 这是一个下面这个是类似的这个并不是handletype是alcument type
[04:30] 这个也不是当前的forword这个是叫initinitname.ecos这个是documental ok这样就设置完了当然这个还有一个优先级是吧咱们可以暂时给一个100当前的这个东西就是故事化的解析咱们就写到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现一个继承自 AbstractCrawlerPageProcessor 的爬虫页面处理器，用于处理页面并提取链接。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 AbstractCrawlerPageProcessor 抽象类的源码，包含 handlePage、isHandleType、isHandleDocumentType 等抽象方法。
画面 2: 在 IDE 中创建 CrawlerInitPageProcessor.java 文件，准备编写具体实现。
画面 3: 编写 CrawlerInitPageProcessor 类，继承 AbstractCrawlerPageProcessor，并重写 handlePage 方法。
画面 4: 在 handlePage 方法中，使用 Ctrl+Shift+Space 自动补全，选择 org.Elasticsearch.common.recycler.Recycler 类。
画面 5: 在 handlePage 方法中，使用 @Autowired 注解注入 CrawlerConfigProperty。
画面 6: 在 handlePage 方法中，使用 Ctrl+Shift+Space 自动补全，选择 Page 类的 getHtml 方法。
画面 7: 在 handlePage 方法中，调用 page.getHtml().xpath() 方法提取 HTML 内容。
画面 8: 在 handlePage 方法中，使用 Ctrl+Shift+Space 自动补全，选择 addSpiderRequest 方法。
画面 9: 在 handlePage 方法中，调用 addSpiderRequestHelper.page.getRequest() 方法。
画面 10: 在 handlePage 方法中，使用 Ctrl+Shift+Space 自动补全，选择 CrawlerItem 的 DocumentType 枚举。
画面 11: 在 handlePage 方法中，调用 addSpiderRequestHelper.page.getRequest() 方法，并传入 CrawlerItem.DocumentType.HELP。
画面 12: 在 handlePage 方法中，使用 Ctrl+Shift+Space 自动补全，选择 crawlerFrom.HandleType 枚举。
画面 13: 在 handlePage 方法中，编写 isHandleType 方法，返回 crawlerFrom.HandleType.FORWARD.name().equals(handleType)。
画面 14: 在 handlePage 方法中，完成 isHandleType 方法的编写。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public abstract void handlePage(Page page);
// 是否需要处理类型
@Param handleType
@return

public abstract boolean isHandleType(String handleType);

// 是否需要文档类型
@Param documentType
@return

public abstract boolean isHandleDocumentType(String documentType);
```

画面 2:
```java
package com.heima.crawler.process.processor.impl;
```

画面 3:
```java
import com.heima.crawler.process.processor.AbstractCrawlerPageProcessor;
import org.springframework.stereotype.Component;
import us.codecraft.wolmigc.Page;

@Component
public class CrawlerInitPageProcessor extends AbstractCrawlerPageProcessor {
    @Override
    public void handlePage(Page page) {

    }
    @Override
    public boolean isHandleType(String handleType) {
        return false;
    }
    @Override
    public boolean isHandleDocumentType(String documentType) {
        return false;
    }
}
```

画面 4:
```java
import org.Elasticsearch.common.recycler.Recycler;
```

画面 5:
```java
@Autowired
private CrawlerConfigProperty crawlerConfigProperty;
```

画面 6:
```java
page.getHtml().xpath()
```

画面 7:
```java
String initPath = crawlerConfigProperty.getInitCrawlerPath();
List<String> helpList = page.getHtml().xpath(initPath).links().all();
addSpiderRequestHelper.page.getRequest();
```

画面 8:
```java
addSpiderRequest(List<String> urlList, Request request, DocumentType documentType) void
```

画面 9:
```java
addSpiderRequestHelper.page.getRequest()
```

画面 10:
```java
CrawlerItem.DocumentType.HELP
```

画面 11:
```java
addSpiderRequestHelper.page.getRequest(), CrawlerItem.DocumentType.HELP
```

画面 12:
```java
crawlerFrom.HandleType.FORWARD.name().equals(handleType)
```

画面 13:
```java
return crawlerFrom.HandleType.FORWARD.name().equals(handleType);
```

画面 14:
```java
return crawlerFrom.HandleType.FORWARD.name().equals(handleType);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

