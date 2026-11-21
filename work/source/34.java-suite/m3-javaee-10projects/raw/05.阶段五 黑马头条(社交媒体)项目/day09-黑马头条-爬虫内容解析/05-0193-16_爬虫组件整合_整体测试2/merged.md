# 16_爬虫组件整合_整体测试2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\16_爬虫组件整合_整体测试2【海量资源尽在 666java.com】.mp4
- 时长 4分13秒（音频 253s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢咱们是把功能给测了然后呢还有同学说啊这一个可能这个流程还是不太清晰那咱们呢再再去分析一下当前咱们写的代码的流程好吧简单去说一下大概呢大家去理解一下好吧行那咱们入口啊入口的话就是当前这个类是吧你首先是调用的测试是有一个handle然后你可以点进去啊我现在所有的都关了啊一个点进去你之后呢他会去调一个start task到这
[00:30] 这之后呢这之后啊你看啊他会去调一个handle叫handle啊其实handle里边刚才说了其实只有一个handle有一个orange data的handle呢里边是有这种内容的啊比如说方法是有内容的其他都是空的啊他只是在这去初始化了一个URL咱们目前的话只有一个扎网啊只有一个扎网行那这个设完之后啊设完之后呢其实他又去调了一个spiderspider start
[01:00] 就是开启了当前的这种webmatic的一个启动就是任务调度就这个你要是不熟的话你应该先去了解或者先去看一下学习一下当前webmatic的一些流程你也可以到官网上去看一下行那这个里边它这个它就会去调用当前四个组件哪四个组件你看其实就是咱们之前装入的这四个组件装入的看到了吗你看比如说有一个
[01:30] 配置processor是吧还有什么呢当前的scanner当然这个没有是吧还有download咱们这个有OK这个还有什么还有一个paypal那这个也没有是吧这个也没有什么后期都会去加上后期都会加上它目前的话比较熟的应该就是当前配置processor这个下载的话其实都是咱们自己已经封装好的都是通过http client或者是说CNNIM这种这种call run都可以去下载
[01:55] 咱们重点还是去翻一下这东西到底是怎么解析的怎么就到了什么处理化的然后一会到这个又到这个又到这个为什么会到这个是吧咱们可以再简单去说一说好咱们你看你们可以点一下这个类这个类里边其实它有很多实现类是吧就是咱们自己实现的实现类叫overstrike-color-page-processor点一下这里边你看这里边它就会去执行当前这个process
[02:26] 那process去干嘛了呢process去执行了handle那handle是谁呢其实这个呢是一个管理器是一个管理器就是它最后写在管理器啊那管理器里边你看啊管理器里边首先呢会去获取两个类型然后呢然后呢是去执行了handle配置看到了吧它就会去执行handle配置那这时候这个handle配置因为像管理类里边它去有三个类
[02:55] 分别是init,hp和doc那你说为什么要去先指引它后指引它再指引它呢其实咱们之前说过是不是在这去说了一个算法应该不是算法应该要优先级所以说咱们在这先去排了一个序所以说它就会按照这个顺序执行比如说它去现在优先级高的肯定是先去执行这时候你去设置的时候你看这个选项级是100这个选项级是110这个是120
[03:24] 是吧所以说呢110肯定是要干嘛肯定是先去执行肯定先去执行所以说呢他就会先去执行当前这个初始化然后呢再去解析他的个人空间就是Helper Page Processor最后呢才会去执行目标最后才会执行这个钻点还没去是吗我放行走了停了吧
[03:48] 好最后呢才会去执行这个目标好吧行啊那这个流程呢大家呢可以再去理解一下好吧主要呢主要的话就是咱们有一个这种模板方法还有一个责任链的模式啊自己去抽取了一下大家呢在代码呢要能看得明白让人看得明白啊如果说后期你要是在真正项目中去用到的话可能感觉会高大上一些好吧行那这个呢咱们就说到这里啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个爬虫框架中页面处理器（PageProcessor）的初始化、配置、执行流程及优先级排序机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 `ProcessingFlowManagerTest` 中启动爬虫的代码，调用 `crawlerConfig.getSpider().start()`。
画面2：展示 `AbstractOriginalDataProcess` 类中的 `handle` 方法，用于初始化数据列表并校验有效性。
画面3：展示 `ProcessingFlowManager` 类中的 `initSpider` 方法，用于初始化爬虫组件（PageProcessor、Scheduler、Downloader、Pipeline）。
画面4：展示 `initSpider` 方法的完整逻辑，包括设置组件和添加管道。
画面5：展示在 `initSpider` 方法中，通过 `getComponent` 方法选择具体的 `PageProcessor` 实现类。
画面6：展示 `AbstractCrawlerPageProcessor` 类中的 `process` 方法，用于处理页面并记录处理时间。
画面7：展示 `CrawlerPageProcessorManager` 类中的 `handle` 方法，用于根据页面类型分发处理。
画面8：展示在 `handle` 方法中，通过 `chooseImplementation` 选择具体的 `PageProcessor` 实现类。
画面9：展示 `AbstractCrawlerPageProcessorList` 类中的 `sort` 方法，用于对处理流程按优先级排序。
画面10：展示 `CrawlerConfigProperty` 类中的 `handle` 方法，用于处理页面的 `handleType` 和 `documentType`。
画面11：展示 `CrawlerPageProcessor` 类中的 `isNeedHandleType` 和 `isNeedDocumentType` 方法。
画面12：展示 `CrawlerPageProcessor` 类中的 `getPriority` 方法，返回优先级值 100。
画面13：展示 `CrawlerPageProcessor` 类中的 `targetParseRuleList` 处理逻辑，用于解析目标数据。
画面14：展示测试用例执行完成，控制台输出测试通过信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
ProcessFlowData processFlowData = new ProcessFlowData();
processFlowData.setHandleType(handleType);
processFlowData.setTargetUrlList(targetUrlList);
for (ProcessFlow processFlow : processFlowList) {
    processFlow.handle(processFlowData);
}
crawlerConfig.getSpider().start();
```

画面2：
```java
//初始化原始数据列表
List<ParseData> initialDataList = processFlowData.getParseDataList();
if (null != initialDataList && initialDataList.isEmpty()) {
    log.info("“初始化URL列表完成，有效URL数量：0”，initialDataList.size());
    initialDataList.add(null);
} else {
    log.error("“没有有效的初始化URL列表”");
}
```

画面3：
```java
private Spider initSpider() {
    Spider spider = null;
    CrawlerComponent component = getComponent(processFlowList);
    if (null != component) {
        PageProcessor pageProcessor = component.getPageProcessor();
        if (pageProcessor != null) {
            spider = Spider.create(pageProcessor);
            if (null != spider && null != component.getScheduler()) {
                spider.setScheduler(component.getScheduler());
            }
            if (null != spider && null != component.getDownloader()) {
                spider.setDownloader(component.getDownloader());
            }
            List<Pipeline> pipelineList = component.getPipelineList();
            if (null != spider && null != pipelineList && !pipelineList.isEmpty()) {
                for (Pipeline pipeline : pipelineList) {
                    spider.addPipeline(pipeline);
                }
            }
        }
    }
    return spider;
}
```

画面4：
```java
private Spider initSpider() {
    Spider spider = null;
    CrawlerComponent component = getComponent(processFlowList);
    if (null != component) {
        PageProcessor pageProcessor = component.getPageProcessor();
        if (pageProcessor != null) {
            spider = Spider.create(pageProcessor);
            if (null != spider && null != component.getScheduler()) {
                spider.setScheduler(component.getScheduler());
            }
            if (null != spider && null != component.getDownloader()) {
                spider.setDownloader(component.getDownloader());
            }
            List<Pipeline> pipelineList = component.getPipelineList();
            if (null != spider && null != pipelineList && !pipelineList.isEmpty()) {
                for (Pipeline pipeline : pipelineList) {
                    spider.addPipeline(pipeline);
                }
            }
        }
    }
    return spider;
}
```

画面5：
```java
PageProcessor pageProcessor = component.getPageProcessor();
```

画面6：
```java
@Override
public long process(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("“开始解析数据页面，url：{}，handleType：{}”，page.getRequest().getUrl(), handleType);
    crawlerPageProcessorManager.handle(page);
    log.info("“解析数据页面完成，url：{}，handleType：{}”，page.getRequest().getUrl(), handleType);
    return System.currentTimeMillis() - currentTimeMillis;
}
```

画面7：
```java
public void handle(Page page) {
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    for (AbstractCrawlerPageProcessor abstractCrawlerPageProcessor : abstractCrawlerPageProcessorList) {
        boolean needHandleType = abstractCrawlerPageProcessor.isNeedHandleType(handleType);
        boolean needDocumentType = abstractCrawlerPageProcessor.isNeedDocumentType(documentType);
        if (needHandleType && needDocumentType) {
            abstractCrawlerPageProcessor.handlePage(page);
        }
    }
}
```

画面8：
```java
public void handle(Page page) {
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    for (AbstractCrawlerPageProcessor abstractCrawlerPageProcessor : abstractCrawlerPageProcessorList) {
        boolean needHandleType = abstractCrawlerPageProcessor.isNeedHandleType(handleType);
        boolean needDocumentType = abstractCrawlerPageProcessor.isNeedDocumentType(documentType);
        if (needHandleType && needDocumentType) {
            abstractCrawlerPageProcessor.handlePage(page);
        }
    }
}
```

画面9：
```java
@Override
public int compare(ProcessFlow o1, ProcessFlow o2) {
    if (o1.getPriority() > o2.getPriority()) {
        return 1;
    } else if (o1.getPriority() < o2.getPriority()) {
        return -1;
    }
    return 0;
}
```

画面10：
```java
@Override
public void handle(Page page) {
    String helpUrl = crawlerConfigProperty.getInitCrawlerXPath();
    List<String> helpList = page.getHtml().xpath(helpUrl).all();
    addSpiderRequest(helpList, page.getRequest(), CrawlerEnum.DocumentType.HELP);
}
```

画面11：
```java
@Override
public boolean isNeedHandleType(String handleType) {
    return CrawlerEnum.HandleType.FORWARD.name().equals(handleType);
}

@Override
public boolean isNeedDocumentType(String documentType) {
    return CrawlerEnum.DocumentType.INIT.name().equals(documentType);
}
```

画面12：
```java
@Override
public int getPriority() {
    return 100;
}
```

画面13：
```java
List<ParseRule> targetParseRuleList = crawlerConfigProperty.getTargetParseRuleList();
if (null != targetParseRuleList && !targetParseRuleList.isEmpty()) {
    for (ParseRule parseRule : targetParseRuleList) {
        log.info("“添加数据字段到page中的field，url：{}，handleType：{}，field：{}”，page.getRequest().getUrl(), handleType, parseRule.getField());
        page.putField(parseRule.getField(), parseRule.getLargeContent());
    }
}
```

画面14：
```text
Process finished with exit code -1
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

