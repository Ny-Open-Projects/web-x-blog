# 02-详情页生成-数据模型准备 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们讲解商品详情页的一个生成

那像商品详情页这一块呢

咱们在第一章其实已经讲过生成静态页

但是那一块只是生成一个普通的静态页

并不涉及到我们商品详情这一块

而我们这里呢要实现秒杀抢单呢

所以得把商品详情这一块给完完整整实现出来了

那这一块呢我们将基于第一章所学的formark来实现

用formark来实现的话

首先我们要明白用formark实现静态页生成有几个因素

第一个首先你要有模板

你有模板之后才能填充这个模板

填充这个模板呢其实就是我们对应的数据了

而那个数据就是我们所说的一个模板数据

对不对

对不对

对不对

所以咱们这一块要准备两方面的东西

一是模板

二是数据模型

好我们先来看一下这个页面需要什么

第一个这个是商品详情

第二个这个是商品的一个规格

后面这一块呢还有价格

还有倒计时

对不对

其实也就是我们商品的详情信息里面的数据信息

因此我们要想去获取它的一个数据

只用这个数据

查询商品详情就可以了

好因此我们等会就先来根据ID查询商品详情

然后再准备一个模板填充数据就OK了

行我们开始来实现一次

要想去实现商品详情的加载

我们在这一块之前其实已经整过一次

之前是直接把商品详情传过来

但这个不是特别方便测试哈

咱们为了方便测试

我们写一个方案

我们先用这个方法做什么事情呢

把ID传过来

我根据ID去查询一下

把商品详情查出来可不可以了

这样是更方便的哈

那等会要在这里去查询商品详情

咱们得调用份接口才行

份接口呢直接找SKU份就可以了

SKU份里面有一个叫Fund by ID

根据ID查询当前商品详情

因此我们这一块可以直接把它注入进来

然后去查询商品详情

实现一次就OK了

SKU份把它给注入进来

注入进来之后

我们就开始去调一下对应的接口哈

调对应的接口去实现根据ID查询商品详情

封装我们的数据模型

这一块呢既然要把ID传过来

是不是得写个ID啊

不用再把整个SKU传过来了

直接写pass variable

value

ID给我就行了

ID

接着我们去根据ID查出来就OK了

行我们写下SKU份.Fund by ID

SKU result

接下来我们把这一块给换一下就OK了

换成ID

这个呢就是它里面的逻辑数据

GETDATE

就OK了

不过我们页面这里还有一个

这个是我们的规格

规格呢白色红外体温

对吧

也就是我们这里后面的数据

这些数据呢

灰色单层冷藏

蓝色单层冷藏

就这些数据

因此我们要把这个对象查出来

然后只取后面的值就OK了

行咱们来实现一下

获取SPEC

DataMap

SKU result

GETDATE

GET

SPEC

拿到了

我们接着需要把它转成MAP

怎么转成MAP呢

因为这本身就是个MAP结构

转成MAP取出对应的值

对应的值组合到一起去

就是我们页面这里要的效果了

行我们来整一下

MAP

String

String

SPEC

MAP

等于用FastJson来转

Operject

SPEC给它MAP.class

接下来呢

我们做这么一个事情

把它里面的值提取出来就OK了

String

SPEC

List

等于

空就行了

循环一下

SPEC List

加等于

我们写一个斜线

加上

entry.getValue

这样子就OK了

OK了之后呢

我们把它存起来

页面就可以直接取出来了

或者你把这个对象直接塞到这个对象的SPEC里面都行

好咱们把它给塞进去也行

或者是把它放到这个SKU里面也可以

DataMap.put一下

SPEC

SPEC List

OK了

那数据模型这一块我们就搞定了

接下来我们将去实现数据模型的填充了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个高并发电商系统中“商品详情页生成”功能的开发讲解。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 Spring Boot 项目中，利用 Feign 客户端调用商品服务获取商品数据，并结合模板引擎（Freemarker）动态生成静态 HTML 页面。整个过程旨在解决商品详情页在高流量下的性能瓶颈，通过“动态生成静态页”来提升访问速度和系统稳定性。视频中还展示了如何通过 `@Autowired` 注入 Feign 客户端，并在控制器中调用服务层方法来完成数据填充和页面生成。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示课程大纲，明确本节主题为“商品详情页生成”，并指出其在高并发场景下的重要性。
*   **00:05 - 00:15**: 展示商品详情页的截图，说明其包含价格、库存、规格等信息，并强调需要根据商品类型（普通或热点）进行不同的处理。
*   **00:15 - 00:25**: 讲解实现思路，即使用 Freemarker 模板引擎来生成静态页面，并需要先准备模板和数据。
*   **00:25 - 00:35**: 在代码编辑器中，展示 `SkuPageController` 类的结构，包括用于删除静态页的 `@DeleteMapping` 方法。
*   **00:35 - 00:45**: 展示用于生成静态页的 `@PostMapping` 方法，其中包含一个 `dataMap` 用于存储模板和数据。
*   **00:45 - 00:55**: 讲解如何通过 Feign 客户端调用商品服务，获取商品数据，并将其填充到 `dataMap` 中。
*   **00:55 - 01:05**: 展示如何获取商品的规格信息（`spec`），并将其解析为 `Map<String, String>` 结构，以便在模板中使用。
*   **01:05 - 01:15**: 讲解如何将规格信息添加到 `dataMap` 中，以便在 Freemarker 模板中进行渲染。
*   **01:15 - 01:25**: 展示最终的 `itemPage(dataMap)` 调用，完成静态页面的生成。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文本内容**:
    *   **课程目标**: “目标6: Lvs+Nginx集群”。
    *   **章节标题**: “1 商品详情页生成”。
    *   **核心概念**: “静态页生成，我们使用freemarker来实现”。
    *   **实现思路**: “我们需要先创建模板，并且准备模板数据，然后填充模板即可”。
    *   **数据模型**: “我们创建一个普通方法，用于根据ID查询商品详情，并生成静态页”。

*   **代码关键内容**:

    **1. 控制器方法：删除静态页**
    ```java
    @DeleteMapping(value = "/html/{id}")
    public Result delHtml(@PathVariable(value = "id") String id) {
        String fileName = id + ".html";
        skuPageService.delHtml(fileName, htmlPath);
        return new Result(flag: true, StatusCode.OK, message: "删除静态页成功！");
    }
    ```

    **2. 控制器方法：生成静态页（基础版本）**
    ```java
    @PostMapping(value = "/html")
    public Result html(@RequestBody Sku sku) throws Exception {
        // 数据模型
        Map<String, Object> dataMap = new HashMap<>();
        dataMap.put("path", htmlPath);
        dataMap.put("templateName", "items.ftl");
        dataMap.put("name", sku.getId() + ".html");
        dataMap.put("address", "北京");
        dataMap.put("sku", sku);

        // 生成静态页
        skuPageService.itemPage(dataMap);
        return new Result(flag: true, StatusCode.OK, message: "生成静态页成功！");
    }
    ```

    **3. 控制器方法：生成静态页（进阶版本，带 Feign 调用）**
    ```java
    @PostMapping(value = "/html/{id}")
    public Result html(@PathVariable(value = "id") String id) throws Exception {
        // 数据模型
        Map<String, Object> dataMap = new HashMap<>();
        dataMap.put("path", htmlPath);
        dataMap.put("templateName", "items.ftl");
        dataMap.put("name", id + ".html");
        dataMap.put("address", "北京");

        // 获取商品数据
        Result<Sku> skuResult = skuFeign.findById(id);
        dataMap.put("sku", skuResult.getData());

        // 获取规格信息
        String spec = skuResult.getData().getSpec();
        Map<String, String> specMap = JSON.parseObject(spec, Map.class);
        String specList = "";
        for (Map.Entry<String, String> entry : specMap.entrySet()) {
            specList += entry.getKey() + ":" + entry.getValue();
        }
        dataMap.put("spec", specList);

        // 生成静态页
        skuPageService.itemPage(dataMap);
        return new Result(flag: true, StatusCode.OK, message: "生成静态页成功！");
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：商品详情页展示与需求分析 (00:00-00:15)**
    *   **演示**: 屏幕上首先展示了一个商品详情页的截图，该页面包含商品图片、价格、库存、规格等信息。
    *   **讲解**: 讲师指出，为了应对高并发，需要将动态页面“生成”为静态页面，以提高访问速度。并强调了根据商品类型（普通或热点）进行不同处理的必要性。

*   **场景二：代码实现 - 删除静态页功能 (00:25-00:35)**
    *   **演示**: 讲师在 IDEA 中打开 `SkuPageController.java` 文件，定位到 `@DeleteMapping` 注解的方法。
    *   **讲解**: 该方法接收一个 `id` 参数，将其拼接成文件名（如 `123.html`），然后调用 `skuPageService.delHtml` 方法删除对应的静态文件。

*   **场景三：代码实现 - 生成静态页功能 (00:35-01:15)**
    *   **演示**: 讲师将光标移动到 `@PostMapping` 方法中，逐步讲解如何构建 `dataMap`。
    *   **讲解**: 首先，将模板路径、模板名称、文件名和地址等基础数据放入 `dataMap`。接着，通过 `skuFeign.findById(id)` 调用远程服务获取商品对象，并将该对象放入 `dataMap`。
    *   **关键步骤**: 讲师演示了如何获取商品的 `spec` 字段（规格信息），并使用 `JSON.parseObject` 方法将其解析为 `Map<String, String>` 结构。然后，通过遍历该 Map，将键值对拼接成字符串，并存入 `dataMap`。
    *   **最终操作**: 调用 `skuPageService.itemPage(dataMap)` 方法，将填充好的数据和模板信息传递给服务层，完成静态页面的生成。

*   **场景四：代码调试与错误处理 (01:15-01:25)**
    *   **演示**: 讲师在代码中添加了 `dataMap.put("spec", specList);` 语句，并在 `itemPage(dataMap)` 调用后添加了 `return new Result(...);` 语句。
    *   **讲解**: 通过这种方式，确保了规格信息能够被正确传递给模板引擎，从而在生成的静态页面中正确显示。同时，返回 `Result` 对象用于前端响应。
