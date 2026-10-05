# Go PaaS 平台开发: Pod 模型开发（上）—— 主结构体与子表设计

## 纲要

- 使用 GORM 定义 Pod 主结构体，关键字段加 `primary_key`、`unique_index` 等约束
- PodName 唯一、Namespace 用于多租户隔离
- 资源字段以 CPU / 内存的"最小值 + 最大值"成对出现，支撑超卖与计费
- 端口、环境变量拆分为独立子表，通过 `ForeignKey:PodID` 关联
- 模型层对应数据库映射，是整个分层的底座

## 模型设计思路

PaaS 平台要把"创建一个应用"这件事产品化，第一步就是把应用的各种属性沉淀成数据库模型。本平台使用 GORM 作为 ORM 框架，所有与数据库交互的模型都放在 `domain/model` 下。模型既要服务数据库映射，也要通过 `json` tag 支持 API 序列化。

Pod 模型并非 K8s 原生 Pod 结构的简单复制，而是平台视角的"超级结构体"——它额外记录了团队、资源配额、计费所需的 CPU/内存上下限等平台业务字段。

## Pod 主结构体

```go
// pod/domain/model/pod.go
package model

type Pod struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	// Pod 名称，全局唯一
	PodName string `gorm:"unique_index;not_null" json:"pod_name"`
	// K8s 命名空间，用于多团队/多租户资源隔离
	PodNamespace string `json:"pod_namespace"`
	// 所属团队 ID（团队权限复杂，平台只记录 ID 做关联）
	PodTeamID string `json:"pod_team_id"`
	// CPU 最小/最大使用量
	PodCpuMin float32 `json:"pod_cpu_min"`
	PodCpuMax float32 `json:"pod_cpu_max"`
	// 副本数量（对应 K8s Deployment 的 replicas）
	PodReplicas int32 `json:"pod_replicas"`
	// 内存最小/最大使用量
	PodMemoryMin float32 `json:"pod_memory_min"`
	PodMemoryMax float32 `json:"pod_memory_max"`
	// 关联的端口与环境变量子表
	PodPort []PodPort `gorm:"ForeignKey:PodID" json:"pod_port"`
	PodEnv  []PodEnv  `gorm:"ForeignKey:PodID" json:"pod_env"`
	// 镜像拉取策略 / 重启策略 / 发布策略 / 镜像
	PodPullPolicy string `json:"pod_pull_policy"`
	PodRestart    string `json:"pod_restart"`
	PodType       string `json:"pod_type"`
	PodImage      string `json:"pod_image"`
}
```

### 字段设计要点

- **PodName**：`unique_index` 保证不重复，是平台的唯一应用标识。
- **PodNamespace**：K8s 命名空间，用于多团队、多服务商、多租户的资源隔离。
- **PodTeamID**：只记录 ID 而非嵌入团队名，因为团队权限体系复杂，不宜与 Pod 强耦合。
- **CPU / 内存的 min + max**：成对出现的设计是平台计费的基石。最小值保障 Pod 最低可用资源，最大值在波峰时按需分配；平台可基于最大值规划资源池、基于最小值判断能否超卖。自建机房成本往往仅为公有云的 20% 左右，超卖能显著提升利润率。

## 端口子表

每个 Pod 可能开放多个端口，且协议（TCP / UDP）可能不同，因此拆成独立表并通过 `PodID` 关联：

```go
// pod/domain/model/pod_port.go
package model

type PodPort struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	PodID int64 `json:"pod_id"`
	ContainerPort int32 `json:"container_port"`
	Protocol string `json:"protocol"` // TCP / UDP
}
```

## 环境变量子表

Pod 启动时常依赖环境变量，且不同环境（开发 / 预发 / 生产）变量值不同，因此也独立成表：

```go
// pod/domain/model/pod_env.go
package model

type PodEnv struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	PodID int64 `json:"pod_id"`
	EnvKey string `json:"env_key"`
	EnvValue string `json:"env_value"`
}
```

环境变量采用 `key = value` 的通用格式，是跨环境流转应用时的关键手段。

## API 速览

| 模型 | 作用 | 关键约束 |
| --- | --- | --- |
| `Pod` | 应用主记录 | `PodName` 唯一、自增 ID |
| `PodPort` | 端口表 | 外键 `PodID`，含协议 |
| `PodEnv` | 环境变量表 | 外键 `PodID`，key/value |

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
