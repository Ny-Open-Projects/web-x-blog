# 19_爬虫系统初始化_文档处理_初始化url解析规则定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\19_爬虫系统初始化_文档处理_初始化url解析规则定义【海量资源尽在 666java.com】.mp4
- 时长 11分7秒（音频 667s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就接着往下讲啊刚才呢咱们是把一些实体类啊给说了一下下面呢咱们再去说一个就是爬床配置的属性那属性呢其实就是还是一个类这个类呢其实也已经提供了这里边内容咱们可以看一下啊它呢一共是包含了五个内容来看一下这五个属性啊第一个呢就是咱们之前第一次设置的这个初始化的一网啊初始化的一网这个呢主要是从配置文件中去读的
[00:31] 去读的然后下面第二个呢就是有一个什么初始化抓取的chartpath表达式chartpath表达式那这表达式是啥呢咱们一会去说因为呢咱们刚才说了咱们需要去设置几块内容啊设置两次是吧要分别抓两次啊来看一下咱们打开也行一块说一说啊首先呢你打开当前某一个分类比如说招牌咱们要抓取的是当前这些文章展示的什么当前的空间是吧其实咱们的目标就是
[01:01] 找到加温这个初始化UR然后是找到当前这些列表中的用户的空间用户的空间这就是咱们的目标其实这个存的就是当前你的规则就是怎么去抓取当前这个文章的用户空间好这是一个然后再往下看然后获取获取什么呢就是帮助一面的抓取规则也就是说现在咱们这个已经从当前那个初始化
[01:31] 而是找到了当前的这一块然后呢然后要从这个空间里边去抓取具体的目标文章的信息应该是目标文章的URL啊行那这是第二个啊然后还有一个就是开启嗯是否开启帮助页面的分页抓取它应该不是是否开启你是需要去定义定义一个什么定义一个总值一个范围一个范围你要去到底是要抓取多少条数据
[02:00] OK啊如果说是0的话就不分页啊如果说大于1的话那就需要进行分页啊然后再往下啊这是有一个目标页抓取的规则那这个呢其实呢就是咱们最重要抓取的规则比如说比如说啊你打开了在这儿啊去打开了一个当前的这种文章然后这个文章的抓取规则其实都是封装到了哪儿啊
[02:24] 都是封装到了当前的这个里边这里边其实才是一个集合因为这里边有可能会有多个字段需要抓取所以说咱们每一个字段都要去用它的某一项这种解析规则去解析所以说它是一个list集合好 那咱们下面就来去手动去编写一下这块内容其实咱们都要去配到哪都要去配到color config当前的属性其实都是为啥呢为了后期
[02:53] 抓取的时候方便所以说咱们都统一都封装到了当前这个color config property所以说咱们需要把它呢把它呢是放到Spring容器中那这个就比较简单了怎么办呢打开当前的color打开之后呢你看看下面内容呢咱们还没有定义咱们在这儿可以在这儿去定义一个方法比如说public咱们返回值呢就是一样返回值就是你要去让Spring去管理的当前这个东西是吧
[03:23] 所以说返回值就是它就是color config propertycolor config property然后咱们是说一个方法我叫get color还是它吧好吧就叫它然后呢然后怎么办呢然后这里边咱们可以设置值来来这可以去加一个注解叫什么admin这个呢就是这个返回值就放到了spin的容器中然后下面呢你就可以在这里边去new了啊比如说你new出来一个它color
[03:58] config property等于new一个colorconfig property然后下面咱们主要是复制复制property.setset谁呢里边有五个值是吧咱们可以一个一个来比如说这里边有一个叫什么need color bar list这个其实咱们之前是应该是拿过的以前的color config当前的列中其实已经
[04:31] 有这个方法了所以说你直接可以获取这个值咱们又算是收拾完了当然这个咱们可以写下注尺都市化URL列表好再往下看这个防止报错咱们可以直接去让它返回好这是第一个值然后下面还有第二个值Property.setInitColorURL不对已经收完了下面这个
[05:00] 这个其实就是一个什么就是一个你的解析的规则解析的规则初始化URL解析规则定义这东西怎么办这东西这样我们可以在这手写当然了咱们也可以去提出来一个变量比如说怎么叫什么叫init它是一个spin性的init power bypass pass pass好
[05:44] 可以把它呢放到这这样就可以了这个规则到底该怎么去写这个规则写呢其实呢你得去干嘛呢你得去找到当前的页面比如说我把这些找到当前的出口号这个页面啊刚才说了你要去找到某一个分类比如说就是家伙啊咱们就现在就以家伙为例比如说你要找到什么呢找到当前这个列表中这个列表中啊比如说某一项某一项什么呢
[06:10] 为象的空间就是说就是当年的空间这个空间啊其实看这样说啊应该是这里边所有的空间啊是吧那这是广告啊这不算啊这个东西也就是说你要去找到当前这个URL找到这个URL这个时候咱们把这个URL解析到定位到就可以了之前咱们之前讲的一个叫XPath所以说咱们可以使用XPath进行定位进行定位啊
[06:40] 这样咱们可以去右键也可以按F12F12之后你可以点一下这东西然后是比如说找到当前的这东西点一下点一下之后你看这个就是有个DDNAME然后这个其实就是咱们想要的内容这个其实就是咱们想要的内容那你也可以点一下你看点点击之后是不是就是某一个用户的空间的OK那这个是没有问题的然后咱们可以继续关了
[07:11] 然后咱们再回过头来那怎么去抓取呢那怎么定位呢这时候呢咱们还要再去分析当前这个页面呢到底是在哪到底是在哪啊行那咱们可以看一下啊首先呢它是DD上面是DL什么DIB LIOK它顶级是DIB那再往上是啥呢再往上肯定啥呢肯定是有一个叫URL是吧所以说呢咱们可以从哪啊可以从当前这个URL去定义啊可以怎么写呢
[07:41] 嗯你看啊打开这个代码啊在这写然后你写写的方法呢就是杠杠是吧从这要是从根路径开始url找到url然后呢然后咱们可以定义它的属性属性是怎样属性是不是叫feed什么loading啊不是它啊不是它是这个是吧feed modefeed杠mode然后是加文呃当然这是一个定义属性是吧定义属性是怎么着class
[08:17] 当然这个招你可以给它删掉因为咱们现在是选择的是分类选择的是分类如果说你想外播的话可能那就没法抓去外播了是吧所以说咱们可以把招招还删了就前面这个就可以了就前面这个好所以说咱们就这么着好然后UR下面是哪一级UR下面LILI是吧所以说咱们在这去写一个LILI其实它也有很多LI
[08:49] 你看很多RI啊,要去找到什么clear fix所以说咱们要去再去定义一个东西啊叫clear fix什么at class然后再往下啊往下咱们还要再去定义啊没完然后这里边是不是有一个div是吧所以说你要是再定义当前i下面div是class-colc1是吧
[09:18] 这到底啥意思这个是他们定义的啊这边也不知道咱们只需要当前能够定位到这个位置就可以啊咱们比方多少级一定要定位到这好吧好再往前走啊这时候呢咱们是一个DIB然后是5号at plus等于什么呢好来看一看啊等于的话就是list-zun好这就是定义到了他的下一级再往下看还有还有还有什么级别
[09:50] div下面是不是有一个dl是吧没问题吧ok啊所以说这时候呢你要去再去定义到dl啊这dl啊其实它是定义了一个名签就不用管它啊咱们也没有必要去学习它咱们只是要能够定位到我自己想要的位置就可以了dl那就写dl呗dl下面是有一个atplus等于好加上之后啊咱们再往下看啊这时候呢就快到了啊
[10:20] 然后DL下面是不是DD啊DD是className最终是能够找到这当前那个A标签没问题吧所以说咱们在这再往下写一层是什么DD然后是什么classAidClass等于什么往前来看一看你就是Name啊Name然后呢下面是你直接写个就可以了因为咱们最终啊目前只写到A就可以我们要去获取到的是一整条
[10:53] 这一整条啊后期咱们可以再去下载的时候可以再去进行处理好吧行那这个初始化的一玩意的定义啊咱们就或者这个路径啊咱们就先说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java爬虫项目中配置和使用XPath表达式来提取网页数据，并展示在浏览器开发者工具中分析页面结构的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中CrawlerConfigProperty类的代码，包含初始化URL列表和XPath表达式的字段定义。
画面2：展示CSDN网站的Java相关文章列表页面。
画面3：展示CrawlerConfig类中定义的配置项，包括爬虫帮助页大小和目标解析规则列表。
画面4：展示IDE中CrawlerConfig类的代码，包含获取CrawlerHelper和CrawlerProxyProvider的Bean方法。
画面5：展示CrawlerConfig类中获取CrawlerConfigProperty的Bean方法。
画面6：展示CrawlerConfig类中获取CrawlerConfigProperty的Bean方法，代码已开始编写。
画面7：展示CrawlerConfig类中为CrawlerConfigProperty对象设置初始化URL列表和XPath表达式。
画面8：展示CSDN网站的Java相关文章列表页面。
画面9：展示浏览器开发者工具中对页面元素的分析，选中了包含“Java排序算法实现方式”的div元素。
画面10：展示浏览器开发者工具中对页面元素的分析，选中了包含“Java排序算法实现方式”的div元素，显示了其HTML结构。
画面11：展示浏览器开发者工具中对页面元素的分析，选中了包含“Java排序算法实现方式”的div元素，显示了其HTML结构。
画面12：展示浏览器开发者工具中对页面元素的分析，选中了包含“Java排序算法实现方式”的div元素，显示了其HTML结构。
画面13：展示浏览器开发者工具中对页面元素的分析，选中了包含“Java排序算法实现方式”的div元素，显示了其HTML结构。
画面14：展示IDE中CrawlerConfig类的代码，正在编写用于提取特定页面元素的XPath表达式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public void setParseContentList(List<String> parseContentList) {
    this.parseContentList = parseContentList;
}
```
```java
//爬虫配置属性CrawlerConfigProperty
com.heima.crawler.process.entity.CrawlerConfigProperty
/**
 * 爬虫配置属性
 */
