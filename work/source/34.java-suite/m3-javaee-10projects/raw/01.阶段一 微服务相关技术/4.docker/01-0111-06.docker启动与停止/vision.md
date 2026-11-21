# 画面线理解：06.docker启动与停止

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\06.docker启动与停止_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:46, 01:39, 02:09, 03:05, 03:23, 03:43, 04:06, 04:23, 04:28, 04:38, 04:43, 04:52, 04:56, 05:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:02:08

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Docker 镜像加速器、启动与停止 Docker 服务，并查看 Docker 常用命令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示文档《Docker 安装与配置》的第2.2节，内容为“设置ustc的镜像”，并展示需编辑的配置文件内容：{"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]}。
画面2：在终端中输入命令：registry-mirrors: ["https://docker.mirrors.ustc.edu.cn"]。
画面3：终端中显示空行，准备执行命令。
画面4：执行 systemctl start docker 命令后，显示 Docker 服务启动成功，状态为 active (running)。
画面5：显示文档《Docker 安装与配置》的第2.3节，内容为“Docker的启动与停止”，并列出 systemctl start docker、systemctl stop docker、systemctl restart docker 等命令。
画面6：执行 systemctl stop docker 命令后，显示 Docker 服务已停止，状态为 inactive (dead)。
画面7：执行 systemctl restart docker 命令后，显示 Docker 服务已重启，状态为 active (running)。
画面8：终端中显示 Docker 服务状态，内容为“Docker Application Container Engine”。
画面9：执行 docker info 命令后，显示 Docker 服务的详细信息，包括版本、存储驱动、镜像仓库等。
画面10：显示桌面，有“传智播客”和“黑马程序员”的联合出品标志。
画面11：桌面显示“传智播客”和“黑马程序员”的联合出品标志。
画面12：显示 Docker 命令帮助文档，列出常用命令如 attach、build、commit、create 等。
画面13：显示 Docker 命令帮助文档，列出常用命令如 diff、exec、export、history 等。
画面14：显示 Docker 命令帮助文档，列出常用命令如 images、inspect、kill、logs、pause、port、ps、pull、push、rename、restart、rm、run、save、search、start、stop、top、unpause、version 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
{"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]}
画面2：
registry-mirrors: ["https://docker.mirrors.ustc.edu.cn"]
画面4：
systemctl start docker
画面5：
systemctl start docker
systemctl stop docker
systemctl restart docker
画面6：
systemctl stop docker
画面7：
systemctl restart docker
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
Registry: https://index.docker.io/v1/
Labels:
Registry Mirrors:
https://docker.mirrors.ustc.edu.cn
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
画面5：PPT标题为“2.3 Docker的启动与停止”，内容包括“systemctl start docker”、“systemctl stop docker”、“systemctl restart docker”。
画面14：PPT标题为“3 常用命令”，内容包括“docker help”、“docker info”、“docker ps”、“docker logs”、“docker stop”、“docker start”、“docker restart”、“docker rm”、“docker rmi”、“docker images”、“docker build”、“docker run”、“docker exec”、“docker attach”、“docker commit”、“docker diff”、“docker export”、“docker import”、“docker tag”、“docker push”、“docker pull”、“docker search”、“docker search”、“docker search”、“docker search”、“docker search”、“docker search”、“docker search”、“
