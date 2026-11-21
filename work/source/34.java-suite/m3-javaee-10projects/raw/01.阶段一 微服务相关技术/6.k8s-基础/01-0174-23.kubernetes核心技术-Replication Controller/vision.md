# 画面线理解：23.kubernetes核心技术-Replication Controller

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\23.kubernetes核心技术-Replication Controller_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:30, 00:36, 01:03, 01:20, 01:30, 01:48, 01:57, 02:06, 02:50, 03:18, 03:30, 04:54, 05:07, 05:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:50:23

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Replication Controller、Replica Set 和 Deployment 的概念、区别与使用方法，通过命令行演示如何创建、查看和调整副本数量。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Replication Controller 的 YAML 配置文件，其中包含 metadata、spec（replicas、selector、template）等字段，以及一个示例命令 `kubectl scale rc nginx --replicas=5`。
画面 2: 与画面 1 内容相同，为同一页面的截图。
画面 3: 展示了终端窗口中执行 `kubectl get pods` 命令后，显示了多个 Pod 的状态，包括 `busybox`、`myweb`、`nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 4: 与画面 3 内容相同，为同一终端窗口的截图。
画面 5: 展示了终端窗口中执行 `kubectl get pods` 命令后，显示了多个 Pod 的状态，包括 `busybox`、`myweb`、`nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 6: 展示了终端窗口中执行 `kubectl scale rc nginx --replicas=5` 命令，用于调整 Replication Controller 的副本数量。
画面 7: 展示了终端窗口中执行 `kubectl scale rc nginx --replicas=5` 命令后，再次执行 `kubectl get pods` 命令，显示了 Pod 的状态，包括 `busybox`、`myweb`、`nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 8: 展示了文档中“4 Replica Set详解”和“5 Deployment详解”两个章节的标题，以及 Deployment 的 YAML 配置文件开头部分。
画面 9: 与画面 8 内容相同，为同一页面的截图。
画面 10: 展示了 Service 的 YAML 配置文件，其中包含 metadata、spec（type、ports、selector）等字段。
画面 11: 展示了 Service 的 YAML 配置文件中 `ports` 字段的详细内容，包括 `containerPort: 80`。
画面 12: 展示了 Service 的 YAML 配置文件中 `selector` 字段的内容，包括 `app: nginx`。
画面 13: 展示了终端窗口中执行 `kubectl scale rc nginx --replicas=5` 命令后，再次执行 `kubectl get pods` 命令，显示了 Pod 的状态，包括 `busybox`、`myweb`、`nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 14: 展示了 Service 的 YAML 配置文件中 `ports` 字段的详细内容，包括 `nodePort: 3333`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
type: NodePort
ports:
  - port: 80
    nodePort: 3333
selector:
  app: nginx
```
画面 3:
```yaml
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
```
画面 4:
```yaml
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
```
画面 6:
```bash
kubectl scale rc nginx --replicas=5
```
画面 8:
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
```
画面 10:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
  - port: 80
    nodePort: 3333
  selector:
    app: nginx
```
画面 11:
```yaml
ports:
  - containerPort: 80
```
画面 12:
```yaml
app: nginx
```
画面 13:
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 5
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
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: PPT 标题为“4 Replica Set详解”和“5 Deployment详解”。
画面 13: PPT 标题为“4 Replica Set详解”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
