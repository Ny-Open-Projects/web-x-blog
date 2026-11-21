# 画面线理解：11.后台服务系统之什么是dubbo

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\11.后台服务系统之什么是dubbo【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:19, 01:44, 01:49, 02:19, 02:27, 02:30, 03:06, 03:15, 03:18, 07:31, 09:54, 09:58, 10:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:32:37

1) 这一组画面整体在讲什么（一句话）：
介绍 Apache Dubbo 框架，包括其定义、架构、特性以及使用场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示 Typora 文档编辑器，内容为课程大纲，当前章节为“3.2. dubbo快速入门”下的“3.2.1. 什么是dubbo?”。
- 文档中包含对 Dubbo 的介绍：“Apache Dubbo™ (incubating)是一款高性能Java RPC框架。”
- 文档中列出的要点：
  - dubbo是由阿里团队开发的一款优秀的RPC框架。
  - 目前dubbo在Apache中孵化，预计很快会毕业。
- 文档底部显示“早期的介绍：”和“什么是RPC？”的标题。

画面2：
- 显示 Apache Dubbo 官网首页。
- 页面标题为“Apache Dubbo”，副标题为“Apache Dubbo™ (incubating)是一款高性能Java RPC框架。”
- 页面包含“快速开始”和“GITHUB”按钮。

画面3：
- 显示 Dubbo 架构图。
- 架构图包含以下组件：
  - Registry（注册中心）
  - Consumer（消费者）
  - Provider（提供者）
  - Monitor（监控）
  - Container（容器）
- 组件间关系：
  - Consumer → Registry（2. subscribe）
  - Consumer → Provider（4. invokes）
  - Consumer → Monitor（5. count）
  - Provider → Registry（3. notify）
  - Provider → Container（6. start）

画面4：
- 显示 Dubbo 特性一览。
- 特性包括：
  - 面向接口代理的高性能RPC调用
  - 智能负载均衡
  - 服务自动注册与发现
  - 高度可扩展能力
  - 运行期流量调度
  - 可视化的服务治理与运维

画面5：
- 显示“快速开始”部分。
- 文字说明：“只需通过几段代码即可快速构建一个Dubbo应用。”
- 展示了一段 Java 代码：
  ```java
  public class Application {
      public static void main(String[] args) throws Exception {
          ServiceConfig<HelloService> service = new ServiceConfig<HelloService>();
          service.setInterface(HelloService.class);
          service.setRegistry(registry);
          service.setApplication(application);
          service.setProtocol(protocol);
          service.setRef(new HelloServiceImpl());
          service.export();
          System.in.read();
      }
  }
  ```

画面6：
- 显示“谁在使用Dubbo”部分。
- 页面底部列出多个使用 Dubbo 的公司标志，包括：
  - Alibaba Group
  - Kingdee
  - dangdang
  - 滴滴出行
  - Qunar.com
  - 阿里云
  - 中国人寿
  - Haier
  - 中国银联
  - 中国电信
  - 微店
  - ICBC
  - 韩都衣舍
  - ROGRAND

画面7：
- 与画面6内容相同，展示“谁在使用Dubbo”部分。
- 页面底部列出多个使用 Dubbo 的公司标志。

画面8：
- 与画面6内容相同，展示“谁在使用Dubbo”部分。
- 页面底部列出多个使用 Dubbo 的公司标志。

画面9：
- 与画面1内容相同，显示 Typora 文档编辑器，内容为课程大纲，当前章节为“3.2. dubbo快速入门”下的“3.2.1. 什么是dubbo?”。
- 文档中包含对 Dubbo 的介绍：“Apache Dubbo™ (incubating)是一款高性能Java RPC框架。”
- 文档中列出的要点：
  - dubbo是由阿里团队开发的一款优秀的RPC框架。
  - 目前dubbo在Apache中孵化，预计很快会毕业。
- 文档底部显示“早期的介绍：”和“什么是RPC？”的标题。

画面10：
- 与画面9内容相同，显示 Typora 文档编辑器，内容为课程大纲，当前章节为“3.2. dubbo快速入门”下的“3.2.1. 什么是dubbo?”。
- 文档中包含对 Dubbo 的介绍：“Apache Dubbo™ (incubating)是一款高性能Java RPC框架。”
- 文档中列出的要点：
  - dubbo是由阿里团队开发的一款优秀的RPC框架。
  - 目前dubbo在Apache中孵化，预计很快会毕业。
- 文档底部显示“早期的介绍：”和“什么是RPC？”的标题。

画面11：
- 与画面1内容相同，显示 Typora 文档编辑器，内容为课程大纲，当前章节为“3.2. dubbo快速入门”下的“3.2.1. 什么是dubbo?”。
- 文档中包含对 Dubbo 的介绍：“Apache Dubbo™ (incubating)是一款高性能Java RPC框架。”
- 文档中列出的要点：
  - dubbo是由阿里团队开发的一款优秀的RPC框架。
  - 目前dubbo在Apache中孵化，预计很快会毕业。
- 文档底部显示“早期的介绍：”和“什么是RPC？”的标题。

画面12：
- 显示“什么是RPC？”部分。
- 页面包含对 RPC 的定义：“RPC (Remote Procedure Call Protocol) — 远程过程调用协议，它是一种通过网络从远程计算机上请求服务，而不需了解底层网络通信细节的协议。”
- 页面包含对 RPC 的说明：“RPC 是一种远程调用协议，请求方通过网络调用远程服务，远程服务响应请求，返回结果。”
- 页面包含一个表格，列出了 RPC 协议的分类：
  - 协议名：Remote Procedure Call Protocol
  - 概念：远程过程调用协议
  - 核心思想：远程调用
  - 通信协议：分层式

画面13：
- 与画面1内容相同，显示 Typora 文档编辑器，内容为课程大纲，当前章节为“3.2. dubbo快速入门”下的“3.2.1. 什么是dubbo?”。
- 文档中包含对 Dubbo 的介绍：“Apache Dubbo™ (incubating)是一款高性能Java RPC框架。”
- 文档中列出的要点：
  - dubbo是由阿里团队开发的一款优秀的RPC框架。
  - 目前dubbo在Apache中孵化，预计很快会毕业。
- 文档底部显示“早期的介绍：”和“什么是RPC？”的标题。

画面14：
- 与画面12内容相同，显示“什么是RPC？”部分。
- 页面包含对 RPC 的定义：“RPC (Remote Procedure Call Protocol) — 远程过程调用协议，它是一种通过网络从远程计算机上请求服务，而不需了解底层网络通信细节的协议。”
- 页面包含对 RPC 的说明：“RPC 是一种远程调用协议，请求方通过网络调用远程服务，远程服务响应请求，返回结果。”
- 页面包含一个表格，列出了 RPC 协议的分类：
  - 协议名：Remote Procedure Call Protocol
  - 概念：远程过程调用协议
  - 核心思想：远程调用
  - 通信协议：分层式
