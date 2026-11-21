# 11-货物类型管理（服务接口开发_新增货物类型_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢继续来看咱们这个新增货物类型

刚才呢我们是已经把这个

sale goods type咱们这个controller方法已经写好了对吧

这里面呢主要完成的是这么两个事啊

一个呢是保存货物类型

还有一个呢是保存我们这个关联信息

这个关联信息呢

我们是封成成list集合

相当于是一个批量保存对吧

是一个批量保存

在这呢我们再来写一下

这个是批量保存

我们这个货物类型和车辆类型的关联

关联信息啊

这个是一个批量保存

所以说呢我们需要封装这么一个对象

这个对象里边呢

一个是设置我们货物类型ID

还有一个是车辆啊

注意这是车辆类型

车辆类型ID

车辆类型ID

好

然后呢这样批量保存

并且呢我们现在呢是定义了

已经定义好了两个service接口对吧

两个service接口

然后呢我们这个service接口呢

其实呢可以啊

可以去继承什么呢

mybattiesplus给咱们提供的一个接口

叫做iservice

咱们前面学过mybattiesplus

应该也都知道

那么它给我们提供了这么一个iservice接口

然后呢这里边呢

我们是不是来指定一个范形对吧

而这个范形的话呢

往往就是我们所对应的这个实体类

实体类

那么继承它有什么好处呢

这就相当于我们常规的这些

中山改查方法是不是全都继承过来了

全都继承过来了

好

这是在这个接口里面定义的

好

同样呢我们刚才这个接口呢

也需要来让它来继承一下

来继承一下iservice接口

然后这个范形呢是不是对应的就是它了

好

就是我们这个关联实体

那接下来我们要做的呢

就是为这两个接口呢

是不是来创建什么呢

来创建它的实现类

咱们呢先来创建第一个

也就是我们这个

i

pd

goosetipeservice这个接口的实现类

这个实现类呢

我们可以在这个base下面呢

给它再来创建一个叫做impl对吧

这是实现啊

然后呢

在这下面来创建这个实现类

我们这个实现类呢

叫做pdgoosetipeserviceimpl

这个类名都比较长啊

这是我们货物类型管理这个服务接口

实现啊

然后呢

该家的注解呢

我们是不是需要来加一个啊

主要呢就是加这个service啊service注解

然后呢我们当前这个接口的话

这个实现类的话呢

是不是需要来继承一下

继承什么呢

哎

因为刚才咱们是不是这些接口呢都继承了

这个对吧

i service这个接口

然后呢我们对应的这边的话呢

也需要继承mybizplus给我们提供的一个副类啊

就叫做service imp啊

这个就是我们的这个接口啊

service imp啊

对吧service imp啊

然后呢我们可以看到它这个类上面呢有两个范型对吧

有两个范型

呃第一个是什么呢

第一个其实是我们的myper接口

也就是我们持久层对吧

咱们通常会定义myper接口来操作数据库啊

只不过我们现在还没有咱们呢先给它写上啊

一会儿再来创建它

咱们这个接口呢就叫做pdgoosetipemyper吧

好

然后呢还有就是我们的实体

第二个呢对应的就是我们的实体

实体呢

实体的话呢是不是就是pdgoosetip

pdgoosetip啊

这个实体

这是继承了啊

注意看这个呢是mybizplus给咱们提供的这个类

那么继承它有什么好处呢

那你就看呢它这个类里面是不是已经把我们常规的这些增伤改查方法其实都已经给我们提供好了

对吧

哎

那么我们就可以直接调它了啊

好

别忘了还要去实现啊

实现咱们刚才说的这个接口叫做ipdgoosetipservice接口

我直接把它复制过来

然后呢我们需要实现刚才看到的那个方法

咱们这里边这个方法savegoosetip

那么现在呢它之所以报错呢是因为我们现在这个myper接口是不是还没有

那咱们呢给它创建一下

把它创建出来

好

那接下来呢我们在这下边呢来创建一个包

这个包呢就叫myper

好

然后这个包下边呢我们再来一层包叫做base

咱们这个分的比较清楚啊

好

