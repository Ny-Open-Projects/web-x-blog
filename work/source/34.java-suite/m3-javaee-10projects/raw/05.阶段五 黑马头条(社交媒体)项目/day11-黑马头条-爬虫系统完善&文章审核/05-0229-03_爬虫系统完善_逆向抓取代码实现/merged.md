# 03_爬虫系统完善_逆向抓取代码实现

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\03_爬虫系统完善_逆向抓取代码实现【海量资源尽在 666java.com】.mp4
- 时长 6分24秒（音频 384s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们就接着往下看下面咱们要去完成的是什么是逆向爬取文章的这种设置这个咱们主要是通过当前管理类Processing, Flow Manager当前这里边咱们要去设置什么逆向的爬虫的处理咱们之前都在这个方法里边去设置的是正向下面咱们就来去完成这段代码好吧代码在哪呢这个代码是在当前的Manager里边是不是有个他
[00:30] 在这你需要去添加方法添加方法其实最终他也是去调用这个只是参数是不太一样的好吧来咱们就在这去写一写public然后是 void然后咱们叫reversereverse handle好这里边咱们又去简单可以去描述一下什么叫逆向处理逆向处理那该怎么去写呢
[01:04] 首先你应该是先去获取已经存在的数据获取已经存在的数据这样的话因为这个逆向是二次抓取是不是二次抓取是的这时候你需要去注入一个什么注入一个当前的privateprivate有一个叫callercaller叫什么newsadditional因为最终咱们是要去当前的这种附加信息
[01:36] 完善是吧所以说你直接去注入当前这个信息就可以了好然后呢你就可以去使用里边的数据那叫用哪个方法呢里边有一个增量的增量的这种类增量的方法啊这个根据当前日期去查询增量的这种增量的文章信息增量的文章信息啊最终的就能去获取前的一个as item list
[02:04] 这样的话里边是有一些IP值的拿到它之后你就可以去干嘛你就可以去进行抓取了但是抓取的时候是这样应该不是抓取应该是要处理当前的这种里边包含的URL的逻辑是吧那行这里边咱们还需要去设置一个什么设置一个这种数据handle在这封装个方法handle reverse date
[02:36] 这个参数就是当前的passitemlist这个方法干嘛的好来我先创建出来这个方法主要就是主要就是来设置它的一个抓取的类型抓取的类型人们之前的默认其实都是正向这会你要去在抓取之前你要重新去把这个数据给重新设置下你要强调一下这东西是要逆向抓取好吧在这反向逆向
[03:09] 逆向同步数据这样啊我写的你看我写完你都知道了if non不等于什么passitemlist并且干嘛非passitemlist.isEmpty它不会空这时候呢你要去循环它这里边有很多是吧你一个一个的要去设置passitem.set一个咱们要设置ocomunitytype那是什么类型呢
[03:41] 它是一个callercallerEnumer.有一个documentType.有一个page这是一个page就是page你才能去解析数据所以说你就要设置为无能力行为page然后第二个呢asItem.set什么有一个叫做documentType对啊candleType是吧这边还是callerEnumer.有一个叫什么candleType是什么是reverse
[04:11] 不是HTML是handle点有一个reverse之前forward是正向reverse就是逆向比如说点那样的话我们就算是重新设了下这个值告诉他就是逆向去抓取的并且你要去抓取到某一个配置这样的话才能真正的去解析一面好吧行那这个设置完之后下面咱们就可以在这打一只log点
[04:42] 开始进行数据逆向更新增量数据数量为多少呢那里很简单啊这写个逗号然后是passitemlist.sys是吧那这个说完之后啊咱们下面的就可以去调用了啊说他咱们还是要去判断一下
[05:13] 不等于当前的passitemlist并且呢是它不等于空是吧tel is empty错了tel is empty然后呢下面就可以去调用stack taskok第一个指示呢就是当前的passitem这时候你要去告诉它你抓取的url是谁所以说你要把这个passitemlist装进去这个呢这个你要告诉它我的抓取的类型是啥url nummer点什么呢
[05:43] 有一个叫handle type.reverseok这样我们就设置完了加了一个并且这样的话就可以了然后的话咱们就在这去写一个吧dlse如果说他没值怎么办没值的话就提示一下怎么提示说数量数据未空不能进行数据更新好吧
[06:15] 那这样的话咱们就算是对完了这个测试的话其实也很简单是吧那这样咱们一会再去测试好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在爬虫系统中实现反向数据更新功能，包括配置代理、启动爬虫任务、处理反向数据列表并设置文档类型与处理类型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示CrawlerConfig类中定义的代理池服务注入和代理提供者配置，包含设置已使用代理IP和更新代理的回调方法。
画面2：展示ProcessingFlowManager类中startTask方法的实现，用于启动爬虫任务，传入参数列表和处理类型。
画面3：展示ProcessingFlowManager类中reverseHandle方法的定义，用于处理反向数据。
画面4：展示ProcessingFlowManager类中reverseHandle方法的实现，调用crawlerNewsAdditionalService查询增量数据。
画面5：展示ProcessingFlowManager类中reverseHandle方法的实现，调用crawlerNewsAdditionalService查询增量数据并处理。
画面6：展示ProcessingFlowManager类中handleReverseData方法的定义，用于处理反向数据列表。
画面7：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。
画面8：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。
画面9：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。
画面10：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。
画面11：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。
画面12：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。
画面13：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。
画面14：展示ProcessingFlowManager类中handleReverseData方法的实现，对parseItemList进行遍历并设置文档类型。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@AutoWired
private CrawlerIpPoolService crawlerIpPoolService;

@Bean
public CrawlerProxyProvider getCrawlerProxyProvider() {
    CrawlerProxyProvider crawlerProxyProvider = new CrawlerProxyProvider();
    crawlerProxyProvider.setUsedProxyIp(isUsedProxyIp());
    //使用代理池
    crawlerProxyProvider.setProxyProviderCallBack(new ProxyProviderCallBack() {
        @Override
        public List<CrawlerProxy> getProxyList() {
            return getCrawlerProxyList();
        }

        @Override
        public void unavailable(CrawlerProxy proxy) {
            unavailable(proxy);
        }
    });
    return crawlerProxyProvider;
}
```

画面2：
```java
public void startTask(List<ParseItem> parseItemList, CrawlerEnum HandleType handleType) {
    ProcessFlowData processData = new ProcessFlowData();
    processData.setHandleType(handleType);
    processData.setParseItemList(parseItemList);
    for (ProcessFlow processFlow : processFlowList) {
        processFlow.handle(processData);
    }
    crawlerConfig.getSpider().start();
}
```

画面3：
```java
public void reverseHandle() {
    //反向处理
}
```

画面4：
```java
@Autowired
private CrawlerNewsAdditionalService crawlerNewsAdditionalService;

public void reverseHandle() {
    //反向处理
}
```

画面5：
```java
public void reverseHandle() {
    List<ParseItem> parseItemList = crawlerNewsAdditionalService.queryIncrementParseItem(new Date());
    handsReversaData(parseItemList);
}
```

画面6：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    //反向处理
}
```

画面7：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

画面8：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

画面9：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

画面10：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

画面11：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

画面12：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

画面13：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

画面14：
```java
private void handleReverseData(List<ParseItem> parseItemList) {
    if (null != parseItemList && !parseItemList.isEmpty()) {
        for (ParseItem parseItem : parseItemList) {
            parseItem.setDocumentType(CrawlerEnum.DocumentType.PAGE.name());
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

