# 画面线理解：13.Elasticsearch集群之故障转移（主节点宕机）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\13.Elasticsearch集群之故障转移（主节点宕机）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:18, 00:32, 00:45, 00:54, 01:33, 01:44, 01:56, 02:18, 02:41, 02:48, 03:05, 04:03, 04:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:50:42

1) 这一组画面整体在讲什么（一句话）：
演示在 Elasticsearch 集群中，通过停止并重启节点来观察集群状态变化及“脑裂”问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档内容，说明 node01 恢复后重新加入集群并重新分配节点信息，下方给出命令：docker stop es-node02。
画面2：Elasticsearch Head 界面显示集群状态为绿色（12 of 12），node01、node02、node03 分别持有分片 0123、1345、0245。
画面3：Elasticsearch Head 界面空白，无数据。
画面4：终端显示 node01 被停止，node03 被启动，集群健康状态从 RED 变为 YELLOW，再变为 GREEN。
画面5：终端显示 docker ps 命令输出，列出容器状态，包括 es-node01、es-node02、es-node03。
画面6：Elasticsearch Head 界面空白。
画面7：PDF 文档内容，与画面1相同，说明将 node02 停止。
画面8：Elasticsearch Head 界面显示集群状态为黄色（8 of 12），node01 为 master，node03 持有分片 0245，下方文字说明集群重新选举并状态变黄。
画面9：Elasticsearch Head 界面空白。
画面10：终端显示 docker ps 命令输出，列出容器状态，包括 es-node01、es-node02、es-node03。
画面11：Elasticsearch Head 界面空白。
画面12：终端显示 docker stop es-node03 命令，随后 docker start es-node03 命令。
画面13：Elasticsearch Head 界面空白。
画面14：PDF 文档内容，说明恢复 node02 后，发现 node02 未加入集群，指出这是“脑裂”问题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
docker stop es-node02

画面4：
root@itcast:node03# docker stop es-node01
root@itcast:node03# docker start es-node01
root@itcast:node03# docker stop es-node01
root@itcast:node03# docker start es-node03
root@itcast:node03# docker ps

画面5：
root@itcast:node03# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
5f18b673160        elasticsearch:6.5.4   "/usr/local/bin/do..."   21 minutes ago      Up 21 minutes       9200/tcp, 9300/tcp   es-node01
620a4f1649b3        elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 20 minutes       9200/tcp, 9300/tcp   es-node02
ead2df7792aa        elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 2 minutes        9200/tcp, 9300/tcp   es-node03
ffbebf54f1a        mongo:4.0.3           "docker-entrypoint..."   3 weeks ago          Up 28 hours         0.0.0.0:27017->27017/tcp   mongodb
a081ff6822e        percona:5.7.23        "docker-entrypoint..."   7 weeks ago          Up 28 hours         0.0.0.0:3306->3306/tcp   percona

画面10：
root@itcast:node03# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
5f18b673160        elasticsearch:6.5.4   "/usr/local/bin/do..."   21 minutes ago      Up 21 minutes       9200/tcp, 9300/tcp   es-node01
620a4f1649b3        elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 20 minutes       9200/tcp, 9300/tcp   es-node02
ead2df7792aa        elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 2 minutes        9200/tcp, 9300/tcp   es-node03
ffbebf54f1a        mongo:4.0.3           "docker-entrypoint..."   3 weeks ago          Up 28 hours         0.0.0.0:27017->27017/tcp   mongodb
a081ff6822e        percona:5.7.23        "docker-entrypoint..."   7 weeks ago          Up 28 hours         0.0.0.0:3306->3306/tcp   percona

画面12：
root@itcast:node03# docker stop es-node03
root@itcast:node03# docker start es-node03

画面14：
docker start es-node02

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：
PPT 标题：从结果中可以看出，集群对 master 进行了重新选举，选择 node01 为 master，并且集群状态变黄。
架构图/流程图结构：
- node01（master）指向分片 012345。
- node03 指向分片 0245。
- 集群状态显示为黄色（8 of 12）。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
