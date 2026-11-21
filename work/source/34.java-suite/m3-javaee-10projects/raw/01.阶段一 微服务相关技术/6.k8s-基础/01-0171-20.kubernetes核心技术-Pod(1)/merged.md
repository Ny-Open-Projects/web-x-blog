# 20.kubernetes核心技术-Pod(1)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\20.kubernetes核心技术-Pod(1)_【海量资源尽在 ubkz.com】.mp4
- 时长 7分55秒（音频 475s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 下面我们介绍容器化进阶课程Kubernetes的一些核心技术首先第一个我们介绍一下PodPod是Kubernetes一个重要的概念每一个Pod都有一个特殊的被称为根容器的Pos容器Pos容器对应的镜像属于Kubernetes平台的一部分除了Pos容器以外我们每个Pod还有一个或多个紧密相关的用户的业务容器
[00:27] 那么例如这个图那我们一个POD它有一个跟容器POS它里面还有一些其他的跟我们的用户的业务相关联的一些user的containers也就是说可以有一个或多个那这是一个单独的POS的图大家可以再往下看一下这是POD在我们整个的Chromalize机群里面的一个图那我们每个POD在我们的node上那一个POD里面可以有多个container
[00:57] 那对于我们这个Pod来说它跟应用有什么区别呢大家可以看一下说每个Pod都是应用的一个实例有专用的IP那么还有一个是Pod和容器那Pod和容器是什么关系一个Pod可以包含多个容器也说我们一个Pod里面可以有多个container那么彼此之间共享网络和存储资源每个Pod中有一个Pos容器
[01:23] 它是用来保存所有的容器状态我们是通过管理这Pos容器达到管理我们Pos中所有容器的效果也就是说我们是通过管理Pos中的Pos这个容器以便去帮助我们管理所有的我们的Pos那Pos跟节点有什么区别呢大家可以看一下
[01:44] 那同一个Pod中的容器总会被调到相应的Node节点也就是说我们一个Pod会分配在我们某一些Node上那不同的节点间Pod的通信是基于一个虚拟的二层网络技术那Pod和Pod之间也是有区别的我们的Pod其实分成两种一种是普通的Pod还有一个是静态的Pod后续我们会介绍普通Pod和静态Pod
[02:12] 那对于一个pod来说我们如何去定义它呢大家下面看到的这部分就是我们定义一个pod通过yaml文件这种方式的一个完整的内容那我们可以给它一个API version它的版本然后我们告诉它当前的类型是一个
[02:29] POD,那我们可以定义一些它的语言数据,例如我们当前的名字,POD的名字它的Namespace,命名空间还有它的一些标签那么Namespace和Labels下面,这后续的课程中我们都会讲那再往下呢,这是关于POD中容器的详细定义也说SPC,我们是用来定义我们POD中的容器那这是Container,然后我们下面这个容器的名称这个容器的
[02:56] 镜像那下面这些还有我们容器中一些命令行的启动下面这些内容啊很多我们就不过多的一一列举大家呢可以回头自己去看一下后续当你看到一个破译定义时
[03:11] 某些信息你不是特别清楚你可以去在这个文档里面去查看一下具体每一个都代表什么意思例如说我们这是一个Post很明显那这是我们的接口对吧那这是我的名字然后ContainerPost就是我们容器要暴露的接口HousePost是我们容器所在主机监听的接口还有呢往下面这些关于我们的Resources这是我们具体的资源的分配的情况OK
[03:39] 这是关于我们如何去定义一个pod对于一个pod来说我们现在已经知道怎么定义了我们去如何使用它呢看一下在空中对运行容器的要求为容器的主程序需要一直在前台运行而不是在后台我们应用需要改造成前台运行的方式如果我们创建的Docker镜像启动命令是后台执行程序
[04:08] 那则在Corelight创建包含这个容器的POD之后运行该命令即认为POD已经结束将立即销毁该POD如果为该POD定义了RC那就是Replication Controller则创建销毁会陷入一个无限循环的过程所以这里面告诉你我们容器它的主进程应该一直是在全台运行的
[04:32] 那对于我们POD来说我们在使用的时候大家可以看一下POD可以由一个或多个容器组合而成也就是说在POD里边你可以有多个容器也可以只有一个那你现在看到的这个例子就是一个容器组成的一个POD那这是我们的一个MyTamkite然后呢我们对外暴露的是8000端口那我们可以看一下当前我们这个
[04:58] CD-user下的local我们有一个Kubernetes目录在这里边我们进入test目录下我们可以cat一下demo1.yaml文件这个文件里边我们就定义了一个我的mytomcat当前我们看一下Kuberctl get pose我看我启动它我们这里边已经有了mytomcat你可以通过Kuberctl
[05:28] ctl replace我们当前的这个文件demo1.yaml你可以去重新把它它不让我去操作是吧那这么办cubectl我们delete掉大F demo1.yaml先把它删掉然后呢我再去重新create一份当前的demo1.yaml我重新把它创建出来这个时候我们再
[06:00] 你看一下我们当前这个MyTimeCat它现在是一个container creating那稍等一会儿呢它就应该是能帮助我们把它创建成功OK啊我这里边可能还是没有创建成功稍等一下也就是说我们现在呢可以是在我当前的一个pod里边只有一个容器而我们也可以是在
[06:26] 一个POD里有多个容器那这个容器呢这些容器呢是几米有格的下面大家看到的这个例子就是我们有两个为几米有格的容器组成的POD那这里边呢是我们创建一个POD那它叫做MyWeb我们这里边呢有两个容器一个是我们当前的Tomcat还有一个是我的RedisTomcat呢对外暴露的是8000段口我们的这个当前的这个
[06:54] Redis是6379那我们可以看一下在这里我们应该可以看一下的是Demo2的这个压模文件这个文件里边就是我当前两个紧密偶合的容器在一个POD里边我们也可以把它这个创建一下我看有没有这个myweb没有对吧OKHuber create-f
[07:26] 然后呢我们把这个Demo2这个创建一下OK这个时候呢我们就已经把它创建了应该写错了Cover CTL Get Pose那这里边我们就有这个MyWeb了那好这是说呀我们当前呢可以去在一个Post里有一个容器或者是一个Post里边有多个容器

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Pod 的核心概念、定义、基本用法及实际操作演示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程标题“容器化进阶Kubernetes核心技术”，并列出目录结构，当前章节为“1 Pod详解”。图示说明一个 Pod 包含 Pause 容器和用户容器。
画面 2: 展示“Pod vs 应用”、“Pod vs 容器”、“Pod vs 节点”等对比要点。图示展示两个节点上的 Pod 及其内部容器，标注了 Labels 和 Service。
画面 3: 展示“1.1 Pod的定义”标题，下方文字说明“下面为yaml定义文件的Pod的完整内容”。
画面 4: 展示 YAML 文件中 Pod 的 metadata 和 spec 部分，包含 containers、image、ports、volumes 等字段的定义。
画面 5: 展示 YAML 文件中 Pod 的 memory、livenessProbe、exec、httpGet、tcpSocket、initialDelaySeconds、periodSeconds、successThreshold、failureThreshold、securityContext、privileged、restartPolicy、nodeSelector、imagePullSecrets、hostNetwork、volumes、emptyDir 等字段的定义。
画面 6: 展示 YAML 文件中 Pod 的 volumes、ports、env、resources、limits 等字段的定义。
画面 7: 展示“1.2 Pod的基本用法”标题，说明 Pod 可以由一个或多个容器组成，并给出“由一个容器组成的Pod示例”和“由两个容器组成的Pod示例”的 YAML 代码。
画面 8: 展示终端命令行，用户在目录中列出文件，查看并编辑名为“demo1.yaml”的文件。
画面 9: 展示终端命令行，用户执行“kubectl get pods”查看 Pod 状态，然后执行“kubectl replace -f demo1.yaml”更新 Pod，接着执行“kubectl delete -f demo1.yaml”删除 Pod。
画面 10: 展示终端命令行，用户执行“kubectl get pods”查看 Pod 状态，然后执行“kubectl get pods -o wide”查看详细信息，接着执行“kubectl describe pod/<Pod_name>”查看 Pod 详细描述。
画面 11: 展示“由两个容器组成的Pod示例”的 YAML 代码，包含两个容器（Tomcat 和 redis）及其端口配置。
画面 12: 展示终端命令行，用户执行“kubectl create -f xxx.yaml”创建 Pod。
画面 13: 展示“由两个容器组成的Pod示例”的 YAML 代码，包含两个容器（Tomcat 和 redis）及其端口配置。
画面 14: 展示“由两个容器组成的Pod示例”的 YAML 代码，包含两个容器（Tomcat 和 redis）及其端口配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```yaml
metadata:
  # 元数据
  name: string
  namespace: string
  # 元数据，pod的命名空间
  labels:
    - name: string
    # 元数据，标签列表
    - name: string
    # 元数据，自定义注释
  annotations:
    - name: string
    # 元数据，自定义注释
spec:
  containers:
    - name: string
    # pod中的容器列表，可以有多个容器
    - name: string
    # 容器的名称
    image: string
    # 容器的镜像
    imagePullPolicy: [Always|Never|IfNotPresent]//获取镜像的策略，默认为Always，每次都会尝试重新下载
    command: [string]
    # 容器的启动命令列表（不配置的话使用镜像内的命令）
    args: [string]
    # 启动参数列表
    workingDir: string
    # 容器的工作目录
    volumes: []
    # 指定容器内部的存储卷设置
    ports:
      - name: string
      # 容器需要暴露的端口名列表
      - name: string
      # 容器需要暴露的端口名
      containerPort: int
      # 容器需要暴露的端口
      hostPort: int
      # 容器在主机监听的端口（容器暴露端口映射到宿主机的端口。设置hostPort时同一台宿主机将不能启动其它容器的端口）
      protocol: string
      # TCP和UDP，默认为TCP
      env:
        - name: string
        # 环境变量的名称
        value: string
        # 环境变量的值
```

