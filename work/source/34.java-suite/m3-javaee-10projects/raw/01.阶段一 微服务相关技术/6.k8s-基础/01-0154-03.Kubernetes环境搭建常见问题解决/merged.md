# 03.Kubernetes环境搭建常见问题解决

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\03.Kubernetes环境搭建常见问题解决_【海量资源尽在 ubkz.com】.mp4
- 时长 5分55秒（音频 355s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们就说一下在我们这个快速入门案例里面我们经常会遇到的一页问题第一个就是一个关于DAO科铺失败的原因这个原因其实非常简单就是因为我们当前的网络那么我们国家对一些国外的这些玉饼进行了屏蔽我们在下载的时候它这个DAO科拉紧性会失败这里边给大家提供两种方案
[00:26] 大家可以去参考的这个方案去执行操作就可以了这里边我就不过多去执行了那么你执行完以后其实这里边有一个比较重要的就是说我们要对Kubernetes下的Kubernetes配置文件进行修改比如说我们在执行完操作以后我们要去做这么一件事就是对我们当前ETC下的Kubernetes下的一个叫做Kubernetes这么一个配置文件进行修改而这个配置文件修改的时候我们
[00:55] 给了两种方案第一种方案呢我们是要去修改我们当前这个配置文件里面的值这么的一个值我把它copy过来回到我当前的配置文件里在这边i我去给它copy一下那这个位置啊你一定要注意我们其实是相当于把这个镜像啊下载到了本地我在本地呢会生成这么一个镜像文件然后呢我们去把它下载
[01:23] 那第二种方案呢其实是对这个产生进行修改我们也是把镜像呢下载下来了然后呢我们在里面呢对它进行了一个本地化的镜像的一个指向我把它呢copy过来在这边我们无论怎么玩呢这两个操作都是把我们这些原本在网上当不下来的这些镜像啊我们干什么呢在本地呀去重新给它当了一下OK
[01:55] 我们save the jj退出一下那退出以后呢我们在这里边需要去做一件事System Controller然后我们要去restart一个叫做Kubernetes的一个服务然后呢你在这里边通过Kubernetes Controller去get pose的时候你看一下我当前这个服务的状态还是这种ready也就是说是我们的continue creating状态你呢
[02:25] 可以去稍等一下他因为应该有点慢你看我们现在是不是已经跑起来一个一个是running了两个都OK了running了也就是我们现在通过刚才给大家看到的讲义上的这两种方案你能解决我们拉曲镜像失败的问题那么拉曲镜像失败以后我们再去访问的时候其实还是会遇到一个问题就是我们的外网是不能访问的我们需要对我们当前ETC下的一个叫做Sysctl可贝格文件
[02:55] 做一些修改在它的里面呢你需要去添加这么一个参数也就是回来你可以看一下我们这里呢有一个文件我们cat一下-etc下的有一个叫做sysctl.cpc这么一文件在这个文件呢我最后加了这么一行看到了吧这一行呢其实是帮我做自动跳转那如果你这个没问题以后呢我们就可以干什么呢去进行一个浏览器的访问了
[03:24] 在这里呢我再去看一下东西啊Kubernetesctl.get svc我看一下我的服务我这服务也有的对吧那在这里呢我们去重新把它打开一次我们现在应该还是加载不上稍等我们这里面还是加载不上是吧加载不上的话呢应该是我们进入到我们的user下的location Kubernetes里面我在这呢去把我们所有的这些服务呢我都重新去
[03:57] 创建一下,Kubernetes CTR,我replace一下我们当前的MyTOMCAT RC我让他去重新replace一下然后呢,我Kubernetes CTR我们去delete一下我们当前的这个所有的服务Kubernetes CTRdelete,sorry,落了一个刚刚all这样的话呢,我再去通过他呀,create一下我们当前的My
[04:28] 他们看看SVC这个文件OK了然后呢我们再试一下看看是否可以访问的OK这样的话呢我们就访问到了我们当前这个容器了那这是给大家做了一个简单例子去展示了一下我们通过Kubernetes去管理我们的容器那在这里面我要强调一点我虽然是在一台机器上去操作其实我这台机器既是master也是node那这里边我们在
[04:59] 快速入门的案例里面所涉及到一些概念像我刚才说的master node还有我们这个cumulant这些我们后续都会给大家介绍我希望大家能通过这个快速入门案例你参考我的讲义去把它完成以后能大概理解说我们通过这个cumulant可以去快速的去把我们的整个集群的应用去建立起来并且我们可以去方便的进行去扩容这个扩容操作其实也比较简单就是我之前说的
[05:29] 你在这里边replace等于2其实就相当于去建立两个pull那大家呢如果在做这个案例过程中遇到的问题呢可以参考我讲义上的这几个方案这里面说了一下关于pull拉取失败的问题还有说了一下外网不同访问还有我们前期的在你去get pose的时候你会拿不到这个数据那这里面都给大家解释了一下应该如何去完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Kubernetes 集群中部署并调试一个名为 mytomcat 的 ReplicaSet 应用，包括解决镜像拉取失败、kubelet 配置错误、服务访问问题等常见部署故障。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程 PPT 的目录结构，当前章节为“2.2 Master安装”，子章节包括“Docker安装”、“kube-apiserver服务”、“kube-Controller-manager服务”、“kube-scheduler服务”、“Node安装”、“kubeadm安装”、“kube-proxy服务”、“自启”、“Node安装”。
- PPT 内容显示了“问题解决”部分，标题为“Docker pull失败”，解决方案包括：
  1. yum install -y
  2. Docker pull registry.access.rechat.com/.../pod-infrastructure:latest
