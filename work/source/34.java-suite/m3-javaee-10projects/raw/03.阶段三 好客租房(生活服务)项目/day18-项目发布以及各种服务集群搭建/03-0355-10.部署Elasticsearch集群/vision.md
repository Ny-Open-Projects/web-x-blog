# 画面线理解：10.部署Elasticsearch集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\10.部署Elasticsearch集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 02:40, 04:14, 06:05, 07:28, 08:21, 09:49, 11:16, 12:28, 13:44, 14:57, 16:21, 17:36, 18:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:52:25

1) 这一组画面整体在讲什么（一句话）：
部署一个由三个节点组成的 Elasticsearch 集群，包括规划、配置文件修改、容器创建与启动，以及集群初始化和文档映射。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程文档中关于部署 Elasticsearch 集群的规划部分，包含一个表格，列出了三个节点的服务器 IP 和容器名。
画面 2: 在终端中，用户进入 es-cluster 目录，列出文件，然后删除 node01、node02、node03 三个节点的目录。
画面 3: 展示了 Elasticsearch 配置文件中关于网络和发现的设置，包括 network.host、http.port、discovery.zen.ping.unicast.hosts 和 discovery.zen.minimum_master_nodes。
画面 4: 用户在终端中执行 docker create 命令，尝试创建名为 es-node01 的容器，但因容器名冲突而失败。
画面 5: 展示了因权限不足导致的 java.nio.AccessDeniedException 错误日志。
画面 6: 展示了 Elasticsearch 启动日志，显示 node01 加载了多个插件，如 rank-eval、repository-url、tribe 等。
画面 7: 展示了 Elasticsearch 配置文件中关于内存和网络的设置，包括 bootstrap.memory_lock、network.host 和 http.port。
画面 8: 用户在终端中执行 scp 命令，将配置文件从 node01 复制到 node03，但因 SSH 认证问题被拒绝。
画面 9: 展示了 node02 启动日志，显示加载了多个插件，如 aggs-matrix-stats、ingest-common、lang-mustache 等。
画面 10: 展示了 node02 启动日志，显示 JVM 参数和内存设置。
画面 11: 展示了 Elasticsearch 配置文件中关于 master 节点和 gateway 的设置，包括 discovery.zen.minimum_master_nodes、node.master、node.data 和 http.cors.enabled。
画面 12: 展示了 node01 无法连接到 master 节点的错误日志。
画面 13: 用户在终端中编辑 elastic search 配置文件。
画面 14: 展示了课程文档中关于文档 mapping 的部分，包含一个 PUT 请求的 JSON 配置，设置索引的 shards 和 replicas 数量。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```markdown
2.3、部署Elasticsearch集群
Elasticsearch集群需要3个节点的集群。
2.3.1、规划
| 服务 | 端口 | 服务器 | 容器名 |
| --- | --- | --- | --- |
| es-node01 | 9200, 9300 | 192.168.1.7 | es-node01 |
| es-node02 | 9200, 9300 | 192.168.1.18 | es-node02 |
| es-node03 | 9200, 9300 | 192.168.1.19 | es-node03 |
```

画面 2:
```bash
root@bitcast01:es-cluster# ll
total 36
drwxr-xr-x 7 root root 4096 Feb 28 15:44 /
-rwxr-xr-x 3 root root 2935 Jan 18 22:45 ./
-rwxr-xr-x 3 root root 3198 Jan 9 12:51 .ik/
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198 Jan 28 15:44 ./
-rwxr-xr-x 3 root root 3198
