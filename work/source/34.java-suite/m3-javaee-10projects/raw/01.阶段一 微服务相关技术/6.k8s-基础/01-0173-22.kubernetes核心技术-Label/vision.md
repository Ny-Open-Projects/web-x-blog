# 画面线理解：22.kubernetes核心技术-Label

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\22.kubernetes核心技术-Label_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:47, 01:13, 01:39, 01:45, 01:51, 02:16, 02:33, 02:40, 02:48, 02:55, 04:27, 04:32, 04:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:49:45

1) 这一组画面整体在讲 Kubernetes 中 Label 的概念、用法及其与 Replication Controller 的关联。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Label 概念介绍，重点是通过 metadata.labels 添加 Label，通过 spec.selector 引用对象。展示 ReplicationController 的 YAML 配置片段，包含 metadata.name、spec.replicas、spec.selector、template.metadata.labels、spec.containers 等字段。
画面2: 展示 ReplicationController 的 YAML 配置，光标在 spec.selector 下方，显示 app: nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面3: 展示 ReplicationController 的 YAML 配置，光标在 spec.template.metadata.labels 下方，显示 app: nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面4: 展示 ReplicationController 的 YAML 配置，光标在 spec.selector 下方，显示 app: nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面5: 展示 Service 的 YAML 配置片段，光标在 spec.selector 下方，显示 app: nginx。下方文字说明 Label 与 Label Selector 不能单独定义，必须附加在 RC 或 Service 的资源定义文件中。
画面6: 展示 Service 的 YAML 配置片段，光标在 spec.selector 下方，显示 app: nginx。下方文字说明 Label 与 Label Selector 不能单独定义，必须附加在 RC 或 Service 的资源定义文件中。
画面7: 展示 Replication Controller 详解章节标题，下方文字说明 RC 是 Kubernetes 核心概念之一，定义 RC 后，Master 节点的 Controller Manager 会定期检查 Pod 数量，若不足则创建 Pod，若过多则删除 Pod。
画面8: 展示 Label 概念介绍，重点是通过 metadata.labels 添加 Label，通过 spec.selector 引用对象。展示 ReplicationController 的 YAML 配置片段，包含 metadata.name、spec.replicas、spec.selector、template.metadata.labels、spec.containers 等字段。
画面9: 展示 ReplicationController 的 YAML 配置片段，光标在 spec.template.metadata.labels 下方，显示 app: nginx。下方展示 Service 的 YAML 配置片段，包含 apiVersion、kind、metadata.name、spec.type、spec.ports、spec.selector。
画面10: 展示 Replication Controller 详解章节标题，下方文字说明 RC 是 Kubernetes 核心概念之一，定义 RC 后，Master 节点的 Controller Manager 会定期检查 Pod 数量，若不足则创建 Pod，若过多则删除 Pod。下方显示命令：kubect1 scale rc nginx --replicas=5。
画面11: 展示 SecureCRT 的 SSH 会话窗口，提示符为 [root@localhost test]#，未输入任何命令。
画面12: 展示 Replication Controller 详解章节标题，下方文字说明 RC 是 Kubernetes 核心概念之一，定义 RC 后，Master 节点的 Controller Manager 会定期检查 Pod 数量，若不足则创建 Pod，若过多则删除 Pod。
画面13: 展示 Label 概念介绍，重点是通过 metadata.labels 添加 Label，通过 spec.selector 引用对象。展示 ReplicationController 的 YAML 配置片段，包含 metadata.name、spec.replicas、spec.selector、template.metadata.labels、spec.containers 等字段。
画面14: 展示 Service 的 YAML 配置片段，光标在 spec.selector 下方，显示 app: nginx。下方文字说明 Label 与 Label Selector 不能单独定义，必须附加在 RC 或 Service 的资源定义文件中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面2:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面3:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面4:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面5:
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面6:
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面7:
kubect1 scale rc nginx --replicas=5

画面8:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面9:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面10:
kubect1 scale rc nginx --replicas=5

画面13:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector:
    app: nginx

画面14:
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 33333
  selector
