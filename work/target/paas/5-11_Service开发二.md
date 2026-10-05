# Go PaaS 平台开发: Service 业务逻辑层开发（二）—— 将 Pod 模型转换为 K8s Deployment

## 纲要

- 核心方法 `PodToK8s`：把平台 Pod 模型翻译为 `appsv1.Deployment`
- ObjectMeta、Selector.MatchLabels、Template.Labels 三处 label 必须对齐
- 容器模板：名称、镜像、端口、环境变量、资源限额
- 端口协议、重启策略通过 `switch` 转换为 K8s 枚举常量
- 资源 `limits` / `requests` 用 `resource.MustParse` 转换；request 小于 limit 才能超卖

## 从模型到 K8s 对象

Service 层拿到 `PodInfo` 后，要把平台视角的数据"翻译"成 K8s 能识别的 Deployment。这是产品化创建资源的核心一步。下面代码按 client-go `v0.22.4`、`appsv1` / `corev1` API 编写（根据讲稿逻辑补充并精简）。

## 构建 Deployment 主体

```go
import (
	appsv1 "k8s.io/client-go/kubernetes/typed/apps/v1"
	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/api/resource"
)

// PodToK8s 将平台 Pod 模型转换为 K8s Deployment
func (u *PodDataService) PodToK8s(info *PodInfo) *appsv1.Deployment {
	labels := map[string]string{
		"app": info.PodName,
	}
	return &appsv1.Deployment{
		ObjectMeta: metav1.ObjectMeta{
			Name:      info.PodName,
			Namespace: info.PodNamespace,
			Labels:    labels, // 自定义展示信息（作者、版本等）均可写在此
		},
		Spec: appsv1.DeploymentSpec{
			// selector 与 template 的 labels 必须匹配
			Selector: &metav1.LabelSelector{
				MatchLabels: labels,
			},
			Template: corev1.PodTemplateSpec{
				ObjectMeta: metav1.ObjectMeta{
					Labels: labels, // 尽量与 MatchLabels 保持一致
				},
				Spec: corev1.PodSpec{
					Containers:    []corev1.Container{u.buildContainer(info)},
					RestartPolicy: u.buildRestartPolicy(info.PodRestart),
				},
			},
		},
	}
}
```

> 关键点：`Spec.Selector.MatchLabels` 与 `Template.ObjectMeta.Labels` 必须一致，Deployment 才能通过标签找到自己管理的 Pod。Deployment 与 Service 是相对独立的资源，二者正是通过 selector 中的标签完成匹配。

## 构建容器模板

```go
func (u *PodDataService) buildContainer(info *PodInfo) corev1.Container {
	return corev1.Container{
		Name:  info.PodName,
		Image: info.PodImage, // 镜像名 + tag，缺省会导致 Pod 起不来
		Ports: u.buildPorts(info.PodPort),
		Env:   u.buildEnv(info.PodEnv),
		Resources: u.buildResources(info),
	}
}
```

### 端口协议转换

```go
func (u *PodDataService) buildPorts(ports []int32) []corev1.ContainerPort {
	out := make([]corev1.ContainerPort, 0, len(ports))
	for _, p := range ports {
		out = append(out, corev1.ContainerPort{
			ContainerPort: p,
			Protocol:      corev1.ProtocolTCP, // 默认 TCP，多协议可在此扩展
		})
	}
	return out
}
```

> 同一组端口尽量保持同一协议；若需混合协议，创建 K8s Service 时需分别处理。

### 环境变量转换

```go
func (u *PodDataService) buildEnv(env map[string]string) []corev1.EnvVar {
	out := make([]corev1.EnvVar, 0, len(env))
	for k, v := range env {
		out = append(out, corev1.EnvVar{
			Name:  k,
			Value: v,
		})
	}
	return out
}
```

### 资源限额（超卖的关键）

```go
func (u *PodDataService) buildResources(info *PodInfo) corev1.ResourceRequirements {
	return corev1.ResourceRequirements{
		Limits: corev1.ResourceList{
			corev1.ResourceCPU:    resource.MustParse(fmt.Sprintf("%f", info.PodCpuMax)),
			corev1.ResourceMemory: resource.MustParse(fmt.Sprintf("%fMi", info.PodMemoryMax)),
		},
		Requests: corev1.ResourceList{
			corev1.ResourceCPU:    resource.MustParse(fmt.Sprintf("%f", info.PodCpuMax/2)),
			corev1.ResourceMemory: resource.MustParse(fmt.Sprintf("%fMi", info.PodMemoryMax/2)),
		},
	}
}
```

- **Limits（最大值）**：波峰时集群分配的上限。
- **Requests（最小值）**：Pod 能跑起来的最小保障。
- 若 `limit == request`（如都设为 2 核），则相当于独占 2 核，空闲也占用，利用率低；把 request 设小（如 3 核 limit、1 核 request），富余算力可被其它 Pod 调度，从而提升资源利用率与平台利润率。

### 重启策略转换

```go
func (u *PodDataService) buildRestartPolicy(p string) corev1.RestartPolicy {
	switch p {
	case "OnFailure":
		return corev1.RestartPolicyOnFailure
	case "Never":
		return corev1.RestartPolicyNever
	default:
		return corev1.RestartPolicyAlways // 兜底 Always，保证数据在预期内
	}
}
```

## 技术点总结

- label 三处对齐是 Deployment 正确工作的前提。
- 协议、重启策略用 `switch` 把平台字符串枚举转成 K8s 常量，保证前端传什么都落入预期。
- `limit` 与 `request` 的差值是超卖与资源池计费的数学基础。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/base/domain/service/base_data_service.go`
- `code/课件/go-paas-html/pages-404.html`
- `code/课件/appstore/domain/service/appStore_data_service.go`
- `code/课件/middleware/domain/service/middle_type_data_service.go`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/go-paas-html/pages-login.html`
- `code/课件/go-paas-html/pages-login2.html`
- `code/课件/go-paas-html/pages-sign-up.html`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
