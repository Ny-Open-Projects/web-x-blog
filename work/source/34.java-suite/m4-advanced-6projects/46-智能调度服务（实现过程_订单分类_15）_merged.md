# 46-智能调度服务（实现过程_订单分类_15） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们就需要来编写这个方法了,就是build transfer order,这个就是查询我们这个中转订单,那么需要注意我们的查询条件是agency id,也就是说我们当前这个机构下边,它的这个中转订单,我们并不是查询所有的中转订单,对吧,我们只关心我们当前这个转运中心或者是网点,下边的这个中转订单,好,

好,那么查询的这个过程啊,其实跟我们前面已经实现的这个什么呢,查询新订单这个过程是非常类似的,只不过就是什么呢,查询的这个订单的状态不一样,所以说呢,我们这一段呢,就不再去一句一句手敲了,怎么办呢,咱们把这个新订单这个代码呢,把它复制过来,然后呢,进行一个相应的修改就可以了,好,那么你看我把它复制一下,整个复制,然后呢,

放到我们当前这个build transfer order这边来,然后呢,进行一个相应的修改,你看啊,我们现在呢,是不是要查询的这个是什么呢,状态是中转的啊,那么也就是说,应该是这种运输中,状态是这种的,好,所以说呢,我们这个地方呢,就可以把这个状态呢,给它改一下,应该是这个状态为什么呢,叫做运输中,好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

然后呢这个set current agency id呢

这个用改吗

其实不用改对吧

因为这个订单呢

只要是在我们这个地方的话呢

也就是current当前的机构id

也就是说明我们要查询的是

属于我们当前这个机构下面的订单

所以这个条件呢是不用改的

然后呢这个调用这个不用改

这个地方呢是不是又进行这个转换对吧

把原先这个list的机构进行便利

便利过程当中构建成这么一个DTO对象

最终呢把它封装成一个list的机核

然后呢这里边呢是需要进行相应的修改的

就是什么呢

你看这个起始机构

这个这个标通过调用这个builder对吧

来构建什么呢

我们这个start agency id

你看啊因为这个代码呢

是从我们前面那个新订单这边考过来的

如果作为新订单的话呢

当前机构是不是就是它的起始机构

但是如果是中转订单的话

当前机构呢

肯定就不是它的这个

什么呢

起始机构了

所以我们这个地方呢

还需要再来扩展一个方法

就是什么呢

就是来获得它的起始机构

目的机构呢

还调用我们原先这个方法

肯定是没有问题的

对吧

所以说呢

我们这个地方呢

需要再来扩展出来一个方法

叫做什么呢

叫做get start agency id

get start

起始机构

对吧

id

然后呢

同样我们可以把这个item呢

给传进来

对吧

那这样的话呢

我们这个地方是不是就又少一个方法

需要把这个方法呢来扩展出来

这就是获得我们这个起始机构

根据订单

订单来获得我们这个起始机构

id吧

因为我们最终只要一个id就可以

所以现在呢

你看我们这个方法呢

就已经写好了

对吧

就是照着我们原先写的那个构建新订单

稍微改造一下就可以

改造成本还是非常非常重要的

那现在呢

就又出来了一个新的方法

叫做get start agency id

这就是获得我们这个起始机构

而这个如何获得起始机构呢

咱们呢

是不是就可以再来仿照一下什么呢

我们当时获得这个end agency id

这个过程

跟它呢

也是有点类似的

所以一会儿呢

我们重点就来编写这个方法

就是获得我们这个起始机构的

先给它来一个return now

然后呢

保证它不报错

好

那么一会儿呢

我们重点就来写这个方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一段关于 Java 后端开发的实战教学片段，主要演示了如何在订单管理系统中，根据订单状态和机构信息，构建一个用于展示或传输的订单分类数据对象（DTO）。讲师通过 IntelliJ IDEA 开发环境，逐步讲解了如何使用 `Stream` API 和 `Builder` 模式来处理订单数据。视频重点展示了如何查询不同状态的订单（如“网点入库”、“运输中”），并将其转换为结构化的 `OrderClassifyDTO` 列表。同时，也涉及了如何从订单对象中提取起始和目的机构 ID，以及在获取地址信息时进行校验的逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示 `TaskOrderClassifyServiceImpl.java` 文件，定位到 `buildTransferOrder` 方法，该方法目前仅返回 `null`，用于演示后续的业务逻辑。
*   **00:00:05 - 00:00:15**: 讲师将光标移动到 `buildNewOrder` 方法，解释其功能是查询“网点入库”状态的订单。
*   **00:00:15 - 00:00:25**: 展示 `OrderStatus` 枚举类，重点讲解 `OUTLETS_WAREHOUSE` 状态的定义。
*   **00:00:25 - 00:00:35**: 讲师在 `buildNewOrder` 方法中，使用 `Stream` API 对查询到的订单列表进行转换，通过 `OrderClassifyDTO.Builder` 构建新的 DTO 对象。
*   **00:00:35 - 00:00:45**: 展示 `OrderClassifyDTO` 的 `Builder` 模式，逐行讲解如何设置 `orderType`、`startAgencyId` 和 `endAgencyId`。
*   **00:00:45 - 00:00:55**: 讲师将 `buildNewOrder` 方法中的订单状态修改为 `IN_TRANSIT`，用于演示查询“运输中”的订单。
*   **00:00:55 - 00:01:05**: 展示 `getStartAgencyId` 方法，该方法用于从订单对象中提取起始机构 ID。
*   **00:01:05 - 00:01:15**: 讲师将光标移动到 `getEndAgencyId` 方法，该方法用于从订单对象中提取目的机构 ID。
*   **00:01:15 - 00:01:25**: 展示 `getEndAgencyId` 方法的实现逻辑，包括调用 `EntCoordsSyncJob` 工具类获取经纬度坐标，并对地址和坐标进行校验。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1 (OrderStatus 枚举)**:
    ```java
    OUTLETS_WAREHOUSE(23003, "OUTLETS_WAREHOUSE"),
    ```

