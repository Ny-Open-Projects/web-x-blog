# 20-货物类型管理（服务接口开发_分页查询货物 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才咱们这个分页方法都已经写完了

接下来我们来测试一下

直接从这来启动一下就可以了

好 咱们这个服务已经启动完了

好 接下来我们就可以来测试一下了

把这边刷新一下

好 来看

这样的话我们能看到这个分页查询

就是这个

然后我们try it out

然后咱们来查一下

比如说我现在

先把一个是我们的page

我要查第一页

然后我查五个

其他我暂时先不写

其他我暂时先不写

然后直接查询

然后我们可以看到一共查出来了是

一共是十一个

一共是十一个

然后这个page size是五

一共是分成三页

然后当前是第一页

然后第一页这些items

能看到它是封装成这种数组

然后status状态是一

好

好

,然后这边

我们再来给它添加一个什么

添加一个条件

比如说现在我要根据什么

我要根据这个name来查

这个name的话

其实对应的是我们货物类型的名称

对吧

比如说我在这来一个食品

加一个食品

然后点再次查询

现在就很少了

是不是只剩下这一个了

只剩下这一个了

你看这个cons是不是等于一

然后页码是不是

页数也变成一

因为这是一个页码

就是数据量很少

数据量很少

然后我们可以换一个其他的

比如说我再加一个什么

我再加一个这个tranctypeid

tranctypeid

tranctypeid

咱们可以从这儿来复制一个

好

这是车辆类型的ID

然后点查询

但是还是这个数据对吧

如果说我们现在把这个食品给去掉

看看还有没有多个

但是这要看具体数据了

应该这样是不是就比较多了

好

一共有8个

这是根据这个车辆ID

车辆类型ID查出来的

好

那么到这儿的话

我们这个测试也是没有问题的

这是关于我们这个分页查询

先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段演示了一个基于 Spring Boot 的物流管理系统中“货物类型”数据的分页查询功能。演示者通过 IntelliJ IDEA 开发环境展示了后端 Java 代码的实现，然后通过 Swagger UI 前端接口文档进行实际调用和测试。核心内容包括：
*   **后端实现**：在 `PdGoodsTypeServiceImpl.java` 中，通过 `Pageable` 接口和 `Page` 对象实现分页查询，并在 `findByPage` 方法中接收 `name`、`truckTypeId`、`truckTypeName` 等查询参数。
*   **前端测试**：在 Swagger UI 中，演示者通过设置分页参数（`page`、`pageSize`）和查询条件（`name`、`truckTypeId`）来调用 `/base/goodsType/page` 接口，并成功获取到分页后的 JSON 数据。
*   **技术栈**：主要使用了 Spring Boot、MyBatis、Swagger UI 和 IntelliJ IDEA。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下按画面切换顺序进行逻辑划分：

*   **章节 1：后端代码实现 (00:00 - 00:02)**
    *   展示了 IntelliJ IDEA 中 `PdGoodsTypeServiceImpl.java` 文件的代码。
    *   重点是 `findByPage` 方法，该方法接收分页参数 `page`、`pageSize` 和查询条件 `name`、`truckTypeId`、`truckTypeName`，并返回一个 `Page<PdGoodsType>` 对象。

*   **章节 2：Swagger UI 接口文档 (00:02 - 00:04)**
    *   切换到浏览器，展示 Swagger UI 的首页，标题为“品达物流管理后台基础数据--Swagger文档”。
    *   重点展示了 `/base/goodsType/page` 接口的详细信息，包括其参数列表和“Try it out”按钮。

*   **章节 3：分页查询测试 (00:04 - 00:07)**
    *   在 Swagger UI 中，演示者填写了分页参数 `page=1`、`pageSize=5`。
    *   点击“Execute”按钮后，成功返回了包含 `counts`、`page`、`pageSize` 和 `items` 字段的 JSON 数据。

*   **章节 4：带条件查询测试 (00:07 - 00:10)**
    *   在 Swagger UI 中，演示者修改了查询条件，将 `name` 参数设置为“食品”。
    *   点击“Execute”按钮后，返回的 JSON 数据中 `items` 数组只包含符合“食品”条件的记录。

