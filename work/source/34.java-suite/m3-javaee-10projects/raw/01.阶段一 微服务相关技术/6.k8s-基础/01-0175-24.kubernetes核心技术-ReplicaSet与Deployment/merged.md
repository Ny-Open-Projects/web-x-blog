# 24.kubernetes核心技术-ReplicaSet与Deployment

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\24.kubernetes核心技术-ReplicaSet与Deployment_【海量资源尽在 ubkz.com】.mp4
- 时长 4分5秒（音频 246s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们介绍一下这个replicateSize这个replicateSize是跟我们的replication它其实是没有本质区别的只是名字不一样那么前期我们已经说过了在这个Kubernetes 1.2以后升级的新概念就是这个replicateSize
[00:18] 那我们知道一下就是说replicate side它呢跟我们那个replication Controller区别主要是它支持集合式的selector也就是说呢我们以前的replication Controller它只是支持这种等式的那Chromalize呢这个官方建议呢避免直接使用replicate side也就是说我们这replicate side不要去直接用那应该和我们的deployment
[00:41] 一起去使用那由于这个replication是replication的一个替代物因此呢它使用上呢是没有什么这个不同地方基本是相同的唯一的区别就是我刚才说的关于我们这个selector它是支持这种集合方式的那这里面呢我们也不用先看我们这个replication怎么定义我们往下看这个关于deployment
[01:04] 那这个Deployment是Kubernetes 1.2以后引入的一个新概念引入的目的就是为了更好地解决我们的Port的编排问题那Deployment的内部使用Replicate来实现那这是也前期说过的那Deployment的定义与Replicate的定义很类似那除了API声明以及这个Key的类型有所不同比如说下面这是一个关于
[01:28] Deployment的一个定义,那我们这个如果想自己去定义一个reput side呢,其实就是这个API server和我们的CAD,其他的呢都是一样的,那大家可以看一下下面这个例子啊,下面这里边呢,我们定义了一个Deployment,那我们可以看,在这里面我们template是指定我们当前的poll的,
[01:48] 那我们引用了我们的标签label我们定义一个label叫app-tel那我们上面这部分是不是spec-selector这部分其实就是干什么去selector去我们当前的这些label那这里面大家看我们当前呢是可以去写成这种集合的方式的那当前这个就是定义了一个deployment那我们也可以看一下当前我们自己的一个deployment
[02:17] 在这里边我们可以cat一下我们的demo4-deployment的yaml文件这就是我们当前的定义的一个简单的当前的我们的一个deployment那我们这里边看预期目标是1然后我们当前使用的这个pod它里边的容器是一个index那我们可以通过kuberctl create去把它创建出来我们这里边可以写上demo4-我的deployment
[02:46] 那我们创建会有问题因为我之前已经创建过了那我们创建过以后我们可以通过get deploy mints去查看我们创建的deployment我们的deployment是这个叫做Nginx deployment我们可以通过kuberctl dsrib rib我们deployment加上我们当前的这个名字
[03:14] 去查看我当前整个deployment的一个详细的信息这里面你就会发现我们这里面是不是有labels看到了吧这也就是我们前期定义的然后我们的selector我们的选择的也是app等于endings那这是说我们创建了一个deployment
[03:34] 那这里啊大家一定要知道就是我们当前这个DipLightment跟我们的RC对比呢其实它就是一个升级那我们在新的版本里面呢建议使用它它呢可以使用我们它内部啊默认使用的是我们这种叫做ReplaySide那这是我们新版本以后推荐使用的它跟我们之前的这种RC呢其实本质的区别没有还是一样的只是它在编排上呢可能会更好一点那这是关于DipLightment

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Kubernetes 中 Deployment 资源的定义、使用方法及其与 ReplicaSet 的关系，并通过命令行演示了 Deployment 的创建和查看。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了文档中“5 Deployment详解”部分，介绍了 Deployment 是 Kubernetes v1.2 引入的新概念，用于解决 Pod 的编排问题，其内部使用 ReplicaSet 实现，并列出了 Deployment 的 API 版本和 Kind 类型。
画面 2: 与画面 1 内容相同，光标在“5 Deployment详解”标题下。
画面 3: 展示了 Deployment 的 YAML 配置文件，其中包含 apiVersion、kind、metadata、spec 等字段，spec 中的 selector 部分被高亮显示。
画面 4: 展示了 Deployment 的 YAML 配置文件，光标位于 spec.template.spec.containers 字段前，准备编辑容器定义。
画面 5: 展示了 Deployment 的 YAML 配置文件，其中 selector 部分被高亮显示。
画面 6: 展示了 Kubernetes 集群的节点状态，包括 Kubernetes-master-demo、Kubernetes-node1-demo、Kubernetes-master-test、Kubernetes-node-test 四个节点。
画面 7: 展示了终端命令行界面，执行了 kubectl create -f demo-deployment.yaml 命令，但因 API 版本不兼容报错，随后执行了 kubectl get deployments 查看部署状态。
画面 8: 展示了终端命令行界面，执行了 kubectl describe deployments Nginx-deployment 命令，查看部署的详细信息。
画面 9: 展示了终端命令行界面，显示了 kubectl describe deployments Nginx-deployment 命令的输出结果，包括 Deployment 的基本信息、策略、状态等。
画面 10: 展示了 Deployment 的 YAML 配置文件，其中 selector 部分被高亮显示。
画面 11: 展示了 Deployment 的 YAML 配置文件，光标位于 spec 字段前。
画面 12: 展示了 Deployment 的 YAML 配置文件，光标位于 spec.template.spec.containers 字段前。
画面 13: 展示了 Deployment 的 YAML 配置文件，光标位于 spec.template.spec.containers 字段前。
画面 14: 展示了文档中“5 Deployment详解”部分，介绍了 Deployment 是 Kubernetes v1.2 引入的新概念，用于解决 Pod 的编排问题，其内部使用 ReplicaSet 实现，并列出了 Deployment 的 API 版本和 Kind 类型。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面 1:
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 1
  selector:
    matchLabels:
      tier: frontend
    matchExpressions:
    - {key: tier, operator: In, values: [frontend]}
  template:
    metadata:
      labels:
        app: app-demo
        tier: frontend
    spec:
      containers:
      - name: Tomcat-demo
        image: Tomcat
        ports:
        - containerPort: 8080

