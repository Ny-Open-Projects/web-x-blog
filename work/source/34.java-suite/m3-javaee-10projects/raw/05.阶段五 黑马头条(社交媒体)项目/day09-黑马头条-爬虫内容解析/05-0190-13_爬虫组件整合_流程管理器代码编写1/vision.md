# 画面线理解：13_爬虫组件整合_流程管理器代码编写1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\13_爬虫组件整合_流程管理器代码编写1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:00, 02:01, 02:45, 03:31, 05:39, 06:41, 07:48, 09:35, 10:50, 11:46, 12:32, 13:19, 14:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:51:23

1) 这一组画面整体在讲什么（一句话）：
讲解爬虫框架中 ProcessingFlowManager 类的初始化逻辑、流程处理列表排序、以及如何根据配置生成并初始化 Spider 对象。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ProcessingFlowManager 类的 Java 代码，包含 @Component 注解、@Autowired 注入的 crawlerConfig、processFlowList 和 crawlerNewsAdditionalService 字段，以及类注释说明其功能。
画面 2: 展示 initProcessingFlow 方法的实现，包括对 processFlowList 排序和调用 configSpider 方法。
画面 3: 展示 AbstractCrawlerPageProcessor.java 文件中的 process 方法，用于解析页面并设置 Site 信息。
画面 4: 展示 ProcessingFlowManager 类的成员变量列表，包括 Process、ProcessBuilder、ProcessHandle 等。
画面 5: 展示 ProcessingFlowManager 类的结构，包含私有字段 crawlerConfig 和 processFlowList。
画面 6: 展示 initProcessingFlow 方法的代码，包含对 processFlowList 的排序和初始化逻辑。
画面 7: 展示 initProcessingFlow 方法中对 processFlowList 的排序逻辑。
画面 8: 展示 initProcessingFlow 方法中调用 configSpider 方法。
画面 9: 展示 configSpider 方法的实现，包含初始化 Spider 对象。
画面 10: 展示 initSpider 方法中获取 CrawlerComponent 并创建 Spider 对象。
画面 11: 展示 initSpider 方法中设置 Spider 的 PageProcessor。
画面 12: 展示 initSpider 方法中设置 Spider 的 Scheduler。
画面 13: 展示 initSpider 方法中设置 Spider 的 Downloader。
画面 14: 展示 initSpider 方法中设置 Spider 的 Pipeline 列表并遍历。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 创建数据处理
 * 对ProcessFlow 接口类型的类进行前置初始化的一些配置处理
 * 强制AbstractOriginalDataProcess 类的 handle 方式，初始化URL 以及初始化 代理数据
 * 并生成Spider，并自定启动
 * 进程管理的入口
 */
@Component
@Slf4j
public class ProcessingFlowManager {

    @Autowired
    private CrawlerConfig crawlerConfig;

    /**
     * 注入实现processFlow 接口的所有类
     */
    @Resource
    private List<ProcessFlow> processFlowList;

    @Autowired
    private CrawlerNewsAdditionalService crawlerNewsAdditionalService;

    /**
     * spring 启动时加载并进行调用
     */
```

画面 2:
```java
private void initProcessingFlow() {
    if (null != processFlowList && !processFlowList.isEmpty()) {
        processFlowList.sort(new Comparator<ProcessFlow>() {
            @Override
            public int compare(ProcessFlow p1, ProcessFlow p2) {
                if (p1.getPriority() > p2.getPriority()) {
                    return 1;
                } else if (p1.getPriority() < p2.getPriority()) {
                    return -1;
                }
                return 0;
            }
        });
        Spider spider = configSpider();
        crawlerConfig.setSpider(spider);
    }
}
```

画面 3:
```java
public CrawlerEnum.ComponentType getComponentType() {
    return CrawlerEnum.ComponentType.PAGEPROCESSOR;
}

@Override
public void process(Page page) {
    long currentTimeMillis = System.currentTimeMillis();
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    log.info("开始解析页面页。url: {}, handleType: {}", page.getUrl(), handleType);
    crawlerPageProcessorManager.handle(page);
    log.info("解析页面完成。url: {}, handleType: {}, 耗时: {}, page: {}, handleType: {}", page.getUrl(), handleType, System.currentTimeMillis() - currentTimeMillis, page, handleType);
}

@Override
public Site getSite() {
    Site site = Site.me().setRetryTimes(getRetryTimes()).setRetrySleep(getRetrySleep()).setSleep(getSleep()).setRetrySleep(getRetrySleep());
    return site;
}
```

画面 4:
```java
protected
ProcessingFlowManager (com.heima.crawler.manager.ProcessingFlowManager)
Process (java.lang)
ProcessBuilder (java.lang)
ProcessHandle (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandleImpl (java.lang)
ProcessHandle
