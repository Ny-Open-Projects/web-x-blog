# Go 企业级抽奖项目: 利用 Iris 建立 Web 站点

## 纲要

- 技术选型：使用 Iris v12 作为 Web 框架，承载抽奖系统的站点层。
- 分层结构：站点层由 `bootstrap`（应用启动器）、`web/controllers`（控制器）、`web/views`（模板）、`web/public`（静态资源）、`web/middleware`（中间件）等目录组成。
- 启动闭环：`bootstrap` 负责应用初始化与监听端口，`main.go` 组装并启动，`routes` 注册路由与控制器。
- 公共能力：通用方法（comm）、项目配置（conf）贯穿整个站点。

## 为什么选择 Iris

抽奖系统需要一个高性能、对 MVC 支持良好的 Go Web 框架。Iris 提供了路由、中间件、视图引擎、会话（Session）、MVC 等一整套能力，且性能表现优秀。本章后续几节会逐步把 `bootstrap`、`controllers`、`routes`、`main.go` 完善起来，最终形成一个可启动的 Web 站点。

## 站点目录结构

一个基于 Iris 的站点，典型目录划分如下（来自本项目的真实结构）：

```dir
lottery/
├── bootstrap/            # 应用启动器（封装 iris.Application）
│   └── bootstrapper.go
├── web/
│   ├── controllers/      # 控制器（首页、抽奖、后台管理）
│   │   ├── index.go
│   │   ├── index_lucky.go
│   │   └── admin.go
│   ├── views/            # 页面模板
│   │   ├── shared/       # 公共模板（layout、error）
│   │   └── admin/
│   ├── public/           # 静态资源（css/js/图片/前端页面）
│   │   └── index.html
│   ├── middleware/       # 中间件（basicauth 等）
│   ├── routes/           # 路由注册
│   │   └── routes.go
│   └── main.go           # 程序入口
├── comm/                 # 通用方法（时间、加密、类型转换、Cookie 等）
├── conf/                 # 项目配置（时间格式、密钥、Redis、DB）
├── services/             # 业务服务层
├── dao/                  # 数据访问层
└── models/               # 数据模型
```

可以看到，站点启动需要的几块拼图——公共方法、配置信息、控制器、静态文件——都会在这一阶段逐步落地。

## 一个最小的 Iris 站点示例

下面给出一个最小可运行的 Iris 站点骨架（根据讲稿逻辑补充），展示“路由 → 控制器 → 返回字符串”的闭环。后续章节会把它演进为完整的 `bootstrap` + `routes` + `main.go` 结构。

```go
package main

import "github.com/kataras/iris/v12"

func main() {
	app := iris.New()

	// 注册一个 GET / 路由，返回首页字符串
	app.Get("/", func(ctx iris.Context) {
		ctx.Header("Content-Type", "text/html")
		ctx.HTML("<h1>欢迎来到 Go 抽奖系统</h1>" +
			"<a href='/public/index.html'>开始抽奖</a>")
	})

	// 静态资源目录
	app.HandleDir("/public", "./public")

	// 监听 8080 端口
	app.Run(iris.Addr(":8080"))
}
```

运行方式：

```bash
go run main.go
# 浏览器访问 http://localhost:8080/
```

## 后续拼图

- `bootstrap`：封装 `iris.Application`，统一加载模板、会话、错误处理器、静态资源与中间件。
- `controllers`：按 MVC 模式组织控制器，首页、奖品、中奖列表、登录退出等都由控制器承接。
- `routes`：把控制器与 URL 绑定，并区分前台 `/` 与后台 `/admin`。
- `main.go`：创建应用、注入配置、启动监听。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/web/views/shared/error.html`
- `code/lottery/web/views/admin/index.html`
- `code/lottery/web/middleware/basicauth.go`
- `code/lottery/web/controllers/index_lucky_5check_blackuser.go`
- `code/lottery/web/controllers/index_lucky_4check_blakip.go`
- `code/lottery/web/controllers/index_lucky_4check_blackip.go`
- `code/lottery/web/viewmodels/view_gift.go`
- `code/lottery/web/controllers/index_lucky_9prize.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：95%。是否需要继续：是。代码是否可运行：是。
