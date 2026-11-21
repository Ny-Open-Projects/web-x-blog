# 05.docker安装

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\05.docker安装_【海量资源尽在 ubkz.com】.mp4
- 时长 7分3秒（音频 423s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,接下来我们来讲解一下Docker的安装与启动首先我们第一个环节就是来说一下Docker的安装Docker官方建议在乌帮图下安装因为我们说Docker本身就是基于乌帮图来发布的这个乌帮图也是属于Linux系统的一种
[00:22] 但是我们之前所学习的 Linux都是synthos所以说我们这里也可以把Docker装到synthos上synthos这里注意的版本用的是synthos 7.x版本也就是说建议是在装在7.x版本之上我们如果说在6.x版本中会有一些问题比如说这时候你需要去安装一些其他很多环境
[00:51] 另外很多DAO和补丁它也不支持更新所以说如果说你采用的是synos那么就一定是采用7.x以上版本我们在这里已经给大家提供了配套的synos的镜像这个镜像是我vray镜像你说我们这里首先应该装一个synos7.x镜像都给大家已经提供了大家首先把synos7的镜像解压
[01:21] 加之后呢我们这里双击这个vmx这个这个这个文件双击一下双击之后呢这时候呢就将这个镜像已经挂载到这个vmware了啊那这时候我们怎么办呢我们可以启动一下启动一下好现在正在启动我们可以把这个send s7呢想象成是一个服务器啊想象服务器啊这里我们输入密码rootitcast密码是itcast
[02:05] 好现在就已经进入到Synos 7了我目前给大家提供的版本是不带桌面的这时候我们可以通过IP ADDR命令我们可以查看当前的系统的这么一个IP当前系统IP这当系统IP是192.168.184.141所以说我们现在就通过
[02:35] 通过什么通过这个secret CRT然后通过它来进行连接打开打开之后咱们这里配一个新的这么一个连接主机名192.168.184.141端口默认是22用户名是root接下来我们点一下完成好然后点一下连接之后我们这里
[03:11] 点击选择接受并保存密码我们输入itcast点击保存密码点确定好现在我们就已经远程的连到这台服务器上了我们可以把它想象成是一个服务器我们说这个系统本身sendOS7的系统就是什么就是我们所说的宿主机后面我们多次会提到这个概念叫宿主机那么把连接上之后
[03:42] 接下来我们再做一些其他的一些环境上的一个选择就是环境上风格的一个选择比如说仿真这里我们选择 Linux这时候界面就变成了黑色另外再改一下什么改一下我们的外观里的编码字符编码我们改成 utm 钢板否则的话就是在遇到一些中文的时候我就回乱码好这是我们说的
[04:14] 第一步就是把环境准备好了环境准备好之后接下来咱们就说一下怎么去安装安装其实这些步骤大家都不用去做了因为我给大家所提供的CentOS旗舰镜像都已经完成这些步骤了所以说我们在这里就简单了解一下第一步我们要去将我们的YAML包更新到最新也就是说通过YAML
[04:43] update这个命令来更新这个样本身的软件然后第二步呢就是要安装需要的这个软件包我们需要什么软件包呢需要去用到一个什么呢用到了一个yamutil这么一个工具包这工具包呢需要去安装的啊需要通过这个样命令来进行一个安装那么安装呢这里提供了一个叫yamconfig manager这么一个功能啊
[05:13] 这个功能我们后边会用到,就是一个工具包,然后工具包里提供这么一个功能,我们会后边去用,另外两个就是说我们它本身的一个驱动的依赖,我们需要去执行这句话来进行安装,安装之后接下来我们要什么,要去用到了 YAML Config Manager,用它干嘛的,主要是用来设置YAML的YAML源为阿里云,
[05:41] 那么如果说是你不设置这个源的话,那个那个源的话,样本的话,他就会默认找什么呢,找这个国外的这个站点啊,那这样一来呢,还有可能你后边这个安装就会有问题啊,就会通过这个网络问题就连接不上,所以说我们这里呢,通过这个改变一下这个样,样,这个源为阿里云,就是通过这句话啊,啊,进行一个设置,设置好之后呢,我们第四步就是要安装DAO壳了,安装DAO壳,
[06:11] 安装Docker的话这里注意要安装什么安装Docker CE也就是说Docker这个软件在1.313版本之后它都分为两个版本两个版本一个是Docker的CE一个是Docker EE那么CE就是社区版EE就是企业版那么企业版是收费的而Docker的CE是社区版是免费使用的这是我们说的安装
[06:40] 那么接下来我们说安装成之后我们可以通过dark-v来查看一下当前的版本当前版本我们用的是18.06.1这个版本是CE的版本好这就是关于dark的安装咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 CentOS 7 系统上安装和配置 Docker，并设置镜像加速器。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Docker 安装与启动章节的文档，内容为安装前的说明，包括更新 yum 包、安装必要软件包、设置 yum 源等步骤。
画面 2: VMware Workstation 界面，显示 CentOS7 虚拟机的设置页面，准备启动。
画面 3: VMware 启动过程，显示 VMware 标志和启动信息。
画面 4: Windows 文件资源管理器，显示 CentOS7 的安装文件（.vmdk, .vmx, .mdk 等）。
画面 5: Windows 桌面，显示 Docker 安装文档的预览窗口。
画面 6: Windows 桌面，显示“传智播客”和“黑马程序员”的联合出品标志。
画面 7: SecureCRT 登录提示，提示主机的 DNS 解析问题。
画面 8: SecureCRT 登录成功，显示 root 用户的命令行界面。
画面 9: SecureCRT 会话选项，设置记录文件路径。
画面 10: Docker 安装文档，显示安装步骤，包括更新 yum、安装软件包、设置阿里云源。
画面 11: Docker 安装文档，显示安装步骤，包括安装 Docker-ce 和验证安装。
画面 12: Docker 安装文档，显示设置 uSTC 镜像的步骤，包括编辑 /etc/Docker/daemon.json 文件。
画面 13: SecureCRT 命令行界面，显示空白屏幕，准备执行命令。
画面 14: Docker 安装文档，显示设置 uSTC 镜像和启动 Docker 的步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
(1) yum 包更新到最新
sudo yum update
(2) 安装需要的软件包。yum-util 提供 yum-config-manager 功能，另外两个是 devicemapper 驱动依赖的
sudo yum install -y yum-utils device-Mapper-persistent-data lvm2
(3) 设置 yum 源为阿里云
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/Docker-ce/linux/centos/Docker-ce.repo
(4) 安装 Docker
sudo yum install Docker-ce
(5) 安装后查看 Docker 版本
Docker -v

画面 10:
(1) yum 包更新到最新
sudo yum update
(2) 安装需要的软件包。yum-util 提供 yum-config-manager 功能，另外两个是 devicemapper 驱动依赖的
sudo yum install -y yum-utils device-Mapper-persistent-data lvm2
(3) 设置 yum 源为阿里云
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/Docker-ce/linux/centos/Docker-ce.repo
(4) 安装 Docker
sudo yum install Docker-ce
(5) 安装后查看 Docker 版本
Docker -v

画面 12:
编辑配置文件：
vi /etc/Docker/daemon.json
在该文件中加入如下内容：
{
  "registry-mirrors": ["https://Docker-mirrors.ustc.edu.cn"]
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2 Docker安装与启动”，子标题为“2.1 安装Docker”。
画面 10: PPT 标题为“2.1 安装Docker”。
画面 12: PPT 标题为“2.2 设置ustc的镜像”，内容为 uSTC 镜像的介绍和配置文件编辑说明。
画面 14: PPT 标题为“2.2 设置ustc的镜像”和“2.3 Docker的启动与停止”，内容为设置镜像和启动 Docker 的命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

