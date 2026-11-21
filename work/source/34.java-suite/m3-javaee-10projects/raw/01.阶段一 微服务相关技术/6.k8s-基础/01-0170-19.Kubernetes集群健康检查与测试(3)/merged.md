# 19.Kubernetes集群健康检查与测试(3)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\19.Kubernetes集群健康检查与测试(3)_【海量资源尽在 ubkz.com】.mp4
- 时长 11分52秒（音频 712s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们把这些在我们讲的东西做一个总结首先来看一下我们的K8s的一个架构和主架那么我们在这个案例里边我们用到了Kuber CTL然后我们也用到了Kuber API Server还有Schedule还有我们的Replication Controller这里边也看到了Node还有我们的Master大家来看我们这个用户是通过Kuber CTL提交运行我们的Docker的container
[00:30] 运行我们这个Docker的容器其实就是一个POD那POD在我们这个Grenace里面它是一组这个容器或者是一个容器的一个组合那API Service它是把请求存储到我们的具体的ETCD里面其实就是一个数据库那Skydew它是去运行这种分配扫描它是确定我们具体当前这个POD运行在哪个node节点上
[00:55] 那我们Kubelet呢它是找到我们自己需要的container在本机上运行那么我们可以通过用户提交的RC也就是我们的replication Controller来监视我们集群中的这个容器并保持数量那我们在之前的这里边可以看一下我们cat一下我们当前的这个endings-rc
[01:22] 在这个文件里面我们当前的这个就是一个replication Controller它是规定了我们是什么样的一个镜像的容器就是我们在运行的是什么然后它也规定了我们当前的什么一个数量这个数量确定了我们的一个副本的数量所以回来刚才我们说到的这个replication Controller它是接受我们机器中的容器并保持我们的数量的
[01:47] 那么用户提交Service描述文件由我们的Kubernetes负责具体的工作流量的转发我们刚才的也是在这里endings-svc我们在这个文件里面来确定具体我们当前服务我们可以去对外映射我们的端口以及我们当前Kubernetes所选择的这种端口类型我们采用的是这种叫做node-port
[02:15] 那我们整个在这里面master还有我们所说的node那这两个它俩都具体有什么样的服务在里面呢我的master里面呢有这个kubernetes api server那kubernetes api server就是这部分它呢是整个我们kubernetes系统一个入口
[02:33] 其封装了核心对象的一个周端改善操作它是以RESTful这种API接口方式提供给我们外部客户和内部的主线调用维持维护我们的REST对象的持久化到ETC中的存储整个我们当前Master API Server它其实就是我们整个的一个入口所有的无论是我们的node还是外部访问其实都是从我们入口去走的
[02:59] 那Compliance Schedule它就是一个什么呢协调的它是为新建立的Pod进行这种节点选择分配的它就是一个协调相当于一个管家它规范了我们当前的Pod具体在哪一个Node上去运行它负责我们基金的资源的调度逐渐的抽离可以方便的替换成其他的调度器那Compliance Controller它是什么呢它是负责执行各种控制器目前已提供很多种控制器来保证Compliance的正常的运行
[03:28] 还有我们最重要的一个叫replication Controller它是管理我们维护我们当前的一个replication Controller它关联了POD保证replication Controller的定义的副本数量与实际运营的POD数量一致我们是在我们当前的replication Controller里面去定义副本的这句话说的其实还是刚才大家看到的这个也就是说我们通过replicase去定义我们当前的一个副本的数量
[03:55] 那Node才是真正干活的,master它是整体上它其实就是一个协调管理,那Node才是真正干活。
[04:02] 那我们Node有我们的Kubernetes,有我们的Kubernetes Proxy,还有Docker。
[04:10] 我们Node上一定要装Docker,它是干什么的?
[04:13] 我们真正的容器运营服务都是通过Docker去做的。
[04:17] 那我们Kubernetes它是通过负责管理,负责管控的一个容器。
[04:21] Kubernetes会从Kubernetes API Server接收我们POD创建请求然后启动和停止容器监控容器运行状态并汇报给Kubernetes API Server也就是说它会一直去跟Kubernetes的API Server去关联一直保持一个同步那我们的Kubernetes Proxy它是负责为我们的POD创建这种代理部Kubernetes Proxy会从Kubernetes API Server获取所有的Service信息
[04:50] 并根据那个Service信息创建代理服务实现Service到pod的请求路由和转发从而实现我们的proxy层级的虚拟转发网络也就是说我们在这里面看到的proxy它其实真正对外访问时我们可以通过proxy去代理去走到我们这里边这是整个我们的一个Kubernetes架构
[05:11] 那我们再往下看我们在搭建过程中啊所遇到的一些问题这里面呢我主要给大家列举出了这么一些问题第一个呢就是简单点的我们在get pose或者是我们在get nodes时啊如果出现这种叫做no resource func的问题那你呢就需要去改一下我们这个API Service的配置文件里面去掉它里面一个叫做Service account那上下就是一个关于我们这个容器拉取失败那这个原因呢其实
[05:41] 其实比较简单就是因为我们国内的网络啊他这个在访问一些网站时可能会因为网络原因产生一些问题所以呢我们需要去通过Docker的一些私有化的仓库去解决那么在这个过程中我们就需要去搭建一个Docker的私有仓库把经线拉取出来以后呢我们放到私有仓库里边然后后续呢我们可以去通过私有仓库啊去
[06:07] 帮助我们建立数据也说我们需要在这整个过程中搭建一个DAO科的私有仓库这是说一下关于我们破坞数据拉取失败的问题这些说完以后大家再看一下下面这是一个我们Kubernetes里面用到的一些命令在我Kubernetes里面我用到了Kubernetes CTL的一个get pose我们可以叫做get pose
[06:34] 其实这个呢是我们获取当前命名空间下的这些容器也就是说我们在当前这里边通过Kuber CTL guide pose我们就可以得到这是有三个容器三个容器呢是刚才我在repation Controller里边去定义的这个副本的一个数量然后呢我们可以获取容器的列表你可以通过Kuber guide allKuber control guide all
[07:01] 我们在这里边可以获得我们整个的一个相关的所有的数据那这里边不仅仅有什么呢我们当前的这些pod还有我们的Service那我们这里边刚才看到的一个index这是我们自己的一个Service然后我们再来看一下还有呢它可以通过这种叫cubercredit-f然后呢你去指定一个我们当前的加密文件去帮助我们创建容器那在我们之前的讲义里边
[07:32] 我们在这个里边也是通过这样的一条命令去创建的然后我们也可以去删除中介在这里呢我可以给大家演示一下我们怎么去删除啊那我们在这呢可以看一下我现在呢Kuberctl get svc我们可以删除我们的服务Kuberctl delete然后呢-f我们直接把它删掉哎我看一下啊他说我们这个不存在
[08:04] sorry, kuberctlgetpose吧我们删这个, kuberctl我们delete-fsorry,不是删我那个名字应该是删我的这个文件也就是说这个我们这里面不有两个文件吗我们应该这么执行kuberctl, d-e-l-e-t我们-f我们可以写个Nginx-rc,yaml那我们也可以去执行
[08:34] SVC YAML然后我们可以看Kubernetes CTL Get SVC这时候对服务它会干什么呢去重新建立起来我们也再来看这个Kubernetes CTL Get我们的pose这时候我们是不是就没有那pose了那我们可以Cret-fngx-rc.yaml那我们再来看Get pose
[09:03] 我们就把这几个服务又重新建立起来了然后我们Coopersctl我们把这个cretcrate-fngx-svc我把这个重新去创建一下我们再来get a pose一下当前我这个状态它刚才全都是0有点问题我现在再执行一遍你会发现全都起来了running
[09:34] 那这个是关于我们当前去删除容器以及创建容器然后呢你可以指定pode跑在哪一个node上大家回去呢可以自己看一下你也可以查看我们的这个日志的一些容器的这个整个的状态也就是说我们可以过来清掉Kuberctl我看一下该的pose吧应该是logs应该这么办吧该的poseKuber
[10:06] ctl logs,他应该是加上这个名字我们这里面没有看到这个具体信息是吧那我们如果看不到的话呢可以这么办couplectl get pose现在呢我们可以通过叫做dsc describedscriberibe然后呢pose后面加上一个具体的名字
[10:40] 我们去看它的一些具体信息那这是刚才我们说看具体信息啊下面呢还有可以去进入我们的容器的一个终端命令我们可以在这里边把这个执行一下那个容器名字呢我们用它然后- 并线的batch那这时候呢你就进入到了你当前的这个容器里边
[11:13] 你就可以看到我们其实是已经在这个Nginx里了OK我可以通过USIT退出这个有点跟我们的Docker就比较相像了那你也可以在一个Port里面还有多个容器用这个container或scansc这种容器去指定那容器的列表刚才我已经给大家看了然后你还可以通过Cover
[11:32] Controller guide svc查看整个容器状态这个命令呢在之前都给大家演示过那整个课程里面呢其实我们还是一个相对来说比较简单的快速入门课程后续有时间我们可以去对Chrome OS的这个学习啊进行一个深入的学习

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Kubernetes 集群的搭建、核心组件功能及常用命令操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: SSH 登录到 Kubernetes 主机，终端提示符为 [root@bogon Kubernetes]#。
画面 2: PPT 页面，标题为“1.1 Master”，展示 Kubernetes Master 节点架构图，包含 api server、scheduler、replication Controller、kubelet、kube-proxy 等组件，并列出各组件功能说明。
画面 3: 与画面 2 内容相同，PPT 页面展示 Kubernetes Master 节点架构图及组件功能。
画面 4: PPT 页面，标题为“1.1 Master”，内容与画面 2 相同，但下方新增“1.2 Node”部分，列出 Kubelet 和 Kube-proxy 的功能。
画面 5: PPT 页面，标题为“总结”，展示 Kubernetes 架构图，包含 api server、scheduler、replication Controller、kubelet、kube-proxy、etcd、node、Internet 等组件，并列出各组件功能说明。
画面 6: PPT 页面，标题为“1.2 Node”，内容与画面 4 相同，展示 Kubelet 和 Kube-proxy 的功能。
画面 7: PPT 页面，标题为“3.常用命令”，列出获取容器、创建容器、删除容器、查看 Pod 状态、查看容器日志、进入容器终端等常用 kubectl 命令。
画面 8: PPT 页面，标题为“3.常用命令”，内容与画面 7 相同，展示常用 kubectl 命令。
画面 9: VS Code 编辑器界面，打开文件“Nginx-rc.yaml”，内容为 ReplicationController 的 YAML 配置，定义了名称、副本数、标签选择器、容器镜像和端口。
画面 10: SecureCRT 终端界面，显示执行了 kubectl delete -f Nginx-svc.yaml 命令，删除了服务，随后执行 kubectl create -f Nginx-svc.yaml 创建服务，最后执行 kubectl get pods 查看 Pod 状态。
画面 11: SecureCRT 终端界面，显示执行了 kubectl delete -f Nginx-rc.yaml 命令，删除了 ReplicationController，随后执行 kubectl create -f Nginx-rc.yaml 创建 ReplicationController，最后执行 kubectl get pods 查看 Pod 状态。
画面 12: VS Code 编辑器界面，打开文件“Nginx-svc.yaml”，内容为 Service 的 YAML 配置，定义了名称、类型、端口、选择器等。
画面 13: SecureCRT 终端界面，显示执行了 kubectl get pods 命令，查看 Pod 状态，显示多个 Nginx Pod 正在运行。
画面 14: VS Code 编辑器界面，打开文件“Nginx-rc.yaml”，内容与画面 9 相同，展示 ReplicationController 的 YAML 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9:
apiVersion: v1
kind: ReplicationController
metadata:
  name: Nginx
