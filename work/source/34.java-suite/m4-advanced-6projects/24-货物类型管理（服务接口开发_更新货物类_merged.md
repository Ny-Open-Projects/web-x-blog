# 24-货物类型管理（服务接口开发_更新货物类 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们服务接口的开发

下一个我们要看的是更新货物类型

这个更新货物类型我们需要先来说一下

除了我们要更新货物类型基本的信息之外

那么也会更新什么呢

货物类型所关联的关联信息

前面我们应该也都写的比较多了

我们货物类型跟车辆类型是不是有一个关联关系

所以我们这个更新的时候

除了这些基本信息要更新

那么关联的车辆类型也有可能是需要更新的

所以说我们在这来看一下咱们这个方法

它的定义传过来了这么两个参数

一个是ID

因为我们根据什么来更新呢

肯定是根据ID来更新货物类型

所以说ID要传过来

然后接下来还有一个DTO对象

就是我们这个GOODS TYPE DTO

这里边封装的除了有我们货物信息

这些基本属性之外

还有关联的信息

关联属性

所以说它都封装在这个里边

那接下来呢

我们把这个方法呢

先来定义一下

还是在咱们这个controller当中

来编写这个方法

public

然后返回值呢

就是我们这个GOODS TYPE DTO

这个对象对吧

这个呢叫做update by ID

然后呢

咱们这个参数啊

直接从我们讲义上考过来就可以了

刚才已经看到了

这么两个参数

一个是ID

这个ID的话呢

咱们是通过这个路径变量对吧

pass variable这样来取一下

还有一个呢就是DTO

而这个DTO的话呢

我们可以看到它这个地方是不是加了这么一个注解

就是这个request body

这说明什么呢

它传过来的时候呢

应该是一个JSON形式的

对吧

然后呢

我们在这儿呢去解析JSON

然后呢把它封装成我们这个DTO对象

这是这个注解它的作用

然后呢

我们在这儿呢

先来加一个注释啊

这个呢就是更新我们这个货物类型信息

更新的话呢

咱们这儿是不是应该这个注解用的是put mapping

对吧

put mapping

然后呢

请求的这个地址呢

跟咱们讲义保持一致啊

就是这块

我们是不是需要把它这个ID啊

传过来

是通过这种路径变量这种方式传过来的

好

这样呢

它自带转义了

这儿就不用管了

好

这么着

好

好

好

就是这个接口啊

已经继承了咱们这个iService接口

对吧

所以说呢

它其实就已经有了这个方法了

那么我们先把它的普通属性更新了

对吧

然后呢

再去考虑它的关联属性

看看怎么更新

好

所以说呢

我们可以分两步来走啊

第一步的话呢

就是什么呢

咱们先把它的普通属性

这个是更新什么呢

我们这个货物类型的普通

属性

所谓普通属性呢

其实就是什么呢

就是除了我们这个关联属性

对吧

这个传个type id

这是关联属性之外的

其他的这些呢

都我们都称为普通属性

这个呢

只是更新它的普通属性

但是呢

它要求传进去的是

我们这个实体对象

对吧

是一个什么呢

是一个pd

goose type

这么一个对象

它要求传的是这么一个对象

而我们现在传过来的呢

实际上是DTO对象

对吧

所以说呢

需要给它来转一下

对吧

需要给它来转一下

咱们可以这样

把我们这个对象呢

先来创建一下

就是我们这个pd

goose type对象

等于new一个pd

goose type

对吧

把它创建出来

然后呢

把咱们这个DTO对象呢

这里面的属性

是不是给它拷贝到

咱们这个对象上面来

好

所以说呢

我们使用这个binutils

点什么呢

copy properties

注意别写反了

这个呢

应该是从

DTO拷贝到什么呢

我们这个pdgoose type

对吧

好

这样的话呢

把这些属性呢

是不是全都拷过来了

对应的呢

是不是还有一个什么呢

还有一个ID对吧

还有一个ID

所以说呢

我们需要把这个ID呢

再单独给它设置一下

把ID再给它单独设置一下

就是这个pdgoose type

点什么呢

set ID

这个ID的话呢

就是我们通过这个路径啊

这种方式传过来了

好

这样的话呢

我们这个pdgoose type呢

整个就已经

封上队了

对吧

封上队之后呢

我们就可以直接调用这个方法

update by id

这个方法呢

我们刚才已经说过了

是继承过来了

然后呢

这样的话

我们这些普通属性呢

其实就已经能够更新成功了

好

那么如果普通属性更新完了之后呢

接下来我们就要考虑什么呢

这个关联属性的更新了

对吧

也就是说下边

就是

更新这个关联

信息

那么关联信息呢

