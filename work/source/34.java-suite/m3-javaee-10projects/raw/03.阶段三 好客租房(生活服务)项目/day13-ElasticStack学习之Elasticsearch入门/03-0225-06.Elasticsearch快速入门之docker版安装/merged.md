# 06.Elasticsearch快速入门之docker版安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\06.Elasticsearch快速入门之docker版安装【海量资源尽在 ubkz.com】.mp4
- 时长 3分51秒（音频 231s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么前面呢我们讲了单机版的安装那么接下来呢我们来讲一下通过这个Docker去做一个安装那么当然了通过这个Docker安装肯定是非常简单的对吧来看一下那么首先第一步拉取镜像这个呢我就不做拉取了那么我已经拉取到我的这个本机了好,那么下面我们来看一下这个创建容器的这个命令那么我们把这个命令拷贝过来那么显然呢我们可以看到这个命令我相信大家应该并不陌生了
[00:27] 然后我们通过DockerCrate创建一个容器名字就是叫ElectSearch然后指定它的一个网络就是网络的一个模式就是host模式并且给它设置参数什么参数就是我们是一个单节点的这样的一个模式然后并且设置它的一个NetworkHost就是我们本机的地址然后指定镜像就可以了
[00:53] OK好然后呢我们把它拷贝过来然后再去做一个执行走那么这个容器呢就已经创建好了那么创建好之后呢我们就可以去启动它了那么启动之后呢我们是不是就可以去查看进程对吧OK那么这样我们就直接来做一个启动吧启动然后呢通过一个dockerlogs-f是不是可以做一个跟随它的一个日志的一个更新那我们来看它那个日志的一个启动的一个情况
[01:21] 好那么我们现在看到了他已经也跑起来了那么捕获几个关键字对吧starting正在启动然后去监听我们端口今天对了当然了我可以看到端口已经变成9201了为什么9201原因是我们刚刚服务是不是没有去把它停掉所以它是就又去加了一个就是我们9200后面加一个1那么这样我们还是把它停掉一下那么通过 Docker然后 stop
[01:50] 然后呢去先把我们这个容器先停掉然后呢我们去找一下我们这个进程q6779去做一个杀死那么这样检查一下检查一下是不是就没有了然后呢我们再去做一个Docker的一个启动那么这样我们去这么来玩Docker start然后以search end然后呢去查看这个进程
[02:16] 好那么我们等待它的一个启动那么现在呢它也跑起来了我们来看一下那么我们捕获几个关键字那么starting启动然后呢我们来看一下这个是绑定的这个监听这个端口9200是ok的然后呢已经启动了ok好那么下面我们来访问一下9200这个端口的服务那么依然是不是还是刚才都访问的这个地址啊然后呢走那么其实可以看到那么这个是不是就是刚刚我们所看到的这个类似的一个信息
[02:45] 但这个名字是不一样的对吧OK好他的cluster这个ID肯定也是不一样的然后但是他的下面的信息呢这个是一样的包括他的lucent的版本是7.5.0那都是一样的OK好嘞那么这个呢就是我们通过这个Docker去做一个安装最终我们所看到的一个效果它都是一样的但是我们会发现通过这个Docker的安装是不是就会简单很多啊在这需要说明的一点是我们现在使用这个Docker的安装呢
[03:15] 简单的一种方式就是我们并没有去给他去挂载一些这个数据的目录为什么呢原因是我们是不是还是需要把数据写到我们的elite设置中啊那么现在呢他是会将数据写到他容器内部这样的话显然是不合适的我们需要把它挂载到外面来但是由于呢我们现在是仅仅做于用于这个开发测试那么所以呢我们就不去做一个具体目录的目录的挂载那么等到我们后面去讲集群的时候呢我们再去讲这样的一个配置啊
[03:45] OK好嘞那么关于一个Docker的一个这样的一个安装那我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 安装并管理 Elasticsearch 服务，包括拉取镜像、创建容器、启动服务、查看日志及使用 kill 命令终止进程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 PDF 文档，标题为“2.2.4. 使用Docker安装”，内容包含步骤：#拉取镜像、#创建容器、#启动、#查看日志。
画面 2: 在 EditPlus 编辑器中，高亮显示创建容器的 Docker 命令：Docker create --name Elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" Elasticsearch:6.5.4。
画面 3: 在终端中，执行 Docker rm Elasticsearch 删除容器，然后执行 Docker images 查看镜像列表。
画面 4: 继续在终端中执行 Docker create 命令创建名为 Elasticsearch 的容器。
画面 5: 在终端中执行 Docker start Elasticsearch 启动容器，然后执行 Docker logs -f Elasticsearch 查看实时日志。
画面 6: 显示 Elasticsearch 启动日志，包含节点初始化、插件加载等信息。
画面 7: 显示 Elasticsearch 启动日志，包含磁盘水位过高警告和分片重定位信息。
画面 8: 在终端中执行 Docker stop Elasticsearch 停止容器。
画面 9: 在终端中执行 kill 6779 命令终止进程。
画面 10: 在终端中执行 kill 6779 命令后，执行 Docker start Elasticsearch 重新启动服务。
画面 11: 显示 Elasticsearch 重新启动后的日志，包含节点初始化、插件加载等信息。
画面 12: 在 Advanced REST Client 中，显示 Elasticsearch 的集群信息，包括 name、cluster_name、version 等。
画面 13: 显示 PDF 文档，内容包含步骤：#拉取镜像、#创建容器、#启动、#查看日志。
画面 14: 显示 PDF 文档，内容与画面 1 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
#拉取镜像
Docker pull Elasticsearch:6.5.4

#创建容器
Docker create --name Elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" Elasticsearch:6.5.4

#启动
Docker start Elasticsearch

#查看日志
Docker logs Elasticsearch

画面 2:
Docker create --name Elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" Elasticsearch:6.5.4

画面 3:
root@iltcast:~# Docker rm Elasticsearch
root@iltcast:~# Docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
Elasticsearch       6.5.4               93199c1d5909        13 days ago         774 MB
centos              7                   1e11168e4c2c        2 weeks ago         202 MB
foxisho/RocketMQ    broker-4.3.2       9e853e279e13        4 weeks ago         377 MB
foxisho/RocketMQ    server-4.3.2       4794ca253a6c        4 weeks ago         377 MB
redis               5.0.2              5959914c5588        5 weeks ago         94.9 MB
mongo               4.1                75f939a18fd9        5 weeks ago         390 MB
ruby                3.5                bdb0c50d6a1b        6 weeks ago         869 MB
ZooKeeper           3.4.5              c6d7f8d264c0        6 weeks ago         128 MB
mongo               4.0.3              0563651ee24e        2 months ago        382 MB
percona             5.7.23             134d5e56e9f9        2 months ago        404 MB
Styletang/RocketMQ-console-ng  5.7.23  174f3b0e638            16 months ago        782 MB
mobz/Elasticsearch-head  5  1b95c598e4b3            24 months ago        824 MB

root@iltcast:~# Docker create --name Elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" Elasticsearch:6.5.4

画面 4:
root@iltcast:~# Docker create --name Elasticsearch --net host -e "discovery.type=single-node" -e "network.host=172.16.55.185" Elasticsearch:6.5.4

画面 5:
root@iltcast:~# Docker start Elasticsearch
root@iltcast:~# Docker logs -f Elasticsearch

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

