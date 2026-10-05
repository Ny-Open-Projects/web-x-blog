# Go PaaS 平台开发: Pod 模型开发（下）—— 策略字段与镜像配置

## 纲要

- 镜像拉取策略 `PodPullPolicy`：Always / IfNotPresent / Never
- 重启策略 `PodRestart`：Always / OnFailure / Never，与控制器强相关
- 发布策略 `PodType`：Recreate / Rolling / Custom（蓝绿、金丝雀、A/B 需高级组件）
- 镜像字段 `PodImage`：镜像名 + tag，是 Pod 启动的前提
- 运营设置（挂盘、域名）可独立成模块，不必全塞进 Pod 模型

## 紧接上文的策略字段

在 5-5 中我们定义了 Pod 的命名、命名空间、资源上下限以及端口、环境变量子表。本节补完 Pod 模型中与"运行策略"相关的字段。这些字段直接对应 K8s 的容器运行语义，平台在创建 Deployment 时会把它们翻译到 K8s 对象上。

## 镜像拉取策略

```go
// 镜像拉取策略
// Always：总是拉取远端镜像
// IfNotPresent：默认值，本地有则使用本地镜像，不拉取
// Never：只使用本地镜像，从不拉取
PodPullPolicy string `json:"pod_pull_policy"`
```

- `Always`：每次启动都重新拉取，保证镜像最新。
- `IfNotPresent`：默认值，本地存在即使用，省带宽。
- `Never`：仅用本地镜像，适用于离线或固定镜像场景。

## 重启策略

```go
// 重启策略
// Always: 当容器失效时, 由 kubelet 自动重启该容器
// OnFailure: 当容器终止运行且退出码不为0时, 由 kubelet 自动重启该容器
// Never: 不论容器运行状态如何, kubelet 都不会重启该容器
// 注意：
// 1. kubelet 重启失效容器的时间间隔以 sync-frequency 乘 2^n 计算，最长延时 5min，10min 后重置
// 2. Pod 的重启策略与控制方式有关：RC/DaemonSet 必须 Always；Job 用 OnFailure 或 Never
PodRestart string `json:"pod_restart"`
```

平台侧记录该策略，便于在创建 K8s Deployment 时透传，同时它也影响平台自身对应用健康状态的判定。

## 发布策略

```go
// pod 的发布策略
// 重建(recreate)：停止旧版本部署新版本
// 滚动更新(rolling-update)：一个接一个地以滚动更新方式发布新版本
// 蓝绿(blue/green)：新版本与旧版本一起存在，然后切换流量
// 金丝雀(canary)：将新版本面向一部分用户发布，然后继续全量
// A/B 测(a/b testing)：以 HTTP 头、cookie、权重等精确方式向部分用户发布
// 可选值：Recreate / Custom / Rolling
PodType string `json:"pod_type"`
```

平台的发布策略字段可取值 `Recreate`（重建）、`Rolling`（滚动）、`Custom`（自定义）。蓝绿、金丝雀、A/B 等高级策略在 K8s 中原生支持有限，通常需配合 Istio、Linkerd、Traefik 或自定义 Nginx/Haproxy 实现，需要深入研发与测试。

## 镜像字段

```go
// 使用的镜像名称+tag
PodImage string `json:"pod_image"`
```

Pod 必须基于镜像启动，镜像名 + tag 缺省会导致 Pod 起不来，前面所有参数也将失去意义。镜像通常从 Docker Hub 或私有镜像仓库拉取。

## 运营设置的边界

平台还涉及挂盘（分布式存储卷）与域名（route）等运营设置。这些**不一定**写进 Pod 模型——它们可以解耦到独立的 Service 与 Route 模块中。在前端详情页上，运营设置可与 Pod 设置一起展示，但底层模型保持独立，符合"单一职责"的分层原则。

## Demo 示例（运行说明）

下面给出一个最小可编译的模型文件，演示如何组合上述字段（节选自 `pod/domain/model`）：

```go
package model

// Pod 平台侧超级结构体（节选策略字段）
type Pod struct {
	ID            int64   `gorm:"primary_key;not_null;auto_increment" json:"id"`
	PodName       string  `gorm:"unique_index;not_null" json:"pod_name"`
	PodNamespace  string  `json:"pod_namespace"`
	PodTeamID     string  `json:"pod_team_id"`
	PodCpuMin     float32 `json:"pod_cpu_min"`
	PodCpuMax     float32 `json:"pod_cpu_max"`
	PodReplicas   int32   `json:"pod_replicas"`
	PodMemoryMin  float32 `json:"pod_memory_min"`
	PodMemoryMax  float32 `json:"pod_memory_max"`
	PodPullPolicy string  `json:"pod_pull_policy"` // Always / IfNotPresent / Never
	PodRestart    string  `json:"pod_restart"`     // Always / OnFailure / Never
	PodType       string  `json:"pod_type"`        // Recreate / Rolling / Custom
	PodImage      string  `json:"pod_image"`       // name:tag
}
```

### 代码说明

- 该结构体与 GORM 兼容，可直接用于 `AutoMigrate` 或 `CreateTable`。
- `PodName` 唯一索引保证应用名不冲突。
- 策略字段均为字符串枚举，创建 K8s Deployment 时由 Service 层翻译为对应常量。

### 技术点总结

- 镜像拉取、重启、发布三类策略是 Pod 运行的"宪法"，必须显式声明。
- 平台建模时把 K8s 原生语义与平台业务字段（团队、资源计费）合二为一。
- 挂盘/域名等运营设置宜独立成模块，避免污染 Pod 核心模型。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/go-paas-front/pod-create.html`
- `code/课件/go-paas-front/pod-detail.html`
- `code/课件/go-paas-front/pod-index.html`
- `code/课件/appstore/domain/model/app_pod.go`
- `code/课件/pod/domain/model/pod_env.go`
- `code/课件/podapi/filebeat.yml`
- `code/课件/pod/filebeat.yml`
- `code/课件/pod/domain/model/pod_port.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
