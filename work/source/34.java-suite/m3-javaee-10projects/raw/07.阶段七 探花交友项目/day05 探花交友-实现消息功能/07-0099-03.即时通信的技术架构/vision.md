# 画面线理解：03.即时通信的技术架构

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\03.即时通信的技术架构_【海量资源尽在 666java.com】.mp4
- 抽帧：9 帧 @ 01:25, 01:47, 04:56, 04:58, 05:22, 05:58, 06:00, 06:07, 08:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:05:16

1) 这一组画面整体在讲即时通讯系统的两种技术实现方案：方案一是自主研发（含Netty、WebSocket、RocketMQ、MongoDB、Redis、ZooKeeper、MySQL），方案二是对接第三方服务（如环信）。

2) 按时间顺序列出每张画面的要点：
画面1：展示“技术方案”章节，介绍即时通讯开发挑战，引出两种方案。方案一为“自主实现，从设计到架构，再到实现”，技术栈为“Netty + WebSocket + RocketMQ + MongoDB + Redis + ZooKeeper + MySQL”。
画面2：继续展示方案一的架构图，图中包含客户端、Netty Server、ZK集群、Redis集群、MongoDB集群、MySQL集群、文件系统等模块。
画面3：独立展示方案一的架构图，清晰显示客户端通过Netty Server连接ZK集群，ZK集群管理Redis、MongoDB、MySQL等数据服务。
画面4：回到Typora文档，展示方案一技术栈“Netty + WebSocket + RocketMQ + MongoDB + Redis + ZooKeeper + MySQL”。
画面5：展示方案二“对接第三方服务完成”，并说明“这种方式简单，只需要按照第三方的api进行对接就可以了”。
画面6：展示方案二的说明，提到“如：环信、网易、微信公众平台”。
画面7：再次展示方案一的架构图，聚焦于Netty Server与ZK集群、数据服务的连接。
画面8：展示方案二的详细说明，包括“如何选择？”的对比分析，以及“3、环信”章节标题。
画面9：展示“3、环信”章节，包含环信官网链接“https://www.easemob.com”，并提示“确定建站，满足必选，亿级并发的即时通讯”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
无。

4) PPT 标题、架构图/流程图的结构、表格数据：
架构图结构（画面3）：
- 客户端 → Netty Server
- Netty Server → ZK集群（连接）
- Netty Server → Redis集群
- Netty Server → MongoDB集群
- Netty Server → MySQL集群
- Netty Server → 文件系统

架构图结构（画面2、4、7）：
- 客户端 → Netty Server
- Netty Server → ZK集群（连接）
- Netty Server → Redis集群
- Netty Server → MongoDB集群
- Netty Server → MySQL集群
- Netty Server → 文件系统

表格数据：
无。

5) 无。
