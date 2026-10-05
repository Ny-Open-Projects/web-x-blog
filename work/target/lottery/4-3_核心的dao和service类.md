# Go 企业级抽奖项目: 核心的 DAO 和 Service 类

## 纲要

- DAO（Data Access Object）面向数据库，只做增删改查；Service 面向数据服务，可调用 DAO、缓存或第三方接口
- 业务逻辑层应直接依赖 Service，而不直接调用 DAO
- DAO 基础方法：`Get`、`GetAll`、`CountAll`、`Search`、`Delete`、`Update`、`Create`
- Service 基础方法与 DAO 高度一致（返回值都是面向数据模型的结果），差异出现在引入缓存或外部接口时
- 特殊方法按业务条件定义，如 `GetByIp(ip)`、`Search(uid, day)`

## DAO 与 Service 的职责边界

DAO 与 Service 是分层架构里相邻的两个角色，区别在于数据来源：

- **DAO** 只面向数据库，职责是纯粹的增删改查（CRUD）。它不关心业务，只知道如何把一条记录读出来、写进去、改掉或软删除。
- **Service** 面向数据服务。它同样对外提供数据结果，但内部可以组合多个 DAO、读写缓存、调用第三方 RPC 接口。换句话说，Service 是 DAO 的上层封装。

因此在抽奖系统的控制器（Controller）里，业务逻辑应当直接调用 Service，而不是直接触碰 DAO。这样既隔离了存储细节，也为后续加入缓存、限流、外部依赖留出了空间。

## 基础方法

两类都围绕数据模型提供一套共性方法，几乎是一个套路：

| 方法 | 作用 | 返回 |
| --- | --- | --- |
| `Get(id)` | 按主键读取一条 | 数据模型（指针） |
| `GetAll(...)` | 读取集合（常带分页） | 模型切片 `[]Model` |
| `CountAll()` | 统计总数 | `int64` |
| `Search(...)` | 带条件搜索 | 模型切片 |
| `Delete(id)` | 删除（多为软删除） | `error` |
| `Update(data, columns)` | 更新指定字段 | `error` |
| `Create(data)` | 插入一条 | `error` |

这些方法无论针对奖品、用户、中奖记录还是优惠券，命名与签名都保持一致，所以一套实现可以套用到所有实体。

## 特殊方法

除了基础方法，还会按业务条件定义专属查询。例如：

- 按 IP 查找黑名单：`GetByIp(ip string) *models.LtBlackip`
- 按用户与日期查找当日参与情况：`Search(uid, day int) []models.LtUserday`

这类方法名直接体现查询维度，调用方一看便知。

## 真实代码片段

下面是 `GiftDao` 中一组典型方法（节选自 `code/lottery/dao/gift_dao.go`），体现 DAO 的结构与基础方法实现：

```go
type GiftDao struct {
	engine *xorm.Engine
}

func NewGiftDao(engine *xorm.Engine) *GiftDao {
	return &GiftDao{engine: engine}
}

// Get 按主键读取，未命中时清空 Id 返回空对象
func (d *GiftDao) Get(id int) *models.LtGift {
	data := &models.LtGift{Id: id}
	ok, err := d.engine.Get(data)
	if ok && err == nil {
		return data
	}
	data.Id = 0
	return data
}

// GetAll 按状态、展示顺序两次排序，便于后台维护
func (d *GiftDao) GetAll() []models.LtGift {
	datalist := make([]models.LtGift, 0)
	err := d.engine.
		Asc("sys_status").
		Asc("displayorder").
		Find(&datalist)
	if err != nil {
		return datalist
	}
	return datalist
}

// Delete 软删除：仅将 sys_status 置为 1
func (d *GiftDao) Delete(id int) error {
	data := &models.LtGift{Id: id, SysStatus: 1}
	_, err := d.engine.Id(data.Id).Update(data)
	return err
}

// Update 通过 MustCols 强制更新指定字段（空值也会落库）
func (d *GiftDao) Update(data *models.LtGift, columns []string) error {
	_, err := d.engine.Id(data.Id).MustCols(columns...).Update(data)
	return err
}

func (d *GiftDao) Create(data *models.LtGift) error {
	_, err := d.engine.Insert(data)
	return err
}
```

`BlackipDao` 则展示了一个按条件查询的特殊方法 `GetByIp`，使用 `Where` + `Limit(1)` 并以切片指针接收结果：

