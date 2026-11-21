# 20.总结

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\20.总结_【海量资源尽在 ubkz.com】.mp4
- 时长 8分39秒（音频 520s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好这个关于Docker课程呢我们就讲解到这里那么接下来呢我们对我们所讲解的内容呢做一个总结那么今天我们主要讲了这个Docker的一些基础知识包括这个Docker的镜像与容器这么一个概念那么这个镜像实际上什么呢镜像我们可以把它看成是一个模板而容器呢是根据这个模板所创建的一台服务器也就是说我们可以在本机
[00:31] 下载或者构建很多镜像比如说CentOS的,MyCircle的Tomcat,Nginx,Redis等等或者甚至是我们自己写的一个应用程序我们也可以创建一个镜像那么如果说我们要想让镜像能够跑起来这时候就是根据镜像来创建容器那么我们可以把每一个创建容器都可以看成是一个服务器都可以看成一个服务器它们之间容器容器之间
[01:00] 他们环境因为是隔离的所以说使用容器来搭建生产环境它的那种安全性也是比较高的那么接下来我们要讲了一个Docker的安装与启动这个安装与启动这里以后大家要掌握如何来安装Docker如何来安装Docker以及我们怎么去设置加速器也就是我们的一些国内的一些镜像那么安装国内镜像之后
[01:29] 通过设置国内镜像我们就可以加快我们的下载的速度那另外一个就是我们要这个讲解了Docker的启动与停止是如何启动的那么Docker本身是一个服务我们就可以通过System CTL这个命令它的Start启动Stop停止Restart重启然后呢Status来看一下它的运行状态还有呢就是我们可以直接设置为开机启动
[01:59] 这样一来呢我们在启动之后呢就不用去手动去进行启动了那么接下来我们要讲的这个命令呢是我们要重点掌握的也就是命令主要有两种一种呢就是我们说的镜像相关的那么这里我们主要学了查看镜像用image还有呢搜索镜像search拉取镜像破删除镜像rmi
[02:27] 这是我们镜像相关的而我们容器相关的有这么几个命令包括ps查看那么查看如果说是你直接写ps那么他查看的就是运行中的容器那么如果说你想查询所有的容器需要后边加参数-a如果说你需要查看最后一次运行容器需要加-l那么如果说想查看停止的那这时候你就加-f然后status等于ext
[02:57] 那好了我们接下来我们下面看就是启动创建和启动容器这个呢其实我们用的是比较多的创建和启动容器呢这里包括两种方式啊一种是以交互式方式来创建一种是以守护式方式创建那么如果是以交互式方式创建那这时候呢它所创建之后它会直接的进到容器内部但是这种方式如果说你通过exit这个命令来退出的话
[03:28] 那这时候呢这个容器就会自动停止但是如果说以守护式方式创建容器呢它的特点是我们创建完之后当前的这个提示符还是在你的速度机这一层并不会自动进入容器而你可以什么呢可以在创建之后通过exec这个命令啊来去再进入到这个容器内之内而这个通过这种方式进入之后再退出这个容器依然是启动状态
[03:56] 那这个时候呢这两种方式呢其实我们就可以根据实际情况啊选择一个最合适的一种方式那么这里还有一些参数啊参数呢有一个i有个t啊有一个v一般来说i呢是一般都会加上这个参数就是表示我创建之后要运行起来那么如果说是t啊如果是t的话就表示是我以交入式方式来进入然后呢如果说以d的话就是以守护式方式来
[04:27] 来构建还有就是我们说杠内杠杠内容表示的是我要创建创建一个名容器我要给起个名字还有杠V表示我的一个目录的映射杠P表示是端口映射这些参数都是非常常用的非常常用的另外一个文件拷贝这时候我们要用的是CP命令启动与停止start stop这个都是非常常用的
[04:55] 目录挂载我们刚才说过了用-v还有就是我们可以查看容器IP地址或者说查看容器的一些其他数据用inspect这个命令来进行就行了如果说我们这个容器想删除那这时候我们可以使用rm命令来删除容器好这是关于常用操作我们就说到这那么接下来我们再看一下应用部署应用部署这里我们讲了四种
[05:22] 应用的一个部署一个是mycircle一个mycircle一个Tomcat一个是index一个是redis那么这几种其实都是对我们之前之前的这个什么之前所学的这些命令它一个应用这里头mycircle至于注意要加一个环境变量如果环境变量的话需要加-e加-e环境变量主要是用于指定我们root用户的登录密码
[05:51] 拉取他们开的那这时候我们会用到这个杠V这个材数拉取这个N这个词呢我们用的是杠P的这个这个映射端口redis我们也一样用的是杠P这是我们说的这个这几种常用软件的一个部署另外一个我们还讲了这个迁移与备份迁移备份的话我们就也是讲了继续讲了几个命令一个是commit就是提交也就是说将容器保存为镜像
[06:20] 还有一个呢就是save将镜像保存为tar文件还有呢就是我们的恢复就是将tar文件通过load命令来进行什么来再恢复为一个镜像这是我们说的这三种命令那么接下来我们又讲了一个dogger file这个dogger file呢实际上是一个脚本是个脚本我们通过这个dogger file呢可以去构建一个脚本让这个构建脚本的过程呢能够自动化这是它的
[06:51] 一个整体的目标让自动化那么这里头我们学了他的一些常用的命令包括from, mantener,env, run这些命令都是我们用到的然后还有的add, copy还有work.jar这些都是每个命令都有相应的一个作用那么我们最后还是用命令来构建了一个JDK 1.8的这么一个镜像因为这个JDK 1.8的镜像我们后期会用它
[07:21] 以这个JDK 8的这个镜像作为基础镜像来创建什么呢创建我们所用的一些微服务这是我们说的这个关于这个Docker file然后另外一个最后我们就讲了一个Docker私有仓库那么Docker私有仓库的构建呢就是本身这个私有仓库也是一个镜像我们把这个镜像下载下来根据这个镜像呢创建一个容器那么这个容器呢其实就是我们说的这个私有仓库了这个部署呢是非常简单的
[07:52] 这里头我们需要注意一点,需要去修改Docker的dermal.json这么一个文件那么这个文件我们需要加上这么一个配置才行那么这个配置的作用主要是用于让Docker能够信任私有仓库的地址但是最后别忘了,修改完配置之后如果想生效就需要重启Docker服务另外一个如果说你想上传到私有镜像这时候别忘了先用targ命令来对它进行打标记
[08:20] 打上标记标记它是哪一个哪一个这个45仓库的属于哪一个45仓库的然后标记之后我们再进行push就可以了这是我们说的关于这个Docker的内容我们就讲解到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了 Docker 的基础概念、安装配置、容器操作、应用部署（MySQL、Tomcat、Nginx、Redis）以及镜像的保存、迁移与私有仓库的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍 Docker 是一个开源项目，由 dotCloud 公司发起，后更名为 Docker Inc.，项目代码在 GitHub 上维护，目标是实现轻量级的操作系统级虚拟化方案，基于 Linux 容器（LXC）技术。
画面2：讲解如何设置 ustu 的镜像加速，需编辑文件 `/etc/Docker/daemon.json`，内容为：
{
  "registry-mirrors": ["https://Docker.mirror.ustc.edu.cn"]
}
画面3：讲解 Docker 的启动与停止命令，包括：
启动：systemctl start Docker
停止：systemctl stop Docker
重启：systemctl restart Docker
查看状态：systemctl status Docker
开机启动：systemctl enable Docker
查看信息：Docker info
画面4：讲解如何拉取镜像（Docker pull 镜像名称），并举例：Docker pull centos:7；讲解如何删除镜像（Docker rmi 镜像ID）及删除所有镜像（Docker rmi docker_images -q）。
画面5：讲解如何查看容器状态，包括查看正在运行的容器（Docker ps -a）和查看已停止的容器（Docker ps -f status=exited）；介绍创建容器常用参数，如 -it 表示交互式运行，-name 表示容器名称。
画面6：讲解如何停止与启动容器，命令为 Docker stop 容器名称/ID 和 Docker start 容器名称/ID；讲解文件拷贝命令 Docker cp。
画面7：继续讲解创建容器的参数，如 -d 表示后台运行，-p 表示端口映射；并演示交互式创建容器（Docker run -it --name 容器名称 /bin/bash）和守护式创建容器（Docker run -d --name 容器名称 /bin/bash）。
画面8：讲解目录挂载（Docker run -v 主机目录:容器目录），并提到 CentOS7 的安全模块 selinux 会阻止挂载，需加参数 --privileged=true；讲解查看容器 IP 地址（Docker inspect 容器ID）和直接输出 IP 地址（Docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称）。
画面9：讲解应用部署，首先拉取 MySQL 镜像（Docker pull centos/mysql-5.7-centos7），然后创建容器（Docker run -d --name=tensquare_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql），并解释参数含义。
画面10：重复画面9的内容，展示拉取 MySQL 镜像和创建容器的命令。
画面11：讲解部署 Tomcat、Nginx 和 Redis，包括拉取镜像（Docker pull Nginx、Docker pull redis）和创建容器（Docker run -d --name=mynginx -p 80:80 Nginx、Docker run -d --name=myredis -p 6379:6379 redis）。
画面12：讲解镜像保存与迁移，命令为 Docker save -o mynginx.tar mynginx；讲解 Dockerfile 是用于定义镜像构建的脚本。
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
ENV JAVA_HOME /usr/local/java/JDK 8.0_171
ENV PATH $JAVA_HOME/bin:$PATH
执行命令并构建镜像
Docker build -t "JDK 8" .
画面14：讲解如何将镜像上传至私有仓库，包括标记镜像（Docker tag 镜像ID 私有仓库地址:镜像名）、启动私有仓库（Docker start registry）和上传镜像（Docker push 私有仓库地址:镜像名）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
{
  "registry-mirrors": ["https://Docker.mirror.ustc.edu.cn"]
}
画面3：
启动Docker:
systemctl start Docker
停止Docker:
systemctl stop Docker
重启Docker:
systemctl restart Docker
查看Docker状态:
systemctl status Docker
开机启动:
systemctl enable Docker
查看Docker概要信息
Docker info
画面4：
Docker pull 镜像名称
例如，我要下载centos7镜像
Docker pull centos:7
Docker rmi 镜像ID
Docker rmi docker_images -q
画面5：
Docker ps -a
Docker ps -l
画面6：
Docker stop 容器名称（或者容器ID）
Docker start 容器名称（或者容器ID）
Docker cp
画面7：
Docker run -it --name 容器名称 /bin/bash
Docker run -d --name 容器名称 /bin/bash
画面8：
Docker run -v /usr/local/myhtml:/usr/local/Tomcat/webapps/ROOT
Docker inspect 容器ID
Docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称
画面9：
Docker pull centos/mysql-5.7-centos7
Docker run -d --name=tensquare_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql
画面11：
Docker pull Nginx
Docker run -d --name=mynginx -p 80:80 Nginx
Docker pull redis
Docker run -d --name=myredis -p 6379:6379 redis
画面12：
Docker save -o mynginx.tar mynginx
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
ENV JAVA_HOME /usr/local/java/JDK 8.0_171
ENV PATH $JAVA_HOME/bin:$PATH
执行命令并构建镜像
Docker build -t "JDK 8" .
画面14：
{"insecure-registries": ["192.168.104.141:5000"]}
Docker tag 192.168.104.141:5000/JDK 8
Docker start registry
Docker push 192.168.104.141:5000/JDK 8

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

