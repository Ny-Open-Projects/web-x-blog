# 画面线理解：19_爬虫数据解析保存_文章保存1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\19_爬虫数据解析保存_文章保存1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:20, 03:13, 04:36, 05:44, 07:31, 07:57, 09:15, 10:17, 11:01, 12:33, 13:53, 14:37, 15:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:12:34

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
