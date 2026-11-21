# 24-分布式事务解决方案Seata（应用_测试4） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好前面呢我们是测试了一下正常的情况

也就是没有发生异常的情况

所有的数据呢都已经提交了

是没有问题的

那接下来呢我们需要来改造一下

就是什么呢

我们人为的给它来

给它这个构造一个异常出来

就是什么呢

看看我们这个数据呢能不能回滚出来

好我在这注意看啊

这是我们下单的这个方法对吧

这是我们下单的这个方法

并且在这已经加了这个注解

前面这些微服务呢

该掉的都已经掉完了对吧

该掉的都已经掉完了

结果到最后这儿呢

是不是出来了一个除零异常

那这个时候呢我们看数据呢

能不能给我回滚回去

如果说发生这个异常

结果呢我们这个订单数据又插入成功了

这说明什么呢

这说明我们数据是不是没有回滚回去

这就表示我们这个分布式事物

没有起到作用对吧

所以我们希望看到的效果就是什么呢

一旦发生这个异常

那么这些数据呢应该都回滚回去

不能够插入成功

但是这改了代码之后呢

别忘了需要重启一下

其他的我们就不重启了

咱们只要重启一下这个什么呢

Customer就可以了

先把它停掉

好停掉之后呢

我们重新来启动一下

好我这边呢已经重启完成了

重启完成之后呢

咱们再来测试一下

首先呢我们先来看一下数据库里面

咱们还是就看我们这个

Order这个表就可以

然后呢我们还是这个地方呢

降序排列对吧

然后呢刷新

刷新一下大家来看啊

这边的话呢

我们总的数据量呢是543条对吧

然后呢这个时间呢是11月26号15.05

这是最后最后一条数据

然后呢我们再来测试一下

当然现在呢肯定是有异常信息对吧

然后呢我们直接来提交一下

还是这条数据

稍等一下

好你看它来了一个什么呢

除零异常对吧

除零异常

好那么已经发生异常了

这个时候呢我们来看数据

能不能进行异常

进来刷新一下

我们发现数据并没有进来

这个其实就是我们希望看到的对吧

这才说明我们的事物起作用了

如果在发生异常的情况下

数据还插进来了

这就说明我们这个分布式事物呢

其实没有起到作用

然后呢我们可以来看一下

咱们这个控制台这边对吧

它这边发生了这个除零异常

然后能不能看到它这个

关于我们这个日志的信息啊

就是什么呢

它发生异常对吧

然后呢我们这个分布式事物

来找一下

看看能不能看到它这个事物回滚的信息啊

正常来说应该是能够看到的

你看这边呢

它是不是要开启一个新的

还是考出来吧

这边不太好找

复制一下

然后呢到这边来

然后呢粘贴一下

在这儿能看到

你看这不是

这是我们前面这个地方

应该会开启一个新的对吧

begin new global transaction

是不是开启一个新的

然后呢在下边开始执行调用各种微服务

调用各种微服务

结果呢到这边是不是发生了异常

所以在这个地方呢

它是不是就进行了一个回滚对吧

在这儿进行了回滚

这边rollback status

回滚的状态是什么呢

rollbacked的已经回滚

那么这是这个事物的这个xid对吧

xid

所以通过这个控制台的日志呢

咱们其实也能够看到对吧

也能够看到

好

这是关于我们这个分布式事物啊

我们进行测试

就测试到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是“品达物流TMS项目”第11章“司机端、快递员端开发”中“测试”部分的演示。讲师通过集成 Swagger UI，对一个用于创建订单并分配快递员的后端接口进行功能测试。演示过程包括：在 Swagger 中构造并发送一个 POST 请求，观察服务端日志以验证业务逻辑的执行流程，并最终通过日志确认了订单创建、货物信息保存和快递员任务分配等关键步骤的成功。整个过程旨在验证分布式事务框架（如 Seata）在实际业务场景中的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中定位到“12、测试”章节，介绍本节目标是使用 Swagger 测试下单接口。
*   **00:05 - 00:15**: 展示了用于测试的 JSON 请求体，包含商品名称、类型、支付方式、取件时间、收件地址和发件地址等字段。
*   **00:15 - 00:25**: 切换到 IntelliJ IDEA，展示 `MailingController.java` 中的 `save` 方法，重点讲解了如何获取收件地址、构建订单实体并调用 Feign 客户端保存订单信息。
*   **00:25 - 00:35**: 展示了 `pickupDispatchTaskFeign.save(...)` 方法的调用，用于保存派单任务。
*   **00:35 - 00:45**: 切换到浏览器，打开 Swagger UI，将之前构造的 JSON 请求体粘贴到请求体中，并点击“Execute”按钮发送请求。
*   **00:45 - 00:55**: 展示了服务端日志，讲师通过日志逐行解释了业务流程：从“开启新事物”到“业务开始日志”，再到“订单保存成功日志”、“货物信息保存成功日志”和“快递员任务保存成功日志”。
*   **00:55 - 01:05**: 日志中出现 `ArithmeticException: / by zero` 错误，讲师指出这是由于测试数据中“取件时间”设置为 `14:00-18:00`，而“预计开始时间”设置为 `14:00`，导致计算时除零。
*   **01:05 - 01:15**: 讲师修改了测试数据，将“预计开始时间”设置为 `14:30`，并再次执行请求。
*   **01:15 - 01:25**: 展示了修改后成功执行的日志，确认了“快递员任务保存成功日志”。
*   **01:25 - 01:35**: 讲师总结，通过日志确认了整个业务流程的正确性，并强调了日志在调试和验证中的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **文档标题**: “品达物流TMS项目”、“第11章 司机端、快递员端开发”、“12、测试”。
    *   **测试目标**: “使用Swagger测试下单接口”。
    *   **日志检查点**: “1. 开启新事物”、“2. 业务开始日志”、“3. 订单保存成功日志”、“4. 货物信息保存成功日志”、“5. 快递员任务保存成功日志”、“6. 提交事务”。

