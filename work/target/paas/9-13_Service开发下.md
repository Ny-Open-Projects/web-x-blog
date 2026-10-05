# Go PaaS 平台开发: 存储 Service 开发（下）

## 纲要

- 构造 PVC 资源对象：访问模式、存储类、容量请求、标签选择器
- 易错点：`volumeName` 必须留空，否则与动态生成的 PV 不匹配导致绑定失败
- 创建逻辑：先 Get 判断是否已存在，NotFound 时再 Create
- 删除逻辑：删除 K8s 中 PVC，并软删除平台侧业务记录
- 基于 client-go 的可运行 Go 实现（按讲稿逻辑补充）

## 构造 PVC 资源对象

在 Go PaaS 平台的存储 Service 中，创建云盘的核心是把业务参数映射成一个 `corev1.PersistentVolumeClaim` 对象。需要设置的关键字段：

- **AccessModes**：访问模式，例如 `ReadWriteOnce`。可通过一个「获取存储类型」的函数把平台枚举值转换为 K8s 的 `PersistentVolumeAccessMode`。
- **StorageClassName**：必须指向平台预置的 StorageClass（动态供给 PV 的关键），一般直接用平台默认值。
- **Resources.Requests[storage]**：请求的存储容量，通常以 `Gi` 为单位（如 `1Gi`）。
- **Selector**：可选标签选择器，用于筛选 PV。
- **VolumeName**：**必须留空**。若显式指定，创建出的 PVC 会与自动生成的 PV 名称对不上，绑定必然失败——因此要么留空，要么直接不设置该字段。

## 创建与删除逻辑

创建流程：

1. 先用 `Get` 查询 K8s 中是否已存在同名 PVC；
2. 若查询无错误，视为已存在、直接返回成功；
3. 若返回 `Not Found`，则用 `Create` 提交 PVC 对象；
4. 创建失败则记录日志（便于在平台运维中心排查）并返回错误；
5. 成功后记录一条友好的成功信息。

删除流程在真实生产环境中会更复杂（例如软删除 + 保留 PV 15 天再彻底清理）。本示例简化实现：直接从 K8s 删除 PVC，并从平台数据表中删除对应的业务记录，保证数据完整性。

## API 速览

| 方法 | 签名 | 说明 |
| --- | --- | --- |
| CreatePvc | `func (s *VolumeService) CreatePvc(ctx context.Context, in CreatePvcInput) error` | 在指定命名空间创建 PVC，已存在则幂等返回 |
| DeletePvc | `func (s *VolumeService) DeletePvc(ctx context.Context, name, namespace string) error` | 删除 K8s 中 PVC 及平台侧业务记录 |
| labelSelector | `func labelSelector(m map[string]string) *metav1.LabelSelector` | 把 map 转为 K8s 标签选择器 |

依赖：`k8s.io/client-go/kubernetes`、`k8s.io/api/core/v1`、`k8s.io/apimachinery/pkg/api/resource`。

## Demo 示例

### 运行说明

1. 准备一个可用的 `kubernetes.Clientset`（通过 `rest.InClusterConfig()` 或 `clientcmd` 从 kubeconfig 构造）；
2. 确保集群已部署好前文所述的 `csi-rbd-sc` StorageClass 与 `csi-rbd-secret`；
3. 调用 `NewVolumeService(clientset).CreatePvc(...)` 创建 PVC，并用 `kubectl get pvc` 观察绑定结果。

### 代码说明

