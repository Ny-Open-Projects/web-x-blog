# 10-账户预警通知-账户预警通知gRpc接口实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始讲解去实现账户预警通知的设置接口

每个用户都可以设置自己的预警条件

触发相应的通知

预警通知可以支持APP的战略性

邮件或者短信方式

通知方式也可以由用户自己选择

但是必须根据实际信息来选择相应的通知方式

比如说有的用户他没有手机信息

这个时候你就不能去选择短信的通知方式

你没有填写邮箱

那么就不能选择邮件的通知方式

这点大家要注意一下

接下来我们来看一下表的具体结构

账户预警通知设置表

这里有账户的ID

股票产品ID

也就是说你要针对哪只股票产品

去设置止损和止盈的条件

下面是stop late

止盈止损的设置比例

目前咱们是根据比例的方式来设置止盈止损

如果大家要根据价格的方式去设置

那么再扩展一个支段去做相应的记录就可以

下面是用户的预警通知方式

在这里咱们可以支持站内信

邮件还有短信的方式

然后是操作时间的记录

这个是生成的实体对象结构

和上面的表结构属性信息是一致的

接下来咱们就去定义

ProBuff数据的传输结构

首先去定义内体的对外传输数据结构

这里我们将定义的脚本做个引用

回到工程当中

定位到stock message

咱们将账户预警通知设置的传输数据结构定义在下面

这个响应的数据体先定义在这里

内部属性暂时为空

如果将来要返回账户的数据结构

我们就把这个数据的设置

返回账户预警通知的ID

那么可以填写在这里

接着我们将数据的请求结构加入到stock message当中

添加注释

这个是账户预警通知设置接口

给它一个序号

接下来我们要去修改reports message

响应数据包

添加注释

这个是账户预警通知设置的返回数据包

它返回的对象是account

1 setting response

给它一个序号

好

那里程的传输数据结构

咱们就已经定义完成

请求包所要传递的信息

咱们可以看到有股票的产品ID

预警的类型

止盈止损的设置比例

以及通知方式

这些都是必要信息

大家注意一下止盈止损的设置比例

它的单位是百分号

如果在这里它设定的值为2.28

那它代表的意思就是2.28%

接下来咱们去定义GRBC的对内传输数据结构

咱们将它的包结构做一个copy

回到工程当中

用户预警通知设置接口是放在用户服务下面

咱们把数据结构定义在stock

user service proto文件里面

这个是请求的数据结构

下面是返回的数据结构

请求数据结构和neti定义的对外传输的请求数据结构

基本上是一致的

这里面增加了账户ID的传递

然后下面是返回的数据结构

这里只要返回处理的状态以及响应消息就可以

接下来我们还要去定义一个账户预警通知设置的RPC接口

添加注释

这个是账户预警设置接口

定义RPC

account

warn

setting

定义请求参数

returns

定义响应的包结构

setting

response

接着的话我们通过PB脚本来生成对应的Java代码

右键open in Tomino

生成GRPC的Java代码

再生成neti的传输数据结构代码

都已经生成完成

咱们来刷新检查一下

neti层的传输数据结构已经生成成功

咱们再检查一下GRPC的传输数据结构

这里也已经成功生成对应的Java代码

那接下来咱们就在交易服务里面去实现账户预警通知设置的GRPC接口

外层GRPC的处理比较简单

咱们直接把它copy到工程当中

找到交易服务

Postdoc.io

进入用户服务的GRPC接口

咱们在最下面添加相应的代码

这里需要定义一个用户服务接口

那咱们在service里面去创建一个纸包

这个包名叫user

专门负责用户相关接口的处理

在这里定义一个接口

接口名称叫ichad

user service

点击OK

接下来咱们再去创建它的实现类

右键new

加class

实现类就叫chaduser service

implement

它要去实现咱们刚才定义的接口

ichaduser service

咱们再回到GRPC接口层

将刚才定义的service注入进来

private

ichaduser service

添加autowide注解

添加注释

这个是用户服务层接口

再回到刚才的GRPC接口

咱们在这里去添加对应的方法

great method

添加注释

