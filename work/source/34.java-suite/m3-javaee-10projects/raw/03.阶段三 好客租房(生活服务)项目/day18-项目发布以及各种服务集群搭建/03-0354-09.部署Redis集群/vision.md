# 画面线理解：09.部署Redis集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\09.部署Redis集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:34, 02:35, 03:40, 04:10, 04:50, 05:13, 06:23, 06:57, 07:40, 08:01, 08:39, 09:30, 12:36, 13:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:51:31

1) 这一组画面整体在讲什么（一句话）：
部署 Redis 集群并验证其集群状态，随后开始部署 Elasticsearch 集群。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Redis 集群规划表，包含 6 个节点的端口、IP 和容器名。下方有创建卷的命令。
画面 2: 显示创建 Redis 容器的命令，从 redis-node01 到 redis-node06，每个容器指定不同的端口和配置文件。
画面 3: 继续显示创建 Redis 容器的命令，聚焦于 redis-node02 到 redis-node06 的创建。
画面 4: 显示终端中正在执行创建 redis-node04、redis-node05、redis-node06 容器的命令。
画面 5: 终端显示创建 redis-node04、redis-node05、redis-node06 容器的命令执行成功，随后执行 docker ps 查看容器状态。
画面 6: 终端显示 docker ps 命令的输出，显示 redis-node05、redis-node06 等容器已启动。
画面 7: 显示 Redis 集群启动命令和进入 redis-node01 容器的命令。
画面 8: 终端显示创建 redis-node04、redis-node05、redis-node06 容器时因名称冲突报错。
画面 9: 终端显示尝试删除冲突容器，但 redis-node05 不存在，redis-node06 也不存在。
画面 10: 显示 Redis 集群启动命令和进入 redis-node01 容器的命令，下方有 shell1 窗口显示 Redis 集群的 IP 地址。
画面 11: 终端显示 docker ps 命令的输出，显示 redis-node05、redis-node06 等容器已启动。
画面 12: 显示 Redis 集群启动命令和进入 redis-node01 容器的命令，下方有 shell1 窗口显示 Redis 集群的 IP 地址。
画面 13: 终端显示 redis-cli 连接 Redis 集群并执行 cluster create 命令，显示集群状态。
画面 14: 显示 Elasticsearch 集群规划表，包含 3 个节点的端口、IP 和容器名。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```markdown
2.2. 部署Redis集群

2.2.1. 规划
服务	端口	服务器	容器名
Redis-node01	6379	192.168.1.18	redis-node01
Redis-node02	6380	192.168.1.18	redis-node02
Redis-node03	6381	192.168.1.18	redis-node03
Redis-node04	16379	192.168.1.19	redis-node04
Redis-node05	16380	192.168.1.19	redis-node05
Redis-node06	16381	192.168.1.19	redis-node06
```

画面 2:
```markdown
2.2.3. 实施
1 docker volume create redis-node01
2 docker volume create redis-node02
3 docker volume create redis-node03
4 docker volume create redis-node04
5 docker volume create redis-node05
6 docker volume create redis-node06
7 #创建容器
8 docker create --name redis-node01 --net host -v redis-node01:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379
9 docker create --name redis-node02 --net host -v redis-node02:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380
10 docker create --name redis-node03 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
11 docker create --name redis-node04 --net host -v redis-node04:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-04.conf --port 16379
12 docker create --name redis-node05 --net host -v redis-node05:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-05.conf --port 16380
13 docker create --name redis-node06 --net host -v redis-node06:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-06.conf --port 16381
```

画面 3:
```markdown
14 docker create --name redis-node01 --net host -v redis-node01:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379
15 docker create --name redis-node02 --net host -v redis-node02:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380
16 docker create --name redis-node03 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
17 docker create --name redis-node04 --net host -v redis-node04:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-04.conf --port 16379
18 docker create --name redis-node05 --net host -v redis-node05:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-05.conf --port 16380
19 docker create --name redis-node06 --net host -v redis-node06:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-06.conf --port 16381
```

画面 4:
```bash
root@itcast03:bin# docker create --name redis-node04 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 16379
45e0937ce1975c0af2ec9c2a8e88f5fe0fb3804b957c2e9f08931f09c143f
root@itcast03:bin# docker create --name redis-node05 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 16380
549d0cad953ad20a6d01537648e5b88a0a5909138e6998d3857734e6370
root@itcast03:bin# docker create --name redis-node06 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 16381
7801e5663cd74975f5ca471fc4269d1713bf75b06b932a1d4303bc9aa63de
```

画面 5:
```bash
root@itcast03:bin# docker start redis-node04 redis-node05 redis-node06
redis-node04
redis-node05
redis-node06
root@itcast03:bin# docker ps
CONTAINER ID	PORTS	IMAGE	NAMES	CREATED	STATUS
549dcaf953a	redis:5.0.2	redis-node05	"docker-entrypoint.s..."	57 seconds ago	Up 5 seconds
6961c4a418d	haproxy	1.9.3	haproxy	"docker-entrypoint.s..."	34 hours ago	Up 18 minutes
3017fe035c3	percona:5.7.23	ms_node2	"docker-entrypoint.s..."	35 hours ago	Up 18 minutes
5308acb31e22	percona:5.7
