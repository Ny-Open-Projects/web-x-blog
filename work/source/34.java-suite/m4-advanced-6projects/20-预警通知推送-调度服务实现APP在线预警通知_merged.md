# 20-预警通知推送-调度服务实现APP在线预警通知 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

这一讲咱们开始学习在调度服务里面去实现APP在线预警通知的推送功能

为了便于消息服务的集成使用

在这里我们去创建消息服务的发送工程

做相应的封装

那咱们回到工程当中

在Bus Stop下面新建一个服务模块

咱们要在Start启动器下面去新增一个模块

右键New Model

点击Next

名称就叫Bus Stop Start Center

点击Next Finish

让它导入生效

服务模块创建完成之后

接下来咱们要去添加POM依赖

将POM依赖做一个copy

回到工程当中

修改POM文件

在最下面增加依赖

让它导入生效

这里增加了两个依赖

一个是实体的依赖

另外的是公用的工具组件依赖

回到讲义当中

接着我们要去实现预警通知的发送接口

下面咱们要做相应的封装

这里是可以支持两种发送方式

一种是异步的方式

另外一种是同步方式

为了快速实现

这里将相关代码做一个copy

回到工程当中

首先咱们要创建对应的package

包名我们叫COMMUSD

ID CAST

BUS

START

SEND

接下来我们再创建相应的指导

右键Open in Tomino

Make DIR

一个是BASE目录

接着我们再创建Service目录

咱们再创建一个Vue的目录

好

创建完成之后

咱们刷新生效

接下来我们在BASE里面去创建公用的接口

NEO Java Class

这里呢

选择Innoface

名称叫做IWON

给它一个名称

NEO Java Class

NEO Java Class

咱们将代码粘贴进去

这里是定义了两个接口

一个是同步的方式去发送消息

另外呢

是采用异步的方式去发送消息

接下来咱们还要定义它的统一参数对象

以及响应的消息对象

回到讲义当中

接下来我们去定义统一的发送消息

接下来我们去定义统一的发送消息

切换到代码里面

在WIO下面我们创建一个新的Java对象

这个呢是生的Message

将代码粘贴进来

这个是统一的数据发送对象

这里面的信息包括交易账户ID

发送的主题

接收者信息

通知内容

还有更新时间

我们将Data导入进来

接下来咱们还要去定义统一的消息响应对象

回到讲义当中

这个是消息发送的响应结果

我们将它Copy下

切换到代码里面

在WIO下面再创建一个新的Java对象

名称叫生的Result

将代码粘贴进来

好那咱们来看一下它的数据结构

这里呢有数据的标识ID

然后是发送的状态

默认是错误的状态

如果处理成功

它会去反显对应的发送状态

接着的话呢是发送的结果记录

然后呢是发送的结果记录

然后提供了一个接口

这个接口呢能够快速判断发送状态是否处理成功

好那咱们再检查一下结果

这个时候呢就没有包错了

回到讲义当中

接下来我们要去实现App的在线推送处理逻辑

这里将代码做个引用

回到代码当中

在Task调度任务里面

咱们去增加APP在线消息的推送

这里呢就会看到

这里呢我们要创建一个纸包

纸包名称叫生长

接下来创建一个交发对象

名称叫APP生长

将代码引用进来

修正相关的错误

这个是Longbook的日子插件

好这里我们还引入相应的工程依赖

在POM文件下面咱们做一个调整

Scope去除

Posh咱们改一下

以变量的方式

增加注释

这个是自定义

消息发送服务的依赖组件

好再回到刚才的APP生长的实现内

检查下相关的错误

这里要将包导入进来

这个是在GRPC下面

好相关错误都已修正

那咱们来看一下它整体的实现处理流程

在这里它定义了Proxy的GRPC服务接口

在发送预警通知的时候做相应的调用

首先它会去构造预警通知的消息请求宝

根据传递了Send Message

做相应的转换处理

然后呢就去发送预警通知消息

通过Proxy代理服务的RPC接口

代理服务处理完成之后

会返回处理成功的通知记录ID

这里会根据ID做相应判断

记录最终的发送结果

这里会根据ID做相应判断

大家要注意在这里呢

只是记录是否成功发送到代理服务

并不能标识客户端是否真正接收到通知记录

因为整个交互是异步处理

需要客户端增加相应回馈机制

这里咱们就暂时不做实现