就是这个bass的这个系

对吧

然后呢对应的在这儿来创建这个接口

叫做goosetipemaper

pdgoosetipemaper

好

把这个接口是不是给定义好

然后呢我们现在呢需要让这个接口干什么呢

是不是需要去

继承我们这个mybethplus给咱们提供的一个叫做basemaper

对吧

basemaper

这么一个复类

然后呢在这儿呢是不是来指定什么呢

还是指定范形

这个范形呢还是我们那个实体类要操作的实体类

那是不是就是pdgoosetipemaper

好

然后呢我们还需要给这个接口呢来加一个注解

对吧

这个注解呢就是myper注解

myper注解

好

在这儿呢我们可以给它加一个注释啊

这是我们的货物类型对吧

货物类型

然后呢myper接口

好

其实呢我们针对这个接口呢就不用再给实现类了

哎

因为它底层呢其实是基于什么呢

基于代理技术

也就是说由我们mybethplus框架对吧

给我们产生代理对象

所以说呢我们直接操作这个接口

那么代理对象呢是由框架来产生的

所以说呢我们这个代码呢就相应的简化了很多

有了这个myper接口之后呢

你看这边它是不是就不再报错了

好

这个呢是我们保存这个货物类型

好

那么咱们在这儿是不是直接调用我们这个myper

哎

就可以进行完成一个保存操作呀

当然了在我们保存之前呢

其实我们需要干什么呢

需要来给它产生一个id

因为呢我们知道咱们这个controller这个地方

传进来的这个dto对象呢

其实根本就没有id对吧

所以说呢我们在这个save方法

咱们这个位置呢就需要在保存之前给它设置id

而这个id如何产生呢

咱们前面是不是在common这个地方

配置这么一个叫做customid

对吧

那么通过这个组件呢

就可以帮我们来生成一个id

来生成一个id

所以说呢我们在这个地方呢

可以把它注进来把它注进来private

咱们这个叫做customid generator对吧

叫做id generator

直接通过一个autoware的呢就注进来了

注进来之后呢就可以使用它来产生一个id了

所以说呢我们在保存它之前呢

需要来设置一下它的id

而它这个id的值呢可以通过id呢

可以通过id generator点什么呢

它这里面是不是给我们提供了这么一个叫做nextid对吧

叫做nextid

好

然后呢它这是不是要我们传进一个实体呀

那么我们把这个实体传进去就可以了

那么大家可以看到这个地方它报错对吧

哎它为什么报错呢

是因为我们这个地方这个setid啊

它接收的是什么呢

是stream类型

而我们刚才这个id generator呢

它产生的其实是一个int类型对吧

哎有时候它类型不匹配

哎那我们就把它放在这里吧

那这个怎么办呢

其实非常简单

我们直接给它转换一下

用一个小的技巧

哎你给它加上一个刷引号

让它做一个类型转换就可以了

哎这样的话你看

我就把这个类型呢给它转成了什么呢

转成了我们这个字符串啊

stream类型

好

这样的话我们这个id是不是就设置好

然后呢我们就可以调用什么呢

调用咱们这个就做base mapper

点什么呢insert对吧insert

然后呢把这个实体对象传进去啊

好

这样呢就保存了啊

还是非常简单的

呃最后呢把我们这个goose type呢

返回一下就可以了

只不过呢

这个地方返回的时候呢

它是不是就已经有了id了啊

就已经有了id了啊

因为我们这个id的话

咱们反过头来是不是在controller这个地方

还需要用它呀

还需要用它啊

好

那么到这儿的话呢

我们这个方法保存货物类型

这个方法呢就已经写完了

还是比较简单的

然后对应的呢

我们是不是还有一个

实现类呢需要来编写

就是咱们这个另外一个

呃

就是这个接口对吧

它的实现类

那么我们先把这个包呢给它来创建一下

你看刚才我们是不是创建的impl

所以在这个trunk下边呢

也需要来创建一个impl啊

这个规范都是一样的啊

接下来呢我们把它的实现类啊

叫做pd trunk type goose

type service impr

把这个实现类呢来编写出来

这是我们的车辆类型

