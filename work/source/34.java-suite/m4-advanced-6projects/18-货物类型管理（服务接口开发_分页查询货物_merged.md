# 18-货物类型管理（服务接口开发_分页查询货物 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们服务接口开发

下一个我们要开发的是分页查询货物类型

那么这个分页方法是这样的

首先我们来看这个方法要求返回值是一个叫做page response每个对象

然后这里边指定一个范形

这个范形我们应该比较了解了,就是goose type DTO

而这个page response这是统一的

只要是分页查询我们统一都返回这个对象

而这个对象呢,咱们可以来看一下

叫做page response,对吧

这是在我们这个pd comment

咱们这里边定义的

在我们这个pd comment这个模块里面定义了这么一个通用的一个分页结果

包装的这么一个类

然后呢这里边封装的是什么呢

都是跟我们分页相关的一些属性

比如说总的条目数,对吧

还有这个页尺寸

其实就是每页显示多少条数据,对吧

还有总的页数,还有当前的页码

然后接下来呢就是items

这个呢就是我们当前这一页要展示的数据列表

所以说呢我们以后啊

所有涉及到的分页

那么返回值呢统一都会返回我们这个page response对象

然后呢这儿指定范形T,对吧

而这个范形呢对应的

最终需要封装到这个list的集合里面去

就是我们集合的元素类型

好

那接下来呢我们就来定义这个方法

咱们先来看一下我们的讲义啊

那么我们要根据这个分页进行查询的话呢

分页条件啊来看一下

首先是page,对吧

这个是页码

还有page size

这就是每页显示的记录数

然后另外呢有三个这个条件

一个是name

就是我们这个货物类型的名称,对吧

然后呢还有一个是tranctype id

这是什么车辆类型的id,对吧

然后还有一个是什么呢

车辆类型的名称

好

那么一共定义的是这么三个

这么三个条件

再加上我们另外这两个对吧

是分页相关的条件

那么一共呢这个方法呢要接收的是这么五个参数啊

就五个参数

好

那接下来呢我们就把这个方法定义出来

还是找到我们这个goose type controller,对吧

接下来呢我们继续往下写

这个呢就是我们分页方法

好

这个分页方法呢叫做find by page啊

然后返回值是不是就是我们这个什么呢?

叫做page response,对吧

就这个,叫做page response

然后呢这个地方呢我们需要来指定一下这个find型

这个find型的话呢

就是我们封装成什么呢?

封装成这个DTO就可以了

叫做goose type DTO

好,这个

那就意味着我们最终呢

这里边指定的咱们这个list的集合里边是不是全是我们这个DTO对象

好

这个方法名呢我们来定义一下

叫做find by page

先来return down,对吧

然后呢我们来定义一下这个方法的参数,对吧

这个方法的参数呢

刚才分析了一共有

刚才已经看到了一共有五个参数,对吧

分别是什么呢

一个是当前页码

还有是这个查询的记录数,对吧

另外呢还有三个是一个是我们这个车辆

这个货物类型的名称,对吧

还有一个是车辆类型的ID

还有一个是车辆类型的名字

车辆类型的名称

一共是这么几个参数

咱们直接把这块抄过来就可以了

因为这个参数呢我们就不再敲了

那么一共是这么五个参数

其中呢

你看我们后边这三个呢

其实不是必须的

required等于false

那也就是说我们不传过来也是可以的

但是另外这两个page跟page size呢

这个是必须的

这是我们分页这个方法

它的参数定义,对吧

分页查询货物类型的记录数据,对吧

分页查询货物类型的记录数据,对吧

分页查询货物类型的记录数据,对吧

分页查询货物类型

然后呢

我们在这呢给它加一个什么呢

API operation吧

分页查询货物类型

一共是这么五个参数

那接下来呢

我们就来编写看我们这个方法

但是还有一个

咱们是不是忘了加一个什么呢

get mapping

get mapping

然后呢

看我们这个请求的路径呢

就叫做gang page

gang page

分页嘛

这个方法呢

就已经定义了

