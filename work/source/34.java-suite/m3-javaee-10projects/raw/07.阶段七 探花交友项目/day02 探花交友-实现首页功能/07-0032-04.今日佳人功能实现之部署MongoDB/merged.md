# 04.今日佳人功能实现之部署MongoDB

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\04.今日佳人功能实现之部署MongoDB_【海量资源尽在 666java.com】.mp4
- 时长 5分7秒（音频 307s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下部署mongodb那么在前面呢我们其实可以看到我们这个mongodb呢主要呢是用于我们数据的一些存储那么推荐系统呢会将一些我们结果数据呢去写入到mongodb中然后呢我们会通过mongodb做一些查询的这样的一些操作那么也就是说我们必须要有一个mongodb这样的一个支持才可以的
[00:26] 好那么接下来呢我们就来部署一下那么首先呢我们需要说明一下就是我们这个MongoDB呢依然采用的是什么呢Docker去做一个这个安装啊OK好那么我们实际的来操作一下那么我们还是呢在我们这台机器呢去做一个安装那么我们首先呢去做一个镜像的一个拉曲就是我们去破这个Mongo这个版本呢我们所使用的是4.0.3啊这样的一个版本然后呢我们回车
[00:56] 那么去拉取这个镜像回车拉取镜像那我们其实我这个镜像呢其实已经存在了如果说你之前没有去拉取过的话那么它会重新做一个这个下载然后呢接下来呢我们就来创建我们的一个MongoDB的一个容器那我们来看一下我们使用的是这个Docker Create这样的一个命令那么容器的名字呢就叫MongoDB
[01:21] 然后我们设置它的一个重启就随着我们的一个计算机的一个重启去做一个重启也就是我们刚刚这台服务器那么服务器重启它就会跟着重启我们这个容器这样的话我们会比较方便一些然后我们所设置它的一个端口的映射就是27017映射到27017然后这个是我们的外部的一个端口对吧然后我们去通过更微去挂载我们的一个
[01:48] 这个数据的一个目录那么叫mongodb指向到这个位置来这个是容器中的一个目录然后这个就是我们的这个镜像的一个名称了然后呢我们去把这个命令来拷贝一下到这个位置呢去做一个执行那么其实可以看到呢我们这个容器呢就已经创建好了那么接下来呢我们通过一个Docker start一个命令来启动我们这个容器啊我们来dock start mongodb啊做一个启动
[02:17] 那么启动完成之后呢我们就需要进入到我们的容器中呢做一些这个操作啊那我们可以来检查一下就是我们这个MongoDB是否已经就已经启动成功了我们来看一下啊那么我们就去start启动之后呢我们去通过这个dockerexec-it然后去进入到这个MongoDB啊然后做一些这个操作那么我们来操作一下走
[02:44] 那么这样的话就进入到我们容器了那么下面我们输入一个什么的mongo这样的一个命令那么其实可以看到它已经就连接到了我们mongo db的服务那么接下来我们通过一个什么售一个什么就是dbs那么通过这个sodbs
[03:04] 那么就可以去查看我们当前的一些这个数据库默认是不是就会有三个啊这样的数据库啊那么其实看到这儿呢我们就知道了哦那么我们现在已经呢就把我们的mongodb这个服务呢就已经安装好了那么刚刚这个操作呢我们是通过这个我们的这个容器啊进入容器呢通过命令行呢做操作啊那么我们也可以通过客户端呢去做一个操作那么接下来呢我们来看一下啊
[03:31] 那么在这呢我安装了客户端叫这个Robo这个这样的一个客户端那么我们可以来打开它呢我们通过这个客户端呢去做一个操作啊那么我们需要连接到我这台机器的这个27017的这样的一个端口那么如果说如果说我们第一次去打开这个软件的话那么我们并没有这个连接啊所以我们需要去按的添加一个这样的一个连接啊就可以了那我们去设置我们的一个这个地址
[04:00] 和一个端口啊就OK好那么我们选中它做一个连接那么连接成功之后呢可以看到在这个位置呢是不是已经看到一些相关我们MongoDB的一些这个信息然后呢下面有一些这么system啊然后呢config啊一些数据库啊哎OK好那么后面的操作呢我们将基于我们这个客户端或者是我们采用这个命令行的方式呢去做一个啊这样的一个操作哎OK好那我们来看一下我们的一个讲义啊
[04:28] 那么刚刚呢我们说到我们进入了这个容器呢我们使用这个mongo啊这样的一个命令呢做一个操作通过一些这个mongo db的一些这个查询的命令呢就可以做一些操作了比如说我们刚刚所使用的就是一个db使啊做这样的一个操作然后呢我们也可以通过一个客户端工具啊这个rebo这个客户端工具做一个这个操作
[04:52] OK好那么到目前为止我们是不是就已经完成了一个mongodb的一个部署以及安装后面我们就基于它来做操作OK好那么关于部署mongodb我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 MongoDB，并通过 Robo 3T 客户端连接并查看数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Typora 文档中“2.1、部署MongoDB”章节，列出 Docker 拉取、创建、启动容器的命令，以及进入容器并使用 MongoDB 客户端的命令。
画面 2: 同画面 1，光标在“Docker start mongodb”命令行上。
画面 3: 同画面 1，光标在“Docker start mongodb”命令行上。
画面 4: 同画面 1，光标在“Docker start mongodb”命令行上。
画面 5: 同画面 1，光标在“Docker start mongodb”命令行上。
画面 6: 同画面 1，光标在“Docker start mongodb”命令行上。
画面 7: 同画面 1，光标在“Docker start mongodb”命令行上。
画面 8: 展示终端窗口，显示 MongoDB 启动日志和警告信息，提示访问控制未启用，以及启用免费监控的命令。
画面 9: 同画面 8，终端中已执行“show dbs”命令，显示数据库列表：admin、config、local。
画面 10: 展示 Robo 3T 客户端的启动界面，包含“黑马程序员”和“博学谷”的标志。
画面 11: 展示 Robo 3T 客户端的“MongoDB Connections”窗口，已创建连接“test1”并指向 IP 地址“192.168.31.81:27017”，准备连接。
画面 12: 同画面 8，终端中“show dbs”命令执行完毕，显示数据库信息。
画面 13: 展示 Typora 文档中“2.1、部署MongoDB”章节，光标在“Docker start mongodb”命令行上。
画面 14: 同画面 1，光标在“Docker start mongodb”命令行上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1-7, 13-14:
```
#拉取镜像
Docker pull mongo:4.0.3

#创建容器
Docker create --name mongodb --restart=always -p 27017:27017 -v mongodb:/data/db mongo:4.0.3

#启动容器
Docker start mongodb

#进入容器
Docker exec -it mongodb /bin/bash

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

