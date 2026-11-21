# 34-智能调度服务（实现过程_订单分类_3） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们就继续来编写我们这个订单分类的实现类

刚才呢我们是分析了一下要实现订单分类对吧

大概分成这么三个关键步骤

好那接下来呢我们就来看啊

接下来我们就要写写具体在哪了

首先呢我在这呢需要封装一个list集合

list集合

然后呢这个集合里面是放的什么呢

就是这个other classified

dto

叫做other classified details

你有一个array list

那么我们为什么要封装这么一个list集合呢

就是因为我们第一步呢

要把当前这个组织机构下边的所有的订单对吧

包括新订单还有中转订单

那么把这两类订单呢都需要把它收集上来

收集上来之后呢需要把它放到这个集合里面去

所以说呢我们当前这个集合呢用于什么呢

用于存放我们当前机构下的这个订单

好

所以需要有这么一个集合来存放

然后呢再来创建这么一个对象

这是我们这个方法的返回值对吧

这个方法的返回值

最终呢我们是需要返回这么一个对象啊

叫做other classified

group details

然后在这也是new一个

array list

最终呢我们要返回的就是这个对象

最终要返回的就是这个对象

但是现在呢我们只是new出来了

还没有去操作它

对吧

那么中间过程呢我们肯定是需要去操作它

最终返回之后呢这里边就已经这个填满了值了

好

然后呢接下来我们就需要干什么呢

是不是先分成两个阶段啊

第一个呢是新订单

还有一个是中转订单

所以呢我们在这个地方呢

就可以直接调用我们这个details

这个例子集合

它的addall这个方法对吧

来添加

添加这个元素进来

那么这个元素呢应该就是什么呢

就是我们的这个

这个

新订单

新订单

然后呢封装成的一个集合

对吧

那这个地方呢我们就需要来抽一个方法出来

也就是这个方法呢

就是专门来干什么呢

来查询我们当前这个机构下边的新订单的

好

所以我们在这个地方呢就需要来抽一个方法出来

这个方法呢就叫什么呢

叫做build new order吧

你看这个名字叫做构建新订单

对吧

然后呢把这个机构ID肯定是这个方法呢

是需要给我传过来的啊

就是这个build new order

然后呢现在肯定是没有这个方法对吧

那么我们现在呢就需要把这个方法来创建一下

好

这个呢直接返回list的就可以啊

没有必要这么复杂

所以我们在这呢直接来一个list的集合

然后呢这个集合里边呢

装的是什么呢

就是这种元素就可以

这个方法呢是用来我们来写一下啊

来干什么呢

获取指定啊

指定机构下的什么呢

新订单

新订单

具体是哪个机构呢

我这是不是已经给你传过来了

对吧

agency ID

好

所以我们在这呢直接调这个方法

然后返回指直接add all

是不是直接添加到我们下面这个创建的这个集合里面去

就可以了

这就是先把我们当前机构下边的所有的新订单

加到这个集合里面去

那么很显然一会儿我们是不是还要再调一个什么呢

中转订单的对不对

也都需要把它加进来

好

所以现在呢

这个重点呢就转移到这个方法了

就是什么呢

我们如何来查询什么呢

这个组织机构下边的新订单

是不是就转换成这个问题了

那这个地方的话

我们要查询订单对吧

那么我们来看一下订单数据呢

其实并不在我们当前这个库里吧

那么这个订单是在哪呢

其实是在我们这个OMS

是不是在这个库里吧

所以我们这个地方呢

就会使用到我们的订单数据

我们这个FIN接口啊

进行远程调用

好

那这块反映有点慢

那么不用管它了

也就是说我们在这个地方呢

其实是需要来调用我们这个FIN接口

所以说呢

在这个地方呢

我们就需要来注入啊

叫做什么呢

叫做order

在这来写一下private

叫做orderfin

orderfin

你看这是一个FIN接口

咱们一会儿可以来看一下

我先把它这个代码写上

outware的吧

我把它注入一下

然后呢这个接口的话呢

我们来看一下

它是不是就可以去调我们这个PDOMS这个服务

对吧

然后在这里边呢

你看是不是就有我们先行的这个方法

对吧

咱们现在呢

就可以去调哪个方法呢

来看一下啊

这里边的方法非常多

来找一下

slag的

找一下这里边应该调哪个方法呢

