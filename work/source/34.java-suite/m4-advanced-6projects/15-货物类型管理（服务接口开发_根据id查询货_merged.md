# 15-货物类型管理（服务接口开发_根据id查询货 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才咱们根据ID查询货物类型

这个代码都已经写完了

但是这忘了写一个API operation

但这个其实你不写也可以

不写的话它就使用默认的

相当于这个地方我们就是这个方法名

这个地方显示的写上更明确一点

但是我们需要说明的就是API operation

这个注解它其实不是必须的

这块我们写好

写好之后我们就可以来启动一下

然后我们可以来测试一下

这已经启动完了

这已经启动完成了

那接下来我们就可以使用咱们这个

打开我们这个Swagger文档

接口文档在这来测试一下

就这个文档

看这个get方法请求

get方式请求这个

根据ID查询货物类型

那么我们可以在这直接来测一下

try it out对吧

然后在这是不是输入一个ID

但是这个ID的话我们不能随便输

是不是需要去找一个真实存在的ID

所以我们可以从这个数据库里面

咱们来找一个

找到我们这个PDBase数据库

然后这里边是不是

直接找咱们这个货物类型表就可以了

货物类型这张表

我们打开这个表

然后就使用咱们这个

数据把这个ID复制过来

这是货物类型的一个ID对吧

然后我们直接贴到这执行

看返回结果

你看它其实已经回来了对吧

已经回来了

那么这里边ID name

这些普通属性就不用管了

最重要的是关联的这个属性

你看传个type IDs

也就是我们当前这个货物类型

那么它对应哪些车辆类型

当然这个记录的是车辆类型的ID

那么也能查到

这样的话我们这个测试呢

是没有问题的

好到这儿的话呢

关于我们根据ID查询货物类型

就说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段主要演示了一个基于 Spring Boot 的微服务项目中，如何实现一个根据货物类型 ID 查询货物类型详情的 RESTful API。讲师通过 IntelliJ IDEA 编辑器展示并讲解了 `GoodsTypeController` 中的 `findById` 方法的代码逻辑，该方法不仅返回货物类型的基本信息，还通过调用 `truckTypeGoodsTypeService` 获取并关联该货物类型所关联的所有车辆类型的 ID。随后，讲师通过 Swagger UI 页面演示了如何调用该 API，并在数据库管理工具中展示了数据表结构，以验证业务逻辑的正确性。整个过程体现了前后端分离、API 文档化（Swagger）以及数据库设计在实际项目开发中的应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示 IntelliJ IDEA 项目结构，聚焦于 `GoodsTypeController.java` 文件。
*   **00:00:05 - 00:00:15**: 讲师在 `GoodsTypeController.java` 中定位并高亮显示 `@GetMapping("/id")` 方法，解释其作用是根据 ID 查询货物类型。
*   **00:00:15 - 00:00:30**: 讲师逐步讲解 `findById` 方法的代码逻辑，包括从服务层获取 `PdGoodsType` 对象、创建 `GoodsTypeDto` 对象并使用 `BeanUtils.copyProperties` 进行属性拷贝。
*   **00:00:30 - 00:00:45**: 讲师重点讲解了如何通过 `truckTypeGoodsTypeService.findAll` 方法查询关联的车辆类型，并使用 Java 8 Stream API 对结果进行处理，最终将车辆类型 ID 列表设置到 `GoodsTypeDto` 对象中。
*   **00:00:45 - 00:00:55**: 讲师在代码中添加了 `return goodsTypeDto;` 语句，完成方法。
*   **00:00:55 - 00:01:05**: 讲师切换到终端，展示 Spring Boot 应用已成功启动。
*   **00:01:05 - 00:01:15**: 讲师打开浏览器，访问 Swagger UI 页面。
*   **00:01:15 - 00:01:30**: 在 Swagger UI 中，讲师定位到 `GET /base/goodsType/{id}` 接口，并准备输入参数。
*   **00:01:30 - 00:01:45**: 讲师在输入框中输入一个具体的货物类型 ID `889255497728`。
*   **00:01:45 - 00:01:55**: 讲师点击“Execute”按钮，执行 API 调用。
*   **00:01:55 - 00:02:05**: 讲师切换到数据库管理工具（如 Navicat），展示 `pd_base` 数据库中的表结构，以验证数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `3.4.2 根据id查询货物类型`
    *   **步骤说明**:
        1.  第一步：在 `GoodsTypeController` 中创建 `findById` 方法。
        2.  第二步：在 `IPdTruckTypeGoodsTypeService` 接口中扩展 `findAll` 方法。

*   **代码关键内容**:
    *   **Controller 方法 (`GoodsTypeController.java`)**:
        ```java
        @GetMapping("/id")
        public GoodsTypeDto findById(@PathVariable(name = "id") String id) {
            PdGoodsType pdGoodsType = goodsTypeService.getById(id);
            GoodsTypeDto goodsTypeDto = new GoodsTypeDto();
            BeanUtils.copyProperties(pdGoodsType, goodsTypeDto);
            // 查询关联的车辆类型ID
            List<PdTruckTypeGoodsType> list = truckTypeGoodsTypeService.findAll(truckTypeId: null, id);
            if (list != null && list.size() > 0) {
                List<String> truckTypeId = list.stream().map(pdTruckTypeGoodsType ->
                        pdTruckTypeGoodsType.getTruckTypeId()
                ).collect(Collectors.toList());
                goodsTypeDto.setTruckTypeIds(truckTypeId);
            }
            return goodsTypeDto;
        }
        ```
    *   **Swagger UI 接口定义**:
        *   **接口路径**: `GET /base/goodsType/{id}`
        *   **参数**: `id` (string, required)
        *   **响应**: `200 OK`

---

### 4) 关键场景与演示描述

*   **场景一：代码编写与调试**
    *   **描述**: 讲师在 IntelliJ IDEA 中，逐行讲解 `findById` 方法的实现。他首先获取数据库中的 `PdGoodsType` 对象，然后创建一个 `GoodsTypeDto` 对象并使用 `BeanUtils.copyProperties` 将数据拷贝过去。接着，他通过 `truckTypeGoodsTypeService.findAll` 方法查询与该货物类型关联的所有车辆类型记录，并使用 `Stream` API 对这些记录进行处理，提取出 `truckTypeId`，最终将这个列表设置到 `GoodsTypeDto` 对象中。整个过程展示了如何在控制器层进行数据聚合和转换。

*   **场景二：API 调用与验证**
    *   **描述**: 讲师启动 Spring Boot 应用后，通过浏览器访问 Swagger UI。他定位到 `GET /base/goodsType/{id}` 接口，输入一个具体的货物类型 ID `889255497728`，并点击“Execute”按钮。系统返回了包含该货物类型信息及其关联车辆类型 ID 的 JSON 数据，成功验证了 API 的功能。

*   **场景三：数据库结构展示**
    *   **描述**: 在演示完 API 后，讲师切换到数据库管理工具，展示了 `pd_base` 数据库中的表结构。这一步是为了让观众了解底层数据表的设计，从而更好地理解业务逻辑是如何在数据库层面实现的。例如，`pd_goods_type` 表存储货物类型信息，`pd_truck_type_goods_type` 表存储货物类型与车辆类型的关联关系。
