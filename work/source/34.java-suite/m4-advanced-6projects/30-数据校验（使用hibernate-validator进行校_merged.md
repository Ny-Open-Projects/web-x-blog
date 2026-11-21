# 30-数据校验（使用hibernate-validator进行校 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

那么刚才呢

我们是对Hibernet Validator

这个框架

所使用到的这些注解

对吧

它给我们提供的这套注解呢

整个过了一遍

那接下来呢

我们就直接使用它

把它应用到我们项目当中来

其实这个框架使用呢

还是非常简单的

就两步就可以了

第一步是什么呢

我们可以修改咱们这个DTO对象

因为这里边呢

是不是封装了我们

货物类型啊

相关的信息

然后呢

我们在这些属性上面呢

来加入相关的注解

就可以了

这是第一步

然后第二步是什么呢

第二步就是

我们在这个地方

比如我们就以这个Controller

的这个Save Goods Type方法为例

对吧

咱们是不是传过来的参数

需要封装成DTO啊

那么这个时候呢

我们希望Hibernet Validator

给我们把这个DTO里边的属性

来进行一个校验

怎么办呢

直接来加这么一个Validated注解

那么这个时候呢

它就会开启校验

对吧

然后呢

看我们这个DTO对象里边

这些属性

对吧

能不能满足要求

具体做什么样的校验呢

就看我们加的什么注解

对吧

你Not Now

是不是就是非空校验

好

所以说就这么两步就可以了

还是非常简单的

好

那接下来呢

我们来看啊

首先呢

我们找到这个DTO

然后呢

在属性上

是不是来加这个注解

就可以了

先把这个DTO呢

找出来

然后呢

咱们呢

就以这个Name为例

对吧

这个Name呢

不能为空

所以说我们在这来

加一个什么Not Now

但是我们需要注意看啊

这个地方呢

它好像并不是我们这个

Habit Native Validator的包

对吧

那么为什么没有

那么我们需要来看一下

咱们当前这个类啊

是在哪个Mainware工程里边

它其实是在我们这个PD Service API

也就是在这个里边

对不对

在这里边的

具体是这个

就是我们这个PD Service Base

Domain

在这个里边

这个呢是一个副工程

它其实是在这个里边

那也就是说

我们当前这个副工程呢

其实并没有去导什么

并没有导入我们这个Habit Native Validator

它的这个Main 坐标

因为前面我们也提到了

在PD Base里边

其实我们是导入了这个什么呢

Web环境

对吧

已经导入了这个Web环境

所以说呢

Habit Native Validator这个框架

这个坐标就已经依赖传递过来了

但是呢

在我们这个什么呢

PD Service API里边

我们是不是并没有导那个Web环境

所以这个时候呢

我们要想使用这个Habit Native Validator呢

就需要显示一下

显示的来导一下它的坐标

好

那么咱们把这个坐标复制过来

直接放在这个副工程上面就可以了

PD Service API

那这样的话

它下面这些子模块是不是就都可以使用了

那么直接把它放在这

这是我们这个Habit Native Validator它的坐标

加上之后呢

但是它需要去下载一下

如果你本地没有

它会下载一下

然后呢

我们到这边来

再来看

它这边是不是自动已经导入了

但是这个是不是不对呀

然后呢

我们把它去掉

然后呢

需要来手动再来导一下

注意看啊

应该是哪呢

是下面这个JavaX Validation

对吧

是这个啊

这是我们Habit Native Validator

使用到的这个

所以是这个

然后还有什么呢

还有一个Status

这个对吧

这个的话呢

我们也把这个注解拷过来啊

这个加的呢

校验的比较多

对吧

一个是不能为空

还有一个是不能为空

还有一个是什么呢

我们这个状态位对吧

Status我们知道它是个状态位

它的取值就两个选择

一个是0

一个是1对吧

如果你给它个2

给它个3

给它个4

其实就没有意义了

所以说呢

我们因为它是个数值型的

所以我们使用Max

指定它最大值是1

然后最小值呢是0

那这样的话它就没有选择

只能选这两个值了

对吧

好

那么我们把这个注解呢

也给它加上

其他的呢

也都是类似的

其他的也都是类似的啊

那么我们

可以挑着来加就可以了