- 画面底部有“黑马程序员”的水印和宣传语。

画面 2：
- 在 SecureCRT 中执行了命令：`kubectl get pods`。
- 输出结果显示了三个 Pod：`mytomcat-fzg2`、`mytomcat-pb6d2`、`mytomcat-pb6d2`，状态均为 `ContainerCreating`，表明应用正在启动但尚未就绪。

画面 3：
- PPT 内容显示了“解决方法”部分，标题为“Docker pull失败”，解决方案包括：
  1. Docker pull kubernetes/pause
  2. Docker tag Docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. Docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_POD_INFRA_CONTAINER 变量：
     KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.126.143:5000/pod-infrastructure:latest"
  6. 重启服务：systemctl restart kube-apiserver systemctl restart kube-Controller-manager systemctl restart kube-scheduler systemctl restart kubelet

画面 4：
- 在 SecureCRT 中执行了命令：`systemctl restart kubelet`。
- 执行 `kubectl get pods` 后，输出显示 `mytomcat-fzg2` 和 `mytomcat-pb6d2` 的状态变为 `Running`，表明应用已成功启动。
- 画面底部显示了 `/etc/kubernetes/kubelet` 文件的配置内容，其中包含：
  KUBELET_API_SERVER="--api-servers=http://127.0.0.1:8080"
  KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.126.144:5000/pod-infrastructure:latest"
  KUBELET_ARGS="--pod-infra-container-image=192.168.126.144:5000/pod-infrastructure:latest"

画面 5：
- PPT 内容显示了“解决方法”部分，标题为“Docker pull失败”，解决方案包括：
  1. Docker pull kubernetes/pause
  2. Docker tag Docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. Docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_ARGS 变量：
     KUBELET_ARGS="--pod-infra-container-image=192.168.126.143:5000/google_containers/pause-amd64:3.0"
  6. 重启 kubelet 服务：systemctl restart kubelet

画面 6：
- PPT 内容显示了“外网不能访问”的问题及解决方案：
  1. vim /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. 解决 kubectl get pods 无资源问题：vim /etc/kubernetes/apiserver，找到 KUBE_ADMISSION_CONTROL="..."，并添加 admission_control_namespaces=... 等参数。
  4. 重启服务：systemctl restart kube-apiserver

画面 7：
- 在 SecureCRT 中执行了命令：`net.ipv4.ip_forward=1`。
- 画面底部显示了 `/etc/sysctl.conf` 文件的内容，其中包含：
  net.ipv4.ip_forward=1

画面 8：
- 浏览器访问了 `http://192.168.126.144:8080`，显示 Apache Tomcat 8.5.33 的欢迎页面，表明应用已成功通过外部访问。

画面 9：
- 在 SecureCRT 中执行了命令：
  1. cat /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. kubectl get svc
  4. kubectl delete svc mytomcat-svc
  5. kubectl delete svc --all
- 输出显示了服务列表和删除操作的结果。

画面 10：
- PPT 内容显示了“外网不能访问”的问题及解决方案：
  1. vim /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. 解决 kubectl get pods 无资源问题：vim /etc/kubernetes/apiserver，找到 KUBE_ADMISSION_CONTROL="..."，并添加 admission_control_namespaces=... 等参数。
  4. 重启服务：systemctl restart kube-apiserver

画面 11：
- PPT 内容显示了“systemctl start kube-proxy”和“Tomcat配置”部分。
- 显示了名为 `mytomcat-svc.yaml` 的 YAML 配置文件内容：
  apiVersion: v1
  kind: ReplicationController
  metadata:
    name: mytomcat
  spec:
    replicas: 2
    selector:
      app: mytomcat
    template:
      metadata:
        labels:
          app: mytomcat
      spec:
        containers:
          - name: mytomcat

画面 12：
- PPT 内容显示了“解决方法”部分，标题为“Docker pull失败”，解决方案包括：
  1. Docker pull kubernetes/pause
  2. Docker tag Docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. Docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_ARGS 变量：
     KUBELET_ARGS="--pod-infra-container-image=192.168.126.143:5000/google_containers/pause-amd64:3.0"
  6. 重启 kubelet 服务：systemctl restart kubelet

画面 13：
- PPT 内容显示了“外网不能访问”的问题及解决方案：
  1. vim /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. 解决 kubectl get pods 无资源问题：vim /etc/kubernetes/apiserver，找到 KUBE_ADMISSION_CONTROL="..."，并添加 admission_control_namespaces=... 等参数。
  4. 重启服务：systemctl restart kube-apiserver

画面 14：
- PPT 内容显示了“解决方法”部分，标题为“Docker pull失败”，解决方案包括：
  1. Docker pull kubernetes/pause
  2. Docker tag Docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. Docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_ARGS 变量：
     KUBELET_ARGS="--pod-infra-container-image=192.168.126.143:5000/google_containers/pause-amd64:3.0"
  6. 重启 kubelet 服务：systemctl restart kubelet

