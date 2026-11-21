# 06-PB通讯工程-编译脚本封装与测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着学习如何去封装编译脚本

上一讲咱们讲解了编译生成交往文件

通过ProtoBuff的工具进行相应的生成

大家可以看到输入的指令比较多

而且不同类型的脚本

它的编译指令是不一样的

那么咱们来看一下能否进行一个简化呢

在最新版本的ProtoBuff当中

它是不支持通背符的命令

也就是说它不能同时去编译多个文件

这样呢

如果我们还是按照之前的方式

去生成对应的ProtoBuff的文件

就会比较繁琐

如果说我们定义了几十个ProtoBuff的脚本

这样的话呢就要执行几十次

对不对

所以在这里呢

咱们就要去封装它的编译指令

通过自定义脚本的方式来进行对应的实现

制定好相应的编译脚本

也能够便于咱们对整体数据结构的维护

如果是调整了数据结构的某个属性

或者是扩展了某些属性信息

咱们只需要执行封装的编译脚本就可以了

不需要再去输入和配置之前的繁琐的操作指令

好

那咱们看一下该如何去实现呢

咱们回到代码当中

在Proto目录下面呢

创建两个脚本

New File

一个呢

是用于GRBC接口的生成脚本

咱们再定义另外一个

这个呢

就是Netty的传输结构生成脚本

咱们回到讲义当中

将这两个脚本呢

Copy进来

一个是GRBC的

另外一个呢

是Netty的

好

那咱们来看一下这些脚本呢

具体是怎样的含义

首先呢

这里是做了一个便利循环

它的循环目录呢

是GRBC的

路径

那在GRBC下面呢

定义的所有的脚本都会进入这个循环处理

这里面就是生成GRBC传输数据层的脚本指令

咱们可以看到这里配置了GRBC的插件

指定了插件的路径

然后是加瓦代码的输出目录

这个呢

是GRBC代码的输出目录

最后面呢

要注意一下这个双百分号加上i代表呢

就是在这里面所便利到的

所有的文件名称

通过这个脚本呢

就帮助咱们实现了批量

Protobuf脚本的代码生成

接下来咱们来看一下Netty的工装脚本

在这里呢

同样也是做了一个便利

它是便利Netty目录下面的所有的PP脚本

那同样拿到PP脚本之后呢

就会进入Proto工具的编译生成对应的加瓦代码

这个呢

是生成加瓦代码的指定路径

然后呢

是指定要生成的PP的脚本路径

生成完成之后呢

会输出对应的脚本文件名称的提示

好

脚本配置完成之后呢

接着咱们就来执行下

看能否呢

生成相关的加瓦代码

回到咱们的工程当中

鉴于验证了

咱们将之前所生成的代码全部删除掉

右键Delete再次删除

将这些包清除掉

这里面也做一个清除

好

删除完成之后呢

咱们就来看一下

首先去生成GRPC的代码

咱们在中端桩口执行ProtoGRPC的脚本

可以看到它已经出现一个提示

说咱们的stockchat deal service这个脚本呢

已经生成完成

那咱们刷新下

可以看到

这里面的加瓦代码呢

都已经成功生成

那接着咱们再来生成一下

Neti的对外传输

数据结构代码

Proto这里呢

要指定Neti脚本

这个名称呢

咱们要改一下

add shift加r

然后呢

将这个c去除

lookback

好

重新执行下

执行完成可以看到呢

它输出了相应的提示信息

那咱们看一下

stockhead和stockmessage的代码有没有生成

刷新咱们的包结构

好

可以看到了

Neti层的代码呢

都已经生成完成

跟之前咱们通过命令方式生成的效果呢

都是一样的

通过脚本可以极大的简化

Proto编译的操作

即便下面有n个ProtoBuff脚本

咱们只需要执行一次对应的封装脚本就可以了

这个非常简便和实用

咱们在后面项目功能的实现当中呢

可能会频繁使用到

好

这一讲呢

就是对ProtoBuff脚本工具使用的方法了

封装

以及呢

对咱们封装的脚本进行了测试

整个脚本都能正常运行

