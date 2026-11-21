# 27-代理服务登录鉴权-用户登录逻辑实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现用户的登录处理流程

首先,咱们定义一个返回对象

login response

外文音,咱们加上一个check catch的异常捕获

打印错误日志

1.get message

异常站

然后要封装错误消息

response

login response

new builder

设置状态

global

consistence

stace error

设置具体错误消息

1.get message

那么咱们去修改pb的数据结构定义

将这里面的状态改成stream

字符类型

重新生成一下

通过这个封装工具

可以快速去生成pb代码

再回到刚才的service

这里就没有再报错

最外层的逻辑

咱们再将它完善一下

response

opposite

opsov

on next

将返回对象输出给调用方

response

opsov.on

opsov.on

complete

接着咱们就来处理用户登录的具体业务逻辑

在checkh里面做具体的实现

咱们去查找用户对象

tel user

stock user dao

咱们先将需要用到的dao注入进来

将用户的数据接口注入进来

stock user dao

加上outwide

添加注入

用户管理的数据层接口

接着再添加交易账号的数据层接口

i check account

do

注入进来

outwide

这个是交易账号的数据层接口

不要忘了

在service上面要增加grpc的注解

标示为grpc接口

好

再回到刚才的业务处理逻辑

通过user dao

咱们去根据用户编号

push用户对象

request

get user number

然后咱们做一个唯空判断

如果是唯空呢

咱们就要抛出异常提示

response

new builder

-set stace

robo

consistence

stace element

设置它的返回消息

提示呢

用户不存在

.bill的进行构建

这里咱们是针对异常做了一个消息的错误包装

通过response ofzoe的对象呢

会将错误消息呢输出给调用方

这里就不需要再抛出一个savage

因为这种提示信息给调用方呢

会更加明确

好

如果能够找到用户呢

咱们就要做下面的业务逻辑处理

首先

对传递过来的密码做一个加密处理

enquire password

enquire youtube

get user password

获取用户传递的密码信息

然后咱们做一个判断

cat user

获取对应的用户密码

然后做一个判断比较

跟咱们的加密密码做判断

如果密码不一致呢

说明健全是失败的

在这里咱们要给出一个错误消息

密码不一致

给出错误消息提示

response

做一个包装

login

response

new builder

set states

global

global

consistence

states error

给出错误描述

用户密码错误

最后呢

进行build的构建

接下来如果密码通过

咱们就来处理下面的逻辑

咱们要拿取交易账户信息

cat account

根据dao

里面的根据用户ID

获取交易账户对象

传递user ID

第四个步骤呢

要去更新用户的登录信息

传递用户的ID

以及当前服务器的时间

把入信息进行

咱们看一下这个数据层接口

他做了些什么事情

点进去

看一下他对应的map

src文件

这里面的src实现也比较简单

他是根据用户ID

然后去修改

用户的最后登录时间

好

咱们再回到

刚才的业务处理逻辑

接下来咱们就要去封装返回消息

login response

.new builder

设置他的一个状态

states

states ok

然后就要返回业务属性

将用户ID返回出去

然后交易账户的ID

也要做一个返回

get account

get ID

最后呢

给出一个返回消息

说明了用户登录成功

要用构建方法

最后咱们再打印一个提示日志

说明了用户登录成功

将用户名称呢

也打印出来

便于咱们的跟踪排查

好

这里咱们就完成了用户登录的处理逻辑

添加对应的注释

用户登录结果处理

咱们回到讲义当中

在这里呢

我们是要查询用户的数据

这个是属于业务数据源

需要跨数据库处理

之前咱们已经实现了交易服务的mybatties

双数据源的集成配置

必须要将双数据源的配置实现好

为了快速实现

节省大家的时间

咱们在这里呢

直接将已经实现的源代码

数据层的接口呢

copy进来

这一块的实现逻辑并不复杂

大家呢可以参考具体的源代码

就不做详细的讲解

好这一讲呢

就是对交易服务登录接口业务逻辑的实现

