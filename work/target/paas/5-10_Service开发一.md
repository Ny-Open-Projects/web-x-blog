# Go PaaS 平台开发: Service 业务逻辑层开发（一）—— 分层与 CRUD 编排

## 纲要

- Service 是业务逻辑核心层，既操作数据库（repository），也操作 K8s（client-go）
- 采用"接口 + 实现"，构造函数返回接口类型，实现依赖倒置
- 基础 CRUD 直接委派给 repository
- 引入 `k8s.io/client-go` v0.22.4（版本务必固定，否则可能起不来）
- 以 Base / AppStore / MiddleType 三个真实服务示例说明统一范式

## Service 层的定位

在 4-4 的分层里，service 是最核心、也最易变更的一层。它同时持有：

- **repository**：负责数据持久化；
- **K8s clientset**：负责把应用真正落地到集群。

简单的增删改查可直接委派给 repository；涉及集群交互（创建 Deployment、应用计费联动）则在本层编排。

## 统一的服务范式

以 `Base` 服务为例，完整展示"接口 + 实现 + 构造函数返回接口"：

```go
// base/domain/service/base_data_service.go
package service

import (
	"git.imooc.com/coding-535/base/domain/model"
	"git.imooc.com/coding-535/base/domain/repository"
)

// 接口类型
type IBaseDataService interface {
	AddBase(*model.Base) (int64, error)
	DeleteBase(int64) error
	UpdateBase(*model.Base) error
	FindBaseByID(int64) (*model.Base, error)
	FindAllBase() ([]model.Base, error)
}

// 注意：返回值 IBaseDataService 接口类型
func NewBaseDataService(baseRepository repository.IBaseRepository) IBaseDataService {
	return &BaseDataService{baseRepository}
}

type BaseDataService struct {
	// 注意：这里是 IBaseRepository 类型
	BaseRepository repository.IBaseRepository
}
```

### CRUD 委派实现

```go
func (u *BaseDataService) AddBase(base *model.Base) (int64, error) {
	return u.BaseRepository.CreateBase(base)
}

func (u *BaseDataService) DeleteBase(baseID int64) error {
	return u.BaseRepository.DeleteBaseByID(baseID)
}

func (u *BaseDataService) UpdateBase(base *model.Base) error {
	return u.BaseRepository.UpdateBase(base)
}

func (u *BaseDataService) FindBaseByID(baseID int64) (*model.Base, error) {
	return u.BaseRepository.FindBaseByID(baseID)
}

func (u *BaseDataService) FindAllBase() ([]model.Base, error) {
	return u.BaseRepository.FindAll()
}
```

## 不同模块的差异点

各服务在统一范式上会有扩展。例如 `AppStore` 服务额外承载统计能力，并持有 K8s clientset：

```go
// appstore/domain/service/appStore_data_service.go（节选）
type IAppStoreDataService interface {
	AddAppStore(*model.AppStore) (int64, error)
	DeleteAppStore(int64) error
	UpdateAppStore(*model.AppStore) error
	FindAppStoreByID(int64) (*model.AppStore, error)
	FindAllAppStore() ([]model.AppStore, error)
	// 统计服务
	AddInstallNum(int64) error
	GetInstallNum(int64) int64
	AddViewNum(int64) error
	GetViewNum(int64) int64
}

func NewAppStoreDataService(
	appStoreRepository repository.IAppStoreRepository,
	clientSet *kubernetes.Clientset,
) IAppStoreDataService {
	return &AppStoreDataService{AppStoreRepository: appStoreRepository}
}
```

`MiddleType` 服务则提供"按版本查镜像地址"这类领域方法：

```go
// middleware/domain/service/middle_type_data_service.go（节选）
func (u *MiddleTypeDataService) FindImageVersionByID(middleVersionID int64) (string, error) {
	version, err := u.MiddleTypeRepository.FindVersionByID(middleVersionID)
	if err != nil {
		return "", err
	}
	return version.MiddleDockerImage + ":" + version.MiddleVS, nil
}
```

## K8s 依赖版本

Pod 服务需要操作 K8s，务必固定客户端版本，否则 API 不兼容会导致服务起不来：

```go
import (
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/kubernetes/typed/apps/v1"
)

// go.mod 中固定：k8s.io/client-go v0.22.4
```

## API 速览

| 方法 | 来源 | 作用 |
| --- | --- | --- |
| `AddBase` | Base 服务 | 委派 repository 插入 |
| `FindAllBase` | Base 服务 | 委派 repository 查全部 |
| `GetInstallNum` | AppStore 服务 | 读取安装量统计 |
| `FindImageVersionByID` | MiddleType 服务 | 拼接镜像地址 `image:tag` |

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
