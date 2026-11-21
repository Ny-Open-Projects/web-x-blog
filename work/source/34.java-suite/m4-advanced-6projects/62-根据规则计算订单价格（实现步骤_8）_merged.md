# 62-根据规则计算订单价格（实现步骤_8） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才咱们service里边计算订单价格这个方法已经写完了

那接下来我们回到咱们的controller当中

打开我们这个controller

来找一下在这个地方

other controller

然后找到什么呢

找到我们这个save方法

大家可以看一下我们现在这个save方法

写的是最简单的一种形式

你看我们是不是传过来一个DTO

这DTO里面其实就是封装了我们订单相关的一些信息

当然并不全

然后它是直接把它拷贝一下

拷贝成这种other这种类型

因为我们这个service操作的是我们的实体类

而不是DTO

所以这个转换一下

转换成这种实体类这种类型

然后直接save

save完之后重新把它拷贝回来

然后把这个DTO是不是给返回

这是我们原先的这种做法

但是这里边有一个关键的

就是我们这个订单价格没有去计算

所以我们在这就需要来

来完善一下

就是在我们真正save之前

需要来调用我们这个service

它的这个计算的方法

大家来看一下

我们在这呢

直接来调用一下

咱们这是不是有个叫做order service

然后呢

我们刚才是不是编写的就是这个calculate amount

计算这个订单价格

然后呢

把我们这个什么呢

order DTO是不是给传进去就可以了

好

好

好

好

好

好

好

好

好

好

好

,然后呢

它是不是就会给我们返回一个map

对吧

返回一个map

而这个map里边封装的呢

是不是就已经

如果能够正常解析的话

就能够把我们这个价格给我们算出来

好

但这套代码呢

我就不再去手敲了

咱们直接把这个拿过来就可以了

你看电用service

然后呢

计算订单价格

然后呢

从这里边呢

get它这个什么呢

DTO对吧

然后呢

重新拷贝一下

重新拷贝一下

拷贝到咱们那个order上面

然后来判断一下

如果有这个这个这个

message的话

是不是说明这个有问题

对吧

好

但是在这儿注意啊

我们这个前后呢

好像不太一致啊

上面写的是sender

对吧

嗯

所以

好

这个

后边这个呢

receiver这个

receiver

好

然后呢

我们整个把这块拿过来啊

然后呢

我们大概读一下这个代码就行了

这块呢

我们就不再手敲了

直接拿过来

嗯

然后呢

把这块覆盖一下

咱们来看一下啊

首先是new那个order

对吧

然后呢

我们调用这个service的这个calculate amount方法

对吧

然后呢

计算订单价格

然后返回值就是个map

这个map里边其实封装的是什么呢

你看我们刚才是怎么写的呀

我是不是如果正常解析的话呢

是不是一个是amount

还有一个是order dto

对吧

好

然后到这边来

你看

首先呢

我们是不是get这个order dto

对吧

先把它get出来

好

然后呢

这个地方如果能够get出来

然后呢

我们是不是就把它copy

copy之后呢

呃

先来判断一下是吧

如果有错误信息的话呢

后边就不用保存了

这就说明我们是不是在这个订单这个坐标计算

对吧

订单距离的时候呢

就其实就已经出错了

所以说这就直接返回了

如果说没有这个错误信息

就说明啊

能够计算成功

那这个时候呢

我们是不是在设置这个amount

设置这个amount

而这个amount的话呢

咱们是不是单独在map里边设置了一项

对吧

就刚才看到了这个amount

然后呢

把它get出来就可以了

get all default

这个其实就是什么呢

如果说啊

如果是有的话

有amount

amount这个key的话呢

直接获取

如果没有的话呢

就使用默认的20

这样就相对来说比较保险一点

对吧

然后呢

我们set完之后呢

这个价格是不是就设置上了

然后呢

直接在save

最终的返回就可以了

所以这块demo比较简单

重点的就是调用了我们这个计算的方法

这是咱们这个controller的这个save方法呢

就已经写好了

然后呢

我们下边其实还有一个方法呢

这个方法

这个方法呢

这个地方呢

在前端也会调用到

所以我们在这儿呢

计算一下

直接把这个map返回

前端自己去解析这个map就可以

所以把这一句打开就可以

好

那么关于咱们这个controller呢

其实就已经完善好了

一会儿呢

我们可以来测试一下

看看我们这个规则呢

能不能触发

对吧

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段来自一个关于“品达物流TMS系统”开发的实战教程，主要聚焦于订单服务模块中“规则引擎”功能的实现。讲师通过 IntelliJ IDEA 开发环境，演示了如何在订单创建流程中，调用规则引擎（Drools）来计算订单价格，并处理地址校验失败的异常情况。核心内容包括：在 `OrderController` 中调用 `OrderService` 的 `calculateAmount` 方法；该方法内部调用规则引擎进行计算；在计算前，先检查地址信息是否有效，若无效则直接返回错误订单；计算成功后，将结果设置到订单对象并保存。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示 `OrderService` 类中的 `calculateAmount` 方法，该方法用于计算订单金额。
*   **00:00:05 - 00:00:15**: 在 `OrderController` 中，讲师将 `orderService.calculateAmount(orderDTO)` 的返回值赋给一个 `Map` 变量 `map`，用于存储计算结果。
*   **00:00:15 - 00:00:25**: 讲师将 `map` 中的 `orderDto` 和 `amount` 字段提取出来，用于后续处理。
*   **00:00:25 - 00:00:35**: 讲师添加了地址校验逻辑，如果 `senderAddress` 或 `receiverAddress` 为空或包含错误信息，则直接返回 `orderDTO`。
*   **00:00:35 - 00:00:45**: 讲师将计算出的金额设置到 `order` 对象中，并调用 `orderService.saveOrder(order)` 保存订单。
*   **00:00:45 - 00:00:55**: 讲师创建一个新的 `OrderDTO` 对象 `result`，并使用 `BeanUtils.copyProperties` 将 `order` 的属性复制到 `result` 中。
*   **00:00:55 - 00:01:05**: 讲师返回 `result`，完成订单创建和价格计算的整个流程。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

