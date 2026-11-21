# 29-索引和静态页实时同步测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好我们开始进行测试

那么测试的时候

我们先看一下这一块

刚才我们做的这一个conner服务

在这里

由于用到了份接口

那这个时候这里要开启份

enable

份client

写个base packaging

第一个是我们

故事

第一个我们想一下

第一个是我们的search

对吧

第二个是不是静态页

好copy

拷过来

第二个是我们的静态页

静态页也给拷过来

好了

这个地址有了

接着我们启动这个微服务

把它给启动一次

好启动一次

启动之后呢

我们一会儿就来进行测试

等它启动

好

目前这一块启动应该没有问题

启动之后呢

我们把这个

这个

这里是生成静态页的目录

对吧

我们看一下索引库这里

这个是我们的索引库

我们做这么一个事情

先做一个数据的修改

我们修改谁呢

我们在这里找一下

我们找一下

找一个数据

就第一个吧

就找这里面的第一个数据

一个数据

我们看一下它的特性

现在这一块是什么样的呢

现在这一块状态是二

那应该没有问题

那我们就把它信息简单改一下

简单改一下就可以了

改个QQ

好保存一次

那么保存一次呢

我们看静态页生成没有

静态页生成了

对吧

好生成了

看一下

没有问题

那我们还要看什么呢

看索引库里面的数据变了没有

那我们要把这一块打开

执行一次搜索

那搜索呢

我们是匹配指定的链

那我们指定是

指定谁指定ID链就行了

搜谁说他好搜一次

看QQ进来没有

这一块是不是还有点问题啊

它并没有变成QQ

所以这个我们要看一下

搜索引擎这里出现了什么问题

这里

好像没有变化

对吧

我们看一下

刚才我们是做的修改操作

那修改操作的话

在这一块

好我们看这一块发生了什么问题呢

把我们搜索为符找到

这里

搜索为符我们可以简单找到一下

那一会会掉这里对不对

那么掉这里了我们再来改一下

把它改成QQ再加个QQQ

多加了好多个Q

好可以了

那么这个时候会掉这一块

这个是我们的一个搜索为符

很遗憾我这里没有写方法调用

对不对

我们方法是写了但是没写调用

所以这一块还要写这个调用才行

好来做一下

索引的更新

点我们写个更新

Modify

Type给它

SKU info给它

那么现在这一块才算OK

刚才没有报错

也没有

执行相关的代码

所以这一块

就发生了刚才这么个问题

大家注意一下就行了

好我们现在再来执行一下相关的一个操作

等它运行起来

运行起来之后呢

我们仍然按照这个来执行一次

我们先看一下这一块

他这里是AAA

是最初的

对吧

并没有QQQ

我们现在把那个QQQ去掉

看一会儿AAA有没有去掉

如果去掉了说明同步更新没有问题

好我们来测试一次

看服务启动了

启动了

我们开始进行一次测试

那么测试了就把QQQ

就把QQQQ

去掉了

那我一点几保存

那边的AAA

应该也要去掉才对

对不对

好我保存一次大家看效果

好点击保存

保存了

我们直接来搜一下数据变了没有

AAA去掉了

应该没有问题了吧

好这是这个

那么这边的详情页肯定也是发生了变化

现在是有QQ刷新一次没了

对吧

好我们再做另一个

另外一个操作是删除的一个操作

那把它变成几了

把它变成一那就不是秒杀商品了

对不对

不是秒杀商品的

我们看他会走哪个步骤

如果不是秒杀商品我们这里有没有做判断呢

等于2

对吧

之前是

2现在是

before是2

之后是1那这个时候是不是要删除啊

好我们来看一下

把它给改成

大家看

改后是1

保存一次

好我们先看静态页干掉没有

静态页没了

对吧

看索引这里大家看啊

索引

刷新一次

搜索一次

没了

是不是索引也干掉了

因此我们这里

