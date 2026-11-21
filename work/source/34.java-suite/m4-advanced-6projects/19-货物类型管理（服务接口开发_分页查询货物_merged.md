# 19-货物类型管理（服务接口开发_分页查询货物 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

继续来看咱们这个分页查询

分页查询我们的货物类型

刚才呢我们control的方法当中啊

find by page这个方法已经写完了

那么下一个呢

我们要写的就是这个service对吧

这个service咱们在这呢

是定义了这个方法

但是呢还没有去实现

所以说我们需要找到它的实现类啊

打开它的实现类

然后呢我们在这呢

来实现这个方法

好这个是分页查询货物类型

这块我们写起来了

其实就比较简单了

那么我们直接使用什么呢

使用我们这个mybeta的框架

给咱们提供的这么一个类啊

就是用来封装我们这个分页查询条件的

就叫做page对吧

咱们应该都用过啊

然后呢它这里边是不是也要指定一个find型

这个find型呢就是我们这个实体类啊

pd ghost type对吧

然后呢这是我们的分页条件page

但是因为这儿已经有这个page对吧

那么我们就叫pd

对吧

对吧

pd ghost type对吧

pd ghost type对吧

pd ghost type对吧

pd ghost type对吧

pd ghost type对吧

然后呢先把它new出来对吧

这个呢这是封装我们的这个条件

new一个page

然后呢把我们这两个参数啊

一个是我们的page

还有一个是page size

是不是需要传进去

还有一个是page size

需要传进去

这是分页的这两个条件

那么同时呢我们是不是还需要根据什么呢

根据这后边这三个参数

进行这个查询

但是这三个参数呢是可以为空的对吧

就是说当它

不为空的时候是不是作为条件

如果为空呢就忽略它

所以说一会儿我们肯定是需要自己去写一个动态circle对吧

去写一个circle

好

咱们先把这个条件封成好

封装分页条件

好

那么主要就是分页相关的这两个

一个是page

还有一个是page size

封装好

好

封装好之后呢

咱们就可以干什么呢

是不是来调用啊

来调用我们这个先来给它添加一个排序吧

加一个排序条件

先来给它添加一个排序条件

先来给它添加一个排序条件

嗯

先来加一个排序条件啊

添加这个排序条件

直接在这个pd配置里面添加就可以了

直接调用它的一个叫做add order这个方法

是吧

然后呢

我们这个地方呢

就可以直接根据什么呢

根据id来进行一个生续排列就可以啊

比如说我们来一个other items.什么呢

asa

然后呢

指定我们的一个属性

id

其实就是根据咱们这个货物类型的id呢

来进行一个生续排列就可以了

好

这是添加了一个排序条件

然后接下来呢

我们是不是就需要来调用我们这个base mapper是不是来进行查询

查出来之后呢

把它封装到我们这个配置对象里面去

对吧

封装到这个配置对象里面去啊

所以我们这块呢

就需要

嗯

调用这个pd

配置点什么呢

set records

记录

对吧

而这个记录的话呢

是不是应该我们是查出来的啊

通过调用我们的base mapper对吧

调用我们这个base mapper

然后呢

我们在这里面来提供这么一个方法叫做find by page

find by page

但是现在还没有啊

一会我们需要去在咱们这个mapper借口里面去定义这个方法

好

然后呢

这这个方法呢

是不是要求

接收几个参数呢

注意

接收几个参数呢

一个呢

就是我们这个配置对象对吧

好

因为我们的配置还有配置size呢

全都封装到这个对象里面去了

所以说呢

我们在这个地方

我们呢

我们在这个地方呢

给它传进去

然后呢

就是我们传过来的这个name对吧

然后还有什么呢

tranctype id

还有一个就是tranctype name

好

把这几个参数都传进去

最终呢

我们是不是把这个pd啊

这个配置返回一下就可以了

好

大家要注意看啊

我们这写的是ipage

这写的是page

这是怎么回事呢

这是因为ipage呢

它其实是个接口

而我们这个page呢

其实是它的实验类

对不对

好

这个我们前面在讲mybizplus的时候呢

应该也都提到过了

所以我们在这呢

就不再过多的去强调了

而是直接啊

直接写代码就可以了

好

那这样的话呢

我这个地方还爆红呢

对吧

哎

这说明什么呢

我们需要在咱们这个myper里边

这个对吧

pd ghost type

这里边

ghost type myper里边来定义刚才我们这个find by page这个方法

