# 08_文档解析_个人空间页解析2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\08_文档解析_个人空间页解析2【海量资源尽在 666java.com】.mp4
- 时长 10分17秒（音频 617s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续啊呃上面呢咱们就来去来和处理在当前那个核心的这个数据啊这就是来处理他们的数据处理数据然后呢在上面咱们首先呢你先要获取一些数据啊所以说咱们在这先去做两个东西好吧那第一个呢是咱们的callerconfig.opt这个咱们需要去获取用这里边的封装了咱们一些我们的一些这种URL数据啊所以说你需要先去入进来
[00:36] 然后第二个呢这个咱们还是需要用到另外一个private咱们的一个什么需要去用到咱们的验证的一些内容啊所以说咱们用一个什么cowler helpercowlercowler这个咱们已经其实在咱们的康Feign中啊康Feign中已经是但是让shrimp去管理了所以说这个咱们可以直接注入啊行那注入
[01:03] 复活完之后呢咱们下面呢就可以去获取数据那获取数据之前呢咱们呢是有一些的数据还是要拿到的比如说呢咱们需要去拿到它的类型拿到它的处理类型获取类型类型怎么获取呢这个类型呢咱们都可以通过这个小什么呢RBAT handle type这里边只需要有一个request就可以
[01:37] request怎么拿呢request其实你可以通过目前这个pitch是说了啊这pitch是谁的呀这pitch是目前的webmatics是吧这里边就可以拿到一个request对象最终的就能去返回一个现在handle type现在目前咱们都是正向是吧然后这是一个啊然后呢下面呢咱们就可以去获取他的URL获取URL啊那URL怎么获取呢其实也是通过当前那个pitch这pitch里边其实对象有很多啊
[02:07] 这是点里边你可以拿get现在就可以拿到一个url但是最终是一个get用这个才是真正的一个字幕块的url比如说什么叫request url这是url然后下面咱们就可以真正的去处理处理之前最好咱们在这去加一个东西什么东西在这咱们去拆一个时间好吧systemsr先去记录时间
[02:36] time millions然后这个呢其实就是咱们那个zuop拿到这个之后呢time吧好吧先记录一下看看这个里能执行多长时间啊然后再往下呢往下咱们也可以去用前的日志啊去记录比如说叫info第一个值呢咱们可以在这写啊说开始解析帮助业帮助业啊
[03:14] 这几期帮助页然后呢URL呢就写一个冒号好吧然后再往下啊然后是handle typehandle type是啥呢写一个东西然后第一个我们的URL就是谁啊叫request URL第二个呢是handle type我会在这记录一下好吧这样的话方便后期啊咱们去找错误啊然后这是记录了
[03:45] 记录完之后呢咱们下面呢就可以去解析了啊那解析的话呢首先呢咱们还是要获取啊获取什么呢获取配置的抓取规则这个规则的话是不是咱们都是封装到当前这个里边啊所以说咱们在这啊直接R set color helper啊应该是set helper color x plus这个呢其实就是一个
[04:19] 然后呢然后呢咱们就可以去发请求但是发请求之前呢咱们还是得再去再去说一下因为咱们现在啊咱们都需要有可能会进行分页是吧所以说呢咱们应该是要获取他的一个什么东西啊他的一个这种配置要size啊那size怎么拿呢其实在这里边有吗有啊而gap这边有color higher part nexthitting size
[04:48] 这个其实拿这个size然后下面你就可以去通过当前这个s pass去获取一些数据这个怎么办咱们可以用pitch.html然后给咱们之前那个unit是一样的s passs pass就是hear color pass然后最终咱们是有一个x这是固定写法好中的咱们就可以写错了
[05:21] 这个呢就能拿到了当前的一个什么当前的一个Helper的Helper的URL list拿了它之后啊拿了之后呢咱们这个呢只是一个最初始化的一个东西这时候呢有可能呢这样说吧这个呢其实就是第一页的URL啊这样说吧比如说啊在这啊你打开了某一个打开了某一个它就是拿到了当前你打开的这个东西然后呢它去获取了
[05:50] 里边的所有的URL那时候有可能会需要分页是吧有可能需要分页吧这时候比如说这下面有1234这时候你只拿到第一页肯定是不行的那这数据肯定不全这时候咱们需要干嘛需要拿第二页从第二页开始拿可能拿到多页这时候所以说咱们在这去拿了一个什么拿了一个这种页码是吧你到底是想要去翻多少页是吧然后这个是一个出出话的URL
[06:20] 应该是刚刚进入个人空间的一碗列表当然这个一碗列表呢就是一个目标一碗列表啊那行那这个拿到之后啊咱们现在要分页的话呢咱们可以再往下再去处理那这处理呢就这样就这么写啊首先呢咱们在这去判断一下或说浪等于谁呀等于前的谁呀前的这个他
[06:48] 这个肯定是有值如果说是0的话那这时候呢咱们就没有必要去分业了好吧它必须是大于1它必须是大于1但是这个值是你自己定义的咱们目前的值是不是默认给了一个10啊默认给了个10啊然后咱们可以再去做判断啊它呢大于1这时候呢咱们才需要分业如果说不需要的话啊如果说它不是大于1那个它不需要分业的话怎么办呢
[07:16] 就可以在这可以直接去调用调用什么呢咱们可以直接调用IdeaSpenderRequest我们就可以直接把这个内容放到Request对象中当然这个是SpenderRequest这时候它就可以去发送请求然后是最终获取数据了好吧行那这个咱们就直接去把这个直接放进去就可以了Help.URList然后第二个咱们需要去把这个
[07:45] 配置点get request,request拿到就可以了行,那这个还需要个参数因为它需要知道是什么类型不是,它需要知道到底是哪一个文档类型,哪个文档类型这时候咱们可以直接去获取follower numeral.get因为是document,document type.page
[08:18] 配置的话呢其实就是个人空间页好吧应该是到下一个页啊到下一个因为咱们现在是Helper你看啊这是一开始初始化下面的是一个是空间是吧然后再往下呢就是配置咱们用不着现在啊目前用不着咱们现在就是三级初始化然后是个人空间然后最后呢是一个目标页目标页啊也就是说咱们现在应该交由下一级去处理交由下一级去处理好吧
[08:45] 嗯行那在这啊咱们设置完之后呢咱们一会儿呢再去编写咱们什么呢咱们这个什么这个分页的逻辑好吧嗯行那这时候咱们在这啊再去加个东西啊嗯也是为了后期啊排错啊方便一些啊首先呢咱们在这啊在这写什么解析帮助业数据完成然后呢
[09:15] 然后是URL是谁你需要去指定一下是吧然后是handlehandletype是谁咱们要去指定一下是吧然后咱们是再写一个耗时耗时耗时耗时多长时间多长时间你也可以写一下第一个值就是配置点在他URL是吧然后第二个就是handletype
[09:49] 三个呢三个就好容易了是吧system.点去谁呀点去咱们这个corner time就可以好吧这就是一个时间OK啊这个咱们就算说着完了啊那这个分页逻辑啊这是分页分页逻辑处理我们呢一会儿再来处理

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 爬虫框架中，通过自定义处理器（CrawlerHelpPageProcessor）解析帮助页，获取页面类型、URL、爬虫路径等信息，并记录日志。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 CrawlerHelpPageProcessor 类的结构，定义了 handlePage 方法，用于处理页面。
画面 2: 在 handlePage 方法中，通过 crawlerHelper.getHandleType(page.getRequest()) 获取页面类型。
画面 3: 代码中调用 crawlerHelper.getHandleType(page)，并显示了该方法的参数和返回值。
画面 4: 在 handlePage 方法中，定义了 private 成员变量 crawlerConfigProperty 和 crawlerHelper。
画面 5: 在 handlePage 方法中，调用 crawlerHelper.getHandleType(page) 获取页面类型，并记录日志。
画面 6: 在 handlePage 方法中，获取当前时间戳、请求 URL 和页面类型。
画面 7: 在 handlePage 方法中，获取爬虫配置中的 XPath 表达式和分页大小。
画面 8: 切换到 CSDN 网站，查看一篇关于 Java 练习的博文。
画面 9: 在 CSDN 网站中，浏览一篇关于 Java 中数组和基本方法的文章。
画面 10: 返回代码编辑器，继续编写 handlePage 方法，调用 crawlerHelper.getHandleType(page)。
画面 11: 展示了枚举类型 DocumentType、ComponentType 和 HtmlType 的定义。
画面 12: 在 handlePage 方法中，记录日志“解析帮助页”。
画面 13: 在 handlePage 方法中，记录日志“解析帮助页数据完成”，并显示耗时和页面信息。
画面 14: 在 handlePage 方法中，记录日志“解析帮助页数据完成”，并显示耗时和页面信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import com.heima.model.crawler.enums.CrawlerEnum;
import lombok.extern.log4j.Log4j2;
import org.springframework.stereotype.Component;
import us.codecraft.webmagic.Page;

