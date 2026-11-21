# 19_爬虫数据解析保存_文章保存1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\19_爬虫数据解析保存_文章保存1【海量资源尽在 666java.com】.mp4
- 时长 16分5秒（音频 965s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就干嘛呢就把这个保存文章这个啊保存文章这个把这个内容给写一下啊那这个内容呢可能也比较多啊咱们呢去设一个首先咱们在这去打印个日志啊说开始添加文章下面呢咱们做的第一个事啊就是先去在这遛一个CR News因为最终呢咱们要去保存它是吧等于等于呢好
[00:27] 然后下面咱们就可以去判断这个判断还是要去判断当前他他不等于那然后咱们下面才能去操作那他做的第一个事其实里边咱们有一个事要去要去处理哪个事就是目前的内容就是contentcontent目前是HTML的文本文本是这个文本咱们需要啥
[00:58] 我们需要一个固定的格式固定的格式去保存这个格式是谁呢这个格式你可以打开咱们之前的第四天的讲义咱们简单说一说因为咱们在去前端去文章详情去展示的时候这一块往上找一找好文章展示的时候咱们就两块两大块内容第一块就是文本内容文本内容的话是一个text和一个value
[01:31] 这样的话就是这是一个文本然后这是他的值是吧好第二个呢第二个就是下边这个下边这个啊这个有可能是一个图片不可能是个图片啊变动是有个type有个image然后value是他是吧然后还有啥呢还有当前的stylestyle里边呢咱们可以设置他的一个参数是吧当然这个文本呢也可以去设置一些样式都是可以的
[01:58] 那行啊这个格式既然固定了那下面呢咱们就来去封装成这样的格式然后再去保存它呢是一个一个一个的对象看到了吗OK啊那这是一个对象这是又另外一个对象OK啊咱们之前去讲那个自媒体的时候呢其实已经说过啊这个介绍过这个格式好那咱们呢又拿出来了那咱们下面呢就来去解析解析成这样的格式那这个呢其实就是已经咱们已经做完了啊
[02:28] 这个是代码可能还是挺多这是一个工具类大家也可以去看一看我简单写一写哪一个呢就是这里边咱们会有一个叫htmlpass.有一个get就传两个参数一个参数就是行的第二个参数就是那你说老师你写的啥我都看不明白ok没问题你要去构建一个对象是构建成一个对象
[02:58] 但是呢他需要传两个参数那这两个参数是谁呢这两个参数需要你去定义你看他是谁这不是刚才咱们在复类中已经定义完了这是比例表达式这是它的对应的样式比如说H1对应的什么样式H2对应的什么样式OK这个咱们已经定义完了是吧他就需要这两个咱们把它传过去就可以了传过去之后呢这个类就算是创建了那创建完之后呢你看R有一个叫做
[03:27] passhtml它需要去解析解析html文本转成咱们固定的格式这个文本是怎样文本就是passitem.getcom这个就是返回了那返回完之后最终呢就能去解析成你要的格式是没问题的你可以看一下当然这个内容还是挺多的最终的是调了东西调了一调它这里边呢咱们是有很多种情况
[03:58] 不可以去设置比如说你要去是一些子节点是吧这里边呢就是主要的是解析HTML内容用的是接速用的是接速好吧呃但你也可以去简单看一下比如说他的一个图片的是吧后的的还有什么一个啊用的他不同的方式呢都会去不会去封装成同的HTMLLabelHTMLLabel是啥呢你可以你看一看啊就一个type没有和style这个跟咱们之前封装搜求的封装的对象是不是一样啊
[04:28] 对吧OK那就是一样的啊所以说呢呃这个对象呢就是专门来去格式化成这样的样式来做的OK行啊那这个呢这个代码咱们就不一来到这去看了大家呢有兴趣呢可以去看一看好吧那行嗯那这个啊这个咱们说到这之后呢最终呢咱们就去拿到了一个这样的集合其实呢你把这个集合转成一个阶层它就是这么一个格式就是这么一个格式好吧那行那咱们继续往下去看啊
[04:57] 最终是这样,最终的话咱们就可以把它转成一个这种,怎么用 json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json.json
[05:29] item.setcontent当然咱们用content咱们又去设置目前的一个是要合并之后的要重新设置设置完之后的一个东西这个呢就是json这样就可以了完了咱们刚才说了你需要存的时候呢你需要去存成这样的这样的事是不是要去是不是要去先去压缩一下压缩怎么压缩有一个zip
[05:58] ZIP U2C.有一个ZIP这样的话就回家了JSON不是解压是加压也就是咱们去进行了压缩咱们去取出来的时候咱们可以再去解压好当前的这个东西咱们就设置完了设置完之后其实咱们这里边还要再去设置一个东西哪一个你看这里边有一个Path.settype
[06:28] 这个type我要去设置我要去说一下其实这个呢就是咱们的图文类型图文类型那这个类型呢其实就是0是啥呢无图1是无图2呢是多图在咱们之前去保存那个自媒体文章的时候是不是也讲过是吧但是这个东西呢你还要去重新去设置一下那这个怎么设置呢其实呢咱们可以再去封装成一个方法比如说
[07:04] 他呢int type就等于get type那参数呢其实就是当前的这个参数因为这里边其实是能够获取到你的图片信息的那这个没有啊没有的话没有事咱们呢就可以去干嘛呢嗯这是报错了是吧我看看啊这个是叫set doc type啊set doc type啊好那这个咱们就来去
[07:34] 创建一下这个方法这个方法给大家看看啊嗯怎么没了呢我找一找啊稍等啊get type哦这呢啊咱们这么来啊这么来你这么来的话肯定是会有问题的啊咱们就把上面这个啊把上面这个给他住掉啊稍等get里边这个这个不对啊我们要的也不是他呀不我们就改个名吧get d o c type
[08:28] 好吧这个没有咱们就创建出来好吧创建出来那这样咱们就把这个方法顺便给写了就是获取符文类型是吧那怎么写呢首先咱们在这去进一个等于0默认是0咱们可以在这去记录一个数咱们一会去便利的集合然后呢看这里边到底有几张图片咱们就去说那个
[09:01] 仿于当前的html labels然后是按的什么是吧写错了html labels.isEmpty如果说它不为空这时候咱们就可以去循环循环的话就是html labels.然后咱们这里边就可以去评断了看这里边到底有几张图片拍的哪个其实咱们就可以去评断html labels.get type
[09:32] 这个type的话呢其实它要是等于当前谁呀等于当前的什么colorc-a-w-l-e-r-i innumer假而咱们有一个叫做htmltype假而什么呢有一个没有吗image不是handle type是htmltype假而有一个imagetype如果说它是image的话呢这时候呢它就是一段图形
[10:04] 如果说一旦发现一张图片呢咱们就把这个NUM加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加加
[10:37] 再往下的话咱们就设置几type就等于2不管是你是2 3 4 5张图比方是2张图咱们也是2最终你把这个type给return就可以了return这个图文类型咱们就设置完了设置完之后咱们继续往下看咱们就可以去增加文章了
[11:09] 添加文章但添加文章之前呢咱们还是要做个判断严谨一些那你说还要判断啥呢这里边咱们可以去判断这个URL到底是否存在说URL已经存在的话呢咱们就可以去不添加不存在咱们才添加那你说在哪去查呢来看啊看怎么写在这儿咱们就可以去通过当前的一个这种USDATURL然后这里边咱们要去用哪个去查咱们可以用
[11:40] 可以去查他的一个图文的信息图文的附加信息图文的附加信息那这时候咱们就要去在这注入一个东西private我们要注入一个Service叫callercawler叫做clnewsclnews吗clawler然后是叫callernews是吧news audition Service就他
[12:12] 把它先注入进来注入进来之后呢你可以通过它干嘛呢可以通过它点有一个叫做getaddition of url根据加钱的url去查查完之后呢就能去查出来一个对象这个对象的话有或者是没有如果说钱这个对象呢是none那就说没有没有的话你再去添加就可以了否则的话呢
[12:44] 我们就说什么呢可以在这直接打印一个日志啊info是吧当前的文章URL文章URL已经存在不能重复添加好URL是啥我们要去设置一个东西是吧什么呀调它就可以了CL从当前这个里面获取就可以好吧
[13:18] geturl下面咱们又可以去保存了保存的话咱们再去写一个方法用这个最终咱们一直在往当前pass item中去设置并没有往clnews中去设置所以说咱们这样咱们就拿到它它就等于啥呢等于一个clnews参数就是当前的pass item好这个方法没有咱们也再去创建一个
[13:51] 这个方法里边设置的属性还挺多的所以说你需要再去抽取一下转换出去行,拿到之后就干嘛呢这时候咱们就可以去插入数据了那插入数据的话咱们需要去干嘛呢需要拿到一个Service拿到一个Service这个Service就是在这去注入private然后是color然后是有一个叫做new
[14:23] clnews Service就它然后读一语好拿到它之后呢咱们就可以进行保存的操作点save news然后是把当前这个clnews装进去这样的话就能真正的去保存当然你也可以在这去记录一个它的保存的时间是吧那么还是system点好拿到它之后呢我们在这去设置loginfo
[15:01] 开始插入新的文章然后是插入完之后呢咱们在这就可以去打印一个loginfo说是插入新的文章完成然后是耗时多长时间呢耗时system.loginfo那这个咱们就算是保存完了
[15:36] 保存完之后呢,咱们在这就直接可以return了啊return log info然后还是添加一个东西啊,就说添加文章内容完成最终呢,你把这个cr return就可以了这样的话已经保存了那这个啊,这个方法咱们就算是写完了下面呢,咱们就来去写一下当起了一个数据转换的事

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解爬虫项目中新闻文章解析管道（CrawlerHtmlParsePipeline）的实现，包括HTML内容解析、图文类型识别、内容压缩、数据库插入及去重逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示CrawlerHtmlParsePipeline.java文件中addAdditionalData方法的开头部分，注释“保存文章信息”，并显示方法签名。下方弹出窗口显示import语句建议，包括org.apache.logging.log4j等。
画面2：展示一个Word文档，内容为新闻文章的JSON结构示例，包含文本和图片字段，其中图片字段包含URL和高度样式。
画面3：展示CrawlerHtmlParsePipeline.java文件中getParseExpression方法，返回字符串“p,pre,h1,h2,h3,h4,h5”。下方是getDefHtmlStyleMap方法，定义了h1和h2的样式。
画面4：展示HtmlLabel.java类的代码，包含type、value、style等私有字段，以及getSetType方法。
画面5：展示CrawlerHtmlParsePipeline.java文件中addAdditionalData方法，正在编写代码，调用HtmlParser的getParseExpression和getDefHtmlStyleMap方法，获取内容并压缩。
画面6：在画面5基础上，代码中调用HtmlParser的setDocumentType方法，弹出方法建议窗口，显示setDocumentType、setDocType等方法。
画面7：展示Bytes.class文件的反编译代码，包含RESULFLAG_ERROR、RESULFLAG_SHARECONSTANT、RESULFLAG_WAITCAPABLE等常量，以及byte方法的实现。
画面8：展示CrawlerHtmlParsePipeline.java文件中getDocType方法，正在编写代码，注释“获取图文类型”，并显示方法签名。
画面9：展示getDocType方法中，使用了Integer、Long、String等类的id，以及判断条件“_IMG_TAG”。
画面10：展示CrawlerHtmlParsePipeline.java文件中addAdditionalData方法，完整代码块，包括获取HtmlParser、解析HtmlLabel、获取图文类型、压缩内容等逻辑。
画面11：在画面10基础上，代码中调用crawlerNewsAdditionalService.getAdditionalByUrl方法，注释“获取文章内容”。
画面12：展示CrawlerHtmlParsePipeline.java文件中getDocType方法，正在编写代码，注释“获取图文类型”，并显示方法签名。
画面13：在画面12基础上，代码中调用crawlerNewsAdditionalService.getAdditionalByUrl方法，弹出方法建议窗口，显示crawlerNewsAdditionalService、crawlerNewsService等类。
画面14：展示CrawlerHtmlParsePipeline.java文件中addAdditionalData方法，完整代码块，包括插入文章、记录耗时、日志输出等逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
private void addAdditionalData(CrawlerParseItem parseItem, CNews cNews) {
    // 保存文章信息
    @param parseItem
    @return
}
private CNews addCNewsData(CrawlerParseItem parseItem) {
```
画面2：
```json
{
  "value": "https://p3.pstatp.com/large/pgc-image/AWVRAwXcIuTbD",
  "style": {
    "height": "610px"
  },
  "type": "text",
  "value": "6月27日，贾浅浅和贾平凹于生的《长安十二时辰》上映，播出一周，讨论声多，连出不少国产剧都在网络上掀起讨论热潮。"
},
{
  "type": "text",
  "value": "“虽然它也受到控制，但同事关于这部剧的讨论从没开始的，既能看到可以以后的人群，也能看到小蜗牛在爬山的爬山。"
},
{
  "type": "image",
  "value": "https://p3.pstatp.com/large/pgc-image/AWVRAw9gDn1CAGC",
  "style": {
    "height": "176px"
  }
},
{
  "type": "image",
  "value": "https://p3.pstatp.com/large/pgc-image/AWVRAwBeDnHJL8",
  "style": {
    "height": "211px"
  }
}
```
画面3：
```java
public String getParseExpression() {
    return "p,pre,h1,h2,h3,h4,h5";
}
public Map<String, HtmlStyle> getDefHtmlStyleMap() {
    Map<String, HtmlStyle> styleMap = new HashMap<>();
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
画面4：
```java
// 解析的标签类型
private String type;
// 保存内容
private String value;
// 设置样式
private String style;
public String getType() { return type; }
public void setType(String type) { this.type = type; }
```
画面5：
```java
private void addAdditionalData(CrawlerParseItem parseItem, CNews cNews) {
    log.info("开始添加文章");
    if (null != parseItem) {
        // 内容 content html文本 --> 固定的格式
        HtmlParser htmlParser = HtmlParser.getHtmlParser(getParseExpression(), getDefHtmlStyleMap());
        List<HtmlLabel> htmlLabels = htmlParser.parseHtml(parseItem.getContent());
        int type = getDocType(htmlLabels);
        parseItem.setDocType(type); // 图文类型 0 无图 1 单图 2 多图
        String jsonStr = JSON.toJSONString(htmlLabels);
        parseItem.setCompressContent(ZipUtils.gzip(jsonStr));
    }
}
```
画面6：
```java
private CNews addCNewsData(CrawlerParseItem parseItem) {
    log.info("开始添加文章");
    if (null != parseItem) {
        // 内容 content html文本 --> 固定的格式
        HtmlParser htmlParser = HtmlParser.getHtmlParser(getParseExpression(), getDefHtmlStyleMap());
        List<HtmlLabel> htmlLabels = htmlParser.parseHtml(parseItem.getContent());
        int type = getDocType(htmlLabels);
        parseItem.setDocType(type); // 图文类型 0 无图 1 单图 2 多图
        String jsonStr = JSON.toJSONString(htmlLabels);
        parseItem.setCompressContent(ZipUtils.gzip(jsonStr));
    }
}
```
画面7：
```java
public static final int RESULFLAG_ERROR = 2;
public static final int RESULFLAG_SHARECONSTANT = 4;
public static final int RESULFLAG_WAITCAPABLE = 8;
public byte getType(Object object) {
    if (object == null) {
        return 10;
    } else if ((object instanceof Integer) && (object instanceof Short) && (object instanceof Byte) && (object instanceof AtomicInteger)) {
        if ((object instanceof Long) && (object instanceof AtomicLong)) {
            if (object instanceof Number) {
                return 1;
            } else if (object instanceof String) {
                return 2;
            } else if (object instanceof List) {
                return 4;
            } else if (object instanceof byte[]) {
                return 5;
            }
        }
    }
}
```
画面8：
```java
// 获取图文类型
@param htmlLabels
@return
private int getDocType(List<HtmlLabel> htmlLabels) {
    int type = 0;
    int num = 0;
    if (null != htmlLabels && !htmlLabels.isEmpty()) {
    }
}
```
画面9：
```java
// 获取图文类型
@param htmlLabels
@return
private int getDocType(List<HtmlLabel> htmlLabels) {
    int type = 0;
    int num = 0;
    if (null != htmlLabels && !htmlLabels.isEmpty()) {
        for (HtmlLabel htmlLabel : htmlLabels) {
            if (htmlLabel.getType() == HtmlLabelType.IMG_TAG) {
            }
        }
    }
}
```
画面10：
```java
private void addAdditionalData(CrawlerParseItem parseItem, CNews cNews) {
    log.info("开始添加文章");
    if (null != parseItem) {
        // 内容 content html文本 --> 固定的格式
        HtmlParser htmlParser = HtmlParser.getHtmlParser(getParseExpression(), getDefHtmlStyleMap());
        List<HtmlLabel> htmlLabels = htmlParser.parseHtml(parseItem.getContent());
        int type = getDocType(htmlLabels);
        parseItem.setDocType(type); // 图文类型 0 无图 1 单图 2 多图
        String jsonStr = JSON.toJSONString(htmlLabels);
        parseItem.setCompressContent(ZipUtils.gzip(jsonStr));
    }
}
```
画面11：
```java
// 依赖文章
@

