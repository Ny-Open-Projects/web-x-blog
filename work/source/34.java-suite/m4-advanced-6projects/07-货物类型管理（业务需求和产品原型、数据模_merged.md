# 07-货物类型管理（业务需求和产品原型、数据模 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面的话呢,咱们已经把这个基础数据微服务开发准备呢都已经准备好了,对吧,主要呢是提供我们Spring Boot的配置文件,对吧,然后呢服务启动类配置类还有一个小的组件就是ID生成器。

好,那么这些准备工作呢都做好之后呢,我们下面呢就来开发我们第一个业务功能,就是这个货物类型的管理。

货物类型呢,其实前面我们都已经提到过了,它其实呢对应的是我们这么一张表,叫做Goose Type,对吧,因为我们在这个货物运输的时候呢,每一个货物呢都会对应一种类型,比如说是什么呢,是这个衣服,对吧,或者是电子产品,或者什么书籍等等。

就是说每一个货物呢都会对应这么一种类型,那么我们这块呢其实就是对我们货物类型呢进行一个数据的维护。

所以从业务上来说呢,这块还是非常非常简单的一个业务,属于非常基础的业务。

好,那么首先呢我们先来看一下咱们这个货物类型管理,第一部分呢就是这个业务需求还有产品原型。

货物类型呢是TMS的基础数据,表示什么呢?表示货物这个物流。

货物的类别,例如什么有服饰,对吧,然后什么食品,数码产品等等。

那么刚才我们也提到了,像什么电子产品等等这些,都属于某一种货物类型。

然后呢具体对应的产品原型的话呢,我们可以来看一下咱们这个图,或者说呢直接通过我们的蓝湖呢也能看到。

因为我们这个图呢其实就是从蓝湖上截取下来的,咱们可以从这边来看一下。

这个呢是我们的货物类型管理。

这个呢是产品经理呢,他设计的时候呢会使用这个平台来管理啊,来管理他这个设计的一些原型,还有一些文档。

在这个后台下边咱们来看一下我们的后台。

然后呢我们直接找到什么呢?找到咱们这个货物类型,对吧,货物类型来找一下,这里面东西稍微多一点。

在这个地方,对吧,这个有一个叫做货品类型,其实就是货物类型啊。

然后呢就是这么一个页面,上面呢是不是有两个,

搜索框,对吧,可以进行搜索。

但是现在你点这个是没有效果的,它这个呢只是一个静态页面,为了能说明这个功能,这样呢更直观一点。

然后呢我们可以点击这个新增,对吧,然后呢可以添加新的货物类型。

然后呢这是一个列表,对吧,并且呢可以实现分页,然后呢可以删除,可以修改。

然后呢这有个刷新按钮。

那么这就是咱们这个货物类型啊,它的一个效果。

这是它的原型,对吧。

然后呢这是新的。

新增的页面。

然后接下来呢我们来看一下,咱们这个原型是这个样子的,最终呢实际上我们操作的数据模型,或者我们的数据库的表,也就是我们的数据模型这一块呢,那么对应操作的就是我们刚才看到的,叫做PD,Goose Type,对吧,这张表。

这张表的结构呢,咱们再整体过一下,有什么呢,ID,这是主件,对吧,然后呢货物类型的名称,对吧,还有默认重量,默认重量单位是千克,还有默认的体积。

对吧。

就是每一种类型呢,我们都给它一个默认值,对吧,重量默认是多少,体积默认是多少。

然后呢还有说明,然后还有一个状态,对吧,是否是禁用的。

这个表呢,整体来说呢,还是非常简单的这么一张表。

那么这是咱们先来了解一下我们的业务需求,还有产品原型,以及对应的要操作的是哪个数据模型。

一会儿呢我们就可以啊,来编写我们的Java代码。

好,那么这是关于业务需求,产品原型,还有数据模型。

好了,现在我们就来看看我们现在的业务需求,我们先来看看,嗯,我们的月务收入,我们认为是1500。

我们的月薪是1300。

我们的月薪是1500。

我们的月薪是3500,我们的月薪是1600。

我们的月薪是410。

我们的月薪是310。

我们的月薪是2500。

我们的月薪是2400,我们的月薪是4500。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是“品达物流TMS项目”第二章“基础数据服务开发”的一部分，具体聚焦于“3. 货物类型管理”模块。讲师通过展示产品原型、数据库表结构和Java实体类代码，系统性地讲解了如何从需求分析到技术实现，定义和管理货物类型。视频内容主要围绕“货物类型”这一核心业务实体展开，涵盖了其前端界面设计、后端数据模型以及对应的Java开发代码，旨在为后续的微服务开发打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示课程大纲，定位到“3. 货物类型管理”下的“3.1 业务需求和产品原型”。
*   **00:05 - 00:15**: 展示“货物类型管理”的产品原型界面，介绍其功能和字段。
*   **00:15 - 00:25**: 切换到“3.2 数据模型”章节，展示数据库表结构。
*   **00:25 - 00:35**: 展示“3.3 导入实体类”的Java代码，讲解实体类的定义。
*   **00:35 - 00:45**: 展示“3.4 服务接口开发”的代码片段（未完全展示）。
*   **00:45 - 00:55**: 展示“3.5 数据校验”的代码片段（未完全展示）。
*   **00:55 - 01:05**: 展示“3.6 导入基础数据服务其他代码”的代码片段（未完全展示）。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   **3.1 业务需求和产品原型**: 描述了货物类型是TMS的基础数据，用于表示物流货物的类别，如服饰、食品、数码产品等。并展示了产品原型界面，包含“货品类型名称”、“品牌编码”、“默认重量”、“默认体积”、“说明”、“操作”等字段。
    *   **3.2 数据模型**: 明确指出货物类型对应的数据模型是 `pd_base` 数据库中的 `pd_goods_type` 表。并展示了该表的结构，包括字段名、类型、长度、小数位数、是否允许为空等信息。
    *   **3.3 导入实体类**: 展示了Java实体类 `GoodsType` 的代码，包含 `@TableName`、`@TableId`、`@TableField` 等MyBatis-Plus注解，以及 `name`、`default_weight`、`default_volume`、`remark`、`status` 等属性。

*   **图表**:
    *   **产品原型图**: 一个包含“货品类型名称”、“品牌编码”、“默认重量”、“默认体积”、“说明”、“操作”等字段的表格。
    *   **数据库表结构图**: 一个包含“字段名”、“类型”、“长度”、“小数位数”、“是否允许为空”等列的表格。

*   **代码**:
    *   **Java实体类代码**:
        ```java
        package com.itehima.pinda.entity.base;

        import java.io.Serializable;
        import java.math.BigDecimal;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.TableName;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com.baomidou.mybatisplus.annotation.IdType;
        import com.baomidou.mybatisplus.annotation.TableId;
        import com.baomidou.mybatisplus.annotation.TableField;
        import com
