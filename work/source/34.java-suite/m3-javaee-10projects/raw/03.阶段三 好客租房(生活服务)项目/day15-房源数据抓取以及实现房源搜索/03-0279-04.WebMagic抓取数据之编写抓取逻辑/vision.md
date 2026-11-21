# 画面线理解：04.WebMagic抓取数据之编写抓取逻辑

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\04.WebMagic抓取数据之编写抓取逻辑【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:17, 02:43, 04:04, 05:08, 06:08, 07:17, 08:10, 09:44, 11:29, 12:31, 13:33, 14:30, 15:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:02:24

1) 这一组画面整体在讲如何使用 WebMagic 框架编写爬虫程序，分别演示了 GitHub 仓库页面爬取和链家网租房页面爬取的代码实现与调试过程。

2) 按时间顺序列出每张画面的要点：
画面 1：
要点：展示 GitHubRepoPageProcessor.java 文件，其中定义了从 GitHub 页面提取仓库名称和 README 内容的逻辑。代码中使用了 .regex() 提取链接，.xpath() 提取标题和内容。
代码：
```java
package cn.itcast.es.wm;
import ...
public class GithubRepoPageProcessor implements PageProcessor {
    @Override
    public void process(Page page) {
        page.addTargetRequests(page.getHtml().links().regex("(https://github.com/[\\w|-]+/[\\w|-]+)").all());
        page.putField(key, "author", page.getHtml().xpath("https://github.com/(\\w+)/.*").toString());
        if (page.getResultsItems().get("name") != null)
            page.setSkip(true);
        page.putField(key, "readme", page.getHtml().xpath("//div[@id='readme']//tidyText()"));
    }
    @Override
    public Site getSite() { return site; }
}
```

画面 2：
要点：展示 LianjiaPageProcessor.java 文件，其中定义了主方法用于启动爬虫，目标 URL 为 github.com/code4craft。
代码：
```java
import us.codecraft.webmagic.processor.PageProcessor;
public class LianjiaPageProcessor implements PageProcessor {
    private Site site = Site.me().setRetryTimes(3).setSleepTime(1000).setTimeOut(10000);
    @Override
    public void process(Page page) {
    }
    @Override
    public Site getSite() {
        return site;
    }
    public static void main(String[] args) {
        Spider.create(new GithubRepoPageProcessor()).addUrl("https://github.com/code4craft").thread(5);
    }
}
```

画面 3：
要点：展示链家网租房页面，同时在浏览器开发者工具中查看页面元素结构，定位到 .content_list-item-title 类的 a 标签，用于后续爬取。

画面 4：
要点：继续在开发者工具中查看页面元素，聚焦于 .content_list-item-title 类的 a 标签，确认其为列表项标题。

画面 5：
要点：展示链家网某房源详情页，同时在开发者工具中查看页面元素结构，定位到 .content_title 类的 p 标签，用于提取标题。

画面 6：
要点：在 IntelliJ IDEA 中编辑 LianjiaPageProcessor.java，使用 xpath 提取 .content_list-item-title 类的 p 标签内的文本内容。
代码：
```java
Selectabl xpal = html.xpath("//p[@class='content_title']/text()");
```

画面 7：
要点：在开发者工具中查看页面元素，聚焦于 .content_list-item-title 类的 a 标签，确认其为列表项标题。

画面 8：
要点：在 IntelliJ IDEA 中编辑 LianjiaPageProcessor.java，定义了提取标题、租金、类型、信息和图片的 xpath 表达式。
代码：
```java
String title = html.xpath("//p[@class='content_title']/text()").toString();
page.putField(key, "title", title);
page.putField(key, "rent", html.xpath("//p[@class='content_aside-title']//span/text()").toString());
page.putField(key, "type", html.xpath("//p[@class='content_article_table']//allText()").toString());
page.putField(key, "info", html.xpath("//div[@class='content_article_info']//allText()").toString());
page.putField(key, "img", html.xpath("//div[@class='content_article_slide_item']//img").toString());
```

画面 9：
要点：在 IntelliJ IDEA 中编辑 LianjiaPageProcessor.java，添加分页爬取逻辑，循环添加下一页 URL。
代码：
```java
// 分页连接
for (int i = 1; i <= 100; i++) {
    page.addTargetRequest(requestString: "https://sh.lianjia.com/zufang/pg" + i);
}
page.addTargetRequest(requestString: "https://sh.lianjia.com/zufang/pg");
```

画面 10：
要点：在 IntelliJ IDEA 中调试 LianjiaPageProcessor.java，查看页面请求和 HTML 内容，确认页面结构。
代码：
```java
// 源码详情读取
List<String> list = html.css(selector: ".content_list-item-title a").links().all();
page.addTargetRequests(list);
```

画面 11：
要点：在 IntelliJ IDEA 中调试 LianjiaPageProcessor.java，查看页面请求和 HTML 内容，确认页面结构。
代码：
```java
String title = html.xpath("//div[@class='content clear w1150']/p/text()").toString();
page.putField(key, "title", title);
```

画面 12：
要点：在 IntelliJ IDEA 中调试 LianjiaPageProcessor.java，查看页面请求和 HTML 内容，确认页面结构。
代码：
```java
// 源码详情读取
List<String> list = html.css(selector: ".content_list-item-title a").links().all();
page.addTargetRequests(list);
```

画面 13：
要点：在 IntelliJ IDEA 中调试 LianjiaPageProcessor.java，查看页面请求和 HTML 内容，确认页面结构。
代码：
```java
// 分页连接
for (int i = 1; i <= 100; i++) {
    page.addTargetRequest(requestString: "https://sh.lianjia.com/zufang/pg" + i);
}
page.addTargetRequest(requestString: "https://sh.lianjia.com/zufang/pg");
```

画面 14：
要点：在 IntelliJ IDEA 中调试 LianjiaPageProcessor.java，查看页面请求和 HTML 内容，确认页面结构。
代码：
```java
String title = html.xpath("//div[@class='content clear w1150']/p/text()").toString();
page.putField(key, "title", title);
```

3) 无。

4) 无。

5) 无。
