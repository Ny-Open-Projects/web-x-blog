# Go 企业级抽奖项目: 定义 DAO

## 纲要

- 以 `GiftDao` 为样板，逐个实现 DAO 基础方法：`Get`、`GetAll`、`CountAll`、`Delete`、`Update`、`Create`
- `Get` 未命中时清空 `Id` 再返回，避免调用方误判
- `GetAll` 用 `Asc("sys_status")` + `Asc("displayorder")` 两次排序，保证后台展示有序
- `Delete` 采用软删除：仅把 `sys_status` 置为 1，不做物理删除
- `Update` 配合 `MustCols(columns...)` 强制更新指定字段，空值也会落库
- 其余五个实体（User、Userday、Blackip、Code、Result）通过拷贝 `GiftDao` 再改结构名与差异字段实现
- `BlackipDao` 提供特殊方法 `GetByIp`，用 `Where` + `Limit(1)` + 切片指针接收

## 定义结构体与构造函数

DAO 本质就是一个持有 XORM 引擎的结构体，相当于面向对象里的“类”。以奖品为例：

```go
type GiftDao struct {
	engine *xorm.Engine
}

func NewGiftDao(engine *xorm.Engine) *GiftDao {
	return &GiftDao{engine: engine}
}
```

`NewGiftDao` 接收一个 `*xorm.Engine`（数据库引擎），返回 DAO 实例，后续所有方法都复用这一引擎。

## Get：主键查询与空值约定

```go
func (d *GiftDao) Get(id int) *models.LtGift {
	data := &models.LtGift{Id: id}
	ok, err := d.engine.Get(data)
	if ok && err == nil {
		return data
	} else {
		data.Id = 0
		return data
	}
}
```

`engine.Get(data)` 会按 `Id` 去对应数据表查出记录并回填到 `data`。这里有个细节：查询未命中时要把 `data.Id` 清为 0 再返回。原因是在构造 `data` 时已经给 `Id` 赋了值，如果不清空，调用方会拿到一个“有 Id 但其余字段全空”的对象，从而误以为查到了数据。统一约定“Id 为 0 表示不存在”，调用方判断更可靠。

## GetAll：两次排序

```go
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
```

注意 `Columns` 用的是数据库字段名（小写 `sys_status`、`displayorder`），不是模型里的大写字段名。做两次排序的原因：

1. 先按 `sys_status` 升序，让“正常（0）”的奖品排在前面，“删除（1）”的沉到后面；
2. 再按 `displayorder` 升序，让转盘上顺序靠前的奖品在前。

这样后台维护与展示顺序更清晰。返回的 `datalist` 用切片（`slice`）承载，先 `make` 并设长度为 0，再交给 `Find` 填充。

## CountAll：统计总数

```go
func (d *GiftDao) CountAll() int64 {
	num, err := d.engine.Count(&models.LtGift{})
	if err != nil {
		return 0
	}
	return num
}
```

统计类数字统一用 `int64`。只要把模型实例传给 `Count`，XORM 就能定位到对应表。

## Delete：软删除

```go
func (d *GiftDao) Delete(id int) error {
	data := &models.LtGift{Id: id, SysStatus: 1}
	_, err := d.engine.Id(data.Id).Update(data)
	return err
}
```

项目要求不做物理删除，所以 `Delete` 实际是把 `sys_status` 改为 1（删除态），再用 `Id(...).Update(...)` 落地。对外接口仍是 `Delete`，调用方无需关心底层是硬删还是软删。

## Update：MustCols 强制更新

```go
func (d *GiftDao) Update(data *models.LtGift, columns []string) error {
	_, err := d.engine.Id(data.Id).MustCols(columns...).Update(data)
	return err
}
```

这是一个容易踩坑的点。XORM 默认的 `Update` 行为是：如果某个字段为零值（如空字符串、0），就跳过不更新。因此当我们确实想把某个字段更新为空时，必须显式传 `MustCols(columns...)` 强制更新这些列。例如标题设为空，若不加 `MustCols`，该字段不会同步到数据库；加上后空值也会强制落库。