车辆类型

然后还有什么货物类型

关系

关系

操作这个实现类

同样呢给它加一个service注解

然后呢我们这个地方是不是需要来

继承什么呢

哎

叫做service impr

同样这个地方是不是也是mapper

然后呢这个mapper的话是不是应该对应的

就是我们的这个

来看一下跟我们刚才这个呢

规范是保持一致就可以了

咱们这个叫做pd goose type mapper

然后呢这个应该叫做什么呢

就做pd trunk type goose type mapper

这是第一个是不是应该是个mapper

然后第二个呢是不是对应的就是我们的实体

对吧

实体的话呢咱们肯定就是

这个

这个类名比较长啊

我直接复制过来

然后呢继承它还需要干什么呢

实现对吧

实现实现我们刚才看到的这个接口

把这个接口直接复制过来

放在这

然后呢我们需要来实现这个批量保存对吧

批量保存这个方法

批量保存我们这个

关联信息具体是什么关联信息呢

就是这个

这两个关联信息

现在呢它报错就是因为我们现在是不是还没有这个什么呢

还没有这个mapper

所以接下来呢我们在这来创建一个mapper

把这个包呢先给它西化一下

创建一个trunk包

然后呢再接下来

把这个接口创建出来

继承一下什么呢

叫做base

base mapper

这个范型呢叫做pd trunk type goose type

然后呢这儿加一个注解对吧

mapper注解

好

这个接口呢也就定义好了

定义好之后回到这边来

你看它就不报错了

然后我们这个地方呢是不是就可以来完成什么呢

批量保存了

完成批量保存

这个批量保存呢其实跟我们刚才这个地方这个保存的是

跟我们这个地方这个保存是类似的

只不过呢这个呢是保存一个对吧

而我们现在这个呢是批量多次

那也就是说我是不是需要去便利我们这个list集合

便利这个list集合

所以我们在这个地方呢需要来处理一下它

点什么呢

在这边我们是不是可以使用这个for each对吧

for each来便利一下

for each

然后呢这里边呢我们还是使用这种

Lambda表达式这种形式啊

便利出来每一个呢是不是对应的就是这么一个叫做pd trunk type goose type对吧

好

然后呢给它做一个pd trunk type

再改成个小写的啊改成小写的啊

然后呢便利出来这个实体对象之后干什么呢

我们是不是希望把它给保存了

但是在保存之前呢还是需要来设置一下什么呢设置一下id对吧

所以说呢我们在这儿呢需要把这个

custom id generator

还是把它需要来注入一下

因为还是需要它

把它注进来

然后呢我们就可以啊在这个地方来设置什么

设置我们这个实体对象

它的id值

另外两个不用了

另外两个因为我们在传进来之前是不是已经给它封装好了的

所以就差一个id了

所以在这个地方呢来set id

这个id的值呢通过id generator.next的id

这个实体呢就还是这个pd trunk type goose type

同样的还是涉及到一个类型的问题

所以说呢我们在这儿呢还是给它加一个

加一个这个空字无创的这个pd trunk type goose type

这个空字无创对吧

就是强制让它转成这种string类型

好那这样的话这个对象呢

它的id属性是不是就已经封装好了

那么封装好之后呢

咱们是不是就可以来保存了啊

那这个地方呢我们就可以来保存了

这个保存的话呢我们可以使用这个什么呢

base mapper.insert

跟我们刚才看到的那个效果是一样的

其实这个地方呢我们也有一种简单的写法就是什么呢

哎因为我们现在是不是已经继承了这个

这个serviceimpl这个副类对吧

它这里面呢其实就已经给我们提供了批量保存的方法

你看是不是叫做savebench对吧

所以说呢我们这个地方呢

我们通过这个4h循环把这些id是不是给设置好

设置好之后呢直接把这个list的集合呢

通过调用副类的这个什么呢

批量保存方法就可以批量保存了

你看叫做什么呢savebench

savebench注意这是调用副类的方法

然后呢把咱们这个list的集合呢

集合传进去

好就可以了

那么这是比较简单的

直接调用副类的方法

批量保存

