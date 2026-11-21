# 04-PB通讯工程-Netty下单接口定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始编译和生成Java文件

在编译生成之前

咱们要先下载ProBuff的编译工具

以及ProBuff GRBC的查检

这样它才能生成GRBC相关的代码

为了咱们的编译使用

可以将ProBuff工具交到环境变量当中

在这里咱们已经将ProBuff工具下载到本地

咱们可以看一下Poto

这个就是ProBuff的编译工具

咱们来看一下如何去编译和使用

在这里提供出来的GRBC的编译指令

咱们将它copy下

回到咱们代码当中

选中GRBC

咱们是在Resource目录下面

咱们要选中Poto

然后Open in Terminal

打开一个控制中桩

接着咱们将刚才copy的指令粘连上去

我们可以看到

这里的Poto命令咱们还没有加入到环境变量当中

如果没有加入的话

需要去指定它的完整路径

完整路径在Test Code下面

咱们来看一下其他命令选项的含义

这个Protopass

它是指定咱们Poto脚本的存放路径

咱们的当前目录是在Protom目录下面

那么Protopass就在GRBC的目录下面

Plugin是ProtoGRBC的一个插件

因为这个是GRBC接口的一个定义

咱们要去生成GRBC接口信息

这个GRBC插件必须要让它加入进来

加入这个插件之后

那么咱们生成的GRBC的代码

可以生成在指定目录下面

如果咱们没有配置这个选项

它默认就会生成在当前目录下面

那么为了便于咱们的使用

这里将GRBC生成的代码

放在咱们的Java目录下面

另外一个选项

就是Java的代码

生成的目录

这个同样也是放在Java目录下面

这里要注意是有两个路径

一个是serviceGRBC接口的生成路径

另外的就是数据消息体

在这里面定义了普通Java代码生成的路径

这些message消息

就通过Java out这个选项输出到指定目录下面

最后咱们要注意一下

虽然咱们指定了ProBuf脚本的存储路径

但是

如果这个目录下面有多个ProBuf脚本的话

它并不会批量去生成

在ProBuf三系列版本当中

ProtoC这个工具

它只能逐个去生成相应的代码

所以最后咱们还要去指定ProBuf文件的具体名称

好

这个就是GRBC的生成指令

那咱们执行一下

看一下它的运行效果

执行过程当中没有报错

说明了它执行成功

咱们来看一下刷新

可以看到生成了对应的Java代码

对不对

这里面Place,Order,Response

然后Request以及GRBC接口

跟咱们在脚本里面定义的信息都是一致的

接着咱们再去生成Neti对外数据传输层的结构代码

咱们copy下指定

回到代码当中

粘贴

修改ProBuf工具的路径

大家可以看到

这条指令已经简化很多

因为Neti对外传输数据层结构这一块

是不需要生成GRBC的接口代码

所以可以不用去配置GRBC的插件信息

那咱们就来执行指令

指令执行完成

咱们看一下它所生成的代码

这里大家可以看到生成的Neti相关的包

我们看一下具体的代码

已经生成了stockhead的数据结构代码

Neti传输层

我们是定义了两个脚本

还有一个是数据传输消息体

咱们也将它生成一下

修改它的名称叫stock message

好生成完成

咱们可以看到stock message相关的代码

就已经生成完成

咱们可以看到stock message相关的代码都已经生成

好在这里咱们就实现了

ProtoBuf脚本的编译

以及Java代码文件的生成

那这一讲咱们就先讲到这里