@Setter
@Getter
public class CrawlerConfigProperty implements Serializable {
    /**
     * 初始化请求URL列表
     */
    private List<String> initCrawlerUrlList;
    /**
     * 初始化页面的xpath表达式
     */
    private String initCrawlerXpath;
    /**
     * 帮助页面提取规则
     */
    private String helpCrawlerXpath;
    /**
     * 开启自动翻页功能
     */
    private Integer crawlerHelpNextPagingSize;
    /**
     * 目标页面提取规则
     */
    private List<ParseRule> targetParseRuleList;
}
```

画面3：
```java
//配置CrawlerConfig
com.heima.crawler.config.CrawlerConfig
/**
 * 单击并跳转页面分页规则
 */
private Integer crawlerHelpNextPagingSize =
    Integer.parseInt(resourceBundle.getString("crawler.help.nextPagingSize"));
```

画面4：
```java
/**
 * CrawlerHelper 贝恩
 */
@Bean
public CrawlerHelper getCrawlerHelper() {
    CookieHelper cookieHelper = getCookieHelper();
    CrawlerHelper crawlerHelper = new CrawlerHelper();
    DataValidataCallBack dataValidataCallBack = getDataValidataCallBack(cookieHelper);
    crawlerHelper.setDataValidataCallBack(dataValidataCallBack);
    return crawlerHelper;
}
```

画面5：
```java
/**
 * CrawlerProxyProvider 贝恩
 */
