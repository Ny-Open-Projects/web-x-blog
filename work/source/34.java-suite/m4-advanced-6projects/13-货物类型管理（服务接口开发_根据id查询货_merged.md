# 13-货物类型管理（服务接口开发_根据id查询货 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面呢,咱们是已经完成了新增货物类型这个服务接口的开发

那么接下来呢,我们来看下一个

下一个呢,是根据ID来查询货物类型

那么首先呢,我们还是先从Controller说起

先在这个里边呢,来创建一个叫做FindByID的方法

这里边打开的比较乱了,我们都关上

然后呢,先找到咱们的Controller

Controller在这儿,有一个叫做GooseTypeController

然后呢,我们在这儿,下面来开发下一个

也就是我们这个根据ID来查询货物类型

先把这个方法呢,咱们来定义一下

Public,然后呢,这个返回值,注意,返回值是什么呢

是使用我们DTO类型,其实就是这个类型

叫做GooseTypeDTO,最终返回这么一个对象

然后这个方法名呢,咱们就叫FindByID吧

FindByID

好

好

,然后呢,传进来一个什么呢

传进来一个String类型的ID,作为参数,对吧

那么这个呢,我们需要来解释一下

就是说我们这个接口,跟前端呢,已经约定好了

那么它在请求的时候呢,会通过这种路径变量的方式

把ID传给我们

这是不是意味着什么呢

我们在这个地方呢,要接收的话呢

需要加这么一个,叫做什么呢

叫做PassVariable,对吧

这个呢,我们应该都比较熟悉了

然后呢,它传的这个参数名呢

Name

当然是这个,这个参数名呢

当然这个Name呢,就不能写到这里边了,对吧

这是它的一个属性

Name等于什么呢

等于ID

同时呢,我们在这个地方呢,还需要来加一个什么呢

加一个GetMapping

因为它是一个Get的方式请求啊

GetMapping

然后呢,在这个地方是不是来描述我们这个路径,对吧

是不是需要使用这种语法啊

一个花光号,对吧

然后里边是ID

这样的话呢,就从路径上取到这个ID,对吧

并且附给我们定义的这个参数

好,这样的话,这个参数是不是就已经获取成功了

先加一个注释啊

这个呢,是根据我们的这个ID,对吧

来查询货物类型

好

咱们先Return一个Now啊

不让它报错

好,那接下来呢,这里边

要根据ID查的话呢,其实就非常简单了,对吧

咱们在这是不是已经注入了一个Service了

就是我们这个GooseType Service

好

然后呢,我们直接调用它的一个什么呢

叫做GetByID的方法

然后呢,把我们的ID是不是传进去

这样呢,就可以直接返回一个什么呢

PD GooseType,对吧

PD GooseType

好,就是我们的货物类型,对吧

好

那么我们需要来看一下

咱们在定义这个Service接口的时候呢

好像并没有那个什么GetByID这个方法,对吧

那么我这个地方为什么能调这个方法呢

其实啊,你看我们前面是不是已经继承了这个什么呢

iService,对吧

已经继承了它

而在它这个接口里边

其实就已经把我们常用的这些方法

诶,再来试试看

让它改查的方法

其中也包括什么呢

GetByID,对吧

根据ID来查询

那么也有这个方法

所以我们在这个地方呢

是不是就可以直接来调用了

好

这样的话呢

我们根据ID呢

其实就已经查询到什么呢

就已经查询到我们这个货物类型了

这是根据ID来查

好

然后查完之后呢

还没完

因为什么呢

咱们来看一下

我们最终是不是要返回的是这个DTO对象

DTO对象

而在这个对象里边

除了我们这个货物类型

这些基本的

属性

像ID,NAME等等

这些属性之外呢

它其实还有一个关联的

对吧

也就是我们当前这个货物类型

它关联了哪些车辆

这是个车辆类型的ID

对吧

车辆类型的ID

那么我们需要来这个

给它设置一下

而我们当前这个查询

有吗

根本就没有

也就是说

它只是查询了我们这个货物类型表

而那个关系表

它根本就没有查询

所以我们在这个地方呢

只是查到这一步

很显然还不够

诶

所以说呢

我们接下来需要干什么呢

需要来查询啊

上面这只是查询基本信息

对吧

然后呢

我们还需要查询

还需要查询什么呢

当前这个货物类型

关联的什么呀

关联的这个车辆类型的ID

还需要查询这个

当然他们是中间

是一个多对多的关系

所以有可能有多个

对吧

有可能有多个

所以我们在这呢

还需要再来查一下

查出来之后呢

把这个对象是不是

重新封装一下

最终封装成这么一个对象

啊

封装成这么一个对象

