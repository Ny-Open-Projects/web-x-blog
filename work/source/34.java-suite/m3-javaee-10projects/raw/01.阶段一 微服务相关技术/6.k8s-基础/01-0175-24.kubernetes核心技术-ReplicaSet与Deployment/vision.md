# 画面线理解：24.kubernetes核心技术-ReplicaSet与Deployment

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\24.kubernetes核心技术-ReplicaSet与Deployment_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:01, 01:26, 01:49, 02:09, 02:14, 02:57, 03:14, 03:32, 03:39, 03:41, 03:57, 03:58, 04:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:51:00

1) 这一组画面整体在讲 Kubernetes 中 Deployment 资源的定义、使用方法及其与 ReplicaSet 的关系，并通过命令行演示了 Deployment 的创建和查看。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了文档中“5 Deployment详解”部分，介绍了 Deployment 是 Kubernetes v1.2 引入的新概念，用于解决 Pod 的编排问题，其内部使用 ReplicaSet 实现，并列出了 Deployment 的 API 版本和 Kind 类型。
画面 2: 与画面 1 内容相同，光标在“5 Deployment详解”标题下。
画面 3: 展示了 Deployment 的 YAML 配置文件，其中包含 apiVersion、kind、metadata、spec 等字段，spec 中的 selector 部分被高亮显示。
画面 4: 展示了 Deployment 的 YAML 配置文件，光标位于 spec.template.spec.containers 字段前，准备编辑容器定义。
画面 5: 展示了 Deployment 的 YAML 配置文件，其中 selector 部分被高亮显示。
画面 6: 展示了 Kubernetes 集群的节点状态，包括 k8s-master-demo、k8s-node1-demo、k8s-master-test、k8s-node-test 四个节点。
画面 7: 展示了终端命令行界面，执行了 kubectl create -f demo-deployment.yaml 命令，但因 API 版本不兼容报错，随后执行了 kubectl get deployments 查看部署状态。
画面 8: 展示了终端命令行界面，执行了 kubectl describe deployments nginx-deployment 命令，查看部署的详细信息。
画面 9: 展示了终端命令行界面，显示了 kubectl describe deployments nginx-deployment 命令的输出结果，包括 Deployment 的基本信息、策略、状态等。
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
      - name: tomcat-demo
        image: tomcat
        ports:
        - containerPort: 8080

画面 7:
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
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
      resources:
        requests:
          cpu: 50m

画面 8:
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 1
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

画面 9:
Name: nginx-deployment
Namespace: default
Selector: app=nginx
Replicas: 1
Updated: 1
Available: 1
Unavailable: 0
Ready: 1
Pods: 1
Created: Sat, 29 Sep 2018 13:55:12 +0800
Labels: app=nginx
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
画面 6: 展示了 Kubernetes 集群的节点状态，包括 k8s-master-demo、k8s-node1-demo、k8s-master-test、k8s-node-test 四个节点。
画面 9: 展示了 kubectl describe deployments nginx-deployment 命令的输出结果，包括 Deployment 的基本信息、策略、状态等。

5) 不要评价画面美观，不要输出与课程无关的内容。
