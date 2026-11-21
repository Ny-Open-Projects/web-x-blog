# 12-仓位总览-代理服务调用实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们要在代理服务里面去实现对持仓服务里面仓位总览接口的调用

首先咱们要去新建一个仓位服务处理器

回到工程当中

咱们在代理服务工程下面去创建一个新的处理器

Process包下面

右键New Java Class

将名称copy过来

这个就叫Stock Position Processor

点击OK

这个调用处理器要去继承抽象内AppStack的Stock Processor

实现公用接口

iBase Stock Processor

然后要将GRBC的持仓服务接口注入进来

Stock Position

这里是Service GRBC

采用组织式方式进行调用

Stock

名称叫Stock

Position

Service Blocking Start

然后加上GRBC Client的注解

名称是GRBC

Position

-Sewer

添加注释

这个是持仓服务的GRBC接口

接下来就是持仓接口的调用处理

这个呢

咱们就从代码当中直接copy进来

好

回到咱们的代码里面

Copy在这下面

上面咱们要添加对应的注写

这个是Service

添加Log波阶的日试插件

咱们再检查一下

GRBC的接口名称

咱们再调整一下

导入对应的包

这个是在Neti的包下面

好

导入完成

那咱们来看一下整理的调用实现流程

首先呢

去构造请求参数

这里的参数信息比较简单

主要传递交易信息

这个是交易账户的ID

这个是从通道反寸里面获取

可以看到

接着的话就是调用GRBC的持仓数据的获取接口

获取到持仓信息

接着的话呢

做一个便利处理

将GRBC里面接收到的持仓数据

做一个复制转换

转换为Neti传输的响应数据包

这个响应数据包的结构也是一个集合

最后

将数据信息组装为完整的返回报文

通过Channel通道将返回报文信息输出给客户端

这个就是整体的调用实现流程

接下来咱们要去扩展工厂的调用实现

咱们在这里增加一个判断

这个是GetAllPosition的接口类型

BreakProcessor

现在将刚才实现的StockOppositionProcessor注入进来

Private Ibase StockProcessor

这个名称是叫StockOppositionProcessor

添加对应的注写

Autobot的增加注释

这是持仓服务的处理器

然后将下面内容做个修改

在这里赋予给Processor

好在这里咱们就完成了工厂的扩展

接下来我们去修改工程配置

增加GRBC的持仓服务的调用配置

修改工程配置增加GRBC的持仓服务的调用配置

修改工程配置增加GRBC的持仓服务的调用配置

增加仓位服务的配置

我们先将它扩比下

保持对齐

然后在这里名称我们要调整下

改成仓位服务的名称

Protection是我的JS

地址的话呢

也要改用持仓服务的名称

好

那在这里

咱们就完成了代理服务

对仓位服务的持仓接口的调用处理

那这一讲的内容咱们就先讲到这里

我们下期再见

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock-proxy”的Java项目的技术实现讲解，核心内容是构建一个代理服务来转发客户端对持仓服务的调用。讲解者通过IDEA开发环境，逐步演示了如何创建一个`StockPositionProcessor`处理器类，该类继承自抽象基类并实现接口，用于处理“获取所有持仓”请求。它通过gRPC客户端连接到后端的持仓服务，处理请求并返回响应。视频还展示了如何通过`StockProcessorFactory`根据请求类型动态创建不同的处理器，并配置了服务的启动参数和gRPC消费者配置。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示课程大纲，当前章节为“3.4 代理服务转发调用处理”。
*   **00:05 - 00:15**: 讲解者在IDEA中打开并展示`StockPositionProcessor.java`文件，介绍其作用是处理客户端的持仓查询请求。
*   **00:15 - 00:25**: 代码演示：在`StockPositionProcessor`类中，定义了一个`@GrpcClient`注解的私有字段`stockPositionServiceStub`，用于连接gRPC服务。
*   **00:25 - 00:35**: 讲解者展示`StockPositionProcessor`类的完整结构，包括其继承关系和实现的接口。
*   **00:35 - 00:45**: 代码演示：在`processRequest`方法中，构造gRPC请求，调用`getPositions`方法，并处理返回结果。
*   **00:45 - 00:55**: 代码演示：在`processRequest`方法中，处理异常情况，包括业务异常和系统异常。
*   **00:55 - 01:05**: 讲解者切换到`StockProcessorFactory.java`文件，展示如何根据请求类型动态创建处理器。
*   **01:05 - 01:15**: 代码演示：在`StockProcessorFactory`中，通过`switch`语句根据`requestType`返回不同的处理器实例。
*   **01:15 - 01:25**: 讲解者展示`bootstrap.yml`配置文件，其中包含了服务端口、Nacos服务发现地址和RocketMQ消费者的配置。
*   **01:25 - 01:35**: 视频末尾，展示“3.5 客户端调用实现与验证”章节，预览了客户端如何调用代理服务。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT/大纲内容**:
    *   **章节标题**: “3.4 代理服务转发调用处理”。
    *   **章节标题**: “3.5 客户端调用实现与验证”。
    *   **大纲结构**: 包含“目标”、“步骤”、“实现”等标准章节。

