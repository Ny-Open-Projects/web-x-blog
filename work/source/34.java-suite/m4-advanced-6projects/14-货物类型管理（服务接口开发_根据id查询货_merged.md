# 14-货物类型管理（服务接口开发_根据id查询货 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们这个接口开发,也就是根据ID来查询货物类型。

刚才我们这个controller当中已经把这个find by ID这个方法已经写好了,对吧?

并且我们是不是在这个service接口里边扩展了这么一个叫做find all这么一个方法。

那么接下来我们就需要还差最后一点,就是需要把这个方法给它实现出来,对吧?

那么这个只是在接口当中定义的方法,然后在我们这个实现类里边,我们需要把它实现出来。

那么实现这个方法,要实现这个方法其实也比较简单,我们直接使用什么呢?

使用一个叫LambdaQueryViper,对吧?

使用这个接口来帮我们进行这个条件的封装就可以了,条件的封装。

因为我们有可能根据它来查,也有可能根据它来查,对吧?

所以我们在这个地方是一个动态的封装这个条件对象。

首先我们需要先把这个条件对象把它创建一下,封装这个条件对象。

这个条件对象我们前面应该都使用过了,叫做LambdaQueryViper。

这是MyBettingPlus给咱们提供的这么一个对象,对吧?

就是用来封装我们的查询条件的。

然后这个对象里边需要指定一个范形,对吧?

这个范形的话是不是应该就是我们这个关联对象,就是对应的这个关联对象。

PD,TrunkType,GhostType。

然后我们这个对象名字就叫什么呢?

LambdaQueryViper吧。

好。

我们扭出来就可以了,扭一个LambdaQueryViper。

扭出来之后呢,是不是就需要来封装条件了,封装条件。

但是这个条件是动态的。

比如说我们传进来的这个传个TypeID,对吧?

它如果不等于空,不等于空的话呢,我们是不是就需要把它作为一个条件来封装。

那么同理啊,这个GhostTypeID也是这个意思。

所以我们在这儿呢,先来判断一下。

先来判断一下,if什么呢?

我们这个使用StringUtils,只叫来判断字符串,是否为空就可以了。

StringUtils点什么呢?

叫做isNotEmpty,对吧?

然后呢,先判断这个传个TypeID吧,传个TypeID。

如果它不等于空,对吧?

不等于空的话呢,我们是不是就需要来干什么?

封装我们的查询条件了。

条件。

那么这个条件呢,是不是就是根据这个传个TypeID来查。

你看我们这里面是不是指定的这个范形是它,

而它这里面是不是确实有一个传个TypeID。

所以说我们在这儿呢,如何来封装呢?

那么跟我们前面的讲法应该都,写法都是一样的。

直接使用什么呢?

LambdaQueryViper,也就是我们定义出来的这个条件对象。

然后呢,来添加一个条件。

这个呢,应该是一个等值查询,对不对?

根据ID呢,肯定一般都是等值查询。

等值的话是不是就是Echo,相等。

然后呢,我们第一个参数呢,第一个参数指定什么呢?

就是根据哪个条件来查,对吧?

根据哪个条件来查呢?

是不是就是通过我们PD,传个Type,

GhostType,然后呢来指定。

但是这个ID的话呢,不要写错了,应该是这个。

传个TypeID,对吧?

传个TypeID。

看一下这个写法,传个TypeID,

只要复制过来,不要写错了。

这是第一个参数,对吧?

第一个参数。

然后呢,接下来第二个参数呢,

第二个参数就是指定我们的值,

这个值呢,就是我们传过来的这个值,对吧?

OK。

当然了,你这样的话,得写get方法,对吧?

这个不是直接写的它属性,应该是写的是get。

get这个什么,传个TypeID。

这样的话呢,它就可以,

知道我们应该根据哪个条件来查了,对吧?

根据的是这个传个TypeID来查。

然后呢,具体我们传进来的值呢,

就是我们这个参数传过来的这个值。

