# 画面线理解：06.Elasticsearch快速入门之docker版安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\06.Elasticsearch快速入门之docker版安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:53, 00:56, 01:07, 01:16, 01:24, 01:47, 01:53, 01:59, 02:14, 02:34, 02:41, 02:59, 03:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:28:19

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 安装并管理 Elasticsearch 服务，包括拉取镜像、创建容器、启动服务、查看日志及使用 kill 命令终止进程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 PDF 文档，标题为“2.2.4. 使用docker安装”，内容包含步骤：#拉取镜像、#创建容器、#启动、#查看日志。
画面 2: 在 EditPlus 编辑器中，高亮显示创建容器的 Docker 命令：docker create --name elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" elasticsearch:6.5.4。
画面 3: 在终端中，执行 docker rm elasticsearch 删除容器，然后执行 docker images 查看镜像列表。
画面 4: 继续在终端中执行 docker create 命令创建名为 elasticsearch 的容器。
画面 5: 在终端中执行 docker start elasticsearch 启动容器，然后执行 docker logs -f elasticsearch 查看实时日志。
画面 6: 显示 Elasticsearch 启动日志，包含节点初始化、插件加载等信息。
画面 7: 显示 Elasticsearch 启动日志，包含磁盘水位过高警告和分片重定位信息。
画面 8: 在终端中执行 docker stop elasticsearch 停止容器。
画面 9: 在终端中执行 kill 6779 命令终止进程。
画面 10: 在终端中执行 kill 6779 命令后，执行 docker start elasticsearch 重新启动服务。
画面 11: 显示 Elasticsearch 重新启动后的日志，包含节点初始化、插件加载等信息。
画面 12: 在 Advanced REST Client 中，显示 Elasticsearch 的集群信息，包括 name、cluster_name、version 等。
画面 13: 显示 PDF 文档，内容包含步骤：#拉取镜像、#创建容器、#启动、#查看日志。
画面 14: 显示 PDF 文档，内容与画面 1 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
#拉取镜像
docker pull elasticsearch:6.5.4

#创建容器
docker create --name elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" elasticsearch:6.5.4

#启动
docker start elasticsearch

#查看日志
docker logs elasticsearch

画面 2:
docker create --name elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" elasticsearch:6.5.4

画面 3:
root@iltcast:~# docker rm elasticsearch
root@iltcast:~# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
elasticsearch       6.5.4               93199c1d5909        13 days ago         774 MB
centos              7                   1e11168e4c2c        2 weeks ago         202 MB
foxisho/rocketmq    broker-4.3.2       9e853e279e13        4 weeks ago         377 MB
foxisho/rocketmq    server-4.3.2       4794ca253a6c        4 weeks ago         377 MB
redis               5.0.2              5959914c5588        5 weeks ago         94.9 MB
mongo               4.1                75f939a18fd9        5 weeks ago         390 MB
ruby                3.5                bdb0c50d6a1b        6 weeks ago         869 MB
zookeeper           3.4.5              c6d7f8d264c0        6 weeks ago         128 MB
mongo               4.0.3              0563651ee24e        2 months ago        382 MB
percona             5.7.23             134d5e56e9f9        2 months ago        404 MB
Styletang/rocketmq-console-ng  5.7.23  174f3b0e638            16 months ago        782 MB
mobz/elasticsearch-head  5  1b95c598e4b3            24 months ago        824 MB

root@iltcast:~# docker create --name elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" elasticsearch:6.5.4

画面 4:
root@iltcast:~# docker create --name elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" elasticsearch:6.5.4

画面 5:
root@iltcast:~# docker start elasticsearch
root@iltcast:~# docker logs -f elasticsearch

画面 6:
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] node name derived from node ID [VsaZJSG]
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] version [6.5.4], pid[1], build[default] from [VsaZJSG] (build [6.5.4])
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] OS[Linux/x86_64] (build [4.4.0-138-generic/amd64]), JVM[Oracle Corporation/OpenJDK 64-Bit Server VM 1.8.0_171-b11]
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721+08:00] [VsaZJSG] [VsaZJSG] started
[2018-12-31T12:50:01.721
