# 25-货物类型管理（服务接口开发_更新货物类型 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们这个controller当中啊,这个update by id方法呢,整个都已经写完了。

接下来呢,还差最后一点,就是咱们这个delete方法,对吧。

那么我们到这里边来,看,这个delete方法已经声明好了,接下来呢,我们需要找到它的实现类,对吧。

然后呢,在实现类里边呢,来实现这个delete方法。

好,实现delete方法。

这个是根据什么呢?根据我们这个车辆类型ID,或者什么呢?

这个货物类型的吧,货物类型ID来删除,关联关系啊,关系,好。

然后呢,我们在这呢,需要来看一下,要删除的话呢,咱们需要怎么删除呢?

其实我们可以直接调用什么呢?调用我们这个base mapper,对吧。

它是不是给我们提供的delete方法。

然后呢,这个地方呢,我们是不是就可以直接来调用这个方法。

然后呢,传进来的其实是一个什么呢,vapor对象,对吧。

这个vapor对象呢,

我们就可以,

还是可以使用什么呢?我们这个lambda query viper,对吧。

还是使用这个对象来封装我们的条件。

只不过这个条件呢,它不是用来这个查询的,它是用来删除的。

所以也叫做删除条件。

但是对象呢,还是这个对象。

然后呢,这个类型呢,还是pd trunk type,goose type,这个关联对象,对吧。

先把它拗出来,先把它拗出来。

好,lambda query viper。

然后呢,

我们是不是需要把条件给它传进去,一个是车辆类型ID,

还有一个是货物类型ID。

那么需要注意的是什么呢?

这两个条件啊,如果说都为空,咱们在这儿直接调用这个就可以了。

如果都为空的话,怎么办?

都为空的话,那么我们还能调这个delete方法吗?

注意,不能啊。

如果说都为空的话呢,我们直接调用delete方法,那相当于什么呢?

没有条件,那就是把所有的,把所有的关联关系都给删除掉了。

这肯定是不行的。

所以说,

我们传进来的这两个参数,至少要有一个不为空。

至少要有一个不为空。

那么同时都不为空也可以,但是不能同时都为空。

所以说呢,我们在调这个delete方法之前需要判断,对吧,需要判断。

那也就是说,我们需要来定义啊,咱们定义这么一个board类型的对象。

然后呢,作为判断的依据,叫做是否能执行,对吧,

cad,

execute。

然后默认值呢,我们先给一个false。

然后接下来呢,我们来判断,

delet,

这个什么呢,

这个,

先来车辆类型吧,

如果车辆类型啊,不为空,对吧。

if什么呢,

这个string utils,

点什么呢,

is not empty吧,

is not,

is not empty。

然后呢,把我们这个什么呢,

传个type id啊,传进去。

如果它不为空,对吧,

不为空的话呢,我们是不是就需要啊,

在这个对象里面来加入一个条件,对吧,

来加入一个条件。

这个条件呢,我们就使用eco就可以啊,

因为我们要删的话,

是不是也是,最终这个where条件是一个等值的。

就是这个传个type id等于我们指定的这个值,对不对。

所以说呢,我们需要来封装一下这个条件。

好,这个eco,然后呢,第一个呢,

是不是指定我们这个pd传个type,

然后呢,这儿是不是应该是传个type id,对吧。

然后具体的值呢,就是我们传过来的,

传个type id这个值。

好,这样的话,这个条件是不是就已经封装好了。

然后呢,封装好之后呢,我们就把这个标志位啊,

注意刚才我们刚才定义的这是个标志位,

给它改成,

什么呢,给它改成一个处。

好,然后呢,我们一会儿在执行delete方法的时候呢,

来判断一下,

if什么呢,

这个值,对吧,看它是否为处。

如果是处的话呢,

我们就可以去执行这个了。

好,这其实就是通过这个标志位啊,

来判断一下,

我们这两个参数是否都为空,对吧。

一旦有一个不为空,

我们就把它的值改成处。

这样的话呢,我们就可以放心大胆的去删了。

当然这个呢,只是封装了一个,对吧。

把这个if呢,复制一份。

