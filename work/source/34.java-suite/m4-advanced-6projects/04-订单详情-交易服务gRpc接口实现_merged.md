# 04-订单详情-交易服务gRpc接口实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就去实现交易服务的订单详情查询接口

首先去修改GRPC Stock Deal Service

回到工程当中

定位到GRPC Stock Deal Service

咱们要去重写获取订单详情的接口

在这里Edit Insert

Overlay Method

选择Get Order点击OK

咱们增加注释

这个是获取订单详情接口

这部分处理逻辑比较简单

咱们就直接从讲音当中将代码拖配进来

将方法内部的代码拖配进去

咱们看一下它整个的实现流程

首先去根据订单ID获取订单的详情信息

这个Service处理也是比较简单

我们可以进去看一下

它是根据订单ID

直接查询数据库

获取订单对象

好

再返回刚才的GRPC层接口

拿到订单对象之后

先做一个围攻判断

订单找到后

将获取的订单信息

拋批至返回的订单详情对象里面

注意

咱们在这里是排除了ExcuseTime这个属性

为什么要排除这个属性呢

咱们来看一下ExcuseTime的类型

在这里呢

在这里ExcuseTime是成交时间

它的类型是Data类型

我们Ctrl来看一下

它在Java YouTube包下面

那返回到刚才的GRPC接口层

因为Pro的Buffer

它是不支持Data的类型

但是PB可以支持基本的类型

比如说Int,Long,String等等

如果咱们一定要用日期类型

可以去采用Pro的Buffer的插件

可以去采用Pro的Buffer的插件

引用Google Pro的Buffer下面的Time Step的Proto脚本

这样就可以让Pro的Buffer支持Time Step类型

但是这样需要引入额外的插件会有些麻烦

那么在这里呢

咱们就直接做个转换

将日期类型直接转换为时间戳

那这个时间戳呢

它就是一个Long类型

这样Pro的Buffer它就能够接收支持

响应的订单详情信息

组装完成之后

就要将数据返回给调用方

通过Response of周围对象做相应的操作

这样呢

就是订单详情的整个处理流程

整个实现处理也是比较简单

那咱们回到讲义当中

这里还有需要注意的一个点

因为在这里咱们是侧重业务逻辑的讲解

并没有对接口加上严格的安全教验控制

但是如果是在生产环境上面

一定要防止伪造参数去跨账号查询数据

这里提供两种解决方案

第一种呢

就是对参数报文进行加密

也就是参数的报文内容

咱们可以通过非对称加密的方式

加密完成之后

然后通过被丢式进行编码

将它转换为字符串

再将字符串内容放入PB里面

进行接口的传输交换

这样即使第三方

先听到这些话话

先拿到传输的报文之后

让它没有密钥

这样也是无法知道咱们传输的具体内容

另外一种方案呢

就是对数据要去增加账号ID的权限判断

也就是在前面实现测单处理的时候

咱们增加了交易账号ID权限的判断处理

这个账号ID不能由客户端去随便传递

应该是由咱们的服务通过与客户的交互

去记录关联相应的信息

去记录关联的交易账号

就比如咱们交易账号ID的获取

是通过缓存信息

圈头通道和交易账号ID的关联缓存去获取的

好

提供这两种方案解决失误

大家可以自行去扩展实现

这一讲就是对交易服务

订单详情接口处理的实现

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是“交易平台”系列课程的第16天，主要讲解如何在基于 gRPC 的微服务架构中，实现一个“获取订单详情”的远程调用接口。讲师通过 IntelliJ IDEA 开发环境，逐步演示了在 `GrpcStockDealService` 服务中编写 `getOrder` 方法的完整过程，包括：
- 使用 Protobuf 生成的 Java 类。
- 通过 `StreamObserver` 处理异步流式响应。
- 从数据库查询订单数据并填充响应对象。
- 处理异常并返回错误信息。
- 最后，讲师补充了关于生产环境安全和 Protobuf 日期类型处理的注意事项。

