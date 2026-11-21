# 画面线理解：05.WebMagic抓取数据之编写Pipeline处理数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\05.WebMagic抓取数据之编写Pipeline处理数据【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:44, 01:27, 02:07, 02:43, 03:13, 03:56, 04:31, 05:29, 05:59, 06:50, 07:16, 08:06, 08:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:03:11

1) 这一组画面整体在讲如何使用 WebMagic 框架编写爬虫程序，从链家网抓取房源信息并保存为 JSON 文件和图片。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 `LianjiaPageProcessor.java` 中的 `process` 方法，用于从 HTML 页面中提取标题、租金、户型、朝向、图片等信息，并调用 `page.putField` 存储。
画面 2: 展示了 `MyPipeline.java` 中的 `process` 方法，用于处理抓取到的数据，创建 `Map<String, Object> data` 并进行字段赋值。
画面 3: 在 `LianjiaPageProcessor.java` 中，添加了判断逻辑：如果提取到的标题为空，则调用 `page.setSkip(true)` 跳过当前页面。
画面 4: 在 `MyPipeline.java` 中，对 `info` 字段进行解析，提取“看房”和“楼层”信息，并分别存入 `time` 和 `floor` 字段。
画面 5: 在 `MyPipeline.java` 中，继续处理 `info` 字段，提取“看房”和“楼层”信息。
画面 6: 在 `MyPipeline.java` 中，添加了下载图片的逻辑，使用 `this.downloadFile` 下载图片并保存到指定路径，同时将图片信息存入 `data`。
画面 7: 在 `MyPipeline.java` 中，将 `data` 转换为 JSON 字符串，并写入 `F:\code\data.json` 文件。
画面 8: 展示了链家网房源详情页的网页截图，包含房屋基本信息和配套设施。
画面 9: 在 `MyPipeline.java` 中，对 `image` 字段进行处理，提取图片 URL。
画面 10: 在 `MyPipeline.java` 中，对 `image` 字段进行处理，提取图片 URL。
画面 11: 展示了下载图片的进度条，显示已下载 48%。
画面 12: 展示了下载完成后的 `images` 文件夹，其中包含两张图片文件。
画面 13: 展示了 `data.json` 文件在 JSON Viewer 中的结构，包含 `image`、`orientation`、`houseType`、`rentMethod`、`title`、`url` 等字段。
画面 14: 展示了 `data.json` 文件在 EditPlus 编辑器中的内容，包含多个房源的 JSON 数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public void process(Page page) {
    Html html = page.getHtml();
    // 房源详情页
    List<String> list = html.css(selector: ".content_list-item-title a").links().all();
    page.addTargetRequests(list);
    String title = html.xpath("//div[@class='content clear w150']/p/text()").toString();
    page.putField(key: "title", title);
    page.putField(key: "rent", html.xpath("//p[@class='content_aside-title']/span/text()").toString());
    page.putField(key: "type", html.xpath("//p[@class='content_article_table']/allText()").toString());
    page.putField(key: "info", html.xpath("//div[@class='content_article_slide_item']/img").toString());
}
```

画面 2:
```java
import us.codecraft.webmagic.ResultItems;
import us.codecraft.webmagic.Task;
import us.codecraft.webmagic.pipeline.Pipeline;

public class MyPipeline implements Pipeline {
    @Override
    public void process(ResultItems resultItems, Task task) {
        StackOverflowError (java.lang)
        StringIndexOutOfBoundsException (java.lang)
        GithubRepoPageProcessor (cn.itcast.es.wm)
        LianjiaPageProcessor (cn.itcast.es.wm)
        sout
        Prints a string to System.out
        soutp
        Prints a formatted string to System.out
        soutp
        Prints method parameter names and values to System.out
        soutv
        Prints a value to System.out
    }
}
```

画面 3:
```java
if (page.getResultItems().get("title") == null) {
    page.setSkip(true);
}
```

画面 4:
```java
data.put("title", resultItems.get("title")); //标题
data.put("rent", resultItems.get("rent")); //租金
String[] types = StringUtils.split(resultItems.get("type"), ' '); //户型
data.put("rentMethod", types[0]); //租赁方式
data.put("houseType", types[1]); //户型，如：2室1厅1卫
data.put("orientation", types[2]); //朝向
String[] infos = StringUtils.split(resultItems.get("info"), separatorChar: ' ');
for (String info : infos) {
    if (StringUtils.startsWith(info, prefix: "看房：")) {
        data.put("time", StringUtils.split(info, separatorChar: ':')[1]);
    } else if (StringUtils.startsWith(info, prefix: "楼层：")) {
        data.put("floor", StringUtils.split(info, separatorChar: ':')[1]);
    }
}
```

画面 5:
```java
String image = StringUtils.split(resultItems.get("img"), separatorChar: '"')[3];
String newName = StringUtils.substringBefore(StringUtils.substringAfterLast(resultItems.getRequest().getUrl(), separator: "/"), separator: ".");
```

画面 6:
```java
try {
    this.downloadFile(imageUrl, new File(pathname: "F:\code\images\\" + newName));
    data.put("image", newName);
    String json = MAPPER.writeValueAsString(data);
    FileUtils.write(new File(pathname: "F:\code\data.json"), data: json + "\n", encoding: "UTF-8", append: true);
} catch (Exception e) {
    e.printStackTrace();
}
```

画面 7:
```java
String json = MAPPER.writeValueAsString(data);
FileUtils.write(new File(pathname: "F:\code\data.json"), data: json + "\n", encoding: "UTF-8", append: true);
```

画面 8: 无代码。

画面 9:
```java
String image = StringUtils.split(resultItems.get("img"), separatorChar: '"')[3];
String newName = StringUtils.substringBefore(StringUtils.substringAfterLast(resultItems.getRequest().getUrl(), separator: "/"), separator: ".");
```

画面 10:
```java
String image = StringUtils.split(resultItems.get("img"), separatorChar: '"')[3];
String newName = StringUtils.substringBefore(StringUtils.substringAfterLast(resultItems.getRequest().getUrl(), separator: "/"), separator: ".");
```

画面 11: 无代码。

画面 12: 无代码。

画面 13:
```json
{
    "image": "SH210919638597144832.jpg",
    "orientation": "10m",
    "houseType": "2室1厅1卫",
    "rentMethod": "整租",
    "title": "整租",
    "url": "https://sh.lianjia.com/zu/SH210919638597144832.html"
}
```

画面 14:
```json
{
    "image": "SH213046324401363916.jpg",
    "orientation": "33m",
    "houseType": "1室1厅1卫",
    "rentMethod": "整租",
    "title": "整租",
    "url": "https://sh.lianjia.com/zu/SH213046324401363916.html"
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