定义出来

之后呢

接下来就是我们这个方法体

对吧

看这个方法体如何编写

那么很明显呢

我们是不是主要的逻辑

应该是在我们的service里边

也就是说我们在service里边

完成真正的分页查询操作

对吧

所以说呢

我们需要在咱们这个

Ghost type service里边呢

来定义一个方法

那么这个方法呢

其实就是用来进行分页查询的

所以我们找到这个service接口

在这儿

对吧

然后呢

我们在这儿来定义这个分页方法

好

public

然后返回值是什么呢

所以这个返回值的话呢

因为我们后边的真正分页呢

是基于什么呢

是基于咱们这个mybat plus来实现的分页

对吧

所以说呢

我们这块的话呢

就需要来返回这么一个对象

叫做什么呢

叫做ipage

这是mybat plus给我们提供的这么一个接口

对吧

这么一个接口

那么因为我们使用的是这个框架来实现的

而这个框架呢

在进行分页之后呢

我们就要把这个框架呢

再进行分页之后呢

返回的值就是这种类型

就叫做ipage

所以说呢

我们需要使用它

当然它这里边呢

你注意看也是有范形的

带范形的

对吧

带范形

所以我们在这儿需要来指定一下

这个范形是什么呢

这个范形其实对应的就是我们这个实体

pd goose type

对吧

后类型这个实体

好

至于我们这个方法名叫什么呢

其实就无所谓了

咱们就叫find page吧

find by page吧

好

find by page

然后呢

这个方法呢

这个方法要接收的参数是什么呢

是不是应该就是咱们controller

这传过来的这五个参数

这五个参数

刚才我们看到对吧

一个page

还有page size

name

tranquil name

还有tranquil type name

等等这些

所以说呢

我们在这个地方呢

就可以直接拿过来

我们讲一讲抄一下

把这几个参数拿过来

回到接口这边

好

这是跟咱们controller完全对应的

来

controller

controller呢

有这几个参数对吧

那么直接传给他

所以我们在这呢

就再加一个这个啊

再一个注释

好

分页查询

货物类型

好

那这样的话呢

我们这个方法呢

就已经定义好了

关于它这个实现类啊

实现类一会我们再去定义

然后呢

我们回到这边来

那么定义好这个方法之后呢

咱们在这是不是就可以直接去调什么呢

直接去调我们这个goodstype

service点什么呢

find by page

对吧

然后呢把我们这些参数啊

第一个是page

第二个是page size

然后第三个是什么呢

是name吧

name

然后还有一个是什么呢

transctype id

最后一个呢是transctype

name

对吧

好

把这几个参数是不是传进去

这样的话呢

我们就得到了这么一个配置对象的吧

这个配置对象我们来接受一下

咱们就叫goodstype page吧

goodstype

page

这个i就不要了

这个是我们的分页查询

好

这就查完了

但是查完之后呢还不行

还需要啊

还需要去进行处理

因为我们是不是查出来的

最终返回呢

要的是page response这种对象

对吧

并且呢

它这里边封装的对象呢

是这种DTO对象

而我们这里边呢

是这种实体类

对吧

所以说呢

很显然还需要进行转换

同时还有一点是什么呢

我们这个分页查询呢

它其实只是查了什么呢

只是查了我们货物类型这些基本信息

而关联的

而关联信息

比如说我们关联的车辆ID

对吧

并没有去查

并没有去查

所以说呢

我们这一块除了需要进行新的对象封装之外

还有一个就是什么呢

关联信息也需要查一遍

也需要查

那么我们每一个这个什么呢

货物类型是不是都有可能会对应多个什么呢

多个这个车辆类型

所以说呢

我们在这块呢

还需要去查

哎

那么这个如何去查呢

这个如何去查呢

那很显然我们是不是需要先把我们这个分页结果便利一遍

对吧

把每一个什么呢

把每一个这个goose type货物类型给它取出来

然后呢

再去查它所对应的关联的车辆类型的ID

对不对

所以说呢

我们这块呢

就需要来这个处理一下