这样的话,我们是不是相当于就封装了这么一个条件。

这个条件呢,就是根据这个传个TypeID来查,等值查询。

那么同理啊,我们其实对于这个GhostTypeID呢,也是这个意思。

所以我们直接复制一下就可以了。

直接复制一下。

然后呢,把这个地方呢,改成GhostTypeID。

好,GhostTypeID。

但是这个地方呢,也得改成get什么呢,GhostTypeID。

OK。

这样的话呢,我们又封装了一个条件,对吧?

然后封装完条件之后呢,就可以直接调用什么呢?

调用我们这个baseMapper。

baseMapper,它的什么呢,selectList的方法,对吧?

然后呢,它传进来的就是我们这个LambdQueryViper这个对象。

好。

那这样的话呢,我们是不是就可以动态地来封装这两个条件,

并且根据这两个条件是不是来进行一个查询。

这个地方我们再简单说一句啊,就是这个baseMapper从哪来的,

你看我们是不是并没有去定义它。

是因为baseMapper呢,它其实是我们继承过来的,对吧?

是我们继承过来的。

在这里边呢,是不是应该就有baseMapper。

所以我们直接就可以用它了。

好,那么到这儿的话呢,我们这个代码呢,就已经都写完了。

一会儿呢,我们可以来测试一下。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段来自一个关于 Spring Boot + MyBatis-Plus 的 Java 后端开发教程。讲师正在演示如何实现一个“车辆类型与货物类型关联信息”的查询功能。核心内容包括：
- 在 `GoodsTypeController` 中，通过 `@PathVariable` 接收 `id` 参数，调用服务层查询关联数据。
- 服务层 `PdTruckTypeGoodsTypeServiceImpl` 中，使用 `LambdaQueryWrapper` 构建动态查询条件。
- 查询条件根据传入的 `truckTypeId` 和 `goodsTypeId` 进行筛选。
- 最终通过 `baseMapper.selectList()` 执行数据库查询并返回结果。
- 教程中还展示了如何处理空值（`StringUtils.isEmpty`）和使用 MyBatis-Plus 的 `eq` 方法进行等值查询。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：展示 `GoodsTypeController` 中的 `findById` 方法，用于根据 ID 查询货物类型信息。
*   **00:05 - 00:10**：在 `findById` 方法中，讲师注释了需要查询关联的车辆类型信息，并调用 `truckTypeGoodsTypeService.findAll(...)`。
*   **00:10 - 00:15**：切换到 `PdTruckTypeGoodsTypeService` 接口，查看其 `findAll` 方法的定义，该方法接收 `truckTypeId` 和 `goodsTypeId` 两个参数。
*   **00:15 - 00:20**：进入 `PdTruckTypeGoodsTypeServiceImpl` 类，讲师开始实现 `findAll` 方法。
*   **00:20 - 00:25**：在 `findAll` 方法中，讲师使用 `LambdaQueryWrapper` 封装查询条件。
*   **00:25 - 00:30**：讲师使用 `StringUtils.isNotEmpty` 判断 `truckTypeId` 是否为空，如果为空则直接返回 `null`。
*   **00:30 - 00:35**：讲师使用 `eq` 方法为 `LambdaQueryWrapper` 添加 `truckTypeId` 的等值查询条件。
*   **00:35 - 00:40**：讲师同样为 `goodsTypeId` 添加等值查询条件。
*   **00:40 - 00:45**：讲师调用 `baseMapper.selectList(lambdaQueryWrapper)` 执行查询。
*   **00:45 - 00:50**：讲师展示了 `batchSave` 方法的实现，用于批量保存关联数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1 (Controller)**：
    ```java
    @GetMapping("/{id}")
    public GoodsTypeDto findById(@PathVariable(name = "id") String id) {
        PdGoodsType pdGoodsType = goodsTypeService.getById(id);
        GoodsTypeDto goodsTypeDto = new GoodsTypeDto();
        BeanUtils.copyProperties(pdGoodsType, goodsTypeDto);
        // 还需要查询当前货物类型关联的车辆类型的id
        List<PdTruckTypeGoodsType> list = truckTypeGoodsTypeService.findAll(null, id);
        if (list != null && list.size() > 0) {
            List<String> truckTypeId = list.stream().map(PdTruckTypeGoodsType::getTruckTypeId)
                    .collect(Collectors.toList());
            goodsTypeDto.setTruckTypeIds(truckTypeId);
        }
        return goodsTypeDto;
    }
    ```