画面 5:
```yaml
memory: string
# pod内存资源的设置
livenessProbe:
  exec:
    # exec方式需要执行的命令/脚本
    command: [string]
    # exec方式需要执行的命令/脚本
  httpGet:
    # 通过httpGet检查健康
    port: string
    # 端口
    host: string
    # 主机
    scheme: string
    # 协议
    httpHeaders:
      - name: string
      # http头名称
      value: string
      # http头值
  tcpSocket:
    # 通过tcpSocket检查健康
    port: string
    # 端口
  initialDelaySeconds: 0
  # 首次检查时间
  periodSeconds: 0
  # 检查间隔时间
  successThreshold: 0
  # 成功阈值
  failureThreshold: 0
  # 失败阈值
  securityContext:
    # 安全配置
    privileged: false
    # 是否允许特权模式
  restartPolicy: Always|Never|OnFailure
  # 重启策略，默认为Always
  nodeSelector: object
  # 节点选择器，表示将该Pod调度到指定的节点上，key:value格式描述
  imagePullSecrets:
    - name: string
    # 镜像拉取密钥
  hostNetwork: false
  # 是否使用主机网络模式，共用Docker网络，默认否
  volumes:
    - name: string
    # 在Pod上定义的共享存储卷
    emptyDir: {}
    # 是一种与生命周期相关的存储卷，是一个临时目录，内容为空
```

