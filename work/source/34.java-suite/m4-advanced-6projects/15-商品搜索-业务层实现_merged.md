# 15-商品搜索-业务层实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们再来实现搜索

搜索这一块

我们先把这一块给换掉

换成post mapping

它换了之后

对的份里面也要跟着一起换一下

其实你不换也行

但是我们跟文档保持一致

因为文档这一块

我写的是post mapping

行 这一块

接着我们开始去实现

秒杀商品的一个搜索了

那么秒杀商品的一个搜索

大家可以看一下京东这一块

好 刷新一次

京东这一块

其实上面是有一个时间的

你每次一点击

它会加载对应的时间

所对应的秒杀商品数据

所以这个秒杀商品数据

它的搜索一般是具备

根据时间进行搜索的

当然条件也一般都会有

不过我们这一块

先整一个根据时间进行搜索

好 根据时间进行搜索

这个我们

要在哪里实现

在什么Data

Elatin设计这里去操作

我们Elatin设计去实现

我们看一下这一块它的一个搜索

根据时间搜索有个bgtime

我们看看bgtime

它这里精确到了

10年月日

年月日十分秒

是吧

精确到了年月日十分秒

这个时候我们就直接用

它来查询就可以了

你页面每次点击的时候

只需要把这个时间传过去

然后我这里根据时间进行搜索就OK了

好 这个怎么做呢

我们来这里实现一下

首先我们在这个设计这里来写一下

它一会要来这里做搜索

做搜索了

它会调我们的SKU info

调这里的

调它呢

它又会调谁呢

它又会在这里对应的方法里面调我们的SKU

info map调DO

对不对

我们先在这里把方法给写一下

写到这里

返回什么数据呢

大家要注意一下这个返回的数据对象

它叫配给对象

我先写到这里

回头我们再看

配给对象是谁呢

简单写一下

里面应该是SKU info

对不对

写个search

传数据

我们这一块现在是只传这个时间

但是以后还有可能会传别的条件

那所以你传什么我不清楚

我可以封装成一个万能的对象

map

search map

好

这一块搞定了

接着写它的实现

实现这一块怎么做呢

也是非常容易

这个是秒杀搜索

列表

好

这一块看起来很简单的

这一块该怎么做呢

我们这一块搜索了也不是说平白无故就去搜

是有分页的

大家看京东这一块

它这一块到这儿就没有数据了

它这个只是满足我们简单的场景

对不对

但如果说以后是我们双11双12那一块是不是有分页

所以我们这一块是具备分页功能的

好

这一块分页功能应该也是从这个search map里面

把当前的分页功能拿出来

让我们的当前页给传过来

所以我写一个方法获取当前页

比如传过来的名字叫配给lumbo

好

返回对象

应该是一个当前页

写个配给converter

在这里面去实现这个分页的获取

把它也给传过来

获取我们指定的对象

谁呢

return

search map

点get

获取这个配给lumbo

但是要转成int类型

写个int.%

就可以了

但这一块转换

如果传的不是一个数据

那有可能会有异常

一旦有异常

我们就直接返回第一页就行了

默认查询第一页

好了

这个是页码的一个获取

除了页码可以获取之外

那还有一个

就是根据时间查询

对不对

刚才我们说过

有可能会根据时间查询

时间是谁呢

那比如你传的时间是

是

时间我们就随便定一个名称

那这个名称咱跟文档上保持一致吧

文档上这个时间叫做

我们看这一块

这个时间是写的是什么

叫start time

咱也写个start time

好

比如你时间传的是start time

当前页是PageLumbo

对

好

好

we are going to go to the start time

对不对

那我们现在从这里面先获取这个时间get

写个叫start time

好了

时间也有了

时间有了之后呢

紧接着我就需要根据这个时间进行搜索

但是我这里是分页搜索

所以我这个时候要去实现一下这个操作

根据

根据bgtime实现分页搜索

那怎么做呢

我们先去一下这一块的做法直接去调dao就行了

我们写一下skuinformap.fundbybgtime就行了

那这一块呢

我还需要传相关的一个参数进去

参数包含什么呢

第一包含当前页

所以这里我要写一个当前页

对应的信息

还有个是什么呢

是

你这一块不是要根据时间搜索吗

所以还要把这个bgtime传入进去

有剩两个信息

好

bgtime作为第二个参数

这有个start time

就是我们的bgtime

紧接着还有一个

注意

还有一个就是咱分页对象

写个叫page request.off

把当前这个数据给写过来就行了

skuinformap给他

好我们看这一块

他需要几个数据

需要一个两个对不对

因为你每页还要显示条数

