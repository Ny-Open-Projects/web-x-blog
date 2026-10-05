# Go 企业级抽奖项目: 实现 IndexController

## 纲要

- MVC 控制器：基于 Iris 的 MVC 模式实现 `IndexController`，承载前台首页与公开接口。
- 上下文与服务注入：控制器内嵌 `iris.Context` 获取请求上下文，并持有 `User/Gift/Code/Result/Userday/Blackip` 等服务的引用，由路由层注入。
- 首页动作：`Get()` 返回欢迎页面，并给出进入抽奖的链接。
- 奖品接口：`GetGifts()` 返回所有“正常状态”的奖品列表（JSON）。
- 中奖榜单：`GetNewprize()` 返回最近的中奖记录，用于大转盘活动展示“活动仍在进行”的氛围。

## IndexController 定义

控制器遵循 MVC 约定：方法名 `GetXxx` 自动映射为 `GET /xxx` 路由；控制器需要的服务在路由注册时通过 `Register` 注入（见下一节）。`Ctx` 通过匿名嵌入 `iris.Context` 获得请求上下文：

```go
package controllers

import (
	"github.com/kataras/iris"
	"imooc.com/lottery/services"
)

type IndexController struct {
	Ctx             iris.Context
	ServiceUser     services.UserService
	ServiceGift     services.GiftService
	ServiceCode     services.CodeService
	ServiceResult   services.ResultService
	ServiceUserday  services.UserdayService
	ServiceBlackip  services.BlackipService
}
```

> 服务字段使用大写导出名，因为路由层需要从外部注入；若写成小写则外部不可见。

## 首页动作

`Get()` 不带后缀，对应根路径 `GET /`。它直接返回一段 HTML 字符串，并提供一个跳转到抽奖页面的链接：

```go
// http://localhost:8080/
func (c *IndexController) Get() string {
	c.Ctx.Header("Content-Type", "text/html")
	return "welcome to Go抽奖系统，<a href='/public/index.html'>开始抽奖</a>"
}
```

## 获取奖品列表

`GetGifts()` 对应 `GET /gifts`。它从礼品服务取出全部奖品，过滤掉非正常状态（`SysStatus != 0`）的奖品后再返回。Iris 会自动把返回的 `map[string]interface{}` 序列化为 JSON：

```go
// http://localhost:8080/gifts
func (c *IndexController) GetGifts() map[string]interface{} {
	rs := make(map[string]interface{})
	rs["code"] = 0
	rs["msg"] = ""
	datalist := c.ServiceGift.GetAll(true)
	list := make([]models.LtGift, 0)
	for _, data := range datalist {
		// 仅返回正常状态的奖品
		if data.SysStatus == 0 {
			list = append(list, data)
		}
	}
	rs["gifts"] = list
	return rs
}
```

## 最新中奖列表

`GetNewprize()` 对应 `GET /newprize`。它返回最近的中奖记录，让前端大转盘页面能实时展示“不断有人中奖”，从而提升参与感：

```go
// http://localhost:8080/newprize
func (c *IndexController) GetNewprize() map[string]interface{} {
	rs := make(map[string]interface{})
	rs["code"] = 0
	rs["msg"] = ""
	gifts := c.ServiceGift.GetAll(true)
	giftIds := []int{}
	for _, data := range gifts {
		// 虚拟券或实物奖才进入外部榜单展示
		if data.Gtype > 1 {
			giftIds = append(giftIds, data.Id)
		}
	}
	list := c.ServiceResult.GetNewPrize(50, giftIds)
	rs["prize_list"] = list
	return rs
}
```

返回结构与 `GetGifts` 一致：统一的 `code` / `msg` 加上具体业务数据，便于前端统一处理。

## 接口约定小结

| 方法 | 路由 | 说明 |
| --- | --- | --- |
| `Get()` | `GET /` | 首页欢迎语 + 抽奖入口 |
| `GetGifts()` | `GET /gifts` | 正常状态奖品列表 |
| `GetNewprize()` | `GET /newprize` | 最近中奖榜单 |

## API 速览

- 控制器方法命名即路由：`GetXxx` → `GET /xxx`，`PostXxx` → `POST /xxx`。
- 返回 `map[string]interface{}` 时，Iris 自动 JSON 序列化。
- 服务通过路由层 `Register(...)` 注入，控制器只声明、不负责创建。

## Demo 示例

运行说明：以下为控制器关键逻辑的精简可运行示例（根据讲稿逻辑补充，依赖 Iris MVC）。

```go
package main

import (
	"github.com/kataras/iris/v12"
	"github.com/kataras/iris/v12/mvc"
)

type IndexController struct {
	Ctx iris.Context
}

// GET /
func (c *IndexController) Get() string {
	c.Ctx.Header("Content-Type", "text/html")
	return "welcome to Go抽奖系统，<a href='/public/index.html'>开始抽奖</a>"
}

// GET /gifts
func (c *IndexController) GetGifts() map[string]interface{} {
	return map[string]interface{}{
		"code":  0,
		"msg":   "",
		"gifts": []string{"实物大奖", "优惠券", "谢谢参与"},
	}
}

func main() {
	app := iris.New()
	m := mvc.New(app)
	m.Handle(new(IndexController))
	app.Run(iris.Addr(":8080"))
}
```

代码说明：展示 Iris MVC 中“方法名即路由”的约定与 JSON 自动序列化。

技术点总结：Iris MVC 用命名约定大幅减少路由样板代码；控制器内嵌 `Context` 与注入式服务让每个 Action 专注业务逻辑；统一返回结构（`code/msg/data`）为前端提供一致的解析契约。

## 总结

相关度：100%。是否需要继续：是。代码是否可运行：否。
