# 35-智能调度服务（实现过程_订单分类_4） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来编写我们这个智能调度

刚才我们是写到了这个get end agency id这个方法

这个方法是需要在这个地方去调的

上面咱们这个代码已经写完了

这是构建我们这个什么呢

新订单对吧

然后在构建新订单的过程当中

我们需要来干什么呢

获取这个目的地机构

其实就是我们收件人所对应的那个网点

对吧

他这个id

而这个的话呢

我们是需要去计算获得的

也就是说在他下单的时候呢

我们并不知道具体他那个收件人那一方

对吧

那么所对应的那个网点到底是那个网点

所以我们在这个地方呢

就需要给他计算出来

那么怎么计算呢

整个这个计算的过程呢

其实还是比较繁琐的

所以我们在这儿啊

在真正写代码之前呢

需要先来梳理一下这个思路

然后呢

思路梳理完之后呢

我们再通过代码的方式

把它实验出来

那么首先呢

我们先来看啊

第一步呢

需要做个什么事呢

就是根据我们当前这个订单

当前订单来获得什么呢

获取这个收件人地址详细信息

详细信息

那可能有的同学就说了

在我们这是不是

这不已经传过来了一个订单吗

对吧

那订单里面应该有详细信息啊

咱们来看一下

确实啊

这里边是有这些数据啊

属性的

是有这些属性的

你看啊

这里边是不是有一个叫做

receiver address

收件人详细地址

但是这个地址的话呢

它可能留的并不是我们所认为的

就是包含什么省市区

有可能什么呢

有可能

它只是写的一个街道的名称

比如说它写的是这个建材城

建材城西路对吧

而

那个省市呢

这省市区这几集呢

我们是不是在

我们的页面上啊

是通过下拉框的方式

来选择出来的

那也就是说在我们这个数据库里面记录的

只是这些省份

城市

还有区线的ID

对吧

然后剩下的呢

这一段呢

这个address呢

其实对应的只是个建材城西路

比如说什么金燕龙对吧

金燕龙

办公楼

办公楼

好

那么

我们这个address可能只是这么一个效果

而最终呢

我希望获得的是什么呢

获得的

应该是

北京市

这个昌平区对吧

昌平区

然后再加上后边建材城西路

所以说呢我们当前

在这个订单表里面存的省市区呢

只是存的省市区的

区线的ID对吧

然后呢这个详细地址呢

可能存的只是后边这一段

所以说我们这个地方呢

就需要最终把它变成这种

带有省市区

这种效果

所以我们这个地方呢

这就是包含什么呢

包含我们这个省

市区

这些

例如是吧

例如我们

最终获得的应该是这么一个效果

那也就是说我们第一步呢需要根据我们当前这个订单对吧

来获取受建人详细地址信息

就类似于这样的包含省市区的

好

然后呢

这是第一步对吧

这是第一步

然后获得这个信息之后啊

我们就可以根据这个详细地址来调用什么呢

调用我们这个百度地图

调用百度地图

它的这个工具类对吧

工具类

然后呢

根据

根据我们上面的地址对吧

来获取对应的这个什么呢

经纬度

坐标

获取经纬度坐标

这是第二步

然后接下来应该是怎么做呢

接下来我们就需要来根据我们这个经纬度坐标啊

根据我们的经纬度

坐标来获取什么呢

来获取

这个对应的这个曲线

曲线

然后检查什么呢

检查我们通过百度地图

地图获取的

获取的这个区域

是否和什么呢

和我们这个下单时

干什么呢

这个选择的

选择的区域

是否一致

是否一致

那么如果不一致的话呢

那就说明这个地址是有问题的

那么后边是没法正常处理

一般情况下呢

如果你正常

正规选择的话呢

一般都能对应上

所以我们在这个地方呢也是需要

通过百度地图

对吧他给我们提供的API

来

检查一下这个区限

对吧到底是哪个比如是朝阳区对吧

然后呢

你这个下单的时候选择的是否是朝阳区

那么我们在这呢需要来检查一下

需要在这来

核对一下对吧

那么如果核对通过之后呢

核对通过之后啊是不是就需要来干什么呢

查询我们当前这个

区线

这一级

下的这个所有网点

那么这个范围呢一般就是

锁定到区线这一级就可以

比如说如果是在北京这个范围之内对吧

那么有可能我们

锁定的这个区线呢就是朝阳区或者昌明区或者海淀区对吧

那么

把这个区下边所有的网点给他查出来

然后查出来之后再干什么呢

在计算我们

这个

当前就是

当前

区域

下

区域下

所有

网点

距离什么呢

距离这个收件人对吧

地址

最近的

最近的网点

距离最近的

这就是我们想要的

所以大家可以看到我们整个

计算的这个过程啊其实还是比较繁琐的

主要呢是

需要有这么

五个

关键的步骤

最终才能把它算出来

这是我们先把这个思路呢

整体来梳理一下

然后一会儿呢我们就需要通过代码的方式呢

把它实现出来

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中订单服务模块的代码实现过程。核心内容是通过 `TaskOrderClassifyServiceImpl` 类中的 `buildNewOrder` 方法，将一个订单列表（`orderList`）转换为一个包含订单分类信息的 DTO 列表（`orderClassifyDTOList`）。该转换过程使用了 `OrderClassifyDTO` 的 Builder 模式和 Java 8 的 Stream API。视频重点演示了如何从订单对象中提取“起始机构”和“目的机构”（网点 ID），并最终构建出一个结构化的订单分类数据。同时，视频也展示了 `Order` 实体类的结构，以及一个名为 `getEndAgencyId` 的辅助方法，该方法旨在根据订单的收货地址信息，通过调用百度地图 API 来查找并返回最接近的网点 ID，但当前代码中该方法仅返回 `null`，表明其功能尚未实现。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 1: 订单分类服务核心方法 `buildNewOrder` (约 0:00 - 0:15)**
    *   展示了 `TaskOrderClassifyServiceImpl` 类中的 `buildNewOrder` 方法。
    *   该方法接收一个 `agencyId`，创建 `OrderSearchDTO`，调用远程服务 `orderFeign` 获取订单列表。
    *   使用 `OrderClassifyDTO.OrderClassifyDTOBuilder` 构建器和 Stream API 对订单列表进行转换。

