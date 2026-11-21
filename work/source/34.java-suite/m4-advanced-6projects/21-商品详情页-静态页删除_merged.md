# 21-商品详情页-静态页删除 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着我们来实现静态业的一个删除

那么删除这一块呢

其实跟我们生成是有关系的

我们看一下

我们生成静态业的名称

叫商品ID加HTML

静态业存储的路径在这一块

那删除呢

其实也是一样

把商品的ID传给我

然后我组装一个名称

在这个路径下把它删掉就可以了

好

我们写这个方法来实现一下

删除商品静态业

void delete HTML

把商品的名称给我传过来

商品的ID传过来

那这一块我们就直接把静态业的整体名称传过来就算了

就不要理传ID了

把它当做整个静态业名称

好

除了静态业名称

你还告诉我这个静态业在哪个路径下

HTML pass

HTML pass

这个是当前静态业它所存在的一个路径

告诉我之后我就知道去哪里删除了

好

我们接着把这个方法给实现一下

在这一块回车去实现这个方法就可以了

那这个时候静态业的路径有了

名称也有了

直接创建一个文件

看文件是否存在

如果存在的话

把它删掉

可以了

这是咱们这一块静态业的一个路径

文件删除

接着我们再控制成调用一次就可以了

在这里新建一个删除方法

好

我们写一个方法

result

写个DLHTML

这一块写起来也比较简单

我们直接写个delete mapping

value HTML

直接写一个你对应的商品ID

给我就可以了

pass variable

value写个ID

商品ID

ID有了

那么我组装一个fill name

那就简单了

ID加上我们的HTML

这就是文件的名称

接着我们就

接着我们就去进行删除了

那么删除直接调我们的业务层就可以了

点delete

把名称给他

fill name给他

接着是这个路径也要给他

那这个时候就进行删除成功了

好

我们在响应用户点ok

接着这一块写个叫删除静态页

成功

那么这一块就搞定了

接着我们给他写一个份接口

那份接口就写到这边来

这一块记得加上我们的斜杠SKU配给

下面这里记得也要加哈

行

这一块删除我们的静态页的方法就写完了

现在我们就在这里删除了

接着我们就会看到我们的中方这一块

我们就来在这里删除他们得到组合的时间

我们就要删除后还是什么

现在我们在这个地方双击时间

我们就在这里删除自己的路径

这里只是删除了斜杠

你的路径现在凭什么都可以删除

脸部的傾向都就可以删除了

我们就直接删除它

欢迎大家加入我们的订阅 aqueles

我们下一期视频再见