通过什么呢

goose type

这个goose type配置

对吧

goose type配置

点什么呢

这块是不是有一个叫做getrecall

这个其实就是获得什么呢

获得它的记录

对吧

哎

你看它是不是就是一个粒子集合

其实就是我们根据这些条件查到的多个什么呢

多个这个货物类型

好

咱们呢

可以先接受一下

recause

货物类型

这个recause

然后呢

我们最好啊

还是在处理之前呢

先来干什么呢

先来这个判断一下

对吧

先来判断一下

if什么呢

goose type

这个recause

这个recause

这个recause

这个recause

这个recause

这个recause

这个recause

这个recause

不等于空

同时啊

goose type recourse

点什么呢

size对吧

然后呢

大于0

这个时候呢我们再进一步处理

怎么处理呢

很显然是不是还是需要去

遍历这个集合对吧

遍历这个集合

把每一个这个货物类型取出来

我们要查什么呢

查它所对应的车辆类型ID对不对

所以说呢

这块的话我们

还是要

把它

拿过来然后呢

调用stream

获得留对象对吧

stream对象

然后呢有了这个对象之后呢

我们就可以map

来处理它

通过map来处理它

然后这里边是怎么玩的呢

首先呢我们是不是需要把货物类型

goose type

来定义一下

goose type

然后这里边干什么呢

咱们是不是需要根据这个货物类型来查什么呢

来查我们这个

车辆类型ID对吧

刚才已经分析过了

所以我们在这个地方呢

就需要

把我们这个什么呢

先把这个货物

应该是货物类型的ID对吧

根据货物类型的ID来查询我们这个车辆

这块的话我们其实前面都已经写过了

咱们当时是在哪块呢

是在我们这个

这块是不是已经写过了

对吧

就是根据我们

这个find all方法使用这个方法

根据咱们这个货物类型的ID

来查询

所以说我们把它拿过来

还是调这个什么呢

find all这个方法

只不过这块呢

同样还是车辆类型ID没有

所以直接传个空

然后呢货物类型的ID呢

是不是就是goose type.getID

就取到了

那这样的话呢我们是不是就

拿到了一个集合

对吧

集合

这个集合呢应该就是传个type

goose type

这个吧

这么一个集合

然后呢

咱们是不是需要对这个集合进行一个处理

因为呢我们现在这里面封装的是这种实体对吧

而现在呢我是不是只需要把它这里边的这个车辆类型ID取出来

我关心的是这个ID

所以说呢我们需要对这个集合呢再进行一个处理

把它封装成什么呢

封装成list的

然后里边是string

这个应该是什么呢

是我们的这个trunk

type ID

这个是我们的这个trunk ID

对吧

咱们想要的是这么一个结果

所以说呢我们需要对这个

进行一个处理

这个怎么处理呢

同样的是不是也是啊

给它来一个stream

然后点map对吧

点map

这里边把谁取出来呢

是不是应该就是把我们的这个

来定义一下这里边应该都是

这种对象

这种对象

改成小写的

然后呢

还是这种形式对吧

然后呢我们直接要谁呢

要它的这个pd.get的这个trunk type ID

是不是只要这个

好

要它这个值

最后呢我们是不是把这一块呢给它来处理一下点什么呢

collect的

然后呢这里边还是collectors.toList

这样的话呢咱们这个集合是不是就已经封装好了

跟前面写的其实是一样的

对吧

然后呢我们

放大一点啊

在这个地方

来看

这块

这是把我们这个list的是不是就已经弄好了

然后呢弄好了之后啊注意还没完

咱们现在呢是不是还是在

当前这个Lambda表达室内部的

然后呢我们是不是就需要

把什么呢

把我们这个DTO对象是不是来创建一下

然后呢

并且来set一下

对吧

所以说我们这块啊

把咱们这个DTO对象来创建一下

这个DTO呢就是

Ghost type DTO对吧

Ghost type DTO

等于new一个

Ghost type DTO

好

然后呢我们是不是把它来设置一下

点什么呢

set