然后呢,把这个改成什么呢,

改成我们这个货物类型ID,对吧。

goose type ID。

这个值呢,也改成它。

但是这个地方呢,也是get goose type ID了。

那么,

这是这两个条件,

动态去封装,对吧。

那么只要有任意一个不为空,

我们就把这个标志位改成处,

然后呢,在这就可以删了。

好,那么到这儿的话呢,

咱们这个删除方法呢,

就已经写完了。

一会儿呢,我们可以来测试一下。

但是这个删除呢,

指的是删除关联关系,对吧。

到这儿的话,我们整个更新方法就已经写完了。

刚才呢,是写的delete方法,

它的实现过程。

好,那么一会儿呢,我们来测试一下。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段来自一个关于 Spring Boot + MyBatis-Plus 框架的实战教学课程。讲师正在演示如何在 `GoodsTypeController` 中实现一个更新货物类型信息的接口。该接口的核心逻辑是：首先更新货物类型的基本信息，然后根据传入的 `truckTypeIds` 列表，先删除原有的关联关系，再批量创建新的关联记录。讲师在演示过程中，重点讲解了如何在 `PdTruckTypeGoodsTypeService` 服务层中实现 `delete` 方法，以删除指定车辆类型与货物类型的关联关系。讲师通过 IntelliJ IDEA 的代码编辑器，逐步编写并调试了 `delete` 方法，使用了 `LambdaQueryWrapper` 来构建动态 SQL 条件，并通过 `baseMapper.delete` 方法执行删除操作。整个过程体现了典型的 CRUD 操作和关联表数据维护的开发流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示 `GoodsTypeController` 中的 `updateById` 方法，该方法用于更新货物类型信息，并调用 `truckTypeGoodsTypeService.delete` 方法来清理旧的关联数据。
*   **00:05 - 00:10**: 切换到 `PdTruckTypeGoodsTypeServiceImpl` 类，讲师开始编写 `delete` 方法的实现。
*   **00:10 - 00:15**: 在 `delete` 方法中，讲师创建了一个 `LambdaQueryWrapper` 对象，并准备构建查询条件。
*   **00:15 - 00:20**: 讲师使用 `StringUtils.isNotBlank` 方法判断传入的 `truckTypeId` 是否为空，并在条件成立时，使用 `eq` 方法将 `truckTypeId` 设置为查询条件。
*   **00:20 - 00:25**: 讲师添加了 `canExecute` 标志变量，并在条件成立时将其设置为 `true`。
*   **00:25 - 00:30**: 讲师添加了对 `goodsTypeId` 的判断逻辑，如果 `goodsTypeId` 不为空，则将其也设置为查询条件，并将 `canExecute` 标志设为 `true`。
*   **00:30 - 00:35**: 讲师在 `canExecute` 为 `true` 时，调用 `baseMapper.delete` 方法执行删除操作。
*   **00:35 - 00:40**: 讲师在 `GoodsTypeController` 中，演示了如何调用 `truckTypeGoodsTypeService.delete` 方法来删除关联数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **`GoodsTypeController` 中的 `updateById` 方法**:
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
                truckTypeGoodsTypeService.delete(truckTypeId: null, id);
                // 重新建立关联关系
                List<PdTruckTypeGoodsType> list = truckTypeIds.stream().map(truckTypeId -> {
                    PdTruckTypeGoodsType pdTruckTypeGoodsType = new PdTruckTypeGoodsType();
                    pdTruckTypeGoodsType.setGoodsTypeId(id); // 货物类型id
                    pdTruckTypeGoodsType.setTruckTypeId(truckTypeId); // 车辆类型id
                    return pdTruckTypeGoodsType;
                }).collect(Collectors.toList());
                truckTypeGoodsTypeService.batchSave(list);
            }
            return pdGoodsType;
        }
        ```
    *   **`PdTruckTypeGoodsTypeServiceImpl` 中的 `delete` 方法**:
        ```java
        @Override
        public void delete(String truckTypeId, String goodsTypeId) {
            LambdaQueryWrapper<PdTruckTypeGoodsType> lambdaQueryWrapper = new LambdaQueryWrapper<>();
            boolean canExecute = false;
            if (StringUtils.isNotBlank(truckTypeId)) {
                lambdaQueryWrapper.eq(PdTruckTypeGoodsType::getTruckTypeId, truckTypeId);
                canExecute = true;
            }
            if (StringUtils.isNotBlank(goodsTypeId)) {
                lambdaQueryWrapper.eq(PdTruckTypeGoodsType::getGoodsTypeId, goodsTypeId);
                canExecute = true;
            }
            if (canExecute) {
                baseMapper.delete(lambdaQueryWrapper);
            }
        }
        ```
    *   **`BaseMapper` 接口中的 `delete` 方法**:
        ```java
        int delete(@Param("ew") Wrapper<T> var1);
        ```

*   **关键概念**:
    *   **MyBatis-Plus 的 `LambdaQueryWrapper`**: 用于构建动态 SQL 查询条件，避免了手动拼接 SQL 的复杂性。
    *   **`@Delete` 注解**: 用于标记删除操作。
    *   **`deleteById`**: 用于根据主键删除记录。
    *   **`deleteByMap`**: 用于根据多个字段的值删除记录。
    *   **`deleteBatchIds`**: 用于根据多个主键批量删除记录。
    *   **`updateById`**: 用于根据主键更新记录。
    *   **`updateByMap`**: 用于根据多个字段的值更新记录。
    *   **`selectById`**: 用于根据主键查询记录。
    *   **`selectByMap`**: 用于根据多个字段的值查询记录。
    *   **`selectList`**: 用于查询所有记录。
    *   **`selectOne`**: 用于查询单条记录。
    *   **`batchSave`**: 用于批量保存记录。
    *   **`saveBatch`**: 用于批量保存记录。
    *   **`StringUtils.isNotBlank`**: 用于判断字符串是否为空或仅包含空白字符。

---

### 4) 关键场景与演示描述

*   **场景一：控制器层逻辑演示 (00:00 - 00:05)**
    *   讲师首先展示了 `GoodsTypeController` 中的 `updateById` 方法。
    *   该方法接收一个 `id` 和一个 `GoodsTypeDto` 对象，用于更新货物类型的基本信息。
    *   在更新完基本信息后，讲师调用了 `truckTypeGoodsTypeService.delete` 方法，用于删除该货物类型与所有车辆类型的关联关系。
    *   讲师强调，这是在更新货物类型信息时，需要清理旧数据的必要步骤。

*   **场景二：服务层 `delete` 方法实现 (00:05 - 00:35)**
    *   讲师切换到 `PdTruckTypeGoodsTypeServiceImpl` 类，开始编写 `delete` 方法。
    *   讲师创建了一个 `LambdaQueryWrapper` 对象，用于构建查询条件。
    *   讲师使用 `StringUtils.isNotBlank` 方法判断 `truckTypeId` 是否为空，如果非空，则使用 `eq` 方法将 `truckTypeId` 设置为查询条件。
    *   讲师同样判断 `goodsTypeId` 是否为空，如果非空，则使用 `eq` 方法将 `goodsTypeId` 设置为查询条件。
    *   讲师使用 `canExecute` 标志变量来控制是否执行删除操作。
    *   讲师在 `canExecute` 为 `true` 时，调用 `baseMapper.delete` 方法执行删除操作。
    *   讲师在 `GoodsTypeController` 中，演示了如何调用 `truckTypeGoodsTypeService.delete` 方法来删除关联数据。

*   **场景三：代码调试与优化 (00:35 - 00:40)**
    *   讲师在 `GoodsTypeController` 中，演示了如何调用 `truckTypeGoodsTypeService.delete` 方法来删除关联数据。
    *   讲师强调，通过 `delete` 方法，可以实现对关联表数据的灵活删除操作。
    *   讲师在 `delete` 方法中，使用了 `LambdaQueryWrapper` 来构建动态 SQL 条件，避免了手动拼接 SQL 的复杂性。
    *   讲师在 `delete` 方法中，使用了 `canExecute` 标志变量来控制是否执行删除操作，避免了不必要的数据库操作。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
