# 8.8 Superset docker安装

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day8 数据可视化
- 源文件：06.阶段六 冷链监控平台项目\day8 数据可视化\8.8 Superset docker安装_【海量资源尽在 666java.com】.mp4
- 时长 5分28秒（音频 328s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来安装一下SuperSight在这里我们使用了这个SuperSight使用Docker的方式来安装SuperSight那么我们首先进入到我们的Linux操作系统里边我们当前的环境是CentOS 7那么我们先搜索一下searchsearch的话SuperSight我们search SuperSight的时候它会列出来我们SuperSight的镜像
[00:28] 我们直接使用第一个镜像这个镜像是官方的一个镜像我们Docker Core然后SuiteSite的镜像名称那此时它会下载SuiteSite的镜像到你本地的这个镜像库这个下载过程呢取决于网络速度如果网速快的话那下载的就会快一些那么我们此时已经下载完了如果下载完了之后呢下一步我们可以先看一下Docker PS
[00:58] DockerImageDockerImage的话它会查看我们本地有哪一些镜像我的当前的镜像已经下载下来了那下一步我们就可以直接创建我们的这个SuperSight容器我DockerRun-D然后-P这个-P的话是两个端口的一个映射一个是在容器里边端口一个是在我们宿主机端口第一个实际上是宿主机的端口7088然后
[01:26] 冒号的时候80888088是SuperSight默认的一个端口在这里我给它改了一下把宿主机的端口改成7088让大家能够理解我们7088代表的是当前的宿主机的8088代表的是我们的容器里边的那么我们在我们的页面上访问的时候我们就使用7088这个端口来进行访问就可以了那我设置完端口之后我们再设置一个我们本地和就是说宿主机的
[01:56] 和这个容器里边的目录的一个映射也就是说我的-v然后加上一个opt Docker然后-superset那它冒号之后冒号什么呢冒号home-superset也就是说在这个里边的时候我们前面部分-v的这个参数的前面部分是我们当前宿主机也就是说我们主机的一个
[02:26] 主机的一个目录那么冒号后面呢是容器里边的一个目录那此时我们再加上我们super set的名称然后直接回车它就会创建了一个super set我们到处ps我们看到当前的这个super set已经启动起来了而且它的这个端它的它的这个容器id也拿到了那下一步我们就要初始化我们的数据库设置我们的用户名和密码那么我们先进入到
[02:56] 我们的容器里边ELEC-IT然后呢我们进到容器里边然后容器IDbin使用这个命令那下一步的话我们再使用super set dbupgrade回车OK它会把服务器的一些数据给它数据库给它创建上包括一些组件给它给它执行一下安装一下
[03:27] 那下一步的话是我们初始化super set的super setinit我们执行了这个passing的一个命令然后它实际上就是执行passing的一个脚本吧它会初始化我们的这个super set那目前是初始化完了初始化完了之后下一步我们就要创建super set的用户名和密码fabmanager然后great-domain-appsuper set那
[04:00] 这个fab命令也是一个也是一个那个passing的一个命令吧它创建了一个执行了一个脚本之后它是执行这个创建用户名的用户名和用户名的一个命令那我直接回车回车之后呢它会提示我输入用户名如果用户名不输入的话就是默认是admin然后呢force name
[04:24] 和lastname我们都是回撤下一步的话密码是我们输入admin123回撤再重新输入密码admin123ok此时它就会给我们创建好了我们的super set了那如果我们要想查看我们这个super set它的一个容器是什么样的呢这样是我们通过我们的这个我们可以跳出来在速度机里边我们
[04:54] 使用使用Docker的命令来查看它的日志Docker PS我们拿到IDDocker log-f然后呢把ID给它迁建上然后此时它就会看到我们的这个看到我们的这个什么看到我们这个日志了然后我们其实在我们的页面上就可以通过7088这个端口来访问我们的这个服务器这是我们整个的
[05:25] SuperSight的安装的一个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Linux 终端中通过 Docker 拉取并运行 Superset 数据可视化平台，并初始化管理员账户。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：终端初始状态，提示符为 [root@iZ2hbkgy36gawe9luintZ ~]#。
画面2：执行 Docker search supersert 命令，列出多个 Superset 相关的 Docker 镜像。
画面3：执行 Docker pull Docker.io/amancevice/superset 命令，拉取镜像。
画面4：执行 Docker run 命令启动容器，参数包括 -d（后台运行）、-p 7000:7000（端口映射）、-v /opt/superset:/home/superset（数据卷挂载）。
画面5：执行 Docker exec 命令进入容器，参数为 -it 58488c34c5（容器ID）/bin/bash。
画面6：在容器内执行 superset init 命令，开始初始化数据库和权限。
画面7：superset init 命令执行中，输出大量数据库迁移日志。
画面8：superset init 命令执行中，继续输出数据库迁移日志。
画面9：在容器内执行 superset manager create-admin --app superset 命令，开始创建管理员账户。
画面10：执行 superset manager create-admin --app superset 命令，提示输入用户名、邮箱、密码。
画面11：执行 superset manager create-admin --app superset 命令，提示输入确认密码。
画面12：执行 superset manager create-admin --app superset 命令，输入确认密码后，命令执行成功并退出。
画面13：执行 Docker ps 命令，查看正在运行的容器，显示 Superset 容器已启动并监听 7000 端口。
画面14：执行 superset manager create-admin --app superset 命令，再次尝试创建管理员账户，提示“Username is already in use”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
Docker search supersert
INDEX NAME DESCRIPTION STARS OFFICIAL AUTOMATED
Docker.io Docker.io/amancevice/superset An extendable Docker image for Airbnb's Superset... 10
Docker.io Docker.io/pitr/flower/superset Superset a Flask-based Docker image 1
Docker.io Docker.io/maedamkz/superset Dockerized Superset 2
Docker.io Docker.io/ganashan/superset Kubernetes 2
Docker.io Docker.io/tygge/superset Kylo Superset Insight for Superset 2
Docker.io Docker.io/airbnb/superset AirBnb Superset 3.22 with MySQL driver... 1
Docker.io Docker.io/neo/superset Superset Docker Image 1
Docker.io Docker.io/ghoshal/superset Apache Superset (incubating) is a modern... 1
Docker.io Docker.io/montana/superset Superset MySQL 1
Docker.io Docker.io/garv/superset superset 1
Docker.io Docker.io/insane/superset superset 1
Docker.io Docker.io/monk/superset superset 1
Docker.io Docker.io/paris/superset Peer to Park Superset 1
Docker.io Docker.io/viktor/superset-worker-pyhton2.7 Superset on K8s 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io/airbnb/superset Superset 1
Docker.io Docker.io

