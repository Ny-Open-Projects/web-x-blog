# 10.目录挂载查看IP与删除容器

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\10.目录挂载查看IP与删除容器_【海量资源尽在 ubkz.com】.mp4
- 时长 8分43秒（音频 523s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好刚才呢我们已经讲解了一个叫CP的命令啊这个CP的命令呢是可以将我们速度机的某一个文件货目录啊拷贝到容器内部也就是在容器内部形成的一个副本啊也可以从容器内部将某一个文件货目录拷贝到速度机上那么这样一来呢我们就可以实现这种文件的这种交换那么当然这种方式呢其实有的时候并不是特别方便
[00:31] 因为我们还得需要去执行一个拷贝命令才能做到这两个目录的内容进行同步对不对那么假如我们希望是对某一个容器内部更方便的进行管理那这时候呢我们就可以通过目录挂载的方式来进行了那么目录挂载这个方式也就是说在创建容器的时候加一个杠威参数杠威参数后面呢就指定宿主机的目录码号容器目录这样一来呢宿主机的目录和容器的目录
[01:00] 就可以形成一个映射关系那么做完这个操作之后我们可以达到什么样的效果呢就是可以通过去修改宿主机的目录就可以影响到容器目录的内容当然你通过去修改容器内部的目录内容也可以去修改宿主机的目录内容因为它们两个目录本来就是处于同一个位置处于同一个位置好了我们现在就给大家演示一下这个目录的挂载
[01:31] 目录夸载,我们这里首先给大家看一下当前我们有两个容器接下来我们再创建一个-di-name等于mycentos3然后-v接下来就是usr local下的myhtml
[02:06] 然后紧接着呢就是我们的容器那个镜像加上标签s3好我们现在回车回来之后呢这个容器我们看一下就创建成功了创建成功之后那接下来我们就可以试验一下到底能不能去影响到这个容器内部的目录呢我们现在就可以进到这个usr local下的myhtml目录
[02:36] 大家看一下当前的目录是空的是吧当前目录是空的那么好我们现在呢来创建这么一个文件啊创建一个文件vi test啊我们随便创建一个文件啊那这时候呢比如说我们输入AAAOK吧随便写然后呢我保存当前呢就有这么一个test的这么一个文件了好了有人文件之后我们来验证一下吧Docker什么呢escc-it
[03:06] 然后接来就是你的容器名称mythin2s3接来-bin-bash好进到容器内部之后我们现在进到我们的目录下mythin2s3这时候你会发现这个里头也有一个tags这么一个文件我们现在可以查看一下这个文件内容是不是和我们刚才所说的内容是一样的对吧好我们退出来这就是说我们的一个目录挂载
[03:37] 就会很方便了就很方便了通常来说我们会将你安装的容器里的某一个文件某一个特别是配置文件进行一个挂载这样一来的我们修改文件起来就比较方便一些那么接下来我们来看一下下面我们要讲的就是查看容器的IP地址那么学会查看容器IP是个比较常用的操作首先我们来学习一个命令叫inspect
[04:07] 这个inspect呢它不仅可以查看容器IP它可以查看容器相关的所有数据我们来给大家演示一下这个命令Docker inspect然后接下来messentos3就是刚才我们创建的大家可以看一下这个里头会包括很多很多的信息对吧会包括很多很多信息包括什么它的ID呀还有创建的时间呢等等这些
[04:37] 很多信息那么其中它的IP地址在哪呢在这儿有一个networksettings下有一个什么呢有一个IPaddress这个部分就是它的IP地址就是它的IP地址那么那说了那假如说我就只想显示IP怎么办呢这时候我们可以通过加上一个格式化format这么一个参数来提取
[05:06] 你只是提取你所需要的这个信息怎么办呢这时候还是这条命令但是这时候要注意讲参数什么呢format等于引号一对大括号注意大括号是两层的是嵌套的那紧接着我加一个点点之后呢是什么呢就是network settings再点然后呢就是IP address
[05:36] 这样一来呢我们就可以通过这种方式来逐层的去筛选我们所需要的信息了那也说这里的内容呢就是要指定你要得到这个信息的这个路径是什么好我们现在回车这时候大家发现现在我显示的是不是就是这个只把IP就显示出来了那么同理其他的信息呢也可以通过这个指定这个format的这个参数来去提取你所需要的信息当然说提取IP地址是一个最方
[06:05] 最常用的一个操作那么接下来我们再看再看下面我们要学习的其实就是一个删除容器的这么一个操作删除容器我们用的什么用的是RM这个命令咱们现在给大家演示一下比如说我现在要删除买CentOS3这个容器那就写RM买CentOS3
[06:33] 这个时候大家会发现啊他这个时候他会有这么一个提示啊那么这个提示是啥意思呢就是说你这个容器呢现在正在运行它是无法移除一个正在运行的一个容器的所以说呢你这里头要你要选想去移除这个容器你首先你要怎么办对先把它停掉啊dockerstop my central s 3
[07:03] 先把它停掉之后我们再去才能移除掉这个容器好那么把它停止之后我们现在来看一下ps-a这时候我会发现这个容器已经停止了对吧停止之后我们再次的来进行移除这时候我们来看这时候就能把这个容器就移除了那么我们说到这的时候再额外说一句
[07:35] 咱们在上一个环节不是讲过一个镜像相关操作命令而镜像的操作命令是什么有一个删除叫RMI这个是删除镜像而RM是什么呢是移除容器一个是对容器操作一个是对镜像操作那么我们在这里额外说一句就是如果说这个当前的镜像有运行中的容器比如说这个CentOS有运行中容器你是无法删除的
[08:04] 你比如说我现在要删除s7这个镜像的话我们来看一下现在呢也是要提示有一个提示是什么呢就是当前你这个镜像是有运行中的容器的那这种情况也是不允许删除的那么什么样情况下能删呢就是需要把当前的你的所有的容器停止或删除然后呢你这个镜像才能进行移除这就是关于我们说的关于
[08:34] 这个目录挂载查看容器IP以及删除容器我们就给大家讲解到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Docker 命令查看和管理容器，特别是通过 Docker inspect 命令获取容器的网络配置和 IP 地址，并演示了如何停止和删除容器。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示终端界面，提示符为 [root@localhost myhtml]，但未显示任何命令或输出。
画面 2: 显示一个名为 "test" 的新文件，但未显示任何命令或输出。
画面 3: 显示 PPT 页面，标题为“3.2.6 查看容器IP地址”，并列出命令：Docker inspect 容器名称（容器ID） 和 Docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称（容器ID）。
画面 4: 显示 Docker inspect 命令的输出，包含容器的配置信息，如 Cpusetcpus、Memory、NetworkSettings 等。
画面 5: 显示 Docker inspect 命令的输出，包含容器的详细信息，如 Status、Image、Name、NetworkMode 等。
画面 6: 显示 Docker inspect 命令的输出，包含容器的详细信息，如 Status、Image、Name、NetworkMode 等。
画面 7: 显示 Docker inspect 命令的输出，包含容器的详细信息，如 Config、NetworkSettings 等。
画面 8: 显示 Docker inspect 命令的输出，包含容器的详细信息，如 NetworkSettings、IP Address 等。
画面 9: 显示 Docker inspect 命令的输出，包含容器的详细信息，如 NetworkSettings、IP Address 等。
画面 10: 显示 Docker ps 命令的输出，列出正在运行的容器，包括 CONTAINER ID、COMMAND、CREATED、STATUS、PORTS、NAMES。
画面 11: 显示尝试删除容器 mycentos 时，因容器正在运行而失败，提示信息为 "Error response from daemon: You cannot remove a running container ... Stop the container before attempting to remove it"。
画面 12: 显示使用 Docker stop 命令停止容器 mycentos，然后再次尝试删除，但提示 "Error response from daemon: You cannot remove a running container ... Stop the container before attempting to remove it"。
画面 13: 显示使用 Docker rm -f 命令强制删除容器 mycentos，然后尝试删除镜像 centos，提示 "Error response from daemon: conflict: unable to remove repository reference 'centos': (must force) - container b5eccd1114b is using its referenced image 51be286772b1"。
画面 14: 显示 PPT 页面，标题为“3.2.5 目录挂载”，并列出命令：Docker run -v /宿主机目录:/容器内目录 容器名:镜像名，以及 Docker run -d -v /宿主机目录:/容器内目录 --name=容器名 镜像名。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 3:
Docker inspect 容器名称（容器ID）
Docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称（容器ID）

画面 4:
{
  "Cpusetcpus": "",
  "Cpusetmems": "",
  "Devices": [],
  "DiskUsage": "",
  "Memory": 0,
  "MemoryReservation": 0,
  "MemorySwap": 0,
  "MemorySwappiness": null,
  "NanoCpus": 0,
  "OomKillDisable": false,
  "PidsLimit": 0,
  "Ulimits": [],
  "CpuPeriod": 0,
  "CpuQuota": 0,
  "CpuSet": "",
  "CpuShares": 0,
  "CpuSetMems": "",
  "CpuSetMemsMask": "",
  "CpuSetMemsList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMems

