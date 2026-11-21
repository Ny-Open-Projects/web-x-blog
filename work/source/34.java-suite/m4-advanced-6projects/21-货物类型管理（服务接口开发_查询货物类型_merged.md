# 21-货物类型管理（服务接口开发_查询货物类型 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才咱们这个分页查询货物类型已经写完了

然后下一个我们来看查询货物类型列表

这个是什么意思呢

咱们直接来看这个方法定义就明白了

查询货物类型列表其实就是什么呢

我可以传过来多个货物类型的ID

你看它是封装成一个例子的集合

那么我们直接根据这个多个集合

根据这多个ID来进行一个查询

其实相当于是一个in条件查询

本质上就是一个什么

select from我们这个表

为了什么呢

ID in

我们这个ID只要在这个集合里边都需要查出来

所以说这个就是查询货物类型列表

它是根据多个ID封装成的例子集合来进行一个查询

接下来我们把这个方法定义出来

先把服务停掉

然后在这儿

在我们这个controller里边继续来写

在这个地方

然后返回值

返回值是不是一个例子的集合

里边它也是封装成一个例子集合

里边封装的DTO

那我整个把这块就拷过来了

返回值是一个例子的

里边封装的还是DTO对象

方法名其实无所谓

然后传进来参数就是IDs

这就要求我们前端再给我们传的时候

或者是什么

或者是我们这个web这段

PD web这段传的时候

给我们传过来这么一个例子的集合就可以了

然后我们先把这儿

还是先写一个return

然后在这加一个get mapping

get mapping

这其实我们写一个空串就可以了

这样的话

它只要发一个get的方式请求

然后请求地址是这个地址

对吧

并且参数能对应上

它就可以正常请求到我们这个方法了

然后我们再加一个API operation

这么一个注解

查询货物类型列表

把这个先写一下

类型列表

好

这个要查询的话

很显然我们是不是要调service来查

那么我们就调用这个什么

ghost type service点什么

它这里边

咱们需要给它提供这么一个方法

这个方法还叫find all

但是跟这个是同名

但是是一个重载的方法

然后我们需要把谁传进去

把这个IDs是不是传进去

把这个IDs传进去

根据这个参数来进行一个查询

那么返回进去

结果很显然应该也是一个例子集合

对吧

例子集合

只不过这个集合里边封装的

还不是这个DTO对象

封装的应该是什么

是我们这个PD

ghost type

是不是我们这个实体

然后一会儿我们再去转换

所以大家可以看到

我们其实写几个方法之后

你就能发现我们这个套路

我们这个套路其实都是固定的

查询的话

基本上你调service

查出来不管怎么封装

它是不是都要封装成这个实体

然后呢

我们再把这个实体呢

给它转成DTO

用于这个网络传输

对吧

基本上全都是这种套路

好

那接下来呢

我们来看啊

这个方法呢

现在报错

就是因为我们现在还没有这个方法

我们可以在这边

找到service

咱们在这呢

来给它创建一下

create

加一个注释吧

查询货物类型

货物类型列表

对吧

好

传进来的就是这个参数

然后一会儿

我们再具体

还是一会儿再去实验它

先到这边来

它是不是就不报错了

然后呢

有了这个list的集合呢

咱们是不是就可以进行处理了

就可以进行处理了

怎么处理呢

同样还是先来判断

对吧

都是一样的list不等于空

同时list.size

大于零

然后呢

我们就可以啊

来进行处理了

因为我们现在查到的是list里面装的是这种对象

我们最终了要返回的是DTO这种对象

所以说呢

我们需要基于list的组合

点什么呢

stream

然后呢

点map

跟前面的套路其实都是一样的

对吧

然后呢

咱们在这儿是不是需要给它转

转一下

那么怎么转呢

在这个地方呢

我们先把这个pd-goosetab

goosetab取出来

就这样

pd-goosetab取出来

然后呢

取出来之后啊

这里边做什么事呢

是不是还是需要根据我们这个货物类型

ID

把它对应的那个关联信息给它查出来

对吧

所以说呢

我们在这儿呢

还是调用我们这个关系这个service

在哪呢

这儿

好

来查一下啊

find out

对吧

然后呢

这儿还是no

然后呢

货物类型ID呢

从这个pd-goosetab.getID

这样是不是就可以拿到了

这样的话

我们这个list的集合呢

就已经查过来了

对吧

查到这个list的集合之后呢

同样还是需要对它是不是进行一个处理

对它进行一个处理

点什么呢

stream

点什么呢

map

对吧

然后呢

把我们这个tranctype

tranctype

goosetab