这里边方法比较多

应该是调的是一个叫做

这个方法

调用这个list的方法

然后这个方法呢

要求我们传一个这个搜索的条件过来

对吧

就是这个叫做ordersearchDTO

所以说呢我们给它传这个条件

然后呢

咱们要传的这个参数是什么呢

我们这个订单的话

一个是传这个来找一下啊

肯定是有这个组织机构

对吧

组织机构

你看啊

这里边有没有那个机构的ID

来找一下这里面东西比较多

在这儿

它继承了它

对吧

继承了它

所以我们在这个地方呢

需要传它这里边的这个

就是组织机构的ID

应该是哪个呢

就是这个叫做current什么agencyID

对吧

当前这个网点的ID

或者是其他的机构ID

那么就是这个字段

然后还有一个是什么呢

还有一个就是那个状态啊

还有一个是订单的状态

你看这个订单状态

那么如果是新订单的话呢

它这个订单状态应该是什么呢

应该是网点入库这个状态

所以我们就用这两个

用这两个条件来卡就可以了

也就是我们当前这个机构下边

并且状态是网点入库的这种订单

那么就是新订单

因为后边呢

网点入库之后呢

再往后呢

是不是就是带装车呀

什么运输中啊

网点出库啊

就是这些状态了

那么现在呢

我们要查的是网点入库这个状态啊

所以说呢

我们回到这边来

我现在是不是已经注入了这个份接口

对吧

然后呢

我是不是就可以通过调用这个什么呢

到这边来调用这个份接口

它的这个刚才看到叫做list的方法

对吧

然后呢

我们需要传一个条件进去啊

传一个条件进去

就是这个什么呢

order search

dto

咱们把它创建出来

order search dto

扭直接扭出来就可以了啊

好

OK

然后呢

把它传进去

那么我们是不是就可以得到什么呢

就可以得到我们这个所有的订单了

对吧

order list

order list

但是需要注意啊

咱们这个方法要求的返回的是这个对吧

是这个dto

所以说呢

一会还需要进行一个转换

不是直接返回这个list的

那么在这呢

这是

调用我们这个份接口

然后呢

实现什么远程调用啊

远程调用

好

查询什么呢

查询当前机构下的这个新订单

新订单

好

它这一直报错啊

我们可以先给它来个return now

让它先编译通过

那下边的话呢

我们是不是就需要来设置这个查询的条件

对吧

查询条件啊

通过这个order

什么search dto.set status

status

好

就是这个状态对吧

这个状态

然后这个状态的话呢

我们是专门定义了一个枚举啊

叫做order status

点什么呢

注意看啊

应该是这个网点入库

网点入库呢

来找一下

应该就是

那个

咱们直接到这里面来看啊

进来看

网点入库的话

是这个

好

get code

好

好

好

好

好

这就是设置什么呢

设置我们这个订单状态啊

订单状态

为什么呢

网点入库

这种状态的

好

呃

然后还有一个条件是什么呢

是不是就是我们当前这个机构的id

对吧

也就是说我们只是查我们当前这个机构下的订单

其他的订单呢

我们肯定是不查的

所以还需要再来加一个条件

set什么呢

current

set current agency id

而这个agency id呢

就是我们传过来的

这个agency id呢

好

好

就这两个条件来卡就可以了

这样的话呢

我们查出来的呢

是不是就是我们这个所需要的这个机构下边的新订单了

啊

然后呢

我们是不是就需要把这个结果呢

重新给它封装一下

封装成我们想要的这种结果

对吧

那么要进行转换的话呢

那肯定是需要便利这个粒子的集合的

对吧

哎

那么咱们可以先在这啊

来个info

来个来个log点info

嗯

那个我们没有啊

没有使用

在这儿来一个sleep for day

然后我们在这儿来记录一下

log.info

先输出一下

这是我们查询到新订单

条数

或者叫做个数

个数

然后在这个地方

可以通过这种站位符这种方式

一共查询到了多少个订单

是咱们来个orderlist.size

对吧

好

这样我们就知道

一共获取到了多少个订单

然后接下来咱们就可以来处理一下

处理它的话咱们直接使用什么

orderlist.stream

使用我们这个stream流

点什么呢

map

这里面来写一个Lambda表达式

这是我们item

来处理

完事之后

给它来个collect

的

对吧

好