*   **代码关键内容**:
    *   **Swagger 请求体 (JSON)**:
        ```json
        {
          "goodsName": "电话",
          "goodsType": "1209411984412801024",
          "goodsWeight": "1",
          "payMethod": 1,
          "pickupTime": "14:00-18:00",
          "pickupType": 2,
          "receiptAddress": "315143F35b128e6ad5496c409c340dd",
          "sendAddress": "9cdbace3a522f4eebd4d4a5628f72beb"
        }
        ```
    *   **Java 代码 (MailingController.java)**:
        ```java
        // 获取收件地址
        Result resultReceive = getReceiveAgencyId(orderDTO);
        if (resultReceive.getCode().toString().equals("0")) {
            return resultReceive;
        }
        String receiveAgencyId = resultReceive.get("agencyId").toString();
        String receiveAgentLocation = resultReceive.get("location").toString();

        // 保存订单信息
        OrderCargoDto cargoDto = buildOrderCargo(entity);
        orderDTO.setOrderFeign(cargoDto);
        orderDTO.save(orderDTO);

        // 保存派单任务
        pickupDispatchTaskDTO.setEstimatedStartTime(LocalDateTime.now());
        pickupDispatchTaskDTO.setEstimatedEndTime(DateUtils.getUTCTime(pickupDateTime));
        if (StringUtils.isNotBlank(courierId)) {
            pickupDispatchTaskDTO.setAssignedStatus(PickupDispatchTaskAssignedStatus.DISTRIBUTED);
        } else {
            pickupDispatchTaskDTO.setAssignedStatus(PickupDispatchTaskAssignedStatus.MANUAL_DISPATCH);
        }
        pickupDispatchTaskFeign.save(pickupDispatchTaskDTO);
        System.out.println(1);
        ```

*   **日志关键内容**:
    *   **成功日志**: `INFO ... MailingController: 订单保存成功`、`INFO ... MailingController: 货物信息保存成功`、`INFO ... MailingController: 快递员任务保存成功`。
    *   **错误日志**: `ERROR ... MailingController: / by zero`。
    *   **调试日志**: `INFO ... NettyClientChannelManager: will connect to ...`、`INFO ... DynamicServerListLoadBalancer: Flipping property: pd-user.ribbon.ActiveConnectionsLimit`。

---

### 4) 关键场景与演示描述

*   **场景一：测试环境准备**
    *   **描述**: 讲师首先在 Typora 文档中定位到测试章节，并展示了用于测试的 JSON 请求体。随后，他切换到 IntelliJ IDEA，展示了 `MailingController.java` 中的 `save` 方法，解释了其业务逻辑，包括获取收件地址、构建订单实体和调用 Feign 客户端。

*   **场景二：Swagger 接口测试**
    *   **描述**: 讲师切换到浏览器，打开 Swagger UI，将之前构造的 JSON 请求体粘贴到请求体中，并点击“Execute”按钮发送请求。他随后在服务端日志中观察到请求处理的各个阶段。

*   **场景三：日志分析与调试**
    *   **描述**: 讲师通过分析服务端日志，逐行解释了业务流程的执行情况。他首先确认了“开启新事物”和“业务开始日志”，然后观察到“订单保存成功日志”、“货物信息保存成功日志”和“快递员任务保存成功日志”。在日志中出现 `ArithmeticException: / by zero` 错误后，讲师修改了测试数据，将“预计开始时间”从 `14:00` 改为 `14:30`，并再次执行请求，最终成功验证了业务流程。

*   **场景四：错误处理与总结**
    *   **描述**: 讲师在日志中发现了除零错误，并解释了其原因。他通过修改测试数据成功解决了问题，并总结了本次测试，强调了日志在调试和验证中的重要性。