@Component
@Slf4j2
public class CrawlerHelpPageProcessor extends AbstractCrawlerPageProcessor {

    @Override
    public void handlePage(Page page) {

    }
}
```

画面 2:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
}
```

画面 3:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
    // 获取爬虫路径
    String crawlerXPath = crawlerConfigProperty.getHelpCrawlerXPath();
    // 获取分页大小
    Integer crawlerHelpPagingSize = crawlerConfigProperty.getHelpNextPagingSize();
}
```

画面 4:
```java
private CrawlerConfigProperty crawlerConfigProperty;
private CrawlerHelper crawlerHelper;
```

画面 5:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
    // 获取爬虫路径
    String crawlerXPath = crawlerConfigProperty.getHelpCrawlerXPath();
    // 获取分页大小
    Integer crawlerHelpPagingSize = crawlerConfigProperty.getHelpNextPagingSize();
}
```

画面 6:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
    // 获取爬虫路径
    String crawlerXPath = crawlerConfigProperty.getHelpCrawlerXPath();
    // 获取分页大小
    Integer crawlerHelpPagingSize = crawlerConfigProperty.getHelpNextPagingSize();
}
```

画面 7:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
    // 获取爬虫路径
    String crawlerXPath = crawlerConfigProperty.getHelpCrawlerXPath();
    // 获取分页大小
    Integer crawlerHelpPagingSize = crawlerConfigProperty.getHelpNextPagingSize();
}
```

