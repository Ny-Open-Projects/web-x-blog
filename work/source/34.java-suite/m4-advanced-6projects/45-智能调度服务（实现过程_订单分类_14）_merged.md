# 45-智能调度服务（实现过程_订单分类_14） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢咱们是测试了一下我们这个calculate这个方法,对吧,那么测试完成之后啊,我们就可以把上面这个地方呢给补全一下了,注意这个地方这是哪呢,这是咱们这个get end agency id,对吧,获得我们这个目的地网点id,刚才呢我们这个方法测完了,说明没有问题,那么没有问题的话呢,我们就可以从这个result结果里边呢来get,

然后这个key的话呢,咱们当时放的时候是不是agency id,所以取的时候呢也是按照它来取就可以了,好,然后给它强转一下就可以了,转成死尊例行,好,那这块呢我们就整个这个方法呢就已经完成了,然后呢这个地方呢我们一共写的方法呢其实还是比较多的,咱们再来梳理一下,你看我们这些私有的方法,

那么整个它这个过程,

调用过程是什么样子的呢,咱们来看,首先呢我们在这呢是不是要进行这个订单分类,对吧,要进行订单分类,那么我们在这呢是不是就会去new了这么一个对象,然后在这里边把我们所有的这种新订单是不是给它放到这个集合里边去,所以这个新订单如何获得呢,我们当时是不是创建了这么一个方法,叫做build new order这个方法,对吧,这样的话呢它就调到了我们这个方法,然后在这个方法里边我们是不是来进行查询,

把这个新订单查上来,查上来之后啊,咱们因为返回结果呢,需要封装成这种DTO这种类型,所以在这个地方呢是不是又做了一个封装,对吧,做了一个封装,那么把它转成了这种形式,当然在转的过程当中啊,有一个地方,有一个数据需要我们去获取,就是什么呢,目的地机构,因为这个呢在我们当时下单的时候呢并不知道它这个目的地网点是哪一个,

所以呢我们在这个地方呢就又扩展出来了这么一个方法,叫做get end agency ID,对吧,把这个原始的订单对象传进去,在这里面呢来进行计算,把这个目的地机构呢给它获取出来,所以这样的话呢我们是不是就又扩展了这么一个方法,get end agency ID,好,

然后在这里边呢咱们是不是先把这个详细信息,对吧,整个给它拼出来,拼成类似于这样的,

那么这个拼接的过程呢我们是又创建了这么一个方法,叫做receiver full address,对吧,好,然后呢把这个地址拼出来之后呢,咱们是不是就调用了百度地图,然后呢获取它的经纬度坐标,对吧,然后这一块呢是不是再来进行这个什么呢,进行对比,对吧,

这个呢这是中间是转成一个map,然后呢再获得它的ad code,根据ad code呢再调用我们的这个API,对吧,FAN接口,然后呢把这个区域对象获取出来,

然后呢我们在这块呢是不是来进行这个对比,好,应该是在这儿,在这儿来进行对比,好,如果能对比上,说明区域数据没问题,然后呢我们是不是再来获取当前这个区线下边所有的网点,当然这儿呢也是调用的FAN接口,好,然后呢这个地方呢我们是不是也开始计算,对吧,这就是刚才我们测试的这个方法,把我们查询到的这些网点以及目的地机构的这个坐标,然后传过来,然后在这儿来进行计算,算完之后呢,把这个,

这个机构的ID给我们返回就可以了,好,这是到目前为止,我们这个已经实现了,已经实现了这个逻辑,我们再来梳理一遍,然后呢我们这块呢相当于这块就已经写完了,对吧,构建新订单才写完,然后呢再往下呢就是什么呢,还有一个中转的订单是不是也需要加到这个集合里面去,所以再往下呢我们就需要再来调这么一个方法,

然后呢扩展另外一个叫做build什么呢,transfer order,好,transfer order,这个就是什么呢,构建我们的这个中转订单,中转订单,好,然后呢这个返回值的话也用不了这么麻烦,咱们直接把这改成一个什么呢,list集合就可以,然后呢同样也是封成成这种DTO对象,好,这个是查询我们的中转,

中转订单,好,所以一会儿呢我们就要来重点来写这个build transfer order这个方法,

