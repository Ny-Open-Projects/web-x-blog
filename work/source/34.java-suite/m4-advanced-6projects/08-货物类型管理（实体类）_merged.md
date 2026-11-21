# 08-货物类型管理（实体类） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们货物类型的管理

接下来我们要做的就是导入实体类

因为我们刚才看到了

咱们最终要操作的是这么一张表

那么跟这张表对应的

是不是应该有一个实体类

这个实体类我们就叫做PD Goose Type

PD Goose Type

这叫货物类型

然后这里边的属性跟咱们表里面的字段

都是一一对应的

所以这个类的话

我们直接把它抄过来就可以了

这是一个实体类

然后我们先把这个包结构给它创建一下

在品达下边我们创建这么两层目录

一个叫做Entity

然后下边是Base

然后我们到这边品达下边

然后我们创建这么两层目录

然后在这个Base下边来创建咱们这个实体类

这个实体类的名字我就不写了

直接抄过来

这叫做PD Goose Type

这个对应的就是我们的

叫做货物类型

实体

然后所涉及到的这些属性

我们都给它抄过来

然后别忘了

还需要实现什么

实现一个虚拟化接口

Serializable

然后我们这个get set的方法

就不用自己写了

因为我们使用的Lambook

所以说我们在这个地方

直接加一个什么

Data注解就可以了

这样的话

它是不是相应的我们的get set的方法

还有常用的什么构造方法等等

这些是不是全都有了

所以说直接加它就可以了

这可以大大简化我们代码量

然后我们这个实体类的话

是不是还需要跟某张表有一个映射关系

所以说我们在这需要来加入这么一个叫做什么

叫做table name

table name

这是myBasePlus给咱们提供的这么一个注解

然后来指定我们当前这个类

这个实体跟哪个表对应

跟那个表对应了

是不是就是我们这个PD Goose Type

PD

注意是显示的

PD是下滑线

不要写错了

Goose Type

这是咱们的表名

这样的话就映射好了

然后呢

我们这个ID的话

你注意看

它是不是通过table ID来描述

这就是我们ID属性跟表里面的这个字段

是不是有个对应关系

并且呢

它这个type ID生成的是什么呢

需要我们是不是给它来指定

就是input

然后呢

下面这些的话

你看我我们是不是没有去写

就是因为我们当前这个属性啊

是不是跟咱们

表里面的字段完全一致

所以说这个时候呢

你可以不再加注解

好

因为它是完全对应的

OK

那么到这的话呢

我们这个实体类呢

是不是就已经导入成功了

这个还是非常简单的

然后呢

除了这个实体类之外呢

其实还有一个叫做PD什么Trunk Type

Goose Type

对吧

这么两个实体类

这个对应的是什么呢

其实对应的是我们的关联表

因为呢

我们前面

其实也提到过了

就是我们的货物类型

是不是跟我们的这个什么呢

车辆类型是不是有对应关系

也就是说什么样的货物还需要用什么样类型的车去拉

对吧

他们应该有这么一个对应关系

所以说呢

我们这个实体呢

还需要再有一个啊

就是这个叫做PD Trunk Type

Goose Type

那么它映射的是哪张表呢

映射的就是这个PD Trunk Type

Goose Type

映射的其实是那个中间的关系表

对吧

中间的关系表好

所以我们需要把这个实体类的关系表呢

实体呢

也创建出来

好

看看它放在哪个包下面啊

它是在这个

在这个Trunk包下面

所以说呢

我们在这个Entity下面再创建一个新的包

叫做Trunk

Trunk呢

翻译过来就是车辆的意思啊

车辆的意思

然后呢

这下面呢

我们来创建这个类

所以说呢

我们你看真正在开发业务代码之前呢

其实呢

这些准备工作都要做好

好

然后呢

我们同样让它去实现什么呢

实现咱们这个

虚拟化接口啊

Serializable

好

这个实体呢

它其实是什么呢

是我们这个车辆

是车辆类型对吧

车辆类型和什么呢

和我们这个货物类型对吧

货物类型这个对应关系啊

对应关系

或者叫做关联关系都可以

同样呢