,collectors.to list

转成list集合

好

然后这里边的代码其实就是什么

我们是不是需要把集合进行一个便利

然后把它最终封装成什么

封装成我们想要的这种list集合

对吧

这种list集合

所以说我们在这处理它的过程

其实就是在处理

就是在封装集合

好

那么集合的话可以怎么封装

对吧

那么我们可以使用一个构建器模式

通过builder来构建

好

这个构建器我们可以使用这个

就是咱们你看

咱们在这个DTO上是不是已经加了builder注解

对吧

所以我们在构建这个对象的时候

就可以使用它这个构建器对象了

点什么呢

builder对吧

然后把这个构建器对象

获取到

然后获取到之后

我们是不是就可以通过这个builder

然后来设置什么呢

一个是current

current agency id

current agency id

就是当前这个机构ID对吧

这个机构ID我们是不是已经传进来了

就是这个agency ID

然后其他的属性需要什么

需要在咱们这个地方来进行编写

在这里边来进行编写

然后我们每一次这个便利的时候

其实都是需要封装出来一个新的这个DTO对象

对吧

最终把它转换成list的集合

也就是说

我们最终返回结果应该就是这么一个list的集合

是这么一个效果

order-customize-dto-list

然后最终返回的呢

其实就是这个list的集合

这块这个代码写起来稍微有一点点绕啊

就是因为什么呢

我们需要这个地方

咱们是不是查出来了这么一个list集合

这块比较简单

然后再通过stream流是不是来便利这个集合

然后呢

便利它的过程当中呢

把它重新整合一下

它就会转换成一种形式

转换成这种形式

最终返回的是这个list集合

那么这个过程当中呢

我们是不是就需要封装这个对象

对吧

封装这个DTO对象

而这个DTO对象呢

是通过builder

构建器这种方式来设置的啊

然后设置的时候呢

我们来看啊

这个DTO对象里面是不是有很多属性需要去设置

这么多的属性都需要设置

对吧

包括这个什么order

对吧

都需要设置

那这样的话呢

我们就需要干什么呢

在这个地方

来通过这个构建器来设置这个DTO对象

我们就需要关系来设置builder.

你看啊

current agency ID呢就不用了

直接在前面已经设置了

对吧

因为这个每个对象呢

都是这都是一样的

然后呢

这个是order

这是原始的订单

对吧

原始订单的话呢

是不是就是我们当前这个item

这是设置原始订单

原始原始订单

好

然后还有什么呢

builder.

咱们来看啊

这个start

start agency ID

start agency ID呢

是不是应该也是我们当前这个机构

对吧

那么我们看通过它呢

能不能获得get什么呢

start

这里面是没有的

那这个呢

这个起始机构呢

其实就是我们传进来的这个agency ID

这样它才是新订单

所以这个呢

是我们的这个起始机构

起始机构

然后呢

还有一个比较关键的啊

就是这个end agency ID

但是这块呢

注意我们一会儿呢

需要去计算

因为这个中止机构对吧

或者叫做目的地

目的地这个机构

也就是我们这个目的地的那个要派送的那个网点

而这个的话呢

我们当前在订单里面是没有的

没有的

所以一会儿呢

我们需要去计算一下

根据什么算呢

其实就是根据我们这个订单

这个订单下单的时候呢

它是不是会留下那个收件人

它的详细地址对吧

所以说呢

我们一会儿就需要根据这个收件人

这个地址

然后去算出来到底应该是哪个网点

最终负责派送

那个呢就是我们这个目的地机构

所以这块呢是需要算的

那么一会儿呢

我们就需要来抽取这么一个方法

这个方法呢就是get什么呢

get这个end agency agency ID

好

就是获取对吧

然后呢把谁传进去呢

咱们可以把这个item传进去

一会儿呢就需要来编写这个方法

咱们这边呢

先给它来一个return now

保证它能编译通过

好

这是这个

然后这里边呢

再设置一个订单的类型就可以了

build.

订单类型是不是叫做order type

对吧

然后这个order type呢

我们可以通过这个item.

get order type来获得

好

就设置这几个属性就可以了

然后设置完了之后呢

别忘了return对吧

我们通过build.

build的方法

build的方法

把这个对象构建出来

你看这个build的方法

它是不是返回

就是我们这个DTO对象对吧

这样的话呢

我们这个list的编译完之后呢

