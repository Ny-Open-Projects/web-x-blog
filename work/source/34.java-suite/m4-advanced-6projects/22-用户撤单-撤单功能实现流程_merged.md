# 22-用户撤单-撤单功能实现流程 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着学习挂单服务测单功能的实现

咱们回到工程当中

找到挂单的服务接口

在Pending下面

GRPC

打开GRPC Stock Pending Service

在下面呢

咱们去重写刚才定义的GRPC接口

Edit Insert

Overlay

选择Local Order

我们添加对应的注释

这个是

用户

测单接口的处理

首先咱们来梳理一下

测单接口的整体处理逻辑

第一步

要进行加锁处理

防止

对列

缓存数据不一致问题

通过加锁处理

挂单服务里面的挂单接口

和用户测单接口

对缓存对列进行操作的时候

就不会产生并发安全的问题

接下来第二步

要获取挂单

不对应的

缓存对列信息

拿到缓存对列信息

咱们再接着下面的逻辑处理

接下来就是根据股票ID

去获取委托挂单信息

咱们就要去根据传递的订单ID

交易账户

以及stock ID

股票产品ID

去挂单对列里面

做便利匹配

我们就要去挂单对列信息

那第四步就要获取

委托挂单列表信息

上面这里是获取

委托挂单信息的

缓存操作对象

拿到获取的

委托挂单列表信息之后

第五步

咱们就要去便利挂单

列表信息

下面呢

就要根据便利所获取的挂单信息

做匹配

如何匹配呢

根据账户的

账户ID和订单ID

去匹配挂单信息

如果匹配成功之后

就要将挂单列表对应的这条订单数据进行清除

清除完成之后

挂单对列就发生了变化

挂单对列就发生了变化

这个时候呢

就要去更新缓存

如果没有匹配

就不需要清除数据

也不需要更新缓存信息

如果挂单对列发生了变更

则需要

更新缓存信息

这样的

咱们就实现了缓存对列里面订单信息的撤回处理

最后呢

还有对持久化的订单信息进行回滚

去修改数据库的订单信息

将订单的状态改为手工测单的状态

标记为这个订单已经是做了撤回处理

最后就是撤回

数据库的订单信息

这个呢是数据库

好

这个呢就是订单撤回的整体实现处理逻辑

具体逻辑的实现

咱们在下面章节再做讲解

这里我们先实现外层代码的处理

首先去定义

recall order response的响应对象

接下来外围定义一个check cache

异常的补货处理

catch部分的代码

咱们就直接从讲义当中copy去处理

接下来外围定义一个check cache异常的补货处理

进来

将红色错误部分做个修正

response

这里也是response

名称写错了

这里修正一下

这里再将响应对象输出给调用房

response

observe

next

传递response对象

observe

在这里标记为处理完成

将整个的实现步骤

咱们先移植过去

放入里面

在内部要返回一个处理成功的响应

response

给它做一个组装

order response

new builder

set state

variable consistency

state ok

再设置它的message

这里提示测单

处理成功

要用builder进行构建

这里回车

再设置它的message

整理下代码

这里加锁的处理

仍然是附用挂单接口里面

所机制的处理

咱们可以先做个实现

signalize

通过pending call consume里面的进台方法

进行调用

在这里咱们将getlog方法

改成公用的

找到getlog

改成public

再回到刚才的实现代码

传递stock id

将处理实现方法

选择选择步骤

拋逼进去

在这里咱们就对挂单

测回接口

整体流程做了一个梳理

以及对外层逻辑

做了一个简单实现

下一讲咱们再来对核心逻辑

做代码的具体实现