画面 6:
```yaml
volumes:
  - name: string
  # 存储卷的名称
  emptyDir: {}
  # 是一种与生命周期相关的存储卷，是一个临时目录，内容为空
ports:
  - name: string
  # 容器需要暴露的端口名
  containerPort: int
  # 容器需要暴露的端口
  hostPort: int
  # 容器在主机监听的端口（容器暴露端口映射到宿主机的端口。设置hostPort时同一台宿主机将不能启动其它容器的端口）
  protocol: string
  # TCP和UDP，默认为TCP
env:
  - name: string
  # 环境变量的名称
  value: string
  # 环境变量的值
resources:
  limits:
    cpu: string
    # 资源限制，容器的最大可用资源数量
    memory: string
    # 资源限制，容器的最大可用资源数量
  requests:
    cpu: string
    # 资源请求，容器启动时可使用的资源数量
    memory: string
    # 资源请求，容器启动时可使用的资源数量
livenessProbe:
  exec:
    # exec方式需要执行的命令/脚本
    command: [string]
    # exec方式需要执行的命令/脚本
```

画面 7:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: Tomcat
      ports:
        - containerPort: 8000
```

画面 8:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: Tomcat
      ports:
        - containerPort: 8000
```

画面 9:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: Tomcat
      ports:
        - containerPort: 8000
```

画面 10:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: Tomcat
      ports:
        - containerPort: 8000
```

画面