*   **标题**: “品达物流TMS项目”
*   **大纲**:
    *   第4章 订单中心服务开发 (pdm-oms)
    *   4.1 订单中心服务数据模型
    *   4.2 订单需求和产品原型
    *   4.3 订单中心服务代码
    *   4.4 订单中心服务平台
    *   4.5 基于百度地图计算订单距离
    *   4.6 规则引擎Drools
    *   4.7 规则引擎计算订单价格
    *   4.8 实现动态规则

#### 代码关键内容

*   **`OrderController.java` 中的 `save` 方法**:
    ```java
    @PostMapping("/")
    public OrderDTO save(@RequestBody OrderDTO orderDTO, HttpServletResponse res) {
        Order order = new Order();
        // 计算订单价格
        Map map = orderService.calculateAmount(orderDTO);
        orderDTO = (OrderDTO) map.get("orderDto");
        // 地址校验
        if ("sender error msg".equals(orderDTO.getSenderAddress()) || "receiver error msg".equals(orderDTO.getReceiverAddress())) {
            return orderDTO;
        }
        // 设置订单金额
        order.setAmount(new BigDecimal(map.getOrDefault("amount", "20").toString()));
        orderService.saveOrder(order);
        OrderDTO result = new OrderDTO();
        BeanUtils.copyProperties(order, result);
        return result;
    }
    ```

*   **`OrderService.java` 中的 `calculateAmount` 方法**:
    ```java
    public OrderDTO calculateAmount(OrderDTO orderDTO) {
        // 调用百度地图服务接口获取寄件人地址对应的坐标经纬度
        String begin = BaiduMapUtils.getCoordinate(orderDTO.getSenderAddress());
        if (begin == null) {
            orderDTO.setSenderAddress("sender error msg");
            return orderDTO;
        }
        // 调用百度地图服务接口获取收件人地址对应的坐标经纬度
        String end = BaiduMapUtils.getCoordinate(orderDTO.getReceiverAddress());
        if (end == null) {
            orderDTO.setReceiverAddress("receiver error msg");
            return orderDTO;
        }
        // 计算距离
        Double distance = BaiduMapUtils.getDistance(begin, end);
        DecimalFormat decimalFormat = new DecimalFormat("#.##");
        String distanceStr = decimalFormat.format(distance / 1000);
        orderDTO.setDistance(new BigDecimal(distanceStr));
        return orderDTO;
    }
    ```

*   **规则引擎代码片段**:
    ```java
    // 在规则引擎中，计算订单价格的逻辑
    // 伪代码示例：
    // if (orderDTO.getSenderAddress() == null || orderDTO.getReceiverAddress() == null) {
    //     return orderDTO;
    // }
    // Double distance = calculateDistance(orderDTO.getSenderAddress(), orderDTO.getReceiverAddress());
    // BigDecimal amount = calculateAmount(distance, orderDTO.getOrderCargoDto().getTotalWeight());
    // orderDTO.setAmount(amount);
    // return orderDTO;
    ```

---

### 4) 关键场景与演示描述

*   **场景一：订单创建与价格计算流程**
    *   **描述**: 讲师在 `OrderController` 中编写 `save` 方法，该方法接收一个 `OrderDTO` 对象。首先，它调用 `orderService.calculateAmount(orderDTO)` 方法来计算订单价格。该方法会调用百度地图API获取寄件人和收件人的坐标，并计算距离，最终返回一个包含订单信息和价格的 `Map`。
    *   **演示**: 讲师在IDE中逐行编写代码，并使用 `BeanUtils.copyProperties` 将 `orderDTO` 的属性复制到 `order` 对象中，然后调用 `orderService.saveOrder(order)` 保存订单。

*   **场景二：地址校验与异常处理**
    *   **描述**: 在计算价格之前，讲师添加了地址校验逻辑。如果 `orderDTO` 中的 `senderAddress` 或 `receiverAddress` 字段为空或包含错误信息（如 "sender error msg"），则直接返回 `orderDTO`，不进行后续的计算和保存。
    *   **演示**: 讲师在 `OrderController` 中添加了一个 `if` 判断语句，并在条件成立时直接 `return orderDTO`。

*   **场景三：规则引擎的调用与结果处理**
    *   **描述**: `calculateAmount` 方法内部调用了规则引擎（Drools）来计算订单价格。规则引擎根据订单的重量、距离等信息，计算出最终的价格，并将结果存储在 `Map` 中。
    *   **演示**: 讲师在 `OrderService` 中编写了 `calculateAmount` 方法，并在其中调用了 `BaiduMapUtils` 类来获取坐标和计算距离。最终，将计算出的价格设置到 `orderDTO` 对象中并返回。

*   **场景四：订单保存与返回**
    *   **描述**: 在地址校验通过且价格计算完成后，讲师将计算出的金额设置到 `order` 对象中，并调用 `orderService.saveOrder(order)` 保存订单。然后，创建一个新的 `OrderDTO` 对象 `result`，并将 `order` 的属性复制到 `result` 中，最后返回 `result`。
    *   **演示**: 讲师在 `OrderController` 中编写了 `order.setAmount(...)` 和 `orderService.saveOrder(order)` 代码，并在最后创建了 `OrderDTO result` 对象并返回。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
