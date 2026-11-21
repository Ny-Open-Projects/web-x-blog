# 22.kubernetes核心技术-Label

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\22.kubernetes核心技术-Label_【海量资源尽在 ubkz.com】.mp4
- 时长 4分55秒（音频 296s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们介绍一下LabelLabel是Kubernetes系统中另一个核心概念一个Label其实就是一个KV的键值对其中K和Volume是由用户自己去指定的Label可以附加到我们的各种资源上如我们的Node, Pod, Service, RC等等一个资源对象可以定义任意数量的Label同一个Label可以被添加到任意数量的资源对象上
[00:27] Label通常在资源对象定义时确定也可以在对象创建后动态添加或删除那大家看一下Label最常见的用法呢是通过Metadata Label字段来给对象添加Label然后呢我们通过一个SPC.Selector来引用对象下面呢就是我们的一个例子在这里边我们当前定义的其实是一个Replication也就是我们当前的一个RC那在这里边我们可以看到这部分
[00:56] template这一部分其实就是相当于我们去定义一个pod那我们前期介绍过一个pod的定义而我们在实际操作中其实很少单独定义pod那都会是在我们的rc里面去定义那这部分就相当于是说我们定义了一个pod那现在在这里边就是我们有一个叫做labels然后app然后我们的
[01:22] Nginx也就是说我们在这里面Metadata Labels在这部分其实我们就定义了一个Label它的Key就是App它的Volume就是Nginx而我们在这里面看到SPEC Selector也就是说我们在这里面看到的SPEC Selector还有下面我们这个Service里面我的SPEC这Selector这部分都是相当于我们再去引用我们刚才定义的Label
[01:50] 那这个label我们到底干什么用呢大家可以看一下label呢是附加到我们Colonize集群中的各种资源对象上那目的呢就是对这些资源对象啊进行一个分组管理而分组管理的核心就是我们的label selector也就是说我们在这里面是说我
[02:09] 定义了当前的一个label而我们可以通过label select去引用它那也就是说我们可以去把它进行一个方便的管理那label和我们当前的label select都是不能单独使用的它的必须是在一些我们的资源对象的定义文件上去附加那一般是在RC或者是Service中定义那大家看到的我们这个例子其实就是在我们当前的RC也是我们的reboot
[02:38] replication Controller和我们的Service里面去引用了我们之前定义的我们的label那我们定义label的目的呢其实就是把我们的资源进行一个方便的一个分组管理那我们也可以看一下在这里边我们可以看一下我们当前的demo3.yaml文件在这我们是定义了我们当前的一个label
[03:05] Matters Label 这里面有App,AppDemo那我们这里边是定义了两组Label然后我们在这里再看一下有一个Selector SPC Selector那我们这里边是把它去进行了一个引用那我们可以来看一下我Pose我现在去获取一下我们当前的Pose这里边有一个叫这么的一个名字这是我创建的我们可以把它先
[03:37] Delet delete掉这是我们刚才那个Demo 3.yaml文件我把它删除掉删除掉以后呢大家再来看一下get pose那我现在这个已经没有了那我们可以把它去创建一下create-f我们Demo 3.yaml那我们现在创建成功我们可以通过dscrib describe然后-f我们看一下Demo 3.yaml
[04:07] 这个时候我们可以看到当前我这里边有一个label这就是我们定义的一个标签我们在整个这里边是把它先定义出来了后续我们在这里就可以通过我们刚才说的SPC selector去把它引用出来OK这是对我们的label做了一个简单的介绍那么大家知道一下我们label它存在的意义其实就是用来进行什么
[04:36] 资源管理的而我们label它是不能单独去定义label select也是一样的那我们必须干什么在我们的这些资源上去定义它比如说附加到我们当前的某些资源上那一般是在我们的replication Controller或者是我的Service中

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Kubernetes 中 Label 的概念、用法及其与 Replication Controller 的关联。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Label 概念介绍，重点是通过 metadata.labels 添加 Label，通过 spec.selector 引用对象。展示 ReplicationController 的 YAML 配置片段，包含 metadata.name、spec.replicas、spec.selector、template.metadata.labels、spec.containers 等字段。
画面2: 展示 ReplicationController 的 YAML 配置，光标在 spec.selector 下方，显示 app: Nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面3: 展示 ReplicationController 的 YAML 配置，光标在 spec.template.metadata.labels 下方，显示 app: Nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面4: 展示 ReplicationController 的 YAML 配置，光标在 spec.selector 下方，显示 app: Nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面5: 展示 Service 的 YAML 配置片段，光标在 spec.selector 下方，显示 app: Nginx。下方文字说明 Label 与 Label Selector 不能单独定义，必须附加在 RC 或 Service 的资源定义文件中。
画面6: 展示 Service 的 YAML 配置片段，光标在 spec.selector 下方，显示 app: Nginx。下方文字说明 Label 与 Label Selector 不能单独定义，必须附加在 RC 或 Service 的资源定义文件中。
画面7: 展示 Replication Controller 详解章节标题，下方文字说明 RC 是 Kubernetes 核心概念之一，定义 RC 后，Master 节点的 Controller Manager 会定期检查 Pod 数量，若不足则创建 Pod，若过多则删除 Pod。
画面8: 展示 Label 概念介绍，重点是通过 metadata.labels 添加 Label，通过 spec.selector 引用对象。展示 ReplicationController 的 YAML 配置片段，包含 metadata.name、spec.replicas、spec.selector、template.metadata.labels、spec.containers 等字段。
画面9: 展示 ReplicationController 的 YAML 配置片段，光标在 spec.template.metadata.labels 下方，显示 app: Nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面10: 展示 Replication Controller 详解章节标题，下方文字说明 RC 是 Kubernetes 核心概念之一，定义 RC 后，Master 节点的 Controller Manager 会定期检查 Pod 数量，若不足则创建 Pod，若过多则删除 Pod。下方显示命令：kubect1 scale rc Nginx --replicas=5。
画面11: 展示 SecureCRT 的 SSH 会话窗口，提示符为 [root@localhost test]#，未输入任何命令。
画面12: 展示 Replication Controller 详解章节标题，下方文字说明 RC 是 Kubernetes 核心概念之一，定义 RC 后，Master 节点的 Controller Manager 会定期检查 Pod 数量，若不足则创建 Pod，若过多则删除 Pod。
画面13: 展示 Label 概念介绍，重点是通过 metadata.labels 添加 Label，通过 spec.selector 引用对象。展示 ReplicationController 的 YAML 配置片段，包含 metadata.name、spec.replicas、spec.selector、template.metadata.labels、spec.containers 等字段。
画面14: 展示 Service 的 YAML 配置片段，光标在 spec.selector 下方，显示 app: Nginx。下方文字说明 Label 与 Label Selector 不能单独定义，必须附加在 RC 或 Service 的资源定义文件中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
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
---
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

画面2:
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
---
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

画面3:
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
---
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

画面4:
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
---
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

画面5:
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

画面6:
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

画面7:
kubect1 scale rc Nginx --replicas=5

画面8:
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
---
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

画面9:
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
---
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

画面10:
kubect1 scale rc Nginx --replicas=5

画面13:
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
---
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

画面14:
apiVersion: v1
kind: Service
metadata:
  name: Nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector

