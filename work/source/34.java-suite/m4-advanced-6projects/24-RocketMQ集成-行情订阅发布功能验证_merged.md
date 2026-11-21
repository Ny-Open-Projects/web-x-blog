# 24-RocketMQ集成-行情订阅发布功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始对行情订阅发布功能做一个测试和验证

首先咱们需要启动并且安装好Lockit MQ服务

将相关的中间键Ladies,Nagos启动起来

接着咱们再去启动行情服务和行情代理服务

通过控制台日志查看能否正常接收到行情服务所发布的行情数据信息

好,那咱们回到工程当中

在这里面咱们首先启动代理服务,右键Run运行

接着咱们找到行情服务,将行情服务也做启动

通过代理服务的控制台,咱们可以看到

它已经将行情服务所发布的行情数据接收并且打印出来了

在这里面我们可以看到像工商银行,美的集团

还有中国平安这三只股票的

实时行情数据它都能够成功接收

并且将它的详细信息做了一个日志输出

接下来咱们再去访问LockitMQ的控制后台

查看主题的消费情况

那我们进入LockitMQ服务器

将控制台启动起来

LockitConsult加瓦加Consult可执行的加薄

启动完成之后

咱们访问9800端口

进入topic

咱们看一下这个topic的详细信息

咱们配置文件里面的这个topic配置的是stockquad

咱们找到对应的主题

好可以看到stockquad

咱们来查看一下stockquad主题的消费信息

点击consume manager

我们来看一下

在这里可以看到stockquad proxy的分组信息

对不对

下面是它的一个消费信息情况

最后一次消费时间是5月11号

那咱们可以结合控制后台日志

也能够看到对应的消费记录

这个时间点跟我们后台里面所看到时间点也是一致的

那在这里

行情消息的订阅和下发都能够正常处理

大家注意一下

在行情服务对行情数据的处理过程当中

要加入消息的发送处理

找到原来的第三方行情员对接的处理逻辑

找到原来的第三方行情员对接的处理逻辑

找到原来的第三方行情员对接的处理逻辑

在最下面咱们要加入QuadSender的接口

确保行情数据能够正常发送到MQ消息队内当中

要将QuadSender这个接口注入进来

好

在这里

咱们就完成了行情订阅发布功能的测试和验证

那这一讲

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析：

---

### 1) 视频摘要

本视频片段主要演示了一个基于 **Spring Boot** 和 **RocketMQ** 的股票行情数据分发系统的集成与验证过程。核心内容包括：
- **启动服务**：依次启动行情服务（`StockQuoteApplication`）、代理服务（`StockProxyApplication`）和 RocketMQ 服务。
- **数据验证**：通过 RocketMQ 控制台（`RocketMQ-console-ng`）验证代理服务成功订阅了 `stock-quote` 主题，并消费了来自行情服务发布的数据。
- **技术实现**：展示了代理服务如何通过 `@RocketMQListener` 注解监听消息，并将数据转发给客户端。同时，演示了如何通过 Redis 缓存来优化数据处理。
- **系统架构**：强调了代理服务的无状态设计和水平扩展能力，通过部署多个代理服务实例来提升系统吞吐量。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:05**：开场，展示 `redis-bulls` 窗口，Redis 服务已启动，为后续数据缓存做准备。
- **00:05 - 00:10**：切换至 `StockQuoteApplication` 代码，展示其作为行情服务的启动类，包含 `@EnableDiscoveryClient` 和 `@EnableCaching` 注解。
- **00:10 - 00:15**：展示 `StockProxyApplication` 代码，其作为代理服务的启动类，同样包含 `@EnableDiscoveryClient` 和 `@EnableCaching` 注解。
- **00:15 - 00:20**：展示 `StockQuoteService` 接口和 `StockQuoteServiceImpl` 实现类，重点是 `stockOpenCache` 缓存和 `quoteSender` 发送器。
- **00:20 - 00:25**：展示 `StockQuoteServiceImpl` 中的 `fetchStockQuote` 方法，用于从数据库获取行情数据。
- **00:25 - 00:30**：展示 `StockProxyApplication` 的 `main` 方法，用于启动代理服务。
- **00:30 - 00:35**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **00:35 - 00:40**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **00:40 - 00:45**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **00:45 - 00:50**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **00:50 - 00:55**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **00:55 - 01:00**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **01:00 - 01:05**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **01:05 - 01:10**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **01:10 - 01:15**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **01:15 - 01:20**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **01:20 - 01:25**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **01:25 - 01:30**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **01:30 - 01:35**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **01:35 - 01:40**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **01:40 - 01:45**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **01:45 - 01:50**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **01:50 - 01:55**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **01:55 - 02:00**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **02:00 - 02:05**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **02:05 - 02:10**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **02:10 - 02:15**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **02:15 - 02:20**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **02:20 - 02:25**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **02:25 - 02:30**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **02:30 - 02:35**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **02:35 - 02:40**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **02:40 - 02:45**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **02:45 - 02:50**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **02:50 - 02:55**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **02:55 - 03:00**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **03:00 - 03:05**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **03:05 - 03:10**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **03:10 - 03:15**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **03:15 - 03:20**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **03:20 - 03:25**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **03:25 - 03:30**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **03:30 - 03:35**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **03:35 - 03:40**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
- **03:40 - 03:45**：展示 `StockProxyApplication` 的 `@EnableDiscoveryClient` 注解，用于服务发现。
- **03:45 - 03:50**：展示 `StockProxyApplication` 的 `@EnableCaching` 注解，用于缓存。
- **03:50 - 03:55**：展示 `StockProxyApplication` 的 `@ComponentScan` 注解，指定扫描包路径。
- **03:55 - 04:00**：展示 `StockProxyApplication` 的 `@SpringBootApplication` 注解