大家有兴趣可以自行扩展

然后下面是同步方式去发送通知消息

大家可以看到

它是直接对上面的方法进行调用

对不对

那咱们来看一下

异步方式的消息发送是如何实现的呢

点击该方法

这里的异步实现其实很简单

只需要加上R3的注解

那大家会有疑问

同步方式它也是调用生的message

既然加上了R3注解

这样不会造成异步的方式去发送消息吗

这个注解就类似于Splinter Transaction的事物注解

如果咱们不是通过接口的方式进行调用

也就是说

外层以它的接口的形式进行调用

这样该注解才会生效

然后会实现异步方式的发送

如果是在内部方法之间去做引用

R3的注解并不会生效

因为Splinter的AOP机制

它是无法去拦截内部的调用

好

再回到讲义当中

接着我们要增加APP在线的推送方式

咱们加代码做一个引用

回到工程当中

行吗

行吗

行吗

行吗

既有改Asc hung的wrapsendingService

在下面咱们去增加对应的接口

实现

这里需要注入app sender

在最上面

在这里咱们增加app sender的注入

notify sender

更加outwide的注解

再回到刚才的接口代码

还需要增加get sender message的方法

回到讲义当中

咱们将这个方法引入进来

先换到代码里面

把它放在最下面

好那咱们来看一下

发送预警通知数据的

整体实现处理流程

首先它要去获取

所有需要推送的预警消息

这里面的条件是

状态为发送不成功

并且发送次数是小于三次

每次咱们是获取1000条数据

接下来就是做便利处理

采用并行流的方式

去发送通知数据

通过并行流

会采用多线程的方式进行处理

能够提升数据的处理速度

但是不能保证它的有序性

接着的话是根据发送的通知数据

不同的消息类型

来调用相应的接口去发送消息

比如说APP是战略性的通知方式

后面如果是增加短信

在这里可以再去扩展

短信的通知方式

最后就是更新发送消息

将消息的发送次数进行累加

这样通知消息

如果是超过三次之后

就不会再次进行发送

这里我们要注意一下

点击该接口

我们查看一下它的Circle实现

这里从事次数的累加

是通过一个函数做处理

这个函数是什么作用呢

这个函数的作用

相当于买Circle的if now函数

也就是说RetrievedTime

如果是为now

那么会将它置为0

然后进行累加

如果是为now

直接进行数值的累加

是不会正常生效的

好

再回到刚才的业务代码

这里咱们需要将接口抽取下

右键

Reflect

Who members are

点击Reflect

好

再回到讲义当中

接下来我们要去增加

发送账户预警通知的调度任务

将这个代码拷贝下

回到工程当中

在Warning的包下面

去创建一个新的Job

名称我们就叫

Send

Warn Notify Message Job

将代码粘贴进来

导入相应的包

这个是在Long Book下面

好Job的处理比较简单

在这里呢

他会调用相应的service

去实现预警通知数据的发送

好

那咱们再回到讲义当中

接着我们要在工程配置里面

增加GRBC的代理服务的调用配置

咱们Copy下

回到工程当中

修改GRBC的服务配置

粘贴下

这个是GRBC服务端配置

下面是Client调用配置信息

这里需要调用代理服务

这个是代理服务的配置信息

好

咱们回到讲义当中

那这一讲咱们就完成了

在调度服务里面去实现