好

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“撤单”（Recall Order）功能的实现，主要聚焦于使用 gRPC 服务和 Redis 缓存来处理订单的撤回请求。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `GrpcStockPendingService` 服务中实现 `recallOrder` 方法。该方法的核心逻辑是：接收撤单请求，通过 Redis 获取对应的订单队列信息，遍历队列中的订单，根据客户 ID 和订单 ID 进行匹配，如果匹配成功则将订单从队列中移除，并更新缓存和数据库。整个过程包含异常处理，确保数据一致性，并通过 gRPC 返回操作结果。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示项目结构，定位到 `GrpcStockPendingService` 服务。
*   **00:00:05 - 00:00:15**: 显示 `recallOrder` 方法的注释，概述其功能：获取队列信息、遍历订单、匹配并清除、更新缓存。
*   **00:00:15 - 00:00:30**: 开始编写 `recallOrder` 方法的主体，首先处理异常，然后获取 Redis 缓存操作对象。
*   **00:00:30 - 00:00:45**: 通过 `RedisCacheManager` 获取缓存，根据股票 ID 获取订单队列。
*   **00:00:45 - 00:01:00**: 遍历订单队列，对每个订单进行匹配检查。
*   **00:01:00 - 00:01:15**: 如果匹配成功，执行清除操作，并更新缓存。
*   **00:01:15 - 00:01:30**: 构建并返回成功的 gRPC 响应。
*   **00:01:30 - 00:01:45**: 处理异常情况，返回错误响应。
*   **00:01:45 - 00:02:00**: 完成方法，确保所有资源和状态正确处理。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **gRPC 服务方法签名**:
        ```java
        @Override
        public void recallOrder(RecallOrderRequest request, StreamObserver<RecallOrderResponse> responseObserver) {
            // 业务逻辑
        }
        ```
    *   **Redis 缓存操作**:
        ```java
        Cache.ValueWrapper cache = cacheManager.getCache(stockLastMsg.getStockId());
        List<LimitPlaceOrderRequestVo> placeOrderRequestList = (List<LimitPlaceOrderRequestVo>) cache.get();
        ```
    *   **订单匹配与清除**:
        ```java
        for (Iterator<LimitPlaceOrderRequestVo> itr = placeOrderRequestList.iterator(); itr.hasNext(); ) {
            LimitPlaceOrderRequestVo placeOrder = itr.next();
            boolean matchPrice = stockTradePendingService.checkMatchPrice(...);
            if (matchPrice) {
                // 清除订单逻辑
                itr.remove();
                // 更新缓存
                cache.put(stockLastMsg.getStockId(), placeOrderRequestList);
            }
        }
        ```
    *   **构建响应**:
        ```java
        response = RecallOrderResponse.newBuilder()
            .setStatus(GlobalConstants.STATUS_OK)
            .setMessage("撤单处理成功！")
            .build();
        ```
    *   **异常处理**:
        ```java
        } catch (ComponentException e) {
            log.error(e.getMessage(), e);
            response = RecallOrderResponse.newBuilder()
                .setStatusCode(e.getErrorCodeEnum().getCode())
                .setMessage(e.getMessage());
        } catch (Exception e) {
            log.error(e.getMessage(), e);
            response = RecallOrderResponse.newBuilder()
                .setStatus(GlobalConstants.STATUS_ERROR)
                .setMessage(e.getMessage());
        }
        ```

*   **关键注释**:
    *   `// 1. 加锁处理，防止队列缓存数据不一致问题`
    *   `// 2. 获取挂单服务对应缓存队列信息`
    *   `// 3. 根据股票ID获取委托挂单信息的缓存操作对象`
    *   `// 4. 获取委托挂单列表信息`
    *   `// 5. 遍历挂单列表信息`
    *   `// 6. 根据账户ID和订单ID匹配挂单信息，如果匹配成功，则进行清除`
    *   `// 7. 如果挂单队列发生了变更，则需要更新缓存信息`
    *   `// 8. 撤回数据库的订单信息`

---

### 4) 关键场景与演示描述

*   **场景一：方法定义与注释**
    *   讲师首先展示了 `GrpcStockPendingService` 类中的 `recallOrder` 方法，并通过注释详细说明了其功能。注释清晰地列出了从获取缓存到更新数据库的整个流程，为后续代码编写提供了明确的指导。

*   **场景二：异常处理与 Redis 初始化**
    *   讲师在方法开头添加了 `try-catch` 块，用于处理可能发生的异常。接着，他通过 `RedisCacheManager` 获取了缓存操作对象，为后续的缓存读写操作做好准备。

*   **场景三：缓存读取与订单遍历**
    *   讲师通过 `cacheManager.getCache(stockLastMsg.getStockId())` 获取了指定股票 ID 的缓存。然后，他将缓存中的订单列表转换为 `List<LimitPlaceOrderRequestVo>`，并使用 `for` 循环遍历该列表。

*   **场景四：订单匹配与清除**
    *   在循环中，讲师调用 `stockTradePendingService.checkMatchPrice(...)` 方法来检查当前订单是否匹配。如果匹配成功，他将该订单从列表中移除（`itr.remove()`），并更新缓存（`cache.put(...)`）。

*   **场景五：响应构建与返回**
    *   在完成所有操作后，讲师构建了一个成功的 gRPC 响应对象，并调用 `responseObserver.onNext(response)` 将其发送给客户端。
    *   如果在过程中发生异常，讲师会捕获异常，并构建一个包含错误信息的响应对象，然后发送给客户端。

*   **场景六：代码调试与优化**
    *   讲师在编写过程中，通过 IDEA 的智能提示功能来选择正确的 `set` 方法，确保代码的正确性。他还会在代码中添加注释，以便于后续维护和理解。

---

通过以上分析，我们可以看到讲师在视频中详细演示了如何在 gRPC 服务中实现一个复杂的业务逻辑，包括异常处理、缓存操作、数据匹配和响应构建等关键步骤。
