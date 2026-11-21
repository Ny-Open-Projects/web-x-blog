# 12-货物类型管理（服务接口开发_新增货物类型 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢咱们的service实现

以及我们的Mapper接口都已经定义好了

最后呢还差最后一小点就是什么呢

就是咱们的这个Mapper映射文件对吧

Mapper映射文件

所以我们接下来呢

就需要把咱们这个两个Mapper接口

那么对应的Mapper映射文件

咱们来创建一下

其实就是插门文件对吧

那么我们在这个resource下边

你看下边有个Mapper对吧

然后在这下边呢我们来创建

咱们再给它细分一下

细分成一个叫做base的包对吧

然后呢再来一个trunk的包

首先呢我们在这个base包下边

来创建咱们第一个叫做什么呢

pd-goosetype-mapper吧

pd-goosetype-mapper

然后呢是一个插门文件

第二插门

然后呢在我们下边这个呢

来创建第二个

跟咱们这个接口名称呢

保持一致对吧

保持一致

好

第二插门

实际上呢

我们现在呢这两个文件里边

其实并不需要我们去定义circle语句

就是因为我们当前调用的

它的增伤改查方法呢

其实都是默认的方法对吧

也就是我们框架其实都已经提供好了

所以说呢我们直接把这两个文件啊

它的大体的这个结构给提供一下就可以了

并不需要我们自己去定义任何circle语句

所以说呢我们

接下来呢就把它这个大体的

你看它这个投信息

以及myper这个结构定义好就可以了

在咱们这个pd-goose-type-myper当中呢

来编写这个

这是这个啊

不要贴错了

这个文件呢

咱们应该很熟悉了

使用过mybatties的

咱们应该都了解

上面是投信息

然后呢下边是一个myper

这么一个根标签

在这里边呢

是不是可以定义我们的增伤改查的circle语句

好

因为我们刚才直接调用的是mybattiesplus

给我们提供的那个insert方法

对吧

实际上那个circle的话

由框架已经提供好了

所以我们并不需要自己在这里面去定义circle

那什么时候我们需要在这定义呢

就是我们自定义的一些这个方法

对吧

自定义的一些circle语句

那这个时候呢

框架没有提供

我们可以自己在这来进行这个编写

这是第一个

然后接下来呢

我们再来看第二个

这是对应的是那个关系表

对吧

对吧

对吧

对吧

然后这个myper

好

主要呢

是检查一下这个地方

就是我们按着control呢

点击一下能点过来

这就说明我们整个这个类路径呢

是完全正确的

如果你这个有编写错误的话呢

有拼写错误的话呢

它其实是点不过来的

所以到这儿的话呢

我们整个这个新增

对吧

新增这个货物类型呢

代码就已经写完了

整体来说呢

其实还是非常简单的

那么我们编写了这个

我们编写了control了

编写了service

编写了myper

对吧

其实对应的就是dao

只不过我们命名上呢

叫做myper

还有最后就是我们的应用文件

那么整个呢

我们都已经写完了

写完之后呢

我们后边呢

就可以进行一个测试了

咱们现在呢

可以来启动一下

看看我们当前编写的这个代码

有没有什么问题

并且呢

我们再来测一下

好

那么现在我们来重新启动一下

好

咱们现在这个服务呢

已经启动完了

并且呢

没有报错

好

那接下来呢

我们来测试一下

咱们就直接使用咱们这个swagger

这个接口呢

来进行测试就可以了

好

但是在测试之前呢

我们先看一下

观察一下我们现在的数据库里边

对应的我们要操作的是两张表

对吧

那么咱们打开这个数据库来看一下

好

连接上

我们要操作的是pdbase

这个数据库

里面的两张表

一个呢

是我们这个货物类型

对吧

货物类型

就是这个pdgootstab

还有一个呢

是那个中间关系表

中间关系表呢

咱们来找一下在哪呢

是这个对吧

pdtranctype

gootstab

那么我们目前呢

要测试的这个接口

对应的会操作这两张表

来看一下

我这里边应该是有一些测试数据的

你看这里面有一些测试数据

这个我们不用管他了

咱们自己再来测就行了

当前的我们来看一下

他这里边一共有

32条数据

对吧

现在有32条数据

然后这个关系表里面呢

有多少条呢

这是有49条数据

这是我们前面的测试数据

这就不用管他了

然后接下来呢

我们来测试这个接口

发信一下

然后呢

我们现在来看

try it out

对吧

然后呢

这个默认值呢

咱们就随便输一个

1

这个来个2

然后这个主件

其实不用输入

对吧

这个主件不用输入

我们

是通过id generator

那个对象呢

给我们生成的

然后呢

咱们这个货物类型名称

比如说我们这个就叫什么呢

叫做

3C

对吧

产品

这个呢

就是随便写一个

然后备注的话呢

就写个5吧

然后这个状态的话呢

我们给一个1

1表示正常

对吧

然后注意看

这是不是有这个

trunk type id

也就是对应的

他要关联我们这个货物

这个这个车辆类型的

id 对吧

车辆类型id

好

那么车辆类型id的话呢

呃

注意咱们这个呢

就不能随便写了

哎

那么我们需要来看一下

咱们这个车辆类型

哎

都有哪些

车辆类型啊

我们来看一下

应该叫做trunk type

PD trunk type

对吧

那么他要关联的是这个啊

指定的是这里面的id

所以说呢

我们从这呢

可以来找一下

这里面也有一些测试数据

对吧

比如说你看我这车辆类型一

车辆类型三等等啊

然后呢

我们可以随便先复制

一个

然后呢

还可以add item

因为它是一个list的集合嘛

所以说我们在这个地方呢

可以有多个车辆类型

咱们再来复制一个

就复制这两个就可以了

好

然后呢

我们现在呢

就可以直接点击execute

咱们来执行一下

走

好

然后呢

注意看

这个read

response

它是不是已经给我们返回回来了

返回回来的其实对应的是什么呢

还是我们那个dto对象对吧

还是dto对象啊

只不过这个时候呢

你注意看他的id是不是就有值了

这说明我们刚才呢

已经保存成功了

并且使用的就是这个id的值

咱们现在回到我们这边来

打开我们刚才这个啊

他应该保存了一个货物类型

打开

你看现在是不是变成了33条数据

刚才呢

我们看到是32条对吧

应该是增加了一倍啊

一个你看就是最后这个是3c产品

这是我们刚才录入的这个啊

然后他的id是这个

然后接下来呢

我们再来看什么呢

就是看他这个中间关系表对吧

中间关系表呢

应该增加了两条数据

因为我们对应的是不是提交过来了两个这个什么呢

车辆类型的id

所以对应的应该是两条关联信息

你看现在是51条

刚才是不是49条数据

只不过这个呢

要找的话确实就不太好找了

因为记录的是他的这个什么呢

记录的是他的id啊

咱们的可以这样来查询一下对吧

查询一下

那么我们可以在这儿来使用这个工具啊

然后呢

打开一个这个界面在这儿来查一下

select from什么呢

咱们这个关系表的吧

我们那个关系表的名字是不是叫这个

拿过来

然后为了为什么呢

咱们

来看一下咱们这个是不是应该是根据这个货物类型id的吧

goose type id来查一下

goose type id等于

我那个值的话呢

我们刚才看到了

他给我们返回的就是这一个id

所以根据他来查一下就可以了

你看是不是能查到

这样的话就把我们

这是刚才插入那两条关联数据对吧

也能查到

这就说明没有问题

monte

嘿

tags

我

这

完全没问题

这个

这

你

你

那个

没问题

还没问题

这个

这样

kraken

真的

有

我的

这个

它的

就是

不是

一个

一个

一个

一个

一个

一个

对

我就

会

说

个

一个

个

一个

一个

一个

