# 08.Kubernetes集群搭建Master安装-kube-apiserver服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\08.Kubernetes集群搭建Master安装-kube-apiserver服务_【海量资源尽在 ubkz.com】.mp4
- 时长 5分7秒（音频 307s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们去把我们的Kubernetes相关的服务安装上首先第一个我们去安装一下Kubernetes API Server我们需要把我们Kubernetes安装这个文件去导入到我们当前的目录下我们退一下CD我们K8s里面我们要RJ去把我们当前的K8s的相关的文件导进来我们这里面应该有个K8s这儿
[00:30] 我们的资料里边这个我们要把Kubernetes Server Linux这个文件导进来之前我们已经介绍过了你可以在网上把它下载下来这样的话我一会儿把它再解压开我们就可以去来进行我们当前Kubernetes的API Server服务的安装我们来看一下它这里边还没有完成有点慢这个文件稍微有点大OK了我这个已经上传完了
[01:00] 然后我们可以看一下我们把它解压开JSVF我们的Comlabs我们等它解压完我们去进入它的目录下面去看一看在我们Comlabs API Server安装其实跟刚才的步骤是一样的我们需要把我们指定的这三个文件copy一下也是copy到user的bmool下你可以去执行这条命令
[01:30] 在我们当前这下面再创建一个Kubernetes server的一个服务那再去做它的一个配置文件就可以了那我们看一下这边完成解压完了以后呢我们LL一下现在呢我已经解压开了那我进入我这个Kubernetes这个目录下面大家看进入这个server这个目录在这个下面呢还有个beam目录在这下面我们可以找到我们想要的文件这里边说我们首先要做的事情是
[02:00] 将这么几个文件呢copy过去稍等一个是Kuber-API server那我们这里面应该可以找到Kuber-API server还有一个是Kuber-ControllerManager就是它还有一个是Kuber Schedule那我们就可以把它copy一下刚才说的Kuber-API server然后还有一个是Kuber-ControllerManager还有一个是Kuber-Schedule
[02:29] OK你把这几个文件都拷贝到user下的bin目录下把他们都拷贝过去拷贝过去以后其实我们就相当已经把服务安装完了接下来你在这个下面去编辑我们当前的这么一个文件也就是它的Service文件我们需要vi一下user下的lab下的我们的systemd下的system再去创建一个文件
[02:59] couple-api-server.serverse这个文件是不存在的我们去把它手动编辑一下在这里呢你把这段配置粘贴过来OKshift jj这样的话就OK了然后呢你再去创建一下它的配置文件把这个相关的配置信息标注一下那我们需要呢去先创建一个make dir
[03:29] 目录ETC下我们的ETSORRY应该是ETC下的KUBERNETESKUBERNETES我们创建这个目录然后呢我们在这个目录下呀去创建它的一个配置文件叫APISERVER这个文件注意这个文件里面呢我们要写些命令你粘贴的时候也要注意了
[03:57] 这个命令啊是这样的首先呢我们来看一下这里呢我们指定etcd的服务的ip然后呢指定了一下我们随可以去访问也说0.000都可以这个注意一下然后呢我们又指定了对外开放的端口然后指定了我们这个整个集群的一些整个集群的哎稍等整个集群的这个网关
[04:28] 我们把这都给它往上缩进一下OK这个里边也是我们把这个格式稍微调整一下要不然我们后续会有问题的这样的话我们配置文件就可以了是不是这你把这些都做完以后我们其实对于我这个Kubernetes API Server就已经安装完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中安装并配置 Kubernetes 的 etcd、kube-apiserver 和 kube-Controller-manager 服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示了通过 SecureCRT 连接服务器后，执行 systemctl daemon-reload 命令，随后查看 etcd 服务状态，确认其已运行。
画面 2: 在文件资源管理器中，用户正在选择一个名为 “duheng” 的文件夹，准备进行后续操作。
画面 3: 在 SecureCRT 会话中，用户执行了 systemctl start etcd.Service 命令，启动 etcd 服务。
画面 4: 用户在终端中执行了 tar -zxvf 命令，解压 Kubernetes 服务器的安装包。
画面 5: 继续解压操作，显示了解压后的文件列表，包括 kube-apiserver、kube-Controller-manager 等组件。
画面 6: 展示了 PPT 页面，标题为 “2.2.4 kube-Controller-manager 服务”，并显示了 kube-Controller-manager 服务的配置文件路径。
画面 7: 继续解压操作，显示了解压后的文件列表，包括 kube-apiserver、kube-Controller-manager 等组件。
画面 8: 用户在终端中执行了 cd 命令，进入 /usr/local/bin 目录，准备安装服务。
画面 9: 展示了 GitHub 上 Kubernetes 的 etcd 3.3.9 版本的发布页面，用户正在查看相关文件。
画面 10: 用户在终端中执行了 cp 命令，将解压后的组件复制到 /usr/bin 目录。
画面 11: 用户在终端中执行了 cp 命令，将解压后的组件复制到 /usr/bin 目录。
画面 12: 展示了 PPT 页面，标题为 “2.2.4 kube-Controller-manager 服务”，并显示了 kube-Controller-manager 服务的配置文件路径。
画面 13: 展示了 PPT 页面，标题为 “2.2.4 kube-Controller-manager 服务”，并显示了 kube-Controller-manager 服务的配置文件路径。
画面 14: 用户在终端中执行了 vi 命令，编辑 /etc/kubernetes/kube-Controller-manager.Service 文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
systemctl daemon-reload
systemctl enable etcd.Service
systemctl start etcd.Service
etcdctl cluster-health