*   **代码关键内容**:

    *   **`StockPositionProcessor.java`**:
        ```java
        @Service
        @Log4j2
        public class StockPositionProcessor extends AbstractStockProcessor implements IBaseStockProcessor {
            @GrpcClient("grpc-position-server")
            private StockPositionServiceGrpc.StockPositionServiceBlockingStub stockPositionServiceStub;
        
            @Override
            public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
                ResponseMessage responseMessage = null;
                StockHeadProto.StockHead stockHead = null;
                try {
                    // 构造请求信息
                    GetAllPositionRequest request = GetAllPositionRequest.newBuilder()
                            .setAccountId(getUserAccountId(channelHandlerContext))
                            .build();
        
                    // 调用gRPC服务
                    final GetAllPositionResponse response = stockPositionServiceBlockingStub.getAllPositions(request);
        
                    // 处理成功响应
                    if (null != response && response.getGetAllPositionDataList().size() > 0) {
                        GetAllPositionList.Builder positionListBuilder = GetAllPositionList.newBuilder();
                        for (int pos = 0; pos < response.getGetAllPositionDataList().size(); pos++) {
                            GetAllPositionData.Builder positionData = GetAllPositionData.newBuilder();
                            BeanUtils.copyProperties(response.getGetAllPositionDataList().get(pos), positionData);
                            positionListBuilder.addGetAllPositionData(positionData);
                        }
                        // 返回成功报文
                        stockHead = generateStockHead(stockMessage.getStockHead(), response.getStatus());
                        responseMessage = ResponseMessage.newBuilder()
                                .setStockHead(stockHead)
                                .setGetAllPositionList(positionListBuilder)
                                .build();
                    }
        
                    // 处理业务异常
                } catch (ComponentException e) {
                    log.error("业务异常", e);
                    stockHead = generateStockHead(stockMessage.getStockHead(), e.getErrorCodeEnum().getCode());
                    responseMessage = ResponseMessage.newBuilder()
                            .setStockHead(stockHead)
                            .setMessage(e.getErrorMessage())
                            .build();
                }
        
                // 处理系统异常
                catch (Exception e) {
                    log.error("系统异常", e);
                    stockHead = generateStockHead(stockMessage.getStockHead(), GlobalConstants.STATUS_ERROR);
                    responseMessage = ResponseMessage.newBuilder()
                            .setStockHead(stockHead)
                            .setMessage(e.getMessage())
                            .build();
                }
        
                // 写入响应
                channelHandlerContext.writeAndFlush(responseMessage);
                log.info("Process in StockPositionProcessor.processRequest write: " + responseMessage);
            }
        }
        ```

    *   **`StockProcessorFactory.java`**:
        ```java
        @Component
        public class StockProcessorFactory {
            @Autowired
            private IBaseStockProcessor stockQuoteProcessor;
        
            @Autowired
            private IBaseStockProcessor stockRecallOrderProcessor;
        
            @Autowired
            private IBaseStockProcessor stockPositionProcessor;
        
            @Override
            public IBaseStockProcessor generateStockProcessor(StockHeadProto.RequestType requestType) throws ComponentException {
                switch (requestType) {
                    case PLACE_ORDER:
                        return stockQuoteProcessor;
                    case RECALL_ORDER:
                        return stockRecallOrderProcessor;
                    case GET_POSITION:
                        return stockPositionProcessor;
                    default:
                        throw new ComponentException("不支持的请求类型: " + requestType);
                }
            }
        }
        ```

    *   **`bootstrap.yml` 配置**:
        ```yaml
        server:
          port: 10693
        spring:
          application:
            name: stock-proxy
          cloud:
            nacos:
              server-addr: 127.0.0.1:8845
              config:
                server-addr: 127.0.0.1:8845
        # RocketMQ 消费端配置
        stream:
          bindings:
            quote:
              consumer:
                # 并发数
                concurrency: 10
                # 最大尝试次数
                maxAttempts: 1
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建代理处理器**
    *   **描述**: 讲解者在IDEA中创建了一个名为`StockPositionProcessor`的Java类，该类继承自`AbstractStockProcessor`并实现了`IBaseStockProcessor`接口。通过`@GrpcClient`注解，它自动注入了gRPC客户端`StockPositionServiceBlockingStub`，用于与后端持仓服务通信。

*   **场景二：实现请求处理逻辑**
    *   **描述**: 在`processRequest`方法中，首先构造一个`GetAllPositionRequest`对象，然后调用`stockPositionServiceBlockingStub.getAllPositions()`方法向后端服务发起请求。根据返回的响应，构建一个`ResponseMessage`对象，并通过`channelHandlerContext.writeAndFlush()`将响应写回给客户端。代码中包含了对业务异常和系统异常的捕获和处理，确保服务的健壮性。

*   **场景三：动态处理器工厂**
    *   **描述**: 讲解者展示了`StockProcessorFactory`类，该类通过`@Component`注解被Spring管理。它通过`@Autowired`注入了不同类型的处理器（如`stockQuoteProcessor`、`stockRecallOrderProcessor`、`stockPositionProcessor`）。`generateStockProcessor`方法根据传入的`requestType`，通过`switch`语句动态返回相应的处理器实例，实现了请求的分发。

*   **场景四：服务配置**
    *   **描述**: 讲解者展示了`bootstrap.yml`配置文件，其中配置了服务的端口（`server.port: 10693`）、服务名（`spring.application.name: stock-proxy`）、Nacos服务发现地址以及RocketMQ消费者的并发数和最大尝试次数，为服务的启动和运行提供了必要的配置支持。