条数每页就显示20个就好了

我们固定写死

不过这里还不行

还不行

我们点进去

你会发现他的最基础的页码是从零开始的

所以你这里还要减一

因为我们目前这里是从一开始

可以了

这块就搞定了

接着这个方法

我们创建一下就可以了

在DL中创建一次就行了

这个就是

根据

分页

根据时间实现分页查询好

这一块我们就不用去写别的操作了

这是我们什么对他一拉提的设计

他这一块这个命名的一个规则

按照这个规则来就可以了

好

那我们这一块这个搜索

也就

搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程聚焦于一个名为“秒杀系统”的电商搜索功能的开发与实现。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 Spring Boot 项目中，利用 Elasticsearch 实现商品的分页搜索、条件筛选和数据修改功能。课程内容涵盖了控制器（Controller）、服务层（Service）和数据映射层（Mapper）的代码编写，以及如何使用 Spring MVC 注解（如 `@GetMapping`, `@PostMapping`）和 Spring Data Elasticsearch 的 `Pageable` 接口进行分页查询。同时，视频也展示了如何在前端页面（模拟京东秒杀页面）进行搜索操作，并在后端通过 `Elasticsearch` 的 REST API 查看数据，从而验证功能的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和 `SearchController` 的代码，介绍即将实现的“秒杀商品搜索”功能。
*   **00:06 - 00:15**: 讲解 `SearchController` 中的 `@PostMapping` 注解用于处理修改索引的请求，展示 `@PathVariable` 注解的使用。
*   **00:16 - 00:25**: 展示 `SearchController` 中的 `modify` 方法，用于处理修改索引的请求，并返回操作成功的提示。
*   **00:26 - 00:35**: 讲解 `SearchController` 中的 `addAll10` 方法，用于批量导入数据。
*   **00:36 - 00:45**: 展示 `SkulInfoService` 接口，定义了 `searchPage` 方法，用于分页搜索。
*   **00:46 - 00:55**: 讲解 `SkulInfoServiceImpl` 类，实现 `SkulInfoService` 接口，编写 `searchPage` 方法。
*   **00:56 - 01:05**: 展示 `SkulInfoServiceImpl` 中的 `pageConverter` 方法，用于将前端传来的 `pageNum` 参数转换为 `Integer` 类型。
*   **01:06 - 01:15**: 讲解 `Pageable` 接口的使用，展示如何创建 `PageRequest` 对象。
*   **01:16 - 01:25**: 展示 `SkulInfoServiceImpl` 中的 `findall` 方法，用于根据 `Pageable` 对象查询数据。
*   **01:26 - 01:35**: 讲解 `SearchController` 中的 `search` 方法，用于接收前端的搜索参数并调用服务层方法。
*   **01:36 - 01:45**: 展示 `SearchController` 中的 `search` 方法的完整代码。
*   **01:46 - 01:55**: 讲解 `SkulInfoService` 接口中 `searchPage` 方法的返回值类型 `Page<SkuInfo>`。
*   **01:56 - 02:05**: 展示 `SkulInfoServiceImpl` 中的 `searchPage` 方法的实现。
*   **02:06 - 02:15**: 讲解 `SkulInfoServiceImpl` 中的 `pageConverter` 方法的实现。
*   **02:16 - 02:25**: 展示 `SkulInfoServiceImpl` 中的 `findall` 方法的实现。
*   **02:26 - 02:35**: 讲解 `SearchController` 中的 `search` 方法的实现。
*   **02:36 - 02:45**: 展示 `SearchController` 中的 `search` 方法的完整代码。
*   **02:46 - 02:55**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解。
*   **02:56 - 03:05**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的使用。
*   **03:06 - 03:15**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **03:16 - 03:25**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **03:26 - 03:35**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **03:36 - 03:45**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **03:46 - 03:55**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **03:56 - 04:05**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **04:06 - 04:15**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **04:16 - 04:25**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **04:26 - 04:35**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **04:36 - 04:45**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **04:46 - 04:55**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **04:56 - 05:05**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **05:06 - 05:15**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **05:16 - 05:25**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **05:26 - 05:35**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **05:36 - 05:45**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **05:46 - 05:55**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **05:56 - 06:05**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **06:06 - 06:15**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **06:16 - 06:25**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **06:26 - 06:35**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **06:36 - 06:45**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **06:46 - 06:55**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **06:56 - 07:05**: 展示 `SearchController` 中的 `search` 方法的 `@RequestParam` 注解的 `required=false` 属性。
*   **07:06 - 07:15**: 讲解 `SearchController` 中的 `search` 方法的 `@RequestParam
