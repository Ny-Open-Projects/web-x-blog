# 画面线理解：14.Elasticsearch集群之故障转移（脑裂问题）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\14.Elasticsearch集群之故障转移（脑裂问题）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:35, 04:11, 05:09, 07:19, 07:41, 08:10, 08:44, 09:09, 09:25, 09:48, 10:01, 11:01, 11:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:51:17

1) 这一组画面整体在讲什么（一句话）：
讲解Elasticsearch集群在节点恢复后出现脑裂问题，并通过设置minimum_master_nodes参数解决该问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档中Elasticsearch集群状态，node01为master，集群状态为黄色，node02和node03的分片状态显示为0、1、2、3、4、5。
画面2：PDF文档显示“2.4.3、脑裂问题”小节标题，说明重启node02后发现其无法加入集群。
画面3：PPT图示展示node01主节点宕机后，node01恢复导致“双主”现象，即脑裂问题。
画面4：PPT图示展示node01恢复后出现“双主”问题，并给出解决方案：设置minimum_master_nodes参数。
画面5：终端显示Elasticsearch配置文件中的discovery.zen.minimum_master_nodes: 1，用于演示脑裂问题。
画面6：终端显示操作命令，包括docker stop和docker start命令，用于停止和启动容器。
画面7：终端显示操作命令，包括cd进入配置目录、vim编辑配置文件、以及docker start启动容器。
画面8：Elasticsearch Head界面显示集群状态为绿色，node03为主节点，node01和node02为从节点。
画面9：Elasticsearch Head界面显示集群状态为绿色，node03为主节点，node01、node02、node03的分片状态显示为0、1、2、3、4、5。
画面10：Elasticsearch Head界面显示集群状态为绿色，node03为主节点，node01和node02为从节点。
画面11：Elasticsearch Head界面显示集群状态为绿色，node03为主节点，node01和node02为从节点。
画面12：终端显示Elasticsearch日志，包含节点启动和集群状态信息。
画面13：PDF文档显示node02恢复后正常加入集群，分片状态显示为1、3、4、5。
画面14：PDF文档展示“双主”问题图示和解决方案，强调设置minimum_master_nodes参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
discovery.zen.ping.unicast.hosts: ["172.16.55.185"]
# Prevent the "split brain" by configuring the majority of nodes (total number of master-eligible nodes / 2 + 1):
discovery.zen.minimum_master_nodes: 1
# For more information, consult the zen discovery module documentation.
# Block initial recovery after a full cluster restart until N nodes are started:
gateway.recover_after_nodes: 3
# For more information, consult the gateway module documentation.
# Various
# Require explicit names when deleting indices:
action.destructive_requires_name: true
http.cors.enabled: true
http.cors.allow-origin: "*"
node.master: true
node.data: true

画面6：
root@itcast:node03# docker stop es-node03
es-node03
root@itcast:node03# docker start es-node03
es-node03
root@itcast:node03# docker stop es-node01 es-node02 es-node03
es-node01
es-node02
es-node03
root@itcast:node03# cd es-cluster
root@itcast:node03# cd node02
root@itcast:node03# vim elasticsearch.yml

画面7：
root@itcast:node03# docker stop es-node03
es-node03
root@itcast:node03# cd es-cluster
root@itcast:node03# cd node02
root@itcast:node03# vim elasticsearch.yml
root@itcast:node03# cd node01
root@itcast:node03# vim elasticsearch.yml
root@itcast:node03# docker start es-node01 es-node02 es-node03

画面12：
root@itcast:node03# docker stop es-node03
es-node03
root@itcast:node03# docker stop es-node02
es-node02
root@itcast:node03# docker stop es-node01
es-node01

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
架构图结构：
- 上层：node01 (M) → node02 (M) → node03
- 下层：node01 (M) → node02 (M) → node03
- 注释：node01主节点宕机，node01恢复，出现了双主，即脑裂问题。

画面4：
架构图结构：
- 上层：node01 (M) → node02 (M) → node03
- 下层：node01 (M) → node02 (M) → node03
- 注释：node01恢复，出现了双主，即脑裂问题。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