@Bean
public CrawlerProxyProvider getCrawlerProxyProvider() {
    CrawlerProxyProvider crawlerProxyProvider = new CrawlerProxyProvider();
    crawlerProxyProvider.setUsedProxyIp(isUsedProxyIp);
    return crawlerProxyProvider;
}
```

画面6：
```java
/**
 * CrawlerConfigProperty 贝恩
 */
@Bean
public CrawlerConfigProperty getCrawlerConfigProperty() {
    CrawlerConfigProperty property = new CrawlerConfigProperty();
    //初始化URL列表
    property.setInitCrawlerUrlList(getInitCrawlerUrlList());
    //初始化xpath表达式
    property.setInitCrawlerXpath(getInitCrawlerXpath());
    return property;
}
```

画面7：
```java
/**
 * CrawlerConfigProperty 贝恩
 */
@Bean
public CrawlerConfigProperty getCrawlerConfigProperty() {
    CrawlerConfigProperty property = new CrawlerConfigProperty();
    //初始化URL列表
    property.setInitCrawlerUrlList(getInitCrawlerUrlList());
    //初始化xpath表达式
    property.setInitCrawlerXpath(getInitCrawlerXpath());
    return property;
}
```

画面14：
```java
// 11[Class="clearfix"] /div[Class=" list_con"] /div[Class=" list_userbar"] /dd[Class="name"] /a
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