拜拜

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的电商系统中“静态页面生成与删除”功能的代码实现过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在控制器（Controller）中定义生成和删除商品详情页的 REST API 接口，并在服务层（Service）中实现具体的文件操作逻辑。整个过程涉及 Spring MVC 的注解（如 `@PostMapping`, `@DeleteMapping`, `@Value`）、Java 的文件操作（`File` 类）、以及服务层的接口与实现。视频重点在于展示如何将业务逻辑（生成/删除静态页）解耦到服务层，并通过 Feign 客户端进行远程调用，体现了分层架构和微服务思想。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示 `SkuPageController.java` 文件，讲解 `@PostMapping` 注解用于处理生成静态页的 POST 请求。
*   **00:05 - 00:15**: 详细讲解控制器中 `itemPage` 方法的实现，包括数据模型的构建（`Map<String, Object>`）和调用服务层方法 `skuPageService.itemPage(dataMap)`。
*   **00:15 - 00:25**: 切换到 `SkuPageService.java` 接口文件，展示 `delHtml` 和 `itemPage` 方法的声明。
*   **00:25 - 00:35**: 切换到 `SkuPageServiceImpl.java` 实现类，讲解 `delHtml` 方法中如何使用 `File` 类检查文件是否存在并进行删除操作。
*   **00:35 - 00:45**: 回到控制器，讲解如何使用 `@DeleteMapping` 注解定义删除接口，并通过 `@PathVariable` 获取 URL 中的 `id` 参数。
*   **00:45 - 00:55**: 在控制器中调用服务层的 `delHtml` 方法，并返回 `Result` 对象，其中 `Status` 为 `20000`。
*   **00:55 - 01:05**: 展示 `SkuPageFeign.java` 接口，讲解如何使用 `@FeignClient` 注解定义一个 Feign 客户端，用于调用远程服务的删除接口。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **控制器 (`SkuPageController.java`)**:
        ```java
        @PostMapping(value = "/html")
        public Result html(@RequestBody Sku sku) throws Exception {
            // 数据模型
            Map<String, Object> dataMap = new HashMap<String, Object>();
            dataMap.put("path", htmlPath);
            dataMap.put("templateName", "items.ftl");
            dataMap.put("name", sku.getId() + ".html"); // /id.html
            dataMap.put("address", "北京");

            // 生成静态页
            skuPageService.itemPage(dataMap);

            return new Result(flag: true, StatusCode.OK, message: "生成静态页成功！");
        }

        @DeleteMapping(value = "/html/{id}")
        public Result delHtml(@PathVariable(value = "id") String id) {
            String fileName = id + ".html";
            skuPageService.delHtml(fileName);
            return new Result(true, 20000);
        }
        ```
    *   **服务接口 (`SkuPageService.java`)**:
        ```java
        public interface SkuPageService {
            void delHtml(String name, String htmlPath);
            void itemPage(Map<String, Object> dataMap) throws Exception;
        }
        ```
    *   **服务实现 (`SkuPageServiceImpl.java`)**:
        ```java
        public class SkuPageServiceImpl extends BaseProcess implements SkuPageService {
            @Override
            public void delHtml(String name, String htmlPath) {
                File file = new File(htmlPath, name);
                if (file.exists()) {
                    file.delete();
                }
            }

            @Override
            public void itemPage(Map<String, Object> dataMap) throws Exception {
                super.writerPage(dataMap);
            }
        }
        ```
    *   **Feign 客户端 (`SkuPageFeign.java`)**:
        ```java
        @FeignClient(name = "seckill-page")
        public interface SkuPageFeign {
            @DeleteMapping(value = "/page/html/{id}")
            Result delHtml(@PathVariable(value = "id") String id);

            @PostMapping(value = "/html")
            Result html(@RequestBody Sku sku) throws Exception;
        }
        ```

*   **关键注解**:
    *   `@PostMapping` - 用于处理 HTTP POST 请求。
    *   `@DeleteMapping` - 用于处理 HTTP DELETE 请求。
    *   `@PathVariable` - 用于从 URL 路径中提取参数。
    *   `@RequestBody` - 用于将 HTTP 请求体中的 JSON 数据绑定到方法参数。
    *   `@Value("${htmlPath}")` - 用于从配置文件中注入属性值。
    *   `@FeignClient` - 用于定义一个 Feign 客户端，用于调用远程服务。

---

### 4) 关键场景与演示描述

*   **场景一：生成静态页**
    *   讲师在控制器中定义了一个 `@PostMapping` 接口，接收一个 `Sku` 对象作为请求体。
    *   在方法体内，创建了一个 `Map` 用于存储页面生成所需的数据，包括模板名称、商品 ID 和地址。
    *   调用 `skuPageService.itemPage(dataMap)` 方法来生成静态页面。
    *   最后，返回一个 `Result` 对象，表示操作成功。

*   **场景二：删除静态页**
    *   讲师在控制器中定义了一个 `@DeleteMapping` 接口，通过 `@PathVariable` 获取 URL 中的 `id` 参数。
    *   将 `id` 与 `.html` 后缀拼接，形成文件名。
    *   调用服务层的 `delHtml` 方法，传入文件名。
    *   返回一个 `Result` 对象，状态码为 `20000`，表示删除成功。

*   **场景三：服务层实现**
    *   讲师展示了服务接口 `SkuPageService` 的定义。
    *   在实现类 `SkuPageServiceImpl` 中，`delHtml` 方法通过 `File` 类检查文件是否存在，并调用 `delete()` 方法删除文件。
    *   `itemPage` 方法调用父类的 `writerPage` 方法来完成页面的生成。

*   **场景四：Feign 客户端**
    *   讲师展示了如何使用 `@FeignClient` 注解定义一个 Feign 客户端 `SkuPageFeign`。
    *   该客户端包含了与服务层相同的 `delHtml` 和 `html` 方法，用于远程调用。

*   **场景五：IDEA 开发环境操作**
    *   讲师在 IntelliJ IDEA 中进行代码编写和调试。
    *   使用了代码补全功能（如 `File` 类的 `delete()` 方法、`Result` 类的构造函数）。
    *   展示了如何在控制器中添加 `@DeleteMapping` 注解，并通过 `@PathVariable` 获取参数。
    *   在服务层中，展示了如何使用 `File` 类进行文件操作。