画面 10:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
    // 获取爬虫路径
    String crawlerXPath = crawlerConfigProperty.getHelpCrawlerXPath();
    // 获取分页大小
    Integer crawlerHelpPagingSize = crawlerConfigProperty.getHelpNextPagingSize();
}
```

画面 11:
```java
public enum DocumentType {
    INIT, HELP, PAGE, OTHER
}

public enum ComponentType {
    NORMAL, PAGEPROCESSOR, PIPELINE, DOWNLOAD, SCHEDULER
}

public enum HtmlType {
    P_TAG("p", "text"),
}
```

画面 12:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
    // 获取爬虫路径
    String crawlerXPath = crawlerConfigProperty.getHelpCrawlerXPath();
    // 获取分页大小
    Integer crawlerHelpPagingSize = crawlerConfigProperty.getHelpNextPagingSize();
}
```

画面 13:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();
    // 记录日志
    log.info("开始解析帮助页，url: {}, handleType: {}", requestUrl, handleType);
    // 获取爬虫路径
    String crawlerXPath = crawlerConfigProperty.getHelpCrawlerXPath();
    // 获取分页大小
    Integer crawlerHelpPagingSize = crawlerConfigProperty.getHelpNextPagingSize();
}
```

画面 14:
```java
@Override
public void handlePage(Page page) {
    // 处理的默认类型
    // 正向
    // 反向
    // Return
    // 获取类型
    String handleType = crawlerHelper.getHandleType(page.getRequest());
    // 获取当前时间戳
    long currentTime = System.currentTimeMillis();
    // 获取请求URL
    String requestUrl = page.getHtml().get();