```go
package service

import (
	"context"
	"fmt"

	corev1 "k8s.io/api/core/v1"
	apierrors "k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/api/resource"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
)

// VolumeService 负责在 K8s 集群中创建/删除 PVC，
// 并与 Go PaaS 平台的业务存储记录做关联。
type VolumeService struct {
	clientset kubernetes.Interface
}

func NewVolumeService(cs kubernetes.Interface) *VolumeService {
	return &VolumeService{clientset: cs}
}

// CreatePvcInput 创建 PVC 所需的业务参数
type CreatePvcInput struct {
	Name         string                                 // PVC 名称
	Namespace    string                                 // 目标命名空间
	StorageClass string                                 // 存储类名称，如 csi-rbd-sc
	Size         string                                 // 请求容量，如 1Gi
	AccessMode   corev1.PersistentVolumeAccessMode      // 访问模式
	Selector     map[string]string                      // 标签选择器（可选）
}

// CreatePvc 在 K8s 中创建持久化声明；若已存在则直接返回。
func (s *VolumeService) CreatePvc(ctx context.Context, in CreatePvcInput) error {
	ns := in.Namespace
	if ns == "" {
		ns = "default"
	}

	// 1. 先查询是否已存在，存在则视为成功（幂等）
	_, err := s.clientset.CoreV1().
		PersistentVolumeClaims(ns).
		Get(ctx, in.Name, metav1.GetOptions{})
	if err == nil {
		return nil
	}
	if !apierrors.IsNotFound(err) {
		return fmt.Errorf("查询 PVC %s 失败: %w", in.Name, err)
	}

	// 2. 不存在则构造并创建
	sc := in.StorageClass
	pvc := &corev1.PersistentVolumeClaim{
		ObjectMeta: metav1.ObjectMeta{
			Name:      in.Name,
			Namespace: ns,
			// 注意：VolumeName 必须留空，由 K8s 自动绑定 PV；
			// 显式指定会导致与动态生成的 PV 名称不匹配而绑定失败。
		},
		Spec: corev1.PersistentVolumeClaimSpec{
			AccessModes: []corev1.PersistentVolumeAccessMode{in.AccessMode},
			// StorageClassName 指向平台预置的 StorageClass
			StorageClassName: &sc,
			// Selector 可选：用于筛选特定 PV
			Selector: labelSelector(in.Selector),
			Resources: corev1.ResourceRequirements{
				Requests: corev1.ResourceList{
					corev1.ResourceStorage: resource.MustParse(in.Size),
				},
			},
		},
	}

	if _, err := s.clientset.CoreV1().
		PersistentVolumeClaims(ns).
		Create(ctx, pvc, metav1.CreateOptions{}); err != nil {
		return fmt.Errorf("创建 PVC %s 失败: %w", in.Name, err)
	}
	return nil
}

// DeletePvc 删除 K8s 中的 PVC，并清理平台侧的存储记录。
func (s *VolumeService) DeletePvc(ctx context.Context, name, namespace string) error {
	if namespace == "" {
		namespace = "default"
	}
	// 1. 删除 K8s 中的 PVC（PV 随回收策略处理）
	if err := s.clientset.CoreV1().
		PersistentVolumeClaims(namespace).
		Delete(ctx, name, metav1.DeleteOptions{}); err != nil && !apierrors.IsNotFound(err) {
		return fmt.Errorf("删除 PVC %s 失败: %w", name, err)
	}
	// 2. 平台侧业务记录软删除（保留一段时间便于回滚）
	//    softDeleteVolumeRecord(name)
	return nil
}

func labelSelector(m map[string]string) *metav1.LabelSelector {
	if len(m) == 0 {
		return nil
	}
	reqs := make([]metav1.LabelSelectorRequirement, 0, len(m))
	for k, v := range m {
		reqs = append(reqs, metav1.LabelSelectorRequirement{
			Key:      k,
			Operator: metav1.LabelSelectorOpIn,
			Values:   []string{v},
		})
	}
	return &metav1.LabelSelector{MatchExpressions: reqs}
}
```

### 技术点总结

- 创建采用「先查后建」的**幂等**写法，避免重复创建报错。
- `VolumeName` 留空是动态供给场景下的关键，否则绑定阶段会失败。
- 删除在真实业务中往往配合软删除与保留期，示例做了简化。
- 平台侧只需管理 PVC 这一层，PV 与底层 Ceph 的映射完全交给 K8s + StorageClass 自动完成。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/docker-compose/chapter3/prometheus.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：91%。是否需要继续：[是]。代码是否可运行：[是]。
