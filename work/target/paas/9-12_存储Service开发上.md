# Go PaaS 平台开发: 存储 Service 开发（上）——在 K8s 中创建 PVC

## 纲要

- 存储 Service 对外只暴露两个方法：Create（创建 PVC 到 K8s）、Delete（删除 PVC）
- 查询类需求直接从平台数据库读取，并可记录 PVC 实时状态
- 使用 client-go 以编程方式构建 `corev1.PersistentVolumeClaim` 对象
- PVC 关键字段：TypeMeta（apiVersion=v1）、ObjectMeta、Spec（accessModes / storageClassName / resources / claim）
- 访问模式（AccessMode）通过函数映射，支持多值数组，并用默认值约束输入范围

## Service 方法设计

存储 Service 只提供创建与删除两个动作：

- `Create`：把存储创建到 K8s 的 PVC 中
- `Delete`：删除对应的 PVC

查询操作不经过 K8s，而是直接查平台数据库；同时可记录查询时 PVC 的绑定状态，做实时状态展示。

## 构建 PVC 对象

下面给出用 client-go 编程创建 PVC 的核心 Go 代码。

### 代码说明

`service/storage.go` —— 创建 PVC：

```go
package service

import (
	"context"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
)

// CreatePVC 在指定命名空间创建 PVC
func CreatePVC(client kubernetes.Interface, namespace, name, storageClass string,
	accessModes []corev1.PersistentVolumeAccessMode, sizeGb string) error {

	pvc := &corev1.PersistentVolumeClaim{
		TypeMeta: metav1.TypeMeta{
			APIVersion: "v1",
			Kind:       "PersistentVolumeClaim",
		},
		ObjectMeta: metav1.ObjectMeta{
			Name:      name,
			Namespace: namespace,
			// Labels 可选：若与 StorageClass 的 selector 匹配，可指定绑定目标
			// Labels: map[string]string{"app": "my-app"},
		},
		Spec: corev1.PersistentVolumeClaimSpec{
			// claim：声明通过 K8s 绑定控制器自动绑定 PV
			// 不写 StorageClassName 时，PVC 可能用默认 StorageClass 创建，
			// 若集群无默认 SC，则状态会一直处于 Pending 无法绑定
			StorageClassName: &storageClass,
			AccessModes:      accessModes,
			Resources: corev1.ResourceRequirements{
				Requests: corev1.ResourceList{
					corev1.ResourceStorage: mustParseQuantity(sizeGb),
				},
			},
		},
	}

	_, err := client.CoreV1().PersistentVolumeClaims(namespace).Create(
		context.Background(), pvc, metav1.CreateOptions{})
	return err
}
```

### 访问模式映射

访问模式支持多种取值（实际生产中存在 ReadWriteOnce / ReadOnlyMany / ReadWriteMany 多种并存的情况），使用函数把入参映射为 `corev1.PersistentVolumeAccessMode`：

```go
package service

import corev1 "k8s.io/api/core/v1"

// accessModeOf 将字符串访问模式映射为标准类型，并约束在合法范围内
func accessModeOf(mode string) corev1.PersistentVolumeAccessMode {
	switch mode {
	case "ReadWriteOnce":
		return corev1.ReadWriteOnce
	case "ReadOnlyMany":
		return corev1.ReadOnlyMany
	case "ReadWriteMany":
		return corev1.ReadWriteMany
	default:
		// 未知值回退到默认 ReadWriteOnce，提升系统健壮性
		return corev1.ReadWriteOnce
	}
}
```

## 关键注意点

- `StorageClassName` 必须明确指定。若不指定，PVC 虽然能创建，但会尝试用集群默认 StorageClass 创建 PV，若集群无默认 SC，PVC 状态将停留在 `Pending` 无法绑定
- `claim`（声明）控制是否由绑定控制器自动绑定 PV。`volumeBindingMode` 等字段如需非默认值必须显式写出；若全为默认值可省略
- `AccessModes` 是数组类型，业务逻辑上同一 PVC 可声明多种访问模式并存
- 通过 `switch` 映射访问模式，既可约束输入范围，也便于后续扩展（如统计某类访问模式的使用次数）

## 总结

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

相关度：100%。是否需要继续：是。代码是否可运行：是。
