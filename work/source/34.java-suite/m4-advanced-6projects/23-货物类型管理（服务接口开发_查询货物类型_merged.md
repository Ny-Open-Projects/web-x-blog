# 23-货物类型管理（服务接口开发_查询货物类型 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才咱们这个

根据多个ID对吧

也就是根据这个ID集合

查询货物类型列表呢

整个代码都已经写完了

并且呢我现在这个服务呢

也已经启动完了

因为这个启动过程呢

还是比较慢的

所以我这提前已经启动好了

那接下来呢

我们就来测试一下就可以了

好 重新刷新一下

咱们这个Swagger文档这个页面

然后呢把这个方法刷出来

就这个 对吧

这个get方式请求

查询货物类型列表

好 然后呢我们可以

try it out点这个按钮

但是这个ID呢

我们其实可以不用传啊

不用传的话

其实就是查所有对吧

那就是没有

那相当于没有添加这个条件

那就查所有这个货物类型

咱们可以来看一下

直接点execute

好 你看它是不是查出来的

就是这应该是所有的货物类型

当然我们也可以传

比如我把这个ID呢复制一下

然后点add item添加一个

对吧

然后呢我还

可以添加多个啊

比如我再来一个

好 直接点execute

这样的话呢

它是不是就根据我们传过去的ID来查

因为我传过去的两个

所以查出来的就是这两个

对吧

那么这个是没什么问题的

那么到这儿的话呢

关于我们这个什么呢

查询货物类型列表啊

就已经写完了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段演示了一个基于 Spring Boot 的后端服务中，如何实现一个根据多个 ID 查询货物类型列表的 RESTful API。演示内容分为两部分：
1.  **代码层面**：在 IntelliJ IDEA 中展示了 `GoodTypeController` 控制器类中的 `findALL` 方法的实现。该方法接收一个 `ids` 参数（类型为 `List<String>`），通过 `Stream` 流处理，调用 `truckTypeGoodsTypeService` 获取与卡车类型关联的货物类型数据，并将结果映射、转换为 `GoodsTypeDto` 对象列表返回。
2.  **接口测试层面**：通过 Swagger UI（`/swagger-ui.html`）对上述接口进行测试。演示了如何通过 Swagger 的图形界面输入多个 ID，发送 GET 请求，并查看返回的 JSON 数据。整个过程验证了接口的正确性和数据转换逻辑。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下按画面切换顺序进行描述：