画面 3:
systemctl start etcd.Service
etcdctl cluster-health

画面 4:
tar -zxvf kubernetes-server-linux-amd64.tar.gz
cd kubernetes/server/bin
ls

画面 5:
ls

画面 6:
vi /etc/kubernetes/apiserver
KUBE_API_ARGS="-storage-backend=etcd3 -etcd-servers=http://127.0.0.1:2379 --insecure-bind-address=0.0.0.0 --insecure-port=8080 --Service-cluster-ip-range=10.0.0.1/24 --Service-node-port-range=30000-32767 --admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota --log-dir=/var/log/kubernetes --v=2"

画面 7:
ls

画面 8:
cd /usr/local/bin
ls

画面 9:
https://github.com/kubernetes/kubernetes/releases

画面 10:
cp kube-apiserver kube-Controller-manager kube-scheduler kubelet /usr/bin/

画面 11:
cp kube-apiserver kube-Controller-manager kube-scheduler kubelet /usr/bin/

画面 12:
vi /etc/kubernetes/apiserver
KUBE_API_ARGS="-storage-backend=etcd3 -etcd-servers=http://127.0.0.1:2379 --insecure-bind-address=0.0.0.0 --insecure-port=8080 --Service-cluster-ip-range=10.0.0.1/24 --Service-node-port-range=30000-32767 --admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota --log-dir=/var/log/kubernetes --v=2"

画面 13:
vi /etc/kubernetes/apiserver
KUBE_API_ARGS="-storage-backend=etcd3 -etcd-servers=http://127.0.0.1:2379 --insecure-bind-address=0.0.0.0 --insecure-port=8080 --Service-cluster-ip-range=10.0.0.1/24 --Service-node-port-range=30000-32767 --admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota --log-dir=/var/log/kubernetes --v=2"

画面 14:
vi /etc/kubernetes/kube-Controller-manager.Service
KUBE_CONTROLLER_MANAGER_ARGS="--master=http://127.0.0.1:8080 --log-dir=/var/log/kubernetes --v=2"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6:
标题: 2.2.4 kube-Controller-manager 服务
内容: kube-Controller-manager 服务依赖于 kube-apiserver 服务。
画面 12:
标题: 2.2.4 kube-Controller-manager 服务
内容: kube-Controller-manager 服务依赖于 kube-apiserver 服务。
画面 13:
标题: 2.2.4 kube-Controller-manager 服务
内容: kube-Controller-manager 服务依赖于 kube-apiserver 服务。
画面 14:
标题: 2.2.4 kube-Controller-manager 服务
内容: kube-Controller-manager 服务依赖于 kube-apiserver 服务。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

