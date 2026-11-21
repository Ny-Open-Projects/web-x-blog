# 画面线理解：06_RabbitMQ概述

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\06_RabbitMQ概述_【海量资源尽在 ubkz.com】.mp4
- 抽帧：9 帧 @ 00:21, 03:01, 03:14, 05:28, 05:59, 06:39, 07:00, 08:01, 09:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:33:29

1) 这一组画面整体在讲什么（一句话）：
本组画面系统介绍了消息队列（MQ）的基本概念，重点讲解了RabbitMQ的架构、核心组件（Broker、Virtual Host、Connection、Channel、Exchange、Queue、Binding）及其工作模式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍AMQP协议，定义其为面向消息的中间件开放标准，类比HTTP。
画面2：介绍RabbitMQ 1.0于2007年发布，采用Erlang语言开发，Erlang由Ericson设计，专为高并发和分布式系统。
画面3：展示RabbitMQ基础架构图，包含Producer、Broker(RabbitMQ Server)、Consumer，以及其中的Connection、Virtual Host、Exchange、Binding、Queue等组件。
画面4：列出RabbitMQ中的相关概念：Broker、Virtual Host、Connection、Channel。
画面5：列出RabbitMQ中的相关概念：Exchange、Queue、Binding。
画面6：说明RabbitMQ提供了6种工作模式：简单模式、work queues、Publish/Subscribe发布与订阅模式、Routing路由模式、Topics主题模式、RPC远程调用模式。
画面7：展示RabbitMQ 6种工作模式的图示，包括“Hello World!”、Work queues、Publish/Subscribe、Routing、Topics、RPC，并标注了支持的语言。
画面8：切换到章节1.7 JMS。
画面9：切换到“小结”页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
架构图（画面3）：
- Producer → Connection → Channel → Exchange → Binding → Queue → Consumer
- Exchange → Binding → Queue
- Broker(RabbitMQ Server) 包含多个 Virtual Host
- Connection 与 Producer 和 Consumer 之间有连接线

表格数据（画面7）：
- 1 "Hello World!"：支持语言 Python, Java, Ruby, PHP, C#, Javascript, Go
- 2 Work queues：支持语言 Python, Java, Ruby, PHP, C#, Javascript, Go
- 3 Publish/Subscribe：支持语言 Python, Java, Ruby, PHP, C#, Javascript, Go
- 4 Routing：支持语言 Python, Java, Ruby, PHP, C#, Javascript, Go
- 5 Topics：支持语言 Python, Java, Ruby, PHP, C#, Javascript, Go
- 6 RPC：支持语言 Python, Java, Ruby, PHP, C#, Javascript, Go（被红色斜线划掉）

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
