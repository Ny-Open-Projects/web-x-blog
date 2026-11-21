# 14.redis部署

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\14.redis部署_【海量资源尽在 ubkz.com】.mp4
- 时长 2分28秒（音频 148s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好,接下来呢我们来学习使用Docker来搭建一个Redis的环境搭建Redis环境的首先我们一样是要先要拉取我们的Redis的镜像那么它的命令就是Docker pull Redis这一步呢我们依然是可以省略的因为我给大家已经提前下载了这个Redis镜像那么我们接下来呢基于这个镜像我们要怎么办
[00:29] 创建一个容器-di-name等于myredis-p代表我要去做端口映射然后这个端口比如说65379它默认还是6379好然后接下来最后我们指定镜像名称redis好这个镜像我们创建成功之后那么接下来我们要怎么办我们就可以
[01:00] 测试一下看到底能不能远程的去连接到 redis我们这里做了端口映射那么我就可以通过连接连接宿主机连接宿主机就可以连接容器的 redis了我这里有一个redis的 windows的客户端咱们现在可以通过它来去做一个连接现在切换到地盘切换到当前的目录
[01:32] 那么这个里头有两个文件一个是redis-cli一个是redis-server那么cli就是我们的客户端程序我们现在可以通过它来去来去连接远程的redis怎么连接这是如果说你直接的去执行命令它连接的像是你本地的 redis那么如果说你想连接远程的这里就加一个-h然后这里空格写上你的远程连接的redis的
[02:02] IP好大家看一下现在是不是就联系成功了我们现在可以去敲命令也是一样的比如说set name abc这时候我就存了一个值这时候我们一样可以通过get name把这个值再取出来对吧一样的这样一来我们redis的环境就搭建完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 Nginx 和 Redis 容器，并展示容器管理与镜像操作命令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于 Docker 部署 Redis 和迁移备份的章节，包含创建容器的命令：Docker run -d --name=Nginx -p 80:80 Nginx。
画面2：同画面1，内容无变化。
画面3：在终端中执行 Docker rm nginx_1 删除容器，然后执行 Docker rmi JDK 8 删除镜像，接着执行 Docker images 查看镜像列表。
画面4：在终端中执行 Docker run -d --name=myredis -p 6379:6379 redis 启动 Redis 容器。
画面5：展示 Windows 文件资源管理器中包含多个软件安装包的目录。
画面6：在文件资源管理器中浏览到包含 redis2.8win32 文件夹的目录。
画面7：在文件资源管理器中选中 redis2.8win32 文件夹。
画面8：在文件资源管理器中打开 redis2.8win32 文件夹，显示其中包含 dump.rdb、redis-windows.conf、redis-cli.exe、redis-server.exe 等文件。
画面9：在文件资源管理器中选中 redis2.8win32 文件夹。
画面10：在文件资源管理器中选中 redis2.8win32 文件夹。
画面11：在命令提示符中进入 redis2.8win32 目录，准备运行 Redis 服务。
画面12：在命令提示符中执行 redis-cli -h 192.168.164.141 命令连接 Redis 服务。
画面13：在命令提示符中执行 redis-cli -h 192.168.164.141 命令连接 Redis 服务。
画面14：在终端中执行 Docker ps 查看正在运行的容器，显示 myredis 和 mynginx 容器的详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
Docker run -d --name=Nginx -p 80:80 Nginx
Docker pull redis
Docker run -d --name=myredis -p 6379:6379 redis
Docker commit Nginx nginx_1
Docker run -d --name=myredis -p 6379:6379 redis

画面3：
Docker rm nginx_1
Docker rmi JDK 8
Docker images
Docker run -d --name=myredis -p 6379:6379 redis

画面4：
Docker run -d --name=myredis -p 6379:6379 redis

画面12：
redis-cli -h 192.168.164.141
192.168.164.141:6379> set name abc
OK
192.168.164.141:6379> get name
"abc"
192.168.164.141:6379> exit

画面14：
Docker ps
COMMAND
CREATED
STATUS
PORTS
NAMES
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

