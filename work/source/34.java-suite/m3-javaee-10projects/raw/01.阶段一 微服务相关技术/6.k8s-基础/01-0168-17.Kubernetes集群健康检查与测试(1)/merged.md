# 17.Kubernetes集群健康检查与测试(1)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\17.Kubernetes集群健康检查与测试(1)_【海量资源尽在 ubkz.com】.mp4
- 时长 5分22秒（音频 322s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们介绍一下我们的健康检查以及我们的视力测试我们在之前已经把我们的Master 147这台机器以及我们的两个Node 148和149这两台机器已经安装完了那么按照我们现在这种描述说我要查看一下我的集星状态我可以通过Coopers CTL Get Nodes去查看
[00:25] 但你发现呢这时候他是没有找到这个命令啊那这个原因呢是因为我在前期搭建我们的master的时候啊其实我在这里边去copy文件时啊漏掉了一个叫做cooperctl所以呢我们可以回到我们当前的userlocalk8s这个目录下进到我的communize这个目录还有他的
[00:55] serverbin目录下在这下面呢我们cp一下把这个cooperctl这个命令啊copy到我们的user的bin下面sorry啊写错了userbin目录下ok那我们call到这个目录下以后呢我们再回到根目录下你执行cooperctl我们get nodes
[01:21] 那这时候呢我们就可以看到我们当前呢有两台node一个是148一个是149那么如果你在查看的时候你发现呢它报的还是我们前期给你说的一个问题就是在我们的前期快速入门里边提到如果你在get nodes的时候你发现呢你拿到的还是这种叫做这儿
[01:48] NoResourceFound那么你就需要去修改一下这个配置文件里面的信息那OK了那我们现在呢已经看到了我们有两个node也就是说我们找到它了那我们还可以去根据这里面提示说查看一下我们master整个机器的状态那我们来看一下还是CooperCTR我们可以get一下CS那这是这条命令
[02:15] 那么我们看到了我们当前整个机器呢是一个健康的状态OK那这些都完成以后呢我们接下来呀去创建一个Nginx的一个replication的一个文件以及我们的Service文件那么我们把整个工程跑起来那好了我们还是到我们的user下的local下Kubernetes这个目录下那么我们在这里呢
[02:42] 首先创建一个叫ngix-rc.yaml文件那在这个文件里边我们要写些东西那可以拿到在我们今天的资料里面我已经把这个文件呢给你copy出来了你呢把这个文件的内容粘贴复制过去其实在这里边我们描述的主要就是我们创建了一个ngix然后呢我们有三个副本那么我们对外暴露的端口是80端口
[03:13] 然后我们这个image镜像就是我们的endings这是我们把我们的replication创建完了还有我们再去创建一个文件这个文件叫endings-svc也就是我们的Service其实我们在这里边可以再创建一下vi我们一个endings-svc.yaml文件
[03:42] 那这个文件里面的我们要做的事情呢也比较简单点开在这里面我们只需要告诉他我们对外映射的时候是3333这么五个三这个端口我们采用的是这种叫做node port这种网络方式回到我们当前这个文件里面这里面我们把它粘贴过去对不对这这OK那这些执行完以后啊我们可以在这里边来看一下
[04:14] 我们先去创建一下我们当前的replication也就是把我们的node执行一下来我们这里边执行一下cubectl然后create-f index我们要rc这个文件OK那这个时候它就帮我已经创建了然后我们再去把我们的Service也创建一下这里边也有命令叫
[04:45] Kuber-CTL-CRE-ATE我们-f,Nginx-svcOK,那这样呢我就把我们当前的这个Service和我们的这个replication就都创建完了然后我们可以通过get pose方式去看一下那大家来看Kuber-CTL-get pose
[05:09] 那这时候你发现我们又是没有找到什么这个no resource is found有时候我没有找到我们当前的pose那这个时候应该怎么解决呢

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Kubernetes 集群的健康检查与示例测试，包括查看节点状态、组件健康状况、创建 Deployment 和 Service 并验证 Pod 运行。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 标题“2.5 健康检查与示例测试”，终端中执行命令 `kubectl get nodes` 查看集群节点状态。
画面 2: PPT 内容为“2.2.2 etcd服务”，说明 etcd 是 Kubernetes 集群的主要服务，需先安装并启动。列出安装 Docker 的步骤和命令。
画面 3: PPT 标题“2.2.3 kube-apiserver 服务”，终端中执行 `cd bin` 并列出 `kube-apiserver` 等二进制文件。
画面 4: PPT 标题“2.2.3 kube-apiserver 服务”，终端中执行 `kubectl get nodes` 查看节点状态。
画面 5: PPT 内容为“mytomcat.svc.yaml”文件内容，展示 Service 的 YAML 配置，包含 selector、template、labels 和 spec。
画面 6: PPT 内容为“解决 kubelet 问题”，列出解决 kubelet 服务问题的方案，包括修改配置文件、重载服务等。
画面 7: PPT 内容为“解决 kubelet 问题”，列出解决 kubelet 问题的方案，包括修改配置文件、重载服务等。
画面 8: PPT 标题“2.5 健康检查与示例测试”，终端中执行 `kubectl get cs` 查看组件健康状态。
画面 9: PPT 标题“2.5 健康检查与示例测试”，终端中执行 `kubectl get cs` 查看组件健康状态。
画面 10: PPT 标题“2.5 健康检查与示例测试”，终端中执行 `kubectl get cs` 查看组件健康状态。
画面 11: PPT 标题“2.5 健康检查与示例测试”，终端中执行 `kubectl get cs` 查看组件健康状态。
画面 12: PPT 标题“2.5 健康检查与示例测试”，终端中执行 `kubectl get cs` 查看组件健康状态。
画面 13: PPT 标题“2.5 健康检查与示例测试”，终端中执行 `kubectl get pods` 查看 Pod 状态。
画面 14: PPT 标题“2.5 健康检查与示例测试”，终端中执行 `kubectl get pods` 查看 Pod 状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```yaml
selector:
  app: mytomcat
template:
  metadata:
    labels:
      app: mytomcat
spec:
  containers:
    - name: mytomcat
      image: Tomcat:7-jre7
      ports:
        - containerPort: 8080
```

画面 5:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mytomcat
spec:
  type: NodePort
  ports:
    - port: 8080
      nodePort: 30001
```

画面 10:
```yaml
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
```

画面 13:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: Nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: Nginx
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题“2.5 健康检查与示例测试”。
画面 2: PPT 标题“2.2.2 etcd服务”，说明 etcd 是 Kubernetes 集群的主要服务，需先安装并启动。
画面 3: PPT 标题“2.2.3 kube-apiserver 服务”。
画面 4: PPT 标题“2.2.3 kube-apiserver 服务”。
画面 5: PPT 标题“mytomcat.svc.yaml”。
画面 6: PPT 标题“解决 kubelet 问题”，列出解决 kubelet 服务问题的方案。
画面 7: PPT 标题“解决 kubelet 问题”，列出解决 kubelet 问题的方案。
画面 8: PPT 标题“2.5 健康检查与示例测试”。
画面 9: PPT 标题“2.5 健康检查与示例测试”。
画面 10: PPT 标题“2.5 健康检查与示例测试”。
画面 11: PPT 标题“2.5 健康检查与示例测试”。
画面 12: PPT 标题“2.5 健康检查与示例测试”。
画面 13: PPT 标题“2.5 健康检查与示例测试”。
画面 14: PPT 标题“2.5 健康检查与示例测试”。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

