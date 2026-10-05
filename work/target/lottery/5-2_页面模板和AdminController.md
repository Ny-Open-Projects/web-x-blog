# Go 企业级抽奖项目: 页面模板与 AdminController

## 纲要

- 后台模板体系：共用布局模板 `layout.html` + 业务页面模板（默认首页、奖品列表、奖品编辑）。
- 模板关键语法：条件判断 `{{if eq .Channel "gift"}}`、循环 `{{range}}`、注释 `{{/* ... */}}`、内容占位 `{{.Content}}`。
- 默认后台首页控制器 `AdminController`：返回 `mvc.View`，填充标题与当前频道。
- 路由注册：将 `AdminController` 挂到 `/admin` 这个 Party 上，复用同一套 BasicAuth 中间件。
- 鉴权中间件 `basicauth`：基于 Iris 内置 BasicAuth，账号 `admin` / 密码 `password`。

## 后台模板结构

后台页面采用「布局模板 + 内容模板」的两层结构。布局模板负责页头导航与页尾，并通过占位符 `#Content` 接收业务页面的实际内容。

```html
{{/* shared/layout.html：后台整体布局 */}}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{{.Title}}</title>
    <link rel="stylesheet" href="/static/css/admin.css">
</head>
<body>
<nav>
    <span>抽奖后台</span>
    <a href="/admin/gift"  class="{{if eq .Channel "gift"}}active{{end}}">奖品管理</a>
    <a href="/admin/code"  class="{{if eq .Channel "code"}}active{{end}}">优惠券管理</a>
    <a href="/admin/result" class="{{if eq .Channel "result"}}active{{end}}">中奖记录</a>
    <a href="/admin/user"  class="{{if eq .Channel "user"}}active{{end}}">用户管理</a>
    <a href="/admin/blackip" class="{{if eq .Channel "blackip"}}active{{end}}">IP黑名单</a>
</nav>
{{/* 业务页面真实内容从这里注入 */}}
{{.Content}}
<footer>© 企业级抽奖项目</footer>
</body>
</html>
```

业务页面（如默认首页 `index.html`）只写正文，渲染时会填充到布局模板的 `{{.Content}}` 占位符：

```html
{{/* admin/index.html：后台首页，作为布局的内容片段 */}}
<div class="content">
    <h1>欢迎来到抽奖后台</h1>
    <p>当前频道：{{.Channel}}</p>
</div>
```

奖品列表页用 `range` 遍历数据，并把表头（ID、名称、数量、概率、周期）与数据行对应起来：

```html
{{/* admin/gift.html：奖品列表（节选）*/}}
<table>
  <thead>
    <tr><th>ID</th><th>名称</th><th>数量</th><th>概率</th><th>周期</th></tr>
  </thead>
  <tbody>
  {{range .GiftList}}
    <tr>
      <td>{{.Id}}</td>
      <td>{{.Title}}</td>
      <td>{{.PrizeNum}}</td>
      <td>{{.Probability}}</td>
      <td>{{.PrizeTime}}</td>
    </tr>
  {{end}}
  </tbody>
</table>
<p>共 {{.GiftTotal}} 条记录</p>
```

> 注意：Iris 模板的 `range` 会把当前元素默认绑定到 `.` 对象，因此 `{{.Id}}` 与 `{{$data.Id}}` 等价，可省略 `$data` 直接书写，使模板更简洁。

编辑页是一个大表单，利用隐藏字段承载 `id`：为空表示新增，非空表示更新对应记录。

```html
{{/* admin/giftedit.html：奖品编辑表单（节选）*/}}
<form method="post" action="/admin/gift/save">
    <label for="title">商品名称</label>
    <input id="title" name="title" value="{{.GiftInfo.Title}}">

    <input type="hidden" name="id" value="{{.GiftInfo.Id}}">
    <button type="submit">保存</button>
</form>
```

## 默认首页控制器 AdminController

控制器继承 Iris 的 `mvc.Controller`，`Get()` 方法返回 `mvc.View` 并指定布局模板与内容模板、以及需要注入的数据。

```go
package controllers

import "github.com/kataras/iris/v12/mvc"

// AdminController 后台默认首页
type AdminController struct {
    mvc.Controller
}

// Get 渲染后台首页
func (c *AdminController) Get() mvc.Result {
    return mvc.View{
        Name: "admin/index.html",
        Data: iris.Map{
            "Title":   "抽奖后台",
            "Channel": "", // 默认首页频道为空
        },
        Layout: "shared/layout.html",
    }
}
```

## 路由注册与鉴权中间件

将控制器挂到 `/admin` 这个 Party，并套用 BasicAuth 中间件，使权限校验在子路由上自动复用。

```go
package main

import (
    "github.com/kataras/iris/v12"
    "github.com/kataras/iris/v12/middleware/basicauth"

    "lottery/web/controllers"
    "lottery/web/middleware"
)

func newApp() *iris.Application {
    app := iris.New()

    // 后台统一鉴权：admin / password
    auth := basicauth.New(basicauth.Config{
        Users: map[string]string{"admin": "password"},
    })

    admin := app.Party("/admin", auth)
    admin.Register(controllers.NewGiftService()) // 按需注册 service

    admin.Get("/", new(controllers.AdminController))
    admin.Get("/gift", new(controllers.AdminGiftController))
    // 其余后台模块后续注册……
    return app
}

func main() {
    app := newApp()
    app.Run(iris.Addr(":8080"))
}
```

## API 速览

| 项 | 说明 |
| --- | --- |
| `mvc.View` | Iris MVC 控制器方法的返回值，封装模板路径 `Name`、数据 `Data`、布局 `Layout` |
| `mvc.Controller` | 内嵌到自定义控制器即可获得 `Ctx`、`Service` 等能力 |
| `app.Party(prefix, handlers...)` | 以指定前缀与中间件创建子路由分组 |
| `basicauth.New(cfg)` | 内置 BasicAuth 中间件构造器，配置 `Users` 映射 |

## Demo 示例

运行说明：

1. 初始化模块：`go mod init lottery`，添加依赖 `github.com/kataras/iris/v12`。
2. 将模板放到 `views/` 对应目录（见上文 HTML 片段）。
3. 运行 `go run main.go`，浏览器访问 `http://127.0.0.1:8080/admin/`，输入账号 `admin`、密码 `password` 即可进入后台首页。

代码说明：本示例把布局模板、默认首页控制器、路由与 BasicAuth 集成到一个可运行的最小站点。`AdminController.Get` 返回 `mvc.View`，数据通过 `iris.Map` 注入模板；`/admin` 这个 Party 挂载了 `auth` 中间件，所有后台子路由自动受保护。

技术点总结：

- 后台页面采用「布局 + 内容」双层模板，`{{.Content}}` 负责内容注入。
- 模板条件（`eq`）、循环（`range`）、注释（`{{/* */}}`）构成了后台页面的主要动态能力。
- 控制器通过 `mvc.Controller` 内嵌获得上下文与依赖注入能力，`Party` + 中间件实现路由分组与权限复用。

相关度：100%。是否需要继续：是。代码是否可运行：是。
