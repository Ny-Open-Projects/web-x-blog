# 26-用户撤单-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们再对本章功能做个回顾与总结

首先咱们回顾下本章的学习目标

在这里主要是两点

第一点要实现用户的测单功能

第二点要去验证多场景下面用户测单的可用性

这里我们验证了两种场景

一个是订单未成交状态下的测单处理

另外一个是订单的部分成交状态下的测单处理

这两种都是比较常用的场景

接下来咱们再回顾下本章所讲解的具体内容

首先咱们从接口层面做了一个定义

定义了测单接口Neti与客户端的交互数据结构

以及GRPC的接口层的传输数据结构

接下来我们就将测单服务功能放在挂单服里面做具体的实现

首先咱们是实现了GRPC接口层的处理

在这里为了防止对联缓存不一致问题

咱们进行了枷锁的处理

GRPC接口主要是做两件事情

第一件事情就是将缓存的对联信息做匹配

然后进行更新

另外一件事情就是要对数据互动的数据做撤回处理

这个是通过service层做对应的实现

接下来我们就对service层做了具体的实现

service层的处理最主要是要做好条件的校验判断

如果是不符合条件的请求

在这里我们要抛出对应的异常

要注意交易账户的判断处理

只有属于该交易账户的订单才能够进行撤回

权限控制是不能够错乱

接下来咱们在代理服务上面

对测单功能进行了一个调用实现

咱们增加了挂单服务的处理器

然后在工厂方法当中做了对应的扩展

最后我们对用户测单功能进行了一个调用实现

做了一个测试和验证

在测试验证之前咱们要去修改模拟器

封装测单的调用方法

通过测试验证咱们实现的用户测单功能接口

是能够正常处理

最后咱们再来总结一下

测单的处理逻辑相对前面的挂单接口处理

试驾单的处理逻辑会比较简单一点

最主要要注意相关条件的

教验判断

避免数据出现错乱

注意它的调用处理顺序

以及交易账户信息的判断处理

在接口的实现过程当中

我们要考虑权限安全的处理

只要和用户相关的接口数据

咱们在实现的时候

一定要全面充分的考虑

对用户账号信息要做必要的检查

不能够出现越权的情况

这涉及到

数据的安全性问题

最后在对测单接口的实现过程当中

咱们也要考虑性能

以及现成安全性的问题

所以在这里

咱们通过了一个同步索

去做对应的实现

接口调用的处理

不能保上百分之百的OK

某些场景下面

咱们要考虑它的容错性

通过测单功能接口的学习

不仅要完成测单的功能

更重要的是掌握整体的处理实现思路

能够编写出一个

现状稳定高性能数据安全性高的接口

这就需要咱们在功能实现的时候

从这些层面做充分的考虑

好

在这里呢

就是对本章功能的回顾与总结

那这一讲的内容就到此结束

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程为“第3章 用户撤单功能实现”的教学内容，主要讲解了在分布式系统中如何实现一个完整的用户撤单功能。课程从定义接口数据结构（使用 Protocol Buffer）开始，逐步深入到后端服务（挂单服务）的实现细节，包括如何处理撤单请求、校验订单状态和账户信息、更新数据库状态、以及如何通过代理服务调用该功能。最后，通过一个完整的测试用例（修改订单ID为35并发送撤单请求）来验证功能的正确性。整个过程强调了在实际开发中需要考虑的多个关键点，如数据一致性、权限安全、线程安全和接口容错性。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**：开场，展示课程大纲，明确本章主题为“第3章 用户撤单功能实现”。
*   **00:05 - 00:15**：进入“3.1 定义接口数据结构”章节，讲解如何修改 `StockMessage.proto` 文件，定义 `StockMessage` 消息体，其中包含 `LoginData` 和 `RecallOrderData` 等字段。
*   **00:15 - 00:30**：进入“3.2 挂单服务撤单功能实现”章节，展示 `GrpcStockPendingService` 服务类的代码，重点讲解 `recallOrder` 方法的实现。
*   **00:30 - 00:45**：深入讲解 `recallOrder` 方法的业务逻辑，包括：
    *   **步骤 6**：遍历 `placeOrderRequestVoList` 队列，检查账户ID和订单ID是否匹配，匹配则从队列中移除。
    *   **步骤 7**：如果队列发生变更，更新缓存。
    *   **步骤 8**：进行数据库撤单处理。
*   **00:45 - 00:55**：讲解数据库处理逻辑，展示如何根据订单ID查询订单，校验账户ID是否匹配，并根据订单状态（`ORDER_STATUS_WAIT` 或 `ORDER_STATUS_PART`）决定是否允许撤单。
*   **00:55 - 01:05**：讲解“3.3 代理服务撤单调用实现”章节，展示如何在代理服务中构造请求并调用挂单服务。
*   **01:05 - 01:15**：讲解“3.4 功能验证”章节，展示测试代码 `NettyClientTest`，模拟发送撤单请求。
*   **01:15 - 01:25**：展示测试结果，包括控制台日志和数据库查询结果，验证撤单成功后订单状态已更新。
*   **01:25 - 01:35**：进入“4. 总结”章节，回顾整个功能实现的关键点和注意事项。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`第3章 用户撤单功能实现`。
    *   **子章节**：`3.1 定义接口数据结构`，`3.2 挂单服务撤单功能实现`，`3.3 代理服务撤单调用实现`，`3.4 功能验证`，`4. 总结`。
    *   **总结要点**：
        1.  撤单的处理逻辑相对简单，要注意相关条件的校验判断，避免数据错乱。
        2.  要考虑接口权限安全的处理，对用户账号信息必要检查，不能出现越权情况。
        3.  对撤单接口的实现，要考虑线程安全以及接口调用某些场景的容错性。

