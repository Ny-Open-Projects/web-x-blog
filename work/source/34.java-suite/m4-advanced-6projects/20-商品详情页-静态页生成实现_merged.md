# 20-商品详情页-静态页生成实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那么静态业的生成呢

我们就要写对应的一个业务流程了

我们来先把对应的包给创建好

Control这个是得有的

接着还有我们的Service也得有

好包都有了

我们开始创建一下对应的一个业务流程了

先新建一个接口叫SKU

配给Service

接口有了

开始在里面写一个方法

OID写个叫ItemPage

那你每次记得要把数据给我传过来

写个Map

String Object Datamap

这个是生成静态业的方法

好接着给它写一个实现

右键新建一个类IMPL

实现刚才这个接口

注意要给容器去管理

那还有一个方法也需要我们去实现

在这里呢

由于要生成静态业

而刚才生成静态业的工具类

我们已经写好了

所以它这里只需要去继承就可以使用了

Base Process

这一块生成静态业的大体流程

我们就搞完了

好我们看这一块该怎么实现

这个是数据模型

我们可以塞一些数据进去

也可以不塞

也可以在控制器里面去塞都行

好我们直接调用一下复类的一个方法

点WritePage

把Datamap给它

这一层我们就搞定了

接着我们写控制器

控制器来调用它

那右键新建一个控制器

叫SKU Page Controller

这一块呢

给个RestController

RequestMapping给它

这里写个Value.Page

不要忘了加上CloseOrganic

CloseOrganic

好我们接着开始写这个静态业生成的方法

写个Public ResultPage

就写个HTML吧

给它一个请求地址

GetMapping

Value写个HTML

这里就写个PostMapping了

因为你要把这个数据给我传过来

对不对

RequestBody

写个叫SKU

把数据给我传过来

传过来之后呢

我再给你去生成对应的一个静态业

New ResultCube

StatusCode.ok

生成静态业成功

好我们开始生成静态业了

要把我们的业务层给注入进来

SKU Page Service

把它直接给注入进来就行了

AutoWrite

注入进来之后呢

我们就去调用它了

我们就来调用它了

但是调用之前一定要注意

你要先把数据模型准备好

因为数据模型里面有很多地方都是我们需要的一些数据

好那这个时候就创建一个Map对象

Map

String

Object

DataMap

RuleHashtagMap

写一个String

写个Object

往里面塞数据就行了

那么塞数据呢

要根据刚才的一个业务流程去猜

第一个是template name

就是模板的名称

第二个是当前的一个生成静态业的名称

还有一个是数据存储的路径

好

这三个给它其实就可以了

你还可以给下自己的一个数据模型

比如说Archers

你可以写个叫北京

好

这个呢

我们接着再写一下生成静态业的一个路径

还有这个文件的名称

文件的名称呢

我们一般是写商品ID.html

这种模式

所以我们这一块可以组装一下

sku.getid

加上一个.html

这个就行了

至于说模板名称的话

那我们现在这里只有一个

items.ftl

ftl

items

这个就写好了

写好之后呢

还有一个是这个路径

路径呢

我们一般不要写死了

一般是配置一下

通过这个配置来决定生成文件的一个路径

所以我们可以把它给注入进来

privity

string

直接用我们的Value属性

把它给注入进来

Value自己注入

注入了之后呢

这一块就直接给它就行了

那于是之后呢

就是这一块数据填充就搞定了

接着我们可以去调用一下我们的service了

sku.pageservice.itempage

datamap给它

这个是生成静态页

行那这一块就搞定了

拋个异常出去

到时候呢

我们要调用它的话

这个时候就要给它写个份接口了

因此呢

我们可以在份接口里面去实现一下这个方法的编写

把这整个拷贝过去

找到我们的page这一块

写个叫做sku.page.fun

接口哈

上面写个叫funclient

里面有个叫name.scule.page

把刚才这个方法编写过来

这个呢就不要了

OK

整个就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于如何在 Spring Boot 项目中实现“静态页面生成”功能的实战教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了从创建服务接口、实现服务类、编写控制器到最终调用生成静态页面的完整流程。核心内容包括：
*   **技术栈**：Spring Boot、Spring MVC、Feign Client、Thymeleaf（通过 `BaseProcess` 类推断）。
*   **核心功能**：根据传入的数据模型（`dataMap`），动态生成一个 HTML 文件并保存到指定路径。
*   **代码结构**：采用分层架构，包括 `controller`、`service` 和 `base` 层。
*   **关键步骤**：定义接口、实现服务、编写控制器、调用服务、处理模板文件。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 1：项目结构与基础配置 (0:00 - 0:30)**
    *   展示项目结构，包含 `seckill-page` 模块。
    *   介绍 `BaseProcess` 类，用于处理静态页面生成的核心逻辑。
    *   代码中显示了 `writerPage` 方法，用于接收模板名、路径和数据，并生成文件。

*   **章节 2：定义服务接口 (0:30 - 1:00)**
    *   在 `com.seckill.page.service` 包下创建 `SkuPageService` 接口。
    *   定义方法 `itemPage(Map<String, Object> dataMap)`，用于生成静态页。