这个接口是保存用户设置的预警信息

咱们再增加业务异常的抛出

sluice onpander exception

copy注释

在实现类当中去实现该接口

添加对应的注释

添加service注解

在下一讲咱们再去做业务层的实现

在这里咱们就完成了账户预警通知设置的传输数据结构的定义

以及GRPC接口层的实现

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程聚焦于一个金融交易系统的“账户预警通知设置”功能的实现。讲师通过讲解和代码演示，系统性地介绍了从需求分析、数据模型设计、接口定义（使用 gRPC 和 Protocol Buffers）、到服务层和数据访问层的完整开发流程。核心内容包括：
*   **功能目标**：允许用户设置账户预警条件（如止损止盈比例），并选择通知方式（APP、邮件、短信）。
*   **技术栈**：使用 Java + Spring Boot + gRPC + Protocol Buffers + MySQL。
*   **核心步骤**：
    1.  **数据模型**：设计 `t_account_warn_setting` 数据表，定义账户ID、预警类型、止损止盈比例、通知方式等字段。
    2.  **接口定义**：在 `.proto` 文件中定义 `StockUserService` 服务及 `AccountWarnSettingRequest` 和 `AccountWarnSettingResponse` 消息结构。
    3.  **代码生成**：使用 `protoc` 工具将 `.proto` 文件编译为 Java 代码。
    4.  **服务实现**：在 `GrpcStockUserService` 中实现 `accountWarnSetting` 方法，调用数据访问层 `ITradeAccountDao` 保存设置。
    5.  **异常处理**：在服务层处理异常，并通过 `responseObserver` 返回响应给客户端。

整个过程体现了微服务架构下，如何通过定义清晰的接口和数据结构，实现不同模块间的协作。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的视频时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：课程开场，介绍本章目标：实现账户预警通知设置接口。
*   **00:30 - 01:00**：讲解数据库设计，展示 `t_account_warn_setting` 表的结构，包括 `id`, `accountId`, `warnType`, `stopRate`, `notifyType` 等字段。
*   **01:00 - 01:30**：定义 gRPC 服务接口，展示 `StockUserService` 中的 `accountWarnSetting` 方法签名。
*   **01:30 - 02:00**：在 `.proto` 文件中定义 `AccountWarnSettingRequest` 和 `AccountWarnSettingResponse` 消息结构。
*   **02:00 - 02:30**：演示使用 `protoc` 工具将 `.proto` 文件编译为 Java 代码，并展示生成的 `AccountWarnSettingData` 类。
*   **02:30 - 03:00**：在服务实现类 `GrpcStockUserService` 中，编写 `accountWarnSetting` 方法的业务逻辑。
*   **03:00 - 03:30**：在 `TradeUserServiceImpl` 中，调用 `ITradeAccountDao` 的 `saveAccountWarnSetting` 方法保存数据。
*   **03:30 - 04:00**：演示异常处理逻辑，当发生异常时，构建并返回 `AccountWarnSettingResponse`。
*   **04:00 - 04:30**：课程总结，回顾实现步骤。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **章节标题**：
    *   `3.2 实现账户预警通知设置接口`
    *   `3.5 功能验证`
    *   `3.5.1 预警通知模板设置验证`
    *   `3.5.2 账户预警通知设置验证`
    *   `3.5.3 生成账户预警通知记录`
*   **表结构**：
    *   `t_account_warn_setting` 表：
        | 属性 | 名称 | 数据类型 | 是否为空 | 注释 |
        | :--- | :--- | :--- | :--- | :--- |
        | id | 主键标识 | bigint(20) | NO | 主键标识 |
        | accountId | 账户ID | bigint(20) | YES | 账户ID |

#### 代码关键内容

*   **Java 类属性定义**：
    ```java
    private Integer warnType; // 预警类型 (0: 止损, 1: 止盈)
    private Double stopRate; // 止盈止损设置比例 (单位: %, 例2.28 代表02.28%)
    private String notifyType; // 通知方式(APP:站内信, EMAIL: 邮件, SMS: 短信, 多个以逗号分隔)
    private Date createTime; // 创建时间
    ```