这个就要看什么呢

我们这个DTO对象这里边封装的这个什么呢

tranctype IDs

对吧

所以说呢

我们先把它取出来

先把它取出来

然后再考虑怎么更新

从DTO里边点get这个tranctype IDs

咱们是不是把这个IDs集合给它取到

对吧

然后呢

我们先来判断一下

先来判断一下

如果它不等于空

对吧

if这个tranctype IDs

如果不等于空

同时呢

它的这个size

大于零

好

这个时候呢

就表示啊

我们是不是需要去更新它

对吧

需要去更新它

这个地方

这个关联属性的更新呢

其实它本质上操作的是哪个表了

大家需要注意啊

我们这个地方的操作的肯定是我们这个中间关系表

对不对

因为车辆类型跟货物类型呢

是个多对多的关系

所以呢

更新关联信息呢

其实操作的是关系表

那么

这块我们具体应该如何来更新呢

这块呢

其实操作关系表一般都是这样的

都是什么呢

先把原先的关联关系

是不是先给清理掉

也就是把我们当前这个货物类型

这个ID是不是对应的就是货物类型的ID啊

那么把这个货物类型啊

所关联的所有的车辆

车辆类型全给它清理掉

然后呢

再关联我们这个

tranctype IDs

重新再建立关联

所以这个地方呢

其实是涉及到

两步啊

第一步是干什么呢

先去清理

清理原有对吧

原有这个关联关联信息

其实就是什么呢

就是把我们当前这个货物类型所关联的所有的车辆信息

车辆类型ID全给清理掉

然后呢

再重新建立一次关联关系

重新建立什么呢

关联关系

那么一般呢

都是

分成这么两步来走啊

那么清理原先的关联关系呢

这是不是就需要根据我们传过来这个ID对吧

哎

这个代表的是货物类型ID

然后呢

把这个中间关系表里边啊

这个世界道的数据都给删除掉

根据这个ID作为条件来删除啊

这就是清理原有的关联关系啊

那么这块的话呢

我们是不是就需要使用我们这个service

就是关联关系的这个service对吧

然后呢

在这里边呢

咱们可以提供一个什么呢

delete方法对吧

delete方法

好

然后这个条件传什么呢

哎

其实如果说我们只是这一个地方需要删的话呢

那么我其实只要把这个ID是不是给传进去就可以了

但是呢

我们这个地方呢

最好还是啊

给它设成两个条件

哪两个条件呢

其实对应的就是什么呢

我们这个这个咱们是不是有一个关联信息实体对吧

它这里边的其实封装了两个属性

一个是什么呢

一个是我们的这个车辆类型ID

还有一个是我们的这个

货物类型

是这个货物类型ID

对吧

这两个

所以说呢

我们希望把这两个都作为条件

那也就意味着咱们这个地方回到我们这个service这边来

把这个放大一点

这个删除的话呢

我们传两个参数进来

哎

一个是什么呢

一个是车辆类型ID

还有一个是货物类型ID

这样的话

这个方法是不是功能会更强大一些

第一个呢

比如就是这个车辆类型ID

那么车辆类型ID呢

我们这儿没有

对吧

因为我们在这儿呢

是要清理的是根据什么呢

根据货物类型ID来清理

所以说呢

这个地方呢

我们先来个NOW

然后呢

把这个ID传进去

这个是清理

咱们先把这个方法的定义出来啊

来个public

这儿呢

我们来个string

并且呢

这个地方呢

我们需要给它

这个参数名了

给它写准确一点

就是什么呢

货物类型ID

是这个车辆类型ID

然后第二个呢

是这个货物类型ID

好

这样的

来写一下

这是根据什么呢

车辆类型ID

或者这个货物类型ID来删除

对吧

删除关联关系

关联关系

写明确一点

这两个呢

当然你可以都有值

对吧

好

那么根据这两个条件了

来进行应用

来进行一个删除

一会儿呢

我们再去看具体怎么实现的

对吧

先把这个方法的定义出来

好

定义出来之后呢

回到我们的control了

这边

你看第一个呢

tranctypeID没有

传个空

然后呢

第二个参数呢

就是我们这个ID

ID对应的就是这个

这个货物类型的ID

对吧

好

这样的话呢

我们这个关系呢

就已经清理完了

清理完之后呢

是不是让他重新再建立关联关系

对吧

重新再建立关联关系

那么重新建立关联关系

对吧

那么重新建立关联关系

对吧

重新建立关联关系的话

其实我们当时呢

在写这个什么呢

在写这个新增的时候

其实就已经写过了

咱们这是不是就已经写过了

那么这个其实就是一个批量

批量这个增加对吧

也就是批量保存我们这个车辆的关联关系