*   **代码关键内容**：

    *   **Protocol Buffer 定义** (`StockMessage.proto`):
        ```protobuf
        message StockMessage {
          // 头部消息
          StockHead stockHead = 1;
          // 消息体
          oneof StockData {
            // 登录的请求包
            LoginData loginData = 2;
            // 撤单的请求包
            RecallOrderData recallOrderData = 3;
          }
        }
        ```

    *   **挂单服务实现** (`GrpcStockPendingService.java`):
        ```java
        @Override
        public void recallOrder(RecallOrderRequest request, StreamObserver<RecallOrderResponse> responseObserver) {
            RecallOrderResponse response = null;
            try {
                // 1. 加锁处理，防止队列缓存不一致
                synchronized (this) {
                    // 6. 如果账户ID和订单ID匹配到数据，则进行清除
                    if (placeOrderRequestVoList != null && !placeOrderRequestVoList.isEmpty()) {
                        Iterator<LimitPlaceOrderRequestVo> itr = placeOrderRequestVoList.iterator();
                        while (itr.hasNext()) {
                            LimitPlaceOrderRequestVo placeOrder = itr.next();
                            if (placeOrder.getOrderId().equals(request.getOrderId()) &&
                                placeOrder.getAccountId().equals(request.getAccountId())) {
                                itr.remove();
                                isModify = true;
                                break;
                            }
                        }
                        if (isModify) {
                            // 7. 如果撤单队列发生变更，需要进行缓存更新
                            cache.put(request.getStockId(), placeOrderRequestVoList);
                        }
                    }
                    // 8. 数据撤单处理
                    TradeOrder order = tradeOrderDao.getOrderBy(request.getOrderId());
                    if (order == null) {
                        throw new ComponentException(ApplicationErrorCodeEnum.ORDER_NOT_FOUND);
                    }
                    if (!order.getAccountId().equals(request.getAccountId())) {
                        throw new ComponentException(ApplicationErrorCodeEnum.ACCOUNT_NOT_MATCH);
                    }
                    // 2. 对订单状态做判断处理，如果是等待成交或部分成交的状态，才允许撤单
                    if (order.getStatus() == GlobalConstants.ORDER_STATUS_WAIT ||
                        order.getStatus() == GlobalConstants.ORDER_STATUS_PART) {
                        tradeOrderDao.updateOrderStatusById(request.getOrderId(), GlobalConstants.ORDER_STATUS_RECALL);
                    }
                }
                response = RecallOrderResponse.newBuilder()
                    .setStatus(GlobalConstants.STATUS_OK)
                    .setMessage("撤单成功！")
                    .build();
            } catch (ComponentException e) {
                // 业务异常返回
                response = RecallOrderResponse.newBuilder()
                    .setStatus(e.getErrorCodeEnum().getCode())
                    .setMessage(e.getErrorCodeEnum().getMessage())
                    .build();
            } catch (Exception e) {
                // 系统异常信息返回
                response = RecallOrderResponse.newBuilder()
                    .setStatus(GlobalConstants.STATUS_ERROR)
                    .setMessage(e.getMessage())
                    .build();
            }
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }
        ```

    *   **代理服务调用** (`NettyClientTest.java`):
        ```java
        public void recallOrder(String orderIdStr) {
            Long orderId = Long.valueOf(orderIdStr);
            System.out.println("******* Send Recall Order, Parameters");
            System.out.println("== orderId: " + orderId);
            // 构造头部信息
            StockHeadProto.StockHead stockHead = StockHeadProto.StockHead.newBuilder()
                .setSeqId(seqId++)
                .setRequestType(StockHeadProto.RequestType.RECALL_ORDER)
                .build();
            RecallOrderData recallOrderData = RecallOrderData.newBuilder()
                .setOrderId(orderId)
                .setStockId(stockId)
                .build();
            StockMessage stockMessage = StockMessage.newBuilder()
                .setStockHead(stockHead)
                .setRecallOrderData(recallOrderData)
                .build();
            // 发送请求
            channel.writeAndFlush(stockMessage);
        }
        ```

    *   **工程配置** (`application.yml`):
        ```yaml
        # grpc 配置
        grpc:
          client:
            # 挂单服务
            grpc-pending-server:
              address: 'discovery://stock-pending'
              enableKeepAlive: true
              keepAliveWithoutCalls: true
              negotiationType: plaintext
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据结构定义** (00:05-00:15)
    *   **描述**：讲师在 Typora 编辑器中展示 `StockMessage.proto` 文件的修改过程。重点讲解了 `StockMessage` 消息体中 `oneof` 的使用，以支持多种请求类型（如登录和撤单），并定义了 `RecallOrderData` 作为撤单请求的数据结构。

*   **场景二：挂单服务实现** (00:15-00:45)
    *   **描述**：讲师展示了 `GrpcStockPendingService` 服务类的 `recallOrder` 方法。通过代码演示了如何处理撤单请求，包括：
        *   **队列处理**：遍历 `placeOrderRequestVoList` 队列，查找并移除匹配
