# 21-简易下单功能-客户端菜单指令交互处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,这一讲呢,咱们接着去实现NAT的模拟客户端

之前呢,咱们实现了模拟客户端下单接口的封装

以及发送处理流程

那接着呢,咱们就去完善整个模拟客户端的交互处理

首先,咱们将Business Handle加入进来

进一个Business Handle

这个是咱们的业务接口处理器

咱们给它一个get方法,edit insert

选中Business Handle

这方法呢,放在下面

之前咱们定义了WAS消息的响应配置通道

咱们将它做一个初始化配置

edit insert

去重写附类的方法

handle edit

list.handle.ecfuture

通过它的通道呢,创建一个新的Promise对象

这样呢,咱们才能通过该对象去操作相关的方法

好

那我们就来看看这个方法

那接下来咱们要对Business Handle做一个初始化

这个在哪里去初始化呢

在Channel Active连接建立成功之后

咱们就进行相应的初始化

因为Business Handle呢,要拿到它的Channel通道

咱们先做一个消息打印

提示呢,Server connected

然后初始化创建业务处理器

Business Handle

New Business Handle

将Channel呢,输入进去

之前咱们加入了预制方法的调用

那么预制方法呢,也是在这里进行处理

调用预制方法

咱们去创建一个新的方法名称

invoke method

这个就是预制调用方法的处理

咱们首先要判断,Method的方法不能为空

如果为空没有指定

咱们就不用做任何处理

接着咱们写入一个学开取异常的补货

然后这里呢,就是预制方法的调用

比如说你想预制去调用咱们的下单接口

那么就通过Business Handle调用place-out方法就可以了

因为咱们传进了Method呢,有可能是不同的接口

所以呢,要加上一个Method方法类型的判断

对Request type做判断,然后调用不同的接口方法

这个咱们就先预制在这里

后面如果是需要使用的时候呢,再做对应的实现

咱们再回到主逻辑

接下来咱们就要去实现菜单的交互

那么我们要定一个对象,StreetMap Buffer

这个对象呢,就是揭露客户端所接收的用户的操作指令

StreetMap Buffer

处理,接收,用户发送的指令

那咱们呢,来做相应的实现

外层的话呢,是一个循环

如果没有输出相应的指令呢

它就会一直去监听用户的交互

因为测试过程当中呢,咱们可能会发送多个接口

这里呢,再输入一个Sys的呢,也可以进行退出

接着咱们就要去拿到它对应的指令

通过RateImpute的方法做处理

咱们去实现RateImpute的方法

添加对应的注释

这种呢,是读取用户输入的支付串,Receive

RateImpute.setLength

这个呢,是将之前的内容呢,做清楚

Ctrl-Alt-T

加上Try-Catch的处理

然后呢,咱们要做一个读取

System.in.read

注意,这个方法呢,会阻塞

它会去读取用户输入的支付串信息

那么什么时候结束呢

直至用户输入了支付串信息

输入回车

那我们来做个对应处理

in不等于-1

就是说有数据输入

然后呢,这个in要不等于回车

这回车符呢,就是-n

这个是在Windows下面

Linux下面的话呢,是-r-n

Append

硬要等于System.in.read

最后呢,咱们就要返回所结束到的支付串信息

如果是出现异常呢

就返回为-n

咱们再回到主逻辑

读取到指定之后,咱们要做一个判断

不同的指定呢,咱们要做不同的处理

这个就根据咱们预先定义的序号

所对应的指定关系

这里输入1呢,就是代表用户的登录

用户登录借口呢,咱们暂时没有实现

在后面实现过程当中呢

咱们再做具体的讲解

接下来的话呢,就是序号为2的指定

这个代表就是

要用下单借口

通过咱们封装的

Case-all的方法

接着的话呢,还有M指令

这个就是要返回到上一个层级

就是咱们的主菜单

可以支持大小写

Show menu

else

然后其他指令呢,咱们就无法识别

不能正常处理

给它一个提示就可以了

好,咱们再回到讲义当中

这里呢,咱们就完成了

Netty模拟客户端的实现

模拟客户端的实现呢

它的内容较多

主要包括呢,模拟客户端

它的一个启动配置

以及websocket的连接调用配置

然后呢,是自定义的

客户端数据接收处理器

在这里呢,咱们加入了

自己所定义的交互指令

最后呢,就是

业务接口处理器

在这里面就是定义咱们的

不同接口的请求参数信息

随着后面项目功能的不断实现

在这里面呢,就是我们的项目功能的不断实现

在这里呢,也会扩充不同的接口调用方法

在这里面呢,也会扩充不同的接口调用方法

Netty模拟客户端呢,咱们就已经实现完成

那这一讲,咱们就先讲到这里

那这一讲,咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Netty 的股票交易代理服务的客户端实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了 `ClientBoundHandler` 类的编写过程。该类负责处理客户端与服务端的 WebSocket 连接、消息收发、以及用户交互命令的解析。核心内容包括：
- **建立连接**：使用 `SimpleChannelInboundHandler` 处理连接事件。
- **消息处理**：实现 `channelActive` 和 `channelRead0` 方法，分别处理连接建立和接收服务端消息。
- **用户交互**：创建一个独立线程来处理用户输入，支持“登录”和“下单”等命令。
- **业务逻辑**：通过 `BusinessHandler` 调用预置方法，将用户指令转换为服务端可识别的 Protobuf 消息。

