# 48-智能调度服务（实现过程_订单分类_17） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,刚才呢,咱们编写的这个get start agency id这个方法呢,就已经写完了。

由于我们刚才这个代码呢,其实是从原先的类似的代码复制过来的,对吧?

所以说我们刚才在这改造的时候呢,并没有改造全,比如说在这,咱们是不是复制了这么一个方法,叫做thunder full address,对吧?

这个地方呢,也是我们从原先的代码复制过来的,比如说这个地方都改成thunder,是吧?

然后还有一个地方呢,其实没有改造全,就是它在拼接的时候,这个地方,对吧?

order.get什么呢?应该是我们的thunder address,对吧?

所以这个地方呢,没有改造全,get thunder address。

好,所以我们需要注意啊,因为是从原先的代码复制过来,所以要检查仔细了。

刚才呢,我们这个地方是遗留了这么一个问题。

然后呢,我们回来。

回到刚才这边来。

然后呢,还有一个地方呢,也没有这个改造好啊,就是判断的这个地方,对吧?

在进行匹配的时候呢,就是我们这个error id跟我们这个订单里边所对应的这个什么呢?

是不是应该是thunder呀?

thunder at这个country id。

应该就是get thunder country id。

就这个。

因为还是啊,还是那句话,因为我们刚才这个是复制过来的啊,所以这个地方呢,没有改造好。

这块呢,是一样的啊,这个error是我们通过这种方式查出来了。

然后呢,其他的地方呢,都已经检查过了,应该是没什么问题。

好,这是对于我们刚才啊,复制过来这个代码呢,做了一个简单的修复。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中 `TaskOrderClassifyServiceImpl` 类的代码实现，核心功能是根据订单信息（特别是收件人地址）来确定最合适的派送网点。该过程涉及多个步骤：首先，获取并校验收件人详细地址；接着，调用百度地图 API 将地址转换为经纬度坐标；然后，通过经纬度查询百度地图的行政区划信息（如省、市、县）；最后，根据行政区划信息查询系统中该区域下的所有网点，并计算出距离收件人最近的网点 ID。整个过程体现了在分布式系统中，如何结合外部服务（如地图服务）和内部数据（如网点数据库）来完成业务逻辑。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节是根据代码逻辑和画面切换的自然分段进行的：

*   **章节 1: 获取并校验收件人地址 (0:00 - 0:05)**
    *   展示 `getStartAgencyId` 方法的入口。
    *   调用 `senderFullAddress` 方法获取完整的收件人地址。
    *   使用 `StringUtils.isBlank` 校验地址是否为空，若为空则抛出异常。

*   **章节 2: 构建并获取详细地址 (0:05 - 0:15)**
    *   展示 `senderFullAddress` 方法的实现。
    *   从订单对象中提取省、市、县的 ID。
    *   使用 `CompletableFuture` 异步调用 `areaMapFuture` 获取对应的行政区划名称。
    *   将省、市、县名称与订单中的收件人地址拼接成一个完整的字符串。

*   **章节 3: 地图坐标转换与区域校验 (0:15 - 0:25)**
    *   调用 `EntCoordSyncJob.getCoordinate` 方法将地址转换为经纬度。
    *   校验经纬度是否为空。
    *   使用 `EntCoordSyncJob.getLocationByPosition` 方法根据经纬度查询百度地图的行政区划信息（`Map`）。
    *   校验返回的 `Map` 是否为空。

*   **章节 4: 区域信息查询与一致性校验 (0:25 - 0:35)**
    *   从 `Map` 中提取 `adcode`（区域编码）。
    *   使用 `areaApi.getByCode` 查询系统中的区域信息。
    *   校验查询结果是否为空。
    *   校验订单中的发件地址区域 ID 是否与根据坐标计算出的区域 ID 一致。

