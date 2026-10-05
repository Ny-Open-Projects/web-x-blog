# Go PaaS 平台开发: 路由 Model 与 Repository 开发

## 纲要

- 路由数据模型设计：`Route` 与 `RoutePath` 一对多关系
- 字段含义：路由名、命名空间、域名、路径、后端 Service 与端口
- `IRouteRepository` 接口定义与 GORM 实现
- 删除时的**事务处理**：主表与关联表一起删，异常回滚
- 关联查询使用 `Preload` 一次性带出 RoutePath

本节在 `route` 微服务中开发路由的 model 与 repository。路由的核心是一张主表加一张关联的路径表，一个路由（域名）可以绑定多条路径，每条路径对应一个后端 Service 及端口。

## 数据模型设计

`Route` 表示一条路由规则，包含路由名、命名空间、对外域名；`RoutePath` 是关联表，记录该路由下每一条路径对应的后端 Service 名称和端口。`RoutePath` 通过 `RouteID` 外键关联到 `Route`。

```go
package model

type Route struct {
	ID            int64       `gorm:"primary_key;not_null;auto_increment"`
	RouteName     string      `json:"route_name"`
	RouteNamespace string      `json:"route_namespace"`
	RouteHost     string      `json:"route_host"`
	RoutePath     []RoutePath `gorm:"ForeignKey:RouteID" json:"route_path"`
}

type RoutePath struct {
	ID                    int64  `gorm:"primary_key;not_null;auto_increment"`
	RouteID               int64  `json:"route_id"`
	RoutePathName         string `json:"route_path_name"`
	RouteBackendService   string `json:"route_backend_service"`
	RouteBackendServicePort int32 `json:"route_backend_service_port"`
}
```

要点说明：

- `RouteHost`：对外绑定的域名，例如 `app1.example.com`。
- `RoutePathName`：绑定的 URI 路径，如 `/` 或 `/api`。
- `RouteBackendService` / `RouteBackendServicePort`：路径实际转发到的后端 Service 名称及其暴露数据的端口。

## Repository 接口与实现

Repository 层封装对 MySQL 的读写，接口定义如下：

```go
package repository

import (
	"git.imooc.com/coding-535/common"
	"github.com/jinzhu/gorm"
	"git.imooc.com/coding-535/route/domain/model"
)

type IRouteRepository interface {
	InitTable() error
	FindRouteByID(int64) (*model.Route, error)
	CreateRoute(*model.Route) (int64, error)
	DeleteRouteByID(int64) error
	UpdateRoute(*model.Route) error
	FindAll() ([]model.Route, error)
}

func NewRouteRepository(db *gorm.DB) IRouteRepository {
	return &RouteRepository{mysqlDb: db}
}
```

### 关联查询

创建与查询时使用 `Preload("RoutePath")` 把关联的路径数据一起带出，否则查出来的 `Route` 只有主表字段、没有路径信息：

```go
func (u *RouteRepository) FindRouteByID(routeID int64) (route *model.Route, err error) {
	route = &model.Route{}
	return route, u.mysqlDb.Preload("RoutePath").First(route, routeID).Error
}

func (u *RouteRepository) FindAll() (routeAll []model.Route, err error) {
	return routeAll, u.mysqlDb.Preload("RoutePath").Find(&routeAll).Error
}
```

### 删除的事务处理（重点）

由于路由主表与路径关联表存在外键关系，删除路由时必须**同时删除主表和关联表**，并用事务保证原子性，遇到错误回滚：

```go
func (u *RouteRepository) DeleteRouteByID(routeID int64) error {
	tx := u.mysqlDb.Begin()
	defer func() {
		if r := recover(); r != nil {
			tx.Rollback()
		}
	}()
	if tx.Error != nil {
		common.Error(tx.Error)
		return tx.Error
	}
	// 先删主表
	if err := u.mysqlDb.Where("id = ?", routeID).Delete(&model.Route{}).Error; err != nil {
		tx.Rollback()
		common.Error(err)
		return err
	}
	// 再删关联表
	if err := u.mysqlDb.Where("route_id = ?", routeID).Delete(&model.RoutePath{}).Error; err != nil {
		tx.Rollback()
		common.Error(err)
		return err
	}
	return tx.Commit().Error
}
```

`CreateRoute` 与 `UpdateRoute` 直接复用 GORM 的 `Create` / `Update` 即可，逻辑简单。

## API 速览

| 方法 | 签名 | 说明 |
| --- | --- | --- |
| InitTable | `InitTable() error` | 初始化 `Route`、`RoutePath` 两张表 |
| FindRouteByID | `FindRouteByID(int64) (*model.Route, error)` | 按 ID 查询并预加载路径 |
| CreateRoute | `CreateRoute(*model.Route) (int64, error)` | 插入一条路由，返回自增 ID |
| DeleteRouteByID | `DeleteRouteByID(int64) error` | 事务删除主表 + 关联表 |
| UpdateRoute | `UpdateRoute(*model.Route) error` | 全量更新路由 |
| FindAll | `FindAll() ([]model.Route, error)` | 查询全部路由并预加载路径 |

## 技术点总结

- 路由采用「一（Route）对多（RoutePath）」建模，对应一个域名绑定多个路径、每个路径指向不同 Service。
- 关联查询务必 `Preload`，否则关联数据为空。
- 删除必须走事务，先主表后关联表，任何一步失败整体回滚，避免产生孤儿数据。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/base/domain/model/base.go`
- `code/课件/appstore/domain/model/app_category.go`
- `code/课件/appstore/domain/model/app_pod.go`
- `code/课件/appstore/domain/model/app_middle.go`
- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/appstore/domain/model/app_volume.go`
- `code/课件/appstore/domain/model/app_isv.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
