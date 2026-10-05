# Go PaaS 平台开发: cap-tool 代码目录生成与 proto 文件生成

## 纲要

- cap-tool：课程定制的命令行脚手架，基于 Cobra 实现，用于一键生成微服务标准目录与基础代码
- 以 Docker 镜像 `cap1573/cap-tool` 分发，通过 `docker run` 调用，无需本机安装 Go 工具链
- 生成命令：`docker run --rm -v $(pwd):$(pwd) -w $(pwd) -e icode=UID cap1573/cap-tool new <仓库地址>`
- 服务名从仓库路径末段自动提取（如 `github.com/xxx/user` → 服务名 `user`）
- proto 代码生成：`make proto` 借助 `cap1573/cap-v3` 镜像把 `.proto` 编译为 Go 代码
- 配套模板：`proto.go`（接口定义）、`makefile.go`、`docker.go`（Dockerfile）、`plugin.go`、`filebeat.go`、`.gitignore`

## cap-tool 是什么

cap-tool 是课程作者封装的脚手架工具，核心目的是把「创建目录 + 写基础代码」这类重复劳动自动化。它的实现要点：

- 使用 `github.com/spf13/cobra` 提供子命令，使用 `github.com/spf13/viper` 读取配置
- 内置若干模板（Go 字符串常量），按仓库名渲染出标准工程
- 打包为 Docker 镜像分发，调用方只需装好 Docker 即可使用

> 注：cap-tool 源码含课程平台防盗校验，未公开；下方展示的是它生成产物的真实模板，可直接作为自己脚手架的参考。

## 工程入口

工具的 `main.go` 仅负责启动 Cobra 根命令：

```go
package main

import (
	"github.com/Cap1573/cap-tool/cmd"
)

func main() {
	cmd.Execute()
}
```

其 `go.mod` 声明了模块路径与关键依赖：

```go
module github.com/Cap1573/cap-tool

go 1.16

require (
	github.com/spf13/cobra v1.2.1
	github.com/spf13/viper v1.8.1
	github.com/xlab/treeprint v1.1.0
)
```

子命令在 `cmd` 包中注册，对外提供三类生成能力：

```go
// cmd/new.go（节选）
var new = &cobra.Command{
	Use:   "new",
	Short: "自动生成 Service 目录",
	Args: func(cmd *cobra.Command, args []string) error {
		if len(args) < 1 {
			return errors.New("请输入项目名称！")
		}
		return nil
	},
	Run: func(cmd *cobra.Command, args []string) {
		new2.NewServiceProject(cmd, args)
	},
}

func init() {
	rootCmd.AddCommand(new)
	rootCmd.AddCommand(newService)
	rootCmd.AddCommand(createApi)
}
```

## 用 cap-tool 生成目录

在目标工作目录下执行（`<仓库地址>` 决定生成的服务名）：

```bash
docker run --rm \
  -v $(pwd):$(pwd) \
  -w $(pwd) \
  -e icode=YOUR_UID \
  cap1573/cap-tool new github.com/yourname/user
```

参数说明：

- `--rm`：容器运行结束后自动删除
- `-v $(pwd):$(pwd)`：把当前目录挂载进容器，使生成结果落到本机
- `-w $(pwd)`：容器内的工作目录，即生成目标
- `-e icode=YOUR_UID`：课程平台校验码（每 30 天刷新一次），用于授权
- `new github.com/yourname/user`：仓库地址，工具从末段 `user` 提取服务名

执行成功后会打印完整目录结构（即 `model / repository / service / handler / proto` 等），与上一节的约定一致。

## 生成的基础代码结构

cap-tool 为每个服务自动生成以下关键代码：

- `model`：仅含初始 `ID` 字段的模型结构体
- `repository`：基于 GORM 的数据访问层，定义接口并初始化 MySQL 表
- `service`：持有 repository 实例，对外暴露 `AddUser` / `DeleteUser` 等接口方法
- `handler`：实现 proto 定义的 RPC（`Call` / `Add` / `Delete` / `Update` 等）
- `main`：借助 go-micro v3 完成初始化与注册

## proto 模板

