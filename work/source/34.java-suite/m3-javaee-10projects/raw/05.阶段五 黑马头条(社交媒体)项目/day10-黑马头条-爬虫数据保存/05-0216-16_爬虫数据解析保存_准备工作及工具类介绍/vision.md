# 画面线理解：16_爬虫数据解析保存_准备工作及工具类介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\16_爬虫数据解析保存_准备工作及工具类介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:40, 01:11, 01:29, 01:52, 02:07, 03:01, 03:32, 03:47, 04:14, 04:49, 05:25, 05:45, 06:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:10:26

1) 这一组画面整体在讲什么（一句话）：
讲解爬虫项目中 HTML 解析管道、线程池和抽象流程类的代码实现与结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 AbstractHtmlParsePipeline.java 文件中的代码，其中包含一个注释“不符合文档类型”，以及一个抛出异常的逻辑。
- 代码片段：
  ```java
  log.info("不符合文档类型, url: {}, documentType: {}, handleType: {}", url, documentType, handleType);
  return;
  ```
  ```java
  protected abstract void handleHtmlData(T parseItem);
  ```

画面2：
- 展示了 AbstractHtmlParsePipeline.java 文件中的代码，其中包含一个注释“开始处理”。
- 代码片段：
  ```java
  Item item = crawlerHelper.getParseItem(resultsItems.getRequest());
  Item itemAll = resultsItems.getAll();
  ```
  ```java
  log.info("开始处理");
  ```

画面3：
- 展示了 PPT 页面，标题为“3.6 其他工具类”，并列出了几个工具类的包路径。
- 代码片段：
  ```java
  public abstract void handleHtmlData(T t);
  ```
  ```java
  public String getParseExpression() {
      return "p,pre,h1,h2,h3,h4,h5";
  }
  ```

画面4：
- 展示了 AbstractHtmlParsePipeline.java 文件中的代码，其中包含对不同 HTML 标签（h1 到 h5）的样式设置。
- 代码片段：
  ```java
  HtmlStyle h1Style = new HtmlStyle();
  h1Style.addStyle("font-size", "18px");
  h1Style.addStyle("line-height", "20px");
  styleMap.put("h1", h1Style);
  ```
  ```java
  HtmlStyle h2Style = new HtmlStyle();
  h2Style.addStyle("font-size", "16px");
  h2Style.addStyle("line-height", "18px");
  styleMap.put("h2", h2Style);
  ```

画面5：
- 展示了 AbstractHtmlParsePipeline.java 文件中的代码，其中包含对 h1 和 h2 标签的样式设置。
- 代码片段：
  ```java
  public Map<String, HtmlStyle> getDefHtmlStyleMap() {
      Map<String, HtmlStyle> styleMap = new HashMap<String, HtmlStyle>();
      HtmlStyle h1Style = new HtmlStyle();
      h1Style.addStyle("font-size", "22px");
      h1Style.addStyle("line-height", "24px");
      styleMap.put("h1", h1Style);
      HtmlStyle h2Style = new HtmlStyle();
      h2Style.addStyle("font-size", "18px");
      h2Style.addStyle("line-height", "20px");
      styleMap.put("h2", h2Style);
  }
  ```

画面6：
- 展示了 AbstractHtmlParsePipeline.java 文件中的代码，其中包含对 h1 和 h2 标签的样式设置。
- 代码片段：
  ```java
  public Map<String, HtmlStyle> getDefHtmlStyleMap() {
      Map<String, HtmlStyle> styleMap = new HashMap<String, HtmlStyle>();
      HtmlStyle h1Style = new HtmlStyle();
      h1Style.addStyle("font-size", "22px");
      h1Style.addStyle("line-height", "24px");
      styleMap.put("h1", h1Style);
      HtmlStyle h2Style = new HtmlStyle();
      h2Style.addStyle("font-size", "18px");
      h2Style.addStyle("line-height", "20px");
      styleMap.put("h2", h2Style);
  }
  ```

画面7：
- 展示了 PPT 页面，标题为“3.2 线程池操作类 CrawlerThreadPool”，并列出了几个相关类的包路径。
- 代码片段：
  ```java
  public abstract void handleHtmlData(T t);
  ```
  ```java
  public String getParseExpression() {
      return "p,pre,h1,h2,h3,h4,h5";
  }
  ```

画面8：
- 展示了 CrawlerThreadPool.java 文件中的代码，其中包含线程池的配置和任务执行的逻辑。
- 代码片段：
  ```java
  private static final ArrayBlockingQueue queue = new ArrayBlockingQueue<>(10000);
  private static final ExecutorService executorService = new ThreadPoolExecutor(1, threadNum, 60L, TimeUnit.SECONDS, queue);
  ```

画面9：
- 展示了 CrawlerThreadPool.java 文件中的代码，其中包含任务提交的逻辑。
- 代码片段：
  ```java
  public static void submit(Runnable runnable) {
      log.info("线程池添加任务, 线程池当前任务数量: {}, 最大线程数: {}, queue.size(): {}, threadNum: {}", queue.size(), threadNum, executorService.execute(runnable);
  }
  ```

画面10：
- 展示了 IntelliJ IDEA 的主界面，显示了项目结构和搜索功能。
- 代码片段：
  ```java
  Search Everywhere Double Shift
  Go to File Ctrl+Shift+N
  Navigation Bar Alt+Home
  Drop files here to open
  ```

画面11：
- 展示了 PPT 页面，标题为“3.7 AbstractProcessFlow”，并列出了几个相关类的包路径。
- 代码片段：
  ```java
  public String getOriginalRequestJsonData(String url, Map<String, String> parameterMap) {
      CrawlerProxy proxy = crawlerProxyProvider.getRandomProxy();
      List<CrawlerCookie> cookieList = cookieHelper.getCookieEntityList(url, proxy);
  }
  ```

画面12：
- 展示了项目结构，其中包含“test”目录。
- 代码片段：
  ```java
  Search Everywhere Double Shift
  Go to File Ctrl+Shift+N
  Navigation Bar Alt+Home
  Drop files here to open
  ```

画面13：
- 展示了 PPT 页面，标题为“3.8 CrawlerHtmlParsePipeline类”，并列出了几个相关类的包路径。
- 代码片段：
  ```java
  jsonData = seleniumClient.getJsonData(crawlerHtml);
  return jsonData;
  ```
  ```java
  public boolean isJson(String jsonData) {
      boolean isJson = false;
      try {
          isJson = JsonValidator.getJsonValidator().validate(jsonData);
      } catch (ExecutionException e) {
          e.printStackTrace();
      }
      return isJson;
  }
  ```

画面14：
- 展示了 AbstractHtmlParsePipeline.java 文件中的代码，其中包含类的注释和导入语句。
- 代码片段：
  ```java
  import org.apache.commons.lang3.StringUtils;
  import org.springframework.beans.factory.annotation.Autowired;
  import us.codcraft.webmagic.Task;
  import java.util.Map;
  ```
  ```java
  /**
   * Html 解析抽象类，定义了公用的方法以及抽象模板
   * HtmlPipeline负责抽取数据的处理，包括：计算、转化到数据库、文件等。
   * WebMagic 默认提供了“抽取到控制台”和“抽取到数据库”两种方式。
   * 如果你希望自定义到指定数据库，则需要编写对应的Pipeline。
   * 对于一次需求一般只需要实现一个Pipeline。
   */
  public abstract class AbstractHtmlParsePipeline<T> extends AbstractProcessFlow implements Pipeline {
  ```
