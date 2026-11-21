# 23-简易下单功能-测试验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就开始对简易下单功能做一个完整的测试和验证

首先要启动StockDio服务

接着要启动StockFloxy代理服务

接着的话要启动NetE测试客户端

在这里要注意一下

启动的时候要将StockDio服务里面的

业务数据源的map文件扫描给注释掉

在这里面将这一段代码注释掉

因为咱们还没有实现用户的登录接口

没有去使用业务数据源

所以在这个目录下面并没有map文件

如果在这里指定配置的话呢

启动的时候会出现错误

所以咱们需要将这段代码先注释掉

咱们回到代码当中

在StockDio下面

找到业务数据源

BitSystemDataSourceConfiguration

将这一段代码SetMapLocation注释掉

测试完成之后呢

咱们再进行恢复

接着咱们就开始去启动交易服务

在启动服务之前呢

要确保相关的中间件

Nacos Ladies启动成功

好咱们启动一下交易服务

交易服务启动完成

整个过程呢没有报错

接着咱们再启动代理服务

行情代理服务呢也是成功启动

接着咱们就来启动模拟客户端

启动完模拟客户端

可以看到以下交互菜单界面

就可以通过指定进行交互操作

用户登录借口呢

在这里还没有实现

下面章节的讲解过程当中呢

会做具体的实现

咱们在这里主要是测试用户下单功能

在进行测试之前

咱们先去检查后台的数据库当中的数据

用户下单会生成订单数据

咱们在数据库当中去查看当前的订单数据信息

通过这条舌头对订单数据做一个倒序查询

咱们执行一下

肯定有价啊

执行完成

可以查看到当前最新的数据ID

是为2518

咱们记录一下

MaxID 2518

测试完成之后

咱们再做一个验证

那咱们接着就通过模拟终端

发送用户下单的指令

咱们可以看到这个握手信息呢

已经交互完成

说明WebSocket的这个长连接是有效的

那咱们在控制台

输入用户下单的指令

调机回车

咱们可以看到用户下单的数据包呢

就已经发送执行完成

这个是发送的下单参数信息

下面的是从服务端所接收的响应消息

咱们可以看到服务端的处理状态是为200

也就是说是处理成功

并且将新生成的订单ID也做了返回

咱们先不着急查看数据库的数据

先来看一下代理服务的日日输出信息

在这里面

咱们可以看到代理服务作为WebSocket的服务端

接收到客户端所发送过来的消息呢

实际上是一个班诺里的二进制的数据包

然后会经过ProBuffer解码器

将二进制数据包转换解码为咱们的自定义的消息对象

下面是代理服务的转发处理消息

咱们可以看到代理服务发送给交易服务的处理结果呢

响应状态是200

也就是说是处理成功

代理服务呢

接收到交易服务的消息

代理服务所返回的订单ID

并且呢将订单ID返回给了模拟客户端

那咱们再看一下交易服务

交易服务往上面查看

这里呢是GIPC接口的处理日志信息

接收到了对应的请求参数信息

并且将它打印出来

咱们可以看到这些参数信息

跟模拟客户端所发送的消息是一致的

好

那咱们再去查看一下数据库的数据

回到数据库当中

咱们再次查询这条社口

可以看到已经生成一条新的数据

ID为2519

好

在这里呢

咱们就完成了简易下单功能的测试和验证

下单功能咱们后续还会做完善和讲解

那这一讲内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频是关于一个名为“bulls-stock-deal”的股票交易系统的技术演示，重点在于验证其代理服务（Proxy Service）的完整性和功能性。演示者通过启动核心服务（`stock-deal`）、代理服务（`stock-proxy`）和一个基于Netty的客户端（`SimulateClient`），来模拟一个完整的交易流程。核心内容包括：
- **服务启动与配置**：演示了如何通过IDEA启动Spring Boot应用，并展示了关键的MyBatis数据源配置类 `BizSystemDataSourceConfiguration`。
- **交易流程模拟**：通过命令行客户端模拟用户登录、下单（Place Order）等操作。
- **数据验证**：在下单后，通过Navicat Premium连接数据库，查询并验证订单数据是否成功写入，从而证明整个交易链路（客户端 -> 代理服务 -> 核心服务 -> 数据库）是通顺且正确的。
- **技术栈**：主要涉及Spring Boot、MyBatis、Netty、Nacos服务注册与发现、以及PostgreSQL数据库。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各帧的时间戳，以下章节是根据画面内容和逻辑顺序进行的划分：