这都根据我们的

是根据我们的业务来定的

所以我们在这呢

就以这个Name

还有Status为例

来加一下就可以

然后加完之后呢

是不是还需要开启啊

要开启的话呢

找到咱们的Controller

具体你要校验对吧

你是在哪个方法这儿校验呢

比如说我们新增的时候

需要校验对吧

新增数据的时候

那这个时候呢

我就需要在这个地方

是不是来加一个什么呢

来加入一个叫做Validated

好

这就表示我要开启校验

好

所以使用起来呢

还是非常简单的

就这么两步对吧

第一步加注解

然后第二步呢

在需要校验的地方

那么加上这个Validated注解

这就表示要开启校验

好

那么这个代码呢

我们就已经改完了

但是其他的增深改查

其他的方法呢

我就不再一个一个去加了

大家可以自己加一下

我这个呢

就以这个新增的方法

也就是添加的这个方法呢

为例啊

好

来加一下就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的Java后端开发教程，具体聚焦于**数据校验**模块。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 Spring Boot 项目中集成并使用 Hibernate Validator 进行数据校验。核心内容包括：
- **第一部分**：修改 `GoodsTypeDto` 数据传输对象（DTO），为其字段添加 `@NotNull`、`@Max`、`@Min` 等 Hibernate Validator 注解，以定义业务规则。
- **第二部分**：在 `GoodsTypeController` 控制器中，使用 `@Validated` 注解和 `@RequestBody` 注解，使 Spring MVC 能够在请求处理前自动触发 DTO 的校验逻辑。
- **第三部分**：展示了如何在 `pom.xml` 中添加 Hibernate Validator 的依赖，并在代码中正确导入相关注解。
整个过程旨在实现对用户输入数据的自动化、标准化校验，以提高代码健壮性和用户体验。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下时间点是根据画面内容和逻辑顺序推断的：

- **0:00 - 0:15**: 视频开场，展示课程大纲，定位到“4.4 使用hibernate-validator进行校验”章节。
- **0:15 - 0:30**: 展示 `GoodsTypeDto` 类的代码，重点讲解 `@NotNull` 注解用于确保 `name` 字段非空。
- **0:30 - 0:45**: 展示 `status` 字段的校验，添加 `@Max(value = 1)` 和 `@Min(value = 0)` 注解，限制其取值范围。
- **0:45 - 1:00**: 切换到 `GoodsTypeController`，演示如何在 `@PostMapping` 方法上添加 `@Validated` 注解，以启用校验。
- **1:00 - 1:15**: 展示 `pom.xml` 文件，演示如何添加 Hibernate Validator 的 Maven 依赖。
- **1:15 - 1:30**: 展示 `GoodsTypeDto` 的完整代码，包括 `@Data`、`@ApiModelProperty` 等注解的使用。
- **1:30 - 1:45**: 展示 `GoodsTypeController` 中的完整方法，包括 `@Autowired` 注入服务、数据拷贝、以及关联数据的处理逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **课程大纲**：
  - 第2章：基础数据服务开发 (pd-base)
    - 4. 数据校验
      - 4.1 数据校验方式
      - 4.2 hibernate validator介绍
      - 4.3 hibernate-validator常用注解
      - 4.4 使用hibernate-validator进行校验
      - 5. 导入基础数据服务其他代码

- **Hibernate Validator 常用注解说明**：
  - `@NotNull`: 不能为 null。
  - `@NotBlank`: 不能为空，检查时会将空格忽略。
  - `@NotEmpty`: 不能为空，这里的空是空字符串。
  - `@Pattern(regexp=...)`: 被注释的元素必须符合指定的正则表达式。
  - `@URL(protocol=..., host, port)`: 检查是否是一个有效的URL，如果提供了protocol, host等，则URL还需满足提供的条件。

#### 代码关键内容

**1. `GoodsTypeDto` 类 (数据传输对象)**