所以我们这块呢

其实已经写过了

咱们把这个代码呢

直接给他抄过来

直接把这块抄过来

就可以了

重新建立关联关系

其实跟前面这个是一样的

然后呢

咱们来看一下

你看我们这个传个type id

是不是就是也是从这取到的

对吧

这是从我们DTO里面获取过来的

好

然后呢

stream

然后呢

这块是不是map

然后处理

处理

咱们这个传个type id

是不是传进来

这个对应呢

是不是货物类型id

货物类型id呢

这个地方应该就是这个id

好

然后呢

最终呢

我们是不是返回这个

关联实体对象

对吧

关联实体这个对象

然后呢

最终封装成一个粒子集合

再调用service

是一个批量保存

这样呢

就其实就已经把它保存了

最后呢

咱们把这个DTO对象呢

来返回一下就可以

返回我们这个DTO

好

但是在这需要注意啊

这个DTO对象呢

它这里边是没有设置id的

对吧

所以说呢

我们这块呢

需要把这个DTO呢

也设置一个id

在这个地方

DTO.setid

好

最后呢

把这个DTO呢

返回就可以了

那么呢

那么到这儿的话呢

咱们这个controller这个方法

更新货物类型

对吧

根据id来更新

同时呢

需要这个关联关系也需要更新

对吧

除了这个基本的信息

普通属性来更新之外呢

还有关联信息也要更新

那么这块代码呢

就已经写完了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的 Java Web 项目中，对“货物类型”（GoodsType）数据进行增删改查（CRUD）操作的后端控制器（Controller）层代码实现。视频主要聚焦于 `GoodsTypeController` 类，演示了如何通过 `@PostMapping` 和 `@PutMapping` 注解处理新增和更新请求。核心内容包括：
*   **数据传输对象 (DTO)**：定义了 `GoodsTypeDto`，用于在前端和后端之间传递数据。
*   **控制器方法**：实现了 `saveGoodsType`（新增）和 `updateById`（更新）两个核心方法。
*   **关联关系处理**：重点演示了如何处理“货物类型”与“车辆类型”之间的多对多关联关系。在更新操作中，通过先删除旧关联，再批量创建新关联，来确保数据的一致性。
*   **代码风格与工具**：使用了 `@Autowired` 进行依赖注入，`BeanUtils.copyProperties` 进行属性拷贝，以及 `Stream` API 进行集合操作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 展示项目结构和 `GoodsTypeController.java` 文件的 `findAll` 方法，用于查询所有货物类型。
*   **00:10 - 00:20**: 展示 `updateById` 方法的注解和方法签名，准备实现更新功能。
*   **00:20 - 00:30**: 在 `updateById` 方法中，创建 `PdGoodsType` 对象并使用 `BeanUtils.copyProperties` 拷贝 DTO 中的属性。
*   **00:30 - 00:40**: 调用 `goodsTypeService.updateById` 方法更新货物类型的普通属性。
*   **00:40 - 00:50**: 处理关联关系，获取 DTO 中的车辆类型 ID 列表 `truckTypeIds`。
*   **00:50 - 01:00**: 判断 `truckTypeIds` 是否非空，如果是，则先调用 `truckTypeGoodsTypeService.delete(null, id)` 清理旧的关联关系。
*   **01:00 - 01:10**: 通过 `Stream` API 将 `truckTypeIds` 转换为 `PdTruckTypeGoodsType` 对象列表，并调用 `batchSave` 方法批量保存新的关联关系。
*   **01:10 - 01:20**: 最后，将 `pdGoodsType` 对象的 ID 设置回 DTO，并返回 DTO。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (控制器 - 查询)**:
    ```java
    public List<GoodsTypeDto> findAll(@RequestParam(name = "ids", required = false) List<String> ids) {
        List<GoodsTypeDto> goodsTypeDtoList = list.stream().map(pdGoodsType -> {
            List<String> truckTypeIds = new GoodsTypeDto();
            BeanUtils.copyProperties(pdGoodsType, goodsTypeDto);
            goodsTypeDto.setTruckTypeIds(truckTypeIds);
            return goodsTypeDto;
        }).collect(Collectors.toList());
        return goodsTypeDtoList;
    }
    ```
    *   **说明**: 该方法接收一个 `ids` 参数，用于查询指定 ID 的货物类型。使用 `Stream` API 对查询结果进行转换，将 `PdGoodsType` 对象映射为 `GoodsTypeDto` 对象，并设置其关联的车辆类型 ID 列表。

