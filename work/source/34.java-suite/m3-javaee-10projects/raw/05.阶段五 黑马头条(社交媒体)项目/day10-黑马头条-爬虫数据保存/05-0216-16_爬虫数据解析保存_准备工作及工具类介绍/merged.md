# 16_爬虫数据解析保存_准备工作及工具类介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\16_爬虫数据解析保存_准备工作及工具类介绍【海量资源尽在 666java.com】.mp4
- 时长 6分6秒（音频 367s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续啊刚才这个差点东西啊咱们在这去补上说你在这去再去打印一个日志啊这日志里边呢咱们就是说当前的解析结束是吧解析结束然后呢是url是啥是啥可以设立一个然后是handlehandle type是啥然后是号识啊号识啊冒号好然后第一个呢是url第二个是handle type第三个是
[00:33] system.点去行那这个设置完之后咱们可以看下笔记里边其实还没有完是吧咱们也可以把这个方法去设置一个前置参数处理这个方法就是数据清洗及清洗以保存行那这两个方法咱们一会会在子类中去实现咱们可以看笔记里边其实还有一些数据咱们需要去设置
[01:11] 那现在是有一个解析表达师还有一个默认的html样式啊咱们可以把它给拷过来两个其实没拉可写的啊你可以看一下啊咱们就是组装组装你可以把当前这个啊引入引入进来好那这是啥呢你可以看一下啊这个把它给粘一下没有粘全吗怎么着行了好就这么着吧啊那这里边呢其实呢第一个呢是一个样式啊
[01:54] 一个样式没粘全是吗其实还少一个啊还少一个咱们再去粘一下啊把这东西也粘过来好吧这个呢其实就是H1因为你要解析之后呢里边呢咱们会有一些标签H1 H2 H3像这个它有样式像H1对应的字体大小和样式是啥OK就这个意思啊咱们呢会去
[02:22] 会去对比到时候咱们去获取真正去存取文章的时候呢咱们需要用到这样的样式所以说咱们只是算是一个工具啊可以放到这当然你的字体比如说A13的时候它就会去设置A13是16和18这个能听明白吧OK啊那这个呢咱们这个是咱们最主要的一个功能咱们一会儿呢再去写子类的时候会去用得着会用得着啊行那这个咱们就先说到这啊
[02:52] 那这个类就算是说这完了说这完了说这完之后咱们下面就可以看一些类这里边还要再去说一个就是现成池因为咱们在去创建子类的时候在去解析的时候为了能够更快一些咱们可以创建一个这种现成池用现成来帮助咱们更快的去处理所以说这又去做了一个现成池的处理类咱们也可以直接去拷贝过来只能够更快一些
[03:22] 到当前process下面有这去创建一个Thread, 念完之后呢直接把当前这个线程这个类啊考过来就可以了啊JUC包下吧JUC这个啊那这个咱们就先弄到这儿, 咱们去用的时候咱们可以再去简单说一说好吧行那这是一个啊这里咱们再往下看看看还需不需要点心
[03:55] 里边还有一个ZIP Utils这个就是对内容的解压和压缩咱们之前用过就不再一说了还有一个HTML Path这个其实它也是针对于HTML内容然后是解析解析完之后是解析成咱们自己想要的一个格式这个也是一个工具类也是在哪在当前的这种Utils里边有一个HTML Path这个是干嘛的咱们一会去用到的时候咱们可以再讲一讲好吧
[04:23] 然后下面还有啊有一个反射的工具类其实咱们刚刚已经用过一次了就是说都是些反射的一些东西设置啊刚才咱们就是设置了一个set properties是吧它就是主要呢就是往对往当前的一个对象中去设置值设置值啊当然通过是反射的方式啊好还有其他工具类啊这个咱们大概说一说因为咱们现在没有讲自己的业务啊一会咱们
[04:52] 用到的时候咱们可以再说还有一些日期的是吧还有一些这种HM Streams的一些工具类还有卡不卡Center咱们要去发消息还有当前这个因为最终的你也要去往文章审核文章那一块去发送消息所以说咱们用到了是当前这个消息类好吧行这个设置完之后咱们还有一步要设置这个咱们也先考过来这个考到哪呢
[05:20] 这个呢主要呢就是考到当前的这个通用的附类中像process下面是不是有一个obstruct process flow啊就它啊你把它考到这考到之后呢那你说什么时候用呢咱们一会去用的时候咱们可以再说好吧用的时候再说啊这个调用的时候咱们可以再去讲因为现在可能那样的话可能会更好理解一些好吧那行那这个咱们所有的准备工作啊基本上做完了啊下面呢
[05:49] 咱们就来去编写当前的这个类这个类呢其实就是当前咱们编写的编写的这个Path叫Obstract HTML Path Pavement它的一个子类然后呢咱们再去处理具体的业务好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

