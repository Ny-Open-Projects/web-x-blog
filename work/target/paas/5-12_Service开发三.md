# Go PaaS 平台开发: Service 业务逻辑层开发（三）—— 落地 K8s 的创建/更新/删除

## 纲要

- `CreatePodToK8s`：先 Get 判断是否存在，不存在才 Create
- `UpdatePodToK8s`：存在则 Update，不存在则提前 Create
- `DeletePodFromK8s`：从 K8s 删除 Deployment，再回写数据库
- 错误统一交由 `common` 包记录，避免主程序直接退出
- 业务层把"数据库记录"与"集群资源"两步操作编排成一致动作

## 把 Deployment 真正写进集群

5-11 解决了"模型 → Deployment 对象"的转换，本节解决"对象 → K8s 集群"的落地。Service 层通过 `clientset.AppsV1().Deployments(namespace)` 完成增删改。

## 创建

```go
import (
	"context"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
)

// CreatePodToK8s 先判断是否存在，不存在则创建
func (u *PodDataService) CreatePodToK8s(info *PodInfo) error {
	ctx := context.Background()
	ns := info.PodNamespace

	// 先查询集群中是否已存在该 Deployment
	_, err := u.clientSet.AppsV1().Deployments(ns).
		Get(ctx, info.PodName, metav1.GetOptions{})
	if err == nil {
		// 已存在，跳过创建（或返回已存在提示）
		return nil
	}

	// 不存在则创建
	deployment := u.PodToK8s(info)
	_, err = u.clientSet.AppsV1().Deployments(ns).
		Create(ctx, deployment, metav1.CreateOptions{})
	if err != nil {
		// 统一交给 common 包记录，不直接让主程序退出
		common.LogError(err)
		return err
	}
	return nil
}
```

> 注意：真正创建前还需在 `main` 中配置 K8s 远程连接（kubeconfig / in-cluster config），本方法只负责业务逻辑。

## 更新

```go
// UpdatePodToK8s 存在则更新，不存在则提前创建
func (u *PodDataService) UpdatePodToK8s(info *PodInfo) error {
	ctx := context.Background()
	ns := info.PodNamespace

	_, err := u.clientSet.AppsV1().Deployments(ns).
		Get(ctx, info.PodName, metav1.GetOptions{})
	if err != nil {
		// 查不到：当作不存在，提前创建
		return u.CreatePodToK8s(info)
	}

	deployment := u.PodToK8s(info)
	_, err = u.clientSet.AppsV1().Deployments(ns).
		Update(ctx, deployment, metav1.UpdateOptions{})
	if err != nil {
		common.LogError(err)
		return err
	}
	return nil
}
```

> `Create` / `Get` / `Update` 的 options 类型不同（`CreateOptions` / `GetOptions` / `UpdateOptions`），不可混用。

## 删除

```go
// DeletePodFromK8s 从 K8s 删除 Deployment，并回写数据库
func (u *PodDataService) DeletePodFromK8s(info *PodInfo) error {
	ctx := context.Background()
	ns := info.PodNamespace

	err := u.clientSet.AppsV1().Deployments(ns).
		Delete(ctx, info.PodName, metav1.DeleteOptions{})
	if err != nil {
		common.LogError(err)
		// 集群删除失败时，可结合事务或日志记录，便于后续手动清理
		return err
	}

	// 集群资源删除成功后，同步删除数据库记录，保证两端一致
	if err := u.PodRepository.DeletePodByID(info.ID); err != nil {
		common.LogError(err)
		return err
	}
	return nil
}
```

## 一致性考量

- 删除操作涉及"集群资源"与"数据库记录"两处，任一步失败都应记录日志，必要时引入补偿（事务或手动清理）保证最终一致。
- 所有 K8s 操作的错误统一进入 `common` 包日志，避免局部 panic 拖垮主程序。

## Demo 示例（运行说明）

以上三个方法依赖一个持有 clientset 与 repository 的 Service 结构（节选自本层设计）：

```go
type PodDataService struct {
	PodRepository repository.IPodRepository
	clientSet     *kubernetes.Clientset
}

func NewPodDataService(repo repository.IPodRepository, cs *kubernetes.Clientset) *PodDataService {
	return &PodDataService{PodRepository: repo, clientSet: cs}
}
```

### 代码说明

- `clientSet.AppsV1()` 对应 `appsv1` API 组，版本固定 `v0.22.4`。
- 先 Get 再 Create/Update 是 K8s 幂等操作的常见范式。

### 技术点总结

- 集群资源与数据库记录需成对编排，删除尤需谨慎（可能联动计费资源）。
- options 类型随操作不同而不同，不能张冠李戴。
- 错误统一旁路记录，保护主程序稳定性。

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
