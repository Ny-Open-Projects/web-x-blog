# 画面线理解：15.Kibana入门学习之通过Docker部署安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\15.Kibana入门学习之通过Docker部署安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:14, 00:24, 00:31, 00:44, 00:53, 01:05, 01:21, 01:33, 02:19, 02:28, 02:34, 02:41, 02:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:24:04

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 部署 Elasticsearch、Kibana 和 Redis，并配置 Filebeat 将数据导入 Kibana。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 讲义，标题为“4.2、通过docker部署”，下方列出“#拉取镜像”和“#创建配置文件”步骤，包含代码：docker pull kibana:6.5.4；vim kibana.yml；server.host: "192.168.1.7"；elasticsearch.url: "http://192.168.1.7:9200"。
画面2：终端显示 Kibana 监控插件状态从黄色变为绿色，Elasticsearch 集群模式为 basic，状态 active，服务器在 http://192.168.1.7:5601 监听，但出现“Unhandled rejection Error: No Living connections”错误。
画面3：终端显示进入 kibana-6.5.4-linux-x86_64 目录并执行 ll 命令，列出目录结构。
画面4：终端显示进入 kibana-6.5.4-linux-x86_64 目录，执行 ll 命令，列出目录结构，然后执行 cd .. 命令。
画面5：终端显示进入 kibana-6.5.4-linux-x86_64 目录，执行 ll 命令，列出目录结构，然后执行 cd .. 命令。
画面6：终端显示进入 kibana-6.5.4-linux-x86_64 目录，执行 ll 命令，列出目录结构，然后执行 cd .. 命令。
画面7：EditPlus 编辑器中显示 Docker 创建 Redis 集群节点的命令，包括 redis-node01、redis-node02、redis-node03，以及配置文件和日志文件路径。
画面8：EditPlus 编辑器中显示 Docker 创建 Kibana 容器的命令，包含 --net host 参数和配置文件路径。
画面9：终端显示执行 docker rm kibana 命令删除容器，然后执行 pwd 命令查看当前目录。
画面10：终端显示 Elasticsearch 和 Kibana 插件状态从 uninitialized 变为 yellow，再变为 green，但出现安全警告。
画面11：终端执行 docker ps 命令，列出正在运行的容器，包括 kibana、redis-node01、redis-node02、redis-node03、es-node01、es-node02、es-node03。
画面12：浏览器打开 Kibana 网页，显示空白页面，左侧导航栏包含 Discover、Visualize、Dashboard、Timeline、Canvas、Machine Learning、Infrastructure、Logs、APM、Monitoring、Management、Default、Collapse 等选项。
画面13：PDF 讲义页面，标题为“4.2、通过docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。
画面14：PDF 讲义页面，标题为“4.2、通过docker部署”，下方列出“#拉取镜像”和“#创建配置文件”步骤，包含代码：docker pull kibana:6.5.4；vim kibana.yml；server.host: "192.168.1.7"；elasticsearch.url: "http://192.168.1.7:9200"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
#拉取镜像
docker pull kibana:6.5.4
#创建配置文件
vim kibana.yml
server.host: "192.168.1.7"
elasticsearch.url: "http://192.168.1.7:9200"

画面7：
docker create --name redis-node01 -v /data/redis-data/node01/data --cluster-enabled yes --cluster-config-file nodes-node-01.conf --loglevel debug --logfile nodes-node-01.log redis:5.0.2
docker create --name redis-node02 -v /data/redis-data/node02/data --cluster-enabled yes --cluster-config-file nodes-node-02.conf --loglevel debug --logfile nodes-node-02.log redis:5.0.2
docker create --name redis-node03 -v /data/redis-data/node03/data --cluster-enabled yes --cluster-config-file nodes-node-03.conf --loglevel debug --logfile nodes-node-03.log redis:5.0.2

画面8：
docker create --name kibana --net host -v /haoke/beats/kibana:/usr/share/kibana/config/kibana.yml kibana:6.5.4

画面14：
#拉取镜像
docker pull kibana:6.5.4
#创建配置文件
vim kibana.yml
server.host: "192.168.1.7"
elasticsearch.url: "http://192.168.1.7:9200"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.2、通过docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。
画面13：PPT标题为“4.2、通过docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。
画面14：PPT标题为“4.2、通过docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