spec:
  replicas: 3
  selector:
    app: Nginx
  template:
    metadata:
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
        ports:
        - containerPort: 80

画面 12:
apiVersion: v1
kind: Service
metadata:
  name: Nginx
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: Nginx

画面 6:
o 解决方案1
1. yum install rhsm -y
2. Docker pull registry.access.redhat.com/rhel7/pod-infrastructure:latest
如果以上两步解决了问题，那么就不需要在执行下面操作
3. Docker search pod-infrastructure
4. Docker pull Docker.io/tianyeb/pod-infrastructure
5. Docker tag tianyeb/pod-infrastructure 192.168.126.143:5000/pod-infrastructure
6. Docker push 192.168.126.143:5000/pod-infrastructure
7. vi /etc/kubernetes/kubelet
修改 KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.126.143:5000/pod-infra-container-image:latest"
8. 重启服务
systemctl restart kube-apiserver
systemctl restart kube-Controller-manager
systemctl restart kube-scheduler
systemctl restart kubelet
systemctl restart kube-proxy

o 解决方案2
1. Docker pull Docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
2. Docker tag Docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
3. Docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
4. vi /etc/kubernetes/kubelet

画面 7:
- 获取当前命名空间下的容器
kubectl get pod
- 获取所有容器列表
kubectl get all
- 创建容器
kubectl create -f kubernetes-pvc.yaml
- 删除容器
kubectl delete pods/test-pd 或者 kubectl delete -f rc-Nginx.yaml
- 查看指定pod跑在哪个node上
kubectl get pod /test-pd -o wide
- 查看容器日志
Kubectl logs Nginx-8586cf59-mwwtc
- 进入容器终端命令
kubectl exec -it Nginx-8586cf59-mwwtc /bin/bash
- 一个Pod里含有多个容器，用 -container or -c 参数。
例如:假如这里有个Pod名为my-pod,这个Pod有两个容器,分别为main-app 和 helper-app,下面的命令将打开main-app的shell的登录界面。
kubectl exec -it my-pod -c container main-app -/bin/bash
- 容器详情列表
kubectl describe pod/mysql-m8rb1
- 查看容器状态
kubectl get svc