好

嗯

这块呢

我就不再手敲了啊

我咱们直接啊

嗯

找到这儿来

在我们这个myper里边来定义这个方法

好

我直接把这个方法呢

拷过来

放到这里面去

好

咱们来看一下

你看

我们是不是这个方法名find by page

跟这个是一样的

然后返回值呢

肯定是一个粒子的集合

里边装的呢

就是我们实体类的吧

这样的话

你看这边它是不是就不报错了

对吧

set recos

接收的就是这个结果

然后呢

参数呢

就是我们传进来的这个结果呢

这三个参数

对吧

就是三个参数

对吧

一个是page

这个呢

是做分页查询的

然后另外三个呢

是作为动态的条件

对吧

查询条件

好

这是我们分页查询啊

这么一个方法的声明

那接下来呢

我们就需要来写一个对应的sql语句

对吧

对应的sql语句

呃

然后呢

它的这个查询条件呢

就是我们传进来的这三个条件

好

那么因为我们在这呢

大家要注意啊

因为我们在这呢

已经加了什么呢

已经加了咱们这个分页

的这个

pagination intercept

这个拦截器

对吧

哎

所以说呢

我们这个动态sql语句里边呢

就不用自己再写什么呢

关于分页的语句了

什么limit

哎

等等这些关键字就不用写了

好

那么我们只是参照这三个

来查询就可以

那么其他的呢

是由这个拦截器啊

由mybases给我们这个提供的拦截器

然后呢

由它来帮我们加入分页的这个语句

好

那接下来呢

我们就需要啊

打开咱们这边

my

per这边是吧

找到什么呢

找到我们这个pd

goose type myper

然后在这里边呢

来编写我们这个分页的动态sql

呃

这个sql呢

我们就不在现场编写了

因为这个sql呢

咱们直接抄过来啊

带着大家来读一下

来看一下它是怎么写的

好

直接复制过来

大家来看

呃

id呢

find by page

这个必须要跟我们这个方法名

是不是能对应上啊

这个必须得能对应上

然后接下来

result type对吧

result type呢

就是我们这个实体类型

它的全路径

对吧

这是这个

那么它要跟谁对应呢

是不是需要跟我们这个类型来对应啊

这都是一些规则啊

都是一些规则

然后呢

到这边来

嗯

看一下这个sql啊

这个sql的话相对来说还是比较简单的

你不要看它好像挺长

是因为它拼接了一些动态的这个

呃

条件对吧

啊

实际上整个这个结构呢

还可以啊

那你看select它

对吧

goose type点星

goose type呢

这是我们这个表的一个别名

对吧

然后呢

这就是表示我要查的是我们

货物类型表所有的字段

然后呢

从我们这个表里面来查

然后呢

这块呢

哎

因为我们还还需要去干什么呢

哎

连接对吧

连接我们那个中间关系表啊

以及那个什么呢

车辆类型表对吧

所以说呢

这块的话呢

我们先来判断一下

判断一下

哎

这个车辆类型id是否为空

如果不为空的话呢

我们是不是就要连接它

因为什么呢

因为我们从control的时候

就能看到传过来的条件

是不是有可能有这个车辆类型的id啊

那么如果传过来它的话呢

我是不是就需要根据它作为条件来查询

根据它作为条件来查询

而对于我们这个货物类型这个表里面

根本就没有这个字段

对吧

它是通过这个关联表

这样是不是关联起来的

所以说呢

我们在这呢

就需要来一个什么left join

对吧

一个左连接

然后呢

连接到我们这个表

好

这是那个中间关系表

对吧

这个名字很长

好

然后呢

它们之间的关系呢

是不是就是这个货物类型id

等于这个表的这个goose type id

好

那么如果是传过来这个参数不等于空

那么我们就需要来做一个连接

因为一会儿呢

这个地方呢

我们是不是需要使用它来作为一个条件

来作为一个条件

那么同理啊

还有可能有这个什么呢

传个type name

对吧

所以说呢

也需要连接一下

好

这个都是类似的

然后接下来呢

是where条件

where条件

where条件呢

首先我们要查的都是

这个

这个呢

stats等于1的

对吧

就是这种正常状态的

状态是正常的

正在使用的

然后呢

接下来

如果是这个name不等于空

对吧

然后呢

我们是不是就加这么一个

同时呢

这个车辆类型呢

它是不是也有状态啊

也得等于1