谢谢大家

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于使用 Protocol Buffers (protobuf) 生成 Java 代码的实战教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何为 gRPC 服务和 Netty 项目分别编译 `.proto` 文件。核心内容包括：在 Windows 系统的命令行中，使用 `protoc` 编译器及其插件（`protoc-gen-grpc-java` 和 `protoc.exe`）将 `.proto` 文件转换为对应的 Java 源码。演示过程详细展示了命令行参数的配置、工作目录的切换以及生成的 Java 文件结构，旨在帮助学习者掌握 protobuf 代码生成的完整流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示本节内容“3.3 编译生成Java文件”，并强调需要下载 `protoc` 编译器和 `protoc-gen-grpc-java` 插件。
*   **00:00:05 - 00:00:15**: 讲师切换到命令行界面，准备执行编译命令。
*   **00:00:15 - 00:00:25**: 讲师在命令行中输入并执行了第一个编译命令，用于生成 gRPC 服务的 Java 代码。
*   **00:00:25 - 00:00:35**: 讲师切换到另一个 `.proto` 文件（`StockMessage.proto`），并执行了第二个编译命令，用于生成 Netty 项目的 Java 代码。
*   **00:00:35 - 00:00:45**: 讲师在 IntelliJ IDEA 中展示了编译后生成的 Java 文件，包括 `StockTradeDeaServiceProto`、`StockHeadProto` 和 `StockMessageProto` 等类。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档内容**:
    *   **标题**: “3.3 编译生成Java文件”
    *   **关键步骤**:
        1.  下载 `Protobuf 编译工具` 以及 `protoc-grpc` 插件，并将 `protoc` 加入环境变量。
        2.  在 `resources/proto` 目录下执行命令。
    *   **命令示例**:
        *   **gRPC 编译命令**:
            ```bash
            protoc --proto_path=./grpc --plugin=protoc-gen-grpc-java=d:/TestCode/protoc-grpc.exe --grpc-java_out=../java --java_out=../java StockTradeDeaService.proto
            ```
        *   **Netty Proto 编译命令**:
            ```bash
            protoc.exe --proto_path=./netty --java_out=../java ./netty/StockHead.proto
            ```

*   **代码示例**:
    *   **`.proto` 文件内容**:
        ```protobuf
        option java_outer_classname = "StockTradeDeaServiceProto";

        service StockTradeDeaService {
          rpc placeOrder (PlaceOrderRequest) returns (PlaceOrderResponse) {
          }
        }

        message PlaceOrderRequest {
          // 股票ID
          int64 stockId = 1;
          // 股票的买卖方向(0:买入，1:卖出)
          int32 direction = 2;
          // 委托类型(0:市价单，1:限价单)
          int32 type = 3;
          // 请求数量/挂单价格
          int32 execVolume = 4;
          // 委托价格
          int64 execPrice = 5;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与命令行操作**
    *   讲师首先在 Typora 文档中介绍了编译所需的工具和环境变量设置。
    *   接着，讲师在 Windows 命令提示符（cmd.exe）中切换到项目目录 `D:\TestCode\`，并执行了第一个编译命令。
    *   命令行输出显示了 `protoc` 工具的版本信息和帮助文档，确认了工具已正确安装并可执行。

*   **场景二：gRPC 服务编译**
    *   讲师在 IntelliJ IDEA 中打开了 `StockTradeDeaService.proto` 文件，展示了其服务定义和消息结构。
    *   讲师在终端中执行了编译命令，将 `StockTradeDeaService.proto` 文件编译为 Java 代码。
    *   编译成功后，IDEA 自动在 `src/main/java` 目录下生成了对应的 Java 类文件。

*   **场景三：Netty 项目编译**
    *   讲师切换到另一个 `.proto` 文件 `StockHead.proto`。
    *   讲师在终端中执行了针对 Netty 项目的编译命令，将 `StockHead.proto` 文件编译为 Java 代码。
    *   编译成功后，IDEA 在 `src/main/java` 目录下生成了对应的 Java 类文件。

*   **场景四：生成的 Java 文件展示**
    *   讲师在 IntelliJ IDEA 中展示了编译后生成的 Java 文件，包括 `StockTradeDeaServiceProto`、`StockHeadProto` 和 `StockMessageProto` 等类。
    *   这些类包含了从 `.proto` 文件中生成的 `registerAllExtensions` 方法和数据结构，用于在 Java 项目中使用 protobuf 数据。