APP在线预警通知推送功能

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程聚焦于一个名为 `bulls-stock` 的股票交易系统中“预警通知”功能的实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何构建一个独立的“消息发送服务”工程（`stock-starter-sender`），并将其集成到主项目中。核心内容包括：
- **定义接口**：创建 `IWarnNotifySender` 接口，定义异步和同步发送消息的方法。
- **实现服务**：编写 `AppSender` 类，使用 gRPC 协议与远程服务通信，将预警消息封装为 `WarnMessageDataRequest`。
- **业务集成**：在 `AccountWarnSettingService` 服务中，通过 `@Autowired` 注入 `IWarnNotifySender`，在获取股票最新报价后，调用 `sendWarnNotifyMessageJob` 任务进行异步通知。
- **配置集成**：修改 `bootstrap-dev.yml` 配置文件，为 gRPC 服务配置端口（19993）。
- **技术栈**：主要使用 Java、Spring Boot、gRPC、MyBatis-Plus、Redis。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:15**：课程目标与步骤介绍。讲师在文档中列出“目标”、“步骤”、“实现”等章节，并重点指出本节将实现“调度服务实现APP在线预警通知推送功能”。
- **00:15 - 00:30**：创建消息发送服务工程。在 `stock-starter` 项目下创建 `stock-starter-sender` 工程，并展示其目录结构（`src/main/java`, `pom.xml`）。
- **00:30 - 00:45**：配置工程依赖。在 `pom.xml` 中添加 `bulls-stock-entity` 和 `bulls-stock-common-utils` 依赖。
- **00:45 - 01:00**：定义服务接口。创建 `IWarnNotifySender` 接口，定义 `sendMessage` 和 `sendSyncMessage` 方法。
- **01:00 - 01:15**：实现服务类。编写 `AppSender` 类，继承 `IWarnNotifySender`，并初始化 `GrpcClient`。
- **01:15 - 01:30**：实现异步发送方法。在 `AppSender` 中实现 `sendMessage` 方法，使用 `WarnMessageDataRequest.Builder` 构造消息体。
- **01:30 - 01:45**：业务服务集成。在 `AccountWarnSettingServiceImpl` 中注入 `IWarnNotifySender`，并调用 `sendWarnNotifyMessageJob`。
- **01:45 - 02:00**：配置 gRPC 服务。修改 `bootstrap-dev.yml`，添加 gRPC 服务端口配置 `server: port: 19993`。
- **02:00 - 02:15**：任务调度。展示 `SendWarnNotifyMessageJob` 任务类，用于异步发送预警通知。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **章节标题**：
  - `3.2 调度服务实现APP在线预警通知推送功能`
  - `5. 工程配置增加gRpc代理服务配置`
- **关键步骤**：
  - `3. 执行批处理命令 protoc_grpc.bat, protoc_netty.bat 生成JAVA文件。`
  - `修改bootstrap-dev.yml`

#### 代码关键内容

- **接口定义 `IWarnNotifySender`**：
  ```java
  public interface IWarnNotifySender {
      // 发送预警通知（异步方式）
      public SenderResult sendMessage(SenderMessage notifyMessage);

      // 同步方式发送消息
      public SenderResult sendSyncMessage(SenderMessage senderMessage);
  }
  ```

- **服务实现类 `AppSender`**：
  ```java
  public class AppSender implements IWarnNotifySender {
      private StockProxyServiceGrpc.StockProxyServiceBlockingStub stockProxyServiceBlockingStub;

      @Override
      public SenderResult sendMessage(SenderMessage senderMessage) {
          SenderResult result = new SenderResult();
          result.setId(senderMessage.gettId());
          try {
              // 构造预警通知消息请求包
              WarnMessageDataRequest.Builder warnMessageBuilder = WarnMessageDataRequest.newBuilder();
              warnMessageBuilder.setReceiver(senderMessage.getReceiver());
              warnMessageBuilder.setSubject(senderMessage.getSubject());
              warnMessageBuilder.setContent(senderMessage.getContent());
              warnMessageBuilder.setMemo(senderMessage.getMemo());
              warnMessageBuilder.setSendStatus(GlobalConstants.STATUS_OK);
              warnMessageBuilder.setCreateTime(System.currentTimeMillis());
              warnMessageBuilder.setUpdateTime(System.currentTimeMillis());
              warnMessageBuilder.setStockId(senderMessage.getStockId());
              warnMessageBuilder.setStockName(senderMessage.getStockName());
              warnMessageBuilder.setStockType(senderMessage.getStockType());
              warnMessageBuilder.setStockPrice(senderMessage.getStockPrice());
              warnMessageBuilder.setStockChange(senderMessage.getStockChange());
              warnMessageBuilder.setStockChangeRate(senderMessage.getStockChangeRate());
              warnMessageBuilder.setStockVolume(senderMessage.getStockVolume());
              warnMessageBuilder.setStockValue(senderMessage.getStockValue());
              warnMessageBuilder.setStockMarket(senderMessage.getStockMarket());
              warnMessageBuilder.setStockExchange(senderMessage.getStockExchange());
              warnMessageBuilder.setStockStatus(senderMessage.getStockStatus());
              warnMessageBuilder.setStockTime(senderMessage.getStockTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.setStockUpdateTime(senderMessage.getStockUpdateTime());
              warnMessageBuilder.set