set这个

trunk type

idis

然后呢把咱们这个集合

放进去

这样的话关联属性是不是就已经有了

关联属性就已经有了

那么同时呢我们刚才是不是已经查上来了

这个集合呀

也就是说我们是不是还需要把我们这个

货物类型

把货物类型啊

他这里边这些基本属性也给他拷贝过来

所以说呢

这个地方

还得来一个拷贝

beauty of their copy

properties

然后呢从我们这个Ghost type开始考

考到谁呢考到我们这个DTO对象对吧

考到DTO对象

也就是Ghost type DTO

考进来

那么最终呢我们是不是把这个DTO来返回一下Ghost type DTO

来返回一下

那么返回之后呢注意看啊我们这块呢这个代码写的稍微有一点点乱啊因为这块呢

他是有

两个这种拉姆道表达式

这种写法

实际上整个这一块的话

相当于是我们的Map这块

最终呢我们是不是

把每一个这个Record处理把这个Ghost type处理

最终的返回的是DTO

对吧

然后呢我们需要把这个集合是不是给他收集起来

所以说在这呢还得继续来调一个什么呢collect的方法对吧

collect的方法

然后呢这里边还是collectors.toList

这样的话呢我们再来接受一下他的返回值

接受一个返回值

那么你看

他是不是就变成了我们这个list的

里边封装的就是DTO了

这是ghost type

ghost type

DTO

DTO

List

那接下来呢我们是不是就可以

把咱们这个

List的集合呢是不是来进行一个处理对吧

来进行一个封装

把它封装成什么呢封装成我们这个

Page response对象

Page response对象

那么这块呢我们

上面是不是已经加了这个builder啊这个注解

但是呢我们可以使用他的构建器模式啊

他提供的一些构建器的方法

然后呢来封装这个对象

所以我们就可以啊

直接来使用他了

这个叫做什么呢

Page咱们来看啊在这个地方来封装一下

叫做Page response对吧

然后呢这个范型我们是不是来指定一下

这个范型刚才已经写过了就是DTO

把它直接复制过来

然后呢

点什么呢

构建器模式嘛

所以builder

然后呢是不是来设置这里边

好

看一下这个有什么问题啊

builder

点什么呢

items

他这儿报错啊这个地方应该是这样啊

点

builder

然后呢

后边我们是不是来设置啊来设置他相关的值

首先让我们先把最重要的list给他设置上

这个items设置上

而这个items呢

应该对应的就是谁呢是不是应该就是咱们这个list的集合对吧

list集合

这是他的

这个

然后点什么呢

还有cons

总的记录数对吧

这个总的记录数呢我们其实啊

刚才是不是已经进行了分页查询

在这个ipage对象里面其实已经封装了

所以我们在这个地方呢

直接来

get什么呢

get这个

total

这就是总的这个记录数

get total

然后接下来呢就是

点page

page其实就是页码对吧

页码的话呢我们是不是直接啊

就是当前我们传过来的这个page

然后还有什么呢

还有一个叫做

pages

pages

pages

这是总的页数对吧

总的页数的话呢我们

还是通过我们这个goose type

这个

page

点什么呢

get pages

这里边已经封装了对吧

然后呢还有什么呢

还有一个是page size

pages size

就这几个

然后这个page size我们是不是也传过来了从这传过来了

pages size

最后呢调用一个build方法就可以了

调用一个build方法

这样就把这个对象是不是构建出来了

现在他这儿报错的话是因为这儿啊

是因为我们这个fine型

fine型是不是刚才没有指定

这个fine型的话呢我们是不是就使用的这个

dto对象

应该是这样来指定fine型

在这个位置

这样的话我们这个对象是不是就已经封装好了

封装好之后呢直接return它就可以了

不用接收了

直接return

那么到这儿的话呢我们

这个分页方法呢其实就已经写完了

这个就已经写完了

但是大家注意我们现在呢

这个分页

在这个service接口这儿呢是不是已经这个提供了这个方法但是呢实现类还没有实现

我们暂时呢先写这么多对吧

