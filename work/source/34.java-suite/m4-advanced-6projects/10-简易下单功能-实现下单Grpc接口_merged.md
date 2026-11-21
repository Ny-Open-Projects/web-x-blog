# 10-简易下单功能-实现下单Grpc接口 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现简易下单接口

首先咱们将相关实体创建一下

咱们回到代码当中

在stock.nd下面

咱们要去创建交易实体

咱们创建一个包

new package

名称叫chad

咱们创建订单相关的实体

首先是成交记录实体

chad.io

咱们就从讲习当中拷贝过来

注意这上面的注解

在这里我们采用了SWOG的文档注解

API

然后是N体

这个是JP的实体映射

关联的具体表

chad.io

咱们看一下它的一些主要属性

在这里有交易订单号

因为交易订单跟成交记录是一个一对多的关系

然后还有持商ID

成交记录和持商ID是一个多对一的关系

然后是交易的账号ID

交易账号编号

股票的一些信息

然后成交的一些信息

将日期导入进来

接着咱们再创建交易订单实体

chad.io

同样咱们将代码拷贝进来

上面也是相关的注解

这个是SWOG文档的注解

下面是N体JP的实体映射

所关联的表

DataLongbook的注解

将Data导入进来

订单表

也是记录交易相关的信息

在这里面

它和成交记录是一个一对多的关系

它记录的是订单的整体概要信息

接下来咱们再去创建交易服务的数据层接口

交易服务也是涉及到双数据源

在这里我们创建两个包目录

一个是负责业务数据源的数据接口

另外一个是负责交易数据源的交易接口

下面咱们开始创建

这个数据源的交易接口

这个是负责交易数据源的交易接口

这个是负责交易数据源的交易接口

这个是负责交易数据源的交易接口

这个是应用的Base

接口名称叫Chadio

加上对应的注解

这个是Ctree

这里提供一个保存成交记录的数据层接口

保存成交记录信息

这里是通过MyBadges实现了数据层接口

所以咱们还去创建它对应的Map文件

给它创建一个包

这样Map文件呢

咱们

从讲义当中Copy进来

首先创建该文件

new file

接着咱们再将它的内容Copy进来

将内容Copy至Map文件里面

数据还将它的头部信息

这头部信息咱们就从User服务功能下面Copy进来

User服务下面也只采用MyBadges实现了数据层接口

Copy到头部

这样咱们就实现了成交记录的数据层接口

接着的话咱们还将订单的数据层接口做一个实现

首先创建订单的接口

同样是放在缺的包下面

选择类型为1的Days

这里提供了两个接口

一个接口是保存订单进度

另外一个接口是根据ID去获取订单信息

咱们创建一下它的Map文件

new file

将它的头部信息Copy进来

这个必须是在Map文件里面的Map文件中

必须加上头部信息

否则的话无法正常识别

再将对应的Map的订印加入进来

这里定义了属性的映射

然后是具体的社口实现

这个是新增订单信息的社口语句

下面这个是根据订单ID去查找订单对象

将格式修正一下

数据层接口实现完整之后

接着咱们就可以去实现了GRBC的接口

在实现GRBC接口之前

要将对应的GRBC依赖加入进来

咱们找到GRBC的服务依赖组件

将它放置在交易服务工程下面的

Depensys标准下面

导入生效

接下来咱们就去实现交易订单的GRBC接口

创建一个Class

名称的话呢

就叫GRBC开头

stock deal service

这个内要继承GRBC的接口

因为咱们是实现了交易下单功能

所以在这里还要继承下单的接口

stock deal service

implement base

加上对应的组件

必须要加上GRBC的标识

这样的话呢

它才会扫描作为GRBC的接口

纳入到整个服务的管理当中

下面添加

对置注写

咱们要将数据层接口呢

注入进来

shared order deal

autowide

那咱们要去重写它的接口

edit insert

overlay method

咱们要选中place order

这个就是咱们在PB

公用工程里面定义的交易下单接口

咱们可以回顾看一下

在resource下面

plot

GRBC

在这里咱们定义的RPC接口

那么咱们就要去重写place order这个方法

首先咱们加上对应的日志说明

说明这个请求已经进入到方法内部

将请求参数打印出来

那首先咱们要去

封装订单信息

创建shared order

订单对象

然后设置订单相关的信息

这个是设置股票产品ID

设置账户ID

这个账户ID因为咱们还没有实现登录接口