画面 10:
kubectl delete -f Nginx-svc.yaml
kubectl create -f Nginx-svc.yaml
kubectl get pods

画面 11:
kubectl delete -f Nginx-rc.yaml
kubectl create -f Nginx-rc.yaml
kubectl get pods

画面 13:
kubectl get pods

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“1.1 Master”，架构图中，api server 指向 etcd、scheduler、replication Controller、kubelet、kube-proxy；scheduler 指向 node；replication Controller 指向 node；kubelet 指向 node；kube-proxy 指向 node；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 4: PPT 标题为“1.1 Master”，架构图中，api server 指向 etcd、scheduler、replication Controller、kubelet、kube-proxy；scheduler 指向 node；replication Controller 指向 node；kubelet 指向 node；kube-proxy 指向 node；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 5: PPT 标题为“总结”，架构图中，api server 指向 etcd、scheduler、replication Controller、kubelet、kube-proxy；scheduler 指向 node；replication Controller 指向 node；kubelet 指向 node；kube-proxy 指向 node；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 6: PPT 标题为“1.2 Node”，架构图中，kubelet 指向 node；kube-proxy 指向 node；api server 指向 kubelet、kube-proxy；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 7: PPT 标题为“3.常用命令”，无架构图。
画面 12: PPT 标题为“Nginx-svc.yaml”，无架构图。
画面 14: PPT 标题为“Nginx-rc.yaml”，无架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