那么如果我们传过来的这个货物类型名字不等于空

那么是不是就使用like啊

其实是一个模糊查询

对不对

如果是车辆类型id呢

不等于空

那么就会使用这个条件来进行一个查询

来进行一个查询

所以说呢

下面这一块

其实跟上面这一块呢

是一个对应关系啊

是一个对应关系

对吧

如果不为空的话呢

我们就需要使用这种关联查询

所以前面呢

需要给它追加上这个left的这个左连接

那么因为我要使用它这个什么呢

transcript type id作为条件

动态拼到这

那么transcript type name呢

其实也是一个意思啊

只不过呢

它是一个什么呢

模糊查询

所以使用like

这个呢

都属于我们这个买卖T4

它的基础语法

对吧

就是编写这个Mapper应设文件

好

整个分析一下这个结构就可以了

好

那么到这儿的话呢

我们整个这个分页代码呢

其实就已经写完了

一会儿呢

我们整体来测试一下这个分页

方法就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的Java后端开发教程，主要演示如何实现一个“分页查询货物类型”的功能。该功能涉及多个层级的代码，包括控制器（Controller）、服务（Service）和数据访问对象（Mapper）。视频通过IntelliJ IDEA开发环境，逐步展示了如何在`GoodTypeController`中定义接口、在`PdGoodsTypeServiceImpl`中实现业务逻辑、以及在`PdGoodsTypeMapper`中编写MyBatis动态SQL语句。核心是实现一个支持按名称、车辆类型ID和车辆类型名称进行多条件模糊查询的分页功能，并将查询结果封装为分页响应对象返回。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:03**: 视频开头，展示`GoodTypeController.java`文件，其中`findPage`方法的返回值被定义为`IPage<PdGoodsType>`，并展示了该方法的完整实现逻辑，包括对查询结果进行处理并返回`PageResponse`。
*   **00:00:03 - 00:00:07**: 切换到`PdGoodsTypeServiceImpl.java`文件，展示`findPage`方法的定义，该方法接收分页参数和查询条件，并返回一个`IPage<PdGoodsType>`对象。
*   **00:00:07 - 00:00:11**: 在`PdGoodsTypeServiceImpl.java`中，演示如何创建一个`Page<PdGoodsType>`对象，并设置分页条件和排序条件。
*   **00:00:11 - 00:00:15**: 展示如何调用`baseMapper.findByPage`方法，将构建好的分页对象和查询参数传递给Mapper层。
*   **00:00:15 - 00:00:19**: 切换到`PdGoodsTypeMapper.java`接口，展示其定义的`findByPage`方法签名。
*   **00:00:19 - 00:00:23**: 切换到`PdGoodsTypeMapper.xml`文件，展示MyBatis的动态SQL语句，用于实现多条件查询。
*   **00:00:23 - 00:00:27**: 详细讲解MyBatis动态SQL中的`<if>`标签，用于根据传入的参数动态拼接WHERE条件。
*   **00:00:27 - 00:00:31**: 展示最终的MyBatis SQL语句，包含LEFT JOIN关联表和复杂的WHERE条件。
*   **00:00:31 - 00:00:35**: 回到`PdGoodsTypeServiceImpl.java`，展示如何将Mapper层查询到的分页结果设置到`Page<PdGoodsType>`对象中。
*   **00:00:35 - 00:00:39**: 展示最终的`findPage`方法，将构建好的分页对象返回。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   在视频的早期，展示了项目结构的目录树，包括`controller`、`service`、`mapper`等包。
    *   在视频的后期，展示了`PdGoodsTypeMapper.xml`文件的结构和内容。

