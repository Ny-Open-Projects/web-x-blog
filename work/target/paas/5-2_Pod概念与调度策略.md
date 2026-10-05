# Go PaaS 平台开发: Pod 核心概念与调度策略

## 纲要

- Pod 是 K8s 中可被调度的最小逻辑单元，一个 Pod 可包含多个容器
- Pod 内容器共享的五大资源：PID、网络、IPC、UTS、存储卷
- Pod 生命周期五态：Pending / Running / Succeeded / Failed / Unknown
- 重启策略：Always / OnFailure / Never，与控制器强相关
- 健康检测：Liveness 探针与 Readiness 探针
- 调度策略：节点亲和性、Pod 亲和/反亲和、污点与容忍、DaemonSet 与批处理调度

## Pod 是什么

Pod 是 K8s 集群中**能被调度的最小逻辑单元**。它与直接使用 Docker 容器不同：Docker 调度的最小单位是容器，而 K8s 调度的最小单位是 Pod——一个 Pod 中可以运行一个或多个容器。可以把 Pod 理解为一个快递盒，盒内可以装多件"物品"（容器）。

一个典型的 Nginx 启动场景：将 Nginx 镜像放入 Pod 中由 K8s 调度；同一个 Pod 内还可以启动一个 busybox 做旁路采集，或启动流量网关容器统一收口流量再转发给 Nginx，实现旁路能力。

## Pod 内共享的资源

同一个 Pod 内的多个容器共享以下资源：

- **PID 命名空间**：容器间可以看到彼此的进程 ID。
- **网络命名空间**：多个容器共享同一个 IP 与端口。
- **IPC 命名空间**：容器间可通过 System V IPC 或 POSIX 消息队列通信。
- **UTS 命名空间**：多个容器共享同一个主机名。
- **存储卷**：将外部分布式存储挂载到 Pod 后，所有容器共享该卷。

## Pod 生命周期

| 状态 | 含义 |
| --- | --- |
| Pending | 已被系统接受，但有一个或多个容器镜像尚未创建（含调度与拉镜像时间） |
| Running | 已绑定到节点，所有容器已创建，且至少一个在运行/启动/重启中 |
| Succeeded | 所有容器均成功终止且不再重启（Job 中常见） |
| Failed | 所有容器已终止，且至少一个以非 0 退出码失败 |
| Unknown | 因网络等原因无法获取状态，属异常态 |

## 重启策略

| 策略 | 行为 |
| --- | --- |
| Always | 容器失效时由 kubelet 自动重启 |
| OnFailure | 容器终止且退出码非 0 时自动重启 |
| Never | 不论状态如何都不重启 |

策略与控制器强绑定：ReplicaSet / DaemonSet 必须设为 `Always` 以保证持续运行；Job 用 `OnFailure` 或 `Never` 保证执行完即止。静态 Pod（如 etcd）由 kubelet 直接创建，不在调度范围内。

## 健康检测

通过两个探针实现自愈与流量控制：

- **Liveness（存活探针）**：判断容器是否存活、是否处于 Running。若不健康则按重启策略处理。若不配置，K8s 默认认为容器永远存活。
- **Readiness（就绪探针）**：判断容器是否启动完成、是否处于 Ready。若失败，EndpointController 会将该 Pod 从 Service 与 Endpoint 列表中摘除，停止接收流量。

探针相关参数：`initialDelaySeconds`（容器启动后首次探测前等待的预热时间）、`timeoutSeconds`（探测等待响应的超时）。

## 调度策略

K8s 调度体系丰富，主要包括：

- **全自动最优调度**：Deployment / ReplicaSet 内置最优节点算法。
- **定向调度**：通过 `nodeSelector`、节点亲和性（nodeAffinity）将 Pod 调度到满足条件的节点。
- **DaemonSet 场景调度**：在每台节点上运行守护进程，如 GlusterFS / Ceph 的存储进程、日志采集（Logstash）、节点性能采集（node-exporter / Prometheus）。
- **批处理调度**：工作队列模式（单进单出）、消费者队列模式（Pod 数量随压力弹性变化）、网格模式。
- **Pod 亲和与反亲和**：Pod 亲和决定哪些 Pod 可部署在同一拓扑域（如两地三中心容灾）；反亲和决定哪些 Pod 不可同域部署。
- **污点（Taint）与容忍（Toleration）**：作用于 Node 与 Pod，二者互斥，用于优化集群内调度分布，与节点亲和方向相反。

## API 速览

Pod 模型将前述概念映射为数据库实体。下面是本 PaaS 平台中 Pod 及其子表的模型定义（来自 `pod/domain/model`）：

```go
// pod/domain/model/pod.go
type Pod struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	PodName string `gorm:"unique_index;not_null" json:"pod_name"`
	PodNamespace string `json:"pod_namespace"`
	//POD 所属的团队
	PodTeamID string `json:"pod_team_id"`
	//POD 使用的CPU最小值
	PodCpuMin float32 `json:"pod_cpu_min"`
	//POD 使用的CPU最大值
	PodCpuMax float32 `json:"pod_cpu_max"`
	//副本数量
	PodReplicas int32 `json:"pod_replicas"`
	//POD 使用的内存最小值
	PodMemoryMin float32 `json:"pod_memory_min"`
	//POD 使用的内存最大值
	PodMemoryMax float32 `json:"pod_memory_max"`
	//POD 开放的端口
	PodPort []PodPort `gorm:"ForeignKey:PodID" json:"pod_port"`
	//POD 使用的环境变量
	PodEnv []PodEnv `gorm:"ForeignKey:PodID" json:"pod_env"`
	//镜像拉取策略: Always / IfNotPresent / Never
	PodPullPolicy string `json:"pod_pull_policy"`
	//重启策略: Always / OnFailure / Never
	PodRestart string `json:"pod_restart"`
	//发布策略: Recreate / Rolling / Custom
	PodType string `json:"pod_type"`
	//使用的镜像名称+tag
	PodImage string `json:"pod_image"`
}
```

```go
// pod/domain/model/pod_port.go
type PodPort struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	PodID int64 `json:"pod_id"`
	ContainerPort int32 `json:"container_port"`
	Protocol string `json:"protocol"`
}
```

```go
// pod/domain/model/pod_env.go
type PodEnv struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	PodID int64 `json:"pod_id"`
	EnvKey string `json:"env_key"`
	EnvValue string `json:"env_value"`
}
```

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
