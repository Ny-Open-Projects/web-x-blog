# 20_爬虫系统初始化_文档处理_用户空间解析规则定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\20_爬虫系统初始化_文档处理_用户空间解析规则定义【海量资源尽在 666java.com】.mp4
- 时长 6分23秒（音频 383s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲刚才咱们是把这个初始化的这种解析的方式解析规则咱们说完了下面咱们再来去看下面还有什么东西Property, Set, Set哪个呢是Helper Color Path这个其实是啥意思就是说用户空间用户空间下的什么解析规则搞的是URL这个是哪个你看
[00:31] 比如说咱们打开当前的某一个分类比如到前端这网稍微有点慢还是找招了然后你随便去点一篇文章当然咱们最终是找到的是当前某一个用户的空间对吧比如说就是当前这个用户空间那咱们要从这里边去抓抓什么东西呢抓的是一个一个文章的URL文章的URL你可以按下up12然后是这个东西比如说就是点它
[01:02] 这个呢其实咱们最终呢是要获取到当前的这个A这个A标签最终要获取到当前这个A标签那这个A标签怎么拿呢其实你可以咱们一块来看一看往上拖一些其实呢这个结构呢比较简单了比刚才那个结构路径要浅一些首先呢这有一个慢慢里边有个DIB看到了吗DIB下面呢这有一个下一级有个DIB
[01:28] 然后再往下是一个h几的h4应该是然后下面是一个a这样的话就拿到了好吧那这个比较好写那咱们一块来写一下在这儿咱们可以还按这种方式去写private然后咱们是一个string咱们叫什么呢咱们叫help color s pass好那这个东西怎么去写咱们把这个先复制复过来
[02:01] 好,我们一块写写首先第一集是啥第一集是不是就是DIV应该是一个classAdigo-list是吧DIV然后是括号,add class等于刚才我拷贝这东西然后再往下一集呢再往下一集是不是也是DIV啊OK,没问题,那咱就继续写DIV然后这个咱们先把class写上
[02:34] 这时候你就可以从这去找到这个class就可以了其实这个是多个class你可以去只要一个就可以了这样的话它也能定位然后你从这个div下面再往下找再往下找找的是h4它只是一个class然后是找a这时候你这么写就可以了比如说在这写h4
[03:05] 这样的话呢其实就能找到当前的A标签了啊就能找到当前的标签OK那这个说完之后啊那咱们就接着往下写啊这是又去加了一个属性然后再往下看看还有什么东西啊Property 点什么set然后咱们再去找一个啊这个吧这个是当前的用户空间下的一个下一页的页大小啊在这写一下啊取
[03:37] 用户空间下的页大小这个东西呢其实呢咱们不用在这去定义啊咱们可以那怎么着呢咱们在这去读就可以了其实呢咱们在之前的配置文件中其实在这已经干嘛已经写了一个配置了一个算算是啊你只需要把这东西注入注入到当前这个配置文件中当前的注入的配置类中就可以了啊怎么写呢private然后呢是它这个integer啊
[04:08] 然后呢咱们怎么写是一个crawl next你们最好是跟那个名称是一样啊然后是sizeok完事啊那他呢就在这去写一个什么6啊然后怎么写里边crawl服务啊你把这个拷贝一下可以了啊把他呢把他啊直接放到这放到这就行了行那这个值啊咱们也算是复完了啊
[04:42] 看看下面还有什么东西, property, set, set这个是啥呢,这个好像是最后一个,什么东西啊就是说用户空间下的什么某一个目标这个啊,错了啊,这个没设置完啦,set, target, path, ruler
[05:13] 后页后页是什么写习规则这个呢就是比如说啊我们打开啊开某一个网站到了一个当前的空间然后咱们呢也抓取了某一个文章信息那这时候呢进入到了当前的文章那这时候咱们要去一条一条的去抓取比如说咱们要抓取的什么东西标题文章作者信息是吧时间还有文章的内容那还有一些连接阅读
[05:44] 阅读数是吧还有一些转发什么的啊还有评论像这些东西咱们都应该去抓取那这时候呢这个啊这个抓取的东西呢就比较多了因为你每一项呢每一项啊比如说啊标题是吧时间像这个像这个呢就算是一项每一项它都有自己的解析规则所以说呢那这边呢是一个要去接受一个什么要接受一个list集合list集合啊因为它并不是一项并不是抓取一项它是抓取很多项
[06:14] OK啊行那这个咱们一会儿再写好吧一会儿再写这个咱们先定义出来一会儿咱们再完成当前的这个代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 爬虫项目中，通过配置类设置爬虫的初始页面 XPath、帮助页面 XPath、分页大小和目标页面解析规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，展示 CrawlerConfig.java 文件，其中定义了 initCrawlerXpath 和 helpCrawlerXpath 的字符串变量，用于配置爬虫的初始页面和帮助页面的 XPath 表达式。
画面 2: 浏览器显示空白页面，地址栏为 https://www.csdn.net/nav/web，表示尚未访问有效内容。
画面 3: 浏览器地址栏变为 https://blog.csdn.net/riwen_x，页面仍为空白，表示尚未加载内容。
画面 4: 浏览器显示 CSDN 博客页面“Java基础Day06”，开发者工具（DevTools）中选中了文章列表项的 HTML 元素，其样式为 article-list article-item-box。
画面 5: 回到 IDEA，代码编辑器中高亮显示了 initCrawlerXpath 的定义，该路径用于定位初始页面的文章列表。
画面 6: 浏览器中开发者工具选中了 article-list 类的元素，其样式为 article-list article-item-box，显示了该元素的 CSS 样式。
画面 7: 浏览器中开发者工具选中了 article-list 类的元素，其样式为 article-list article-item-box，显示了该元素的 CSS 样式。
画面 8: IDEA 中，代码编辑器高亮显示了 helpCrawlerXpath 的定义，该路径用于定位帮助页面的文章列表。
画面 9: IDEA 中，代码编辑器显示了 CrawlerConfigProperty 类的 setter 方法列表，包括 setTargetParseRuleList、setCrawlerHelpNextPagingSize、setInitCrawlerUrlList 等。
画面 10: IDEA 中，代码编辑器高亮显示了 setHelpCrawlerXpath 方法，用于设置帮助页面的 XPath。
画面 11: IDEA 中，代码编辑器高亮显示了 setCrawlerHelpNextPagingSize 方法，用于设置分页大小。
画面 12: IDEA 中，代码编辑器高亮显示了 setCrawlerHelpNextPagingSize 方法，用于设置分页大小。
画面 13: 浏览器显示空白页面，地址栏为 https://blog.csdn.net/riwen_x/article/details/102575415，表示尚未加载内容。
画面 14: IDEA 中，代码编辑器高亮显示了 setCrawlerHelpNextPagingSize 方法，用于设置分页大小。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private String initCrawlerXpath="//ul[@class='feedlist_mod']//li[@class='clearfix']//div[@class='article-item-box']";
private String helpCrawlerXpath="//div[@class='article-list']//div[@class='article-item-box']";
```

画面 5:
```java
private String initCrawlerXpath="//ul[@class='feedlist_mod']//li[@class='clearfix']//div[@class='article-item-box']";
```

画面 8:
```java
private String helpCrawlerXpath="//div[@class='article-list']//div[@class='article-item-box']";
```

画面 9:
```java
public CrawlerConfigProperty getCrawlerConfigProperty() {
    CrawlerConfigProperty property = new CrawlerConfigProperty();
    //初始化列表
    property.setInitCrawlerUrlList(getInitCrawlerUrlList());
    //初始化规则定义
    property.setInitCrawlerXpath(initCrawlerXpath);
    //用户空间下的解析规则
    property.setHelpCrawlerXpath(helpCrawlerXpath);
    return property;
}
```

画面 10:
```java
private String helpCrawlerXpath="//div[@class='article-list']//div[@class='article-item-box']";
```

画面 11:
```java
private Integer crawlerHelpNextPagingSize;
```

画面 12:
```java
private Integer crawlerHelpNextPagingSize;
```

画面 14:
```java
private Integer crawlerHelpNextPagingSize;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