*   **章节 3：实现服务层 (1:00 - 1:30)**
    *   创建 `SkuPageServiceImpl` 类，实现 `SkuPageService` 接口。
    *   代码中显示了 `BaseProcess` 类的 `writerPage` 方法的调用，用于将数据写入文件。

*   **章节 4：编写控制器层 (1:30 - 2:30)**
    *   在 `com.seckill.page.controller` 包下创建 `SkuPageController`。
    *   使用 `@RestController` 和 `@PostMapping` 注解定义一个 HTTP 接口。
    *   通过 `@Autowired` 注入 `SkuPageService`。
    *   在控制器中接收 `Sku` 对象，将其数据放入 `Map<String, Object>`，然后调用服务层的 `itemPage` 方法。

*   **章节 5：处理模板与生成文件 (2:30 - 3:00)**
    *   在 `resources/templates` 目录下放置一个名为 `items.ftl` 的模板文件。
    *   在控制器中，将 `sku` 对象的属性（如 `name`、`id`、`address`）放入 `dataMap`。
    *   调用 `skuPageService.itemPage(dataMap)` 生成静态页面。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1：`BaseProcess` 类中的 `writerPage` 方法**
    ```java
    void writerPage(Map<String, Object> dataMap) throws Exception {
        String templateName = dataMap.get("templateName").toString();
        String path = dataMap.get("path").toString();
        File file = new File(path);
        if (!file.exists()) {
            file.mkdirs();
        }
    }
    ```
    *   **功能**：根据传入的 `templateName` 和 `path`，创建文件并准备写入。

*   **关键代码片段 2：`SkuPageService` 接口**
    ```java
    public interface SkuPageService {
        void itemPage(Map<String, Object> dataMap);
    }
    ```
    *   **功能**：定义了生成静态页面的服务契约。

*   **关键代码片段 3：`SkuPageServiceImpl` 类中的实现**
    ```java
    public class SkuPageServiceImpl extends BaseProcess implements SkuPageService {
        @Override
        public void itemPage(Map<String, Object> dataMap) {
            // 调用 BaseProcess 的 writerPage 方法
            writerPage(dataMap);
        }
    }
    ```
    *   **功能**：继承 `BaseProcess`，实现 `itemPage` 方法，调用父类方法完成文件生成。

*   **关键代码片段 4：`SkuPageController` 控制器**
    ```java
    @RestController
    @RequestMapping(value = "/page")
    @CrossOrigin
    public class SkuPageController {
        @Autowired
        private SkuPageService skuPageService;

        @PostMapping(value = "/html")
        public Result html(@RequestBody Sku sku) throws Exception {
            Map<String, Object> dataMap = new HashMap<String, Object>();
            dataMap.put("templateName", "items.ftl");
            dataMap.put("path", "/id.html");
            dataMap.put("name", sku.getName());
            dataMap.put("id", sku.getId());
            dataMap.put("address", "北京");

            skuPageService.itemPage(dataMap);

            return new Result(true, StatusCode.OK, "生成静态页成功！");
        }
    }
    ```
    *   **功能**：接收 HTTP POST 请求，解析 `Sku` 对象，构造 `dataMap`，调用服务层生成静态页，并返回成功响应。

*   **关键代码片段 5：`FeignClient` 配置**
    ```java
    @FeignClient(name = "seckill-page")
    public interface SkuPageFeign {
        @PostMapping("/page/html")
        Result html(@RequestBody Sku sku);
    }
    ```
    *   **功能**：用于微服务间调用，但视频中未实际使用。

---

### 4) 关键场景与演示描述

*   **场景 1：创建服务接口**
    *   讲师在 `com.seckill.page.service` 包下右键，选择“新建” -> “接口”，命名为 `SkuPageService`。
    *   在接口中定义了 `itemPage(Map<String, Object> dataMap)` 方法。

*   **场景 2：实现服务层**
    *   讲师在 `com.seckill.page.service.impl` 包下右键，选择“新建” -> “类”，命名为 `SkuPageServiceImpl`。
    *   选择继承 `BaseProcess` 并实现 `SkuPageService` 接口。
    *   在实现类中，调用 `writerPage(dataMap)` 方法。

*   **场景 3：编写控制器**
    *   讲师在 `com.seckill.page.controller` 包下创建 `SkuPageController`。
    *   使用 `@RestController` 和 `@RequestMapping` 注解。
    *   使用 `@PostMapping` 定义 `/html` 接口。
    *   使用 `@RequestBody` 接收 `Sku` 对象。

*   **场景 4：处理模板文件**
    *   讲师在 `resources/templates` 目录下创建 `items.ftl` 文件。
    *   在控制器中，将 `sku` 的属性（如 `name`、`id`、`address`）放入 `dataMap`。
    *   调用 `skuPageService.itemPage(dataMap)`。

*   **场景 5：生成静态文件**
    *   讲师在 `BaseProcess` 中的 `writerPage` 方法中，根据 `templateName` 和 `path` 生成文件。
    *   例如，将 `items.ftl` 模板渲染后，生成 `/id.html` 文件。

*   **场景 6：返回响应**
    *   控制器中，调用服务后，返回 `Result` 对象，包含 `flag=true`、`statusCode=OK` 和 `message="生成静态页成功！"`。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