好

然后这里边我们要谁呢

是不是只要它的这个ID就可以了

对吧

也就是说我们这个

type.gettranctypeID

只要这个ID就可以了

好

然后呢

处理完之后呢

map完之后

点collect

把它的这个

ID呢都收集起来

转成一个list的集合

然后呢collects.toList的

这个代码呢

我们其实都已经写过很多遍了

这样呢

我们就得到了这个IDs

tranctypeIDs

好

OK

这个ID弄好之后呢

我们是不是就可以来进行这个对象的封装了

封装成这个DQ

这跟前面代码都是一样的

等于new一个DQ

这个goose type DTO

对吧

好

又是来之后呢

我们就可以直接调用它

点set什么呢

tranctypeIDs

然后呢

这来一个tranctypeIDs

好

同样呢

普通的属性呢

咱们是不是都已经查过了

在这个find all方法这

跟我们返回的就已经查过了

所以说呢

我们在这呢

把这些属性的都拷贝过来

PD goose type

然后呢

目标呢

就是这个DQ

goose type DQ

好

最终呢

我们是不是把这个

DQ对象来返回一下

就可以了

goose type DQ

好

把它来返回一下

别忘了

这个整个到

这块的话

整个我选中这块

这都是我们

这个Lambda表达式

它的

它的这个代码块

对吧

然后呢

我们在这呢

直接来一个什么呢

collect的

collectors.to list

好

到这儿的话呢

我们

这个

list的集合

是不是就已经封装好了

这个list集合

就已经封装好了

好

咱们就叫

goose type DTO

好

goose type DTO list

最终呢

我们是不是要返回的

就是这么一个集合

所以

把它返回一下就可以了

这是

当这个查出来之后呢

我们再查关联信息

并且进行这个对象的封装

对吧

然后呢

最后把它返回

如果呢

判断它等于空的话

直接return到

就可以了

好

那么到这儿的话呢

我们这个controller

这个方法呢

就已经写完了

一会儿呢

我们再去写这个什么

service里边具体

是如何实现final方法的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的 Java 项目中，如何实现一个分页查询和条件查询的 RESTful API。核心内容是 `GoodTypeController` 中的 `findPage` 和 `findAll` 方法，以及它们如何调用 `GoodTypeService` 进行业务逻辑处理。视频重点演示了如何通过 `@RequestParam` 接收前端传入的分页参数（`page`, `pageSize`）和业务条件（`name`, `truckTypeId`, `truckTypeName`），如何使用 `Pageable` 进行分页，如何通过 `Stream` API 进行数据转换和聚合，以及如何使用 `BeanUtils.copyProperties` 进行对象属性复制。整个过程体现了典型的分层架构（Controller -> Service -> Mapper）和现代 Java 的函数式编程风格。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下时间点是根据画面内容和逻辑顺序推断的：

*   **00:00:00 - 00:00:15**: 展示项目结构和 `GoodTypeController` 中的 `findPage` 方法。重点是 `@RequestParam` 注解和 `Pageable` 的使用。
*   **00:00:15 - 00:00:30**: 展示 `findPage` 方法的实现细节，包括创建 `Page` 对象、添加排序条件、调用 `mapper.findByPage`。
*   **00:00:30 - 00:00:45**: 切换到 `findAll` 方法，展示其接收 `ids` 参数并调用 `goodTypeService.findAll`。
*   **00:00:45 - 00:01:00**: 展示 `findAll` 方法的业务逻辑：如果 `ids` 不为空，则调用 `truckTypeGoodsTypeService.findAll` 获取关联数据。
*   **00:01:00 - 00:01:15**: 展示如何使用 `Stream` API 对 `truckTypeGoodsTypes` 进行 `map` 操作，提取 `truckTypeId`。
*   **00:01:15 - 00:01:30**: 展示如何使用 `BeanUtils.copyProperties` 将 `truckTypeIds` 复制到 `GoodsTypeDto` 对象中。
*   **00:01:30 - 00:01:45**: 展示如何使用 `Collectors.toList()` 将 `Stream` 转换为 `List`。
*   **00:01:45 - 00:02:00**: 展示最终的 `return goodTypeDtoList;` 语句，完成整个业务逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (分页查询)**：
    ```java
    @Override
    public IPage<PdGoodsType> findByPage(Integer page, Integer pageSize, String name, String truckTypeId, String truckTypeName) {
        Page<PdGoodsType> pdPage = new Page<>(page, pageSize);
        pdPage.addOrder(OrderItem.asc("id"));
        pdPage.setRecords(mapper.findByPage(pdPage, name, truckTypeId, truckTypeName));
        return pdPage;
    }
    ```
    *   **关键点**：使用 `Page` 对象进行分页，`addOrder` 设置排序，`setRecords` 设置分页数据。

