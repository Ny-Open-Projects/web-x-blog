# 23-分布式事务解决方案Seata（应用_测试3） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

刚才呢

我们是测试了一下

对于这种正常状态下

对吧

那么我们测试整个流程是能够跑通的

通过它这个日志信息能够看到

对吧

全局事务开启

然后呢

全都执行完之后呢

事务提交

好

中间呢

可能是由多个分支事务来构成

对吧

多个分支事务来构成

现在呢

我们可以这样啊

你看我现在是debug方式启动的

我想带着大家来看一下什么呢

就是我们这个事务

它的一个中间状态

什么意思呢

也就是说

我们这个事务还没有提交的时候呢

中间呢

它会操作我们那个SETA那个数据库

当然了

当我们这个事务最终提交完之后呢

它那个三张表里面数据呢

就已经清空了

所以我们在这儿呢

给它加一个断点

加一个断点

咱们来看啊

那么我们可以这样

在这个return这儿

加一个断点

也就是前面这些是不是全都操作完

但是呢

因为这个方法还没有执行完成

所以最终还没有提交

那这个时候呢

我们来看一下什么呢

咱们来看一下SETA这个数据库里边

这三张表

现在呢

我们可以来看一下

这个表里面应该都是空的

你看是不是没有数据

然后呢

包括branch table

这是不是也没有数据

还有这个什么lock table

也没有数据

对吧

好

然后呢

我们接下来呢

再来提交一次啊

我再来提交一次

注意看

这边是不是已经加了断点了

对吧

加了断点了

它会停下来

然后呢

我们提交

好

你看它已经停在这儿了

然后呢

就差最后提交了

对吧

那些分支事务其实都已经该做的操作都已经做完了

就差最后统一提交了

然后这个时候呢

是一个中间状态

咱们来看这个global table里边

哎

你注意看它是不是有这么一条数据

有这么一条数据

然后呢

我们可以来看一下

这是我们的Rxid对吧

它是前面这个ipd

只是加上端口号

加上后边这么一串

而这个事务id呢

哎

其实你会发现啊

它们非常像

哎

我把这一段拿出来

是不是就是我这个事务id

对吧

哎

然后呢

status是1

哎

然后呢

还有application id

对吧

应用id是pdweb

什么customer

然后呢

这个是这个service

这是不是就是我们设置的

大家还记得那个串吧

哎

然后呢

这是事务的名称叫saveorder

为什么叫saveorder呢

哎

因为我这个这个地方写了啊

在这个地方

是不是写了

这是我事务的名称

叫做saveorder

但是你这不写也可以

它会默认跟我们生成一个

啊

然后呢

还这个超时时间对吧

但是现在有可能会超时

因为已经过了很长时间了

然后呢

再看分支

这个表

哎

这个表里边

因为现在已经执行完了

对吧

因为它们那边都已经过去了

所以这边看不见了

全局的那个能看到

这边这个都看不到了

啊

那就算了啊

那么能够看到全局的这个就可以

因为那边呢

都已经执行完了

啊

然后呢

我们可以给它

放过去啊

看看会不会超时啊

因为我在这儿

这个断点已经加了很长时间了

好

然后呢

我们看一下页面这边

SXS

哎

没有问题

好

然后呢

如果想看这个

呃

分支事务呢

我们也可以怎么做呢

你需要在这个分支这边

也就是比如说我们这个PD work

或者是PD OMS这边

来给它加一个什么呢

断点

呃

它这边是不是会

哎

呃

保存订单对吧

会保存订单

所以我们在这儿呢

给它加一个断点

让它从这儿停下来啊

然后这边这个呢

就给它去掉了

咱们再来提交一个啊

再来停交一个

你看再次提交啊

你看它现在停到了我们这个order controller

对吧

然后呢

现在还没有去去提交啊

然后呢

我们从这边来看一下

看一下这个branch table

哎

你看它现在是不是从这能够看到

而

这个呢就是我们一个分支

哎

一个分支事务对吧

分支事务

然后呢

这是我们全局的那个什么呢

全局的这个事务ID

然后呢

这是分支哎

这个分支的ID

哎

这是事务ID

然后呢

这边这是resource ID

资源ID对吧

你看我们当前操作的是不是OMS这个库

对吧

哎

这是资源ID

然后呢

branch type是AT

然后呢

cline的ID

这是我们客户端的ID

好

然后呢

还有application data

这个这个是空的

对吧

好

能够看到这个就可以了

然后呢

我们把断点只要一放过去呢

他就会把这个数据呢

又给删掉了

好

给他放过去

然后呢

这边你再刷新一下

你看数据就没有了

相当于他只是一个中间的状态啊

只是一个中间的状态

包括我们全局事务呢

其实你放完之后呢

他也就没有了

好

所以这是我们结合的

咱们这几张表对吧

哎

那么他这个全局事务在执行的过程当中啊

