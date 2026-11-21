# 07.镜像相关命令

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\07.镜像相关命令_【海量资源尽在 ubkz.com】.mp4
- 时长 9分1秒（音频 541s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们现在呢来学习第三小节的内容常用命令那么常用的命令呢其实主要包括两大类第一大类呢就是镜像相关的操作第二个方面呢就是容器相关的一些操作好,我们首先来看一下第一个就是镜像相关镜像相关的命令呢咱们先看一下第一个命令就是要查看镜像那么所谓查看镜像呢就是查看你本地
[00:30] 已经存在哪些镜像咱们来看一下这时候我们用Docker命令Docker imagesimages这个命令大家看一下当我们输完这个命令之后大家会看到有这么一个列表对吧那么列表第一行就是指的是标题第一个repostery这个什么呢就是我们指的这个镜像的名称
[00:59] 这一列指的是镜像的名称那么镜像名称后边有一个tag是什么呢就是标签这个标签什么意思呢就是一般强行来说就是这个镜像的一个版本区分就是一个版本区分因为我们说镜像很有可能会出现重名那么重名的话有可能就是版本有区别所以通常我会把版本作为它的tag还有就是后边有一个什么image id
[01:26] 就是我们的镜像id这个镜像id就是一个唯一的一个id是一个唯一的id那么后面这个部分呢created就是什么呢created就是这个镜像它所产生它有创建的时间它创建的时间有多长时间还有就是后面就是size就是这个镜像所占用的大小所占用大小这是我们说的关于第一个命令
[01:56] 那么我们说当我们在刚刚装完的DAO壳之后其实你在输这个命令是你是看不到这些数据的你之所以能看到这些数据是因为我给大家所提供的这个这个这个synos镜像已经下载好了这些镜像了这些镜像是已经提前下载的那么这样的话同学们就可以在没有网络的环境下也可以就是学习学习和练习本章的一些内容
[02:26] 这是我们说的一个第一个命令就是查看镜像第二个我们要学习的这个命令呢就叫搜索镜像搜索镜像那么搜索镜像的话就是我们搜的实际上是互联网上的这个镜像搜索的是互联网镜像那么怎么来做呢用这个用这个Docker search这个命令查询
[02:54] 查询什么比如说我现在要搜索森头S名称含有森头S这样的镜像都哪些好我们现在就输入这样一个命令这时候呢大家看到这个列表中所列出来的实际上就是什么呢就是这个所有啊这个镜像名称中包含森头S的这么一个查询结果那我们现在呢就可以基于这个查询结果啊来进行什么呢来进行这个
[03:25] 这个相应的这个下载就可以对着这个名称来进行下载这是我们说的第二个命令就是搜索镜像那么搜索镜像的这里头包括了一些这个标题的这个四段信息我们来这里简单解释一下内容就是我们的镜像的名称后面那个部分呢就是指这个镜像的描述就指这个镜像它是具体的内容是什么
[03:56] 这里有个简单的描述,Homer Starters,Stars,Stars是什么呢?
[04:05] 就是我们的星,就是我们的什么,就是它的一个评价,用户的评价,那么评价数越多,好评度就越多,就是Stars,Homer这个字段表示什么呢?
[04:19] 表示的是,是否是什么呢?
[04:22] 官方提供的镜像,是否是官方提供的?
[04:26] 还有就是后边这个是有一个就是automatic的就是我们说的是否是由这个dog harbor自动构建流程所创建的一些景象这是我们说的一个搜索景象讲完搜索景象之后我们再讲拉曲景象那么拉曲景象如何拉曲呢这是我们用的命令叫破破就拉曲好我们现在就来拉曲一个
[04:59] 其中一个镜像啊啊比如说啊我们现在拉一个拉取一个哪个镜像呢Docker,Tor我们可以拉取这个镜像Total-CentOS好现在我们回车这时候呢当你没有指定这个标签的时候没有指定这个标签的时候那这时候呢它就采用的是默认式拉拉test这么一个默认的就是
[05:33] 它是一个最后版本的这么一个镜像那么如果说你要指定个具体的指定具体他个来进下载的话我们就加上冒号然后这个他个名称就可以了好大家看一下现在的这种情况的就是他正在去下载这个镜像就是下载这个镜像当我们下载成功之后我们就可以通过什么刚才的images命令来去查看到这个
[06:02] 已经下载完成的镜像这是关于这个拉取镜像那么接下来呢我们再说一下这个删除镜像那么这个删除镜像怎么来删除呢我们可以按照镜像的ID来进行删除也可以按照镜像名称来删除那么不管是镜像ID还是镜像名称我们这里头它的命令是什么呢叫RMIDocker RMI后面是镜像名称或者ID
[06:33] 但一般来说最好是指定id那么如果说你要删除所有的镜像这时候我们就可以使用什么可以使用这个命令就是rm后边注意后边不是普通的单引号这个引号是什么是你键盘上esc键也是左上角那个esc在esc键下边那个键所敲出来字数
[07:01] 并不是那个引号并不是那个单引号的那这个命令就是用来删除所有镜像删除所有镜像那这个删除所有镜像这里的部分这个引号里的部分实际上就是也是一个命令我们可以把这个命令的结果作为什么呢作为这个命令的参数来执行这是我们说的这个删除镜像主要有这么两种两种写法
[07:32] 好现在镜像已经快要下载完成了一会我们就可以用刚才下载的镜像来练习我们的镜像的删除好接下来我们来演示一下如何来删除镜像比如说我们现在先查看一下我们Docker中都有哪些镜像比如说我们要删除这个镜像怎么办这时候我们就可以
[08:03] 写Docker RMI这是我们的命令删除镜像命令这时候你可以使用这个名称也可以使用 id我们可以把id复制一下好这时候它就进行删除了删除后咱们现在看一下再通过这个命令大家看一下是不是就已经在列表中查询不到了就表示我们已经删除成功了那么下面这个命令我们就不给大家演示了因为如果说你要把所有镜像都删除掉的话
[08:36] 你后边所有的命令都就没法玩了你还得需要重新去下载这个的速度就会比较慢这是我们说的关于镜像相关的操作命令这里需要大家掌握的就是比较长的这4种一个是查看另外一个就是搜索第三个就是如何去拉取第4个是删除

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 命令搜索、拉取和管理镜像。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Docker 镜像信息的文档内容，包括 REPOSITORY、TAG、IMAGE ID、CREATED、SIZE 等字段说明，以及 3.1.2 搜索镜像和 3.1.3 拉取镜像的小节标题。
画面2：展示 Docker 命令列表，包括 attach、build、create、Docker images 等命令，下方提示“Run 'Docker COMMAND --help' for more information on a command.”。
画面3：展示文档内容，光标位于“Docker search 镜像名称”命令行示例处。
画面4：在终端中执行 Docker images 命令，列出本地镜像，包括 centos、redis、Nginx 等，以及 registry。
画面5：在终端中执行 Docker search centos 命令，列出搜索结果，包括 NAME、DESCRIPTION、STARS、OFFICIAL、AUTOMATED 等字段。
画面6：展示文档内容，光标位于“Docker pull centos:7”命令行示例处。
画面7：在终端中执行 Docker search centos 命令，列出搜索结果。
画面8：展示文档内容，包括 3.1.2 搜索镜像、3.1.3 拉取镜像、3.1.4 删除镜像等小节标题。
画面9：在终端中执行 Docker pull centos 命令，显示拉取过程和完成信息。
画面10：在终端中执行 Docker version 命令，显示 Docker 版本信息，包括 IMAGE ID、CREATED、SIZE 等。
画面11：在终端中执行 Docker search centos 命令，列出搜索结果。
画面12：在终端中执行 Docker pull ZooKeeper 命令，显示拉取过程和完成信息，最后显示拉取后的镜像列表。
画面13：展示文档内容，包括 3.1.4 删除镜像和 3.2 容器相关命令的小节标题。
画面14：展示文档内容，光标位于“Docker pull centos:7”命令行示例处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
REPOSITORY, 镜像名称
TAG, 镜像标签
IMAGE ID, 镜像ID
CREATED, 镜像的创建日期（不获取镜像的日期）
SIZE, 镜像大小
这些镜像都是存储在Docker宿主机的/var/lib/Docker目录下
3.1.2 搜索镜像
如果你需要从网络中查找需要的镜像，可以通过以下命令搜索
Docker search 镜像名称
NAME, 仓库名称
DESCRIPTION, 镜像描述
STARS, 用户评价，反应一个镜像的受欢迎程度
OFFICIAL, 是否官方
AUTOMATED, 自动构建，表示该镜像由Docker Hub自动构建流程创建的
3.1.3 拉取镜像
拉取镜像就是从中央仓库中下载镜像到本地
例如，我要下载centos:7镜像
Docker pull centos:7
3.1.4 删除镜像
按镜像ID删除镜像
Docker rmi 镜像ID
删除所有镜像
Docker rmi Docker images -q
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
inspect Return low-level information on Docker objects
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
Run 'Docker COMMAND --help' for more information on a command.
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