*   **关键代码片段 2 (Service Interface)**：
    ```java
    public interface PdTruckTypeGoodsTypeService extends IService<PdTruckTypeGoodsType> {
        // 批量保存
        void batchSave(List<PdTruckTypeGoodsType> pdTruckTypeGoodsTypes);
        // 根据车辆类型或者货物类型查询关联信息
        List<PdTruckTypeGoodsType> findAll(String truckTypeId, String goodsTypeId);
    }
    ```

*   **关键代码片段 3 (Service Implementation)**：
    ```java
    @Override
    public List<PdTruckTypeGoodsType> findAll(String truckTypeId, String goodsTypeId) {
        LambdaQueryWrapper<PdTruckTypeGoodsType> lambdaQueryWrapper = new LambdaQueryWrapper<>();
        if (StringUtils.isNotEmpty(truckTypeId)) {
            lambdaQueryWrapper.eq(PdTruckTypeGoodsType::getTruckTypeId, truckTypeId);
        }
        if (StringUtils.isNotEmpty(goodsTypeId)) {
            lambdaQueryWrapper.eq(PdTruckTypeGoodsType::getGoodsTypeId, goodsTypeId);
        }
        return baseMapper.selectList(lambdaQueryWrapper);
    }
    ```

*   **关键代码片段 4 (Entity)**：
    ```java
    @TableName("pd_truck_type_goods_type")
    public class PdTruckTypeGoodsType implements Serializable {
        @TableId(value = "id", type = IdType.INPUT)
        private String id;
        @TableField(value = "truck_type_id")
        private String truckTypeId;
        @TableField(value = "goods_type_id")
        private String goodsTypeId;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1：控制器层调用服务层**
    讲师在 `GoodsTypeController` 中，通过 `@GetMapping("/{id}")` 注解定义了一个 REST 接口。当接收到一个 `id` 参数时，它会调用 `goodsTypeService.getById(id)` 获取货物类型信息，然后调用 `truckTypeGoodsTypeService.findAll(null, id)` 来获取与该货物类型关联的所有车辆类型 ID，并将这些 ID 设置到返回的 `GoodsTypeDto` 对象中。

*   **场景 2：构建动态查询条件**
    讲师在 `PdTruckTypeGoodsTypeServiceImpl` 中，使用 `LambdaQueryWrapper` 来构建查询条件。他首先检查 `truckTypeId` 是否为空，如果非空，则调用 `eq` 方法添加 `truckTypeId` 的等值查询条件。接着，他同样检查 `goodsTypeId` 是否为空，并添加对应的等值查询条件。

*   **场景 3：执行数据库查询**
    在构建好查询条件后，讲师调用 `baseMapper.selectList(lambdaQueryWrapper)` 方法。这个方法会根据 `LambdaQueryWrapper` 中的条件，向数据库发送查询语句，并返回符合条件的 `PdTruckTypeGoodsType` 对象列表。

*   **场景 4：处理空值和异常**
    讲师在代码中使用 `StringUtils.isNotEmpty` 来判断参数是否为空，这是一种良好的编程实践，可以避免在查询时传入空值导致的潜在问题。如果参数为空，他选择直接返回 `null`，这在某些业务场景下是合理的。

*   **场景 5：IDE 交互与调试**
    教程中，讲师多次使用 IntelliJ IDEA 的智能提示功能（如 `eq` 方法的自动补全），这有助于开发者快速编写正确的代码。同时，他也展示了如何在代码中添加注释，以提高代码的可读性。