```go
// GetByIp 根据 IP 获取黑名单信息
func (d *BlackipDao) GetByIp(ip string) *models.LtBlackip {
	datalist := make([]models.LtBlackip, 0)
	err := d.engine.
		Where("ip=?", ip).
		Desc("id").
		Limit(1).
		Find(&datalist)
	if err != nil || len(datalist) < 1 {
		return nil
	}
	return &datalist[0]
}
```

注意：`Find` 的目标参数必须传切片指针（`&datalist`），否则 XORM 无法回填数据。

对应地，`GiftService` 在接口层只依赖 DAO，把调用透传出去（节选自 `code/lottery/services/gift_service.go`）：

```go
type GiftService interface {
	GetAll(useCache bool) []models.LtGift
	CountAll() int64
	Get(id int, useCache bool) *models.LtGift
	Delete(id int) error
	Update(data *models.LtGift, columns []string) error
	Create(data *models.LtGift) error
}

type giftService struct {
	dao *dao.GiftDao
}

func NewGiftService() GiftService {
	return &giftService{dao: dao.NewGiftDao(datasource.InstanceDbMaster())}
}
```

## API 速览

- `dao.NewGiftDao(engine *xorm.Engine) *GiftDao`：构造 DAO，注入 XORM 引擎
- `(*GiftDao).Get(id int) *models.LtGift`：主键查询
- `(*GiftDao).GetAll() []models.LtGift`：全量查询（双排序）
- `(*GiftDao).Update(data, columns) error`：配合 `MustCols` 强制更新指定列
- `(*GiftDao).GetByIp(ip string) *models.LtBlackip`：条件查询示例
- `services.NewGiftService() GiftService`：构造 Service，内部持有 DAO 与数据源

## Demo 示例

下面给出一个最小可运行的 DAO 定义示例（以简化版奖品模型演示基础方法，需引入 `github.com/go-xorm/xorm` 与对应模型）：

```go
package main

import (
	"fmt"

	"github.com/go-xorm/xorm"
	_ "github.com/go-sql-driver/mysql"
)

// Gift 简化模型，仅保留演示字段
type Gift struct {
	Id    int    `xorm:"pk autoincr"`
	Title string `xorm:"varchar(255)"`
}

type GiftDao struct {
	engine *xorm.Engine
}

func NewGiftDao(engine *xorm.Engine) *GiftDao {
	return &GiftDao{engine: engine}
}

func (d *GiftDao) Get(id int) *Gift {
	data := &Gift{Id: id}
	ok, _ := d.engine.Get(data)
	if !ok {
		return &Gift{}
	}
	return data
}

func (d *GiftDao) Create(g *Gift) error {
	_, err := d.engine.Insert(g)
	return err
}

func main() {
	engine, err := xorm.NewEngine("mysql",
		"root:password@tcp(127.0.0.1:3306)/lottery?charset=utf8")
	if err != nil {
		panic(err)
	}
	dao := NewGiftDao(engine)
	g := &Gift{Title: "iPhone"}
	if err := dao.Create(g); err != nil {
		panic(err)
	}
	fmt.Println("created gift id =", dao.Get(g.Id).Id)
}
```

运行说明：准备一张 `gift` 表（含 `id` 自增主键与 `title` 字段），安装 `go-xorm/xorm` 与 `go-sql-driver/mysql` 后执行 `go run main.go`。

代码说明：示例演示了 DAO 的典型结构——持有一个 `*xorm.Engine`，通过 `NewXxxDao` 注入；`Get` 用主键回填、`Create` 用 `Insert`。这与项目中 `GiftDao` 的写法完全一致。

技术点总结：DAO 与 Service 分层让存储细节与业务逻辑解耦；DAO 只做 CRUD，Service 在上层组合 DAO/缓存/外部接口；基础方法统一命名、特殊方法按查询维度命名；XORM 的 `Find` 必须传切片指针，`Update` 配合 `MustCols` 才能强制更新空值字段。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/dao/user_dao.go`
- `code/lottery/services/code_service.go`
- `code/lottery/services/userday_service.go`
- `code/lottery/dao/userday_dao.go`
- `code/lottery/dao/blackip_dao.go`
- `code/lottery/services/result_service.go`
- `code/lottery/dao/code_dao.go`
- `code/lottery/dao/result_dao.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
