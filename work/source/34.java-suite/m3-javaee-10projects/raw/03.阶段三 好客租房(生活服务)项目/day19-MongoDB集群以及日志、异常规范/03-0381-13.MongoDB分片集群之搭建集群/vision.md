# 画面线理解：13.MongoDB分片集群之搭建集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\13.MongoDB分片集群之搭建集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 02:19, 03:43, 04:12, 05:59, 06:59, 07:53, 08:45, 09:03, 09:45, 10:09, 12:08, 13:48, 14:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:08:38

1) 这一组画面整体在讲什么（一句话）：
使用 Docker 在单机环境下搭建 MongoDB 的配置服务器（Config Server）和分片集群（Sharded Cluster）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：终端空命令行，左侧文件夹视图显示项目目录结构。
画面2：执行创建三个配置服务器容器的 Docker 命令，指定端口、数据卷和副本集名称。
画面3：显示配置服务器初始化后的 MongoDB Shell 输出，包含集群时间戳和签名信息。
画面4：展示 Typora 编辑器中的 Markdown 文档，内容为 MongoDB 集群搭建步骤，包含创建配置服务器和分片服务器的命令。
画面5：终端执行初始化配置服务器的命令，输出包含选举 ID 和集群时间戳。
画面6：终端连续执行创建六个分片服务器容器的 Docker 命令，指定端口和数据卷。
画面7：Typora 文档中展示初始化分片服务器的命令，包含创建分片服务器的 Docker 命令。
画面8：终端显示分片服务器初始化后的 MongoDB Shell 输出，包含状态信息和同步状态。
画面9：Typora 文档中展示初始化分片服务器的命令，包含创建分片服务器的 Docker 命令。
画面10：终端执行初始化分片服务器的命令，输出包含集群时间戳和签名信息。
画面11：终端显示分片服务器初始化后的 MongoDB Shell 输出，包含状态信息和同步状态。
画面12：终端执行创建 mongos 节点容器的 Docker 命令，指定端口、配置服务器地址和 MongoDB 版本。
画面13：Typora 文档中展示启动 mongos 节点的命令和启用分片的命令。
画面14：Typora 文档中展示启用分片、创建集合和插入测试数据的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
docker create --name configsrvr01 -p 17000:27019 -v mongoconfigsvr-data-01:/data/configdb mongo:4.0.3 --configsvr --replSet "rs_configsvr" --bind_ip_all
docker create --name configsrvr02 -p 17001:27019 -v mongoconfigsvr-data-02:/data/configdb mongo:4.0.3 --configsvr --replSet "rs_configsvr" --bind_ip_all
docker create --name configsrvr03 -p 17002:27019 -v mongoconfigsvr-data-03:/data/configdb mongo:4.0.3 --configsvr --replSet "rs_configsvr" --bind_ip_all

画面4：
#创建三个configsvr节点
docker create --name configsrvr01 -p 17000:27019 -v mongoconfigsvr-data-01:/data/configdb mongo:4.0.3 --configsvr --replSet "rs_configsvr" --bind_ip_all
docker create --name configsrvr02 -p 17001:27019 -v mongoconfigsvr-data-02:/data/configdb mongo:4.0.3 --configsvr --replSet "rs_configsvr" --bind_ip_all
docker create --name configsrvr03 -p 17002:27019 -v mongoconfigsvr-data-03:/data/configdb mongo:4.0.3 --configsvr --replSet "rs_configsvr" --bind_ip_all

#创建三个shard节点，每个分片都有3个数据节点
docker create --name shardsvr01 -p 37000:27018 -v mongoshardsvr-data-01:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr02 -p 37001:27018 -v mongoshardsvr-data-02:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr03 -p 37002:27018 -v mongoshardsvr-data-03:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr

#集群
docker create --name shardsvr04 -p 37003:27018 -v mongoshardsvr-data-04:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr05 -p 37004:27018 -v mongoshardsvr-data-05:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr06 -p 37005:27018 -v mongoshardsvr-data-06:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr

#启动容器
docker start shardsvr01 shardsvr02 shardsvr03

#进入容器执行
docker exec -it shardsvr01 /bin/bash
mongo 172.16.55.185:37000

#初始化集群
rs.initiate(
  {
    "_id": "rs_shardsvr1",
    "members": [
      { "_id": 0, "host": "172.16.55.185:37000" },
      { "_id": 1, "host": "172.16.55.185:37001" },
      { "_id": 2, "host": "172.16.55.185:37002" }
    ]
  }
)

画面5：
docker create --name shardsvr01 -p 37000:27018 -v mongoshardsvr-data-01:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr02 -p 37001:27018 -v mongoshardsvr-data-02:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr03 -p 37002:27018 -v mongoshardsvr-data-03:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr

画面6：
docker create --name shardsvr04 -p 37003:27018 -v mongoshardsvr-data-04:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr05 -p 37004:27018 -v mongoshardsvr-data-05:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr
docker create --name shardsvr06 -p 37005:27018 -v mongoshardsvr-data-06:/data/db mongo:4.0.3 --replSet "rs_shardsvr1" --bind_ip_all --shardsvr

画面7：
#初始化集群
rs.initiate(
  {
    "_id": "rs_shardsvr1",
    "members": [
      { "_id": 0, "host": "172.16.55.185:37000" },
      { "_id": 1, "host": "172.16.55.185:37001" },
      { "_id": 2, "host": "172.16.55.185:37002" }
    ]
  }
)

画面9：
#初始化集群二
rs.initiate(
  {
    "_id": "rs_shardsvr2",
    "members": [
      { "_id": 0, "host": "172.16.55.185:37003" },
      { "_id": 1, "host": "172.16.55.185:37004" },
      { "_id": 2, "host": "172.16.55.185:370