这个呢是在我们这个controller当中把这个fine的page方法写好

一会儿呢我们再去

写这个

分页方法具体的实现

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 的 Java 项目中，实现“分页查询货物类型”功能的开发过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `GoodsTypeController` 中创建一个分页查询接口，并在 `IPdGoodsTypeService` 接口中定义其业务逻辑。核心内容包括：定义控制器方法的注解和参数、调用服务层方法、处理分页数据、以及使用 Java Stream API 和 `BeanUtils` 工具类进行对象属性映射。整个过程展示了典型的前后端分离架构中，控制器层如何调用服务层来完成数据查询和转换。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 IDE 中定位到 `GoodsTypeController.java` 文件，并展示了当前正在开发的章节 `3.4.4 分页查询货物类型`。
*   **00:00:05 - 00:00:15**: 讲师开始编写 `findByPage` 方法，定义了 `@GetMapping("/page")` 注解和 `@ApiOperation` 注解，并声明了 `page`, `pageSize`, `name`, `truckTypeId`, `truckTypeName` 等参数。
*   **00:00:15 - 00:00:25**: 讲师将 `@ApiOperation` 注解的值设置为“分页查询货物类型”，并开始编写方法体，初步返回 `null` 作为占位符。
*   **00:00:25 - 00:00:35**: 讲师切换到 `IPdGoodsTypeService.java` 文件，查看并定义了 `findPage` 方法的签名，该方法返回 `IPage<PdGoodsType>` 类型。
*   **00:00:35 - 00:00:45**: 讲师回到 `GoodsTypeController.java`，在方法体中调用 `goodsTypeService.findPage(...)` 方法，并将返回值赋给 `goodsTypePage`。
*   **00:00:45 - 00:00:55**: 讲师获取分页数据中的记录列表 `goodsTypePage.getRecords()`，并开始处理数据转换。
*   **00:00:55 - 00:01:05**: 讲师使用 Java Stream API 对 `goodsTypePageRecords` 进行处理，调用 `truckTypeGoodsTypeService.findAll(...)` 方法获取关联的 `truckTypeId` 列表。
*   **00:01:05 - 00:01:15**: 讲师使用 `BeanUtils.copyProperties` 方法将 `PdTruckTypeGoodsType` 对象的属性复制到 `GoodsTypeDto` 对象中，并设置 `truckTypeIds`。
*   **00:01:15 - 00:01:25**: 讲师使用 `Collectors.toList()` 将流转换为 `List<GoodsTypeDto>`，并将其赋值给 `goodsTypeDtoList`。
*   **00:01:25 - 00:01:35**: 讲师使用 `PageResponse.builder()` 方法构建最终的分页响应对象，设置 `items`, `counts`, `page`, `pages` 等属性。
*   **00:01:35 - 00:01:45**: 讲师完成 `findPage` 方法的编写，最终返回 `PageResponse` 对象。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲中明确标示了当前章节为 `3.4.4 分页查询货物类型`。
    *   在 `GoodsTypeController.java` 中，注释清晰地说明了每个参数的含义，例如 `@param page 页码`、`@param name 货物类型名称` 等。