会把我们这个全局事务还有分支事务

包括锁定的哪些表

把它存储在这个相应的表里面去

当我们整个这个流程跑通了

对吧

分布式事务已经结束了

那么这些中间状态记录的这个数据呢

就都被清除

清除掉了

而操作这个表是谁操作的呢

很显然我们并没有去操作

对不对

而是由谁呢

由Cita Server去操作的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程聚焦于一个名为“pinda”的分布式电商系统（或称“Pinda”平台）的订单与派单核心模块。讲师通过 IntelliJ IDEA 和 Navicat Premium 等开发工具，演示了从用户下单、系统计算派送费用、获取快递员、到最终生成订单并记录位置信息的完整业务流程。同时，视频也深入讲解了系统底层的技术架构，包括基于 Spring Boot 的微服务架构、分布式事务解决方案（如 Seata 分布式事务中间件）以及数据库设计（如订单表、锁表等）。整个演示过程结合了代码逻辑、数据库操作和日志输出，旨在展示一个高并发、高可用的分布式系统如何协同工作。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下章节按画面出现的逻辑顺序进行划分：

- **章节 1：系统启动与服务架构概览 (约 0:00 - 0:30)**
  - 展示了 IntelliJ IDEA 中的项目结构，包含 `pd-web-customer`、`pd-auth`、`pd-order` 等多个微服务模块。
  - 启动了 `WebCustomerApplication`，并在控制台输出了服务启动成功的日志和 Swagger 文档访问地址。
  - 展示了多个微服务的启动日志，表明这是一个多服务协同的系统。

- **章节 2：订单创建与派单逻辑 (约 0:30 - 1:30)**
  - 进入 `MailingController` 的代码，演示了用户下单后，系统如何根据收货地址计算派送费用。
  - 代码逻辑包括：获取快递员 ID、计算派送费用、保存派送任务。
  - 展示了 `orderDTO` 对象的构建和 `orderFeign.save(orderDTO)` 调用，用于将订单信息保存到订单服务。

- **章节 3：数据库操作与事务管理 (约 1:30 - 2:30)**
  - 切换到 Navicat Premium，展示了 `pd_order` 表的数据，验证了订单的创建。
  - 展示了 Seata 的锁表（`branch_table`, `global_table`, `lock_table`）结构，用于演示分布式事务的实现。
  - 通过日志输出，展示了 Seata 事务的开始、提交和回滚过程，以及 `orderDTO` 对象的持久化操作。

- **章节 4：代码调试与日志分析 (约 2:30 - 3:30)**
  - 在 IntelliJ IDEA 中，对 `MailingController` 的代码进行调试，观察变量值和日志输出。
  - 展示了 `orderDTO` 对象的详细信息，包括 `amount`、`create_time`、`receiver_location` 等字段。
  - 通过日志分析，验证了系统在处理订单时的各个步骤是否成功。

- **章节 5：系统架构与技术栈总结 (约 3:30 - 结束)**
  - 通过多个服务的启动日志，再次强调了微服务架构。
  - 展示了 Seata 的锁表结构，总结了分布式事务的实现方式。
  - 最终画面停留在 Seata 的锁表设计图上，作为本节的收尾。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **代码片段 (Code Snippets)**

  - **订单创建与派单逻辑 (MailingController.java)**
    ```java
    if (result.get("code").toString().equals("0")) {
        return result;
    }
    String agencyId = result.get("agencyId").toString();
    orderDTO.setAgencyId(agencyId);
    String sendLocation = result.get("location").toString();
    Result resultCourier = getCourierId(sendLocation, orderDTO);
    if (resultCourier.get("code").toString().equals("0")) {
        return resultCourier;
    }
    String courierId = resultCourier.get("userId").toString();
    ```

  - **获取收货地址的网点 (MailingController.java)**
    ```java
    private Result getReceiveAgencyId(OrderDTO orderDTO) {
        String address = receiverFullAddress(orderDTO);
        if (StringUtils.isBlank(address)) {
            return Result.error("收货地址不能为空");
        }
        Result resultReceive = getReceiveAgencyId(orderDTO);
        if (resultReceive.get("code").toString().equals("0")) {
            return resultReceive;
        }
        String receiveAgencyId = resultReceive.get("agencyId").toString();
        String receiveAgentLocation = resultReceive.get("location").toString();
    }
    ```

  - **订单保存 (OrderController.java)**
    ```java
    order.setAmount(new BigDecimal(map.getOrDefault("amount", "0").toString()));
    order.setOrderType(orderType);
    order.setCreateBy("admin");
    order.setCreateTime(LocalDateTime.now());
    order.setUpdateTime(LocalDateTime.now());
    order.setVersion(0);
    order.setDelFlag(0);
    order.setOrderStatus(OrderStatusEnum.UNPAID.getCode());
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrderType(orderType);
    order.setOrder
