# 画面线理解：03.MongoDB复制集之架构

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\03.MongoDB复制集之架构【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:17, 01:18, 02:12, 02:15, 02:16, 02:17, 02:19, 02:28, 03:02, 03:04, 03:22, 04:22, 04:23, 04:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:03:41

1) 这一组画面整体在讲什么（一句话）：
讲解 MongoDB 复制集的架构，包括三节点复制集和含 arbiter 节点的复制集的组成、主从选举机制及工作原理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 标题：1.2. 架构
- 内容：基本的架构由3台服务器组成，一个三成员的复制集，由三个数据节点，或者两个数据节点，一个作为仲裁者。
- 图表：三节点复制集架构图（Primary、两个 Secondary，Heartbeat、Replication）
- 文字说明：当主库宕机后，两个从库都会进行竞选，其中一个变为主库，当原主库恢复后，作为从库加入当前的复制集即可。

画面 2：
- 图表：主库宕机后，两个 Secondary 进行选举，最终选出新 Primary。
- 文字说明：Election for New Primary → New Primary Elected。

画面 3：
- 内容：与画面 1 相同，但图中 Primary 节点被红色叉号覆盖，表示主库宕机。
- 文字说明：当主库宕机后，两个从库都会进行竞选，其中一个变为主库，当原主库恢复后，作为从库加入当前的复制集即可。

画面 4：
- 标题：1.2.2. 存在arbiter节点的复制集
- 内容：一个主库，一个从库，可以在选举中成为主库，一个arbiter节点，在选举中，只进行投票，不能成为主库。
- 图表：三节点复制集架构图（Primary、Secondary、Arbiter），Primary 被红色叉号覆盖，下方显示选举流程。

画面 5：
- 标题：1.3. Primary选举
- 内容：复制集通过replSetInitiate命令（或mongo shell的initiate()）进行初始化，初始化后各个成员间开始发送心跳消息，并发起Primary选举操作，获得【大多数】成员投票支持的节点，会成为Primary，其余节点成为Secondary。
- 图表：选举流程图（Secondary 和 Arbiter 之间 Heartbeat，选举后 Primary 和 Arbiter 之间 Heartbeat）。

画面 6：
- 内容：与画面 5 相同，但图中 Primary 节点被红色叉号覆盖，表示主库宕机。
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 7：
- 内容：与画面 5 相同，但图中 Primary 节点被红色叉号覆盖，表示主库宕机。
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 8：
- 标题：1.2.2. 存在arbiter节点的复制集
- 内容：一个主库，一个从库，可以在选举中成为主库，一个arbiter节点，在选举中，只进行投票，不能成为主库。
- 图表：三节点复制集架构图（Primary、Secondary、Arbiter），Primary 被红色叉号覆盖，下方显示选举流程。

画面 9：
- 内容：与画面 8 相同，但图中 Primary 节点被红色叉号覆盖，表示主库宕机。
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 10：
- 内容：与画面 8 相同，但图中 Primary 节点被红色叉号覆盖，表示主库宕机。
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 11：
- 内容：与画面 5 相同，但图中 Primary 节点被红色叉号覆盖，表示主库宕机。
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 12：
- 内容：与画面 5 相同，但图中 Primary 节点被红色叉号覆盖，表示主库宕机。
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 13：
- 标题：1.2.2. 存在arbiter节点的复制集
- 内容：一个主库，一个从库，可以在选举中成为主库，一个arbiter节点，在选举中，只进行投票，不能成为主库。
- 图表：三节点复制集架构图（Primary、Secondary、Arbiter），Primary 被红色叉号覆盖，下方显示选举流程。

画面 14：
- 标题：1.2. 架构
- 内容：基本的架构由3台服务器组成，一个三成员的复制集，由三个数据节点，或者两个数据节点，一个作为仲裁者。
- 图表：三节点复制集架构图（Primary、两个 Secondary，Heartbeat、Replication）。
- 文字说明：当主库宕机后，两个从库都会进行竞选，其中一个变为主库，当原主库恢复后，作为从库加入当前的复制集即可。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5：
复制集通过replSetInitiate命令（或mongo shell的initiate()）进行初始化，初始化后各个成员间开始发送心跳消息，并发起Primary选举操作，获得【大多数】成员投票支持的节点，会成为Primary，其余节点成为Secondary。

【大多数】的定义
假设复制集内成员数量为N，则大多数为 N/2 + 1，当复制集内存活成员数量不足大多数时，复制集会选举失败。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
- 标题：1.2. 架构
- 图表结构：
  - Primary → Secondary（Replication）
  - Primary ←→ Secondary（Heartbeat）
  - Secondary ←→ Secondary（Heartbeat）
- 文字说明：当主库宕机后，两个从库都会进行竞选，其中一个变为主库，当原主库恢复后，作为从库加入当前的复制集即可。

画面 2：
- 图表结构：
  - Primary 被红色叉号覆盖。
  - Secondary ←→ Secondary（Heartbeat）。
  - 下方箭头指向：New Primary Elected。
  - New Primary Elected → Secondary（Replication）。
  - New Primary Elected ←→ Secondary（Heartbeat）。

画面 4：
- 标题：1.2.2. 存在arbiter节点的复制集
- 图表结构：
  - Primary → Secondary（Replication）
  - Primary ←→ Secondary（Heartbeat）
  - Primary ←→ Arbiter（Heartbeat）
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 5：
- 标题：1.3. Primary选举
- 图表结构：
  - Secondary ←→ Arbiter（Heartbeat）
  - 下方箭头指向：New Primary Elected。
  - New Primary Elected ←→ Arbiter（Heartbeat）。
  - New Primary Elected → Secondary（Replication）。
  - New Primary Elected ←→ Secondary（Heartbeat）。

画面 8：
- 标题：1.2.2. 存在arbiter节点的复制集
- 图表结构：
  - Primary → Secondary（Replication）
  - Primary ←→ Secondary（Heartbeat）
  - Primary ←→ Arbiter（Heartbeat）
- 文字说明：当主库宕机时，将会选择从库成为主库，主库修复后，将其加入到现有的复制集即可。

画面 14：
- 标题：1.2. 架构
- 图表结构：
  - Primary → Secondary（Replication）
  - Primary ←→ Secondary（Heartbeat）
  - Secondary ←→ Secondary（Heartbeat）
- 文字说明：当主库宕机后，两个从库都会进行竞选，其中一个变为主库，当原主库恢复后，作为从库加入当前的复制集即可。