好那么到这儿的话呢

我们这个service以及我们的maiper接口呢

其实都已经定义好了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一节关于 Spring Boot + MyBatis-Plus 框架下，如何实现“货物类型”与“车辆类型”之间多对多关系的持久化操作的实战教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了从 Controller 层接收请求，到 Service 层处理业务逻辑，再到 Mapper 层执行数据库操作的完整流程。核心内容包括：
*   **业务逻辑拆分**：将“保存货物类型”和“保存货物类型与车辆类型关联关系”两个步骤分离。
*   **分层架构**：清晰展示了 Controller、Service、Mapper 三层的职责。
*   **MyBatis-Plus 用法**：演示了 `@Transactional`、`saveOrUpdateBatch`、`batchSave` 等方法的使用。
*   **自定义 ID 生成器**：引入 `CustomIdGenerator` 为实体对象生成主键 ID。
*   **Mapper 接口设计**：讲解了如何为关联表设计 Mapper 接口。
*   **代码调试与错误处理**：在编写代码过程中，讲师展示了如何识别并修正编译错误（如 `@Mapper` 注解不适用）。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：开场，展示项目结构和 `GoodTypeController.java` 中的 `saveGoodsType` 方法，该方法负责保存货物类型及其关联的车辆类型。
*   **00:05 - 00:10**：进入 `PdGoodsTypeService.java`，讲解 Service 层的职责。
*   **00:10 - 00:15**：查看 `PdGoodsTypeServiceImpl.java`，演示如何实现 `saveGoodsType` 方法。
*   **00:15 - 00:20**：讲解 `@Transactional` 注解的作用，以及 `saveOrUpdateBatch` 方法的使用。
*   **00:20 - 00:25**：展示 `saveOrUpdateBatch` 方法的源码，解释其内部逻辑。
*   **00:25 - 00:30**：讲解 `@Mapper` 注解的使用，以及如何为关联表创建 Mapper。
*   **00:30 - 00:35**：展示 `PdTruckTypeGoodsTypeMapper.java` 的接口定义。
*   **00:35 - 00:40**：讲解 `PdTruckTypeGoodsTypeServiceImpl.java` 中的 `batchSave` 方法。
*   **00:40 - 00:45**：演示如何为关联实体对象设置 ID。
*   **00:45 - 00:50**：讲解如何使用 `CustomIdGenerator` 为实体生成 ID。
*   **00:50 - 00:55**：展示 `batchSave` 方法的完整实现。
*   **00:55 - 01:00**：总结本节内容，强调分层设计和 MyBatis-Plus 的便捷性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1 (Controller 层)**：
    ```java
    public GoodsTypeDto saveGoodsType(GoodsTypeDto goodsTypeDto) {
        // 保存货物类型信息到货物类型表
        PdGoodsType pdGoodsType = new PdGoodsType();
        BeanUtils.copyProperties(goodsTypeDto, pdGoodsType);

        // 保存货物类型和车辆类型关联信息到关联表
        if (String truckTypeIds = goodsTypeDto.getTruckTypeIds(); truckTypeIds != null && truckTypeIds.size() > 0) {
            List<PdTruckTypeGoodsType> list = truckTypeIds.stream().map(truckTypeId -> {
                PdTruckTypeGoodsType pdfTruckTypeGoodsType = new PdTruckTypeGoodsType();
                pdfTruckTypeGoodsType.setGoodsTypeId(goodsTypeId); // 货物id
                pdfTruckTypeGoodsType.setTruckTypeId(truckTypeId); // 车辆id
                return pdfTruckTypeGoodsType;
            }).collect(Collectors.toList());
            return pdGoodsTypeGoodsTypeService.batchSave(list);
        }
        BeanUtils.copyProperties(pdGoodsType, goodsTypeDto);
        return goodsTypeDto;
    }
    ```

*   **关键代码片段 2 (Service 层 - 通用方法)**：
    ```java
    @Transactional
    default boolean saveOrUpdateBatch(Collection<T> entityList) {
        return this.saveOrUpdateBatch(entityList);
    }
    ```