*   **00:00 - 00:02**: 展示 IntelliJ IDEA 开发环境，聚焦于 `GoodTypeController.java` 文件。代码中定义了 `@GetMapping` 注解的 `findALL` 方法，其参数为 `@RequestParam(name = "ids", required = false) List<String> ids`。
*   **00:02 - 00:04**: 代码滚动，展示 `findALL` 方法的完整实现。核心逻辑是：如果 `list` 不为空，则使用 `stream().map()` 将 `PdGoodsType` 对象转换为 `GoodsTypeDto` 对象，并通过 `BeanUtils.copyProperties` 进行属性拷贝，最后收集为 `List<GoodsTypeDto>` 返回。
*   **00:04 - 00:06**: 切换到浏览器，显示 Swagger UI 页面正在加载。
*   **00:06 - 00:08**: Swagger UI 加载完成，显示“品达物流管理后台基础数据--Swagger文档”页面，其中列出了 `Goods Type Controller` 的所有接口。
*   **00:08 - 00:10**: 选中并展开 `GET /base/goodsType` 接口，查看其参数和响应信息。
*   **00:10 - 00:12**: 在 Swagger UI 的参数输入框中，点击“Add Item”按钮，添加一个 ID 参数。
*   **00:12 - 00:14**: 输入第一个 ID `1230685120449613824`，点击“Execute”按钮发送请求。
*   **00:14 - 00:16**: 展示请求成功后的响应结果，返回了包含该 ID 对应货物类型数据的 JSON。
*   **00:16 - 00:18**: 在参数输入框中，再次点击“Add Item”按钮，添加第二个 ID。
*   **00:18 - 00:20**: 输入第二个 ID `12306856064790176`，点击“Execute”按钮发送请求。
*   **00:20 - 00:22**: 展示请求成功后的响应结果，返回了包含两个 ID 对应货物类型数据的 JSON。
*   **00:22 - 00:24**: 切换到 Typora 文档，显示了与视频演示内容相对应的文档章节“3.4.5 查询货物类型列表”，并展示了代码注释和实现逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码 (Java)**:
    *   **控制器方法**:
        ```java
        @GetMapping("**")
        @ApiOperation(value = "查询货物类型列表")
        public List<GoodsTypeDto> findALL(@RequestParam(name = "ids", required = false) List<String> ids) {
            if (list != null && list.size() > 0) {
                List<GoodsTypeDto> goodsTypeDtoList = list.stream().map(pdGoodsType -> {
                    List<PdTruckTypeGoodsType> truckTypeGoodsTypes = truckTypeGoodsTypeService.findAll(null, pdGoodsType.getId());
                    List<String> truckTypeIds = truckTypeGoodsTypes.stream().map(PdTruckTypeGoodsType::getTruckTypeId).collect(Collectors.toList());
                    GoodsTypeDto goodsTypeDto = new GoodsTypeDto();
                    BeanUtils.copyProperties(pdGoodsType, goodsTypeDto);
                    goodsTypeDto.setTruckTypeIds(truckTypeIds);
                    return goodsTypeDto;
                }).collect(Collectors.toList());
                return goodsTypeDtoList;
            }
            return null;
        }
        ```
    *   **文档中的伪代码/注释**:
        ```java
        // 第一步：在GoodTypeController中创建findALL方法
        @ApiOperation(value = "获取货物类型列表")
        public List<GoodsTypeDto> findALL(@RequestParam(name = "ids", required = false) List<String> ids) {
            return goodTypeService.findAll(ids).stream().map(pdGoodsType -> {
                BeanUtils.copyProperties(pdGoodsType, dto);
                dto.setTruckTypeIds(truckTypeGoodsTypeService.findAll(null, pdGoodsType.getId()).stream().map(PdTruckTypeGoodsType::getTruckTypeId).collect(Collectors.toList()));
                return dto;
            }).collect(Collectors.toList());
        }
        ```

*   **图表/界面**:
    *   **Swagger UI 界面**: 展示了 API 的参数、响应和测试功能。
    *   **IDEA 项目结构**: 展示了 `pom.xml`、`application.yml`、`GoodTypeController.java` 等文件的结构。

---

### 4) 关键场景与演示描述

1.  **场景一：接口开发与实现**
    *   **描述**: 开发者在 IntelliJ IDEA 中编写 `GoodTypeController` 的 `findALL` 方法。该方法接收一个 `ids` 参数，用于查询多个货物类型的详细信息。方法内部通过 `Stream` 流处理，调用 `truckTypeGoodsTypeService` 获取与每个货物类型关联的卡车类型 ID，并将所有数据转换为 `GoodsTypeDto` 对象列表返回。
    *   **技术要点**: 使用了 `@RequestParam` 注解接收前端传入的 `ids` 参数（类型为 `List<String>`），使用 `Stream` 流进行数据处理，使用 `BeanUtils.copyProperties` 进行对象属性拷贝，使用 `Collectors.toList()` 收集结果。

2.  **场景二：接口测试与验证**
    *   **描述**: 通过 Swagger UI 对 `GET /base/goodsType` 接口进行测试。用户在参数输入框中输入一个或多个 ID，点击“Execute”按钮发送请求。系统返回包含对应货物类型数据的 JSON 响应。
    *   **技术要点**: 使用 Swagger UI 进行接口测试，验证了接口的参数传递和数据返回功能。演示了如何通过前端传递多个 ID，并成功获取到对应的数据。

3.  **场景三：文档与代码对照**
    *   **描述**: 视频最后切换到 Typora 文档，展示了与代码实现相对应的文档内容。文档中详细描述了 `findALL` 方法的实现步骤和逻辑，与代码中的注释和实现保持一致。
    *   **技术要点**: 通过文档与代码的对照，帮助学习者理解接口的业务逻辑和实现细节。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
