# 画面线理解：04.RocketMQ的核心概念讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\04.RocketMQ的核心概念讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:28, 02:29, 03:26, 04:48, 05:42, 06:08, 07:05, 07:56, 09:17, 10:04, 10:52, 12:04, 12:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:56:06

1) 这一组画面整体在讲 RocketMQ 的核心架构与核心概念，通过手绘流程图和 PPT 讲解生产者、消费者、NameServer 和 Broker 的交互关系。

2) 按时间顺序列出每张画面的要点：
画面 1: 打开绘图软件，准备绘制架构图。
画面 2: 绘制出 producer、consumer 和一个中间的连接框。
画面 3: 添加 nameserver 节点，并用连线连接 producer 和 nameserver。
画面 4: 添加 broker 节点，连接 producer 到 broker，并标注“发送消息”，连接 consumer 到 broker，并标注“查找broker”。
画面 5: 将 broker 节点扩展为一个“broker集群”，并标注“broker集群”。
画面 6: 保持当前结构，未新增内容。
画面 7: 在右侧添加一个放大框，准备展示 broker 内部结构。
画面 8: 在放大框内绘制出 topic 和 Message queue 的结构。
画面 9: 保持当前结构，未新增内容。
画面 10: 切换到 PPT，显示“1.3、核心概念说明”页面，内容为 Producer、Consumer、NameServer 的定义。
画面 11: 切换回绘图软件，保持当前结构。
画面 12: 在放大框内调整“Message queue”文字位置。
画面 13: 保持当前结构，未新增内容。
画面 14: 切换到 PPT，显示“1.3、核心概念说明”页面，内容为 Producer、Consumer、NameServer 的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
PPT 标题：1.3、核心概念说明
架构图结构：
- Producer Cluster → NameServer Cluster → Broker Cluster → Consumer Cluster
- Producer Cluster 与 NameServer Cluster 之间有“注册”关系。
- NameServer Cluster 与 Broker Cluster 之间有“路由”关系。
- Broker Cluster 与 Consumer Cluster 之间有“消费”关系。
表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
