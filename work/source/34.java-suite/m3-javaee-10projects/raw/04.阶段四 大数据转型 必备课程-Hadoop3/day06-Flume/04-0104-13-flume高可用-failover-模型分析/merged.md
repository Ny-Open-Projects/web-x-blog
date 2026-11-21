# 13-flume高可用-failover-模型分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\13-flume高可用-failover-模型分析【海量资源尽在 ubkz.com】.mp4
- 时长 6分9秒（音频 370s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来继续学习Floom我们来学一个Floom的一个高可用方案所谓的高可用呢就是我们可以搭建一个Floom的一个集群当某一个Floom挂掉之后呢而其他的Floom可以快速的作为补充OK这就是所谓的高可用在这里呢我们提供一个Floom的一个高可用的方案来看一下在这里呢我准备了三台主机
[00:27] 分别在每一台主机上启动一个flume的一个实例那么第一台呢是node01它呢作为一个我们的一个主节点而node02 node03呢作为我们的一个从节点那么这个集群搭建完之后要去解决什么需求呢我来给大家画一下来打开我们的画图是这样的好这里边有三台主机我们来先来画一下这个是我们的node01好node01
[00:59] 那么还有两个这是我们的node02node03node02node03那我们呢可以分别在每台机子上启动一个urgent进程urgent实例也就是flume的urgent实例好这里urgent这里urgentOK这里urgent那么这三个urgent分别做什么事情呢我们来提一下我们的需求需求需求呢第一
[01:39] 就是node01node01去去采集一个文件的新增数据一提到这个新增数据你立刻就想到我们刚做过的那个tel-f是不是可以监控文件的变化对就是那个这是第一个需求第二个这是第二个第二个的话呢node01采集数据之后那么发送给
[02:16] node02或者或者node03的flume实例的flume二进团flume二进团也就是说这个node01负责采集采集完之后呢发给node02或者node03在这里我为什么用或呢是这样的我们这里呢我们为了体现这个高可用呢我呢可以这样我呢给某一个
[02:50] 记子发比如说我先给node02这个agent发数据当node02这个记子挂掉之后呢这个时候是不是就出现故障了那这个node03呢可以快速的作为补充这个呢可以实现他们两个之间的高可用我要做这么一件事情好了那么要做这么一件事情的话我们来想一想我们需要做什么事情呢我们是不是还是那几个步骤啊第一配置对吧第二个呢我们来启动Floom实例第三来测试
[03:20] 也是这样的一个道理那接下来问题是如何实现配置呢配置无非就是配置每一台主机它的三个组件SourceChannelSync对不对好那接下来咱们先做一个初步的分析咱们来分析一下它们每一个Urgent它的三个组件首先看第一个Node01这个Node01的话呢咱们先看看它的一个Source是一个什么类型这个Source的话呢表示数据从哪里来
[03:49] 我们这里呢去采集一个文件的新增数据那么是不是要监控tl-f的结果所以说它的source是execOK那再看到的channelchannel这个channel呢咱们一直用的是memory channelmemory channel所以说呢这个还是memory好那么还有呢它的一个什么呢它的一个sync关键是这个sync怎么写咱们这个node01
[04:19] 它收集到这个数据之后它要发给node02和node03它是不是要发给下一机的agent这个时候多个agent之间的一个传递我们这个sync用什么用咱们刚学过这个evr用这个这是它的一个三个组件写完了写完之后咱们看左边这个那么这个对于node02来讲它也有三个组件一个是sauce它的sauce怎么写
[04:48] 它的数据是不是从这个node01过来的那么它是多个agent之间的一个集点所以说这个时候呢它也要error好那它的这个channel呢还是用memory我们还是用memory好这个那接下来再说它的sync我们这个sync呢比如说我们node02收到数据之后想去保存到哪里呢我们可以把它保存到hdfs所以这里呢我写hdfs可以吧
[05:23] OK好了那么这个node02完了还有node03呢那node03我们会发现它和node02是不是一样啊好但是呢这个配置和以往不同的是在哪里呢我如何做到node02这个二进它挂掉之后呢那么这个时候node03立刻就上位呢或者立刻作为补充呢这个地方有一个叫它的一个处理机制有一个叫什么故障转移机制故障转移机制那么我们这里边用的叫
[05:52] 一个故障转移机制叫Failover待会大家会看到这个词叫Failover这叫故障转移它挂掉它立刻作为补充OK好那么关于它的整个简单的一个模型呢咱们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