OK,所以整体这个代码的结构啊,这个execute方法其实是我们的主线对不对,是我们的主线,只不过在这个主线执行过程当中啊,有很多细节,而这些细节呢实验起来比较复杂,所以我们又封装成了一个一个的方法,对吧,这样最终呢我们可以看到扩展出来的方法,

就会越来越多,但是呢我们最好还是按照这个主线的思路去走,好,那么一会儿呢我们就来编写这个方法,就是构建我们的中转订单,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程聚焦于一个订单分类服务的实现，主要讲解了如何根据订单的收件人地址信息，通过调用百度地图API获取经纬度坐标，进而查询该地址所属的行政区划（区县），并最终在该区域内查找距离收件人最近的网点（机构）来完成订单的分类。核心代码位于 `TaskOrderClassifyServiceImpl.java` 文件中，演示了如何将订单数据流式处理、构建查询条件、调用外部服务、处理异常以及返回分类结果。整个过程体现了典型的“领域驱动设计”中的服务层逻辑，结合了地理信息（GIS）服务和业务规则。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 1: 服务入口与订单分类逻辑 (00:00 - 00:15)**
    *   展示了 `execute` 方法的主入口，接收 `agencyId`, `jobId`, `logId` 三个参数。
    *   初始化两个 `List` 用于存储新订单和中转订单。
    *   调用 `buildNewOrder` 方法获取新订单数据。

*   **章节 2: 新订单构建与查询 (00:15 - 00:30)**
    *   详细讲解 `buildNewOrder` 方法。
    *   创建 `OrderSearchDTO` 对象，设置订单状态为 `OUTLETS_WAREHOUSE`（网点或仓库）。
    *   调用 `orderFeign.list` 方法查询符合条件的订单列表。
    *   使用 `OrderClassifyDTOBuilder` 构建并收集 `OrderClassifyDTO` 对象。

*   **章节 3: 地址解析与区域查询 (00:30 - 00:45)**
    *   展示了 `EntCoordSyncJob.getCoordinate(address)` 方法，用于将地址转换为经纬度坐标。
    *   对坐标进行校验，若为空则抛出异常。
    *   调用 `EntCoordSyncJob.getLocationByPosition(location)` 获取区域信息。
    *   通过 `areaApi.getByCode` 方法，根据区域编码查询系统中的区域数据。

*   **章节 4: 网点查找与结果计算 (00:45 - 01:00)**
    *   调用 `agencyScopeFeign.findAllAgencyScope(area.getAreaId())` 获取当前区域下的所有网点。
    *   对网点列表进行校验，若为空则抛出异常。
    *   调用 `calculate` 方法，传入网点列表和收件人坐标，计算出距离最近的网点。
    *   最终返回 `result.get("agencyId")` 作为分类结果。

