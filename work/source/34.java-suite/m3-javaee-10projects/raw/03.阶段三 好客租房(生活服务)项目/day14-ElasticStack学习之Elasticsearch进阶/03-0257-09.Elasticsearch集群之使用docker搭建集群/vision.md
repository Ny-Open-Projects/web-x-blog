# 画面线理解：09.Elasticsearch集群之使用docker搭建集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\09.Elasticsearch集群之使用docker搭建集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:30, 02:24, 04:26, 05:42, 07:06, 07:50, 10:07, 11:13, 12:51, 13:51, 14:32, 16:44, 19:08, 20:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:48:45

1) 这一组画面整体在讲如何使用 Docker 搭建并配置一个 Elasticsearch 集群，包括配置文件修改、容器创建和集群健康检查。

2) 按时间顺序列出每张画面的要点：
画面 1: 登录到远程服务器，终端提示符为 root@itcast:~#，左侧显示 /root 目录结构。
画面 2: 编辑 Elasticsearch 配置文件，显示 node.name: node01，node.attr.rack: r1，path.data: /path/to/data，path.logs: /path/to/logs，bootstrap.memory.lock: true。
画面 3: 继续编辑配置文件，显示 discovery.zen.ping.unicast.hosts: ["172.16.55.185"]，http.cors.enabled: true，http.cors.allow-origin: " "，node.master: true，node.data: true。
画面 4: 继续编辑配置文件，显示 network.host: 172.16.55.185，http.port: 9201。
画面 5: 在 node02 上执行命令，显示 grep 结果：cluster.name: es-itcast-cluster，network.host: 172.16.55.185，http.cors.enabled: true，http.cors.allow-origin: " "，node.master: false，node.data: true。
画面 6: 在 EditPlus 编辑器中，显示用于创建 Docker 容器的命令：docker create --name es-node01 --net host -v /haoke/es-cluster/node01/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /haoke/es-cluster/node01/jvm.options:/usr/share/elasticsearch/config/jvm.options -v /haoke/es-cluster/node01/data:/usr/share/elasticsearch/data elasticsearch:6.5.4。
画面 7: 在 EditPlus 编辑器中，显示用于创建 Docker 容器的命令：docker create --name es-node02 --net host -v /haoke/es-cluster/node02/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /haoke/es-cluster/node02/jvm.options:/usr/share/elasticsearch/config/jvm.options -v /haoke/es-cluster/node02/data:/usr/share/elasticsearch/data elasticsearch:6.5.4。
画面 8: 在终端中，显示 Elasticsearch 启动失败的错误日志，包含 java.nio.file.AccessDeniedException。
画面 9: 在终端中，显示 Elasticsearch 启动失败的错误日志，包含 java.nio.file.AccessDeniedException。
画面 10: 在终端中，进入 es-cluster 目录，列出 node01 和 node02 目录，进入 node01 目录，列出 jvm.options 和 elasticsearch.yml 文件。
画面 11: 在终端中，显示 Elasticsearch 启动失败的错误日志，包含 java.nio.file.AccessDeniedException。
画面 12: 在浏览器中打开 Elasticsearch Head 插件，页面为空白。
画面 13: 在 PDF 文档中，显示集群状态查询结果：{"cluster_name": "es-itcast-cluster", "status": "green", "timed_out": false}，并说明主分片和副本分片。
画面 14: 在 PDF 文档中，显示使用 Docker 搭建集群的步骤，包括创建目录和修改配置文件，配置内容为：
cluster.name: es-itcast-cluster
node.name: node01
node.master: true
node.data: true
network.host: 172.16.55.185
http.port: 9200
discovery.zen.ping.unicast.hosts: ["172.16.55.185"]
discovery.zen.minimum_master_nodes: 1
http.cors.enabled: true
http.cors.allow-origin: " "

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
node.name: node01
node.attr.rack: r1
# Paths
path.data: /path/to/data
path.logs: /path/to/logs
# Memory
bootstrap.memory.lock: true

画面 3:
discovery.zen.ping.unicast.hosts: ["172.16.55.185"]
# Prevent the "Split brain" by configuring the majority of nodes (total number of master-eligible nodes / 2 + 1):
discovery.zen.minimum_master_nodes: 1
# Block initial recovery after a full cluster restart until N nodes are started:
gateway.recover_after_nodes: 3
# Require explicit names when deleting indices:
action.destructive_requires_name: true
http.cors.enabled: true
http.cors.allow-origin: " "
node.master: true
node.data: true

画面 4:
# Network
network.host: 172.16.55.185
http.port: 9201

画面 5:
cluster.name: es-itcast-cluster
network.host: 172.16.55.185
http.cors.enabled: true
http.cors.allow-origin: " "
node.master: false
node.data: true

画面 6:
docker create --name es-node01 --net host -v /haoke/es-cluster/node01/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /haoke/es-cluster/node01/jvm.options:/usr/share/elasticsearch/config/jvm.options -v /haoke/es-cluster/node01/data:/usr/share/elasticsearch/data elasticsearch:6.5.4

画面 7:
docker create --name es-node02 --net host -v /haoke/es-cluster/node02/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /haoke/es-cluster/node02/jvm.options:/usr/share/elasticsearch/config/jvm.options -v /haoke/es-cluster/node02/data:/usr/share/elasticsearch/data elasticsearch:6.5.4

画面 14:
cluster.name: es-itcast-cluster
node.name: node01
node.master: true
node.data: true
network.host: 172.16.55.185
http.port: 9200
discovery.zen.ping.unicast.hosts: ["172.16.55.185"]
discovery.zen.minimum_master_nodes: 1
http.cors.enabled: true
http.cors.allow-origin: " "

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13: PDF 文档中，架构图显示 node01 和 node02，node01 有 5 个分片（0-4），node02 有 5 个分片（0-4），并标注“主分片”和“副本分片”。表格数据为集群状态查询结果：{"cluster_name": "es-itcast-cluster", "status": "green", "timed_out": false}。

5) 不要评价画面美观，不要输出与课程无关的内容。