我们这个地方呢

也给它加一个什么呢

Data注解

这样我们的Get Set的方法

对吧

就都有了

然后呢

这个地方呢

也得需要一个Table Name

对吧

来映射一下

映射

映射哪张表呢

这个表名比较长啊

咱们直接抄过来吧

不要写错了

映射的是这个中间关系表

好

PD

Trunk Type

Goose Type

好

然后呢

这里边的属性呢

其实跟咱们表里边的字段呢

肯定都是一一对应的

直接拿过来

好

就这么三个属性对吧

一个是ID

主件

还有一个是Trunk Type ID

还有一个是Goose Type ID

好

你看可以看一下咱们前面说到的这个表结构呢

肯定也是这个样子的

你看是不是就是这么三个字的ID

然后Trunk Type ID

还有Goose Type ID

好

OK

那么这个块呢

我们这个实体类呢

也就提供好了

实体类提供好之后呢

我们一会儿呢

就可以进行什么呢

我们相关的这个接口开发

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告：

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的Java后端开发教程，具体聚焦于“基础数据服务”模块中的“货物类型管理”功能。讲师通过演示如何将数据库表结构（`pd_goods_type`）映射为Java实体类（`PdGoodsType`），并进一步创建关联实体类（`PdTruckTypeGoodsType`）和对应的控制器接口（`GoodsTypeController`），来实现货物类型数据的增删改查功能。整个过程使用了IntelliJ IDEA开发环境，并结合了MyBatis-Plus、Lombok等主流Java框架和工具，展示了从数据库设计到代码实现的完整开发流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: **章节 3.2 数据模型**。讲师首先展示了数据库表 `pd_goods_type` 的结构，包括字段 `id`, `name`, `default_weight`, `default_volume`, `remark`, `status` 及其数据类型和约束。
*   **00:05 - 00:15**: **章节 3.3 导入实体类**。讲师开始编写Java实体类 `PdGoodsType`，并演示了如何使用 `@TableName` 和 `@TableId` 注解将数据库表和字段映射到Java类。
*   **00:15 - 00:25**: **章节 3.3 导入实体类（续）**。讲师继续编写 `PdGoodsType` 类，添加了 `name`, `defaultWeight`, `defaultVolume`, `remark`, `status` 等字段，并使用 `@TableField` 注解进行映射。
*   **00:25 - 00:35**: **章节 3.3 导入实体类（续）**。讲师演示了如何使用 `@Data` 注解（来自Lombok）自动生成getter、setter等方法，简化了实体类的编写。
*   **00:35 - 00:45**: **章节 3.3 导入实体类（续）**。讲师切换到另一个实体类 `PdTruckTypeGoodsType`，用于关联车辆类型和货物类型，同样使用了 `@TableName` 和 `@TableId` 注解。
*   **00:45 - 00:55**: **章节 3.3 导入实体类（续）**。讲师在 `PdTruckTypeGoodsType` 类中添加了 `truckTypeId` 和 `goodsTypeId` 字段，用于建立车辆与货物的关联。
*   **00:55 - 01:05**: **章节 3.4 服务接口开发**。讲师开始编写控制器层代码，创建 `GoodsTypeController` 类，并导入了相关的DTO、Service和实体类。
*   **01:05 - 01:15**: **章节 3.4 服务接口开发（续）**。讲师在 `GoodsTypeController` 中定义了 `saveGoodsType` 方法，用于处理新增货物类型请求。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   **章节标题**: “3.2 数据模型”、“3.3 导入实体类”、“3.4 服务接口开发”。
    *   **数据库表结构**: `pd_goods_type` 表的字段列表，包括 `id`, `name`, `default_weight`, `default_volume`, `remark`, `status` 及其数据类型和约束。
    *   **Java实体类代码**:
        *   `PdGoodsType` 类：包含 `id`, `name`, `defaultWeight`, `defaultVolume`, `remark`, `status` 字段，并使用 `@TableName`, `@TableId`, `@TableField` 注解。
        *   `PdTruckTypeGoodsType` 类：包含 `id`, `truckTypeId`, `goodsTypeId` 字段，并使用 `@TableName`, `@TableId` 注解。
    *   **控制器代码**:
        *   `GoodsTypeController` 类：包含 `saveGoodsType` 方法，用于处理新增货物类型请求。