然后给我们这个前端来返回

好

所以这块的话呢

我们就需要来查询

关联的这个车辆类型ID

那这个怎么查呢

咱们呢

可以在我们这个

另外一个service啊

刚才我们用到了

就是这个对吧

ipd trunk type

goose type service

在这里边呢

我们可以来

再来声明一个方法

诶

这叫什么方法呢

这个方法名其实叫什么

无所谓啊

关键是什么呢

我们这个查询条件啊

可以传什么呢

可以传我们这个车辆类型ID

也可以传这个货物类型ID

那么根据这两个条件

我们来查询

在这呢

我们在这来声明一下

声明完之后呢

我们在controller当中啊

就可以来这个调用了

public

先把这个关键字写上

然后呢

返回值

它是不是有可能有多个呀

因为是多对多的关系

所以说呢

我们在这儿

来一个例子的集合

然后集合里边呢

放的是什么呢

其实就是我们这个关联对象

对吧

大家还记得吧

PD什么

trunk type

goose type

对吧

这个

好

然后呢

这个方法名呢

就叫做什么呢

叫做find all吧

find

诶

find all

好

find all

然后呢

这个方法呢

它的参数是什么呢

它的参数啊

一个是什么呢

一个是我们这个车辆类型ID

还有一个呢

就是货物类型ID

所以这个方法呢

这两个参数呢

我们都可以传进来

一个是车辆类型

车辆类型是不是叫做

全科type

ID

这个是我们的车辆类型ID

然后还有一个呢

是goose type ID

那么我们接受这么两个参数

这个方法的注释呢

我们来写一下

这个是根据什么呢

根据我们的这个车辆类型ID

或者什么呢

这个货物类型来查询

好

查询什么呢

查询关联信息吧

啊

关联信息

好

这个方法呢

就定义好了

具体实现

我们一会再去实现

咱们先把这个service里边呢

添加这么一个方法

有了这个方法之后呢

回到咱们刚才编写的control这儿

对吧

然后呢

在这个地方呢

我是不是就可以去调用它了

我就这个地方就可以调它了

那么呢 这个地方呢 我就这个地方就可以调它了

那么怎么调呢

非常简单了

你看现在我们这个货物类型的ID其实是知道的

其实就是当前这个ID

对不对

就是这个ID

所以我们这块呢

就可以啊

直接这样来查

通过这个什么呢

通过我们刚才定义的这个

这个service

传个type

goose type service

然后点什么呢

Find out

然后呢

传进来什么呢

第一个车辆类型ID用传吧

其实不用传

对吧

然后呢

第二个呢

第二个其实就是我们这个传过来的这个ID

对吧

第一个不用传

因为车辆类型ID

没有

我们现在呢

其实是希望使用这个货物类型ID来查

对吧

所以说呢

我们把这个ID是不是传进去

把这个ID传进去

这样的话呢

我们是不是就得到了这么一个LIS的集合

一个LIS的集合

这个集合里边装的是什么呢

就是PD

就是我们这个关联对象对吧

关联对象

而在这个关联对象里面呢

我们现在是想要什么东西

我们其实是想要的是这个

是这个传个typeID对吧

传个typeID

而现在呢

它是不是一个LIS的集合呀

它LIS集合

然后呢

里边装了多个

现在呢

我们是希望把这里边的这个什么呢

这个车辆类型ID是不是一个一个给它取出来

然后呢

再给它封装成什么了

再给它封装成我们的这个集合对吧

然后最终复制给谁呢

复制给我们这个DTO里边的

DTO里面的

这个属性对吧

传个typeID

所以我们在这个地方呢

简单对这个LIST是不是做一个流计算就可以了

对吧

stream流

所以说呢

我们在这个地方呢

就可以直接使用这个LIST的点什么呢

stream

当然在使用之前呢

我们最好还是先来判断一下

先来判断一下

意味着什么呢

这个LIST不等于空对吧

先判断一下

然后呢

同时这个LIST的点size

然后呢

大于0

这个时候呢

再做进一步处理

是比较保险的

如果查出来是个空的话呢

那我们就没有必要执行下面的代码了对吧

所以说呢

这块的话我们就可以啊

直接使用这个什么呢

LIST的点什么stream对吧

stream

然后呢点map

这里边具体怎么处理呢

是不是写一个这个Lambda表达式对吧

通过Lambda表达式这种语法

然后呢来处理

那么我们需要知道

我编辑出来每一个呢

是不是就是这么一个对象

就是这么一个对象对吧

当然给它改成一个小写的比较合适

好

然后呢

编辑出来都是这么一个对象

然后呢

我们需要对它进行

何种处理呢

其实非常简单

我们是不是只需要把