实时同步也没有任何问题

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个名为“秒杀项目”（seckill-project）的分布式电商搜索系统的技术实现过程。核心内容围绕如何通过 **Canal** 监听数据库变更，利用 **Feign** 远程调用，将商品库存（Sku）的增删改操作同步到 **Elasticsearch** 中，从而实现搜索结果的实时更新。视频通过 IntelliJ IDEA 编辑器展示代码逻辑，并通过浏览器和 ElasticSearch 管理界面演示数据同步效果。整个系统架构基于 Spring Boot，并集成了 Spring Data Elasticsearch 和 OpenFeign。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 展示项目结构，定位到 `SearchApplication.java`，并高亮显示 `@EnableFeignClients` 注解，说明系统使用了 Feign 进行服务间调用。
*   **00:04 - 00:07**: 在 `SkuHandler` 类中，演示如何根据商品状态（`after.getStatus()`）判断是“修改索引”（type=2）还是“删除索引”（type=3），并调用 `skuPageFeign.html` 或 `skuPageFeign.delHtml` 方法。
*   **00:08 - 00:11**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **00:12 - 00:15**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **00:16 - 00:19**: 在 `SkuHandler` 类中，演示如何根据商品状态（`before.getStatus()` 和 `after.getStatus()`）判断是“删除索引”（type=3）还是“修改索引”（type=2），并调用 `skuPageFeign.delHtml` 或 `skuPageFeign.html` 方法。
*   **00:20 - 00:23**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **00:24 - 00:27**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **00:28 - 00:31**: 在 `SkuHandler` 类中，演示如何根据商品状态（`after.getStatus()`）判断是“修改索引”（type=2）还是“删除索引”（type=3），并调用 `skuPageFeign.html` 或 `skuPageFeign.delHtml` 方法。
*   **00:32 - 00:35**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **00:36 - 00:39**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **00:40 - 00:43**: 在 `SkuHandler` 类中，演示如何根据商品状态（`before.getStatus()` 和 `after.getStatus()`）判断是“删除索引”（type=3）还是“修改索引”（type=2），并调用 `skuPageFeign.delHtml` 或 `skuPageFeign.html` 方法。
*   **00:44 - 00:47**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **00:48 - 00:51**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **00:52 - 00:55**: 在 `SkuHandler` 类中，演示如何根据商品状态（`after.getStatus()`）判断是“修改索引”（type=2）还是“删除索引”（type=3），并调用 `skuPageFeign.html` 或 `skuPageFeign.delHtml` 方法。
*   **00:56 - 00:59**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **01:00 - 01:03**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **01:04 - 01:07**: 在 `SkuHandler` 类中，演示如何根据商品状态（`before.getStatus()` 和 `after.getStatus()`）判断是“删除索引”（type=3）还是“修改索引”（type=2），并调用 `skuPageFeign.delHtml` 或 `skuPageFeign.html` 方法。
*   **01:08 - 01:11**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **01:12 - 01:15**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **01:16 - 01:19**: 在 `SkuHandler` 类中，演示如何根据商品状态（`after.getStatus()`）判断是“修改索引”（type=2）还是“删除索引”（type=3），并调用 `skuPageFeign.html` 或 `skuPageFeign.delHtml` 方法。
*   **01:20 - 01:23**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **01:24 - 01:27**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **01:28 - 01:31**: 在 `SkuHandler` 类中，演示如何根据商品状态（`before.getStatus()` 和 `after.getStatus()`）判断是“删除索引”（type=3）还是“修改索引”（type=2），并调用 `skuPageFeign.delHtml` 或 `skuPageFeign.html` 方法。
*   **01:32 - 01:35**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **01:36 - 01:39**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **01:40 - 01:43**: 在 `SkuHandler` 类中，演示如何根据商品状态（`after.getStatus()`）判断是“修改索引”（type=2）还是“删除索引”（type=3），并调用 `skuPageFeign.html` 或 `skuPageFeign.delHtml` 方法。
*   **01:44 - 01:47**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **01:48 - 01:51**: 在 `SearchController` 中，演示如何通过 `@GetMapping` 接收前端传来的查询请求，并调用 `skuInfoService.findPage` 方法。
*   **01:52 - 01:55**: 在 `SkuHandler` 类中，演示如何根据商品状态（`before.getStatus()` 和 `after.getStatus()`）判断是“删除索引”（type=3）还是“修改索引”（type=2），并调用 `skuPageFeign.delHtml` 或 `skuPageFeign.html` 方法。
*   **01:56 - 01:59**: 在 `SearchController` 中，演示如何通过 `@PostMapping` 接收前端传来的修改请求，并调用 `skuInfoService.modify(type, skuInfo)` 方法。
*   **02:00 - 02:03**: 在 `Search
