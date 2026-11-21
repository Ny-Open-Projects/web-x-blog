# 06.docker启动与停止

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\06.docker启动与停止_【海量资源尽在 ubkz.com】.mp4
- 时长 5分8秒（音频 309s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 在安装Docker之后我们需要做一件事情就是要设置一个国内的镜像站点因为如果说你不设置这一步呢你Docker最常用的一个下载操作也就是拉取一些镜像去下载一些镜像这个速度是非常慢因为它直接连国外站点那么怎么样才能加快我们的速度加快我们的下载速度就是要设置我们的这个镜像
[00:32] 设置镜像其实就是什么就是要修改一个文件这个文件就是在etc下的一个Docker下的什么叫diamond.json这么一个文件咱们可以打开看一眼用vi命令打开叫etc目录下的Docker下的什么就是diamond.json打开这个文件
[01:07] 这个文件呢如果是你刚安装成功的Docker这个时候呢是这个内容是空的啊那这时候呢如果说是空的你就需要去加上这么一点内容啊这个内容其实我已经事先加好了这个内容就是用于指定注册中心的这么一个镜像地址这个镜像地址其实就是我们说的ustc啊这么一个国内镜像国内镜像那么当然我们把这个加上之后呢我们这里可以去保存退出就可以了啊
[01:37] 这是因为这部分我已经帮他做了所以大家呢就不需要去自己完成了所以说呢这里呢就是如果说你是重新搭一个DAO壳的环境的话这一步呢是需要按照这个步骤来完成的好那接下来呢我们说镜像设置好了那接下来我们就说这个DAO壳怎么去启动呢我们说要启动这个服务之后我们才能使用DAO壳因为DAO壳的本身呢是一个什么呢是服务器客户端的那种
[02:06] 加固模式那么接下来我们来启动这个Docker怎么启动呢就用我们系统提供的一个命令叫Systemctl命令这个命令后边是加什么就是start就代表启动启动谁启动Docker服务好实际上之后这时候Docker就已经启动成功了那么你怎么样才能知道这个Docker的启动状态我们仍然是通过Systemctl命令
[02:39] 有一个status然后接下来就是服务名这时候我们就可以看到这个这个Docker它在处于什么这个状态处于是启动状态还是停止状态好了接下来我们再去再去停止Docker服务停止的话用stopdocker好停止之后我们再次查看这个状态大家看一下这个状态是不一样的是吧
[03:13] 上面这个状态是一个激活状态而下面是什么是一个停止的状态这是我们说的这个Docker它的一个启动与停止当然还有就是说我们有的时候需要比如说改了一些配置文件是吧这是我需要去重启重启第一种方式就是先stop然后start当然还有一种更便捷的方式就是restart就是什么就是重启
[03:45] 这是我们说的重启Docker另外呢假如说我们想让这个Docker在开机之后自动就启动了那这时候我们需要去使用什么呢这个Systemctl然后呢Enable然后呢Docker这时候呢我们说它就实现了一个开机自动启动的这么一个功能开机自动启动的功能那当然我们说这个
[04:21] 要查看DAO客一些概要信息这时候我们可以通这个DAO客本身的命令DAO客info当我们启动之后DAO客的命令是可以用的后面还会学习一系列的命令就是DAO客他提供了一系列命令当然title都是DAO客再有我们会说一下DAO客本身有一个在线帮助文档在线的当帮助文档用DAO客杠杠hub这时候它就是
[04:53] 给你列举了这个Docker所提供的一些所有的命令所有的命令这是关于Docker的这么一个启动与停止咱们就说到这儿

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Docker 镜像加速器、启动与停止 Docker 服务，并查看 Docker 常用命令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示文档《Docker 安装与配置》的第2.2节，内容为“设置ustc的镜像”，并展示需编辑的配置文件内容：{"registry-mirrors": ["https://Docker.mirrors.ustc.edu.cn"]}。
画面2：在终端中输入命令：registry-mirrors: ["https://Docker.mirrors.ustc.edu.cn"]。
画面3：终端中显示空行，准备执行命令。
画面4：执行 systemctl start Docker 命令后，显示 Docker 服务启动成功，状态为 active (running)。
画面5：显示文档《Docker 安装与配置》的第2.3节，内容为“Docker的启动与停止”，并列出 systemctl start Docker、systemctl stop Docker、systemctl restart Docker 等命令。
画面6：执行 systemctl stop Docker 命令后，显示 Docker 服务已停止，状态为 inactive (dead)。
画面7：执行 systemctl restart Docker 命令后，显示 Docker 服务已重启，状态为 active (running)。
画面8：终端中显示 Docker 服务状态，内容为“Docker Application Container Engine”。
画面9：执行 Docker info 命令后，显示 Docker 服务的详细信息，包括版本、存储驱动、镜像仓库等。
画面10：显示桌面，有“传智播客”和“黑马程序员”的联合出品标志。
画面11：桌面显示“传智播客”和“黑马程序员”的联合出品标志。
画面12：显示 Docker 命令帮助文档，列出常用命令如 attach、build、commit、create 等。
画面13：显示 Docker 命令帮助文档，列出常用命令如 diff、exec、export、history 等。
画面14：显示 Docker 命令帮助文档，列出常用命令如 images、inspect、kill、logs、pause、port、ps、pull、push、rename、restart、rm、run、save、search、start、stop、top、unpause、version 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
{"registry-mirrors": ["https://Docker.mirrors.ustc.edu.cn"]}
画面2：
registry-mirrors: ["https://Docker.mirrors.ustc.edu.cn"]
画面4：
systemctl start Docker
画面5：
systemctl start Docker
systemctl stop Docker
systemctl restart Docker
画面6：
systemctl stop Docker
画面7：
systemctl restart Docker
画面9：
Server Version: 18.06.1-ce
Storage Driver: overlay2
Backing Filesystem: xfs
Supports d_type: true
Native Overlay Diff: true
Logging Driver: json-file
Cgroup Driver: cgroups
Plugins:
 - Volume: local
 - Network: bridge host macvlan null overlay
 - Log: awslogs fluentd gcplogs gelf journald json-file splunk syslog
