> 原文锚点：第 29~39 段「那 k 八 s 的优势…自动化…高可用…自动扩展…自动恢复…负载均衡…社区活跃并且生态系统比较完善（普罗米修斯/Prometheus、graph/Grafana）」（六大优势：自动化/高可用/弹性扩缩/自愈/负载均衡/生态）

## 一句话总述
K8s 的核心优势可归为六点：**自动化**（部署/重启/复制/伸缩）、**高可用**（多副本+自愈）、**弹性扩缩**（HPA 按负载自动调副本）、**自动恢复**（副本机制减少单点）、**内置负载均衡**（Service 分发流量）、**生态完善**（Prometheus/Grafana 等）。

## 面试官视角
这题考「为什么选 K8s」而非背清单。考点：① 六优势能否系统归类（自动化/可用/弹性/生态）；② 每个优势背后的**机制**（如高可用靠副本+自愈，弹性靠 HPA）；③ 能否对比「裸容器/脚本部署」凸显价值。能讲清机制而非名词，是加分点。

## 主问答
**Q（面试官原话）：** K8s 相比直接跑容器有什么优势？

**A：**
1. **自动化运维**：声明式 YAML 描述期望状态，K8s 自动完成部署、滚动升级、回滚、重启——人不再手敲 `docker run`/脚本，Git 即基础设施。
2. **高可用 + 自动恢复**：`ReplicaSet` 维持指定副本数，Pod 挂了控制器立刻拉起新副本，**单点故障影响被副本稀释**；配合多 Master 实现控制面高可用。
3. **弹性扩缩**：`HPA` 实时追踪 CPU/内存/自定义指标，自动增减 Pod 副本，应对流量峰谷——无需人工干预，提升资源利用率与可用性。
4. **内置负载均衡与服务发现**：`Service` 给一组同 Label 的 Pod 提供**稳定虚拟 IP + 自动转发**，kube-proxy 维护转发规则，调用方无需感知后端 Pod 变化。
5. **故障自愈与滚动升级**： readiness/liveness 探针检测异常，自动重启或剔除；滚动升级逐个替换副本，业务不中断。
6. **生态完善**：Prometheus（监控）、Grafana（可视化）、Istio（服务网格）等开箱集成，社区活跃、事实标准。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 列几个优势？ | 系统归类 | 自动化/高可用/弹性/生态 | 零散背算 L1 未过 |
| L2 | 高可用靠啥？ | 副本+自愈 | RS 维持副本+探针重启 | 说「K8s 保证」算 L2 未过 |
| L3 | 弹性怎么实现？ | HPA 机制 | 指标追目标副本数 | 答不清算 L3 未过 |
| L4 | 负载均衡谁做？ | Service/kube-proxy | Service VIP+iptables/IPVS | 说「nginx」算 L4 未过 |
| L5 | 和裸容器比？ | 价值定位 | 声明式+自愈+生态 vs 手运维 | 无对比算 L5 未过 |

## 版本与兼容性
- HPA 早期基于 `metrics-server`（CPU/内存），现支持 `custom.metrics`/`external.metrics`（如 QPS、队列长度），KEDA 可接任意事件源。
- 自愈依赖 `livenessProbe`/`readinessProbe` 配置合理——配错探针反而会造成频繁重启（踩坑点）。
- 与「微服务治理」（见 `157-microservice-governance.deep.md`/`158-microservice-fault-tolerance.deep.md`）互补：K8s 提供基础设施级弹性，服务网格提供应用级治理。

## 总结与追问预判
收口：**K8s 优势 = 自动化 + 高可用(副本自愈) + 弹性(HPA) + 负载均衡(Service) + 生态**，本质是「把运维经验沉淀进控制循环」。预判追问：① 用在哪些场景（见 `1515-k8s-scenarios-features.md`）；② 架构基础（见 `1515-k8s-architecture.md`）。回答时把「声明式期望状态 + 控制循环调和」这句抛出，最显深度。

## ⚠️ 原文纠错
源视频转写将 Kubernetes / 高可用 / 自动扩展 / 负载均衡 / Prometheus / Grafana 等音译为崩坏词（如「k 八 s」「第六个优势/第六将流量」序号错乱、「普罗米修斯」保留、「graph」指代 Grafana），本卡已还原为规范术语（Kubernetes / 高可用 / 自动扩缩 / 负载均衡 / Prometheus / Grafana）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 答「优势」时务必落到**机制**而非名词：高可用→「RS 维持副本 + 探针自愈」；弹性→「HPA 按指标追目标副本数」。只背「K8s 高可用弹性好」等于没答；讲清控制循环（调和期望状态）才是面试官想听的。

```yaml
# 弹性扩缩：HPA 按 CPU 利用率自动维持 2~10 个副本
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata: { name: nginx-hpa }
spec:
  scaleTargetRef: { apiVersion: apps/v1, kind: Deployment, name: nginx }
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource: { name: cpu, target: { type: Utilization, averageUtilization: 70 } }
```

```go
// Go 侧用 client-go 扩缩 Deployment 副本（弹性能力的编程入口）
package main

import (
	"context"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
)

func scale(deploy, ns string, replicas int32) error {
	cfg, _ := rest.InClusterConfig()
	cli, _ := kubernetes.NewForConfig(cfg)
	return cli.AppsV1().Deployments(ns).Scale(
		context.TODO(), deploy,
		&autoscalingScale{Spec: metav1.ObjectMeta{}, Status: struct{}{}},
		0, metav1.UpdateOptions{},
	).Error()
}
```