一个

一个

一个

一个

一个

一个

一个

一个

就是

一个

一个

一个

一个

一个

一个

一个

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于一个名为“品达TMS”（Pinda TMS）的物流管理系统开发教程的一部分，具体聚焦于“货物类型管理”功能的实现。讲师通过 IntelliJ IDEA 和 Navicat Premium 等开发工具，演示了如何在 Spring Boot + MyBatis 框架下，完成从数据库表设计、Mapper 接口定义、Service 层业务逻辑编写，到最终通过 Swagger UI 进行接口测试的完整开发流程。核心内容包括：创建 `PdGoodsType` 实体类、定义 `PdGoodsTypeMapper` 和 `PdTruckTypeGoodsTypeMapper` 接口、编写 `PdGoodsTypeServiceImpl` 服务类实现增删改查功能，并通过 Swagger UI 进行测试，最后在 Navicat 中验证数据库中的数据变更。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:04**: 视频开头，讲师在 IntelliJ IDEA 中展示 `PdGoodsTypeServiceImpl.java` 文件，讲解 `saveGoodsType` 方法的实现，其中使用了 `@Autowired` 注入 `CustomIdGenerator` 生成主键，并调用 `baseMapper.insert` 方法插入数据。
*   **00:04 - 00:08**: 讲师切换到 `PdTruckTypeGoodsTypeServiceImpl.java` 文件，演示 `batchSave` 方法，用于批量保存货物类型与车辆类型的关联关系。
*   **00:08 - 00:12**: 讲师展示 `PdTruckTypeGoodsTypeMapper.xml` 文件，讲解 MyBatis 的 XML 映射文件结构，包括 `mapper` 标签和 `namespace` 属性。
*   **00:12 - 00:16**: 讲师展示 `PdTruckTypeGoodsTypeMapper.java` 接口文件，讲解其继承自 `BaseMapper` 并使用 `@Mapper` 注解。
*   **00:16 - 00:20**: 讲师在浏览器中打开 Swagger UI 网页，准备进行接口测试。
*   **00:20 - 00:24**: 讲师在 Swagger UI 中展示 `SaveGoodsType` 接口的请求参数，包括 `id`, `name`, `remark`, `status`, `truckTypeIds`。
*   **00:24 - 00:28**: 讲师在 Swagger UI 中填写请求参数，设置 `name` 为“3C产品”，`status` 为“1”，并点击“Execute”按钮发送请求。
*   **00:28 - 00:32**: 讲师在 Navicat 中打开 `pd_goods_type` 数据表，展示新插入的记录。
*   **00:32 - 00:36**: 讲师在 Navicat 中打开 `pd_truck_type` 数据表，展示其结构。
*   **00:36 - 00:40**: 讲师在 Navicat 中打开 `pd_truck_type_goods_type` 数据表，展示其结构。
*   **00:40 - 00:44**: 讲师在 Navicat 的 SQL 编辑器中输入 SQL 查询语句，用于验证数据关联。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   项目名称：品达TMS项目。
    *   当前章节：第2章 基础数据服务开发。
    *   子章节：3.4 货物类型管理。
    *   子章节：3.4.1 新增货物类型。
    *   子章节：3.4.2 查询所有货物类型。
    *   子章节：3.4.3 查询货物类型列表。
    *   子章节：3.4.4 删除货物类型。
    *   子章节：3.4.5 修改货物类型。
    *   子章节：4. 数据校验。
    *   子章节：5. 导入基础数据及其他代码。

