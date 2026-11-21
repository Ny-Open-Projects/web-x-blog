# 画面线理解：05.Elasticsearch实现位置查询之搭建集群

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\05.Elasticsearch实现位置查询之搭建集群_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:57, 02:13, 03:28, 04:12, 05:46, 06:26, 07:03, 08:33, 08:51, 09:11, 09:30, 10:00, 11:05, 11:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:24:15

1) 这一组画面整体在讲什么（一句话）：
搭建并启动一个包含三个节点的 Elasticsearch 集群，包括配置系统参数、创建目录、复制配置文件和使用 Docker 启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：在 Typora 编辑器中展示搭建 Elasticsearch 集群的步骤，包含配置文件和命令。
- 代码：
  # 单个进程可分配线程数
  vm /etc/sysctl.conf
  vm.max_map_count=262144
  # 立即生效
  /sbin/sysctl -p
  mkdir /itcast/tanhua/es-cluster/node01 -p
  mkdir /itcast/tanhua/es-cluster/node02 -p
  mkdir /itcast/tanhua/es-cluster/node03 -p
  # 复制资料目录下的jvm.options到node01, node02, node03目录
  # 在node01目录下，创建elasticsearch.yml文件，并输入如下内容：
  cluster.name: es-tanhua-cluster
  node.name: node01
  node.master: true
  node.data: true
  network.host: 192.168.31.81
  http.port: 9200

画面 2：
- 内容：在 Typora 编辑器中展示搭建 Elasticsearch 集群的步骤，包含配置文件和命令。
- 代码：
  # 单个进程可分配线程数
  vm /etc/sysctl.conf
  vm.max_map_count=262144
  # 立即生效
  /sbin/sysctl -p
  mkdir /itcast/tanhua/es-cluster/node01 -p
  mkdir /itcast/tanhua/es-cluster/node02 -p
  mkdir /itcast/tanhua/es-cluster/node03 -p
  # 复制资料目录下的jvm.options到node01, node02, node03目录
  # 在node01目录下，创建elasticsearch.yml文件，并输入如下内容：
  cluster.name: es-tanhua-cluster
  node.name: node01
  node.master: true
  node.data: true
  network.host: 192.168.31.81
  http.port: 9200

画面 3：
- 内容：在终端中执行创建目录和进入 node01 目录的命令。
- 命令：
  mkdir /itcast/tanhua/es-cluster/node01 -p
  mkdir /itcast/tanhua/es-cluster/node02 -p
  mkdir /itcast/tanhua/es-cluster/node03 -p
  cd /itcast/tanhua/es-cluster/
  ll
  cd node01
  pwd

画面 4：
- 内容：在终端中执行复制 jvm.options 文件到 node01 目录的命令。
- 命令：
  vim jvm.options
  cp jvm.options .. /node02/
  cp jvm.options .. /node03/

画面 5：
- 内容：在终端中执行复制 jvm.options 文件到 node01 目录的命令。
- 命令：
  cp jvm.options .. /node02/
  cp jvm.options .. /node03/

画面 6：
- 内容：在终端中编辑 elasticsearch.yml 文件，显示配置内容。
- 配置：
  node.name: node02
  node.master: true
  node.data: true
  network.host: 192.168.31.81
  http.port: 9201
  discovery.zen.ping.unicast.hosts: ["192.168.31.81"]
  discovery.zen.minimum_master_nodes: 2
  http.cors.enabled: true
  http.cors.allow-origin: "*"

画面 7：
- 内容：在终端中执行复制 jvm.options 文件到 node02 目录的命令。
- 命令：
  cp jvm.options .. /node02/
  cp jvm.options .. /node03/

画面 8：
- 内容：在终端中执行使用 Docker 创建 Elasticsearch 容器的命令。
- 命令：
  docker create --restart=always --name es-node01 -p 9200:9200 -v /itcast/tanhua/es-cluster/node01/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /itcast/tanhua/es-cluster/node01/jvm.options:/usr/share/elasticsearch/config/jvm.options -v es-cluster-node01-data:/usr/share/elasticsearch/data elasticsearch:6.5.4

画面 9：
- 内容：在 Typora 编辑器中展示 Docker 启动命令。
- 代码：
  docker start es-node01 && docker logs -f es-node01
  docker start es-node02 && docker logs -f es-node02
  docker start es-node03 && docker logs -f es-node03

画面 10：
- 内容：在终端中显示 Docker 容器启动日志。
- 日志：
  [2019-10-29T02:57:29,660] [INFO] [o.e.p.PluginsService] [node01] loaded module [mapper-extras]
  [2019-10-29T02:57:29,661] [INFO] [o.e.p.PluginsService] [node01] loaded module [parent-join]
  [2019-10-29T02:57:29,661] [INFO] [o.e.p.PluginsService] [node01] loaded module [rank-eval]
  [2019-10-29T02:57:29,664] [INFO] [o.e.p.PluginsService] [node01] loaded module [repository-url]
  [2019-10-29T02:57:29,664] [INFO] [o.e.p.PluginsService] [node01] loaded module [transport-netty4]
  [2019-10-29T02:57:29,665] [INFO] [o.e.p.PluginsService] [node01] loaded module [tribe]
  [2019-10-29T02:57:29,666] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-core]
  [2019-10-29T02:57:29,667] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-graph]
  [2019-10-29T02:57:29,668] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-logstash]
  [2019-10-29T02:57:29,668] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-ml]
  [2019-10-29T02:57:29,669] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-monitoring]
  [2019-10-29T02:57:29,671] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-rollup]
  [2019-10-29T02:57:29,671] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-security]
  [2019-10-29T02:57:29,673] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-sql]
  [2019-10-29T02:57:29,673] [INFO] [o.e.p.PluginsService] [node01] loaded module [x-pack-watcher]
  [2019-10-29T02:57:29,674] [INFO] [o.e.p.PluginsService] [node01] loaded plugin [ingest-user-agent]
  [2019-10-29T02:57:29,674] [INFO] [o.e.p.PluginsService] [node01] loaded plugin [ingest-user-agent]
  [2019-10-29T02:57:29,675] [INFO