最终呢

它是不是调用了collect的方法

然后呢

把我们构建的这个对象呢

一个一个封装到这个list的集合当中

那么最终呢

把这个集合返回就可以了

好

这块呢

其实就是对于我们这个数据的一个处理

好

那么关于咱们这个

获取某个机构下边新订单呢

我们先写到这

但是这呢

我们是不是留下了一个问题

就是什么呢

咱们这个方法

也就是说我们一会需要来编写这个方法

这个就是获取什么呢

获取我们这个目的

机构目的地

它的这个网点嘛

一般肯定都是网点来负责派送对吧

那个ID

而这个的话呢

就需要根据我们这个订单呢

来查询

因为我们当前数据库里面

没有去计算

所以一会我们重点来写这个方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的订单分发系统的核心服务实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何实现一个订单分类服务 `TaskOrderClassifyServiceImpl`。该服务的核心功能是根据指定的机构（`agencyId`）获取其下的所有新订单，并将这些订单按“起始机构”、“目的网点”、“订单类型”等维度进行分组封装，最终返回一个 `OrderClassifyGroupDTO` 列表。整个过程涉及服务层、数据传输对象（DTO）、枚举类、以及远程调用（Feign）等技术点，体现了典型的微服务架构中的业务逻辑处理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示项目结构，定位到 `TaskOrderClassifyServiceImpl` 类。
*   **00:05 - 00:15**: 介绍 `execute` 方法的入口，定义了 `agencyId`, `jobId`, `logId` 三个参数。
*   **00:15 - 00:25**: 定义两个 `List` 变量 `orderClassifyDTOS` 和 `orderClassifyGroupDTOS` 用于数据存储。
*   **00:25 - 00:35**: 调用 `buildNewOrder` 方法获取指定机构下的新订单列表。
*   **00:35 - 00:45**: 展示 `OrderStatus` 枚举类，定义了订单状态，如 `PENDING` (待件)、`PICKED_UP` (已取件)、`OUTLETS_SINCE_SENT` (网点自提)。
*   **00:45 - 00:55**: 在 `buildNewOrder` 方法中，创建 `OrderSearchDTO` 对象，设置状态为 `OUTLETS_WAREHOUSE`，并调用 `orderFeign.list` 远程接口获取订单。
*   **00:55 - 01:05**: 使用 `Stream` API 对订单列表进行处理，通过 `map` 和 `collect` 将订单转换为 `OrderClassifyDTO` 对象并收集到列表中。
*   **01:05 - 01:15**: 展示 `OrderClassifyDTO` 类的结构，包含 `startAgencyId`, `endAgencyId`, `orderType`, `goodsType`, `currentAgencyId` 等字段。
*   **01:15 - 01:25**: 使用 `OrderClassifyDTOBuilder` 构建器模式，为每个订单创建 `OrderClassifyDTO` 对象。
*   **01:25 - 01:35**: 展示 `getEndAgencyId` 方法，用于获取订单的目的网点ID。
*   **01:35 - 01:45**: 完成 `buildNewOrder` 方法，返回处理后的订单分组列表。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **核心代码：`TaskOrderClassifyServiceImpl.java`**
    ```java
    public class TaskOrderClassifyServiceImpl implements ITaskOrderClassifyService {

        @Override
        public List<OrderClassifyGroupDTO> execute(String agencyId, String jobId, String logId) {
            List<OrderClassifyDTO> orderClassifyDTOS = new ArrayList<>();
            List<OrderClassifyGroupDTO> orderClassifyGroupDTOS = new ArrayList<>();

            // 获取当前机构下的所有订单数据（分为新订单和中转订单）
            orderClassifyDTOS.addAll(buildNewOrder(agencyId));

            // 进行订单分类
            // 将分类结果保存到数据库

            return orderClassifyGroupDTOS;
        }

        private List<OrderClassifyDTO> buildNewOrder(String agencyId) {
            OrderSearchDTO orderSearchDTO = new OrderSearchDTO();
            // 订单状态为网点入库
            orderSearchDTO.setStatus(OrderStatus.OUTLETS_WAREHOUSE.getCode());
            orderSearchDTO.setCurrentAgencyId(agencyId);
            // 调用Feign接口实现远程调用，查询当前机构下的新订单
            List<Order> orderList = orderFeign.list(orderSearchDTO);

            Log.info("查询到新订单个数: {}", orderList.size());

            return orderList.stream().map(item -> {
                OrderClassifyDTOBuilder builder = OrderClassifyDTO.builder();
                builder.startAgencyId(agencyId); // 起始机构
                builder.endAgencyId(getEndAgencyId(item)); // 目的地机构
                builder.orderType(item.getOrderType()); // 订单类型
                builder.goodsType(item.getGoodsType()); // 商品类型
                builder.currentAgencyId(agencyId); // 当前机构
                return builder.build();
            }).collect(Collectors.toList());
        }
    }
    ```