它这个对象里边的ID给它取出来就可以了

对吧

把这里边的这个ID给它取出来

所以说呢

这块的话呢

我们直接

获取它的ID就可以了

通过这个type点什么呢

get

get trunk type

ID对吧

然后呢

get它之后呢

点collect它

然后呢

把它收集好对吧

这个是不是应该就是

还是我们这个collectors

点什么呢

to list对吧

to list

这样的话

我们这个trundypeID

是不是就已经搞定了

这块呢

一会再整理

我们先把这个

记好

这个应该就是我们

这个叫做trundypeID

就是这么一个list结果了

好

就是这么一个list结合

对吧

这么一个list的结合

好

这个地方呢

咱们是不是应该没有这个括号对吧

这样多写了一个括号

然后呢

这个地方呢

应该是我们这个stream类型对吧

我们需要把这个类型给它写上

好

这样的话呢

我们这个list的结合呢

是不是就已经处理好了

通过我们这种stream流这种方式啊

就已经把它处理好了

处理好之后呢

我们是不是需要

把我们这个返回结果来封装一下

对吧

反过结果来封装一下

所以我们在这个地方呢

需要来创建这么一个

在这儿啊

好

来创建一个DTO对象的吧

在这个地方吧

好

好

来创建一个DTO对象

好

就是这个DTO对吧

然后呢

我们直接啊

通过这个

goose type DTO等于new一个goose type DTO

把这个DTO对象是不是new好

那么new好之后呢

还没有完

哎

我们需要把这里边的属性啊

对应的

从我们这个查出来的pdgoose type里边

把它拷贝进来

对吧

把它拷贝进来

所以我们在这个地方呢

需要使用binutils对吧

就是使用我们这个binutils

然后呢

来copy一个什么呢

copy properties吧

好

然后圆的话呢

很显然是不是就是我们那个pdgoose type

目标呢

是不是就是这个goose type DTO

好

这个DTO对象

好

然后呢

我们这些普通的属性其实就已经拷贝过去了

对吧

这些普通的属性啊

就已经拷贝过去了

这个还没有

哎

为什么呢

就是因为我们现在是不是查出来的

这里边那个idc呢

还没有封成好

所以接下来呢

我们再单独给它设置一下就可以了

对吧

再单独给它设置一下就可以

咱们呢

把这个代码顺序呢

简单给它调整一下

再调整一下

好

然后呢

如果这边不等于空的话呢

我们是不是再来设置一下什么呢

咱们这个goose type呢

这个goose type DTO.set什么呢

是不是应该叫做settranctype ids

对吧

这个

然后呢

把它设置上我们查出来的这个id

好

最后呢

把咱们这个DTO对象啊

goose type DTO对象

返回一下

是不是就可以了

好

整个这个代码写起来呢

还是比较简单的

主要一个查这么两步

对吧

一个呢

是根据id

把我们这个货物类型普通信息查上来

然后呢

第二部分呢

就是查询我们这个关联的对吧

查询关联的车辆类型的id

然后呢

把它封装进去

最终呢

把它返回一下就可以了

当然了

我们这块呢

还没有完全写完

因为什么呢

大家还记得吧

我们刚才呢

在这个service里边

扩展了findall方法

但是在我们的实现类里面呢

其实还没有去实现它

你看

咱们这边是不是报错了

因为我们现在呢

需要去实现这个findall方法

好

那么一会儿呢

我们再具体去写代码

咱们呢

现在呢

直接啊

先把这个方法呢

给它扩展出来

一会儿呢

我们再去具体实现它

这个呢

就是根据我们的车辆类型

还有货物类型id

对吧

然后呢

查询这个关联信息

那么返回值呢

是封装成粒子的集合来返回

好

那么关于咱们这个

根据id查询呢

