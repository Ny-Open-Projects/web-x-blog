# Go PaaS 平台开发: go-micro v3 添加集群版 Consul（下）

## 纲要

- 在上一节部署好 Consul 集群的基础上，本节把 go-micro v3 服务的注册中心替换为 Consul。
- 关键依赖：`github.com/asim/go-micro/plugins/registry/consul/v3`。
- 通过 `micro.Registry(...)` 把 Consul 注册中心注入服务，启动后服务会出现在 Consul UI 的 Services 中。
- 同时演示注册中心地址的本地/容器内两种写法。

## 引入 Consul 注册中心依赖

在 go-micro v3 中，各类中间件以独立插件形式提供。Consul 注册中心插件位于：

```bash
go get github.com/asim/go-micro/plugins/registry/consul/v3
```

注意路径中的 `plugins/registry/consul/v3`，与 v2 时代的引用方式不同，务必写对版本后缀，否则 `go mod` 会拉取错误版本导致编译失败。

## 本地开发时的注册中心地址

本地开发时，Consul 运行在宿主机，地址写作 `127.0.0.1:8500`：

```go
package main

import (
	"github.com/asim/go-micro/v3"
	"github.com/asim/go-micro/v3/registry"
	"github.com/asim/go-micro/plugins/registry/consul/v3"
)

func main() {
	// 创建 Consul 注册中心，指向本地 8500 端口
	reg := consul.NewRegistry(
		registry.Addrs("127.0.0.1:8500"),
	)

	service := micro.NewService(
		micro.Name("go.micro.srv.paas"),
		micro.Registry(reg),
	)

	service.Init()

	if err := service.Run(); err != nil {
		panic(err)
	}
}
```

## 容器内 / 集群内的地址写法

当服务与 Consul 运行在同一个 docker-compose 网络中时，可以直接用 Consul 服务名（如 `consul1:8500`）代替 IP，由 Docker 内部 DNS 解析：

```go
reg := consul.NewRegistry(
	registry.Addrs("consul1:8500"),
)
```

部署到 Kubernetes 时，注册中心地址通常来自环境变量或配置文件，避免在代码里硬编码。

## 验证服务是否注册成功

1. 编译并运行服务：

```bash
go build -o srv-paas && ./srv-paas
```

2. 打开 Consul UI `http://127.0.0.1:8500`，进入 `Services` 页。
3. 刷新后能看到 `go.micro.srv.paas` 已出现在服务列表，且 `micro` 前缀的内部服务（如 `consul` 自身）也在其中，说明注册成功。

## Demo 示例

### 运行说明

- 先按 3-4 启动 Consul 集群。
- 在 base 工程根目录执行 `go mod tidy`，确保 `consul/v3` 插件已下载。
- `go run main.go` 启动服务，再去 Consul UI 验证。

### 代码说明

上面的三段代码分别演示了：依赖引入、本地地址注册、容器内地址注册。核心只有两步——`consul.NewRegistry(...)` 创建注册中心，再用 `micro.Registry(reg)` 注入服务。

### 技术点总结

- v3 的注册中心以插件引入，`registry.Addrs(...)` 指定地址。
- 本地用 `127.0.0.1:8500`，同网络用服务名，生产用环境变量。
- 注册成功后可在 Consul UI 的 `Services` 页实时查看，这是排查服务发现问题的最快手段。

相关度：100%。是否需要继续：是。代码是否可运行：是。
