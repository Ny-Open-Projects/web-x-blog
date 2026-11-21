# 画面线理解：3-HDFS的文件副本机制

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\3-HDFS的文件副本机制【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 03:20, 03:49, 06:05, 06:11, 06:25, 08:43, 08:50, 08:58, 09:22, 09:26, 09:33, 12:28, 12:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:54:39

1) 这一组画面整体在讲 HDFS 文件副本和 Block 块存储机制，包括文件如何被分割成块、块如何在多个 DataNode 上存储副本、以及副本的分布策略。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 HDFS 文件系统架构，NameNode 存储元数据，DataNode 存储文件内容，以及 Block Replication 的概念图。
画面 2: 展示一个 300M 文件被分割成三个块（128M, 128M, 44M），并由 NameNode 管理，三个 DataNode 作为存储节点。
画面 3: 展示 hdfs-site.xml 配置文件中设置 NameNode 数据目录的配置项。
画面 4: 展示文件块副本机制，每个块分布在不同的 DataNode 上，图示中显示了块的副本分布。
画面 5: 展示 hdfs-site.xml 配置文件中设置 DataNode 数据目录、NameNode HTTP 地址、副本数、权限等配置项。
画面 6: 展示文件块副本机制图，与画面 4 类似，但图示中显示了块的副本分布。
画面 7: 展示百度搜索页面，搜索框中输入“机架”。
画面 8: 展示百度图片搜索结果页面，搜索关键词为“机架”。
画面 9: 展示百度图片搜索结果中的一个服务器机架图片。
画面 10: 展示一个绘图软件界面，图示中显示了 DataNode 的存储块分布。
画面 11: 展示一个空白的绘图软件界面。
画面 12: 展示文件块副本机制图，图示中显示了块的副本分布，并标注了“机架感知”。
画面 13: 展示一个客户端访问 HDFS 的流程图，客户端请求被路由到 rack1 和 rack2 中的 DataNode。
画面 14: 展示文件块副本机制图，图示中显示了块的副本分布。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet type="text/xsl" href="configuration.xsl">
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///export/servers/hadoop-3.1.1/datas/namenode/namenodedatas</value>
  </property>
</configuration>
```

画面 5:
```xml
<property>
  <name>dfs.datanode.data.dir</name>
  <value>file:///export/servers/hadoop-3.1.1/datas/datanode/datanodeDatas</value>
</property>
<property>
  <name>dfs.namenode.http-address</name>
  <value>node01:50070</value>
</property>
<property>
  <name>dfs.replication</name>
  <value>3</value>
</property>
<property>
  <name>dfs.permissions.enabled</name>
  <value>false</value>
</property>
<property>
  <name>dfs.namenode.checkpoint.edits.dir</name>
  <value>file:///export/servers/hadoop-3.1.1/datas/dfs/nn/edits</value>
</property>
<property>
  <name>dfs.namenode.secondary.http-address</name>
  <value>node01.hadoop.com:50090</value>
</property>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“1.4 HDFS 文件副本和 Block 块存储”，图示中 NameNode 指向三个 DataNode。
画面 2: 图示中 NameNode 指向三个 DataNode。
画面 4: 图示中 NameNode 指向三个 DataNode，每个 DataNode 中包含不同颜色的块。
画面 6: 图示中 NameNode 指向三个 DataNode，每个 DataNode 中包含不同颜色的块。
画面 12: 图示中 NameNode 指向三个 DataNode，每个 DataNode 中包含不同颜色的块，并标注了“机架感知”。
画面 13: 图示中 Client 指向 rack1 中的 DataNode，rack1 中的 DataNode 指向 rack2 中的 DataNode。

5) 不要评价画面美观，不要输出与课程无关的内容。
