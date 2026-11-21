# 画面线理解：12.Elasticsearch集群之故障转移（data节点宕机）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\12.Elasticsearch集群之故障转移（data节点宕机）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:44, 02:25, 02:46, 03:00, 03:16, 03:26, 03:38, 03:55, 04:25, 05:09, 05:47, 06:08, 07:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:50:04

1) 这一组画面整体在讲什么（一句话）：
演示 Elasticsearch 集群在节点故障后如何恢复，包括创建索引、查看集群状态、节点分配变化及恢复操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 PDF 文档中，弹出“新建索引”对话框，索引名称为“haoke”，分片数为“6”，副本数为“1”，并点击“OK”。
画面 2: 在 Elasticsearch Head 界面，显示索引“haoke”在三个节点（node01、node02、node03）上均分配了分片，集群状态为“green”。
画面 3: Elasticsearch Head 界面空白，无数据。
画面 4: Elasticsearch Head 界面空白，无数据。
画面 5: Elasticsearch Head 界面空白，无数据。
画面 6: Elasticsearch Head 界面空白，无数据。
画面 7: Elasticsearch Head 界面空白，无数据。
画面 8: 在 PDF 文档中，显示“Unassigned”分片状态，node02 和 node03 的分片分配情况，以及说明文字。
画面 9: Elasticsearch Head 界面空白，无数据。
画面 10: 在 PDF 文档中，显示“Unassigned”分片状态，node02 和 node03 的分片分配情况，以及说明文字。
画面 11: 在 PDF 文档中，显示“docker start es-node01”命令，以及 Elasticsearch Head 界面中 node02 和 node03 的分片分配情况。
画面 12: Elasticsearch Head 界面空白，无数据。
画面 13: Elasticsearch Head 界面空白，无数据。
画面 14: 在 PDF 文档中，显示“docker start es-node01”命令，以及 Elasticsearch Head 界面中 node02 和 node03 的分片分配情况。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1: 索引名称: haoke
分片数: 6
副本数: 1
画面 11: docker start es-node01
画面 14: docker start es-node01

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: 说明文字：
• 需要连接到node2的端口9201进行查看状态
• 当前集群状态为黄色，表示主节点不可用，副本节点分配不完全可用
过一段时间观察，发现节点列表中看不到node01，副本节点分配到了node02和node03，集群状态恢复到绿色。
画面 10: 说明文字：
• 需要连接到node2的端口9201进行查看状态
• 当前集群状态为黄色，表示主节点不可用，副本节点分配不完全可用
过一段时间观察，发现节点列表中看不到node01，副本节点分配到了node02和node03，集群状态恢复到绿色。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
