# 17-货物类型管理（服务接口开发_查询所有货物 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么代码咱们都已经写完了

接下来呢我们来启动一下

测试一下我们查询所有货物类型这个服务接口

还是从这来起一下

好咱们这个服务呢已经启动成功了

没有什么问题

好那接下来呢我们还是到这个页面

咱们来刷新一下

这是刚才我们测试的这个接口

我们重新刷新一下

好来看

它是不是又多出来一个

就是查询所有货物类型

好那接下来呢我们直接来try it out

对吧

直接点exclude

查询

好这样的话应该就把所有的这个货物类型呢

都给我们查出来了

你看这是我们这个返回的

对吧response body

好返回的数据

因为有多个啊

所以它是封成了粒子集合了

那么反到这边呢

就是我们这个json数组

好这样的话呢

我们这个查询也没有什么问题

到这儿的话呢

关于我们查询所有货物类型

就先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的 Java 项目（`pd-base`）中，如何实现一个用于查询所有货物类型的 RESTful API。核心内容包括：
- 在 `GoodsTypeController` 控制器中定义 `@GetMapping("/all")` 接口。
- 通过 `BeanUtils.copyProperties` 方法将服务层返回的 `PdGoodsType` 对象转换为 `GoodsTypeDto` 对象。
- 使用 `Stream` 和 `Collectors.toList()` 对数据进行处理。
- 最终通过 Swagger UI 进行接口测试，验证了接口的正确性。

视频主要演示了从代码编写到接口测试的完整流程，重点在于数据转换和接口调用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:01:00**：展示项目结构和 `GoodsTypeController.java` 文件。讲解了 `@GetMapping("/all")` 方法的作用是查询所有货物类型。
*   **00:01:00 - 00:02:00**：展示代码逻辑，重点讲解 `BeanUtils.copyProperties` 方法用于将 `PdGoodsType` 对象的属性复制到 `GoodsTypeDto` 对象中。
*   **00:02:00 - 00:03:00**：展示 `Stream` 流式处理和 `Collectors.toList()` 方法，用于将 `PdGoodsType` 列表转换为 `GoodsTypeDto` 列表。
*   **00:03:00 - 00:04:00**：切换到 Swagger UI 页面，演示如何通过 Swagger UI 测试 `GET /base/goodsType/all` 接口。
*   **00:04:00 - 00:05:00**：在 Swagger UI 中点击“Execute”按钮，成功调用接口并返回数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **文档标题**：`品达物流管理后台基础数据--Swagger文档`
*   **章节标题**：`3.4.3 查询所有货物类型`
*   **文档内容**：
    *   **第一步**：在 `GoodsTypeController` 中创建 `findALL` 方法。
    *   **第二步**：在 `IPdGoodsTypeService` 接口中扩展 `findALL` 方法。
    *   **第三步**：在 `PdGoodsTypeServiceImpl` 中实现 `findALL` 方法。

#### 代码关键内容

*   **控制器代码 (`GoodsTypeController.java`)**：
    ```java
    @GetMapping("/all")
    @ApiOperation(value = "查询所有货物类型")
    public List<GoodsTypeDto> findAll() {
        List<PdGoodsType> goodsTypeList = goodsTypeService.findAll();
        if (goodsTypeList != null && goodsTypeList.size() > 0) {
            List<GoodsTypeDto> goodsTypeDtoList = goodsTypeList.stream().map(goodsType -> {
                GoodsTypeDto goodsTypeDto = new GoodsTypeDto();
                BeanUtils.copyProperties(goodsType, goodsTypeDto);
                return goodsTypeDto;
            }).collect(Collectors.toList());
            return goodsTypeDtoList;
        }
        return null;
    }
    ```

*   **服务接口代码 (`IPdGoodsTypeService.java`)**：
    ```java
    List<PdGoodsType> findAll();
    ```

*   **服务实现代码 (`PdGoodsTypeServiceImpl.java`)**：
    ```java
    @Override
    public List<PdGoodsType> findAll() {
        // 实现代码
    }
    ```

#### 图表 / 图形界面

*   **IDE 界面**：IntelliJ IDEA，显示了项目结构和代码编辑器。
*   **Swagger UI 界面**：
    *   展示了 `POST /base/goodsType` 和 `GET /base/goodsType/{id}` 接口。
    *   展示了 `GET /base/goodsType/all` 接口，并成功执行后返回了数据。

---

### 4) 关键场景与演示描述

*   **场景一：代码编写与调试**
    *   **描述**：在 IntelliJ IDEA 中，开发者在 `GoodsTypeController.java` 文件中编写了 `@GetMapping("/all")` 方法。代码逻辑包括调用服务层的 `findAll()` 方法获取 `PdGoodsType` 对象列表，然后使用 `Stream` 流式处理，通过 `BeanUtils.copyProperties` 方法将每个 `PdGoodsType` 对象转换为 `GoodsTypeDto` 对象，最后使用 `Collectors.toList()` 方法将转换后的对象列表返回。
    *   **技术点**：展示了 Spring MVC 的 `@GetMapping` 注解、Java Stream API、`BeanUtils.copyProperties` 方法、`Collectors.toList()` 方法。

*   **场景二：接口测试**
    *   **描述**：开发者切换到浏览器，打开 Swagger UI 页面。在 Swagger UI 中，开发者选择了 `GET /base/goodsType/all` 接口，点击“Execute”按钮，成功调用接口并返回了数据。
    *   **技术点**：展示了如何使用 Swagger UI 进行 API 测试，验证了接口的正确性。

*   **场景三：错误处理**
    *   **描述**：在 Swagger UI 中，开发者尝试调用 `GET /base/goodsType/{id}` 接口，但返回了 500 错误，错误信息为 `“Source must not be null”`。
    *   **技术点**：展示了接口在未正确处理参数时可能出现的错误。

---

以上是根据视频画面进行的结构化技术分析。
