# 画面线理解：08.MongoDB复制集之增加arbiter节点

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\08.MongoDB复制集之增加arbiter节点【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:32, 00:55, 01:16, 02:13, 02:43, 04:02, 04:25, 05:22, 06:05, 06:41, 07:19, 07:40, 08:11, 09:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:06:11

1) 这一组画面整体在讲什么（一句话）：
演示如何通过添加仲裁节点（arbitrator）来解决 MongoDB 副本集在主节点故障时无法选举新主节点的问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1: 在 MongoDB 副本集的 SECONDARY 节点上执行插入操作，因不是主节点而报错。
画面2: 使用 docker 命令停止 mongo03 容器。
画面3: 在 SECONDARY 节点上查询副本集状态，显示其同步源为 mongo01。
画面4: 使用 docker 命令启动 mongo03 容器。
画面5: 在 SECONDARY 节点上查询副本集状态，显示其状态为 PRIMARY，但配置版本为 -1，表明存在配置不一致。
画面6: 在 PRIMARY 节点上执行 rs.status()，显示其状态为 PRIMARY，但随后日志显示尝试重新连接失败，接着成功重新连接。
画面7: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 2。
画面8: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 3。
画面9: 展示了 Markdown 文档中关于“增加arbitrator节点”的测试步骤。
画面10: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 5。
画面11: 使用 docker 命令创建并启动一个新的 MongoDB 容器 mongo04，并将其加入副本集。
画面12: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 3。
画面13: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 5。
画面14: 展示了 Markdown 文档中关于“增加arbitrator节点”的测试步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
rs0:SECONDARY> db.user.insert({"id" : 1003, "name" : "wangwu"})
WriteCommandError({
  "operationTime" : Timestamp(1551779827, 1),
  "ok" : 0,
  "errmsg" : "not master",
  "code" : 10107,
  "codeName" : "NotMaster",
  "$clusterTime" : {
    "clusterTime" : Timestamp(1551779827, 1),
    "signature" : {
      "hash" : BinData(0, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="),
      "keyId" : NumberLong(0)
    }
  }
})
rs0:SECONDARY> db.user.find()
{ "_id" : ObjectId("5c7e43aebad2c3f5c4280dca"), "id" : 1001, "name" : "zhangsan" }
{ "_id" : ObjectId("5c7e47b24b6a894337b0b0e7"), "id" : 1002, "name" : "lisi" }
{ "_id" : ObjectId("5c7e47b24b6a894337b0b0e7"), "id" : 1003, "name" : "wangwu" }

画面2:
root@itcast:~# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
0fe207830106        mongo:4.0.3         "docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# docker stop mongo03
mongo03
root@itcast:~# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
0fe207830106        mongo:4.0.3         "docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# docker start mongo03
mongo03

画面3:
{
  "optimeDurable" : {
    "ts" : Timestamp(155179817, 1),
    "t" : NumberLong(2)
  },
  "optimeDate" : ISODate("2019-03-05T09:56:57Z"),
  "optimeDurableDate" : ISODate("2019-03-05T09:56:57Z"),
  "lastHeartbeat" : ISODate("2019-03-05T11:02:50.898Z"),
  "lastHeartbeatRecv" : ISODate("2019-03-05T11:02:51.421Z"),
  "pingMs" : NumberLong(0),
  "syncingTo" : "",
  "syncSourceHost" : "",
  "syncSourceId" : -1,
  "infoMessage" : "",
  "configVersion" : 1
}

画面4:
root@itcast:~# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
0fe207830106        mongo:4.0.3         "docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# docker start mongo03
mongo03
root@itcast:~# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
4b39968a0c1b        mongo:4.0.3         "docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
0fe207830106        mongo:4.0.3         "docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
c45c4b1594d        mongo:4.0.3         "docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# docker start mongo03
mongo03

画面5:
{
  "id" : 1,
  "name" : "172.16.55.185:27018",
  "health" : 1,
  "state" : 1,
  "stateStr" : "PRIMARY",
  "uptime" : 4232,
  "optime" : {
    "ts" : Timestamp(1551783771, 1),
    "t" : NumberLong(3)
  },
  "optimeDurable" : {
    "ts" : Timestamp(1551783771, 1),
    "t" : NumberLong(3)
  },
  "optimeDate" : ISODate("2019-03-05T11:02:50Z"),
  "optimeDurableDate" : ISODate("2019-03-05T11:02:50Z"),
  "lastHeartbeat" : ISODate("2019-03-05T11:04:31.381Z"),
  "lastHeartbeatRecv" : ISODate("2019-03-05T11:04:31.381Z"),
  "pingMs" : NumberLong(0),
  "syncSourceId" : -1,
  "infoMessage" : "Error connecting to 172.16.55.185:27017 :: caused by ::"
}

画面6:
rs0:PRIMARY> rs.status()
2019-03-05T11:04:42.058+0000 I NETWORK  [js] trying reconnect to 172.16.55.185:27018 failed
2019-03-05T11:04:42.059+0000 I NETWORK  [js] reconnect 172.16.55.185:27018 ok
rs0:SECONDARY>

画面7:
2019-03-05T11:05:51.777+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2019-03-05T11:05:51.777+0000 I STORAGE  [initandlisten] ** See http://dochub