*   **代码关键内容**:
    *   **实体类 `PdGoodsType`**:
        ```java
        @Data
        @TableName("pd_goods_type")
        public class PdGoodsType implements Serializable {
            private static final long serialVersionUID = 1L;
            @TableId(value = "id", type = IdType.INPUT)
            private String id;
            private String name;
            private BigDecimal defaultWeight;
            private BigDecimal defaultVolume;
            private String remark;
            private Integer status;
        }
        ```
    *   **实体类 `PdTruckTypeGoodsType`**:
        ```java
        @Data
        @TableName("pd_truck_type_goods_type")
        public class PdTruckTypeGoodsType implements Serializable {
            private static final long serialVersionUID = 1L;
            @TableId(value = "id", type = IdType.INPUT)
            private String id;
            private String truckTypeId;
            private String goodsTypeId;
        }
        ```
    *   **控制器 `GoodsTypeController`**:
        ```java
        package com.iteima.pinda.controller.base;
        import com.iteima.pinda.DTO.base.GoodsTypeDto;
        import com.iteima.pinda.common.utils.Constant;
        import com.iteima.pinda.common.utils.Result;
        import com.iteima.pinda.entity.truck.PdTruckTypeGoodsType;
        import com.iteima.pinda.service.truck.IPdTruckTypeGoodsTypeService;
        import org.springframework.beans.BeanUtils;
        import org.springframework.web.bind.annotation.*;
        @RestController
        @RequestMapping("/goodsType")
        public class GoodsTypeController {
            @Autowired
            private IPdTruckTypeGoodsTypeService pdTruckTypeGoodsTypeService;
            @PostMapping("/save")
            public Result saveGoodsType(@RequestBody GoodsTypeDto goodsTypeDto) {
                // 业务逻辑
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库表结构展示** (00:00-00:05)
    *   讲师在Typora编辑器中展示了 `pd_goods_type` 表的结构，通过表格形式清晰地列出了所有字段、数据类型、长度、是否允许为空等信息，为后续的Java实体类开发提供了依据。

*   **场景二：实体类 `PdGoodsType` 开发** (00:05-00:25)
    *   讲师在IntelliJ IDEA中创建了 `PdGoodsType` 类，并逐步添加了 `@TableName` 和 `@TableId` 注解，将数据库表名和主键字段映射到Java类。
    *   讲师演示了如何使用 `@TableField` 注解为其他字段（如 `name`, `defaultWeight`）添加映射关系。
    *   讲师使用 `@Data` 注解（来自Lombok）自动生成了所有字段的getter、setter方法，大大简化了代码量。

*   **场景三：关联实体类 `PdTruckTypeGoodsType` 开发** (00:25-00:45)
    *   讲师创建了 `PdTruckTypeGoodsType` 类，用于表示车辆类型与货物类型的关联关系。
    *   讲师在类中添加了 `truckTypeId` 和 `goodsTypeId` 字段，并使用 `@TableId` 注解进行映射。
    *   讲师演示了如何使用 `@Data` 注解自动生成getter、setter方法。

*   **场景四：控制器接口开发** (00:45-01:05)
    *   讲师在 `GoodsTypeController` 中定义了 `saveGoodsType` 方法，用于处理新增货物类型请求。
    *   讲师演示了如何使用 `@PostMapping` 注解将HTTP POST请求映射到该方法。
    *   讲师展示了如何使用 `@RequestBody` 注解接收前端传来的JSON数据（`GoodsTypeDto`）。

*   **场景五：代码编辑与调试** (01:05-01:15)
    *   讲师在IntelliJ IDEA中对 `GoodsTypeController` 类进行编辑，添加了必要的导入语句和方法体。
    *   讲师演示了如何使用IDE的代码提示功能，快速定位和添加必要的注解和方法。

---

以上是根据视频画面进行的结构化分析报告，涵盖了视频的主要内容、技术要点和演示过程。
