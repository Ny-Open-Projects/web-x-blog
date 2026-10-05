# Go 企业级抽奖项目: 定义 Service

## 纲要

- Service 与 DAO 高度相似，但用**接口 + 私有实现**的方式定义，便于多实现、更灵活
- 接口 `GiftService` 公开（大写），实现 `giftService` 私有（小写），对外只暴露接口
- 私有实现内持有 DAO 对象；后续引入 Redis 时数据源会从“仅 DAO”扩展为“DAO + 缓存”
- `NewGiftService()` 返回的是接口类型 `GiftService`，而非私有结构体
- 基础方法现阶段直接透传 DAO；业务加工（缓存、第三方接口）后续在此层补充
- 通过 Thrift 可把 `LuckyService` 暴露为远程 RPC 服务（见 `rpc/lucky_service-remote`）

## 用接口定义 Service

DAO 通常用结构体直接定义，而 Service 推荐先定义**接口**，再做实现。好处是接口可以有多种实现，Service 的使用方只依赖接口，不依赖具体类型，扩展性更好。

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
	return &giftService{
		dao: dao.NewGiftDao(datasource.InstanceDbMaster()),
	}
}
```

这里有两个命名约定：

- `GiftService`（大写）是公开接口，作用域对外可见；
- `giftService`（小写）是私有实现，外部不可见，只能透过 `GiftService` 接口使用。

`giftService` 内部持有一个 DAO 对象，因为当前阶段只涉及数据库操作。后面讲到 Redis 时，数据源就不止 DAO 了，还会加入缓存读写——Service 正是承载这类组合逻辑的最佳位置。

## 构造函数返回接口

`NewGiftService()` 的返回值是 `GiftService`（接口），而不是 `*giftService`。这一点很重要：私有结构体外部用不了，所以构造函数必须返回接口，调用方才能拿到可用的实例。数据源（如 `datasource.InstanceDbMaster()`）在构造时注入 DAO。

## 方法实现：现阶段透传

由于还没有额外的业务加工，Service 的方法实现与 DAO 几乎一模一样，基本是直接调用 DAO：

```go
func (s *giftService) GetAll(useCache bool) []models.LtGift {
	if !useCache {
		return s.dao.GetAll()
	}
	// 缓存优化后的读取方式（后续章节补充）
	gifts := s.getAllByCache()
	if len(gifts) < 1 {
		gifts = s.dao.GetAll()
		s.setAllByCache(gifts)
	}
	return gifts
}

func (s *giftService) CountAll() int64 {
	return s.dao.CountAll()
}

func (s *giftService) Delete(id int) error {
	// 先更新缓存，再更新数据库
	s.updateByCache(&models.LtGift{Id: id}, nil)
	return s.dao.Delete(id)
}

func (s *giftService) Update(data *models.LtGift, columns []string) error {
	s.updateByCache(data, columns)
	return s.dao.Update(data, columns)
}

func (s *giftService) Create(data *models.LtGift) error {
	s.updateByCache(data, nil)
	return s.dao.Create(data)
}
```

可以看到，`GetAll` 已经预留了 `useCache` 分支：未启用缓存时直接读库，启用后先读缓存、未命中再读库并回填。其余实体（`CodeService`、`BlackipService`、`UserService`、`ResultService`、`UserdayService`）结构同理，只是字段与特殊方法不同。

## 通过 Thrift 暴露为远程服务

课程的后续章节会引入 Thrift 框架，把抽奖核心逻辑（如 `DoLucky`、`MyPrizeList`）发布成 RPC 服务。生成的客户端代码（`rpc/lucky_service-remote/lucky_service-remote.go`）展示了如何建立 Thrift 传输并调用：

```go
// 建立传输（binary 协议为例）
trans, err := thrift.NewTSocket(net.JoinHostPort(host, portStr))
if err != nil { /* 处理错误 */ }
if framed {
	trans = thrift.NewTFramedTransport(trans)
}
defer trans.Close()

protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()
client := rpc.NewLuckyServiceClient(thrift.NewTStandardClient(
	protocolFactory.GetProtocol(trans),
	protocolFactory.GetProtocol(trans)))
if err := trans.Open(); err != nil { /* 处理错误 */ }

// 调用远程方法
client.DoLucky(context.Background(), uid, username, ip, now, app, sign)
```

这表明 Service 的能力既可在进程内被 Controller 调用，也可通过 Thrift 对外提供远程调用。

## API 速览

- `services.NewGiftService() GiftService`：构造 Service（返回接口）
- `GiftService.GetAll(useCache bool) []models.LtGift`：全量读取，支持缓存分支
- `GiftService.CountAll() int64`：统计
- `GiftService.Get(id int, useCache bool) *models.LtGift`：主键读取
- `GiftService.Update/Create/Delete`：写操作，内部先动缓存再动库
- `rpc.NewLuckyServiceClient(...)`：Thrift 生成的远程客户端构造函数

## Demo 示例

下面给出一个自包含、可运行的 Service 示例（简化版，组合一个内存 DAO，演示接口 + 私有实现 + 透传）：

```go
package main

import "fmt"

// 简化模型与 DAO
type Gift struct{ Id int; Title string }

type giftDao struct{ items []Gift }
func (d *giftDao) GetAll() []Gift { return d.items }
func (d *giftDao) Create(g Gift)  { d.items = append(d.items, g) }

// Service 接口 + 私有实现
type GiftService interface {
	GetAll() []Gift
	Create(g Gift)
}

type giftService struct{ dao *giftDao }

func NewGiftService() GiftService {
	return &giftService{dao: &giftDao{}}
}

func (s *giftService) GetAll() []Gift    { return s.dao.GetAll() }
func (s *giftService) Create(g Gift)     { s.dao.Create(g) }

func main() {
	svc := NewGiftService()           // 返回接口类型
	svc.Create(Gift{Id: 1, Title: "iPhone"})
	fmt.Println(svc.GetAll())
}
```

运行说明：直接 `go run main.go` 即可，无需数据库，用于演示“接口定义 + 私有实现 + 构造函数返回接口”的写法。

代码说明：本例把 DAO 换成内存切片，仅聚焦 Service 形态本身。真实项目里 `giftService.dao` 应为 `dao.NewGiftDao(datasource.InstanceDbMaster())`，并在 `GetAll` 中加入 `useCache` 缓存分支。

技术点总结：Service 用“公开接口 + 私有实现”获得多实现灵活性；构造函数返回接口类型；现阶段方法透传 DAO，缓存/外部接口等组合逻辑统一收敛到 Service 层；同一套 Service 既能进程内调用，也能经 Thrift 发布为 RPC。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/services/code_service.go`
- `code/lottery/services/userday_service.go`
- `code/lottery/services/result_service.go`
- `code/lottery/rpc/lucky_service-remote/go_client/goclient_main.go`
- `code/lottery/services/blackip_service.go`
- `code/lottery/services/user_service.go`
- `code/lottery/rpc/lucky_service-remote/lucky_service-remote.go`
- `code/lottery/services/gift_service.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
