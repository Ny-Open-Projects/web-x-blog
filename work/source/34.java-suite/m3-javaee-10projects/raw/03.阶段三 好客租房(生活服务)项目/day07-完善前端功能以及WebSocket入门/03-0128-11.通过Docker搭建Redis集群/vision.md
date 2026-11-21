# 画面线理解：11.通过Docker搭建Redis集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\11.通过Docker搭建Redis集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 02:50, 04:10, 06:01, 07:06, 07:47, 08:41, 09:09, 09:52, 10:47, 11:24, 14:20, 15:10, 17:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:25:00

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 搭建 Redis 集群，包括创建容器、启动服务、初始化集群和验证集群状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“使用Docker搭建Redis集群”的章节，包含创建三个 Redis 容器的 Docker 命令。
画面 2: 在 EditPlus 编辑器中，高亮显示了创建三个 Redis 容器的 Docker 命令。
画面 3: 在 EditPlus 编辑器中，高亮显示了启动三个 Redis 容器的 Docker 命令。
画面 4: 在 Xshell 终端中，执行了创建容器的命令，并查看了容器列表，随后进入 redis-node01 容器。
画面 5: 在 Xshell 终端中，执行了 redis-cli 命令以创建 Redis 集群，显示了哈希槽分配过程。
画面 6: 在 Xshell 终端中，继续执行 redis-cli 命令，提示需要确认配置。
画面 7: 在 Xshell 终端中，用户输入 'yes' 确认配置，集群开始发送 CLUSTER MEET 消息。
画面 8: 在 Xshell 终端中，用户停止了三个 Redis 容器，并删除了数据目录。
画面 9: 展示 PDF 文档中关于“删除容器和数据目录”及“重新创建集群”的章节，包含相关命令。
画面 10: 在 Xshell 终端中，执行了 docker inspect 命令查看容器网络配置。
画面 11: 在 Xshell 终端中，执行了 redis-cli 命令创建集群，显示了哈希槽分配完成。
画面 12: 在 Xshell 终端中，执行了 redis-cli 命令，验证了集群的节点状态和槽位覆盖情况。
画面 13: 在 Xshell 终端中，执行了 redis-cli 命令，从不同节点查询数据，验证集群功能。
画面 14: 展示 PDF 文档中关于“查看集群信息”的章节，包含集群状态的截图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
#拉取镜像
docker pull redis:5.0.2

#创建容器
docker create --name redis-node01 -v /data/redis-data/node01:/data -p 6379:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf
docker create --name redis-node02 -v /data/redis-data/node02:/data -p 6380:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf
docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf

#启动容器
docker start redis-node01 redis-node02 redis-node03

#开始创建集群
#进入redis-node01进行操作
docker exec -it redis-node01 /bin/bash
```

画面 2:
```bash
docker create --name redis-node01 -v /data/redis-data/node01:/data -p 6379:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf
docker create --name redis-node02 -v /data/redis-data/node02:/data -p 6380:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf
docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf
```

画面 3:
```bash
docker start redis-node01 redis-node02 redis-node03
docker exec -it redis-node01 /bin/bash
```

画面 4:
```bash
root@itcast:~# docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379 redis:5.0.2 --cluster-config-file nodes-node-03.conf
57f41507aa82  redis:5.0.2  "docker-entrypoint..."  4 seconds ago  Created
root@itcast:~# docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS
57f41507aa82        redis:5.0.2         "docker-entrypoint..."  4 seconds ago       Created
6b9c986651e5        redis:5.0.2         "docker-entrypoint..."  5 seconds ago       Created
381b7436e274        redis:5.0.2         "docker-entrypoint..."  5 seconds ago       Created
a801fcf982ce        percona:5.3         "docker-entrypoint..."  2 weeks ago         Up 11 days
0f2181>2181/tcp, 388/tcp  zk
9f4a71b7b20c5        zookeeper:3.5      "docker-entrypoint..."  3 weeks ago         Up 11 days
redis-node01
redis-node02
redis-node03
root@itcast:~# docker exec -it redis-node01 /bin/bash
```

画面 5:
```bash
root@itcast:~# docker exec -it redis-node01 /bin/bash
root@8381b47306c74:/data# redis-cli --cluster create 172.17.0.1:6379 172.17.0.1:6380 172.17.0.1:6381 --cluster-replicas 0
>>> Performing hash slots allocation on 3 nodes...
Master[1] -> Slots 0 - 5460
Master[2] -> Slots 10923 - 16383
M: 9126a6a3a30fe16a037940fa43613ba67ed9fc 172.17.0.1:6379
M: 46e0c2d41ff83eccd4bb7a285ee04668fd25a 172.17.0.1:6380
M: 1582808ad949cb60fd14f1993d417d0ee102d86 172.17.0.1:6381
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
```

画面 6:
```bash
root@8381b47306c74:/data# redis-cli --cluster create 172.17.0.1:6379 172.17.0.1:6380 172.17.0.1:6381 --cluster-replicas 0
>>> Performing hash slots allocation on 3 nodes...
Master[1] -> Slots 0 - 5460
Master[2] -> Slots 10923 - 16383
M: 9126a6a3a30fe16a037940fa43613ba67ed9fc 172.17.0.1:6379
M: 46e0c2d41ff83eccd4bb7a285ee04668fd25a 172.17.0.1:6380
M: 1582808ad949cb60fd14f1993d417d0ee102d86 172.17.0.1:6381
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
```

画面 7:
```bash
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
...
root@itcast
