# 画面线理解：20.总结

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\20.总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:17, 01:28, 02:04, 02:22, 02:56, 03:31, 04:05, 04:58, 05:23, 05:33, 06:04, 06:33, 07:31, 08:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:11:18

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了 Docker 的基础概念、安装配置、容器操作、应用部署（MySQL、Tomcat、Nginx、Redis）以及镜像的保存、迁移与私有仓库的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍 Docker 是一个开源项目，由 dotCloud 公司发起，后更名为 Docker Inc.，项目代码在 GitHub 上维护，目标是实现轻量级的操作系统级虚拟化方案，基于 Linux 容器（LXC）技术。
画面2：讲解如何设置 ustu 的镜像加速，需编辑文件 `/etc/docker/daemon.json`，内容为：
{
  "registry-mirrors": ["https://docker.mirror.ustc.edu.cn"]
}
画面3：讲解 Docker 的启动与停止命令，包括：
启动：systemctl start docker
停止：systemctl stop docker
重启：systemctl restart docker
查看状态：systemctl status docker
开机启动：systemctl enable docker
查看信息：docker info
画面4：讲解如何拉取镜像（docker pull 镜像名称），并举例：docker pull centos:7；讲解如何删除镜像（docker rmi 镜像ID）及删除所有镜像（docker rmi docker_images -q）。
画面5：讲解如何查看容器状态，包括查看正在运行的容器（docker ps -a）和查看已停止的容器（docker ps -f status=exited）；介绍创建容器常用参数，如 -it 表示交互式运行，-name 表示容器名称。
画面6：讲解如何停止与启动容器，命令为 docker stop 容器名称/ID 和 docker start 容器名称/ID；讲解文件拷贝命令 docker cp。
画面7：继续讲解创建容器的参数，如 -d 表示后台运行，-p 表示端口映射；并演示交互式创建容器（docker run -it --name 容器名称 /bin/bash）和守护式创建容器（docker run -d --name 容器名称 /bin/bash）。
画面8：讲解目录挂载（docker run -v 主机目录:容器目录），并提到 CentOS7 的安全模块 selinux 会阻止挂载，需加参数 --privileged=true；讲解查看容器 IP 地址（docker inspect 容器ID）和直接输出 IP 地址（docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称）。
画面9：讲解应用部署，首先拉取 MySQL 镜像（docker pull centos/mysql-5.7-centos7），然后创建容器（docker run -d --name=tensquare_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql），并解释参数含义。
画面10：重复画面9的内容，展示拉取 MySQL 镜像和创建容器的命令。
画面11：讲解部署 Tomcat、Nginx 和 Redis，包括拉取镜像（docker pull nginx、docker pull redis）和创建容器（docker run -d --name=mynginx -p 80:80 nginx、docker run -d --name=myredis -p 6379:6379 redis）。
画面12：讲解镜像保存与迁移，命令为 docker save -o mynginx.tar mynginx；讲解 Dockerfile 是用于定义镜像构建的脚本。
画面13：展示 Dockerfile 示例内容：
FROM centos:7
指定镜像创建者信息
MAINTAINER ITCAST
工作目录
WORKDIR /usr
RUN mkdir -p /usr/local/java
#ADD jar包到容器中
ADD jdk-8u171-linux-x64.tar.gz /usr/local/java/
配置 java 环境变量
ENV JAVA_HOME /usr/local/java/jdk1.8.0_171
ENV PATH $JAVA_HOME/bin:$PATH
执行命令并构建镜像
docker build -t "jdk1.8" .
画面14：讲解如何将镜像上传至私有仓库，包括标记镜像（docker tag 镜像ID 私有仓库地址:镜像名）、启动私有仓库（docker start registry）和上传镜像（docker push 私有仓库地址:镜像名）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
{
  "registry-mirrors": ["https://docker.mirror.ustc.edu.cn"]
}
画面3：
启动docker:
systemctl start docker
停止docker:
systemctl stop docker
重启docker:
systemctl restart docker
查看docker状态:
systemctl status docker
开机启动:
systemctl enable docker
查看docker概要信息
docker info
画面4：
docker pull 镜像名称
例如，我要下载centos7镜像
docker pull centos:7
docker rmi 镜像ID
docker rmi docker_images -q
画面5：
docker ps -a
docker ps -l
画面6：
docker stop 容器名称（或者容器ID）
docker start 容器名称（或者容器ID）
docker cp
画面7：
docker run -it --name 容器名称 /bin/bash
docker run -d --name 容器名称 /bin/bash
画面8：
docker run -v /usr/local/myhtml:/usr/local/tomcat/webapps/ROOT
docker inspect 容器ID
docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称
画面9：
docker pull centos/mysql-5.7-centos7
docker run -d --name=tensquare_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql
画面11：
docker pull nginx
docker run -d --name=mynginx -p 80:80 nginx
docker pull redis
docker run -d --name=myredis -p 6379:6379 redis
画面12：
docker save -o mynginx.tar mynginx
画面13：
FROM centos:7
指定镜像创建者信息
MAINTAINER ITCAST
工作目录
WORKDIR /usr
RUN mkdir -p /usr/local/java
#ADD jar包到容器中
ADD jdk-8u171-linux-x64.tar.gz /usr/local/java/
配置 java 环境变量
ENV JAVA_HOME /usr/local/java/jdk1.8.0_171
ENV PATH $JAVA_HOME/bin:$PATH
执行命令并构建镜像
docker build -t "jdk1.8" .
画面14：
{"insecure-registries": ["192.168.104.141:5000"]}
docker tag 192.168.104.141:5000/jdk1.8
docker start registry
docker push 192.168.104.141:5000/jdk1.8

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
