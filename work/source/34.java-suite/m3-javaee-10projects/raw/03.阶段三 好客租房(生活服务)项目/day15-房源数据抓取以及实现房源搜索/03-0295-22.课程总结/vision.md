# 画面线理解：22.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\22.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:17, 00:39, 00:54, 01:10, 01:33, 01:59, 02:10, 02:34, 02:51, 03:01, 03:20, 03:32, 04:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:14:19

1) 这一组画面整体在讲什么（一句话）：
使用 WebMagic 框架抓取链家房产数据，并通过 Elasticsearch 实现搜索功能优化，包括高亮、分词和拼音支持。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 课程介绍页，说明使用 WebMagic 抓取链家数据，目标网站为上海链家网。
画面 2: 展示了 `LianjiaPageProcessor` 类的 Java 代码，用于解析页面并提取标题、类型、信息等字段。
画面 3: 展示了在终端中解压 Elasticsearch 压缩包的命令：`cd /haoke/es-cluster/` 和 `#将IK的zip压缩包解压到该目录`。
画面 4: 展示了使用 REST 客户端向 Elasticsearch 发送数据的 Java 代码片段，包含循环和请求处理逻辑。
画面 5: 展示了链家网站的房源搜索页面截图，包含房源信息和价格。
画面 6: 展示了 Elasticsearch 的 Java API 包导入和搜索结果类导入。
画面 7: 展示了处理 Elasticsearch 搜索结果的 Java 代码，包括字段写入和高亮处理。
画面 8: 展示了课程目录页，当前章节为“3、整合搜索功能”。
画面 9: 展示了 `SearchController` 的 Java 代码，包含 REST 控制器注解和依赖注入。
画面 10: 展示了使用 Docker 创建 Elasticsearch 节点的命令。
画面 11: 展示了 Elasticsearch 中 `highlight` 字段的 JSON 结构示例。
画面 12: 展示了为 Elasticsearch 索引设置分片数量的 PUT 请求。
画面 13: 展示了 Elasticsearch 搜索结果的 JSON 格式，包含高亮字段和源数据。
画面 14: 展示了搜索框中输入“东fang”的搜索结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.Site;
import us.codecraft.webmagic.Spider;
import us.codecraft.webmagic.processor.PageProcessor;

public class LianjiaPageProcessor implements PageProcessor {
    private Site site = Site.me().setRetryTimes(3).setSleepTime(200);

    @Override
    public void process(Page page) {
        Html html = page.getHtml();
        page.addTargetRequests(html.css(".content_list-item-title a").links());
        page.putField("title", html.xpath("//div[@class='content clear w150']/p/text()").toString());
        page.putField("type", html.xpath("//p[@class='content_aside--title']/span/text()").toString());
        page.putField("info", html.xpath("//div[@class='content_article_table']/allText()").toString());
        page.putField("img", html.xpath("//div[@class='content_article_slide_item']/img").toString());
    }
}
```

画面 3:
```bash
cd /haoke/es-cluster/
#将IK的zip压缩包解压到该目录
#将Docker容器启动
```

画面 4:
```java
"UTF-8";
String createStr = "{ \"index\": { \"_index\": \"haoke\", \"_type\": \"house\" } }";
StringBuilder sb = new StringBuilder();
int count = 0;
for (String line : lines) {
    sb.append(createStr + "\n" + line + "\n");
    if (count >= 100) {
        request.setEntity(sb.toString());
        Response response = this.restClient.performRequest(request);
        System.out.println("请求完成：" + response.getStatusLine());
        System.out.println(EntityUtils.toString(response.getEntity()));
        count = 0;
        sb = new StringBuilder();
        count++;
    }
}
```

画面 6:
```java
package cn.itcast.haoke.dubbo.api.service;
import cn.itcast.haoke.dubbo.api.vo.HouseData;
import cn.itcast.haoke.dubbo.api.vo.SearchResult;
```

画面 7:
```java
searchHit.getId(), true);
} catch (IllegalAccessException e) {
    e.printStackTrace();
}
Map<String, Object> sourceAMap = searchHit.getSourceAsMap();
sourceAMap.entrySet();
for (Map.Entry<String, Object> entry : sourceAMap.entrySet()) {
    Field field = Fieldutils.getField(clazz, entry.getKey(), true);
    if (null == field) {
        continue;
    }
    try {
        Fieldutils.writeField(obj, entry.getKey(), entry.getValue(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
}
// 处理高亮
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    // 处理高亮字段
}
```

画面 9:
```java
package cn.itcast.haoke.dubbo.api.controller;
import cn.itcast.haoke.dubbo.api.service.SearchService;
import cn.itcast.haoke.dubbo.api.vo.SearchResult;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.io.UnsupportedEncodingException;
import java.util.Set;
@RequestMapping("search")
@RestController
@CrossOrigin
public class SearchController {
    private static final Logger LOGGER = LoggerFactory.getLogger(SearchController.class);
    @Autowired
    private SearchService searchService;
    @Autowired
    private RedisTemplate redisTemplate;
}
```

画面 10:
```bash
#解压压缩包，解压到/haoke/es-cluster/pinyin
unzip elasticsearch-analysis-pinyin-6.5.4.zip
#重新启动容器
docker stop es-node01 es-node02 es-node03
docker rm es-node01 es-node02 es-node03
docker create --name es-node01 --net host -v /haoke/es-cluster/node01/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /haoke/es-cluster/ik:/usr/share/elasticsearch/plugins/ik -v /haoke/es-cluster/pinyin:/usr/share/elasticsearch/plugins/pinyin -v /haoke/es-cluster/data:/usr/share/elasticsearch/data elasticsearch:6.5.4
docker create --name es-node02 --net host -v /haoke/es-cluster/node02/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /haoke/es-cluster/ik:/usr/share/elasticsearch/plugins/ik -v /haoke/es-cluster/pinyin:/usr/share/elasticsearch/plugins/pinyin -v /haoke/es-cluster/data:/usr/share/elasticsearch/data elasticsearch:6.5.4
```

画面 11:
```json
{
    "start_offset": 0,
    "end_offset": 0,
    "type": "word",
    "position": 1
},
{
    "token": "hua",
    "start_offset": 0,
    "end_offset": 0,
    "type": "word",
    "position": 2
}
```

画面 12:
```json
PUT http://192.168.1.7:9200/haoke/
{
    "settings": {
        "number_of_shards": 6
    }
}
```

画面 13:
```json
{
    "highlights": {
        "fields": {
            "title": []
        }
    }
}
```

画面 14:
```java
.withHighlightFields(new HighlightBuilder.Field("title")) // 设置高亮
.build();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“课程介绍”，内容包括“编写爬虫抓取房源数据”、“开发搜索引擎接口服务”、“整合前端开发实现搜索功能”、“优化搜索功能增加高亮和分页功能”、“热词搜索功能实现”、“拼音分词”。
画面 6: 标题为“4、优化搜索功能”，子标题“4.1、高亮”。
画面 8: 标题为“3、整合搜索功能”，子标题“3.1、整合搜索功能”。
画面 12: 标题为“6.3、房源索引增加拼音支持”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
