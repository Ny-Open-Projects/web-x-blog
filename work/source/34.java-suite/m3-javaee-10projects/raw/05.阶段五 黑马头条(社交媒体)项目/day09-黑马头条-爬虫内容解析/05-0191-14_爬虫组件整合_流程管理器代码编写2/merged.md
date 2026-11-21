# 14_爬虫组件整合_流程管理器代码编写2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\14_爬虫组件整合_流程管理器代码编写2【海量资源尽在 666java.com】.mp4
- 时长 8分16秒（音频 496s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续把这个方法给写完啊这个方法呢主要干嘛呢主要是来抓取抓取组件的封装封装啊写错了啊好下面呢咱们就来去封装一下当前这个对象就可以了啊这个对象是compound然后是等于new一个colorcompound然后呢大家在里边需要去封装哪些参数呢其实咱们在这获取的时候其实已经知道了咱们主要是封装几个四个
[00:32] 是吧,封装四个啊好来看一下嗯当然了这个那这个参数是怎么来的呢其实都是从当前这个集合中来的是吧咱们可以把它给循环一下啊那循环完之后呢咱们就可以去判断了啊然后判断的话然后不同的类型咱们要去设置不同的属性在这里边就可以了好吧那这个怎么去判断呢其实呢咱们在之前呢这个目前这个类里边其实有一个叫做get component type
[00:59] 然后如果说它等于color.num.compoundtype比如说processageprocessor它就是一个文档解析这时候你就可以去往当前compound.setageprocessor就把当前procesflow就可以了需要去转这是一个咱们可以往下写as if
[01:30] 咱们可以设置第二个啊这个其实差不多啊拨备一下前面不用改不用改啊咱们需要改后边的啊那是谁啊点比如说怎么叫paypal land好吧一样的啊然后呢这块你写的时候你要注意啊用这个paypal land它是有多条啊并不是一个所以说你在这去写的时候写什么这个我集合集合中去添加啊还是谁啊还是当年那个sysflow当然这个也要强转
[02:02] 好吧行那这样就可以了再往下如果说它等于谁咱们再去拷贝一个拷贝一个上面的东西再拷到这这个咱们看还有什么有一个download是吧download这时候你直接去往里边封装的时候就是set download就把当前这个placeflow可以强转一下这是一个还有一个scandlerr4就可以了
[02:35] 弄在else if里面还是一样还是得需要拷贝拿过来然后这个是叫做scandler好然后是compound.setscandler不是processflow,长转你把这个对象给返回就可以了return compound这个方法就解完了
[03:06] 那这个方法写完之后呢下面呢咱们可以再去写一个这种执行的方法public然后呢咱们可以去写一个voidstarttask这是干嘛的呢我们一路来说啊好我们在这儿去摆个都市那里边有参数啊有参数一个参数呢就是平行的一个这种r就是出入化的一个rpathpathalist好吧
[03:40] 第二个参数就是当前的到底是哪种类型Numer.handletype然后这个咱们就叫handletype好,咱们在这去写一个注释,删掉然后这个方法主要就是开始开始处理开始处理爬虫任务好吧,开始处理爬虫任务
[04:08] 这里边该怎么写呢其实你都应该通过当前一个 persist date persis date persis是吧c e s sfollow datefollow date咱们用一下它它是一个这种呼向类是吧等于用一个它用完它之后咱们就可以去到里边的方法但是你可以干嘛你可以先去先去设置它的这种类型是吧
[04:41] 先去设置类型叫 process.dat.set.handletype那就是handletype第二个咱们就可以去设置他的什么passet什么说错了passesflowdat.set.itemlist就是他的初始化的UR然后咱们就可以去执行他的这种handle方法这个方法咱们就可以去做循环了
[05:13] 这个循环到底是谁?
[05:15] 其实这个循环就是刚才注入的东西咱们还可以这么写process.flawless.for循环是它,咱们是循环这里边的一个叫做handle,它就是需要一个process.out好,这个设置完了
[05:44] 设置完之后,咱们还需要去再做一个事需要去config.com.jpg 里面有一个bat.spade当前的一个模统这样的话,咱们就设置完了为了方便测试,咱们可以在这去写一个方法这个方法主要是来处理什么呢?
[06:10] 处理咱们的一个这种像的
[06:13] 你看笔记里边其实这里边刚才我写的方法其实最后一个就是开始爬床的任务处理是吧但这里边是有一个异步还有一个逆向其实目前的话咱们指示啥呢指示正向逆向的话咱们先不讲咱们先去测一下这个正向OK咱们为了方便测试直接去写这么一个方法就可以叫handle好吧在下边写一下
[06:43] public void handle没有参数这个就是一个正向爬去你直接去调了一个方法就可以了第一个参数咱们可以传一个none因为这个参数其实不传也行为什么不传也行因为这里边
[07:14] 咱们去设置当前的那么多里边是有一个叫做Observate Orange Data Process里边它会执行handle这个方法handle方法里边其实已经把当前这个初始化的URL给初始化了初始化的URL已经加载了所以说你没有必要再去设置一遍所以说你直接传一个当然后第二个材数你可以去设置一个正向这个正向的话就比较简单了叫color.handletype.forward就完了
[07:44] forward就是逆向好吧目前这个代码就算是写完了当然别记中的里边还有一个逆向逆向里边为什么不写呢因为这里边还涉及到了一个当前的Service这个Service最终咱们会去存储是吧咱们也会去设置一些值但这个Service咱们并没有咱们先去测试测试完之后咱们下面就来去编写Service然后再去编写这个逆向好行拿这个方法拿这个
[08:12] 这个例咱们就暂时写在这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解爬虫框架中 ProcessingFlowManager 类如何根据配置列表初始化并组装 PageProcessor、Pipeline、Downloader 和 Scheduler 等组件，并启动爬虫任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 ProcessingFlowManager.java 文件中 getComponent 方法的初始部分，正在定义方法签名和创建 CrawlerComponent 实例。
画面 2：在 getComponent 方法中，遍历 processFlowList，判断第一个元素的类型并设置 PageProcessor。
画面 3：继续在 getComponent 方法中，判断 processFlow 的类型为 PIPELINE 时，调用 component.addPipeline 方法添加管道。
画面 4：在 getComponent 方法中，判断 processFlow 的类型为 DOWNLOAD 时，调用 component.setDownloader 方法设置下载器。
画面 5：在 getComponent 方法中，判断 processFlow 的类型为 SCHEDULER 时，调用 component.setScheduler 方法设置调度器。
画面 6：在 getComponent 方法中，完成所有类型判断后，返回 component 实例。
画面 7：在 getComponent 方法后，开始编写 startTask 方法，定义方法签名。
画面 8：在 startTask 方法中，创建 ProcessFlowData 实例，并设置 handleType。
画面 9：在 startTask 方法中，遍历 processFlowList，调用每个 ProcessFlow 的 handle 方法处理数据。
画面 10：在 startTask 方法中，调用 crawlerConfig.getSpider().start() 启动爬虫。
画面 11：切换到 Typora 编辑器，展示文档中关于 ProcessingFlowManager 的注释和代码结构说明。
画面 12：回到 IDE，展示 startTask 方法的完整代码，包括调用 crawlerConfig.getSpider().start()。
画面 13：切换到 AbstractOriginalDataProcess.java 文件，展示初始化数据列表的代码，包括判断初始数据列表是否为空。
画面 14：回到 ProcessingFlowManager.java 文件，展示 startTask 方法的完整代码，包括调用 startTask 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
private CrawlerComponent getComponent(List<ProcessFlow> processFlowList) {
    CrawlerComponent component = new CrawlerComponent();
    for (ProcessFlow processFlow : processFlowList) {
        if (processFlow.getComponentType() == CrawlerEnum.ComponentType.PAGEPROCESSOR) {
            component.setPageProcessor((PageProcessor) processFlow);
        }
    }
}
```

画面 2：
```java
if (processFlow.getComponentType() == CrawlerEnum.ComponentType.PAGEPROCESSOR) {
    component.setPageProcessor((PageProcessor) processFlow);
}
```

画面 3：
```java
else if (processFlow.getComponentType() == CrawlerEnum.ComponentType.PIPELINE) {
    component.addPipeline(processFlow);
}
```

画面 4：
```java
else if (processFlow.getComponentType() == CrawlerEnum.ComponentType.DOWNLOAD) {
    component.setDownloader((Downloader) processFlow);
}
```

画面 5：
```java
else if (processFlow.getComponentType() == CrawlerEnum.ComponentType.SCHEDULER) {
    component.setScheduler((Scheduler) processFlow);
}
```

画面 6：
```java
return component;
```

画面 7：
```java
public void startTask(List<ParseItem> parseItemList, CrawlerEnum.HandleType handleType) {
```

画面 8：
```java
ProcessFlowData processFlowData = new ProcessFlowData();
processFlowData.setHandleType(handleType);
```

画面 9：
```java
for (ProcessFlow processFlow : processFlowList) {
    processFlow.handle(processFlowData);
}
```

画面 10：
```java
crawlerConfig.getSpider().start();
```

画面 11：
```java
/**
 * 获取组件封装
 * @param processFlowList
 * @return
 */
private CrawlerComponent getComponent(List<ProcessFlow> processFlowList) {
    CrawlerComponent component = new CrawlerComponent();
    for (ProcessFlow processFlow : processFlowList) {
        if (processFlow.getComponentType() == CrawlerEnum.ComponentType.PAGEPROCESSOR) {
            component.setPageProcessor((PageProcessor) processFlow);
        } else if (processFlow.getComponentType() == CrawlerEnum.ComponentType.PIPELINE) {
            component.addPipeline(processFlow);
        } else if (processFlow.getComponentType() == CrawlerEnum.ComponentType.DOWNLOAD) {
            component.setDownloader((Downloader) processFlow);
        } else if (processFlow.getComponentType() == CrawlerEnum.ComponentType.SCHEDULER) {
            component.setScheduler((Scheduler) processFlow);
        }
    }
    return component;
}
```

画面 12：
```java
public void startTask(List<ParseItem> parseItemList, CrawlerEnum.HandleType handleType) {
    ProcessFlowData processFlowData = new ProcessFlowData();
    processFlowData.setHandleType(handleType);
    for (ProcessFlow processFlow : processFlowList) {
        processFlow.handle(processFlowData);
    }
    crawlerConfig.getSpider().start();
}
```

画面 13：
```java
if (!null != initialDataSetList && !initialDataSetList.isEmpty()) {
    addSpiderRequest(initialDataSetList);
} else {
    log.error("没有有效的初始化URL列表");
}
```

画面 14：
```java
public void startTask(List<ParseItem> parseItemList, CrawlerEnum.HandleType handleType) {
    ProcessFlowData processFlowData = new ProcessFlowData();
    processFlowData.setHandleType(handleType);
    for (ProcessFlow processFlow : processFlowList) {
        processFlow.handle(processFlowData);
    }
    crawlerConfig.getSpider().start();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