*   **数据传输对象：`OrderClassifyDTO.java`**
    ```java
    public class OrderClassifyDTO {
        private String startAgencyId;
        private String endAgencyId;
        private Integer orderType;
        private String goodsType;
        private String currentAgencyId;

        public String groupBy() {
            if (StringUtils.isNotBlank(this.startAgencyId) && StringUtils.isNotBlank(this.endAgencyId) && StringUtils.isNotBlank(this.currentAgencyId)) {
                return this.startAgencyId + "#" + this.endAgencyId + "#" + this.currentAgencyId;
            }
            return null;
        }
    }
    ```

*   **枚举类：`OrderStatus.java`**
    ```java
    public enum OrderStatus {
        PENDING(23000, "PENDING"), // 待件
        PICKED_UP(2300, "PICKED_UP"), // 已取件
        OUTLETS_SINCE_SENT(2002, "OUTLETS_SINCE_SENT"); // 网点自提
    }
    ```

*   **远程调用接口：`OrderFeign.java`**
    ```java
    @FeignClient(value = "order-service", fallback = OrderFeignFallback.class)
    public interface OrderFeign {
        @PostMapping("/order/list")
        List<Order> list(@RequestBody OrderSearchDTO orderSearchDTO);
    }
    ```

*   **订单搜索 DTO：`OrderSearchDTO.java`**
    ```java
    public class OrderSearchDTO {
        @ApiModelProperty(value = "订单状态", required = true, example = "0")
        private Integer orderStatus;

        @ApiModelProperty(value = "客户id")
        private String memberId;

        @ApiModelProperty(value = "公用搜索字段")
        private String keyword;

        public Integer getPage() { return page == null ? 1 : page; }
        public Integer getPageSize() { return pageSize == null ? 10 : pageSize; }
    }
    ```

---

### 4) 关键场景与演示描述

1.  **场景一：服务方法入口**
    *   讲师首先展示了 `TaskOrderClassifyServiceImpl` 类中的 `execute` 方法。
    *   他解释了该方法接收三个参数：`agencyId`（机构ID）、`jobId`（定时任务ID）、`logId`（日志ID），用于标识本次订单分类操作的上下文。
    *   他定义了两个 `List` 变量，用于存储中间结果和最终结果。

2.  **场景二：构建新订单列表**
    *   讲师将光标移动到 `buildNewOrder` 方法，并开始讲解其内部逻辑。
    *   他创建了一个 `OrderSearchDTO` 对象，并将其状态设置为 `OUTLETS_WAREHOUSE`，表示查询网点入库状态的订单。
    *   他调用 `orderFeign.list` 方法，通过远程调用获取订单列表，并在控制台打印出订单数量。

3.  **场景三：Stream 流式处理**
    *   讲师使用 `Stream` API 对 `orderList` 进行处理。
    *   他通过 `map` 方法将每个 `Order` 对象转换为 `OrderClassifyDTO` 对象，并使用 `OrderClassifyDTOBuilder` 构建器模式来设置各个字段。
    *   他通过 `collect(Collectors.toList())` 将处理后的对象收集到一个列表中。

4.  **场景四：数据封装与返回**
    *   讲师展示了 `OrderClassifyDTO` 的结构，解释了 `groupBy` 方法的作用是将订单信息按机构组合成一个字符串。
    *   他演示了如何通过 `OrderClassifyDTOBuilder` 构建器来设置 `startAgencyId`、`endAgencyId`、`orderType` 等字段。
    *   最后，他将处理后的 `OrderClassifyDTO` 列表返回，作为 `execute` 方法的最终结果。

整个演示过程逻辑清晰，代码结构良好，充分展示了如何在微服务架构中实现复杂的业务逻辑。