*   **章节 5：多条件组合查询测试 (00:10 - 00:13)**
    *   在 Swagger UI 中，演示者进一步设置了 `truckTypeId` 参数为 `123103137595676608`。
    *   点击“Execute”按钮后，返回的 JSON 数据中 `items` 数组只包含同时满足“食品”和指定 `truckTypeId` 条件的记录。

*   **章节 6：文档与代码对照 (00:13 - 00:15)**
    *   切换到 Typora 编辑器，展示项目文档 `第2章 基础数据服务开发(pdd-base)` 中的“3.4.5 查询货物类型列表”部分。
    *   文档中展示了 `GoodsTypeController` 中 `findAll` 方法的注解和 `@ApiOperation` 说明，以及对应的 MyBatis SQL 查询语句，其中包含了 `WHERE` 条件判断。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (Java - `PdGoodsTypeServiceImpl.java`)**
    ```java
    @Override
    public Page<PdGoodsType> findByPage(Integer page, Integer pageSize, String name, String truckTypeId, String truckTypeName) {
        Page<PdGoodsType> pdPage = new Page<>(page, pageSize);
        // ... 其他业务逻辑
        return pdPage;
    }
    ```
    *   该方法用于实现分页查询，接收多个查询参数并返回一个分页对象。

*   **代码片段 2 (MyBatis SQL)**
    ```sql
    <if test="truckTypeName != null">
        AND truck_type.name LIKE CONCAT('%', #{truckTypeName}, '%')
    </if>
    ```
    *   这是 MyBatis XML 映射文件中的动态 SQL 片段，用于根据 `truckTypeName` 参数构建查询条件。

*   **Swagger UI 接口参数**
    *   **接口路径**: `/base/goodsType/page`
    *   **查询参数**:
        *   `name` (string, required): 货物类型名称。
        *   `page` (Integer, required): 当前页码。
        *   `pageSize` (Integer, required): 每页记录数。
        *   `truckTypeId` (string, query): 卡车类型ID。
        *   `truckTypeName` (string, query): 卡车类型名称。

*   **响应数据结构 (JSON)**
    ```json
    {
        "counts": 1,
        "pageSize": 5,
        "page": 1,
        "items": [
            {
                "id": "1230412847457895680",
                "name": "食品",
                "defaultWeight": 10,
                "defaultVolume": 10,
                "remark": "食品类商品",
                "truckTypeId": "123103137595676608",
                "status": 1
            }
        ]
    }
    ```
    *   `counts`: 总记录数。
    *   `pageSize`: 每页记录数。
    *   `page`: 当前页码。
    *   `items`: 当前页的数据列表。

---

### 4) 关键场景与演示描述

*   **场景 1：后端分页逻辑实现**
    *   **描述**：演示者在 IntelliJ IDEA 中定位到 `PdGoodsTypeServiceImpl.java` 文件，高亮显示了 `findByPage` 方法。该方法接收分页参数和查询条件，并通过 `Page` 对象封装返回结果，体现了 Spring Data JPA 或 MyBatis 的分页查询能力。

*   **场景 2：Swagger UI 分页查询**
    *   **描述**：演示者在 Swagger UI 中点击 `/base/goodsType/page` 接口，填写 `page=1` 和 `pageSize=5`，点击“Execute”后，成功返回了包含 1 条记录的分页数据。这验证了后端分页功能的正确性。

*   **场景 3：带条件的分页查询**
    *   **描述**：演示者在 Swagger UI 中将 `name` 参数设置为“食品”，并执行查询。返回结果中 `items` 数组只包含名称为“食品”的记录，证明了查询条件的有效性。

*   **场景 4：多条件组合查询**
    *   **描述**：演示者在 Swagger UI 中同时设置了 `name` 为“食品”和 `truckTypeId` 为 `123103137595676608`。执行后，返回的数据只包含同时满足这两个条件的记录，展示了接口支持多条件组合查询的能力。

*   **场景 5：文档与代码对照**
    *   **描述**：演示者切换到 Typora 文档，展示了 `GoodsTypeController` 中 `findAll` 方法的注解和对应的 MyBatis SQL 查询。这为理解后端实现提供了文档支持，也展示了开发中常用的注释和 SQL 映射方式。