*   **关键代码片段 2 (buildNewOrder 方法)**:
    ```java
    orderSearchDTO.setStatus(OrderStatus.OUTLETS_WAREHOUSE.getCode());
    orderSearchDTO.setCurrentAgencyId(agencyId);
    List<Order> orderList = orderFeign.list(orderSearchDTO);
    Log.info("查询到新订单个数: {}", orderList.size());

    OrderClassifyDTO.OrderClassifyDTOBuilder builder = OrderClassifyDTO.builder();
    builder.currentAgencyId(agencyId);
    List<OrderClassifyDTO> orderClassifyDTOList = orderList.stream().map(item -> {
        builder.order(item); // 原始订单
        builder.startAgencyId(getStartAgencyId(item)); // 起始机构
        builder.endAgencyId(getEndAgencyId(item)); // 目的地机构
        builder.orderType(item.getOrderType());
        return builder.build();
    }).collect(Collectors.toList());
    ```

*   **关键代码片段 3 (getEndAgencyId 方法)**:
    ```java
    String location = EntCoordsSyncJob.getCoordinate(address);
    if (StringUtils.isBlank(location)) {
        exceptionHappend("收件人地址不正确");
    }
    ```

*   **关键代码片段 4 (buildTransferOrder 方法)**:
    ```java
    orderSearchDTO.setStatus(OrderStatus.IN_TRANSIT.getCode());
    orderSearchDTO.setCurrentAgencyId(agencyId);
    List<Order> orderList = orderFeign.list(orderSearchDTO);
    Log.info("查询到新订单个数: {}", orderList.size());

    OrderClassifyDTO.OrderClassifyDTOBuilder builder = OrderClassifyDTO.builder();
    builder.currentAgencyId(agencyId);
    List<OrderClassifyDTO> orderClassifyDTOList = orderList.stream().map(item -> {
        builder.order(item); // 原始订单
        builder.startAgencyId(getStartAgencyId(item)); // 起始机构
        builder.endAgencyId(getEndAgencyId(item)); // 目的地机构
        builder.orderType(item.getOrderType());
        return builder.build();
    }).collect(Collectors.toList());
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 查询“网点入库”订单**:
    讲师在 `buildNewOrder` 方法中，通过设置 `OrderStatus.OUTLETS_WAREHOUSE` 来查询状态为“网点入库”的订单。演示了如何使用 `orderFeign.list` 远程调用接口获取订单列表，并通过 `Stream` API 对列表进行转换。

*   **场景 2: 使用 Builder 模式构建 DTO**:
    讲师详细演示了如何使用 `OrderClassifyDTO.OrderClassifyDTOBuilder` 来构建对象。通过 `map` 方法，对每个订单对象进行处理，依次设置 `orderType`、`startAgencyId` 和 `endAgencyId`，最后调用 `build()` 方法生成新的 `OrderClassifyDTO` 对象。

*   **场景 3: 查询“运输中”订单**:
    讲师将 `buildNewOrder` 方法中的订单状态修改为 `OrderStatus.IN_TRANSIT`，并演示了如何查询“运输中”的订单，其逻辑与查询“网点入库”订单类似。

*   **场景 4: 提取机构 ID**:
    讲师展示了 `getStartAgencyId` 和 `getEndAgencyId` 方法，用于从订单对象中提取起始和目的机构 ID。在 `getEndAgencyId` 方法中，演示了如何调用 `EntCoordsSyncJob` 工具类获取经纬度坐标，并对地址和坐标进行校验，以确保数据的准确性。

*   **场景 5: 代码重构与注释**:
    讲师在 `buildTransferOrder` 方法中，通过注释和代码修改，演示了如何将业务逻辑从“网点入库”扩展到“运输中”，并保持代码的可读性和可维护性。