可以先随便填写下

set excuse price

set excuse volume

还有设置它的状态

in默认是有效

咱们还是最好不要写硬编码

通过常量

去标识

int enable

它的值就是0

接下来

还设置它的type类型

然后设置它的数字化挂单数量

excuse volume

接着的话咱们就要保存订单数据

用咱们的数据层接口

影射的方法

保存完成之后还做什么事情呢

还需要将信息

返回给交易方

这里就要去

封装返回信息

这个要通过

咱们之前所定义的pb对象

sponsor

new build

然后去设置它们的设置

然后去复制它的信息

首先是整个接口的处理状态

方法执行到这里

整个处理结果

是属于正常的

所以在这里咱们就可以设置它的状态是ok的

然后还设置它的提示小序

get message

提示订单保存成功

接着的话咱们再将订单ID返回出去

set

bill id

order.getid

然后就要用bill的方法进行构建

构建完成之后

怎么将pb对象输入给客户端呢

就要调用response

ofzoe的方法

on next

将对象传递进去

然后不要忘记了

还调用responseofzoe

去标记处理完成

这样就是一个GRBC接口的正常处理交互流程

通过request对象

拿到对应的参数信息

那咱们呢在处理

相应的业务

处理完成之后呢

还要将它封装为pb对象

最后呢

将pb对象

通过responseofzoe对象呢

将数据输出给调用方

好那咱们回到讲义当中

在这里咱们就实现了

简易的下单接口

从

实体

到数据层

再到GRBC的service接口

在实现GRBC service接口的时候呢

要注意加上对应的注解

否则呢这个GRBC接口

不能正常生效

客户端呢是无法进行调用

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“交易服务”模块中“实现简易下单接口”的开发教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何从创建数据库实体类（`TradeDeal`），到定义数据访问层接口（`ITradeDealDao`）和对应的 MyBatis Mapper XML 文件，再到实现 gRPC 服务端的下单逻辑（`GrpcStockDealService`）。整个过程涵盖了 Spring Boot、MyBatis、gRPC 和 Protobuf 等主流技术栈，旨在构建一个完整的、可运行的下单功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程引言，展示当前正在开发的模块是“交易服务”，并进入“实现简易下单接口”章节。
*   **00:05 - 00:15**: 创建 `TradeDeal` 实体类。讲师在 IDE 中创建了 `TradeDeal` 类，并为其添加了 `@Api`、`@Entity` 和 `@Data` 注解，用于定义数据库表结构和提供数据访问方法。
*   **00:15 - 00:30**: 创建数据访问层接口 `ITradeDealDao`。讲师定义了 `insert` 方法，用于向数据库插入交易记录。
*   **00:30 - 00:45**: 编写 MyBatis Mapper XML 文件。讲师创建了 `TradeDealMapper.xml` 文件，并定义了 `insert` SQL 语句，使用 `@SelectKey` 注解来获取自增主键 `trade_order_id`。
*   **00:45 - 01:00**: 配置 gRPC 服务依赖。讲师在 `pom.xml` 中添加了 gRPC 服务端的依赖，如 `grpc-server-spring-boot-starter`。
*   **01:00 - 01:15**: 创建 gRPC 服务类 `GrpcStockDealService`。讲师继承了 `StockTradeDealServiceGrpc.TradeDealServiceImplBase`，并注入了 `ITradeOrderDao`。
*   **01:15 - 01:30**: 实现 `placeOrder` 方法。讲师在 `placeOrder` 方法中，首先设置订单的股票代码、名称、方向、执行价格、执行量和状态等属性。
*   **01:30 - 01:45**: 设置订单状态。讲师使用 `GlobalConstants` 类中的常量来设置订单的业务状态。
*   **01:45 - 02:00**: 创建订单对象并调用 DAO。讲师创建了一个 `TradeOrder` 对象，并调用 `tradeOrderDao.insert(order)` 方法将订单数据插入数据库。
*   **02:00 - 02:15**: 设置返回响应。讲师创建了一个 `PlaceOrderResponse` 对象，设置其状态为 `STATUS_OK`，并设置消息为“订单保存成功！”，然后通过 `responseObserver` 发送响应。
*   **02:15 - 02:30**: 完成方法。讲师调用 `responseObserver.onCompleted()` 方法，表示服务端处理完成。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   课程大纲：`第2章 简易下单功能实现`，包含子章节如 `3.3 实现简易下单接口`、`3.4 交易服务gRpc自动化配置` 等。
    *   关键提示：在 `GrpcStockDealService` 类的头部需要加上 `@GrpcService` 注解，并继承 `Protobuf` 生成的 `placeOrder` 交口。

