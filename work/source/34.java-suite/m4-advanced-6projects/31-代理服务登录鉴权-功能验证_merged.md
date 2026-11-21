# 31-代理服务登录鉴权-功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对代理服务登录健全功能做一个测试和验证

在做验证之前

咱们要去修改模拟客户端

实现用户登录接口请求数据包的封装

并且要去增加菜单的交互操作指令

好那咱们回到代码当中

在Proxy工程下面

找到咱们的模拟客户端的实现代码

在Business Handle下面

咱们去封装一个用户登录的接口

Public

Void

UseLogic

添加注释

这个是用户登录接口

给它设置请求参数信息

登录账号呢

咱们去采用Admin

UsePassword呢

也是一样的

也是Admin

然后咱们将参数信息打印出来

Send

Use

Login

Therameters

打印用户账号

打印用户账号

打印用户密码

然后呢去构造它的头部信息

Stalk

Head Proto

通过PB去创建对应的信息

设置它的虚拟号

Sequence ID

自证方式

设置呢它的请求接口类型

从每一句当中获取

UseLogin

该用Build的方法进行构建

接下来咱们再去构造

用户登录接口的请求数据包

Login Date

设置用户的账号

设置用户密码

该用Build的方法进行构建

接下来呢就要去组装

请求消息包

Stalk Message

Set Stock Head

将头部信息传递进去

将请求参数体呢

传入进去

Login Date

该用Build的构建方法

最后呢就要发送消息

至服务端

通过Send Message方法

将Stalk Message的信息

传入到户端

将Stalk Message请求消息传递进去

接下来咱们再去完成

菜单的交付指定操作

这里呢就调用刚才所实现的

用户登录接口

UseLogin

好咱们再回到讲义当中

测试接口咱们就已经实现完成

这里呢我们增加了一个

用户登录接口的封装处理

然后我们看一下

整体的模拟测试流程是怎样的

在用户连接建立成功之后

咱们先发送下单的请求

这个时候直接发送下单请求

是不能通过登录健全的处理

它应该会返回一个错误提示信息

接着咱们再去发送

用户登录的接口请求

然后再去尝试发送下单请求

通过日志来观察

这两种交互流程有没有区别

验证代理服务的登录健全功能

是否正常生效

在进行测试验证之前

先将中间键启动起来

Nagos Ladies

然后启动下单请求

然后再去发送下单请求

这个时候直接发送下单请求

是不能通过登录健全的处理

然后启动咱们的交易服务

代理服务

以及模拟客户端

让咱们回到工程当中

在这里面

咱们就开始去启动交易服务

找到Stock User

找到Stock Deal Application

右键Long运行

正在启动交易服务

大家注意一下

交易服务的启动

要将业务数据源

Map的扫描路径

这一段配置正确

之前咱们已经注释了

在这里启动的时候

咱们已经实现了

业务数据源的接口

所以要将这一段功能进行开启

否则用户登录功能

是没法正常使用

交易服务就已经启动完成

接着咱们再去启动代理服务

整个服务的启动过程当中

可能还会出现

各种各样的一些细节问题

大家要学会去排查处理

提升自己的问题解决能力

在实际工作当中

可能会碰到更加复杂的一些问题

好 代理服务也已经启动成功

接着咱们就来看看

接下来启动模拟客户端

咱们按照预期的测试流程

先直接输入用户下单的指令

可以看到

它已经返回了健全的提示消息

提示咱们用户没有登录

或者是已经过期

需要重新进行登录

接着咱们就进行正常流程的测试

首先发起用户登录指令

可以看到服务端返回用户登录成功

接着咱们再发送一个用户下单的指令

好 用户下单指令服务端

也能够接收处理成功

返回了订单的ID给我们

咱们可以去查看代理服务的日志

在这里它抛出了登录健全的提示信息

也说明能够正常进行拦截控制

再看一下交易服务

交易服务的用户登录接口也是处理成功

这里日志并没有爆出异常

好 在这里咱们就完成了

用户代理服务登录健全功能的测试验证

咱们回到讲义当中

