# 16.Kubernetes集群搭建Node2安装

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\16.Kubernetes集群搭建Node2安装_【海量资源尽在 ubkz.com】.mp4
- 时长 7分16秒（音频 436s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢我们讲一下我们这个node2这个节点如何选装那么步骤呢跟node1是一样的那这个时候呢我们就可以去把node1克隆一份那么你只需要注意修改一下IP地址就可以那么来看一下怎么去做呢我们这么办首先呢回到我们当前的这个虚拟机我是我们试验员
[00:28] 在这里边我们把当前这台机器先停一下我们电源关闭然后呢我呢右键管理克隆下一步下一步我创建一个完整的克隆下一步这个呢我们就叫Kubernetes-node2-demo那么你指定到你自己适合的位置我就到我这个目录下Ctrl C
[01:01] OK那这时候呢它正在克隆稍等一下等克隆完以后呢我们把它启动一下好了完成了我们可以关闭这个时候呢我们就已经有个Node2的Demo我们把它开启这时候呢Node2的Demo啊它的IP地址应该跟刚才一样还是148因为我们是完整克隆过来的我什么都没有修改我们在这里边呢
[01:52] 一会通过148应该是可以连接上的稍等一下它正在启动有点慢应该快启动完成了好了我们连一下你看我还是能把它连上的这里面我要处理一下它etc下的sysconfig然后我的network-script我们把一亿付cfd文件重新编辑一下首先第一件事我就要把它改了它的IP地址不在118
[02:28] 而是149第二件事呢我们要重新给它生成一个mark这里边高级我们重新生成一个mark就是c确定确定回到我们自己的这里边我们要把这个mark呀重新给它okshift jj我们保存一下好了那这样的话呢我当前这台机器呀就已经
[02:57] 把它改完了我把它呢重新关了然后我把我这个node1啊先启动因为node2啊让我关掉了对吧那我先把node1启动起来我们这时候再连的时候呢其实它就是node1了稍等一下这边还没起来好了我们再连这个是我的node1是当前是我们当前的148那这个呢是149我重新起一下
[03:51] 在这里呢,我可以重新去建立一个连接149,账户就是root,OK那这个时候可能会连接失败,因为我当前这个149这台机器还没起来关闭,我这边应该应该有一个149,这个我们把它删掉,看着不舒服我这里边应该有149,OK密码,我们保存密码,确定OK了
[04:25] 那这样的话呢我们就连接到当前EVE C1F IG连接到我们当前这台机器了然后回来我在这呢需要去选项绘画我在这个终端外观那会儿啊指定了Utl-8OK那148和149啊这两台机器啊我都起来了但是149呢是从148克隆过来的回头你来看一下我们现在呢
[04:50] 这个node1节点在安装的时候我们coupleit是不是做了一些配置那我们现在来看看我要改一些东西改什么呢首先第一个你就要改的是coupleit这个配置文件所以我们在这里边vi我们etc下的coupleit我们要把这个配置文件改一下这个配置文件要改什么呢192.168.126.142这个有点问题是吧我看一眼
[05:21] 我们现在这个配置文件不对啊这么办我把它呢整个都删掉我把它整个都删掉然后呢我们重新去把它这个粘贴复制一份稍等一下我们这个配置文件这是我们的Kubernetes那么我这个配置文件我们要知道这儿
[05:58] 我们当前这台机器是149ShiftJJOK然后我们再来看VI一下我们这里边有一个配置文件-etc下的我们的Kubernetes下的KubernetesConfig这个文件我好像也是有问题它的服务器应该是147ShiftJJOK
[06:35] 然后我们还有一个是Kubernetes的配置文件我们看看Kubernetes这个配置文件是这个文件我们vi一下etc下的Kubernetes下的proxy这个配置文件来看我们要改的是当前我们服务器是147没问题但是我自己是149OK吧把这个保存cpj
[07:05] 那这样的话呢我们把相应的配置文件里面这些IP改完我们当前这台机器就OK了那也就是说我们的node2这个节点就安装完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 VMware Workstation 中启动并配置 Kubernetes 集群节点（Kubernetes-node1-demo 和 Kubernetes-node2-demo），并通过 SecureCRT 登录进行网络和服务配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: VMware Workstation 主界面，显示虚拟机列表，其中“Kubernetes-node1-demo”被选中，右侧是 SecureCRT 会话窗口，显示登录到 192.168.126.148 的 Linux 系统（CentOS 7）。
画面 2: VMware Workstation 主界面，显示“创建和管理虚拟机”的欢迎页面。
画面 3: 在 VMware Workstation 中，选中“Kubernetes-node1-demo”，弹出“虚拟机设置”对话框，显示“已分配”状态，配置信息包括：内存 8 GB，处理器 4，硬盘 20 GB，网络适配器为 NAT。
画面 4: 启动“Kubernetes-node1-demo”虚拟机，屏幕显示 VMware 启动动画。
画面 5: “Kubernetes-node1-demo”虚拟机启动后，SecureCRT 会话窗口显示登录成功，提示“Last Login: Sat Sep 15 04:15:08 2018 From 192.168.126.1”。
画面 6: “Kubernetes-node1-demo”虚拟机启动后，SecureCRT 会话窗口显示登录成功，提示“Last Login: Sat Sep 15 04:15:08 2018 From 192.168.126.1”。
画面 7: 在 VMware Workstation 中，尝试关闭“Kubernetes-node2-demo”虚拟机，弹出确认对话框，询问是否关闭。
画面 8: 在 VMware Workstation 中，选中“Kubernetes-node2-demo”，右键菜单中显示“Kubernetes-node2-demo”虚拟机路径。
画面 9: 启动“Kubernetes-node2-demo”虚拟机，屏幕显示 VMware 启动动画。
画面 10: “Kubernetes-node2-demo”虚拟机启动后，SecureCRT 会话窗口显示空白。
画面 11: 在 SecureCRT 会话中，执行“ifconfig”命令，弹出“网络配置”窗口，显示多个网络接口，包括“inet 192.168.126.148”。
画面 12: 在 SecureCRT 会话中，执行“ifconfig”命令，显示网络接口信息，包括“lo”和“eth0”接口的详细配置。
画面 13: 在浏览器中打开“马哥智学”网站，页面显示“Kubernetes”相关文档，包括“WorkingDirectory=/var/lib/kubelet”、“ExecStart=/usr/bin/kubelet”等配置。
画面 14: 在 SecureCRT 会话中，执行“vi /etc/kubernetes/kubelet.conf”命令，显示配置文件内容，包括“server: http://192.168.126.148:8080”、“context: local”、“current-context: mycontext”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 13: 
```
Documentaion:https://github.com/GoogleCloudPlatform/kubernetes
After-Docker-Service
Requires=Docker.Service

[Service]
WorkingDirectory=/var/lib/kubelet
ExecStart=/usr/bin/kubelet
ExecStartPre=/usr/bin/mkdir -p /var/lib/kubelet
Restart=on-failure
KillMode=process
RuntimeDirectory=/var/lib/kubelet
RuntimeDirectoryMode=0755
User=root
Group=root
EnvironmentFile=/etc/sysconfig/kubelet
Environment="KUBELET_ARGS=--kubeconfig=/etc/kubernetes/kubeconfig --hostname-override=192.168.126.148 --logtostderr=false --logtostderr=false --v=2 --fail-swap-on=false"
```

画面 14:
```
kind: Config
clusters:
- cluster:
    server: http://192.168.126.148:8080
  name: local
contexts:
- context:
    cluster: local
    user: root
  name: mycontext
current-context: mycontext
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13: PPT 标题为“高可用化的Kubernetes快速入门课程”，左侧目录结构包括“1.Kubernetes概述”、“2.Kubernetes安装”、“2.3 Node安装”等。页面内容包含“Documentaion:https://github.com/GoogleCloudPlatform/kubernetes”、“After-Docker-Service”、“Requires=Docker.Service”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