*   **章节 5: 查询网点并计算最近网点 (0:35 - 0:45)**
    *   根据校验通过的区域 ID，查询该区域下的所有网点（`agencyScope`）。
    *   校验网点列表是否为空。
    *   调用 `calculate` 方法计算距离收件人最近的网点。
    *   返回最终的网点 ID。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段：**

    *   **方法签名：**
        ```java
        private String getStartAgencyId(Order order) {
        ```

    *   **地址拼接逻辑：**
        ```java
        StringBuffer stringBuffer = new StringBuffer();
        stringBuffer.append(provinceName).append(cityName).append(countyName).append(order.getReceiverAddress());
        return stringBuffer.toString();
        ```

    *   **地图坐标转换与区域查询：**
        ```java
        String location = EntCoordSyncJob.getCoordinate(address);
        Map map = EntCoordSyncJob.getLocationByPosition(location);
        String adcode = (String) map.get("adcode");
        R'Area' areaR = areaApi.getByCode(adcode + "000000");
        Area area = areaR.getData();
        ```

    *   **区域一致性校验：**
        ```java
        if (!order.getSenderCountyId().equals(area.getId())) {
            exceptionHappend(msg: "发件地址区域id和根据坐标计算出的区域不一致");
        }
        ```

    *   **网点查询与计算：**
        ```java
        List<AgencyScopeDto> agencyScope = agencyScopePeign.findAllAgencyScope(area.getId().toString(), agencyId: null, agencyId: null);
        if (agencyScope == null || agencyScope.size() == 0) {
            exceptionHappend(msg: "无法获取收件人所在网点信息");
        }
        Result result = calculate(agencyScope, location);
        return (String) result.get("agencyId");
        ```

*   **关键注释：**
    *   `// 根据当前订单获取发件人地址详细信息`
    *   `// 调用百度地图工具类，根据地址获取对应的经纬度坐标`
    *   `// 根据经纬度获取对应的区县检查通过百度地图获取的区域是否和下单时选择的区域一致`
    *   `// 根据adcode（区域编码）查询我们系统中的区域信息`
    *   `// 查看当前县区下的所有网点`
    *   `// 计算当前区域下所有网点距离收件人地址最近的网点`

---

### 4) 关键场景与演示描述

*   **场景 1: 地址校验与拼接**
    *   **描述：** 讲师首先展示了 `getStartAgencyId` 方法，强调其核心是获取收件人地址。接着，他将焦点移至 `senderFullAddress` 方法，演示了如何从订单对象中提取省、市、县的 ID，并使用 `CompletableFuture` 异步获取对应的行政区划名称。最后，他将这些名称与订单中的收件人地址拼接成一个完整的字符串，这一步是后续所有操作的基础。

*   **场景 2: 地图服务集成与校验**
    *   **描述：** 讲师演示了如何调用百度地图的 `getCoordinate` 方法将地址转换为经纬度，并通过 `getLocationByPosition` 方法获取对应的行政区划信息。他特别强调了对返回结果的校验，包括检查经纬度是否为空、返回的 `Map` 是否为空，以及从 `Map` 中提取 `adcode`。

*   **场景 3: 区域一致性与网点查询**
    *   **描述：** 讲师展示了如何使用 `areaApi.getByCode` 查询系统中的区域信息，并校验其有效性。接着，他演示了如何将订单中的发件地址区域 ID 与根据坐标计算出的区域 ID 进行对比，确保两者一致。如果一致，他将调用 `agencyScopePeign.findAllAgencyScope` 查询该区域下的所有网点，并最终调用 `calculate` 方法计算出距离收件人最近的网点 ID。

*   **场景 4: 异常处理**
    *   **描述：** 在每个关键步骤中，讲师都演示了如何使用 `exceptionHappend` 方法抛出异常。这些异常信息（如“收件人地址不能为空”、“发件地址区域id和根据坐标计算出的区域不一致”）是系统在业务逻辑出错时的反馈，有助于调试和维护。
