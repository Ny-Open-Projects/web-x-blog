# 画面线理解：06.MongoDB复制集之搭建集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\06.MongoDB复制集之搭建集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:53, 02:06, 02:58, 03:32, 04:36, 05:34, 05:54, 06:22, 06:40, 07:11, 08:28, 09:11, 09:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:04:51

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 在三台虚拟机上搭建 MongoDB 复制集（Replica Set）并进行基本操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档中“1.5. 搭建复制集”章节的代码，包含创建三个 MongoDB 容器的 docker create 命令和启动命令。
画面 2: 在终端中执行 docker create 命令创建第一个容器 mongo01。
画面 3: 显示 Typora 文档中“1.5. 搭建复制集”章节的代码，包含创建三个 MongoDB 容器的 docker create 命令和启动命令。
画面 4: 在终端中执行 docker ps 查看容器状态，然后执行 docker start 启动 mongo02 和 mongo03 容器。
画面 5: 显示 Typora 文档中“1.5. 搭建复制集”章节的代码，包含创建三个 MongoDB 容器的 docker create 命令和启动命令。
画面 6: 在终端中执行 rs.initiate() 命令初始化复制集，显示成功初始化并切换到 PRIMARY 状态。
画面 7: 显示初始化复制集后的返回结果，包含集群时间戳、配置版本和签名信息。
画面 8: 显示复制集成员状态，其中 PRIMARY 节点为 mongo01，SECONDARY 节点为 mongo02。
画面 9: 显示复制集成员状态，其中 PRIMARY 节点为 mongo01，SECONDARY 节点为 mongo02。
画面 10: 在 PRIMARY 节点上创建 test 数据库并插入一条用户记录。
画面 11: 在 PRIMARY 节点上查询刚插入的用户记录，成功返回结果。
画面 12: 在 SECONDARY 节点上尝试查询用户记录，因不是主节点而失败。
画面 13: 在 SECONDARY 节点上执行 rs.slaveOk() 后，查询用户记录成功返回。
画面 14: 显示 Typora 文档中“1.5. 搭建复制集”章节的代码，包含初始化复制集的 rs.initiate() 命令和成功返回结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
#创建Mongo容器
docker create --name mongo01 -p 27017:27017 -v mongo-data-01:/data/db mongo:4.0.3 --repSet "rs0" --bind_ip_all
docker create --name mongo02 -p 27018:27017 -v mongo-data-02:/data/db mongo:4.0.3 --repSet "rs0" --bind_ip_all
docker create --name mongo03 -p 27019:27017 -v mongo-data-03:/data/db mongo:4.0.3 --repSet "rs0" --bind_ip_all

#启动容器
docker start mongo01 mongo02 mongo03

#进入容器操作
docker exec -it mongo01 /bin/bash

#登录到Mongo服务
mongo 172.16.55.185:27017

#初始化复制集配置
rs.initiate({
  _id : "rs0",
  members : [
    { _id : 0, host : "172.16.55.185:27017" },
    { _id : 1, host : "172.16.55.185:27018" },
    { _id : 2, host : "172.16.55.185:27019" }
  ]
})
```

画面 6:
```javascript
rs.initiate({
  _id : "rs0",
  members : [
    { _id : 0, host : "172.16.55.185:27017" },
    { _id : 1, host : "172.16.55.185:27018" },
    { _id : 2, host : "172.16.55.185:27019" }
  ]
})
```

画面 14:
```bash
#进入容器操作
docker exec -it mongo01 /bin/bash

#登录到Mongo服务
mongo 172.16.55.185:27017

#初始化复制集配置
rs.initiate({
  _id : "rs0",
  members : [
    { _id : 0, host : "172.16.55.185:27017" },
    { _id : 1, host : "172.16.55.185:27018" },
    { _id : 2, host : "172.16.55.185:27019" }
  ]
})
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
