# 22-静态页生成和删除测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接着来测试一下静态业的生成和静态业的删除

那这一块静态业的生成要用配给HTML用Post的方式提交

并且要传递SKU对象信息

SKU对象信息呢是我们的json数据类型

好那这个时候这个数据为了让它能在页面展示

我们把它放到数据模型里面去

页面呢直接把整个对象给输出

这一块我们直接给输出一下

第二

看一会儿能不能把我们对应的数据给生成了

行这是这一块

接着我们给它创建一个启动类来测试这个静态业的生成

右键新建一个配给Application

这一块加个Spring Boot Application

Spring Application Run

配给Application Class

行

静态业生成这一块我们来启动测试

我们先来模拟一个商品来测试一下静态业的生成

生成之后呢

它应该在地盘配给HTML

也就是这个目录下会创建一个静态文件

好我们来打开我们的iDeal的测试工具

在这一块Post的请求输入HTTP

Localhost 18087

输入我们的地址

配给HTML

并且我们要模拟一个商品数据

在这一块我就写一个商品信息的一个数据了

ID我就不模拟太多

1234

商品名称LAM

黑马IT培训

好OK点击提交看一下效果

那这一块静态业生成了

我们打开看一下黑马ID培训是可以的

黑马ID培训是可以的

黑马ID培训是可以的

接着我们再来测试删除

那么删除我们就要调用上面这个方法

这个提交方式是Delete方式

并且要输入我们当前商品的一个ID

好我们测试一次

把这一块打开

加上我们商品的名称

商品的ID1234

提交方式用Delete方式

好测试一次

为了让大家看到效果

我们就把这个窗口缩小一点点

我们就把这个窗口缩小一点点

我们就把这个窗口缩小一点点

我们就把这个窗口缩小一点点

我们就把这个窗口缩小一点点

我们就把这个窗口缩小一点点

我们就把这个窗口缩小一点点

提交

静态液就被删掉了

OK

那我们这里静态液的生成

和静态液的删除就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的静态页面生成与管理系统的开发过程。核心内容包括：
- **项目结构与启动**：演示了 Spring Boot 项目的标准结构，并通过 `PageApplication` 类的 `main` 方法启动应用。
- **控制器开发**：重点讲解了 `SkuPageController` 类，其中包含两个核心功能：
    1.  **静态页面删除**：通过 `@DeleteMapping` 注解，接收一个商品 ID，调用服务层删除对应的 `.html` 静态文件。
    2.  **静态页面生成**：通过 `@PostMapping` 注解，接收一个 `Sku` 对象，将数据填充到 FreeMarker 模板 `items.ftl` 中，生成一个名为 `id.html` 的静态页面。
