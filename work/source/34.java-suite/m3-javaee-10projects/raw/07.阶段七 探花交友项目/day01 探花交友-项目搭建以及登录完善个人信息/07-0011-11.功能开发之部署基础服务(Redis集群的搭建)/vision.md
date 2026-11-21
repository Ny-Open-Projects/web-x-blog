# 画面线理解：11.功能开发之部署基础服务（Redis集群的搭建）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\11.功能开发之部署基础服务（Redis集群的搭建）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:40, 01:38, 02:20, 02:30, 02:40, 02:51, 03:11, 03:46, 03:53, 04:03, 04:54, 05:12, 05:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:05:25

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 Redis 集群，包括创建容器、启动容器、进入容器并执行 Redis 集群初始化命令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于部署 Redis 集群的 Docker 命令，包括创建三个节点的命令和进入容器执行集群命令的步骤。
画面2：展示 Typora 文档中关于部署 Redis 集群的 Docker 命令，包括创建三个节点的命令和进入容器执行集群命令的步骤。
画面3：展示 Typora 文档中关于部署 Redis 集群的 Docker 命令，包括创建三个节点的命令和进入容器执行集群命令的步骤。
画面4：终端中执行了 docker create 命令创建 Redis 容器，显示了 Docker 版本信息。
画面5：终端中执行了 docker ps 命令，列出已运行的容器，包括 mongo、mongodb、mysql、rabbitmq、zookeeper。
画面6：终端中执行了 docker start 命令，启动了 redis-node01、redis-node02、redis-node03 三个容器。
画面7：展示 Typora 文档中关于部署 Redis 集群的 Docker 命令，包括创建三个节点的命令和进入容器执行集群命令的步骤。
画面8：终端中执行了 redis-cli --cluster create 命令，开始创建 Redis 集群，显示了三个节点的 IP 和端口。
画面9：终端中执行了 redis-cli --cluster create 命令，开始创建 Redis 集群，显示了三个节点的 IP 和端口。
画面10：终端中执行了 redis-cli --cluster create 命令，开始创建 Redis 集群，显示了三个节点的 IP 和端口。
画面11：终端中执行了 redis-cli --cluster create 命令，开始创建 Redis 集群，显示了三个节点的 IP 和端口。
画面12：终端中执行了 redis-cli --cluster create 命令，开始创建 Redis 集群，显示了三个节点的 IP 和端口。
画面13：终端中执行了 redis-cli --cluster create 命令，开始创建 Redis 集群，显示了三个节点的 IP 和端口。
画面14：展示 Typora 文档中关于部署 RocketMQ 的内容，包括拉取镜像的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
#创建Redis集群，该集群有3个节点
docker create --name redis-node01 --net host -v redis-node01:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379
docker create --name redis-node02 --net host -v redis-node02:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380
docker create --name redis-node03 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381

#启动容器
docker start redis-node01 redis-node02 redis-node03

#进入redis-node01容器进行操作
docker exec -it redis-node01 /bin/bash

#创建集群
redis-cli --cluster create 192.168.31.81:6379 192.168.31.81:6380 192.168.31.81:6381 --cluster-replicas 0
```

画面8：
```bash
redis-cli --cluster create 192.168.31.81:6379 192.168.31.81:6380 192.168.31.81:6381 --cluster-replicas 0
```

画面12：
```bash
127.0.0.1:6379> set abc 123
(error) MOVED 7638 192.168.31.81:6380
127.0.0.1:6379> 
```

画面13：
```bash
127.0.0.1:6379> set abc 123
(error) MOVED 7638 192.168.31.81:6380
127.0.0.1:6379> 
```

画面14：
```bash
#拉取RocketMQ
docker pull foxiaoxi/rocketmq:server-4.3.2
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