整个测试咱们也是按照预计的流程进行了验证

通过异常流以及正常流做了验证

服务端的处理也是正常符合咱们的预期

订单数据咱们在这里就不再查看

之前咱们对简易下单功能也是做了测试和验证

好 这一讲的内容咱们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于“代理服务登录鉴权”技术实现的课程演示。主要内容围绕如何在基于 Netty 的长连接通信架构中，通过一个代理服务（Proxy）来拦截并验证客户端的登录请求。演示过程包括：修改客户端的 `ClientBoundHandler` 类以处理连接激活事件；在业务处理器 `BusinessHandler` 中构造并发送登录请求（包含用户凭证和订单信息）；在服务端配置双数据源和事务管理器；最后，通过模拟客户端发送请求并观察服务端日志与数据库结果，验证鉴权逻辑的正确性。整个过程旨在展示如何实现一个安全、可控的用户登录和订单处理流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示课程大纲，当前章节为“3.4 测试验证”。
*   **00:00:05 - 00:00:15**：进入“3.4 测试验证”章节，首先展示 `ClientBoundHandler` 类的代码，用于处理客户端连接激活事件。
*   **00:00:15 - 00:00:30**：切换到 `BusinessHandler` 类，演示如何构造用户登录请求。首先定义用户名和密码，然后使用 `StockHeadProto.StockHead.newBuilder()` 构造请求头。
*   **00:00:30 - 00:00:45**：继续在 `BusinessHandler` 中，使用 `LoginData.newBuilder()` 构造登录数据，并最终使用 `StockMessage.newBuilder()` 将登录头和登录数据封装成一个完整的请求消息。
*   **00:00:45 - 00:01:00**：展示 `ClientBoundHandler` 中的 `channelActive` 方法，用于模拟客户端的交互菜单，其中包含调用 `businessHandler.userLogin()` 的逻辑。
*   **00:01:00 - 00:01:15**：切换到 `biz-system-data-source` 模块，展示 `BizSystemDataSourceConfiguration` 类，配置了 `DataSourceTransactionManager` 和 `SqlSessionTemplate`。
*   **00:01:15 - 00:01:30**：在 `BizSystemDataSourceConfiguration` 中，配置了 `SqlSessionFactory` 和 `SqlSessionTemplate`，并指定了 `@MapperScan` 的包路径。
*   **00:01:30 - 00:01:45**：启动服务端应用，观察控制台日志，显示服务已启动并进入“strict repository configuration mode”。
*   **00:01:45 - 00:02:00**：模拟客户端发送登录请求，服务端日志显示收到登录请求，但因用户未登录而返回错误码 300。
*   **00:02:00 - 00:02:15**：再次发送登录请求，服务端日志显示登录成功。
*   **00:02:15 - 00:02:30**：发送下单请求，服务端日志显示成功获取订单 ID 为 4。
*   **00:02:30 - 00:02:45**：展示数据库查询结果，确认订单 ID 为 4 的记录已成功插入。
*   **00:02:45 - 00:03:00**：视频结尾，总结用户鉴权功能已成功实现。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.4 测试验证`。
    *   **关键结论**：`符合预期，用户鉴权功能已成功生效。`
    *   **日志分析**：`可以看到三次请求，第一次返回错误码300，要求重新登陆；第二次用户登陆请求成功；第三次再次发送下单请求，成功获取订单为4的ID。`
    *   **数据库截图**：展示了一个包含 `id`, `stockid`, `status`, `type`, `direction`, `involume`, `execvolume`, `execprice`, `execetime` 等字段的表格，其中 `id=4` 的记录被高亮显示。

*   **代码关键内容**：

    *   **`ClientBoundHandler` 类**：
        ```java
        public class ClientBoundHandler extends SimpleChannelInboundHandler<ResponseMessage> {
            @Override
            public void channelActive(ChannelHandlerContext ctx) {
                System.out.println("========== Server Connected");
                // 模拟客户端菜单
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        // ... 省略菜单逻辑 ...
                        if ("1".equalsIgnoreCase(command)) {
                            businessHandler.userLogin();
                        } else if ("2".equalsIgnoreCase(command)) {
                            businessHandler.placeOrder(command);
                        } else if ("m".equalsIgnoreCase(command)) {
                            showMenu();
                        } else {
                            System.out.println("Unrecognized Command!");
                        }
                    }
                }).start();
            }
        }
        ```

    *   **`BusinessHandler` 类**：
        ```java
        public void userLogin() {
            String userNo = "admin";
            String userPwd = "admin";
            System.out.println("******* Send User Login, Parameters *******");
            System.out.println("= userNo: " + userNo);
            System.out.println("= userPwd: " + userPwd);

            // 构造请求头
            StockHeadProto.StockHead stockHead = StockHeadProto.StockHead.newBuilder()
                .setSeqId(seqId++)
                .setStockId(1)
                .build();

            // 构造登录数据
            LoginData loginData = LoginData.newBuilder()
                .setUserNo(userNo)
                .setUserPwd(userPwd)
                .build();

            // 组装请求数据包
            StockMessage stockMessage = StockMessage.newBuilder()
                .setStockHead(stockHead)
                .setLoginData(loginData)
                .build();
        }
        ```

    *   **`BizSystemDataSourceConfiguration` 类**：
        ```java
        @Configuration
        @MapperScan(basePackages = "com.icast.bulls.stock.deal.dao", sqlSessionTemplateRef = "bizSystemSqlSessionTemplate")
        public class BizSystemDataSourceConfiguration {
            @Bean(name = "bizSystemSqlSessionFactory")
            public SqlSessionFactory bizSystemSqlSessionFactory(@Qualifier("bizSystemDataSource") DataSource dataSource) {
                SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
                bean.setDataSource(dataSource);
                bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources(locationPattern));
                return bean.getObject();
            }

            @Bean(name = "bizSystemSqlSessionTemplate")
            public SqlSessionTemplate bizSystemSqlSessionTemplate(@Qualifier("bizSystemDataSource") DataSource dataSource) {
                return new SqlSessionTemplate(bizSystemSqlSessionFactory(dataSource));
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：客户端连接激活与菜单模拟**
    *   **描述**：演示者在 `ClientBoundHandler` 中重写了 `channelActive` 方法，用于在客户端连接成功后，启动一个新线程来模拟用户交互菜单。菜单包含“1. 用户登录”、“2. 下单”等选项。
    *   **技术点**：展示了如何在 Netty 服务端处理客户端连接事件，并通过线程模拟用户操作。

*   **场景二：构造并发送登录请求**
    *   **描述**：在 `BusinessHandler` 中，演示者通过 `StockHeadProto.StockHead.newBuilder()` 和 `LoginData.newBuilder()` 构造了请求头和登录数据，并最终封装成 `StockMessage` 对象。
    *   **技术点**：展示了如何使用 Protocol Buffers（.proto）生成的 Java 类来构建和发送结构化数据包。

*   **场景三：服务端日志与数据库验证**
    *   **描述**：演示者启动服务端应用后，模拟客户端发送登录和下单请求。服务端日志显示了三次请求的处理过程：第一次因未登录返回错误码 300，第二次登录成功，第三次下单成功并返回订单 ID 4。
    *   **技术点**：通过日志和数据库查询结果，验证了用户鉴权和业务逻辑的正确性。

*   **场景四：双数据源配置**
    *   **描述**：演示者展示了 `BizSystemDataSourceConfiguration` 类，其中配置了 `DataSourceTransactionManager` 和 `SqlSessionTemplate`，并使用 `@MapperScan` 注解扫描 DAO 接口。
    *   **技术点**：展示了如何在 Spring Boot 项目中配置数据源和事务管理器，支持多数据源场景。

*   **场景五：最终验证与总结**
    *   **描述**：视频最后，演示者通过 PPT 展示了数据库中订单 ID 为 4 的记录，并总结“用户鉴权功能已成功生效”。
    *   **技术点**：通过最终的验证结果，确认了整个鉴权和