Swarm: inactive
Default Isolation: default
Kernel Version: 4.15.0-46-generic
Operating System: CentOS Linux 7 (Core)
Architecture: x86_64
Number of Docker containers: 0
Name: localhost
ID: 21MS-01N7-8302-97B7-21UM-4B20-8B20-5B2M-HPDU-6ZM-4VEN-D35J-2LVM
Debug Mode (Client): false
Debug Mode (Server): false
Registry: https://index.Docker.io/v1/
Labels:
Registry Mirrors:
https://Docker.mirrors.ustc.edu.cn
画面12：
Commands:
attach
Attach local standard input, output, and error streams to a running container
build
Build an image from a Dockerfile
commit
Create a new image from a container's changes
create
Create a new container
diff
Inspect changes to files or directories on a container's filesystem
events
Get real time events from the server
exec
Run a command in a running container
export
Export a container's filesystem as a tar archive
history
Show the history of an image
images
List images
inspect
Return low-level information on Docker objects
kill
Kill one or more running containers
login
Log in to a Docker registry
logout
Log out from a Docker registry
logs
Log the logs of a container
pause
Pause all processes within one or more containers
port
List port mappings or a specific mapping for the container
ps
List containers
pull
Pull an image or a repository from a registry
push
Push an image or a repository to a registry
rename
Rename a container
restart
Restart one or more containers
rm
Remove one or more containers
run
Run a command in a new container
save
Save one or more images to a tar archive (streamed to STDOUT by default)
search
Search the Docker Hub for images
start
Start one or more stopped containers
stop
Stop one or more running containers
top
Display the running processes of a container
unpause
Unpause all processes within one or more containers
version
Show the Docker version information
画面13：
Commands:
attach
Attach local standard input, output, and error streams to a running container
build
Build an image from a Dockerfile
commit
Create a new image from a container's changes
create
Create a new container
diff
Inspect changes to files or directories on a container's filesystem
events
Get real time events from the server
exec
Run a command in a running container
export
Export a container's filesystem as a tar archive
history
Show the history of an image
images
List images
inspect
Return low-level information on Docker objects
kill
Kill one or more running containers
login
Log in to a Docker registry
logout
Log out from a Docker registry
logs
Log the logs of a container
pause
Pause all processes within one or more containers
port
List port mappings or a specific mapping for the container
ps
List containers
pull
Pull an image or a repository from a registry
push
Push an image or a repository to a registry
rename
Rename a container
restart
Restart one or more containers
rm
Remove one or more containers
run
Run a command in a new container
save
Save one or more images to a tar archive (streamed to STDOUT by default)
search
Search the Docker Hub for images
start
Start one or more stopped containers
stop
Stop one or more running containers
top
Display the running processes of a container
unpause
Unpause all processes within one or more containers
version
Show the Docker version information
画面14：
Commands:
attach
Attach local standard input, output, and error streams to a running container
build
Build an image from a Dockerfile
commit
Create a new image from a container's changes
create
Create a new container
diff
Inspect changes to files or directories on a container's filesystem
events
Get real time events from the server
exec
Run a command in a running container
export
Export a container's filesystem as a tar archive
history
Show the history of an image
images
List images
inspect
Return low-level information on Docker objects
kill
Kill one or more running containers
login
Log in to a Docker registry
logout
Log out from a Docker registry
logs
Log the logs of a container
pause
Pause all processes within one or more containers
port
List port mappings or a specific mapping for the container
ps
List containers
pull
Pull an image or a repository from a registry
push
Push an image or a repository to a registry
rename
Rename a container
restart
Restart one or more containers
rm
Remove one or more containers
run
Run a command in a new container
save
Save one or more images to a tar archive (streamed to STDOUT by default)
search
Search the Docker Hub for images
start
Start one or more stopped containers
stop
Stop one or more running containers
top
Display the running processes of a container
unpause
Unpause all processes within one or more containers
version
Show the Docker version information

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PPT标题为“2.3 Docker的启动与停止”，内容包括“systemctl start Docker”、“systemctl stop Docker”、“systemctl restart Docker”。
画面14：PPT标题为“3 常用命令”，内容包括“Docker help”、“Docker info”、“Docker ps”、“Docker logs”、“Docker stop”、“Docker start”、“Docker restart”、“Docker rm”、“Docker rmi”、“Docker images”、“Docker build”、“Docker run”、“Docker exec”、“Docker attach”、“Docker commit”、“Docker diff”、“Docker export”、“Docker import”、“Docker tag”、“Docker push”、“Docker pull”、“Docker search”、“Docker search”、“Docker search”、“Docker search”、“Docker search”、“Docker search”、“Docker search”、“