- **0:00 - 0:05**：视频开头，展示课程大纲（`Day13.md`），并聚焦于第3.10节“测试验证”。
- **0:05 - 0:15**：演示者在IDEA中启动 `StockDealApplication` 服务，查看控制台日志，确认服务已成功启动并初始化。
- **0:15 - 0:25**：演示者启动 `StockProxyApplication` 服务，控制台日志显示代理服务已启动。
- **0:25 - 0:35**：演示者启动 `SimulateClient`（Netty客户端），并展示其交互菜单。
- **0:35 - 0:45**：客户端执行“Place Order”操作，发送订单参数（如 `stockId`, `type`, `execPrice`）。
- **0:45 - 0:55**：在服务端控制台日志中，可以看到订单处理的详细过程，包括 `StockDealProcessor` 接收请求并处理。
- **0:55 - 1:05**：客户端收到服务器响应，显示订单已成功处理。
- **1:05 - 1:15**：演示者切换到Navicat Premium，连接数据库并执行SQL查询 `SELECT * FROM trade_order ...`，成功查到新生成的订单记录，证明交易流程成功。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容
- **课程大纲**：显示了第3章“代理服务登录鉴权实现”的详细目录，其中第3.10节为“测试验证”，是本视频的核心内容。
- **配置说明**：在IDEA中，`BizSystemDataSourceConfiguration` 类的注释中包含关键配置信息，如：
  ```text
  login-password: admin123
  # 监控后台开关，开启可通过后台管理查看
  enabled: true
  ```

#### 代码关键内容

- **数据源配置类**：`BizSystemDataSourceConfiguration.java`
  ```java
  @Configuration
  @MapperScan(basePackages = "com.itecast.bulls.stock.deal.dao.biz", sqlSessionTemplateRef = "bizSystemSqlSessionFactory")
  public class BizSystemDataSourceConfiguration {
      @Bean(name = "bizSystemSqlSessionFactory")
      public SqlSessionFactory bizSystemSqlSessionFactory(@Qualifier("bizSystemDataSource") DataSource dataSource) throws Exception {
          SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
          bean.setDataSource(dataSource);
          // 扫描mapper文件
          bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:/com/itecast/bulls/stock/deal/dao/biz/mapper/*.xml"));
          return bean.getObject();
      }

      @Bean(name = "bizSystemTransactionManager")
      public PlatformTransactionManager bizSystemTransactionManager(@Qualifier("bizSystemDataSource") DataSource dataSource) {
          return new DataSourceTransactionManager(dataSource);
      }
  }
  ```

- **服务启动日志**：
  - `StockDealApplication` 启动日志：
    ```text
    INFO 17012 --- [main] o.s.w.s.c.ServletRegistrationBean : Servlet StockDealServlet mapped to [/stock-deal]
    INFO 17012 --- [main] o.s.w.s.c.ContextLoader : Root WebApplicationContext initialized in 2202 ms
    ```
  - `StockProxyApplication` 启动日志：
    ```text
    INFO 10500 --- [main] c.i.b.s.p.StockProxyApplication : Started StockProxyApplication in 18.887 seconds (JVM running for 18.887)
    ```

- **客户端交互日志**：
  ```text
  1: User Login [用户登录]
  2: Place Order [用户下单]
  0: Exit [退出客户端]
  2: Place Order
  ====== Send Place Order, Params ======
  == direct:0
  == execPrice:655
  == volume:100
  == stockId:1
  == type:1
  == execPrice:100
  ======== Receive Server Message ========
  message: "200"
  ```

- **数据库查询语句**：
  ```sql
  SELECT * FROM trade_order ORDER BY id DESC LIMIT 10;
  ```

---

### 4) 关键场景与演示描述

- **场景一：服务启动与配置验证**
  - **描述**：演示者在IDEA中依次启动 `StockDealApplication` 和 `StockProxyApplication`。通过查看控制台日志，确认两个服务均已成功启动并初始化。重点展示了 `BizSystemDataSourceConfiguration` 类中的 `@MapperScan` 注解和 `SqlSessionFactoryBean` 的配置，说明了数据源和Mapper文件的加载方式。

- **场景二：客户端交互与订单提交**
  - **描述**：演示者启动 `SimulateClient`，在命令行界面输入“2”选择下单。客户端发送一个包含 `stockId=1`, `type=1`, `execPrice=100` 的订单请求。服务端日志显示 `StockDealProcessor` 接收并处理了该请求，返回状态码“200”，表明请求成功。

- **场景三：数据库数据验证**
  - **描述**：在订单处理完成后，演示者切换到Navicat Premium，连接到PostgreSQL数据库。执行SQL查询 `SELECT * FROM trade_order ORDER BY id DESC LIMIT 10;`，成功查到一条新的订单记录（`id=2519`），并显示了其详细信息（如 `stockId`, `execPrice`, `execTime`）。这证明了从客户端到数据库的整个交易流程是完整且正确的。

- **场景四：异常处理与日志分析**
  - **描述**：在日志中，可以看到一些关于Spring事务管理器和MyBatis SqlSession的警告信息，例如：
    ```text
    Creating a new SqlSession
    SqlSession [org.apache.ibatis.session.defaults.DefaultSqlSession@5441e6f] was not registered for synchronization because synchronization is not active
    ```
    这些信息表明在当前的事务上下文中，SqlSession没有被Spring管理，但这在非事务性操作中是正常的，不影响核心功能的验证。

---

以上是基于视频画面进行的结构化技术分析报告。
