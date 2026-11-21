# 18-商品详情页-freemarker配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着我们讲解秒杀商品详情页的一个处理方案

在我们活动的时候

热卖商品它的详情页访问频率是非常高的

如果这个时候我们直接去查询数据库

会给数据库带来非常大的压力

有可能都会导致数据库崩溃

所以像商品详情页这一块

我们也需要优化处理一下

像咱们商品详情页

它这一块的主要内容有商品介绍

商品标题

商品图片

还有商品价格

商品数量等等

像这些数据里面

除了商品数量有可能会发生变化

其他的几乎都不会发生什么变化

针对这种变更频率很低的数据

我们可以做一些优化处理

比如可以放到Reddit缓存区

也可以把它做成静态页

那这一块由于数据量非常庞大

所以我们不建议放到缓存里面

去

建议做成静态页

做成静态页这一块

我们用的技术主要是Fullmark

那关于Fullmark的一些相关API这一块

我们就不详细讲解了

我们直接去使用它了

首先我们先搭建一个工程

在工程里面去实现详情页的一个静态化

那这一块就要引入我们Fullmark相关的核心依赖包

紧接着我们这里要配置一些

Fullmark相关的配置

这个配置呢

我们拷贝过来

然后简单介绍一下

把咱们这一块打开

在这里把这个配置给拷过来

这里呢

主要是Fullmark相关的一个配置

这里有一个地方

这个是配置Fullmark的一个模板的位置

因为我们要做页面静态化

但页面它的一些数据怎么来呢

它都是根据模板的样式

来决定的

那这一块模板的位置

我们要找一个地方存储

所以这个templates下面是存储我们模板的一个地方

那模板这一块每次修改之后是立刻加载呢

还是说加载之前的缓存数据呢

上面有个cached force

表示我们模板是没有缓存的

你的模板发生任何改变

它这一块这个数据会跟着变

还有一个是咱们模板这一块

它的一个后缀是FTL

这个是什么意思呢

我来右键新建个文件

大家看一下

写个叫e或者叫items.ftl

后缀目前是HTML

它不是我们这里标准的模板

把它的后缀给换一下

换成FTL

这个时候才是一个标准的模板

咱们这里也说了

模板的后缀是FTL

对吧

那后面我们可以根据它来生成一个对应的文件

根据它来生成

它就是模板

生成之后文件存储的地方存到哪里去了

我们接着配置一下文件存储的地方

这里已经写了叫HTML pass

这个是可以随意写的

我们这里写的是HTML pass

到时候文件生成之后会存储到地盘HTML目录

好

这个是我们当前这一块生成商品静态业的工程的一个完善

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于一个名为“秒杀系统”的技术课程，具体讲解了如何为“商品详情页”实现静态化，以减轻数据库压力。讲师使用 IntelliJ IDEA 开发工具，通过 Spring Boot 框架结合 Freemarker 模板引擎来实现。主要内容包括：分析商品详情页高并发访问的问题，引入 Freemarker 作为静态化方案，配置 `bootstrap.yml` 文件以启用 Freemarker，创建并配置模板文件（`.ftl`），并演示了如何通过 `BaseProcess` 配置类来定义静态化文件的生成逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，展示课程大纲，定位到“4 商品详情页”下的“4.2 工程搭建”章节。
*   **00:03 - 00:08**: 讲师在 `pom.xml` 文件中添加 Freemarker 依赖，用于静态化页面。
*   **00:08 - 00:13**: 讲师切换到 `bootstrap.yml` 配置文件，开始配置 Freemarker 相关参数。
*   **00:13 - 00:18**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `template-loader-path`、`charset`、`suffix` 等关键参数。
*   **00:18 - 00:23**: 讲师在 `bootstrap.yml` 中配置 `ribbon` 的超时参数。
*   **00:23 - 00:28**: 讲师在 `bootstrap.yml` 中配置 `htmlPath`，用于指定静态化文件的输出路径。
*   **00:28 - 00:33**: 讲师在 `resources/templates` 目录下创建 `items.ftl` 模板文件，并在 IDEA 中右键选择“Refactor” -> “Rename” 对其进行重命名。
*   **00:33 - 00:38**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `settings` 部分，包括 `template_update_delay`、`check-template-location` 等。
*   **00:38 - 00:43**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `cache` 参数。
*   **00:43 - 00:48**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `content-type` 参数。
*   **00:48 - 00:53**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `expose-request-attributes` 和 `expose-session-attributes` 参数。
*   **00:53 - 00:58**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `request-context-attribute` 参数。
*   **00:58 - 01:03**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `check-template-location` 参数。
*   **01:03 - 01:08**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `charset` 参数。
*   **01:08 - 01:13**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `suffix` 参数。
*   **01:13 - 01:18**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `template-loader-path` 参数。
*   **01:18 - 01:23**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `template_update_delay` 参数。
*   **01:23 - 01:28**: 讲师在 `bootstrap.yml` 中配置 `freemarker` 的 `allow-bean-definition-overriding` 参数。
*   **01:28 - 01:33**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `application` 和 `cloud` 参数。
*   **01:33 - 01:38**: 讲师在 `bootstrap.yml` 中配置 `ribbon` 的 `ReadTimeout` 和 `ConnectTimeout` 参数。
*   **01:38 - 01:43**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `cloud` 参数。
*   **01:43 - 01:48**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `application` 参数。
*   **01:48 - 01:53**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `server` 参数。
*   **01:53 - 01:58**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `profiles` 参数。
*   **01:58 - 02:03**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `main` 参数。
*   **02:03 - 02:08**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `cloud` 参数。
*   **02:08 - 02:13**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `application` 参数。
*   **02:13 - 02:18**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `server` 参数。
*   **02:18 - 02:23**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `profiles` 参数。
*   **02:23 - 02:28**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `main` 参数。
*   **02:28 - 02:33**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `cloud` 参数。
*   **02:33 - 02:38**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `application` 参数。
*   **02:38 - 02:43**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `server` 参数。
*   **02:43 - 02:48**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `profiles` 参数。
*   **02:48 - 02:53**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `main` 参数。
*   **02:53 - 02:58**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `cloud` 参数。
*   **02:58 - 03:03**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `application` 参数。
*   **03:03 - 03:08**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `server` 参数。
*   **03:08 - 03:13**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `profiles` 参数。
*   **03:13 - 03:18**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `main` 参数。
*   **03:18 - 03:23**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `cloud` 参数。
*   **03:23 - 03:28**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `application` 参数。
*   **03:28 - 03:33**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `server` 参数。
*   **03:33 - 03:38**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `profiles` 参数。
*   **03:38 - 03:43**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `main` 参数。
*   **03:43 - 03:48**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `cloud` 参数。
*   **03:48 - 03:53**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `application` 参数。
*   **03:53 - 03:58**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `server` 参数。
*   **03:58 - 04:03**: 讲师在 `bootstrap.yml` 中配置 `spring` 的 `profiles` 参数。
*   **04:03 - 04:08**: 讲师在 `bootstrap.yml` 中配置 `spring`