`proto.go` 中维护接口定义模板，其中 `ProtoSRV` 给出了标准 CRUD 服务骨架（注意 `{{.Alias}}` 等占位符在生成时被服务名替换）：

```go
// tpl/proto.go（节选：ProtoSRV 模板）
service {{title .Alias}} {
	rpc Add{{title .Alias}}({{title .Alias}}Info) returns (Response) {}
	rpc Delete{{title .Alias}}({{title .Alias}}Id) returns (Response) {}
	rpc Update{{title .Alias}}({{title .Alias}}Info) returns (Response) {}
	rpc Find{{title .Alias}}ByID({{title .Alias}}Id) returns ({{title .Alias}}Info) {}
	rpc FindAll{{title .Alias}}(FindAll) returns (All{{title .Alias}}) {}
}

message {{title .Alias}}Info {
	int64 id = 1;
}
message {{title .Alias}}Id {
	int64 id = 1;
}
message FindAll {}
message Response {
	string msg = 1;
}
message All{{title .Alias}} {
	repeated {{title .Alias}}Info {{.Alias}}_info = 1;
}
```

## Makefile 与 Dockerfile 模板

`makefile.go` 把 proto 生成与镜像构建固化为 `make` 目标：

```makefile
# tpl/makefile.go（节选）
.PHONY: proto
proto:
	sudo docker run --rm -v $(shell pwd):$(shell pwd) -w $(shell pwd) \
	  cap1573/cap-v3 --proto_path=. --micro_out=. --go_out=:. \
	  ./proto/{{.Alias}}/{{.Alias}}.proto

.PHONY: build
build:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o {{.Alias}} *.go

.PHONY: docker
docker:
	docker build . -t {{.Alias}}:latest
```

`docker.go` 给出服务镜像的 `Dockerfile` 模板（基于 alpine，并附带 filebeat 采集日志）：

```dockerfile
# tpl/docker.go（节选：DockerSRV）
FROM alpine
ADD {{.Alias}} /{{.Alias}}
ADD filebeat.yml /filebeat.yml
ENTRYPOINT [ "/{{.Alias}}" ]
```

其余模板：`plugin.go` 用于注入 go-plugins 的匿名导入，`filebeat.go` 提供 `filebeat.yml` 日志采集配置，`.gitignore` 忽略 IDE 目录。

## API 速览

| 命令 | 作用 |
| --- | --- |
| `docker run ... cap1573/cap-tool new <repo>` | 生成标准微服务目录与基础代码 |
| `make proto` | 用 cap-v3 镜像把 `.proto` 编译为 Go 代码 |
| `make build` | 交叉编译出 linux/amd64 二进制 |
| `make docker` | 构建服务镜像 |

| 环境变量 | 作用 |
| --- | --- |
| `icode` | cap-tool 授权校验码，通过 `-e` 传入容器 |

## Demo 示例

运行说明：需本机已安装 Docker；`<repo>` 末段即服务名。

代码说明：下面演示「生成目录 → 生成 proto 代码 → 编译 → 构建镜像」的完整链路。

```bash
# 1. 生成 user 服务目录（服务名取自仓库路径末段 user）
docker run --rm -v $(pwd):$(pwd) -w $(pwd) \
  -e icode=YOUR_UID cap1573/cap-tool new github.com/yourname/user

# 2. 进入工程目录，生成 proto 对应的 Go 代码（依赖 cap-v3 镜像）
cd user
make proto

# 3. 拉取依赖并编译
go mod tidy
make build

# 4. 构建镜像
make docker
```

技术点总结：

- 服务名由仓库地址末段自动推断，保持目录、模块、镜像命名一致
- `make proto` 将 go-micro v3 的 `protoc` 流程封装进镜像，避免本机安装 protoc 工具链
- 生成代码遵循 `handler → service → repository → model` 分层，与目录约定完全对齐

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/cap-tool/tpl/proto.go`
- `code/课件/cap-tool/tpl/ignore.go`
- `code/课件/cap-tool/tpl/plugin.go`
- `code/课件/cap-tool/tpl/filebeat.go`
- `code/课件/cap-tool/tpl/docker.go`
- `code/课件/cap-tool/go.mod`
- `code/课件/cap-tool/tpl/makefile.go`
- `code/课件/cap-tool/main.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
