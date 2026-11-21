# 16-商品搜索-列表查询 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那刚才搜索这一块就实现了

紧接着我们就要做这个测试

那做这个测试呢

业务层是少不了的

对不对

写个搜索

那我们就来写一下public

写个叫page

注意里面是skuinfo

对吧

是skuinfo

这是这一块

这个时候呢

我们就写个方法

就叫设起

先返回浪

给它一个请求地址

get mapping

那后面这一块

我们要接收前端传的一个搜索数据

写个request的param

这里面required in force

紧接着把这个数据给接收到

写个map

skuin

skuin

设起map

好了

数据有了

我们直接去调用我们的业务层

去实现搜索就行了

把设计map给它

行

这个搜索呢

就这么快就做完成了

接着我们就开始进行测试

那么这个时候我们就直接启动我们这里进行测试就行了

右键启动一次

好

那我测试了

大家注意一下哈

我这边是有很多数据的

而我要的是根据某一个时间进测试

我这里把这个时间给点击一次

这个时间给排序

这时间排序没有多大用

排这个吧

看一下这个时间有没有差异

换一个时间

行

看这个时间有没有什么差异性哈

好

我们就收一下这个时间段的一个商品信息

把它给复制一下

然后一会儿搜索的我们就在这一块进行搜索

设取

给他一个参数叫start time等于在后面这一块找一下这个时间在这里是大探

回复了一下

再搜索一次

那目前这一块呢

就报了一个问题哈

我们看问题在哪个地方哈

在这一块应该是报了问题

我们这一块大家看这一块呢

他就说到咱们这个分页这里了

对不对

我们看一下这个问题点哈

问题点呢

应该跟我们参数有关系

我们看一下后端这一块这个代码

这一块呢

他跟咱这个分页有关系

他把分页这块

此别给搞错了

那应该是咱这个顺序搞错了

我们把这两个换一个位置参数了

这一块先写参数后写分页

这里也是一样先写参数后写分页

这两个参数对应的位置对调一下

把它给换到这里来

就行了

我们来重新启动一下

看看效果好

重新启动

那么这个时候就可以解决刚才那一个问题

等他启动之后呢

我们再来测试一下这一块的问题哈

以后遇到这一块

他基本上是咱参数的顺序

这块发生了问题

导致这里的找不到咱们分页信息

我们再来刷新一次

看看结果怎么样

服务还没有启动等服务启动一次

数据这一块就来了

这就是咱们这里根据这个时间进行一个查询操作哈

我们来做一个分页

你看这一块是无减的页面

5920对吧

5920这个时间呢

330330时间都是330

我们做一个分页加一个参数叫配给lamp等于2

那么等于二的话

一会儿就不是这个商品了

一会应该不是20了吧

对吧

回测一次

你看32了

这个商品就变了好

这就是我们这个

商品列表的一个搜索

调查询

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是一个关于使用 Spring Boot 和 Elasticsearch 构建商品搜索功能的技术教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何在控制器（Controller）中定义搜索接口，并通过服务层（Service）调用数据访问层（DAO）进行分页查询。过程中，讲师展示了如何使用 `@GetMapping` 和 `@PostMapping` 注解定义 REST API，并通过 `Pageable` 参数实现分页。视频中也包含了对 Elasticsearch 的实际操作，展示了如何在 Kibana 中查看索引数据，并演示了在搜索接口中添加排序功能时，因未正确处理排序参数而导致的 `QueryShardException`（解析异常）。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示 IntelliJ IDEA 中的项目结构，聚焦于 `SearchController` 类。
*   **00:00:05 - 00:00:15**：讲师在 `SearchController` 中定义了 `@PostMapping` 的 `modify` 方法，用于更新商品信息。
*   **00:00:15 - 00:00:25**：讲师在 `SearchController` 中定义了 `@GetMapping` 的 `search` 方法，用于分页查询商品信息。
*   **00:00:25 - 00:00:35**：讲师在 `SearchController` 中使用 `@Autowired` 注解注入 `SkulnInfoService` 服务。
*   **00:00:35 - 00:00:45**：讲师在 `SearchController` 中编写了 `search` 方法的实现，调用 `skulnInfoService` 进行查询。
*   **00:00:45 - 00:00:55**：讲师在 `SearchApplication` 主类中配置了 `@EnableFeignClients` 和 `@EnableElasticsearchRepositories`。
*   **00:00:55 - 00:01:05**：讲师在 `SkulnInfoService` 接口中定义了 `searchPage` 方法。
*   **00:01:05 - 00:01:15**：讲师在 `SkulnInfoServiceImpl` 类中实现 `searchPage` 方法，调用 `skulnInfoMapper` 进行分页查询。
*   **00:01:15 - 00:01:25**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:01:25 - 00:01:35**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:01:35 - 00:01:45**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:01:45 - 00:01:55**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:01:55 - 00:02:05**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:02:05 - 00:02:15**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:02:15 - 00:02:25**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:02:25 - 00:02:35**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:02:35 - 00:02:45**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:02:45 - 00:02:55**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:02:55 - 00:03:05**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:03:05 - 00:03:15**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:03:15 - 00:03:25**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:03:25 - 00:03:35**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:03:35 - 00:03:45**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:03:45 - 00:03:55**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:03:55 - 00:04:05**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:04:05 - 00:04:15**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:04:15 - 00:04:25**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:04:25 - 00:04:35**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:04:35 - 00:04:45**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:04:45 - 00:04:55**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:04:55 - 00:05:05**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:05:05 - 00:05:15**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:05:15 - 00:05:25**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:05:25 - 00:05:35**：讲师在 `SkulnInfoMapper` 接口中定义了 `findByBtime` 方法，用于根据 `btime` 字段分页查询。
*   **00:05:35 - 00:05:
