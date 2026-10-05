# Go PaaS 平台开发: 云应用市场 Repository 代码开发

## 纲要

- Repository 层职责：在领域模型与数据库之间做持久化，对上层 Service 屏蔽存储细节
- 接口设计：基础 CRUD + 初始化表 + 统计接口（安装/浏览量）
- 统计字段的更新技巧：使用 `gorm.Expr` 做原子自增，避免并发下的计数丢失
- 关联查询：通过 `Preload` 一次性把图片、Pod、中间件、存储、评论一并查出
- 级联删除：删除主应用前开启事务，按依赖顺序手动清理各子表，保证数据一致

## 接口定义

Repository 首先定义一组接口 `IAppStoreRepository`，把「需要操作哪些数据」先声明清楚，再落地实现。除了常规的增删改查，还补充了应用市场高频使用的统计方法：添加/获取安装量、添加/获取浏览量。

```go
package repository

import (
	"git.imooc.com/coding-535/appStore/domain/model"
	"git.imooc.com/coding-535/common"
	"github.com/jinzhu/gorm"
)

// 创建需要实现的接口
type IAppStoreRepository interface {
	// 初始化表
	InitTable() error
	// 根据 ID 查找数据
	FindAppStoreByID(int64) (*model.AppStore, error)
	// 创建一条 appStore 数据
	CreateAppStore(*model.AppStore) (int64, error)
	// 根据 ID 删除一条 appStore 数据
	DeleteAppStoreByID(int64) error
	// 修改更新数据
	UpdateAppStore(*model.AppStore) error
	// 查找 appStore 所有数据
	FindAll() ([]model.AppStore, error)

	// 添加安装数量
	AddInstallNumber(int64) error
	// 获取安装数量
	GetInstallNumber(int64) int64
	// 添加浏览量
	AddViewNumber(int64) error
	// 获取浏览量
	GetViewNumber(int64) int64
}

// 创建 appStoreRepository
func NewAppStoreRepository(db *gorm.DB) IAppStoreRepository {
	return &AppStoreRepository{mysqlDb: db}
}

type AppStoreRepository struct {
	mysqlDb *gorm.DB
}
```

## 初始化表结构

`InitTable` 通过 GORM 的 `CreateTable` 一次性创建聚合根及其所有关联子表。只要模型定义好了，建表工作非常轻量。

```go
// 初始化表
func (u *AppStoreRepository) InitTable() error {
	return u.mysqlDb.CreateTable(
		&model.AppStore{}, &model.AppComment{}, &model.AppVolume{},
		&model.AppPod{}, &model.AppImage{}, &model.AppCategory{},
		&model.AppIsv{}, &model.AppMiddle{},
	).Error
}
```

## 统计接口：原子自增是关键

安装量、浏览量是被高频并发更新的字段。如果先 `SELECT` 再 `UPDATE`，在并发场景下会丢失计数。正确做法是直接在 SQL 层做 `字段 = 字段 + 1` 的原子自增，GORM 中通过 `UpdateColumn` 配合 `gorm.Expr` 实现。

```go
// 添加安装数量统计（原子自增，避免并发丢计数）
func (u *AppStoreRepository) AddInstallNumber(appID int64) error {
	return u.mysqlDb.Model(&model.AppStore{}).
		Where("id = ?", appID).
		UpdateColumn("app_install", gorm.Expr("app_install + ?", 1)).Error
}

// 获取安装数量统计
func (u *AppStoreRepository) GetInstallNumber(appID int64) int64 {
	appStore, err := u.FindAppStoreByID(appID)
	if err != nil {
		common.Error(err)
		return 0
	}
	return appStore.AppInstall
}

// 添加浏览量统计
func (u *AppStoreRepository) AddViewNumber(appID int64) error {
	return u.mysqlDb.Model(&model.AppStore{}).
		Where("id = ?", appID).
		UpdateColumn("app_views", gorm.Expr("app_views + ?", 1)).Error
}

// 获取浏览量
func (u *AppStoreRepository) GetViewNumber(appID int64) int64 {
	appStore, err := u.FindAppStoreByID(appID)
	if err != nil {
		common.Error(err)
		return 0
	}
	return appStore.AppViews
}
```

## 关联查询：Preload 一次性加载