*   **代码片段 2 (条件查询)**：
    ```java
    @GetMapping(value = "查询货物类型列表")
    @ApiOperation(value = "查询货物类型列表")
    public List<GoodsTypeDto> findAll(@RequestParam(name = "ids", required = false) List<String> ids) {
        List<PdGoodsType> list = goodTypeService.findAll(ids);
        if (list != null && list.size() > 0) {
            List<PdTruckTypeGoodsType> truckTypeGoodsTypes = truckTypeGoodsTypeService.findAll(...);
            List<String> truckTypeIds = truckTypeGoodsTypes.stream().map(...).collect(Collectors.toList());
            GoodsTypeDto goodsTypeDto = new GoodsTypeDto();
            BeanUtils.copyProperties(goodsTypeDto, truckTypeIds);
            return goodsTypeDtoList;
        }
        return null;
    }
    ```
    *   **关键点**：使用 `@GetMapping` 和 `@ApiOperation` 注解，`@RequestParam` 接收 `ids` 参数，`Stream` API 进行数据转换，`BeanUtils.copyProperties` 进行属性复制。

*   **代码片段 3 (Stream API)**：
    ```java
    List<String> truckTypeIds = truckTypeGoodsTypes.stream()
        .map(truckTypeGoodsType -> truckTypeGoodsType.getTruckTypeId())
        .collect(Collectors.toList());
    ```
    *   **关键点**：使用 `stream()` 创建流，`map()` 对每个元素进行转换，`collect(Collectors.toList())` 收集结果。

*   **代码片段 4 (BeanUtils.copyProperties)**：
    ```java
    BeanUtils.copyProperties(goodsTypeDto, truckTypeIds);
    ```
    *   **关键点**：将 `truckTypeIds` 列表中的值复制到 `goodsTypeDto` 对象的相应属性中。

*   **代码片段 5 (Collectors.toList())**：
    ```java
    .collect(Collectors.toList());
    ```
    *   **关键点**：将 `Stream` 转换为 `List`。

---

### 4) 关键场景与演示描述

*   **场景 1: 分页查询实现**
    *   **描述**：讲师首先展示了 `GoodTypeController` 中的 `findPage` 方法。他解释了如何通过 `@RequestParam` 接收前端传入的分页参数（`page`, `pageSize`）和业务条件（`name`, `truckTypeId`, `truckTypeName`）。然后，他演示了如何创建一个 `Page` 对象，并使用 `addOrder` 设置排序条件。最后，他调用了 `mapper.findByPage` 方法，并将结果设置到 `Page` 对象中，返回给前端。

*   **场景 2: 条件查询实现**
    *   **描述**：讲师切换到 `findAll` 方法，解释了如何接收 `ids` 参数。他演示了如何调用 `goodTypeService.findAll` 获取数据。然后，他展示了如何使用 `Stream` API 对数据进行处理，包括 `map` 和 `collect` 操作。他特别强调了 `BeanUtils.copyProperties` 的使用，用于将查询结果中的 `truckTypeId` 列表复制到 `GoodsTypeDto` 对象中。

*   **场景 3: Stream API 演示**
    *   **描述**：讲师在 `findAll` 方法中，对 `truckTypeGoodsTypes` 列表进行了 `Stream` 操作。他演示了如何使用 `map` 方法将每个 `PdTruckTypeGoodsType` 对象转换为 `String` 类型的 `truckTypeId`，并使用 `collect(Collectors.toList())` 将结果收集到一个 `List` 中。

*   **场景 4: BeanUtils.copyProperties 演示**
    *   **描述**：讲师在 `findAll` 方法中，创建了一个 `GoodsTypeDto` 对象，并使用 `BeanUtils.copyProperties` 方法将 `truckTypeIds` 列表中的值复制到 `goodsTypeDto` 对象的相应属性中。他解释了这种方法可以简化对象属性的赋值过程。

*   **场景 5: 代码调试与优化**
    *   **描述**：在演示过程中，讲师展示了如何使用 IntelliJ IDEA 的智能提示功能来选择正确的 `map` 方法。他通过 `Ctrl+Shift+Space` 快捷键，查看了 `Stream` API 的可用方法，并选择了 `map` 方法。他还展示了如何使用 `BeanUtils.copyProperties` 方法，并通过 `Ctrl+Shift+Space` 快捷键查看了 `copyProperties` 方法的参数。