整个过程旨在教授学生如何在实际项目中实现一个健壮、可维护的 gRPC 服务接口。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节划分是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: 视频开头，展示课程大纲和本节目标。讲师指出本节将实现“交易服务 gRpc 接口实现”。
*   **00:15 - 00:30**: 展示 `GrpcStockDealService` 的 `getOrder` 方法的 Java 代码框架，包括方法签名和 `StreamObserver` 的使用。
*   **00:30 - 00:45**: 讲师讲解如何在 `try` 块中根据请求中的 `orderId` 查询数据库，调用 `stockDealService.getOrder(...)` 方法。
*   **00:45 - 01:00**: 讲师演示如何使用 `BeanUtils.copyProperties` 方法将查询到的 `TradeOrder` 对象的属性复制到响应对象 `GetOrderResponse` 中，并设置执行时间。
*   **01:00 - 01:15**: 讲师讲解 `catch` 块的处理逻辑，区分业务异常和系统异常，并分别返回对应的错误响应。
*   **01:15 - 01:30**: 讲师演示如何通过 `responseObserver.onNext(response.build())` 和 `responseObserver.onCompleted()` 将最终结果发送给调用方。
*   **01:30 - 01:45**: 讲师切换到 PPT 页面，讲解生产环境的安全性问题，包括参数防伪和账号权限判断。
*   **01:45 - 02:00**: 讲师讲解 Protobuf 不支持 `Date` 类型的问题，并给出解决方案：使用 `google/protobuf/timestamp.proto`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：显示了“交易平台 - Day 16”的学习目标，包括“第1章 订单详情接口”和“第2章 仓位总览功能”。
*   **关键知识点**：
    *   接口逻辑实现比较简单，根据 ID 查询对应订单。
    *   生产上要防止伪造参数跨号查询数据，解决方案有两种：一种是参数报文加密，另一种是对数据增加账号 ID 权限判断。
    *   注意 Protobuf 不支持 Date 类型，可以用 `google.protobuf.Timestamp`，需要引入 `import "google/protobuf/timestamp.proto";`。

#### 代码关键内容

*   **服务接口定义**：
    ```java
    @Override
    public void getOrder(GetOrderRequest request, StreamObserver<GetOrderResponse> responseObserver) {
        log.info("Process in GrpcStockDealService.getOrder, request: " + request);
        GetOrderResponse.Builder response = GetOrderResponse.newBuilder();
        try {
            // 根据订单ID获取订单详情信息
            TradeOrder order = stockDealService.getOrder(request.getOrderId());
            if (null != order) {
                BeanUtils.copyProperties(order, response, new String[]{"execTime"});
                response.setExecTime(order.getExecTime().getTime());
            }
        } catch (Exception e) {
            // 系统异常信息返回
            log.error(e.getMessage(), e);
        }
        responseObserver.onNext(response.build());
        responseObserver.onCompleted();
    }
    ```

*   **数据访问层方法**：
    ```java
    public TradeOrder getOrder(Long orderID) {
        return tradeOrderDao.getById(orderID);
    }
    ```

*   **Protobuf 生成的类**：
    *   `GetOrderRequest` 和 `GetOrderResponse`。
    *   `TradeOrder`。
    *   `PlaceOrderResponse`。

---

### 4) 关键场景与演示描述

*   **场景一：服务接口实现**
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `GrpcStockDealService.java` 文件，演示如何实现 `getOrder` 方法。他首先定义了方法签名，然后创建了一个 `GetOrderResponse.Builder` 对象来构建响应。
    *   **技术点**：展示了 gRPC 服务方法的典型结构，使用 `StreamObserver` 来处理异步响应。

*   **场景二：数据查询与属性填充**
    *   **描述**：讲师在 `try` 块中调用 `stockDealService.getOrder(...)` 方法获取订单数据。他使用 `BeanUtils.copyProperties` 方法将 `TradeOrder` 对象的属性复制到响应对象中，并特别设置了 `execTime` 字段。
    *   **技术点**：演示了如何使用工具类简化对象属性复制，以及如何处理日期类型（通过 `getTime()` 方法）。

*   **场景三：异常处理**
    *   **描述**：讲师在 `catch` 块中处理异常。他区分了业务异常和系统异常，并分别使用 `PlaceOrderResponse.newBuilder().set...` 来构建错误响应。
    *   **技术点**：展示了如何在 gRPC 服务中优雅地处理错误，并向客户端返回结构化的错误信息。

*   **场景四：生产环境安全与 Protobuf 日期类型**
    *   **描述**：讲师切换到 PPT 页面，讲解了在生产环境中防止伪造参数和数据安全的重要性。他提到 Protobuf 不支持 `Date` 类型，并给出了使用 `google.protobuf.Timestamp` 的解决方案。
    *   **技术点**：强调了实际项目开发中安全性和数据类型兼容性的重要性。

*   **场景五：代码调试与运行**
    *   **描述**：讲师在 IDE 中使用鼠标点击和键盘操作，逐步调试代码，查看 `responseObserver.onNext(...)` 和 `onCompleted()` 的调用过程。
    *   **技术点**：展示了开发过程中如何通过 IDE 进行调试和验证代码逻辑。

---

以上是根据视频画面内容整理的技术分析报告。
