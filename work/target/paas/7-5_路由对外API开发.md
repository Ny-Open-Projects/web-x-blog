# Go PaaS 平台开发: 路由对外 API 开发

## 纲要

- `routeApi` 网关服务：把 `route` 微服务通过 HTTP API 暴露给前端
- `RouteApi` handler 五个方法：FindRouteById / AddRoute / DeleteRouteById / UpdateRoute / Call
- 从 HTTP 请求的参数（`req.Get` / `req.Post`）取路由字段
- `form.FormToSvcStruct` 用反射把表单字段批量映射到 proto 结构
- 启动要点：服务名 `go.micro.api.routeApi`、端口不冲突、依赖 `route` 服务已注册

`route` 微服务是内部的 gRPC 服务，前端不能直接调。本节新建一个 `routeApi` 网关服务，把路由能力以 HTTP 接口（`/routeApi/...`）暴露出去。

## 服务入口与依赖

`routeApi` 的 `main.go` 用 go-micro 的 API 模式注册，关键是把服务名定为 `go.micro.api.routeApi`，并通过 `NewRouteService` 拿到内部 `route` 服务的客户端：

```go
routeService := go_micro_service_route.NewRouteService("go.micro.service.route", service.Client())
if err := routeApi.RegisterRouteApiHandler(service.Server(), &handler.RouteApi{RouteService: routeService}); err != nil {
	common.Error(err)
}
```

注意：API 服务名带 `Api` 后缀时，框架会自动做服务名映射，这里显式指向 `go.micro.service.route`。启动前要确保 `route` 服务以及 Consul、MySQL 都已起来，否则依赖拉取会失败。

## Handler 方法一览

```go
type RouteApi struct {
	RouteService route.RouteService
}
```

### 按 ID 查询

从 URL 的 `route_id` 参数取值，校验存在后调用内部服务，结果 JSON 化返回：

```go
func (e *RouteApi) FindRouteById(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	log.Info("Received routeApi.FindRouteById request")
	if _, ok := req.Get["route_id"]; !ok {
		rsp.StatusCode = 500
		return errors.New("参数异常")
	}
	routeIdString := req.Get["route_id"].Values[0]
	routeId, err := strconv.ParseInt(routeIdString, 10, 64)
	if err != nil {
		common.Error(err)
		return err
	}
	routeInfo, err := e.RouteService.FindRouteByID(ctx, &route.RouteId{Id: routeId})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(routeInfo)
	rsp.Body = string(b)
	return nil
}
```

### 添加路由

从表单 `req.Post` 取路径名、后端 Service 名和端口（**当前课程演示为「一个域名 + 一个路径 + 一个服务」**，多路径可循环处理），再交给 `form.FormToSvcStruct` 把其余字段映射进结构，最后调用内部 `AddRoute`：

```go
func (e *RouteApi) AddRoute(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	log.Info("Received routeApi.AddRoute request")
	addRouteInfo := &route.RouteInfo{}
	routePathName, ok := req.Post["route_path_name"]
	if ok && len(routePathName.Values) > 0 {
		port, err := strconv.ParseInt(req.Post["route_backend_service_port"].Values[0], 10, 32)
		if err != nil {
			common.Error(err)
			return err
		}
		routePath := &route.RoutePath{
			RoutePathName:           req.Post["route_path_name"].Values[0],
			RouteBackendService:     req.Post["route_backend_service"].Values[0],
			RouteBackendServicePort: int32(port),
		}
		addRouteInfo.RoutePath = append(addRouteInfo.RoutePath, routePath)
	}
	form.FormToSvcStruct(req.Post, addRouteInfo)
	response, err := e.RouteService.AddRoute(ctx, addRouteInfo)
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}
```

> 端口、后端 Service 名等字段必须赋值，否则后面设置 Ingress 会失败；这层既可在前端校验，也可在后端补一层校验。

### 删除路由

同样从 `route_id` 取参，校验后调用内部 `DeleteRoute`：

