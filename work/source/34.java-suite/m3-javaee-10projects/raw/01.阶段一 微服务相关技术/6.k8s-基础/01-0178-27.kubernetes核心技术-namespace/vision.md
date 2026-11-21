# 画面线理解：27.kubernetes核心技术-namespace

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\27.kubernetes核心技术-namespace_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:39, 00:55, 01:03, 01:19, 01:20, 01:37, 01:38, 02:02, 02:13, 02:30, 02:39, 02:41, 02:43, 03:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:53:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Kubernetes 中使用 Namespace 来隔离资源，并通过 YAML 文件创建和查看 Namespace 中的 Pod。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在终端执行 `docker search testwebserver` 命令，搜索 Docker Hub 上的镜像，结果包含多个与 webserver 相关的镜像。提示信息显示因私有仓库证书问题导致连接被拒绝。
画面2：在终端执行 `kubectl get pods` 命令，列出当前命名空间下的所有 Pod，显示多个 Pod 正在运行或创建中。
画面3：在 Typora 中打开《容器化进阶Kubernetes核心技术》文档，显示第8章“Namespace详解”内容，其中包含创建 Namespace 和 Pod 的 YAML 配置示例。
画面4：在 Typora 文档中，高亮显示了 YAML 配置文件中的 `kind: Pod` 部分，下方显示了 `kubectl get pods --namespace=development` 命令。
画面5：在 Typora 文档中，光标位于 `kubectl get pods --namespace=development` 命令行上，准备执行。
画面6：在终端执行 `kubectl get pods` 命令，显示了多个 Pod 的状态，包括 `Running` 和 `ContainerCreating`。
画面7：终端界面为空，等待输入命令。
画面8：在终端执行 `cat demo-namespace.yaml` 命令，显示了创建 Namespace 的 YAML 文件内容。
画面9：在终端执行 `cat demo-pod.yaml` 命令，显示了创建 Pod 的 YAML 文件内容。
画面10：在终端执行 `kubectl get pods` 命令，显示了所有 Pod 的状态。
画面11：在 Typora 文档中，光标位于“9 Service 详解”章节的开头，准备讲解 Service 的概念。
画面12：在 Typora 文档中，光标位于“9 Service 详解”章节的开头，准备讲解 Service 的概念。
画面13：在 Typora 文档中，光标位于“8. Namespace详解”章节的开头，准备讲解 Namespace 的概念。
画面14：在 Typora 文档中，光标位于“8. Namespace详解”章节的开头，准备讲解 Namespace 的概念。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: development
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

画面4：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

画面8：
```yaml
apiVersion: v1
kind: namespace
metadata:
  name: development
```

画面9：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

画面10：
```yaml
apiVersion: v1
kind: namespace
metadata:
  name: development
```

画面11：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：PPT标题为“8. Namespace详解”，内容包括 Namespace 的定义、创建和查看命令。
画面4：PPT标题为“8. Namespace详解”，内容包括 Namespace 的创建和查看命令。
画面5：PPT标题为“8. Namespace详解”，内容包括 Namespace 的创建和查看命令。
画面11：PPT标题为“9 Service 详解”，内容包括 Service 的定义和基本用法。
画面12：PPT标题为“9 Service 详解”，内容包括 Service 的定义和基本用法。
画面13：PPT标题为“8. Namespace详解”，内容包括 Namespace 的定义和创建命令。
画面14：PPT标题为“8. Namespace详解”，内容包括 Namespace 的定义和创建命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