那这一讲内容呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock` 的股票交易系统中，**用户登录服务（GrpcStockUserService）的实现过程**。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 gRPC 服务中实现一个登录接口。核心内容包括：
- **服务接口定义**：使用 `LoginRequest` 和 `LoginResponse` 作为请求和响应的 Protobuf 消息。
- **服务实现类**：`GrpcStockUserService` 继承自 `StockUserServiceGrpc.StockUserServiceImplBase`。
- **业务逻辑**：实现用户登录的完整流程，包括：
  1.  根据用户编号查询用户信息（通过 `TradeUserDao`）。
  2.  对用户密码进行加密比对（使用 `EncryptUtil` 工具类）。
  3.  如果登录成功，返回用户信息并更新用户最后登录时间（通过 `TradeAccountDao`）。
  4.  通过 `StreamObserver` 异步通知客户端登录结果。
- **技术栈**：Java、Spring Boot、gRPC、Protobuf、MyBatis、双数据源（`TradeUser` 和 `TradeAccount` 表）。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：视频开头，展示项目结构和 `GrpcStockUserService` 类的 `userLogin` 方法的初始状态。
*   **00:05 - 00:15**：讲师开始编写 `try-catch` 块，用于处理数据库查询异常，并初始化 `LoginResponse` 对象。
*   **00:15 - 00:25**：讲师在 `try` 块中添加注释，说明第一步是根据用户编号查询用户信息。
*   **00:25 - 00:35**：讲师编写代码，通过 `stockUserDao.getByUserNo(request.getUserNo())` 查询用户对象 `tradeUser`。
*   **00:35 - 00:45**：讲师添加 `if (null == tradeUser)` 判断，如果用户不存在，则设置错误状态并返回。
*   **00:45 - 00:55**：讲师开始处理密码校验逻辑，定义 `String encryptPassword` 变量并调用 `EncryptUtil.encryptSigned(...)` 方法。
*   **00:55 - 01:05**：讲师编写密码比对逻辑 `boolean pwdMatch = tradeUser.getPassword().equals(encryptPassword);`。
*   **01:05 - 01:15**：讲师在密码不匹配时，设置错误响应并返回。
*   **01:15 - 01:25**：讲师开始处理登录成功后的逻辑，声明 `TradeAccount tradeAccount` 对象。
*   **01:25 - 01:35**：讲师通过 `tradeAccountDao.getByUserId(tradeUser.getId())` 获取用户账户信息。
*   **01:35 - 01:45**：讲师调用 `stockUserDao.updateUserLogin(...)` 方法更新用户最后登录时间。
*   **01:45 - 01:55**：讲师构建并设置成功的 `LoginResponse` 对象，包括状态码、用户ID和账户ID。
*   **01:55 - 02:05**：讲师调用 `responseObserver.onNext(response)` 和 `responseObserver.onCompleted()` 通知客户端。
*   **02:05 - 02:15**：讲师切换到 Markdown 文档，展示 `Day13.md` 中关于“代理服务登陆接口调用实现”的章节内容，作为本节的总结和参考。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   在视频末尾（02:05），讲师切换到 `Day13.md` 文档，其中明确指出“**这里要查询用户数据，需要跨数据库，我们采用双数据源方案来实现**”。
    *   文档中还提到“**3. 参考源代码，实现 `IStockUserDao` 与 `ITradeAccountDao` 数据层接口**”，这与视频中代码的实现逻辑一致。

*   **关键代码片段**：

    ```java
    // 1. 根据用户编号，查找获取用户对象信息(微校判断，如果用户不存在，则抛出异常提示)
    TradeUser tradeUser = stockUserDao.getByUserNo(request.getUserNo());
    if (null == tradeUser) {
        response = LoginResponse.newBuilder().setStatus(GlobalConstants.STATUS_ERROR).setMessage("用户不存在").build();
    } else {
        // 2. 用户密码校验，通过加密方式判断
        String encryptPassword = EncryptUtil.encryptSigned(request.getUserPwd());
        boolean pwdMatch = tradeUser.getPassword().equals(encryptPassword);
        if (!pwdMatch) {
            response = LoginResponse.newBuilder().setStatus(GlobalConstants.STATUS_ERROR).setMessage("密码不一致").build();
        } else {
            // 3. 返回用户的登录成功信息(返回用户账号信息)
            TradeAccount tradeAccount = tradeAccountDao.getByUserId(tradeUser.getId());
            stockUserDao.updateUserLogin(tradeUser.getId(), new Date());
            response = LoginResponse.newBuilder()
                .setStatus(GlobalConstants.STATUS_OK)
                .setUserId(tradeUser.getId())
                .setAccountId(tradeAccount.getId())
                .setMessage("登录成功")
                .build();
        }
    }
    // 4. 通知客户端
    responseObserver.onNext(response);
    responseObserver.onCompleted();
    ```

*   **关键公式 / 图表**：
    *   无直接公式或图表展示，但代码中涉及了加密算法（`EncryptUtil.encryptSigned(...)`）和状态码（`GlobalConstants.STATUS_ERROR` / `GlobalConstants.STATUS_OK`）。

---

### 4) 关键场景与演示描述

*   **场景一：服务方法初始化** (00:00-00:15)
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `GrpcStockUserService` 类，定位到 `userLogin` 方法。他首先为方法添加了 `try-catch` 块，并初始化了 `LoginResponse` 对象，为后续的异常处理和响应构建做准备。

*   **场景二：用户查询与异常处理** (00:15-00:35)
    *   **描述**：讲师在 `try` 块中编写了核心业务逻辑。他使用 `stockUserDao.getByUserNo(...)` 方法根据请求中的用户编号查询数据库。如果查询结果为 `null`，他立即构建一个状态为 `STATUS_ERROR` 的响应对象，并设置错误信息“用户不存在”，然后返回。

*   **场景三：密码加密与比对** (00:35-01:05)
    *   **描述**：讲师在用户存在的情况下，调用 `EncryptUtil.encryptSigned(...)` 方法对客户端传入的密码进行加密。然后，他将加密后的密码与数据库中存储的用户密码进行比对。如果比对失败，他构建一个状态为 `STATUS_ERROR` 的响应对象，设置错误信息“密码不一致”，并返回。

*   **场景四：登录成功与数据更新** (01:05-01:45)
    *   **描述**：当密码比对成功后，讲师首先通过 `tradeAccountDao.getByUserId(...)` 获取用户的账户信息。接着，他调用 `stockUserDao.updateUserLogin(...)` 方法，将用户的最后登录时间更新为当前时间。然后，他构建一个状态为 `STATUS_OK` 的成功响应对象，并设置用户ID和账户ID。

*   **场景五：异步通知客户端** (01:45-02:05)
    *   **描述**：在构建好最终的响应对象后，讲师调用 `responseObserver.onNext(response)` 方法将响应发送给客户端。最后，他调用 `responseObserver.onCompleted()` 方法，通知客户端本次请求处理完毕。

*   **场景六：文档总结** (02:05-02:15)
    *   **描述**：讲师切换到 `Day13.md` 文档，总结本节内容。他强调了本节实现的登录服务是“代理服务登录接口调用实现”的一部分，并指出在实际项目中，需要通过“双数据源方案”来实现跨库查询，这与视频中代码中同时使用 `stockUserDao` 和 `tradeAccountDao` 的设计思路完全一致。