*   **章节 5: 异常处理与返回 (01:00 - 01:15)**
    *   展示了 `exceptionHappend` 方法，用于统一抛出异常信息。
    *   代码中使用了 `try-catch` 块来捕获并处理异常。
    *   最终将分类结果（`orderClassifyGroupDTOs`）返回给调用方。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段：**

    *   **订单分类服务入口：**
        ```java
        public List<OrderClassifyGroupDTO> execute(String agencyId, String jobId, String logId) {
            List<OrderClassifyDTO> orderClassifyDTOS = new ArrayList<>();
            List<OrderClassifyGroupDTO> orderClassifyGroupDTOS = new ArrayList<>();
            orderClassifyDTOS.addAll(buildNewOrder(agencyId));
            // 进行订单分类
            // 将分类结果保存到数据库
            return orderClassifyGroupDTOS;
        }
        ```

    *   **新订单构建：**
        ```java
        private List<OrderClassifyDTO> buildNewOrder(String agencyId) {
            OrderSearchDTO orderSearchDTO = new OrderSearchDTO();
            orderSearchDTO.setStatus(OrderStatus.OUTLETS_WAREHOUSE.getCode());
            orderSearchDTO.setCurrentAgencyId(agencyId);
            List<Order> orderList = orderFeign.list(orderSearchDTO);
            OrderClassifyDTO.OrderClassifyDTOBuilder builder = OrderClassifyDTO.builder();
            List<OrderClassifyDTO> orderClassifyDTOList = orderList.stream().map(item -> {
                builder.order(item); // 原始订单
                builder.startAgencyId(agencyId); // 起始机构
                builder.endAgencyId(getEndAgencyId(item)); // 目的机构
                builder.orderType(item.getOrderType()); // 订单类型
                return builder.build();
            }).collect(Collectors.toList());
            return orderClassifyDTOList;
        }
        ```

    *   **地址解析与区域查询：**
        ```java
        String location = EntCoordSyncJob.getCoordinate(address);
        if (StringUtils.isBlank(location)) {
            exceptionHappend("收件人地址不正确");
        }
        Map map = EntCoordSyncJob.getLocationByPosition(location);
        if (ObjectUtils.isEmpty(map)) {
            exceptionHappend("根据经纬度获取区域信息为空");
        }
        String adcode = (String) map.get("adcode");
        R<Area> areaR = areaApi.getByCode(adcode + "000000");
        Area area = areaR.getData();
        if (area == null) {
            exceptionHappend("没有查询到区域数据");
        }
        ```

    *   **网点查找与距离计算：**
        ```java
        List<AgencyScopeDTO> agencyScope = agencyScopeFeign.findAllAgencyScope(area.getAreaId()).toString();
        if (agencyScope == null || agencyScope.size() == 0) {
            exceptionHappend("无法获取收件人所在网点信息");
        }
        Result result = calculate(agencyScope, location);
        return result.get("agencyId");
        ```

    *   **距离计算核心逻辑：**
        ```java
        private Result calculate(List<AgencyScopeDTO> agencyList, String location) {
            Map<String, Double> agencyMap = Maps.newHashMap();
            for (AgencyScopeDTO agencyScopeDto : agencyList) {
                for (List<Map> maps : agencyScopeDto.getMultiPoints()) {
                    String point = getPoint(map);
                    Double distance = EntCoordSyncJob.getDistance(point, location);
                    Double preDistance = (Double) agencyMap.get(agencyScopeDto.getAgencyId());
                    if (preDistance == null || distance < preDistance) {
                        agencyMap.put(agencyScopeDto.getAgencyId(), distance);
                    }
                }
            }
            List<Map.Entry<String, Double>> list = new ArrayList<>(agencyMap.entrySet());
            // 返回最近网点的ID
            return new Result(list.get(0).getKey());
        }
        ```

*   **关键注释：**

    *   `// 调用百度地图工具，根据地址获取对应的经纬度坐标`
    *   `// 根据经纬度坐标获取对应的区县检查百度地图获取的区域是否和下单时选择的区域一致`
    *   `// 计算当前区域下所有网点距离收件人地址最近的网点`
    *   `// 将分类结果保存到数据库`

---

### 4) 关键场景与演示描述

*   **场景 1: 订单分类服务的主流程演示 (00:00 - 00:15)**
    *   讲师在IDE中高亮显示 `execute` 方法，解释其作用是“存放当前机构下的订单”。
    *   通过代码注释 `// 获取当前机构下的所有订单数据(分为新订单和中转订单)`，说明了数据的来源和分类。
    *   展示了 `orderClassifyDTOS.addAll(buildNewOrder(agencyId));` 这一行代码，强调了新订单的构建是第一步。

*   **场景 2: 新订单构建与查询演示 (00:15 - 00:30)**
    *   讲师将光标移动到 `buildNewOrder` 方法，解释其功能是“查询中转订单”。
    *   通过代码 `orderSearchDTO.setStatus(OrderStatus.OUTLETS_WAREHOUSE.getCode());` 展示了如何设置订单状态。
    *   讲师强调了 `orderFeign.list(orderSearchDTO)` 这一行，说明了通过Feign客户端调用远程服务查询订单。

*   **场景 3: 地址解析与区域查询演示 (00:30 - 00:45)**
    *   讲师高亮了 `EntCoordSyncJob.getCoordinate(address)` 方法，解释其作用是“将地址转换为经纬度坐标”。
    *   展示了 `if (StringUtils.isBlank(location))` 的异常处理逻辑，强调了数据校验的重要性。
    *   讲师解释了 `areaApi.getByCode(adcode + "000000")` 的作用是“根据区域编码查询系统中的区域数据”。

*   **场景 4: 网点查找与距离计算演示 (00:45