我们先写到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个 Java Spring Boot 项目的实战教学，主要演示了如何在控制器（Controller）中通过服务层（Service）查询“货物类型”及其关联的“车辆类型”信息。核心内容包括：
*   **项目结构**：展示了项目目录结构，包含 `BaseApplication` 启动类、`GoodTypeController` 控制器、`IPdTruckTypeGoodsTypeService` 服务接口及其实现类。
*   **数据模型**：重点讲解了 `GoodsTypeDto` 数据传输对象（DTO）和 `PdTruckTypeGoodsType` 实体类，以及它们之间的关系。
*   **业务逻辑**：演示了如何在 `findById` 方法中，先通过 `goodsTypeService` 获取货物类型，再通过 `truckTypeGoodsTypeService` 查询关联的车辆类型列表，并将结果封装到 DTO 中返回。
*   **技术点**：使用了 Spring MVC 的 `@GetMapping` 注解、`@PathVariable` 注解、`BeanUtils.copyProperties` 方法进行属性拷贝、以及 Java 8 的 Stream API 进行集合操作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:04**: 展示项目启动类 `BaseApplication`，确认项目已成功启动。
*   **00:04 - 00:10**: 跳转到控制器 `GoodTypeController`，定位到 `findById` 方法，准备演示查询逻辑。
*   **00:10 - 00:15**: 在 `findById` 方法中，先通过 `goodsTypeService.getById(id)` 获取 `PdGoodsType` 实体。
*   **00:15 - 00:20**: 通过 `truckTypeGoodsTypeService.findAll(truckTypeId: null, id)` 查询关联的车辆类型列表。
*   **00:20 - 00:25**: 使用 `Stream` API 对查询结果进行处理，提取 `truckTypeId` 并封装到 `GoodsTypeDto` 中。
*   **00:25 - 00:30**: 完成 `GoodsTypeDto` 的属性设置，并返回结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **控制器 `GoodTypeController` 中的 `findById` 方法**：
    ```java
    @GetMapping("/{id}")
    public GoodsTypeDto findById(@PathVariable(name = "id") String id) {
        PdGoodsType pdGoodsType = goodsTypeService.getById(id);
        // 还需要查询当前货物类型关联的车辆类型的id
        List<PdTruckTypeGoodsType> list = truckTypeGoodsTypeService.findAll(truckTypeId: null, id);
        if (list != null && list.size() > 0) {
            List<String> truckTypeId = list.stream().map(PdTruckTypeGoodsType::getTruckTypeId).collect(Collectors.toList());
            pdGoodsType.setTruckTypeIds(truckTypeId);
        }
        return pdGoodsType;
    }
    ```

*   **服务接口 `IPdTruckTypeGoodsTypeService`**：
    ```java
    public interface IPdTruckTypeGoodsTypeService extends IService<PdTruckTypeGoodsType> {
        // 批量保存
        public void batchSave(List<PdTruckTypeGoodsType> pdTruckTypeGoodsTypes);
        // 根据id查询
        public PdTruckTypeGoodsType getById(String id);
        // 查询关联的车辆类型
        public List<PdTruckTypeGoodsType> findAll(String truckTypeId, String goodsTypeId);
    }
    ```

*   **数据传输对象 `GoodsTypeDto`**：
    ```java
    public class GoodsTypeDto implements Serializable {
        private static final long serialVersionUID = -6890776123674482761L;
        @ApiModelProperty("主键")
        private String id;
        @ApiModelProperty("物品类型名称")
        private String name;
        @ApiModelProperty("默认重量，单位：千克")
        private Double weight;
        // ... 其他属性
        private List<String> truckTypeIds; // 关联的车辆类型ID列表
    }
    ```

#### **关键公式 / 图表**

*   **Stream API 的常用方法**：
    *   `stream()`：创建流。
    *   `map(Function<T, R> mapper)`：将流中的每个元素转换为另一个对象。
    *   `collect(Collectors.toList())`：将流中的元素收集到一个 `List` 中。
    *   `filter(Predicate<T> predicate)`：过滤流中的元素。
    *   `forEach(Consumer<? super T> action)`：对流中的每个元素执行操作。

---

### 4) 关键场景与演示描述

*   **场景一：项目启动与导航**
    *   **描述**：视频开始时，画面显示了 IntelliJ IDEA 的项目视图，用户首先打开了 `BaseApplication` 启动类，确认项目已成功启动。随后，用户导航到 `GoodTypeController` 文件，定位到 `findById` 方法，准备演示查询逻辑。

*   **场景二：查询货物类型及其关联车辆类型**
    *   **描述**：在 `findById` 方法中，用户首先通过 `goodsTypeService.getById(id)` 获取 `PdGoodsType` 实体。接着，通过 `truckTypeGoodsTypeService.findAll(truckTypeId: null, id)` 查询与该货物类型关联的所有车辆类型记录。用户使用 `Stream` API 对查询结果进行处理，通过 `map` 方法提取每个 `PdTruckTypeGoodsType` 对象的 `truckTypeId`，并使用 `collect(Collectors.toList())` 将其收集到一个 `List<String>` 中。最后，将该列表设置到 `GoodsTypeDto` 的 `truckTypeIds` 属性中。

*   **场景三：代码调试与优化**
    *   **描述**：在演示过程中，用户对代码进行了调试和优化。例如，在 `findById` 方法中，用户使用了 `if (list != null && list.size() > 0)` 判断查询结果是否为空，以避免空指针异常。同时，用户展示了如何使用 `Stream` API 对集合进行高效的处理，提高了代码的可读性和性能。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解视频内容。
