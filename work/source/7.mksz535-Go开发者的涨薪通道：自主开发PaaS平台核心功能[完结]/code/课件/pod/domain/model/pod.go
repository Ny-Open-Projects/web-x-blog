package model

//POD的状态
//挂起（Pending）：Pod 已被 Kubernetes 系统接受，但有一个或者多个容器镜像尚未创建。等待时间包括调度 Pod 的时间和通过网络下载镜像的时间，这可能需要花点时间。
//运行中（Running）：该 Pod 已经绑定到了一个节点上，Pod 中所有的容器都已被创建。至少有一个容器正在运行，或者正处于启动或重启状态。
//成功（Succeeded）：Pod 中的所有容器都被成功终止，并且不会再重启。
//失败（Failed）：Pod 中的所有容器都已终止了，并且至少有一个容器是因为失败终止。也就是说，容器以非0状态退出或者被系统终止。
//未知（Unknown）：因为某些原因无法取得 Pod 的状态，通常是因为与 Pod 所在主机通信失败。
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
	PodPort[] PodPort `gorm:"ForeignKey:PodID" json:"pod_port"`
	//POD 使用的环境变量
	PodEnv[] PodEnv `gorm:"ForeignKey:PodID" json:"pod_env"`
	//镜像拉取策略
	//Always：总是拉取 pull
	//IfNotPresent：默认值,本地有则使用本地镜像,不拉取
	//Never：只使用本地镜像，从不拉取
	PodPullPolicy string `json:"pod_pull_policy"`
	//重启策略
	//Always: 当容器失效时, 由kubelet自动重启该容器
	//OnFailure: 当容器终止运行且退出码不为0时, 由kubelet自动重启该容器
	//Never: 不论容器运行状态如何, kubelet都不会重启该容器
	//注意：
	//1.kubelet重启失效容器的时间间隔以sync-frequency乘以2n来计算, 例如1丶2丶4丶8倍等, 最长延时5min, 并且在重启后的10min后重置该时间
	//2.pod的重启策略与控制方式有关
	//- RC和DeamonSet必须设置为Always,需要保证该容器持续运行
	//- Job: OnFailure或Never, 确保容器执行完成后不再重启
	PodRestart string `json:"pod_restart"`
	//pod的发布策略
	//重建(recreate)：停止旧版本部署新版本
	//滚动更新(rolling-update)：一个接一个地以滚动更新方式发布新版本
	//蓝绿(blue/green)：新版本与旧版本一起存在，然后切换流量
	//金丝雀(canary)：将新版本面向一部分用户发布，然后继续全量发布
	//A/B测(a/b testing)：以精确的方式（HTTP 头、cookie、权重等）向部分用户发布新版本。A/B测实际上是一种基于数据统计做出业务决策的技术。在 Kubernetes 中并不原生支持，需要额外的一些高级组件来完成改设置（比如Istio、Linkerd、Traefik、或者自定义 Nginx/Haproxy 等）。
	//Recreate,Custom,Rolling
	PodType string `json:"pod_type"`
	//使用的镜像名称+tag
	PodImage string `json:"pod_image"`
	//@TODO 挂盘
	//@TODO 域名设置
}
