# 画面线理解：21_爬虫系统初始化_文档处理_目标页解析规则

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\21_爬虫系统初始化_文档处理_目标页解析规则【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:08, 04:16, 05:24, 07:02, 08:50, 10:31, 12:04, 13:56, 15:44, 17:02, 18:22, 19:05, 20:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:42:32

1) 这一组画面整体在讲如何在Java爬虫项目中配置解析规则（ParseRule），通过在CrawlerConfig.java中定义XPath表达式来提取网页元素。

2) 按时间顺序列出每张画面的要点：
画面1：展示IDEA中CrawlerConfig.java文件，高亮显示了初始化解析规则的代码段，包括设置爬虫路径、帮助爬虫路径、分页大小和解析规则列表。
画面2：在CSDN博客页面，查看“支付宝沙箱接口测试”文章，用于理解支付接口相关知识。
画面3：在IDEA中，展示CrawlerConfig.java中定义目标解析规则的代码，添加了“标题”字段的解析规则。
画面4：在IDEA中，继续编辑CrawlerConfig.java，添加了“作者”字段的解析规则，XPath为“//a[@class='follow-nickname']”。
画面5：在IDEA中，继续编辑CrawlerConfig.java，添加了“发布日期”字段的解析规则，XPath为“//span[@class='time']”。
画面6：在浏览器中，使用开发者工具查看CSDN文章页面的HTML结构，定位“Java Lambda表达式详解手册及实例”文章的标题元素。
画面7：在浏览器中，打开CSDN博客“Java基础Day05”文章，准备学习方法概述。
画面8：浏览器页面空白，可能为页面加载或切换过程。
画面9：在浏览器中，打开CSDN博客“Java基础Day06”文章，准备学习Debug模式。
画面10：在浏览器中，继续查看“Java基础Day06”文章，聚焦于“1.1什么是Debug模式”部分。
画面11：在IDEA中，编辑CrawlerConfig.java，添加了“点赞数”字段的解析规则，XPath为“//div[@class='tool-box']/ul[@class='menu-list']/li[@class='btn-like-box']/button”。
画面12：在IDEA中，继续编辑CrawlerConfig.java，添加了“评论数”字段的解析规则，XPath为“//div[@class='tool-box']/ul[@class='menu-list']/li[@class='to-commentBox']/p”。
画面13：在浏览器中，使用开发者工具查看CSDN文章页面的HTML结构，定位“Java Lambda表达式详解手册及实例”文章的评论数元素。
画面14：在IDEA中，展示CrawlerConfig.java中初始化解析规则的代码段，包括设置爬虫路径、帮助爬虫路径、分页大小和解析规则列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
property.setInitCrawlerXpath(initCrawlerXpath);
property.setHelpCrawlerXpath(helpCrawlerXpath);
property.setCrawlerHelpNextPagingSize(crawlerHelpNextPagingSize);
property.setTargetParseRuleList(getTargetParseRuleList());
return property;
```

画面3：
```java
private List<ParseRule> getTargetParseRuleList() {
    List<ParseRule> parseRules = new ArrayList<ParseRule>();
    parseRules.add(new ParseRule(field: "title", CrawlerEnum.ParseRuleType.XPATH, rule: "//h1[@class='title-article']");
```

画面4：
```java
parseRules.add(new ParseRule(field: "title", CrawlerEnum.ParseRuleType.XPATH, rule: "//h1[@class='title-article']"));
```

画面5：
```java
parseRules.add(new ParseRule(field: "author", CrawlerEnum.ParseRuleType.XPATH, rule: "//a[@class='follow-nickname']");
```

画面6：
```html
<div class="article-header">
    <h1 class="article-title-box">Java Lambda表达式详解手册及实例</h1>
</div>
```

画面9：
```html
<div class="article-content">
    <div class="article-info-box">
        <span class="article-info">作者：River_x</span>
    </div>
</div>
```

画面11：
```java
parseRules.add(new ParseRule(field: "likes", CrawlerEnum.ParseRuleType.XPATH, rule: "//div[@class='tool-box']/ul[@class='menu-list']/li[@class='btn-like-box']/button"));
```

画面12：
```java
parseRules.add(new ParseRule(field: "commentCount", CrawlerEnum.ParseRuleType.XPATH, rule: "//div[@class='tool-box']/ul[@class='menu-list']/li[@class='to-commentBox']/p"));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
