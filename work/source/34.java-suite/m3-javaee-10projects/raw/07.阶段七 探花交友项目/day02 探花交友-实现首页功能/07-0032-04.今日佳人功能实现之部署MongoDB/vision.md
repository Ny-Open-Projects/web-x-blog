# 画面线理解：04.今日佳人功能实现之部署MongoDB

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\04.今日佳人功能实现之部署MongoDB_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:29, 00:43, 01:08, 01:31, 02:06, 02:17, 02:50, 03:22, 03:39, 03:43, 04:25, 04:47, 04:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:19:07

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 MongoDB，并通过 Robo 3T 客户端连接并查看数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Typora 文档中“2.1、部署MongoDB”章节，列出 Docker 拉取、创建、启动容器的命令，以及进入容器并使用 MongoDB 客户端的命令。
画面 2: 同画面 1，光标在“docker start mongodb”命令行上。
画面 3: 同画面 1，光标在“docker start mongodb”命令行上。
画面 4: 同画面 1，光标在“docker start mongodb”命令行上。
画面 5: 同画面 1，光标在“docker start mongodb”命令行上。
画面 6: 同画面 1，光标在“docker start mongodb”命令行上。
画面 7: 同画面 1，光标在“docker start mongodb”命令行上。
画面 8: 展示终端窗口，显示 MongoDB 启动日志和警告信息，提示访问控制未启用，以及启用免费监控的命令。
画面 9: 同画面 8，终端中已执行“show dbs”命令，显示数据库列表：admin、config、local。
画面 10: 展示 Robo 3T 客户端的启动界面，包含“黑马程序员”和“博学谷”的标志。
画面 11: 展示 Robo 3T 客户端的“MongoDB Connections”窗口，已创建连接“test1”并指向 IP 地址“192.168.31.81:27017”，准备连接。
画面 12: 同画面 8，终端中“show dbs”命令执行完毕，显示数据库信息。
画面 13: 展示 Typora 文档中“2.1、部署MongoDB”章节，光标在“docker start mongodb”命令行上。
画面 14: 同画面 1，光标在“docker start mongodb”命令行上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1-7, 13-14:
```
#拉取镜像
docker pull mongo:4.0.3

#创建容器
docker create --name mongodb --restart=always -p 27017:27017 -v mongodb:/data/db mongo:4.0.3

#启动容器
docker start mongodb

#进入容器
docker exec -it mongodb /bin/bash

#使用MongoDB客户端进行操作
mongo
> show dbs #查询所有的数据库
admin 0.000GB
config 0.000GB
local 0.000GB
```

画面 8-9, 12:
```
2019-09-01T01:49:01.105+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** Read and write access to data and configuration is unrestricted.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine.
2019-09-01T01:49:01.106+0000 I CONTROL [initandlisten] **
