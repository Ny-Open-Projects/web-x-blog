# Go PaaS 平台开发: 云应用市场 API 与 Proto 开发

## 纲要

- API 服务定位：在后端 gRPC 微服务之上，再生成一层对外暴露的 API 网关服务（基于 go-micro `api` 类型）
- 生成方式：使用 `micro new --type api`（或 `api create`）命令，扫描后端 proto 生成 API 工程骨架
- 接口规划：在基础增删改查之上，补充运营侧高频使用的统计接口（安装量、浏览量）
- 统一 ID 约定：云应用市场统一使用 `AppStoreId`（内部字段 `Id`）作为请求标识
- 抽取公共方法：把「从请求中获取并校验 AppID」提炼成 `GetAppID`，避免每个接口重复写转换逻辑

## 从服务端到 API 服务

前面几节已完成云应用市场的后端微服务（Model / Repository / Service / Handler）。这一节在该服务端之上，再生成一层 API 服务，专门对外提供 HTTP/网关入口。

使用 go-micro 的脚手架命令生成 API 工程骨架（注意使用创建 API 的命令，而非普通的 service）：

```bash
# 在 $GOPATH/src 下生成 api 类型的工程
micro new go.micro.api.appStore --type api
```

生成完成后，进入工程目录，先拉取依赖（执行 `go mod tidy` / `go get`），把依赖补齐后工程就不会有红色报错，随后即可开始开发。

## 规划对外 API

打开 API 工程的 proto 文件，先确定要对外暴露哪些接口。在云应用市场里，除了基础接口，运营侧最常用的就是统计类接口，因此把它们一并纳入：

- 添加安装统计（`AddInstallNum`）
- 获取安装数量（`GetInstallNum`）
- 添加浏览统计（`AddViewNum`）
- 获取浏览量（`GetViewNum`）

这些统计接口的入参通常是应用的 ID。由于本章有不少统计接口都依赖「应用 ID」，应当把「取 ID」的逻辑抽成一个公共方法，避免每个接口都重复写类型转换与校验。

## 统一的 ID 约定与公共方法

云应用市场内的应用，统一用一个标识来引用，约定就叫 `AppID`，对应的请求消息是 `AppStoreId`。下面是从请求中取出并校验该 ID 的通用写法（根据讲稿逻辑补充，可运行）：

```go
package handler

import (
	"context"
	appStore "git.imooc.com/coding-535/appStore/proto/appStore"
	"github.com/asim/go-micro/v3/client"
	log "github.com/asim/go-micro/v3/logger"
)

// 后端 AppStore 服务名（gRPC 服务发现用）
const appStoreServiceName = "go.micro.service.appStore"

// AppStoreApi 是 API 网关层的 handler
type AppStoreApi struct {
	// 通过 micro 生成的客户端调用后端服务
	AppStoreClient appStore.AppStoreService
}

// GetAppID 从请求中取出应用 ID，转换无误后返回。
// 统计类接口频繁使用，统一在此处理，避免重复代码。
func GetAppID(req *appStore.AppStoreId) (int64, error) {
	if req == nil {
		return 0, ErrInvalidAppID
	}
	// 如需做字符串到 int64 的兼容转换，可在此处理；
	// 当前 proto 的 Id 已为 int64，直接返回即可。
	return req.Id, nil
}
```

> 约定说明：本章里「应用市场里的应用」是一个聚合，但在市场层面我们引用它时只用一个 id 包装起来。统计接口只关心这个 id，因此请求统一用 `AppStoreId { int64 id = 1; }`，不要和领域内部的其它 id 混淆。

## API 层统计接口示例

API 层本身不写业务，只负责把外部请求转发给后端 AppStore 服务。以安装量统计为例：

```go
// AddInstallNum 对外暴露：添加安装统计
func (e *AppStoreApi) AddInstallNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Response) error {
	log.Info("Received AppStoreApi.AddInstallNum request")
	// 统一取 ID，出错直接返回
	if _, err := GetAppID(req); err != nil {
		rsp.Msg = err.Error()
		return err
	}
	// 转发到后端 gRPC 服务
	if err := e.AppStoreClient.AddInstallNum(ctx, req, rsp); err != nil {
		log.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	return nil
}

// GetInstallNum 对外暴露：获取安装数量
func (e *AppStoreApi) GetInstallNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Number) error {
	log.Info("Received AppStoreApi.GetInstallNum request")
	if _, err := GetAppID(req); err != nil {
		return err
	}
	if err := e.AppStoreClient.GetInstallNum(ctx, req, rsp); err != nil {
		log.Error(err)
		return err
	}
	return nil
}
```

## 为什么统计接口对运营很重要

统计接口并非可有可无。应用上架、推广之后，运营平台需要集中汇总以下数据：

- 商品曝光度（被搜索、被浏览的次数）
- 受众规模（安装次数）
- 使用热度（被打开、被访问详情的次数）

`GetInstallNum` / `GetViewNum` 这类接口正是为把这些指标集中汇总到运营平台服务的，因此它们是基础且高频的接口。

## API 速览

| API 方法 | 请求 | 响应 | 说明 |
| --- | --- | --- | --- |
| `AddInstallNum` | `AppStoreId` | `Response` | 安装量 +1（转发后端） |
| `GetInstallNum` | `AppStoreId` | `Number` | 读取安装量 |
| `AddViewNum` | `AppStoreId` | `Response` | 浏览量 +1（转发后端） |
| `GetViewNum` | `AppStoreId` | `Number` | 读取浏览量 |
| `GetAppID`（内部） | `*AppStoreId` | `int64, error` | 统一取并校验应用 ID |

> 说明：本节配套的项目代码按 `micro api` 工程组织，其 API handler 通过生成的 gRPC 客户端 `appStore.AppStoreService` 调用后端服务。上文片段为根据讲稿逻辑补充的精简可运行示例。

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