画面 7:
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: Nginx
spec:
  replicas: 1
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
      resources:
        requests:
          cpu: 50m

画面 8:
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: Nginx-deployment
  labels:
    app: Nginx
spec:
  replicas: 1
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

画面 9:
Name: Nginx-deployment
Namespace: default
Selector: app=Nginx
Replicas: 1
Updated: 1
Available: 1
Unavailable: 0
Ready: 1
Pods: 1
Created: Sat, 29 Sep 2018 13:55:12 +0800
Labels: app=Nginx
Annotations: <none>
Status: Running
Strategy: RollingUpdate
MinReadySeconds: 0
RollingUpdate: 1 max unavailable, 1 max surge
Conditions:
  Type: Available
  Status: True
  Reason: MinimumReplicasAvailable
OldReplicasets: <none>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: 标题为“5 Deployment详解”，内容为 Deployment 是 Kubernetes v1.2 引入的新概念，用于解决 Pod 的编排问题，其内部使用 ReplicaSet 实现，并列出了 Deployment 的 API 版本和 Kind 类型。
画面 6: 展示了 Kubernetes 集群的节点状态，包括 Kubernetes-master-demo、Kubernetes-node1-demo、Kubernetes-master-test、Kubernetes-node-test 四个节点。
画面 9: 展示了 kubectl describe deployments Nginx-deployment 命令的输出结果，包括 Deployment 的基本信息、策略、状态等。

5) 不要评价画面美观，不要输出与课程无关的内容。

