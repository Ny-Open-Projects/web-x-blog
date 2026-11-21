# 12.Kubernetes集群搭建Node安装-准备工作

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\12.Kubernetes集群搭建Node安装-准备工作_【海量资源尽在 ubkz.com】.mp4
- 时长 2分55秒（音频 175s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面呢我们说一下node节点安装那么无论我们的node1节点还是后续我们的node2节点那么他们在安装之前呢都有一些准备工作那么第一件事呢他是需要把我们这个kubernetes的一些安装的文件或者一些服务啊给他安装到我们当前的这个节点上一个是kubernetes还有一个是kubeproxy那我们先把这个事情做一下啊我呢在当前的user下local
[00:29] 创建了一个Kubernetes目录那我们可以通过RG命令去把我们当前的这个Kubernetes软件给它装过来我先把它上传上来上传上来以后我们把它解压开然后找到我们的Kubernetes和Kubernetes proxycopy到user BIM目录下那第二件事就是我们必须在在node节点上去安装Docker那么大家可以参考我们之前master节点上的Docker的安装
[01:00] 我们看一下这边是否传完了马上就完事现在已经84%了88%我们这个上传完以后一会我去把这个coupleit和我们当前的这个coolproxy文件给它找到copy到userbin一下那我在这里边tar-jxvf我们的tar那这里边我们稍微等一下等它把它解压完解压完以后我们再去操作
[01:26] 那关于这个node节点啊这个前期准备就这么两件事大家一定要注意了还有就是你要注意我这个node节点跟我讲一上在最开始关于进行搭建的我们这个IP地址是有差异的你一定要注意了我们现在这个文件上写的是140和141这是我们的master和我的node而我真实操作中我的master是147我的node是148那回来我们还是看到这
[01:54] 我现在已经把它解压开了然后我们lcd进我们的Kubernetes这文件然后我们再来看cd我们的server然后cd我的bim目录下找到我们要的Kubernetes还有一个叫做Kubernetes我们cp一下我们把这个Kubernetes还有这个Kubernetes-proxy这两个文件copy到我们user下的bim目录下
[02:25] OK,这是第一件事我们关于这个node节点的要准备的第二件事就是关于我们的这个Docker安装我说了你参考我们的原来master里面的Docker安装我的YAML我的镜像都已经配置好了那我只需要去YAML install我们的Docker-enjne然后呢我干挖一下我去安装它把它安装完我们整个node节点的准备工作就完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在Kubernetes集群部署过程中，通过SecureCRT远程连接到Node1节点，解压并安装Kubernetes组件（如kubelet、kube-proxy等）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，讲解Docker安装步骤，包括配置yum源和安装Docker-engine命令。
画面2：SecureCRT终端界面，显示已连接到目标服务器，准备执行命令。
画面3：在SecureCRT中执行“pwd”命令查看当前目录，并弹出文件传输窗口，准备上传文件。
画面4：在SecureCRT中执行“rz”命令，开始从本地上传文件，显示传输进度。
画面5：文件传输继续进行，显示传输进度和剩余时间。
画面6：切换到PPT页面，显示“2.3 Node1安装”章节，提示在Node1节点上安装Docker并启动Docker服务。
画面7：在SecureCRT终端中，执行“tar -zxvf kubernetes-server-linux-amd64.tar.gz”命令，解压Kubernetes服务器组件。
画面8：继续解压操作，显示解压后的文件列表。
画面9：切换到PPT页面，显示“2.1 环境准备与规划”章节，列出各节点角色、IP地址和组件。
画面10：切换回PPT页面，显示“2.3 Node1安装”章节，提示配置systemd服务文件。
画面11：在SecureCRT终端中，执行“cd server”命令，进入解压后的server目录。
画面12：在SecureCRT终端中，执行“mkdir -p /usr/local/bin”命令，创建bin目录。
画面13：在SecureCRT终端中，执行“cp kubelet kube-proxy /usr/local/bin/”命令，复制Kubernetes组件到bin目录。
画面14：在SecureCRT终端中，执行“cp kubelet kube-proxy /usr/local/bin/”命令，继续复制Kubernetes组件到bin目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
[...]
[ dockerrepo ]
name=Docker repository
baseurl=https://mirrors.aliyun.com/Docker-ce/linux/centos/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/Docker-ce/linux/centos/7/Docker-ce.repo
[...]
画面1：
[...]
yum install Docker-engine
[...]
画面1：
[...]
Docker -v
[...]
画面7：
tar -zxvf kubernetes-server-linux-amd64.tar.gz
[...]
画面11：
cd server
[...]
画面12：
mkdir -p /usr/local/bin
[...]
画面13：
cp kubelet kube-proxy /usr/local/bin/
[...]
画面14：
cp kubelet kube-proxy /usr/local/bin/
[...]

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.2.1 Docker安装”，包含三个步骤：(1) 配置yum源，(2) 安装Docker，(3) 安装后查看Docker版本。
画面6：PPT标题为“2.3 Node1安装”，内容包括“在Node1节点上，以同样的方式把从压缩包中解压出的二进制文件kubelet kube-proxy放到/usr/bin目录中。”和“在Node1节点上需要先安装Docker，请参考Master上Docker的安装，并启动Docker”。
画面9：PPT标题为“2.1 环境准备与规划”，表格包含三列：角色、IP、组件，内容包括“etcd, kube-apiserver, kube-Controller-manager, kube-scheduler”等。
画面10：PPT标题为“2.3 Node1安装”，内容包括“在Node1节点上，以同样的方式把从压缩包中解压出的二进制文件kubelet kube-proxy放到/usr/bin目录中。”和“在Node1节点上需要先安装Docker，请参考Master上Docker的安装，并启动Docker”。
画面13：PPT标题为“2.3 Node1安装”，内容包括“在Node1节点上，以同样的方式把从压缩包中解压出的二进制文件kubelet kube-proxy放到/usr/bin目录中。”和“在Node1节点上需要先安装Docker，请参考Master上Docker的安装，并启动Docker”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