- **技术栈**：使用了 Spring Boot、Spring MVC、FreeMarker 模板引擎，并通过 RESTful API 进行交互。
- **演示验证**：通过 REST Client 工具发送 HTTP 请求，验证了删除和生成静态页面功能的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:04**：展示项目结构，打开 `PageApplication.java` 文件，准备启动项目。
*   **00:04 - 00:08**：在 `PageApplication.java` 中，使用 `@SpringBootApplication` 注解启动 Spring Boot 应用。
*   **00:08 - 00:12**：在 `PageApplication.java` 中，编写 `main` 方法，调用 `SpringApplication.run(PageApplication.class, args)` 启动应用。
*   **00:12 - 00:16**：使用 REST Client 工具，向 `http://localhost:18087/page` 发送 POST 请求，演示静态页面生成功能。
*   **00:16 - 00:20**：在浏览器中访问生成的静态页面 `http://localhost:18087/1234.html`，验证页面内容。
*   **00:20 - 00:24**：回到 `SkuPageController.java`，查看 `@DeleteMapping` 注解的删除方法。
*   **00:24 - 00:28**：使用 REST Client 工具，向 `http://localhost:18087/page/del-html` 发送请求，验证删除功能。
*   **00:28 - 00:32**：回到 `SkuPageController.java`，查看 `@PostMapping` 注解的生成方法。
*   **00:32 - 00:36**：在 `SkuPageController.java` 中，展示如何将 `Sku` 对象的数据（如 `name`, `address`, `sku`）填充到 `dataMap` 中，用于生成静态页面。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**：
    *   **控制器类 `SkuPageController.java`**：
        ```java
        @DeleteMapping(value = "/html/{id}")
        public Result delHtml(@PathVariable(value = "id") String id) {
            String fileName = id + ".html";
            skuPageService.delHtml(fileName, htmlPath);
            return new Result(flag: true, StatusCode.OK, message: "删除静态页成功！");
        }

        @PostMapping(value = "/html")
        public Result html(@RequestBody Sku sku) throws Exception {
            // 数据模型
            Map<String, Object> dataMap = new HashMap<>();
            dataMap.put("path", htmlPath);
            dataMap.put("templateName", "items.ftl");
            dataMap.put("name", sku.getId() + ".html"); // /id.html
            dataMap.put("address", "北京");
            dataMap.put("sku", sku);

            // 生成静态页
            skuPageService.itemPage(dataMap);
            return new Result(flag: true, StatusCode.OK, message: "生成静态页成功！");
        }
        ```
    *   **服务层方法（隐含）**：
        *   `delHtml(String fileName, String htmlPath)`：删除指定路径下的 `.html` 文件。
        *   `itemPage(Map<String, Object> dataMap)`：将 `dataMap` 中的数据填充到 FreeMarker 模板 `items.ftl` 中，生成静态页面。
    *   **模板文件 `items.ftl`**：
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            今天去${address}玩！
        </body>
        </html>
        ```
    *   **主应用类 `PageApplication.java`**：
        ```java
        @SpringBootApplication
        public class PageApplication {
            public static void main(String[] args) {
                SpringApplication.run(PageApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目启动与页面生成**
    *   **描述**：讲师首先展示了 Spring Boot 项目的目录结构，然后在 `PageApplication.java` 中编写了 `main` 方法。通过调用 `SpringApplication.run(PageApplication.class, args)`，成功启动了应用。
    *   **演示**：在 REST Client 中，向 `/page` 发送 POST 请求，请求体包含一个 `Sku` 对象。服务层接收到数据后，将 `name`、`address` 和 `sku` 等信息填充到 `dataMap` 中，并调用 `itemPage(dataMap)` 方法，最终生成了 `1234.html` 文件。
    *   **结果**：在浏览器中访问 `http://localhost:18087/1234.html`，页面成功显示了“今天去北京玩！”的内容，验证了静态页面生成功能。

*   **场景二：静态页面删除**
    *   **描述**：讲师在 `SkuPageController.java` 中展示了 `@DeleteMapping` 注解的 `delHtml` 方法。该方法接收一个商品 ID，将其转换为文件名（如 `1234.html`），然后调用服务层的 `delHtml` 方法删除该文件。
    *   **演示**：在 REST Client 中，向 `/page/del-html` 发送请求，请求体包含一个商品 ID。服务层成功删除了对应的 `.html` 文件。
    *   **结果**：返回的响应体中包含 `flag: true` 和 `message: "删除静态页成功！"`，表明删除操作成功。

*   **场景三：数据模型与模板填充**
    *   **描述**：讲师重点讲解了 `@PostMapping` 注解的 `html` 方法。该方法接收一个 `Sku` 对象，并将其属性（如 `id`、`name`、`address`）填充到 `dataMap` 中。
    *   **演示**：在代码中，`dataMap.put("name", sku.getId() + ".html");` 表示将商品 ID 作为文件名。`dataMap.put("address", "北京");` 表示将地址设置为“北京”。最后，`skuPageService.itemPage(dataMap);` 调用服务层方法，将这些数据填充到 `items.ftl` 模板中。
    *   **结果**：最终生成的静态页面内容为“今天去北京玩！”，成功将数据从后端传递到前端模板。

---

以上是根据视频画面进行的完整技术分析。