```java
package com.ithema.pinda.DTO.base;

import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import java.io.Serializable;
import java.math.BigDecimal;
import java.util.List;

@Data
public class GoodsTypeDto implements Serializable {

    @ApiModelProperty("主键")
    private String id;

    @ApiModelProperty("物品类型名称")
    @NotNull
    private String name;

    @ApiModelProperty("默认重量")
    private BigDecimal defaultWeight;

    @ApiModelProperty("默认体积")
    private BigDecimal defaultVolume;

    @ApiModelProperty("状态 0: 禁用 1: 正常")
    @NotNull
    @Max(value = 1)
    @Min(value = 0)
    private Integer status;

    @ApiModelProperty("备注")
    private String remark;

    @ApiModelProperty("车辆类型id列表")
    private List<String> truckTypeIds;
}
```

**2. `GoodsTypeController` 类 (控制器)**

```java
@RestController
@RequestMapping("/goodsType")
public class GoodsTypeController {

    @Autowired
    private IPdTruckTypeGoodsTypeService truckTypeGoodsTypeService;

    @PostMapping(value = "添加货物类型")
    public GoodsTypeDto saveGoodsType(@Validated GoodsTypeDto goodsTypeDto) {
        GoodsType pdGoodsType = new PdGoodsType();
        BeanUtils.copyProperties(goodsTypeDto, pdGoodsType);
        pdGoodsType = goodsTypeService.saveGoodsType(pdGoodsType);
        String goodTypeId = pdGoodsType.getId();

        List<String> truckTypeIds = goodsTypeDto.getTruckTypeIds();
        if (truckTypeIds != null && truckTypeIds.size() > 0) {
            List<PdTruckTypeGoodsType> list = truckTypeIds.stream().map(truckTypeId -> {
                PdTruckTypeGoodsType pdTruckTypeGoodsType = new PdTruckTypeGoodsType();
                pdTruckTypeGoodsType.setGoodsTypeId(goodTypeId);
                pdTruckTypeGoodsType.setTruckTypeId(truckTypeId);
                return pdTruckTypeGoodsType;
            }).collect(Collectors.toList());
            truckTypeGoodsTypeService.saveBatch(list);
        }
        return goodsTypeDto;
    }
}
```

**3. `pom.xml` 依赖配置**

```xml
<dependencies>
    <dependency>
        <groupId>io.springfox</groupId>
        <artifactId>springfox-swagger2</artifactId>
    </dependency>
    <dependency>
        <groupId>org.hibernate</groupId>
        <artifactId>hibernate-validator</artifactId>
        <version>6.0.18.Final</version>
    </dependency>
</dependencies>
```

---

### 4) 关键场景与演示描述

- **场景一：数据校验注解的添加**
  - 讲师在 `GoodsTypeDto` 类中，为 `name` 字段添加 `@NotNull` 注解，以确保该字段不能为空。
  - 随后，为 `status` 字段添加 `@Max(value = 1)` 和 `@Min(value = 0)` 注解，以限制其只能在 0 和 1 之间。

- **场景二：控制器方法的校验启用**
  - 讲师在 `GoodsTypeController` 的 `saveGoodsType` 方法上添加 `@Validated` 注解。
  - 这使得 Spring MVC 在处理请求时，会自动对 `@RequestBody` 注入的 `GoodsTypeDto` 对象进行校验。
  - 如果校验失败，会抛出 `MethodArgumentNotValidException` 异常，从而可以统一处理校验错误。

- **场景三：依赖管理**
  - 讲师在 `pom.xml` 文件中，添加了 `hibernate-validator` 的 Maven 依赖。
  - 通过 `groupId`、`artifactId` 和 `version` 指定具体的依赖项，确保项目能正确引入 Hibernate Validator 库。

- **场景四：代码结构与模块化**
  - 讲师展示了项目结构，包括 `pd-service-api`、`pd-service-base-domain` 等模块。
  - 说明了 `GoodsTypeDto` 位于 `pd-service-base-domain` 模块中，而控制器位于 `pd-service-api` 模块中，体现了微服务架构中的模块划分。

- **场景五：数据关联处理**
  - 在控制器方法中，讲师演示了如何处理 `truckTypeIds` 字段。
  - 通过 `stream().map(...).collect(...)` 的方式，将字符串列表转换为 `PdTruckTypeGoodsType` 对象列表，并调用服务层的 `saveBatch` 方法进行批量保存，实现了数据关联的处理。

---

以上是根据视频画面进行的结构化技术分析，旨在帮助理解视频中的核心知识点和操作流程。