*   **章节 2: 订单分类 DTO 构建逻辑 (约 0:15 - 0:30)**
    *   详细展示了 `orderList.stream().map(...)` 的转换逻辑。
    *   通过 `builder.startAgencyId(...)` 和 `builder.endAgencyId(...)` 设置订单的起始和目的网点 ID。
    *   通过 `builder.orderType(...)` 设置订单类型。

*   **章节 3: 订单实体类 `Order` 结构 (约 0:30 - 0:45)**
    *   切换到 `Order.java` 文件，展示了 `Order` 实体类的结构。
    *   重点展示了 `orderType` 和 `pickupType` 字段，用于区分订单类型（同城/城际）和取件类型。

*   **章节 4: 收货地址相关字段 (约 0:45 - 0:55)**
    *   在 `Order.java` 中，展示了 `receiverProvinceId`, `receiverCityId`, `receiverCountyId`, `receiverAddress` 等收货地址相关的字段。

*   **章节 5: 辅助方法 `getEndAgencyId` 的设计与实现 (约 0:55 - 1:10)**
    *   展示了 `getEndAgencyId(Order item)` 方法。
    *   该方法的注释说明了其设计目标：根据收货地址信息，通过百度地图 API 查找并返回最接近的网点 ID。
    *   当前代码中该方法仅返回 `null`，表明其功能尚未实现。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1: `buildNewOrder` 方法**
    ```java
    private List<OrderClassifyDTO> buildNewOrder(String agencyId) {
        OrderSearchDTO orderSearchDTO = new OrderSearchDTO();
        orderSearchDTO.setStatus(OrderStatus.OUTLETS_WAREHOUSE.getCode());
        orderSearchDTO.setCurrentAgencyId(agencyId);
        // 调用远程服务获取订单列表
        List<Order> orderList = orderFeign.list(orderSearchDTO);
        log.info("查询到新订单个数: {}", orderList.size());
        OrderClassifyDTO.OrderClassifyDTOBuilder builder = OrderClassifyDTO.builder();
        builder.currentAgencyId(agencyId);
        List<OrderClassifyDTO> orderClassifyDTOList = orderList.stream().map(item -> {
            builder.order(item); // 原始订单
            builder.startAgencyId(agencyId); // 起始机构
            builder.endAgencyId(getEndAgencyId(item)); // 目的地机构（目的网点）
            builder.orderType(item.getOrderType()); // 订单类型
            return builder.build();
        }).collect(Collectors.toList());
        return orderClassifyDTOList;
    }
    ```

*   **关键代码片段 2: `getEndAgencyId` 方法（注释）**
    ```java
    /**
     * 获取目的网点id
     * @param item
     * @return
     */
    private String getEndAgencyId(Order item) {
        // 根据当前订单获取收件人地址详细信息，包含省市区，例如：北京市昌平区建材城西路金燕龙办公楼
        // 调用百度地图工具，根据地址获取对应的经纬度坐标
        // 根据经纬度坐标获取对应的区县检查通过百度地图获取的区域是否和下单时选择的区域一致
        // 查询当前区县下的所有网点
        // 计算当前区县下所有网点距离收件人地址最近的网点
        return null;
    }
    ```

*   **关键代码片段 3: `Order` 实体类字段**
    ```java
    private Integer orderType; // 订单类型，1为同城订单，2为城际订单
    private Integer pickupType; // 取件类型，1为同城订单，2为城际订单
    private String receiverProvinceId; // 收件人省份id
    private String receiverCityId; // 收件人城市id
    private String receiverCountyId; // 收件人区县id
    private String receiverAddress; // 收件人详细地址
    private String receiverAddressId; // 收件人地址id
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 订单分类服务的构建过程**
    *   讲师在 IDE 中定位到 `TaskOrderClassifyServiceImpl` 类。
    *   通过鼠标悬停和高亮，演示了 `buildNewOrder` 方法的逻辑。
    *   重点演示了 `orderList.stream().map(...)` 中的 `builder.endAgencyId(getEndAgencyId(item))` 语句，说明了如何获取目的网点 ID。

*   **场景 2: 订单实体类的结构分析**
    *   讲师切换到 `Order.java` 文件。
    *   通过滚动和高亮，展示了 `orderType` 和 `pickupType` 字段，解释了它们在订单分类中的作用。
    *   展示了 `receiverProvinceId`, `receiverCityId`, `receiverCountyId`, `receiverAddress` 等字段，说明了收货地址信息的存储结构。

*   **场景 3: `getEndAgencyId` 方法的设计意图**
    *   讲师在 `TaskOrderClassifyServiceImpl` 中定位到 `getEndAgencyId` 方法。
    *   通过高亮和滚动，详细阅读了该方法的注释。
    *   通过注释内容，解释了该方法的设计目标：通过百度地图 API，根据收货地址信息，查找并返回最接近的网点 ID。
    *   最后，讲师指出当前代码中该方法仅返回 `null`，暗示其功能尚未实现，需要后续开发。