*   **Protocol Buffers (.proto) 文件**：
    ```protobuf
    service StockUserService {
        rpc userLogin (LoginRequest) returns (LoginResponse) {}
        rpc accountWarnSetting (AccountWarnSettingRequest) returns (AccountWarnSettingResponse) {}
    }

    message AccountWarnSettingRequest {
        int64 accountId = 1; // 账户ID
        int64 stockId = 2; // 股票产品ID
        int32 warnType = 3; // 预警类型 (0: 止损, 1: 止盈)
        double stopRate = 4; // 止盈止损设置比例 (单位: %, 例2.28 代表02.28%)
        string notifyType = 5; // 通知方式(APP:站内信, EMAIL: 邮件, SMS: 短信, 多个以逗号分隔)
    }

    message AccountWarnSettingResponse {
        string status = 1;
        string message = 2;
    }
    ```

*   **Java 服务实现类 (GrpcStockUserService)**：
    ```java
    public class GrpcStockUserService extends StockUserServiceGrpc.StockUserServiceImplBase {
        @Autowired
        private IStockUserDao stockUserDao;
        @Autowired
        private ITradeAccountDao tradeAccountDao;

        @Override
        public void accountWarnSetting(AccountWarnSettingRequest request, StreamObserver<AccountWarnSettingResponse> responseObserver) {
            try {
                // 业务逻辑
                AccountWarnSettingData data = AccountWarnSettingData.newBuilder()
                    .setAccountId(request.getAccountId())
                    .setStockId(request.getStockId())
                    .setWarnType(request.getWarnType())
                    .setStopRate(request.getStopRate())
                    .setNotifyType(request.getNotifyType())
                    .build();
                tradeAccountDao.saveAccountWarnSetting(data);
                // 成功响应
                AccountWarnSettingResponse response = AccountWarnSettingResponse.newBuilder()
                    .setStatus("SUCCESS")
                    .setMessage("设置成功")
                    .build();
                responseObserver.onNext(response);
                responseObserver.onCompleted();
            } catch (Exception e) {
                // 异常处理
                log.error(e.getMessage(), e);
                AccountWarnSettingResponse response = AccountWarnSettingResponse.newBuilder()
                    .setStatus(GlobalConstants.STATUS_ERROR)
                    .setMessage(e.getMessage() == null ? "null" : e.getMessage())
                    .build();
                responseObserver.onNext(response);
                responseObserver.onCompleted();
            }
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库设计演示**
    *   **描述**：讲师在 Typora 文档中展示 `t_account_warn_setting` 表的结构，强调 `accountId` 是可选字段，而 `id` 是主键。同时，通过代码片段展示了 Java 类中对应的字段，如 `warnType` 和 `stopRate`，并解释了它们的含义和数据类型。

*   **场景二：gRPC 接口定义**
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `StockMessage.proto` 文件，展示 `StockUserService` 服务的定义。他重点讲解了 `accountWarnSetting` 方法，以及其请求和响应消息 `AccountWarnSettingRequest` 和 `AccountWarnSettingResponse` 的结构。他特别指出了 `notifyType` 字段的含义，即通知方式可以是 APP、EMAIL、SMS，并用逗号分隔。

*   **场景三：代码生成与编译**
    *   **描述**：讲师在终端中执行 `protoc` 命令，将 `.proto` 文件编译为 Java 代码。屏幕上显示了成功生成 `AccountWarnSettingData`、`StockMessage` 等类的消息。他解释了这些生成的类如何用于服务端的业务逻辑。

*   **场景四：服务层实现**
    *   **描述**：讲师在 `GrpcStockUserService` 类中编写 `accountWarnSetting` 方法。他演示了如何使用 `AccountWarnSettingRequest` 对象构建 `AccountWarnSettingData`，并调用 `tradeAccountDao.saveAccountWarnSetting(data)` 方法保存数据。他还演示了如何在发生异常时，构建一个包含错误信息的 `AccountWarnSettingResponse` 并返回给客户端。

*   **场景五：异常处理与响应**
    *   **描述**：讲师在 `GrpcStock