*   **代码关键内容**:
    *   **Service 层代码 (`PdGoodsTypeServiceImpl.java`)**:
        ```java
        @Autowired
        private CustomIdGenerator idGenerator;

        @Override
        public PdGoodsType saveGoodsType(PdGoodsType pdGoodsType) {
            pdGoodsType.setId(idGenerator.nextId(pdGoodsType + ""));
            baseMapper.insert(pdGoodsType);
            return pdGoodsType;
        }
        ```
    *   **Service 层代码 (`PdTruckTypeGoodsTypeServiceImpl.java`)**:
        ```java
        @Override
        public void batchSave(List<PdTruckTypeGoodsType> truckTypeGoodsList) {
            truckTypeGoodsList.forEach(truckTypeGoods -> {
                truckTypeGoods.setId(idGenerator.nextId(truckTypeGoods + ""));
            });
            saveBatch(truckTypeGoodsList);
        }
        ```
    *   **Mapper 接口代码 (`PdTruckTypeGoodsTypeMapper.java`)**:
        ```java
        package com.itehima.pinda.mapper.truck;
        import com.itehima.pinda.entity.truck.PdTruckTypeGoodsType;
        import org.apache.ibatis.annotations.Mapper;
        import org.apache.ibatis.annotations.Param;
        import org.apache.ibatis.annotations.Select;
        import org.apache.ibatis.annotations.Update;
        import org.springframework.stereotype.Repository;
        import java.util.List;
        @Mapper
        public interface PdTruckTypeGoodsTypeMapper extends BaseMapper<PdTruckTypeGoodsType> {
        }
        ```
    *   **MyBatis XML 映射文件 (`PdTruckTypeGoodsTypeMapper.xml`)**:
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
        <mapper namespace="com.itehima.pinda.mapper.truck.PdTruckTypeGoodsTypeMapper">
        </mapper>
        ```

*   **图表/数据库结构**:
    *   **数据库表结构图**: 展示了 `pd_goods_type`、`pd_truck_type`、`pd_truck_type_goods_type` 等表的结构。
    *   **数据表内容**: 展示了 `pd_goods_type` 表中新增的记录，以及 `pd_truck_type_goods_type` 表中关联的数据。

---

### 4) 关键场景与演示描述

*   **场景一：Service 层开发与测试**
    *   **描述**: 讲师在 IntelliJ IDEA 中编写 `PdGoodsTypeServiceImpl` 类，实现了 `saveGoodsType` 方法。该方法首先通过 `CustomIdGenerator` 生成主键 `id`，然后调用 `baseMapper.insert` 方法将对象插入数据库。讲师随后在 Swagger UI 中调用此接口，成功创建了一条新的货物类型记录。
    *   **技术点**: Spring Boot + MyBatis 的集成、自定义 ID 生成器、Mapper 接口调用、Swagger UI 接口测试。

*   **场景二：批量操作与关联数据处理**
    *   **描述**: 讲师在 `PdTruckTypeGoodsTypeServiceImpl` 中编写了 `batchSave` 方法，用于批量保存货物类型与车辆类型的关联关系。该方法遍历传入的列表，为每个对象生成 ID，然后调用 `saveBatch` 方法进行批量插入。
    *   **技术点**: 批量操作、数据关联、Spring Boot 的批量插入功能。

*   **场景三：数据库验证**
    *   **描述**: 讲师在 Navicat Premium 中打开数据库，首先查看 `pd_goods_type` 表，确认新插入的货物类型记录已存在。接着，讲师查看 `pd_truck_type_goods_type` 表，确认了新插入的关联数据。
    *   **技术点**: 数据库操作、数据验证、SQL 查询。

*   **场景四：Swagger UI 接口测试**
    *   **描述**: 讲师在浏览器中打开 Swagger UI，定位到 `SaveGoodsType` 接口。讲师填写了 `name` 为“3C产品”，`status` 为“1”，并点击“Execute”按钮。接口返回 200 OK，表明操作成功。
    *   **技术点**: API 接口测试、Swagger UI 使用。

*   **场景五：SQL 查询验证**
    *   **描述**: 讲师在 Navicat 的 SQL 编辑器中输入 SQL 查询语句 `SELECT * FROM pd_base.pd_truck_type_goods_type WHERE goods_type_id = 1`，用于验证数据关联。
    *   **技术点**: SQL 查询、数据关联验证。
