# 18_爬虫系统初始化_文档处理_文档处理实体类介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\18_爬虫系统初始化_文档处理_文档处理实体类介绍【海量资源尽在 666java.com】.mp4
- 时长 5分8秒（音频 309s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续讲刚才咱们是把这个思路给说了一下说了一下然后下面咱们去说一些前置的工作那首先呢是有两个类啊还是需要大家知道啊第一个是pass item那这个类呢其实就是定义的咱们转换后的转换后对象的股价
[00:20] 那这个类呢其实已经提供了啊看这里边有什么类型其实咱们之前也接触过比如说咱们现在呢是有抓取类型有正向和反向目前都是正向当然也有反向啊后期还会再说还有抓取文档的类型咱们也会去设置还有渠道的名称初始化的URL像这些都会去获取是吧还有一些需要处理需要处理的内容获取需要处理的内容这是content
[00:48] 然后呢下面还有一些东西再看啊这还有一个类叫color path item其实它这个类呢是继承了当前上面这个类叫path item然后这个类呢其实就是最终怎么样获取的内容的信息比如说咱们还是打开这个空间比如说你去找了一篇文章这个文章是不是咱们要抓取的目标文章呢那这个文章里边的像些标题是吧嗯但这个文章还内容比较少咱们再换一个啊标题啊
[01:19] 比如说作者信息啊这里边好像都没有信息是吧咱们再换一个好吧换一个啊就拿这个来说吧好吧拿这个来说啊比如说他的作者信息文章信息还有什么呢内容时间是吧咱们这些呢都要去抓去还有图片啊还有图片当然内容里边其实也包含了图片信息对吧
[01:44] OK那这个呢其实就是咱们的一个最终啊最终要去解析的一些东西比如说说明博客一晚二是吧嗯这一晚二呢其实就是这个一晚二是吧然后呢再往下看个人空间的标签的策略啊标题啊类型啊文档类型副标题作者还有日期阅读量评论数量简单量其实这些咱们都要抓取是吧图文的内容压缩后的内容因为内容有可能会比较多所以说咱们有可能会进行压缩
[02:10] 用压缩啊是咱们之前去展示文章的时候啊其实已经说了咱们有一个解压和一个压缩的一个工具类大家还有一些吧OK啊那这个呢其实咱们在这呢也可以进行压缩行那这个呢其实就是要最终要解析文章的一些字段这个字段呢咱们要会去用当前这个类去进行封装好好再往下看啊这里边就还有一个类大家也要熟悉要熟悉啊这个呢叫password
[02:41] 那这是干嘛的呢这就是来去抓取那种规则的封装规则的封装那什么规则呢你看啊这里边是有首先呢是要有一个field咱们还是打开某一篇文章直接去右键打开框架原代码来然后这里边内容呢你可以看一下比如说我要去找到它的一个标题啊比如这就是标题那这个标题的话你看我要去封装封装的字段啥呢这就是封装的字段咱们要封装的字段啊然后规则啥呢
[03:11] 规则的话咱们现在都是用比如说用Xpass或者JSuperOK咱们现在都是用Xpass用那个外包妈这个提供的我Xpass去定位当前这个路径比如说我要去找到当前的问题这时候咱们就可以去定位比如说DIV下面的这东西然后下面是有一个DIV这个比如说下面还有一个H1是吧然后咱们就可以获取这个内容这个内容其实就是啥
[03:41] 这个内容其实就是当前的标题就是当前的标题行那这个就是获取标题的方式咱们可以通过当前这么去定位去找到他的文本内容最终是保存就可以了好吧下面还有还有一些解析的规则是吧还有规则其实这个都是一些教研的这个是教研规则这是真正解析的规则好吧
[04:09] 行那这个咱们一会去用的时候大家可能会好一些可能会很好理解一下现在咱们就先说到这然后咱们主要是通过当前最终URL去获取内容好简单说一下再去说一下刚才咱们是有三个类是吧第一个类就是说咱们是封装了一些文档的一些类型比如说你要是正向还有什么类型是文档什么类型还有什么频道然后下面第二个类这个类就是最终你要去解析的字段
[04:38] 都是封装到了当前这个类中啊然后再去保存数据雇杀的啊现在最后最后啊咱们都是用当前这个类这个类里边的一些属性去封装咱们最重要解析的内容那还有一个就是这个呢就是来去干嘛来去怎么去找到你的内容啊就是封装了一些规则封装了一些规则啊那行那这三个类啊咱们就说完了啊然后下面呢咱们就真正的去写一些代码写一些代码然后呢再去再去设一些配置好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解爬虫项目中文档处理模块的代码结构，包括解析实体类 ParseItem 和解析规则类 ParseRule 的定义与实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档处理模块的章节标题“6.3 文档处理”，并列出三个处理步骤：解析初始URL、解析列表页、解析最终URL。同时显示了抽象类 ParseItem 的代码结构，包含字段如 handleType、documentType、channelName，以及抽象方法 getInitialUrl() 和 getParserContent()。
画面2：聚焦于 ParseItem 抽象类中的 getInitialUrl() 方法，其注释说明“获取初始的URL”，并显示了该方法的抽象定义。
画面3：浏览器页面空白，无实质内容。
画面4：显示 CSDN 博客文章《阅读目录（置顶）(长期更新计算机领域知识)》的目录页，包含多个技术主题的链接。
画面5：显示 CSDN 博客文章《阅读目录（置顶）(长期更新计算机领域知识)》的“微信公众号”部分，包含一个二维码和相关文章链接。
画面6：显示 CSDN 博客文章《Java常用设计模式之适配器模式》，其中包含一个结构图，展示适配器模式的六种类型：类的适配器模式、对象的适配器模式、装饰模式、代理模式、桥接模式、组合模式。
画面7：展示“对象的适配器模式”的类图，包含 Source、Targetable、Adapter、Wrapper 四个类，以及它们之间的继承和实现关系。
画面8：展示继承自 ParseItem 的 CrawlerParseItem 类的代码，包含字段如 id、summary、url、spatialUrl，并有注释说明。
画面9：展示“装饰模式”的类图，包含 SourceSub1、SourceSub2、Wrapper、WrapperTest 四个类，以及它们之间的继承和实现关系。
画面10：展示网页源代码，包含 HTML 结构和多个 <a> 标签，用于链接到其他文章。
画面11：展示 ParseRule 类的代码，包含字段如 field、urlValidateRegular、parseRuleType、rule、parseContentList，并有注释说明。
画面12：展示 ParseItem 抽象类中的 getHandleType() 和 getDocumentType() 方法，以及 setHandleType() 方法。
画面13：展示 ParseRule 类中 parseRuleType 字段的注释“解析规则类型”，并显示了其类型为 CrawlerEnum.ParseRuleType。
画面14：展示 ParseRule 类中 getRule()、setRule()、getParseContentList()、setParseContentList() 方法的代码实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public abstract class ParseItem implements Serializable {
    /**
     * 处理类型 有正向 反向两种
     * FORWARD 正向 REVERSE 反向
     */
    private String handleType = null;
    /**
     * 文档的类型
     */
    private String documentType = null;
    /**
     * 渠道名
     */
    private String channelName;
    /**
     * 获取初始的URL
     * @return
     */
    public abstract String getInitialUrl();
    /**
     * 获取需要处理的内容
     * @return
     */
    public abstract String getParserContent();
    public String getHandleType() {
        return handleType;
    }
```

画面2：
```java
    /**
     * 获取初始的URL
     * @return
     */
    public abstract String getInitialUrl();
```

画面8：
```java
public class CrawlerParseItem extends ParseItem {
    /**
     * 影投ID
     */
    private String id;
    /**
     * 摘要
     */
    private String summary;
    /**
     * 博客url
     */
    private String url;
    /**
     * 个人空间URL
     */
    private String spatialUrl;
```

画面11：
```java
public class ParseRule {
    /**
     * 指定字段
     */
    private String field;
    /**
     * URL 校验规则
     */
    private String urlValidateRegular;
    /**
     * 解析规则类型
     */
    private CrawlerEnum.ParseRuleType parseRuleType;
    /**
     * 规则
     */
    private String rule;
    /**
     * 指定内容列表
     */
    private List<String> parseContentList;
```

画面14：
```java
    public String getRule() {
        return rule;
    }
    public void setRule(String rule) {
        this.rule = rule;
    }
    public List<String> getParseContentList() {
        return parseContentList;
    }
    public void setParseContentList(List<String> parseContentList) {
        this.parseContentList = parseContentList;
    }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：
标题：“3 Java常用设计模式之适配器模式”
结构图：
(1) 适配器模式
├── 类的适配器模式
├── 对象的适配器模式
├── (2)装饰模式
├── (3)代理模式
├── (4)桥接模式
├── (5)桥接模式
└── (6)组合模式

画面7：
结构图：
Source
├── method1()
└── method2()
Targetable
├── method1()
└── method2()
Adapter
└── method1()
└── method2()
Wrapper
└── method1()
└── method2()

画面9：
结构图：
SourceSub1
└── method1()
SourceSub2
└── method2()
Wrapper
└── method1()
└── method2()
WrapperTest
└── method1()
└── method2()

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

