# 画面线理解：13-flume高可用-failover-模型分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\13-flume高可用-failover-模型分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:48, 00:50, 01:24, 01:57, 02:31, 03:04, 03:38, 04:12, 04:38, 04:45, 05:19, 05:26, 05:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:06:31

1) 这一组画面整体在讲什么（一句话）：
演示如何在 node01 上配置 Flume Agent，使其采集文件新增数据并分发到 node02 和 node03 上的 Flume Agent。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“3. 高可用方案”中的“3.1. 角色分配”部分，表格列出 Agent1、Collector1、Collector2 的 HOST 和角色。
画面2：空白绘图软件界面。
画面3：绘图软件界面，光标在画布中央。
画面4：绘制了三个节点框，分别标注为 node01、node02、node03，node01 内部标注“Agent”。
画面5：在左上角添加文本框，内容为“需求: 1:node01去采集一个文件的新增数据”。
画面6：在文本框中追加内容“2:node01采集数据之后发送给node02 或者node03的flume的Agent”。
画面7：从 node01 的“Agent”框引出两条带箭头的线，分别指向 node02 和 node03 的“Agent”框。
画面8：在 node01 的“Agent”框右侧添加一个虚线框。
画面9：在虚线框内输入配置信息：“Source: exec Channel:memory Sink:avro”。
画面10：将虚线框内的配置信息调整为：“Source: exec Channel:memory Sink:avro”（内容未变）。
画面11：在 node01 的“Agent”框左侧添加一个虚线框。
画面12：在左侧虚线框内输入配置信息：“Source:avro Channel:memory Sink:hdfs”。
画面13：在 node03 的“Agent”框右侧添加一个虚线框。
画面14：在右侧虚线框内输入配置信息：“Source:avro Channel:memory Sink:hdfs”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
Flume的Agent和Collector分布如下表所示：
名称      HOST        角色
Agent1    node01      Web Server
Collector1 node02      AgentMstr1
Collector2 node03      AgentMstr2
```
画面9：
```
Source: exec
Channel:memory
Sink:avro
```
画面12：
```
Source:avro
Channel:memory
Sink:hdfs
```
画面14：
```
Source:avro
Channel:memory
Sink:hdfs
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3. 高可用方案”，子标题“3.1. 角色分配”，表格内容如上。
画面7：架构图结构：node01 的“Agent”框 → node02 的“Agent”框（箭头）；node01 的“Agent”框 → node03 的“Agent”框（箭头）。
画面9：在 node01 的“Agent”框右侧添加一个虚线框，框内文字为“Source: exec Channel:memory Sink:avro”。
画面12：在 node02 的“Agent”框左侧添加一个虚线框，框内文字为“Source:avro Channel:memory Sink:hdfs”。
画面14：在 node03 的“Agent”框右侧添加一个虚线框，框内文字为“Source:avro Channel:memory Sink:hdfs”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