整个演示旨在展示如何构建一个轻量级的、基于 Netty 的客户端，用于模拟用户与后端服务的交互。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:15**：介绍项目结构，展示 `ClientBoundHandler` 类在项目中的位置。
- **00:16 - 00:30**：讲解 `BusinessHandler` 类，展示其 `sendMsg` 方法用于向服务端发送消息。
- **00:31 - 00:45**：演示 `ClientBoundHandler` 的 `channelActive` 方法，用于处理连接建立事件。
- **00:46 - 01:00**：编写 `channelRead0` 方法，用于接收并解析服务端发送的 Protobuf 消息。
- **01:01 - 01:15**：实现用户交互逻辑，创建新线程处理用户输入。
- **01:16 - 01:30**：编写 `showMenu` 方法，显示用户可选择的命令。
- **01:31 - 01:45**：实现 `readInput` 方法，读取用户输入并根据命令调用相应业务方法。
- **01:46 - 02:00**：演示如何调用 `businessHandler` 的方法，如 `placeOrder`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

- **标题**：第3章 代理服务登陆鉴权实现
- **子章节**：
  - 3.8 Netty模拟客户端编写
  - 3.9 测试验证
- **核心说明**：
  - 配置好对应的 Protobuf 编码器与解码器，以及自定义数据处理器。

#### 代码关键内容

- **`BusinessHandler.java`**：
  ```java
  private static Long seqId = 0L;
  public BusinessHandler(Channel ctx) {
      this.ctx = ctx;
  }

  private void sendMsg(Message msg) {
      if (null == msg || !ctx.isWritable()) {
          return;
      }
      ctx.writeAndFlush(msg);
  }
  ```

- **`ClientBoundHandler.java`**：
  ```java
  @Override
  public void channelActive(ChannelHandlerContext ctx) throws Exception {
      // 设置握手信息
      handler.setHandshaker(handshaker);
      handshaker.handshake(channel);
      // 阻塞等待是否握手成功
      future = handshaker.handshakeFuture().sync();
      System.out.println("----channel:" + future.channel());
  }

  private void recvMsg(ResponseMessage msg) {
      StockHeadProto.StockHead stockHead = msg.getStockHead();
      System.out.println("********** Receive Server Message **********");
      System.out.println("seqId: " + seqId);
      System.out.println("requestType: " + stockHead.getRequestType());
      System.out.println("status: " + msg.getStatus());
      System.out.println("message: " + msg.getMessage());
      if (stockHead.getRequestType() == StockHeadProto.RequestType.PLACE_ORDER) {
          System.out.println("order id: " + msg.getPlaceOrderResp().getDealId());
      }
  }

  private void showMenu() {
      System.out.println("Please Enter Command:");
      System.out.println("1: User Login【用户登录】");
      System.out.println("2: Place Order【下单】");
      System.out.println("3: Exit【退出】");
  }

  private void readInput() {
      StringBuffer recv = new StringBuffer();
      new Thread(new Runnable() {
          @Override
          public void run() {
              showMenu();
              while (!"0".equalsIgnoreCase(recv.toString()) && !"exit".equalsIgnoreCase(recv.toString())) {
                  try {
                      String command = readlnInput(recv);
                      if ("1".equals(command)) {
                          businessHandler.login();
                      } else if ("2".equals(command)) {
                          businessHandler.placeOrder();
                      }
                  } catch (Exception e) {
                      e.printStackTrace();
                  }
              }
          }
      }).start();
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：连接建立与握手**
  - 讲师在 `ClientBoundHandler` 类中重写 `channelActive` 方法。
  - 通过 `handler.setHandshaker(handshaker)` 设置握手处理器，并调用 `handshaker.handshake(channel)` 进行握手。
  - 使用 `future = handshaker.handshakeFuture().sync()` 阻塞等待握手完成，并打印成功后的通道信息。

- **场景二：接收服务端消息**
  - 讲师在 `channelRead0` 方法中处理接收到的消息。
  - 解析 Protobuf 消息中的 `StockHead` 和 `ResponseMessage`。
  - 根据 `requestType` 判断是登录、下单还是其他类型，并打印相应的消息内容。

- **场景三：用户交互与命令处理**
  - 讲师创建一个新线程来处理用户输入。
  - 在 `showMenu` 方法中显示登录、下单和退出三个选项。
  - 通过 `readlnInput` 方法读取用户输入，并根据输入值调用 `businessHandler` 的相应方法（如 `login` 或 `placeOrder`）。

- **场景四：异常处理**
  - 在所有关键方法中（如 `channelActive`、`channelRead0`、`readInput`）都添加了 `try-catch` 块，用于捕获并打印异常堆栈，确保程序的健壮性。

---

以上是根据视频画面进行的结构化技术分析，旨在帮助理解该 Netty 客户端的实现逻辑。
