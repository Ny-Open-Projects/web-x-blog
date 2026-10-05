# Go PaaS 平台开发: Repository 数据访问层开发（上）

## 纲要

- Repository 层通过"接口 + 实现"约束数据类型，解耦业务与数据库
- 以 `IPodRepository` 为例：InitTable / FindPodByID / CreatePod / DeletePodByID / UpdatePod / FindAll
- `InitTable` 用 GORM 的 `CreateTable` 一键建表，关联子表一并创建
- `FindPodByID` 用 `Preload` 把端口、环境变量子表一并查出
- `CreatePod` 返回自增 ID；构造函数返回接口类型便于上层依赖倒置

## 为什么先写 Repository

在需求持续迭代时，改业务只动 service、改表只动 repository、改模型只动 model，三层互不污染。Repository 层是所有与数据库交互代码的归宿。本层采用"接口定义 + 结构体实现"的模式，接口约束了数据类型与能力边界。

## 定义接口

以 Pod 为例，先把要对外暴露的数据库操作抽象成接口：

```go
// pod/domain/repository/pod_repository.go
package repository

import (
	"git.imooc.com/coding-535/pod/domain/model"
	"github.com/jinzhu/gorm"
)

// 创建需要实现的接口
type IPodRepository interface {
	InitTable() error
	FindPodByID(int64) (*model.Pod, error)
	CreatePod(*model.Pod) (int64, error)
	DeletePodByID(int64) error
	UpdatePod(*model.Pod) error
	FindAll() ([]model.Pod, error)
}
```

构造函数返回**接口类型**，这是依赖倒置的关键——上层 service 只依赖 `IPodRepository`，不依赖具体实现：

```go
func NewPodRepository(db *gorm.DB) IPodRepository {
	return &PodRepository{mysqlDb: db}
}

type PodRepository struct {
	mysqlDb *gorm.DB
}
```

> 提示：未实现接口方法时，编辑器会因"返回接口但方法缺失"而报红；当所有方法补齐后红线自动消失，可作为实现进度的自检手段。

## 初始化表

借助 GORM，建表无需手写 SQL。把主表与关联子表一并创建：

```go
func (u *PodRepository) InitTable() error {
	return u.mysqlDb.CreateTable(&model.Pod{}, &model.PodEnv{}, &model.PodPort{}).Error
}
```

`CreateTable` 会根据结构体上的 GORM tag 自动建表，相比传统 SQL 脚本更易维护、可随模型演进。

## 根据 ID 查找（含关联）

Pod 与其端口、环境变量是父子关系，查询时用 `Preload` 一次性把关联数据加载出来：

```go
func (u *PodRepository) FindPodByID(podID int64) (pod *model.Pod, err error) {
	pod = &model.Pod{}
	return pod, u.mysqlDb.Preload("PodEnv").Preload("PodPort").First(pod, podID).Error
}
```

`Preload("PodEnv")` / `Preload("PodPort")` 对应模型上 `gorm:"ForeignKey:PodID"` 声明的外键关系。

## 创建 Pod

创建后把自增主键反馈给调用方：

```go
func (u *PodRepository) CreatePod(pod *model.Pod) (int64, error) {
	return pod.ID, u.mysqlDb.Create(pod).Error
}
```

## 同样的模式适用于其它模块

`base`、`volume`、`svc`、`route`、`middleware` 等模块的 Repository 结构完全一致，仅模型不同。例如 `BaseRepository`：

```go
// base/domain/repository/base_repository.go（节选）
type IBaseRepository interface {
	InitTable() error
	FindBaseByID(int64) (*model.Base, error)
	CreateBase(*model.Base) (int64, error)
	DeleteBaseByID(int64) error
	UpdateBase(*model.Base) error
	FindAll() ([]model.Base, error)
}

func NewBaseRepository(db *gorm.DB) IBaseRepository {
	return &BaseRepository{mysqlDb: db}
}
```

## API 速览

| 方法 | 签名 | 说明 |
| --- | --- | --- |
| `InitTable` | `() error` | 创建主表及关联子表 |
| `FindPodByID` | `(int64) (*model.Pod, error)` | 按 ID 查，含 Preload 关联 |
| `CreatePod` | `(*model.Pod) (int64, error)` | 插入并返回自增 ID |
| `DeletePodByID` | `(int64) error` | 删除（下节含事务） |
| `UpdatePod` | `(*model.Pod) error` | 更新 |
| `FindAll` | `() ([]model.Pod, error)` | 查全部 |

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/base/domain/repository/base_repository.go`
- `code/课件/volume/domain/repository/volume_repository.go`
- `code/课件/svc/domain/repository/svc_repository.go`
- `code/课件/pod/domain/repository/pod_repository.go`
- `code/课件/go-paas-html/pages-404.html`
- `code/课件/route/domain/repository/route_repository.go`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/middleware/domain/repository/middle_type_repository.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