好

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于“交易服务”项目中使用 Protocol Buffers (protobuf) 进行数据结构定义和 Java 代码自动生成的实践教程。讲师主要讲解了如何通过自定义批处理脚本（`.bat`文件）来解决新版 Protobuf 不支持通配符命令、无法一次性编译多个 `.proto` 文件的问题。视频内容聚焦于创建和使用 `proto_grpc.bat` 和 `proto_netty.bat` 两个脚本，分别用于为 gRPC 和 Netty 服务生成对应的 Java 类文件，并通过 IntelliJ IDEA 的项目结构展示了生成后的代码。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 课程大纲展示，当前位于“第2章 简易下单功能实现”的“3.4 封装编译脚本”部分。
*   **00:03 - 00:06**: 讲师解释了为什么需要封装脚本，即新版 Protobuf 不支持通配符命令，无法同时编译多个文件。
*   **00:06 - 00:10**: 展示了 `proto_grpc.bat` 脚本的代码内容，该脚本会遍历 `grpc/` 目录下的所有 `.proto` 文件并执行编译。
*   **00:10 - 00:14**: 展示了 `proto_netty.bat` 脚本的代码内容，该脚本会遍历 `netty/` 目录下的所有 `.proto` 文件并执行编译。
*   **00:14 - 00:18**: 在 IntelliJ IDEA 中，讲师演示了如何在项目目录下执行 `proto_grpc.bat` 脚本，并在终端中查看输出日志。
*   **00:18 - 00:22**: 讲师切换到 `proto_netty.bat` 脚本，演示了如何执行它来为 Netty 服务生成 Java 文件。
*   **00:22 - 00:26**: 在 IntelliJ IDEA 的项目结构视图中，讲师高亮显示了由脚本生成的 Java 类文件，如 `PlaceOrderRequest`、`StockMessage` 等，证明了脚本的有效性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.4 封装编译脚本”。
    *   **核心说明**: “最新Protobuf不支持通配符命令，不能同时编译多个文件，这里我们通过自定义脚本来支持，制定好脚本也能便于对数据结构的维护。”
    *   **脚本列表**: “1. proto_grpc.bat 文件” 和 “2. proto_netty.bat 文件”。

*   **代码内容**:
    *   **`proto_grpc.bat` 脚本**:
        ```bat
        @echo off
        for %%i in (grpc/*.proto) do (
            d:/TestCode/protoc.exe --plugin=protoc-gen-grpc-java=d:/TestCode/protoc-grpc.exe --grpc-java_out=../java ../grpc/%%i
            echo generate %%i to java file successfully!
        )
        ```
    *   **`proto_netty.bat` 脚本**:
        ```bat
        @echo off
        for %%i in (netty/*.proto) do (
            d:/TestCode/protoc.exe --proto_path=./netty --java_out=../java ../netty/%%i
            echo generate %%i to java file successfully!
        )
        ```
    *   **终端输出示例**:
        ```
        generate StockTradeDealService.proto to java file successfully!
        generate StockHead.proto to java file successfully!
        generate StockMessage.proto to java file successfully!
        ```

---

### 4) 关键场景与演示描述

*   **场景一：脚本创建与内容展示 (00:06 - 00:10)**
    *   讲师在 Typora 文档中展示了 `proto_grpc.bat` 脚本的完整代码。
    *   代码使用了 `for %%i in (grpc/*.proto) do` 循环，遍历 `grpc` 目录下的所有 `.proto` 文件。
    *   每次循环都会调用 `protoc.exe` 命令，指定插件 `protoc-gen-grpc-java` 和输出目录 `../java`，并生成对应的 Java 文件。

*   **场景二：脚本执行与结果验证 (00:14 - 00:26)**
    *   讲师在 IntelliJ IDEA 的终端中执行 `proto_grpc.bat` 脚本。
    *   终端输出显示成功生成了 `StockTradeDealService.proto`、`StockHead.proto` 和 `StockMessage.proto` 对应的 Java 文件。
    *   讲师随后切换到 `proto_netty.bat` 脚本，执行后终端输出显示成功生成了 `StockHead.proto` 和 `StockMessage.proto` 的 Java 文件。
    *   最后，讲师在 IntelliJ IDEA 的项目结构中，高亮显示了生成的 Java 类文件，如 `PlaceOrderRequest`、`StockMessage` 等，直观地证明了脚本的正确性和有效性。

---

**总结**: 本视频通过实际操作演示了如何利用批处理脚本解决 Protobuf 编译中的痛点，为后续的 gRPC 和 Netty 服务开发奠定了基础。