## Create：插入

```go
func (d *GiftDao) Create(data *models.LtGift) error {
	_, err := d.engine.Insert(data)
	return err
}
```

只是简单地把模型对象 `Insert` 进库。

## 复制到其他实体

其余五个 DAO（`UserDao`、`UserdayDao`、`CodeDao`、`ResultDao`、`BlackipDao`）结构高度相似，做法是把 `GiftDao` 复制一份，把 `Gift` 相关类型整体替换为对应实体类型，再改差异点即可，无需从头敲。例如 `CodeDao` 排序改为按 `id` 降序，`BlackipDao` 则需按 IP 而非主键查询：

```go
// GetByIp 根据 IP 获取黑名单，使用 Where 条件 + Limit(1)
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

要点：`Find` 的目标一定是切片指针（`&datalist`），否则回填时会报错；条件查询用 `Where("ip=?", ip)`，结果不足一条时返回 `nil`。

## API 速览

- `NewGiftDao(engine) *GiftDao` / `NewBlackipDao(engine) *BlackipDao` 等同构构造函数
- `(*GiftDao).Get(id int) *models.LtGift`：主键查询，未命中返回 `Id=0`
- `(*GiftDao).GetAll() []models.LtGift`：双排序全量查询
- `(*GiftDao).CountAll() int64`：总数统计
- `(*GiftDao).Delete(id int) error`：软删除（置 `sys_status=1`）
- `(*GiftDao).Update(data, columns []string) error`：配合 `MustCols` 强制更新
- `(*GiftDao).Create(data) error`：插入
- `(*BlackipDao).GetByIp(ip string) *models.LtBlackip`：条件查询特殊方法

## Demo 示例

下面以 `GiftDao` 为基础，演示一个可运行的 DAO（需 MySQL 与对应表，依赖 `xorm`）：

```go
package main

import (
	"fmt"

	"github.com/go-xorm/xorm"
	_ "github.com/go-sql-driver/mysql"
)

type LtGift struct {
	Id         int
	Title      string
	SysStatus  int
	Displayorder int
}

func (t LtGift) TableName() string { return "lt_gift" }

type GiftDao struct {
	engine *xorm.Engine
}

func NewGiftDao(engine *xorm.Engine) *GiftDao { return &GiftDao{engine: engine} }

func (d *GiftDao) Get(id int) *LtGift {
	data := &LtGift{Id: id}
	ok, _ := d.engine.Get(data)
	if !ok {
		return &LtGift{}
	}
	return data
}

func (d *GiftDao) GetAll() []LtGift {
	list := make([]LtGift, 0)
	d.engine.Asc("sys_status").Asc("displayorder").Find(&list)
	return list
}

func (d *GiftDao) Delete(id int) error {
	data := &LtGift{Id: id, SysStatus: 1}
	_, err := d.engine.Id(data.Id).Update(data)
	return err
}

func main() {
	engine, _ := xorm.NewEngine("mysql", "root:password@tcp(127.0.0.1:3306)/lottery?charset=utf8")
	dao := NewGiftDao(engine)
	fmt.Println("gifts:", dao.GetAll())
	_ = dao.Delete(1)
}
```

运行说明：建表 `lt_gift(id, title, sys_status, displayorder)`，`go run main.go` 即可查看全量列表并执行软删除。

代码说明：示例完整呈现了“构造 DAO → 注入引擎 → 调用基础方法”的闭环，和项目中的 `GiftDao` 一一对应。

技术点总结：DAO 用结构体持有 XORM 引擎，基础方法统一命名；`Get` 以 `Id==0` 表示空、`GetAll` 用数据库字段名做双排序、`Delete` 用软删除、`Update` 用 `MustCols` 处理空值、`Find` 必须传切片指针；多实体 DAO 用拷贝改类型的方式快速产出。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/dao/user_dao.go`
- `code/lottery/dao/userday_dao.go`
- `code/lottery/dao/blackip_dao.go`
- `code/lottery/dao/code_dao.go`
- `code/lottery/dao/result_dao.go`
- `code/lottery/dao/gift_dao.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