```go
func (e *RouteApi) DeleteRouteById(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	if _, ok := req.Get["route_id"]; !ok {
		rsp.StatusCode = 500
		return errors.New("参数异常")
	}
	routeId, err := strconv.ParseInt(req.Get["route_id"].Values[0], 10, 64)
	if err != nil {
		common.Error(err)
		return err
	}
	response, err := e.RouteService.DeleteRoute(ctx, &route.RouteId{Id: routeId})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(response)
	rsp.Body = string(b)
	return nil
}
```

### 更新与默认 Call

`UpdateRoute` 在本课程中留给读者自行实现（逻辑与添加类似，复用内部 `UpdateRoute`）；`Call` 是默认方法，对应 `/routeApi/` 或 `/routeApi/call`，返回全部路由：

```go
func (e *RouteApi) Call(ctx context.Context, req *routeApi.Request, rsp *routeApi.Response) error {
	allRoute, err := e.RouteService.FindAllRoute(ctx, &route.FindAll{})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(allRoute)
	rsp.Body = string(b)
	return nil
}
```

## 表单字段映射工具

`form.FormToSvcStruct` 通过反射，按结构体的 `json` tag 把 HTTP 表单里的 `Pair` 值批量赋值到目标结构，并做类型转换；`route_path` 这种嵌套结构被跳过、由上面的显式逻辑处理：

```go
func FormToSvcStruct(data map[string]*routeApi.Pair, obj interface{}) {
	objValue := reflect.ValueOf(obj).Elem()
	for i := 0; i < objValue.NumField(); i++ {
		dataTag := strings.Replace(objValue.Type().Field(i).Tag.Get("json"), ",omitempty", "", -1)
		dataSlice, ok := data[dataTag]
		if !ok {
			continue
		}
		valueSlice := dataSlice.Values
		if len(valueSlice) <= 0 {
			continue
		}
		if dataTag == "route_path" {
			continue
		}
		// 类型不一致时调用 TypeConversion 转换（int/int32/int64/float/time...）
		name := objValue.Type().Field(i).Name
		structFieldType := objValue.Field(i).Type()
		val := reflect.ValueOf(valueSlice[0])
		if structFieldType != val.Type() {
			val, _ = TypeConversion(valueSlice[0], structFieldType.Name())
		}
		objValue.FieldByName(name).Set(val)
	}
}
```

## API 速览

| 接口（HTTP） | 内部方法 | 说明 |
| --- | --- | --- |
| `/routeApi/FindRouteById?route_id=` | `FindRouteById` | 按 ID 查询单条路由 |
| `/routeApi/AddRoute`（POST） | `AddRoute` | 添加路由（表单含路径、后端 Service、端口） |
| `/routeApi/DeleteRouteById?route_id=` | `DeleteRouteById` | 删除路由 |
| `/routeApi/UpdateRoute`（POST） | `UpdateRoute` | 更新路由（课程留作练习） |
| `/routeApi/` 或 `/routeApi/call` | `Call` | 返回全部路由 |

## 技术点总结

- `routeApi` 是面向前端的网关层，内部通过 gRPC 调用 `route` 微服务。
- 参数从 `req.Get`（URL）/ `req.Post`（表单）取，端口务必解析为 int32。
- `FormToSvcStruct` 用反射+类型转换把表单映射到 proto，嵌套的 `route_path` 需手动构造。
- 启动前确认 `route` 服务、Consul、MySQL 在线；服务名、端口按本机环境区分。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/routeapi/filebeat.yml`
- `code/课件/routeapi/go.mod`
- `code/课件/routeapi/proto/routeApi/routeApi.proto`
- `code/课件/routeapi/plugin/hystrix/hystrix.go`
- `code/课件/routeapi/form/form.go`
- `code/课件/routeapi/README.md`
- `code/课件/routeapi/main.go`
- `code/课件/routeapi/handler/routeApiHandler.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
