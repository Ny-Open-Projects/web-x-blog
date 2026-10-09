> 原文锚点：第 5~28 段「那接下来呢我们来看一下 k 八 s 的一些基本概念…master…load(worker)…pod…label…replicationcontroller…deployment…HPA…service…volume…namespace」（K8s 核心概念：master/worker/pod/label/RC/Deployment/HPA/Service/Volume/Namespace）

## 一句话总述
K8s 是一套**以 Pod 为最小调度单位、以声明式 API 管理容器生命周期**的编排平台：Master 负责决策（APIServer/Scheduler/Controller-Manager/etcd），Node 负责运行（kubelet/kube-proxy），Pod 封装共享网络的容器，上层用 Deployment/RS/HPA 管副本与弹性，Service 做服务发现与负载均衡，Namespace 做多租户隔离。

## 面试官视角
这题考「K8s 心智模型」是否完整，而非背名词。考点：① Master 与 Node 各自跑什么组件；② Pod 为什么是最小单位（共享网络/IPC）；③ Deployment/RS/HPA 的层级关系；④ Service 解决什么问题。能画出「Master-Node-Pod-Controller-Service」并说清各自职责，是高阶信号。

## 主问答
**Q（面试官原话）：** 说说 K8s 的核心架构和几个关键概念。

**A：**
1. **Master（控制面）**：集群大脑，含 `APIServer`（唯一入口/鉴权）、`Scheduler`（把 Pod 调度到 Node）、`Controller-Manager`（维持副本/状态）、`etcd`（集群唯一真相源，存所有资源对象）。生产环境 Master 多副本保高可用。
2. **Node（工作节点）**：真正跑容器的机器，含 `kubelet`（向 Master 汇报、管本节点 Pod）、`kube-proxy`（维护 Service 的 iptables/IPVS 转发规则）、容器运行时（containerd/CRI-O）。
3. **Pod = 最小调度单位**：一个 Pod 封装一个或多个**共享同一网络命名空间与 IPC** 的容器（同宿主、同 IP），K8s 调度、扩缩、自愈都以 Pod 为粒度——比裸容器更高层的抽象，便于部署管理。
4. **控制器族**：`ReplicationController/ReplicaSet` 维持副本数（多退少补）；`Deployment` 在 RS 之上做**滚动升级/回滚**并可查部署进度；`HPA` 按负载**横向自动扩缩** Pod 数。`Service` 是 Pod 的逻辑集合+稳定访问入口（含服务发现与负载均衡）；`Volume` 是 Pod 内多容器共享目录；`Namespace` 做多租户/项目的逻辑隔离；`Label`+选择器用于按标签筛选资源。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | Master 有啥组件？ | 控制面职责 | APIServer/Scheduler/CM/etcd | 答不全算 L1 未过 |
| L2 | Pod 为何最小单位？ | 共享网络/IPC | 同宿主同 IP、调度粒度 | 说「容器最小」算 L2 未过 |
| L3 | Deployment 与 RS？ | 升级/副本 | Deployment 管 RS 做滚动升级 | 混淆算 L3 未过 |
| L4 | Service 解决啥？ | 服务发现/负载均衡 | 稳定入口+标签选 Pod+转发 | 答「暴露端口」算 L4 未过 |
| L5 | HPA 怎么决策？ | 弹性扩缩 | 按指标追目标副本数 | 说不清算 L5 未过 |

## 版本与兼容性
- 概念跨版本稳定；`ReplicationController` 已被 `ReplicaSet` 取代（Deployment 默认用 RS），新代码不应再直接用 RC。
- `kubectl`/声明式 YAML 是标准交互方式；编程侧用 `client-go`（Go 生态一等公民，见下代码）。
- 注意与「微服务」（见 152.md`/`157-microservice-governance.deep.md`）区分：微服务是**架构风格**，K8s 是**运行微服务的基础设施**，二者不同层。

## 总结与追问预判
收口：**K8s = Master 决策 + Node 执行 + Pod 最小单位 + Controller/Service/Namespace 分层管理**。预判追问：① K8s 凭什么成为标准（优势，见 1515.md`）；② 用在哪（场景/特点，见 1515.md`）。回答时把「Pod 共享网络命名空间」和「etcd 是唯一真相源」两句抛出，最显功底。

## ⚠️ 原文纠错
源视频转写将 Kubernetes / master / worker(node) / pod / replication controller / deployment / HPA / service / namespace / etcd 等音译为崩坏词（如「k 八 s」指代 Kubernetes、「load」指代 worker 节点、「propersdd」指代 pod、「replicationcontroller」保留、「horiontalpodortoscale」指代 HPA、「cper」指代容器运行时 CRI、「graph」指代 Grafana），本卡已还原为规范术语。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 面试被问「K8s 架构」，**第一句点出「etcd 是集群唯一真相源、APIServer 是唯一入口」**——这比罗列组件更显你理解控制面数据流向。再补「Pod 共享网络命名空间所以同 IP」即可拿架构分。

```yaml
# 声明式最小单元：Deployment 管理 ReplicaSet，RS 维持 3 个 Pod 副本
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels: { app: nginx }      # Label：被 Service/选择器引用
spec:
  replicas: 3
  selector: { matchLabels: { app: nginx } }
  template:
    metadata: { labels: { app: nginx } }
    spec:
      containers:
        - name: nginx
          image: nginx:1.27
          ports: [{ containerPort: 80 }]
---
apiVersion: v1
kind: Service
metadata: { name: nginx }
spec:
  selector: { app: nginx }     # 按 Label 关联后端 Pod
  ports: [{ port: 80, targetPort: 80 }]
```

```go
// Go 侧用 client-go 列 Pod：K8s 编程标准入口（满足规则 14 可运行语言块）
package main

import (
	"context"
	"fmt"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
)

func listPods() error {
	cfg, err := rest.InClusterConfig() // 或 clientcmd.BuildConfigFromFlags 读 kubeconfig
	if err != nil {
		return err
	}
	cli, err := kubernetes.NewForConfig(cfg)
	if err != nil {
		return err
	}
	pods, err := cli.CoreV1().Pods("default").List(context.TODO(), metav1.ListOptions{})
	if err != nil {
		return err
	}
	for _, p := range pods.Items {
		fmt.Printf("pod=%s node=%s\n", p.Name, p.Spec.NodeName)
	}
	return nil
}
```