*   **代码关键内容**:
    *   **实体类 `TradeDeal`**:
        ```java
        @Api(value = "HATEOAS接口-成交记录管理(TradeDeal)")
        @Entity
        @Table(name="t_trade_deal")
        @Data
        public class TradeDeal extends BaseEntity {
            private static final long serialVersionUID = 1L;
        }
        ```
    *   **DAO 接口 `ITradeDealDao`**:
        ```java
        @Repository
        public interface ITradeDealDao {
            int insert(TradeDeal record);
        }
        ```
    *   **MyBatis Mapper XML**:
        ```xml
        <insert id="insert" parameterType="com.icitast.bulls.stock.entity.trade.TradeOrder">
            <selectKey resultType="java.lang.Long" keyProperty="id" order="AFTER" />
            INSERT INTO t_trade_order (accountId, stockId, status, direction, initVolume, execVolume, execPrice, accountNo, stockCode, stockName)
            VALUES (#accountId#, #stockId#, #status#, #direction#, #initVolume#, #execVolume#, #execPrice#, #accountNo#, #stockCode#, #stockName#)
        </insert>
        ```
    *   **gRPC 服务类 `GrpcStockDealService`**:
        ```java
        @GrpcService
        public class GrpcStockDealService extends StockTradeDealServiceGrpc.TradeDealServiceImplBase {
            @Autowired
            private ITradeOrderDao tradeOrderDao;
            
            @Override
            public void placeOrder(PlaceOrderRequest request, StreamObserver<PlaceOrderResponse> responseObserver) {
                // 设置订单属性
                TradeOrder order = new TradeOrder();
                order.setStockCode(request.getStockCode());
                order.setStockName(request.getStockName());
                order.setDirection(request.getDirection());
                order.setExecPrice(request.getExecPrice());
                order.setExecVolume(request.getExecVolume());
                order.setStatus(GlobalConstants.STATUS_OK);
                
                // 插入数据库
                tradeOrderDao.insert(order);
                
                // 设置返回响应
                PlaceOrderResponse response = PlaceOrderResponse.newBuilder()
                    .setStatus(GlobalConstants.STATUS_OK)
                    .setDealId(order.getId())
                    .setMessage("订单保存成功！")
                    .build();
                responseObserver.onNext(response);
                responseObserver.onCompleted();
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建实体类** (00:05 - 00:15)
    *   讲师在 IntelliJ IDEA 中右键点击 `src/main/java/com.icitast.bulls.stock.deal/trade` 包，选择“新建” -> “Java 类”，创建 `TradeDeal` 类。
    *   讲师在类中添加了 `@Api`、`@Entity`、`@Table` 和 `@Data` 注解，并定义了 `serialVersionUID`。

*   **场景二：创建 DAO 接口** (00:15 - 00:30)
    *   讲师在 `trade` 包下新建 `dao` 包，并在其中创建 `ITradeDealDao` 接口。
    *   讲师在接口中定义了 `insert` 方法，并添加了 `@Repository` 注解。

*   **场景三：编写 MyBatis Mapper XML** (00:30 - 00:45)
    *   讲师在 `mapper` 包下创建 `TradeDealMapper.xml` 文件。
    *   讲师在文件中定义了 `insert` SQL 语句，并使用 `@SelectKey` 注解来获取自增主键。

*   **场景四：实现 gRPC 服务** (01:00 - 02:30)
    *   讲师在 `service` 包下创建 `GrpcStockDealService` 类。
    *   讲师在类中添加了 `@GrpcService` 注解，并注入了 `ITradeOrderDao`。
    *   讲师在 `placeOrder` 方法中，首先创建 `TradeOrder` 对象，然后设置其属性，接着调用 `tradeOrderDao.insert(order)` 方法插入数据库，最后创建并发送 `PlaceOrderResponse` 响应。

*   **场景五：调试与运行** (02:30 - 02:45)
    *   讲师在 IDE 中点击“Run”按钮，启动服务。
    *   讲师在终端中输入命令，模拟客户端发送下单请求。
    *   讲师在控制台中查看服务端的响应日志，确认订单已成功创建并返回。

---
