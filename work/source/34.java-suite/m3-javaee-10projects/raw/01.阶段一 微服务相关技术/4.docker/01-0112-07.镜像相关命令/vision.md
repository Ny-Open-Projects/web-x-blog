# 画面线理解：07.镜像相关命令

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\07.镜像相关命令_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:34, 02:34, 02:46, 03:08, 04:05, 04:25, 04:48, 05:25, 05:59, 07:32, 08:16, 08:37, 08:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:03:02

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 命令搜索、拉取和管理镜像。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Docker 镜像信息的文档内容，包括 REPOSITORY、TAG、IMAGE ID、CREATED、SIZE 等字段说明，以及 3.1.2 搜索镜像和 3.1.3 拉取镜像的小节标题。
画面2：展示 Docker 命令列表，包括 attach、build、create、docker images 等命令，下方提示“Run 'docker COMMAND --help' for more information on a command.”。
画面3：展示文档内容，光标位于“docker search 镜像名称”命令行示例处。
画面4：在终端中执行 docker images 命令，列出本地镜像，包括 centos、redis、nginx 等，以及 registry。
画面5：在终端中执行 docker search centos 命令，列出搜索结果，包括 NAME、DESCRIPTION、STARS、OFFICIAL、AUTOMATED 等字段。
画面6：展示文档内容，光标位于“docker pull centos:7”命令行示例处。
画面7：在终端中执行 docker search centos 命令，列出搜索结果。
画面8：展示文档内容，包括 3.1.2 搜索镜像、3.1.3 拉取镜像、3.1.4 删除镜像等小节标题。
画面9：在终端中执行 docker pull centos 命令，显示拉取过程和完成信息。
画面10：在终端中执行 docker version 命令，显示 Docker 版本信息，包括 IMAGE ID、CREATED、SIZE 等。
画面11：在终端中执行 docker search centos 命令，列出搜索结果。
画面12：在终端中执行 docker pull zookeeper 命令，显示拉取过程和完成信息，最后显示拉取后的镜像列表。
画面13：展示文档内容，包括 3.1.4 删除镜像和 3.2 容器相关命令的小节标题。
画面14：展示文档内容，光标位于“docker pull centos:7”命令行示例处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
REPOSITORY, 镜像名称
TAG, 镜像标签
IMAGE ID, 镜像ID
CREATED, 镜像的创建日期（不获取镜像的日期）
SIZE, 镜像大小
这些镜像都是存储在Docker宿主机的/var/lib/docker目录下
3.1.2 搜索镜像
如果你需要从网络中查找需要的镜像，可以通过以下命令搜索
docker search 镜像名称
NAME, 仓库名称
DESCRIPTION, 镜像描述
STARS, 用户评价，反应一个镜像的受欢迎程度
OFFICIAL, 是否官方
AUTOMATED, 自动构建，表示该镜像由Docker Hub自动构建流程创建的
3.1.3 拉取镜像
拉取镜像就是从中央仓库中下载镜像到本地
例如，我要下载centos:7镜像
docker pull centos:7
3.1.4 删除镜像
按镜像ID删除镜像
docker rmi 镜像ID
删除所有镜像
docker rmi docker images -q
```

画面2：
```
Commands:
attach Attach local standard input, output, and error streams to a running container
build Build an image from a Dockerfile
commit Create a new image from a container's changes
copy Copy files/folders between a container's filesystem
create Create a new container
diff Display the difference between two filesystems
events Receive real time events from the server
exec Execute a command in a running container
export Export a container's filesystem as a tar archive
history Show the history of an image
import Import the contents of a tarball to create a filesystem image
images List images
inspect Return low-level information on docker objects
kill Kill one or more running containers
login Log in to a Docker registry
logout Log out from a Docker registry
logs Return the logs of a container
pause Pause all processes within one or more containers
port List port mappings or a specific mapping for the container
ps List containers
pull Pull an image or a repository from a registry
push Push an image or a repository to a registry
rename Rename a container
restart Restart one or more containers
rm Remove one or more containers
run Run a command in a new container
save Save one or more images to a tar archive (streamed to STDOUT by default)
search Search the Docker Hub for images
start Start one or more stopped containers
stats Display a live stream of containers' resource usage statistics
stop Stop one or more running containers
top Show the running processes of a container
unpause Unpause all processes within one or more containers
update Update configuration of one or more containers
version Show the Docker version information
wait Block until one or more containers stop, then print their exit codes
Run 'docker COMMAND --help' for more information on a command.
```

画面4：
```
REPOSITORY TAG IMAGE ID CREATED SIZE
centos 7 2e4d0f4aaf6f 9 days ago 44MB
centos 7 51b6902770f8 3 weeks ago 20MB
centos 7 4e40b13f1f60 3 weeks ago 83MB
centos 7 2a2c22320f60 4 weeks ago 22MB
centos 7 2b201b07680 4 weeks ago 33MB
registry latest 2b201b07680 4 weeks ago 33MB
```

画面5：
```
NAME DESCRIPTION STARS OFFICIAL AUTOMATED
centos The official build of CentOS. 4635 [OK] [x]
centos-ansible Ansible on CentOS. 115 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7.5.1804.x86_64. 99 [x] [x]
centos-7-ansible CentOS-7.5.1804.x86_64 / CentOS-7