*   **关键代码片段**:

    **1. 控制器方法定义 (GoodsTypeController.java)**

    ```java
    @GetMapping("/page")
    @ApiOperation(value = "分页查询货物类型")
    public PageResponse<GoodsTypeDto> findByPage(
        @RequestParam(name = "page") Integer page,
        @RequestParam(name = "pageSize") Integer pageSize,
        @RequestParam(name = "name", required = false) String name,
        @RequestParam(name = "truckTypeId", required = false) String truckTypeId,
        @RequestParam(name = "truckTypeName", required = false) String truckTypeName
    ) {
        // 业务逻辑
    }
    ```

    **2. 服务接口定义 (IPdGoodsTypeService.java)**

    ```java
    public interface IPdGoodsTypeService extends IService<PdGoodsType> {
        // ... 其他方法 ...
        // 分页查询货物类型
        @ApiOperation(value = "分页查询货物类型")
        public IPage<PdGoodsType> findPage(Integer page, Integer pageSize, String name, String truckTypeId, String truckTypeName);
    }
    ```

    **3. 控制器方法实现 (GoodsTypeController.java)**

    ```java
    @GetMapping("/page")
    @ApiOperation(value = "分页查询货物类型")
    public PageResponse<GoodsTypeDto> findByPage(
        @RequestParam(name = "page") Integer page,
        @RequestParam(name = "pageSize") Integer pageSize,
        @RequestParam(name = "name", required = false) String name,
        @RequestParam(name = "truckTypeId", required = false) String truckTypeId,
        @RequestParam(name = "truckTypeName", required = false) String truckTypeName
    ) {
        IPage<PdGoodsType> goodsTypePage = goodsTypeService.findPage(page, pageSize, name, truckTypeId, truckTypeName);
        List<PdGoodsType> goodsTypePageRecords = goodsTypePage.getRecords();
        if (goodsTypePageRecords != null && goodsTypePageRecords.size() > 0) {
            List<GoodsTypeDto> goodsTypeDtoList = goodsTypePageRecords.stream().map(goodsType -> {
                List<String> truckTypeIds = truckTypeGoodsTypeService.findAll(truckTypeId, goodsType.getId()).stream().map(pdTruckTypeGoodsType -> pdTruckTypeGoodsType.getTruckType().getId()).collect(Collectors.toList());
                GoodsTypeDto goodsTypeDto = new GoodsTypeDto();
                BeanUtils.copyProperties(goodsType, goodsTypeDto);
                goodsTypeDto.setTruckTypeIds(truckTypeIds);
                return goodsTypeDto;
            }).collect(Collectors.toList());
            return PageResponse.builder()
                .items(goodsTypeDtoList)
                .counts(goodsTypePage.getTotal())
                .page(goodsTypePage.getCurrent())
                .pages(goodsTypePage.getPages())
                .build();
        }
        return null;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：创建分页查询接口**
    *   **描述**: 讲师在 `GoodsTypeController.java` 中创建了一个名为 `findByPage` 的方法。该方法使用 `@GetMapping("/page")` 注解定义了 HTTP GET 请求的路径，并使用 `@ApiOperation` 注解描述了接口的功能。方法接收多个 `@RequestParam` 参数，用于接收前端传递的分页和筛选条件。
    *   **技术点**: 展示了 Spring MVC 的请求映射和参数绑定机制。

*   **场景二：调用服务层方法**
    *   **描述**: 讲师在控制器方法中调用了 `goodsTypeService.findPage(...)` 方法。通过 IDE 的智能提示，讲师确认了服务接口 `IPdGoodsTypeService` 中 `findPage` 方法的签名，并将返回值赋给 `goodsTypePage` 变量。
    *   **技术点**: 展示了 Spring 的依赖注入和面向接口编程，以及如何在控制器中调用服务层方法。

*   **场景三：处理分页数据和对象转换**
    *   **描述**: 讲师获取了分页数据中的记录列表 `goodsTypePage.getRecords()`，并使用 Java Stream API 对其进行处理。对于每一条记录，讲师调用 `truckTypeGoodsTypeService.findAll(...)` 方法获取关联的 `truckTypeId` 列表，并使用 `BeanUtils.copyProperties` 方法将 `PdGoodsType` 对象的属性复制到 `GoodsTypeDto` 对象中。
    *   **技术点**: 展示了 Java Stream API 的使用、对象属性复制（`BeanUtils.copyProperties`）以及如何处理关联数据。

*   **场景四：构建分页响应对象**
    *   **描述**: 讲师使用 `PageResponse.builder()` 方法构建了一个 `PageResponse` 对象。该对象包含了分页查询的结果（`items`）、总记录数（`counts`）、当前页码（`page`）、总页数（`pages`）等信息。最后，讲师将构建好的对象返回。
    *   **技术点**: 展示了如何使用 Builder 模式构建复杂的响应对象，以及如何封装分
