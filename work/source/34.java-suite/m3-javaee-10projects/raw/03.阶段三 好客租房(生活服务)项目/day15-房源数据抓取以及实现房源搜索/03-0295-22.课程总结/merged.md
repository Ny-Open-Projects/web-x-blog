# 22.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\22.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 4分15秒（音频 255s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程内容呢做一个总结那么首先第一个呢今天我们讲的是webmagic的一个爬虫的一个编写那通过它呢就可以去抓取一些我们想要的一些好那么我们接着继续往下面看然后呢下面呢我们是具体的这个实现我们就不说了也希望大家能够动手呢去写一下这个的实现OK然后呢我们是在我们抓完数据之后啊那我们就会把我们的图片的去上传到
[00:28] OSS这个服务中这是第一个点然后我们在上传完成之后把数据导入到我们的elac设置然后导入之前先去做一个IK分子器的一个设置因为前面我们集群并没有添加IK分子器我们做了一个IK分子器的添加然后我们又去定义了我们的一个mapping定义了一个mapping然后这个里面是不是讲了这么两个字段OK然后做一个批量的导入
[00:54] 写一个代码做一个批量一个导入然后我们后面是不是就可以去开发我们的一个搜索这个功能那么开发搜索功能首先去开发我后台的一个搜索的一个接口服务OK那么在我们接口服务开发完成之后那么我们就需要去整合我们的前端去做一个开发那么在整合前端的时候会稍微麻烦一点就是在我们原有的前端的基础之上它没有一个搜索的页面需要我们自己去做一个编写这个就会稍微麻烦那么一点点
[01:23] 那么也希望大家能够动手去跟着去做一下这样的话就帮助于我们去理解前端的一些这种内容OK好那么在我们做完之后我们是不是对我们的搜索功能做了优化两个优化点一个就是高亮高亮最重要的一个点就是在我们的一个数据的一个这个就是分装的这个位置这个是一个关键点那么这个里面我们通过这个反射的一个机制去做一个实现
[01:49] 这样的话更加的通用那么当我们以后在对象中添加多些其他的一些字段的时候我们就不用去修改代码逻辑了ok也希望大家把这个技巧能去学到手好嘞那么这是这个内容然后我们是在后面是不是还学习了分页插件的一个使用ok这个就这个就其实插件用起来比较简单只是说我们的一些细节的处理包括一些内容的回显
[02:17] 一些数据的传递就是home传递到我们的设置吧对吧设置吧再去回调回去等等这个会稍显麻烦一点但它的整个使用还是比较简单的然后后面我们讲了一个功能叫热词的一个搜索那么从它的一个功能的定义到它的一个分析功能的分析然后到最后的一个实现我们都做了一站的讲解最后是不我们就会实现我们前面所说的这样的效果当你的结果比较少的时候会显示这样的一个提示出来你是不是应该去搜索
[02:46] 搜索他建议去搜索OK好那么然后最后呢我们讲了一个拼音分词那么我们可以通过拼音呢也可以去做一些搜索这样的话呢给用户的一个体验是不是就比较好一点啊但在这个里面需要大家掌握的两个点啊第一个呢就是我们在我们做缩影的时候呢可以对我们的分词器做一个定义那第二个呢就
[03:07] 就是它第二个就是在这个位置就是我们可以为我们的字段添加一个子字段然后比如说像拼音做这样的添加这个是应用比较经典这样的一个应用OK好嘞那么后面我们是不是就基于这样的应用来重新创建了我们房源的一个索引然后我们把数据是不是重新导入进去对吧
[03:29] 然后我们就可以就做一个查询了当然在我们做查询的时候还有一个点需要大家注意的就是我们希望通过多个字段的匹配的方式去做一个查询这样的话就方便我们去最终的一个高亮显示以及我们的功能就用户的一个使用的功能OK好那么通过这种方式最后我们是不是就实现了这样的一个效果那么可以看到在这个位置是多次的一个匹配OK
[03:56] 好嘞那么再说一下就是在后面这个位置就不需要去设置那个拼音高亮因为你设置他也不会去返回这个是一个小小的一个问题了OK好嘞那么这个就是我们今天的所有的一些内容OK对今天的内容的做一个总结好那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.haoke.dubbo.api.Service;
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
package cn.itcast.haoke.dubbo.api.Controller;
import cn.itcast.haoke.dubbo.api.Service.SearchService;
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
unzip Elasticsearch-analysis-pinyin-6.5.4.zip
#重新启动容器
Docker stop es-node01 es-node02 es-node03
Docker rm es-node01 es-node02 es-node03
Docker create --name es-node01 --net host -v /haoke/es-cluster/node01/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml -v /haoke/es-cluster/ik:/usr/share/Elasticsearch/plugins/ik -v /haoke/es-cluster/pinyin:/usr/share/Elasticsearch/plugins/pinyin -v /haoke/es-cluster/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4
Docker create --name es-node02 --net host -v /haoke/es-cluster/node02/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml -v /haoke/es-cluster/ik:/usr/share/Elasticsearch/plugins/ik -v /haoke/es-cluster/pinyin:/usr/share/Elasticsearch/plugins/pinyin -v /haoke/es-cluster/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4
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