应用市场展示一个商品时，往往要把它的图片、Pod、中间件、存储、评论一起带出来。`FindAppStoreByID` 用 `Preload` 把各关联表一并查询，避免 N+1 问题。

```go
// 根据 ID 查找 AppStore 信息（含关联子表）
func (u *AppStoreRepository) FindAppStoreByID(appStoreID int64) (appStore *model.AppStore, err error) {
	appStore = &model.AppStore{}
	return appStore, u.mysqlDb.
		Preload("AppImage").
		Preload("AppPod").
		Preload("AppMiddle").
		Preload("AppVolume").
		Preload("AppComment").
		First(appStore, appStoreID).Error
}
```

## 基础 CRUD

创建与更新相对简单：结构体在进入 Repository 之前，已经在接口层、Service 层被处理干净，这里只需通过 GORM 落库。

```go
// 创建 AppStore 信息
func (u *AppStoreRepository) CreateAppStore(appStore *model.AppStore) (int64, error) {
	return appStore.ID, u.mysqlDb.Create(appStore).Error
}

// 更新 AppStore 信息
func (u *AppStoreRepository) UpdateAppStore(appStore *model.AppStore) error {
	return u.mysqlDb.Model(appStore).Update(appStore).Error
}

// 获取结果集
func (u *AppStoreRepository) FindAll() (appStoreAll []model.AppStore, err error) {
	return appStoreAll, u.mysqlDb.Find(&appStoreAll).Error
}
```

## 级联删除：事务 + 手动按序清理

删除一个云应用时，它下面挂载的图片、Pod、中间件、存储、评论都要一并清除。子表多、依赖重，必须开启事务，并手动按依赖顺序逐个删除，确保要么全部成功、要么整体回滚，杜绝脏数据。

```go
// 根据 ID 删除 AppStore 信息（级联删除，开事务）
func (u *AppStoreRepository) DeleteAppStoreByID(appStoreID int64) error {
	// 开启事务
	tx := u.mysqlDb.Begin()
	// 遇到 panic 回滚
	defer func() {
		if r := recover(); r != nil {
			tx.Rollback()
		}
	}()
	if tx.Error != nil {
		return tx.Error
	}

	// 删除应用主记录
	if err := u.mysqlDb.Where("id = ?", appStoreID).Delete(&model.AppStore{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	// 删除应用图片
	if err := u.mysqlDb.Where("app_id = ?", appStoreID).Delete(&model.AppImage{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	// 删除中间件关联
	if err := u.mysqlDb.Where("app_id = ?", appStoreID).Delete(&model.AppMiddle{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	// 删除对应的 Pod 组合
	if err := u.mysqlDb.Where("app_id = ?", appStoreID).Delete(&model.AppPod{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	// 删除存储关联
	if err := u.mysqlDb.Where("app_id = ?", appStoreID).Delete(&model.AppVolume{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	// 删除应用评论
	if err := u.mysqlDb.Where("app_id = ?", appStoreID).Delete(&model.AppComment{}).Error; err != nil {
		tx.Rollback()
		return err
	}

	return tx.Commit().Error
}
```

> 工程实践提示：级联删除采用「手动逐个删除」而非数据库级联，好处是可以在删除过程中插入业务逻辑，例如删除数据库记录后，通知对象存储清理磁盘上的真实图片文件，或通知其他业务系统做关联处理。

## API 速览

| 方法 | 签名 | 说明 |
| --- | --- | --- |
| `InitTable` | `() error` | 创建聚合根及所有关联子表 |
| `FindAppStoreByID` | `(int64) (*model.AppStore, error)` | 按 ID 查询，Preload 加载全部关联 |
| `CreateAppStore` | `(*model.AppStore) (int64, error)` | 创建并返回自增 ID |
| `DeleteAppStoreByID` | `(int64) error` | 事务级联删除主记录与子表 |
| `UpdateAppStore` | `(*model.AppStore) error` | 更新应用记录 |
| `FindAll` | `() ([]model.AppStore, error)` | 查询全部 |
| `AddInstallNumber` | `(int64) error` | 安装量原子自增 |
| `GetInstallNumber` | `(int64) int64` | 读取安装量 |
| `AddViewNumber` | `(int64) error` | 浏览量原子自增 |
| `GetViewNumber` | `(int64) int64` | 读取浏览量 |

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

相关度：100%。是否需要继续：是。代码是否可运行：[是]。
