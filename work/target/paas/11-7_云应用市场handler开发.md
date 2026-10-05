# Go PaaS 平台开发: 云应用市场 Handler 开发

## 纲要

- Handler 层职责：作为 gRPC 服务端入口，把 proto 请求转换为领域模型，再委托给 Service 处理
- 统计类接口：`AddInstallNum` / `GetInstallNum` / `AddViewNum` / `GetViewNum` 的实现与 Service 一一对应
- 写操作接口：`AddAppStore` / `DeleteAppStore` / `UpdateAppStore` 的入参与返回处理
- 读操作接口：`FindAppStoreByID` / `FindAllAppStore` 的数据搬运
- 结构体转换：`common.SwapTo` 借助 JSON Tag 在 proto 结构与领域模型之间互转

## Handler 的结构

Handler 持有 `IAppStoreDataService` 接口（Service 层抽象），并不依赖具体实现。这样依赖方向是 Handler → Service → Repository → Model，层次清晰、易于替换与测试。

```go
package handler

import (
	"context"
	"git.imooc.com/coding-535/appStore/domain/model"
	"git.imooc.com/coding-535/appStore/domain/service"
	"git.imooc.com/coding-535/common"
	log "github.com/asim/go-micro/v3/logger"
	appStore "git.imooc.com/coding-535/appStore/proto/appStore"
	"strconv"
)

type AppStoreHandler struct {
	// 注意这里的类型是 IAppStoreDataService 接口类型
	AppStoreDataService service.IAppStoreDataService
}
```

## 统计类接口

统计接口逻辑很薄：校验入参、调用 Service、组织返回。错误统一通过 `common.Error` 记录，并把错误信息回写给 `Response.Msg`，让前端明确知道失败原因。

```go
// 添加安装统计
func (e *AppStoreHandler) AddInstallNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Response) error {
	if err := e.AppStoreDataService.AddInstallNum(req.Id); err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	rsp.Msg = "统计成功"
	return nil
}

// 获取安装数量
func (e *AppStoreHandler) GetInstallNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Number) error {
	rsp.Num = e.AppStoreDataService.GetInstallNum(req.Id)
	return nil
}

// 添加浏览统计
func (e *AppStoreHandler) AddViewNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Response) error {
	if err := e.AppStoreDataService.AddViewNum(req.Id); err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	rsp.Msg = "统计成功"
	return nil
}

// 获取浏览量
func (e *AppStoreHandler) GetViewNum(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Number) error {
	rsp.Num = e.AppStoreDataService.GetViewNum(req.Id)
	return nil
}
```

## 添加应用

`AddAppStore` 接收 proto 的 `AppStoreInfo`，先通过 `common.SwapTo` 把请求结构按 JSON Tag 转换为领域模型 `AppStore`，再交给 Service 落库。成功后把新生成的自增 ID 写回响应。

```go
// Call is a single request handler called via client.Call or the generated client code
func (e *AppStoreHandler) AddAppStore(ctx context.Context, info *appStore.AppStoreInfo, rsp *appStore.Response) error {
	log.Info("Received *appStore.AddAppStore request")
	appStoreModel := &model.AppStore{}
	if err := common.SwapTo(info, appStoreModel); err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}

	appStoreID, err := e.AppStoreDataService.AddAppStore(appStoreModel)
	if err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	rsp.Msg = "应用市场中新应用添加成功 ID 号为：" + strconv.FormatInt(appStoreID, 10)
	common.Info(rsp.Msg)
	return nil
}
```

## 删除与更新

删除直接透传 ID 给 Service；更新则先按 ID 查出已有记录，再把请求中的数据 Swap 覆盖到原模型上，最后调用更新。这里「先查后改」很关键——它保证了未出现在请求里的字段不会被清零。

```go
func (e *AppStoreHandler) DeleteAppStore(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.Response) error {
	log.Info("Received *appStore.DeleteAppStore request")
	return e.AppStoreDataService.DeleteAppStore(req.Id)
}

func (e *AppStoreHandler) UpdateAppStore(ctx context.Context, req *appStore.AppStoreInfo, rsp *appStore.Response) error {
	log.Info("Received *appStore.UpdateAppStore request")
	appStoreModel, err := e.AppStoreDataService.FindAppStoreByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err := common.SwapTo(req, appStoreModel); err != nil {
		common.Error(err)
		return err
	}
	return e.AppStoreDataService.UpdateAppStore(appStoreModel)
}
```

## 查询接口

单条查询与列表查询同样依赖 `SwapTo` 把领域模型转回 proto 响应结构。`FindAllAppStore` 需要遍历结果集，逐条转换后 `append` 到 `AllAppStore.AppStoreInfo`。

```go
func (e *AppStoreHandler) FindAppStoreByID(ctx context.Context, req *appStore.AppStoreId, rsp *appStore.AppStoreInfo) error {
	log.Info("Received *appStore.FindAppStoreByID request")
	appStoreModel, err := e.AppStoreDataService.FindAppStoreByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err := common.SwapTo(appStoreModel, rsp); err != nil {
		common.Error(err)
		return err
	}
	return nil
}

func (e *AppStoreHandler) FindAllAppStore(ctx context.Context, req *appStore.FindAll, rsp *appStore.AllAppStore) error {
	log.Info("Received *appStore.FindAllAppStore request")
	allAppStore, err := e.AppStoreDataService.FindAllAppStore()
	if err != nil {
		common.Error(err)
		return err
	}
	// 整理数据格式
	for _, v := range allAppStore {
		appStoreInfo := &appStore.AppStoreInfo{}
		if err := common.SwapTo(v, appStoreInfo); err != nil {
			common.Error(err)
			return err
		}
		rsp.AppStoreInfo = append(rsp.AppStoreInfo, appStoreInfo)
	}
	return nil
}
```

## 关于 SwapTo

Handler 中大量使用 `common.SwapTo` 在 proto 结构与领域模型之间互转，其实现非常简洁：先 `json.Marshal` 源结构，再 `json.Unmarshal` 到目标结构，利用双方相同的 JSON Tag 完成字段映射。

```go
package common

import "encoding/json"

// 通过 json tag 进行结构体赋值
func SwapTo(request, target interface{}) (err error) {
	dataByte, err := json.Marshal(request)
	if err != nil {
		return
	}
	err = json.Unmarshal(dataByte, target)
	return
}
```

> 注意：依赖 JSON Tag 转换要求 proto 生成结构与领域模型的 Tag 命名一致（如都使用 `app_sku`），否则会出现字段丢失。如果某次联调发现关联子表查不出来，优先检查 Handler 调用 Repository 时的返回值是否真正写了关联数据。

## API 速览

| Handler 方法 | 请求 | 响应 | 说明 |
| --- | --- | --- | --- |
| `AddAppStore` | `AppStoreInfo` | `Response` | 新增云应用，返回自增 ID |
| `DeleteAppStore` | `AppStoreId` | `Response` | 级联删除 |
| `UpdateAppStore` | `AppStoreInfo` | `Response` | 先查后改，避免字段清零 |
| `FindAppStoreByID` | `AppStoreId` | `AppStoreInfo` | 含关联子表 |
| `FindAllAppStore` | `FindAll` | `AllAppStore` | 列表查询 |
| `AddInstallNum` | `AppStoreId` | `Response` | 安装量 +1 |
| `GetInstallNum` | `AppStoreId` | `Number` | 读取安装量 |
| `AddViewNum` | `AppStoreId` | `Response` | 浏览量 +1 |
| `GetViewNum` | `AppStoreId` | `Number` | 读取浏览量 |

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