*   **代码片段 2 (控制器 - 更新)**:
    ```java
    @PutMapping("/{id}")
    @ApiOperation(value = "更新货物类型信息")
    public GoodsTypeDto updateById(@PathVariable(name = "id") String id, @RequestBody GoodsTypeDto dto) {
        PdGoodsType pdGoodsType = new PdGoodsType();
        BeanUtils.copyProperties(dto, pdGoodsType);
        pdGoodsType.setId(id);
        // 更新货物类型的普通属性
        goodsTypeService.updateById(pdGoodsType);
        // 更新关联信息
        List<String> truckTypeIds = dto.getTruckTypeIds();
        if (truckTypeIds != null && truckTypeIds.size() > 0) {
            // 清理原有关联信息
            truckTypeGoodsTypeService.delete(null, id);
            // 重新建立关联关系
            List<PdTruckTypeGoodsType> list = truckTypeIds.stream().map(truckTypeId -> {
                PdTruckTypeGoodsType pdTruckTypeGoodsType = new PdTruckTypeGoodsType();
                pdTruckTypeGoodsType.setGoodsTypeId(id); // 货物类型id
                pdTruckTypeGoodsType.setTruckTypeId(truckTypeId); // 车辆类型id
                return pdTruckTypeGoodsType;
            }).collect(Collectors.toList());
            // 批量保存货物类型和车辆类型的关联信息
            truckTypeGoodsTypeService.batchSave(list);
        }
        return dto;
    }
    ```
    *   **说明**: 这是视频的核心代码。它接收一个 ID 和一个 DTO，首先将 DTO 的属性拷贝到 `PdGoodsType` 实体对象中，并设置 ID。然后调用服务层更新普通属性。接着，它获取 DTO 中的车辆类型 ID 列表，如果列表非空，则先调用 `delete(null, id)` 清理旧的关联，再通过 `Stream` API 将 ID 列表转换为 `PdTruckTypeGoodsType` 对象列表，并调用 `batchSave` 方法批量保存新的关联关系。最后，返回 DTO。

*   **代码片段 3 (DTO 类)**:
    ```java
    @Data
    public class GoodsTypeDto implements Serializable {
        private static final long serialVersionUID = -6890776123674482761L;
        @ApiModelProperty("主键")
        private String id;
        @ApiModelProperty("物品类型名称")
        private String name;
        // 默认重量，单位：千克
        // ...
        private List<String> truckTypeIds; // 车辆类型ID列表
    }
    ```
    *   **说明**: 定义了 `GoodsTypeDto` 类，用于在控制器和前端之间传递数据。它包含了货物类型的基本信息（如 ID、名称）和一个 `truckTypeIds` 列表，用于存储关联的车辆类型 ID。

---

### 4) 关键场景与演示描述

*   **场景 1: 更新操作的入口**
    *   **描述**: 视频首先展示了 `@PutMapping("/{id}")` 注解，表明这是一个用于更新指定 ID 货物类型信息的 HTTP PUT 请求。方法签名 `updateById` 也清晰地表明了其功能。

*   **场景 2: 属性拷贝与普通属性更新**
    *   **描述**: 在方法体内，首先创建了一个 `PdGoodsType` 实例，并使用 `BeanUtils.copyProperties(dto, pdGoodsType)` 将 DTO 中的属性（如名称）拷贝到实体对象中。接着，通过 `pdGoodsType.setId(id)` 设置了主键 ID。最后，调用 `goodsTypeService.updateById(pdGoodsType)` 将普通属性更新到数据库。

*   **场景 3: 关联关系的清理与重建**
    *   **描述**: 这是视频的核心演示部分。代码首先获取了 DTO 中的车辆类型 ID 列表 `truckTypeIds`。接着，通过一个 `if` 判断，如果列表非空，则执行关联关系的清理和重建。
        *   **清理**: 调用 `truckTypeGoodsTypeService.delete(null, id)` 方法，其中 `null` 代表不指定具体的车辆类型 ID，`id` 是货物类型的 ID。这通常用于删除与当前货物类型关联的所有车辆类型记录。
        *   **重建**: 使用 `Stream` API 将 `truckTypeIds` 转换为 `PdTruckTypeGoodsType` 对象列表。每个对象都设置了 `goodsTypeId`（货物类型 ID）和 `truckTypeId`（车辆类型 ID）。最后，调用 `truckTypeGoodsTypeService.batchSave(list)` 方法，将整个列表批量保存到数据库中，从而建立了新的关联关系。

*   **场景 4: 方法返回**
    *   **描述**: 在完成所有操作后，方法最后返回了 `dto`，即更新后的 DTO 对象，以便前端可以获取到最新的数据。

---

以上是根据视频画面进行的结构化技术分析。视频通过代码演示，清晰地展示了如何在 Spring Boot 项目中实现对关联数据的增删改操作。