*   **代码关键内容**:
    *   **控制器层 (`GoodTypeController.java`)**:
        ```java
        @GetMapping("/findPage")
        public IPage<PdGoodsType> findPage(@RequestParam Integer page, @RequestParam Integer pageSize, @RequestParam String name, @RequestParam String truckTypeId, @RequestParam String truckTypeName) {
            // 业务逻辑
            IPage<PdGoodsType> goodsTypePage = goodsTypeService.findPage(page, pageSize, name, truckTypeId, truckTypeName);
            return goodsTypePage;
        }
        ```
        *   该方法接收分页参数和查询条件，并调用服务层方法。
        *   最终返回一个`IPage<PdGoodsType>`对象，表示分页查询结果。

    *   **服务层 (`PdGoodsTypeServiceImpl.java`)**:
        ```java
        @Override
        public IPage<PdGoodsType> findPage(Integer page, Integer pageSize, String name, String truckTypeId, String truckTypeName) {
            Page<PdGoodsType> pdPage = new Page<>(page, pageSize);
            pdPage.addOrder(OrderItem.asc("id")); // 设置排序条件
            pdPage.setRecords(baseMapper.findByPage(pdPage, name, truckTypeId, truckTypeName)); // 调用Mapper层查询
            return pdPage;
        }
        ```
        *   创建一个`Page`对象用于分页。
        *   设置排序条件。
        *   调用`baseMapper.findByPage`方法执行数据库查询，并将结果设置到`Page`对象中。
        *   返回`Page`对象。

    *   **Mapper层 (`PdGoodsTypeMapper.java`)**:
        ```java
        public interface PdGoodsTypeMapper extends BaseMapper<PdGoodsType> {
            List<PdGoodsType> findByPage(Page<PdGoodsType> page, @Param("name") String name, @Param("truckTypeId") String truckTypeId, @Param("truckTypeName") String truckTypeName);
        }
        ```
        *   定义了`findByPage`方法，用于查询分页数据。

    *   **MyBatis XML (`PdGoodsTypeMapper.xml`)**:
        ```xml
        <select id="findByPage" resultType="com.iteima.pinda.entity.base.PdGoodsType">
            SELECT goods_type.*
            FROM pd_goods_type goods_type
            <if test="truckTypeId != null || truckTypeName != null">
                LEFT JOIN pd_truck_type_goods_type truck_type_goods_type ON goods_type.id = truck_type_goods_type.goods_type_id
                <if test="truckTypeName != null">
                    LEFT JOIN pd_truck_type truck_type ON truck_type_goods_type.truck_type_id=truck_type.id
                </if>
            </if>
            <where>
                goods_type.status=1
                <if test="truckTypeName != null">
                    AND truck_type.status=1
                </if>
                <if test="name != null">
                    AND goods_type.name LIKE "%#{name}%"
                </if>
                <if test="truckTypeId != null">
                    AND truck_type_goods_type.truck_type_id = #{truckTypeId}
                </if>
                <if test="truckTypeName != null">
                    AND truck_type.name LIKE "%#{truckTypeName}%"
                </if>
            </where>
        </select>
        ```
        *   使用`<if>`标签实现动态SQL，根据传入的参数动态拼接WHERE条件。
        *   使用`LEFT JOIN`关联`truck_type_goods_type`和`truck_type`表，实现多表查询。
        *   最终查询满足条件的`goods_type`记录。

---

### 4) 关键场景与演示描述

*   **场景一：分页查询功能的实现**:
    *   **演示描述**: 视频首先展示了`GoodTypeController`中`findPage`方法的实现，该方法接收分页参数和查询条件，并调用`goodsTypeService.findPage`方法。接着，视频展示了`PdGoodsTypeServiceImpl`中`findPage`方法的实现，该方法创建一个`Page`对象，设置排序条件，并调用`baseMapper.findByPage`方法执行数据库查询。最后，视频展示了`PdGoodsTypeMapper`接口中`findByPage`方法的定义，以及`PdGoodsTypeMapper.xml`中对应的MyBatis动态SQL语句。

*   **场景二：MyBatis动态SQL的编写**:
    *   **演示描述**: 视频详细讲解了如何在`PdGoodsTypeMapper.xml`中编写MyBatis动态SQL。通过`<if>`标签，根据传入的参数动态拼接WHERE条件。例如，当`truckTypeName`不为空时，会关联`truck_type`表，并在WHERE条件中添加`truck_type.status=1`。当`name`不为空时，会添加`goods_type.name LIKE "%#{name}%"`条件。当`truckTypeId`不为空时，会添加`truck_type_goods_type.truck_type_id = #{truckTypeId}`条件。当`truckTypeName`不为空时，会添加`truck_type.name LIKE "%#{truckTypeName}%"`条件。

*   **场景三：分页对象的封装与返回**:
    *   **演示描述**: 视频展示了如何在服务层将Mapper层查询到的分页结果设置到`Page`对象中。通过调用`pdPage.setRecords(...)`方法，将查询到的列表设置到`Page`对象中。最后，将`Page`对象返回给控制器层，由控制器层返回给前端。

*   **场景四：项目结构与代码组织**:
    *   **演示描述**: 视频通过IDEA的项目结构视图，展示了项目的包结构，