*   **关键代码片段 3 (Service 层 - 实现类)**：
    ```java
    @Service
    public class PdGoodsTypeServiceImpl extends ServiceImpl<PdGoodsTypeMapper, PdGoodsType> implements PdGoodsTypeService {
        @Override
        public PdGoodsType saveGoodsType(PdGoodsType pdGoodsType) {
            pdGoodsType.setId(idGenerator.nextId(pdGoodsType));
            baseMapper.insert(pdGoodsType);
            return pdGoodsType;
        }
    }
    ```

*   **关键代码片段 4 (Mapper 层 - 关联表)**：
    ```java
    public interface PdTruckTypeGoodsTypeMapper extends BaseMapper<PdTruckTypeGoodsType> {
        // 通常会定义自定义的 SQL 方法
    }
    ```

*   **关键代码片段 5 (Service 层 - 关联表)**：
    ```java
    @Service
    public class PdTruckTypeGoodsTypeServiceImpl extends ServiceImpl<PdTruckTypeGoodsTypeMapper, PdTruckTypeGoodsType> implements PdTruckTypeGoodsTypeService {
        @Override
        public void batchSave(List<PdTruckTypeGoodsType> pdTruckTypeGoodsTypes) {
            pdTruckTypeGoodsTypes.forEach(pdTruckTypeGoodsType -> {
                pdTruckTypeGoodsType.setId(idGenerator.nextId(pdTruckTypeGoodsType));
                baseMapper.insert(pdTruckTypeGoodsType);
            });
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1：Controller 层业务逻辑拆分 (00:00-00:05)**
    讲师首先展示了 `GoodTypeController.java` 中的 `saveGoodsType` 方法。该方法接收一个 `GoodsTypeDto` 对象，首先调用 `goodsTypeService.saveGoodsType` 保存货物类型，然后通过 `truckTypeIds` 字段获取关联的车辆类型 ID 列表，并调用 `pdTruckTypeGoodsTypeService.batchSave` 方法保存关联关系。这体现了业务逻辑的分层和解耦。

*   **场景 2：Service 层实现与 MyBatis-Plus 方法调用 (00:10-00:20)**
    讲师切换到 `PdGoodsTypeServiceImpl.java`，演示了如何实现 `saveGoodsType` 方法。他使用了 `@Transactional` 注解确保操作的原子性，并调用了 `baseMapper.insert` 方法。同时，他展示了 `saveOrUpdateBatch` 方法的源码，解释了 MyBatis-Plus 如何通过 `@Transactional` 和 `saveOrUpdateBatch` 方法来处理批量操作。

*   **场景 3：关联表 Mapper 设计与 Service 实现 (00:30-00:45)**
    讲师展示了 `PdTruckTypeGoodsTypeMapper.java` 的接口定义，强调了 MyBatis-Plus 的 `BaseMapper` 接口。接着，他演示了 `PdTruckTypeGoodsTypeServiceImpl.java` 中的 `batchSave` 方法。他使用 `Stream` 流将 `truckTypeIds` 转换为 `PdTruckTypeGoodsType` 对象列表，并调用 `baseMapper.insert` 方法进行批量插入。

*   **场景 4：自定义 ID 生成器集成 (00:45-00:55)**
    讲师在 `PdGoodsTypeServiceImpl.java` 中引入了 `CustomIdGenerator`，并将其注入到 Service 中。在 `saveGoodsType` 方法中，他调用 `idGenerator.nextId(pdGoodsType)` 为 `pdGoodsType` 设置主键 ID，然后调用 `baseMapper.insert` 方法插入数据。这展示了如何在 MyBatis-Plus 中集成自定义的 ID 生成策略。

*   **场景 5：代码调试与错误处理 (00:55-01:00)**
    讲师在编写 `batchSave` 方法时，遇到了编译错误。他通过 IDEA 的提示，发现 `@Mapper` 注解不适用于 `CustomIdGenerator` 类。他通过修改代码，将 `CustomIdGenerator` 的类型改为 `@Service`，并将其注入到 Service 中，从而解决了编译错误。这体现了在实际开发中如何处理和解决代码错误。
