# Go PaaS 平台开发: svcAPI 工程创建与接口业务逻辑开发

## 纲要

- 用 `cap-tool createAPI` 生成 svcApi 工程（handler / plugin / proto 三目录）
- 生成 `.pb.go` / `.micro.go`：执行 `make proto` 后 `go mod tidy` 拉依赖
- `SvcApi` handler 结构：持有后端 `svc.SvcService` 客户端
- 四个接口：`FindSvcById` / `AddSvc` / `DeleteSvcById` / `Call`（默认查全部）
- `AddSvc` 端口特殊处理和 `ClusterIP` 模式 switch，再经 `form` 插件反射映射
- 服务治理插件：限流、熔断（hystrix）、链路追踪、负载均衡在 `main.go` 装配

## 生成 API 工程

与 `newservice` 不同，生成对外 API 工程使用 `createAPI` 命令（仓库地址即服务名，如 `svcApi`）。生成目录含三层：

- `handler/`：接口业务逻辑（需要自己写）。
- `plugin/`：限流、熔断等治理插件。
- proto 文件：需再执行 `make proto` 生成 `.pb.go` / `.micro.go`（初始报红是因为未生成）。

随后把工程推到远程仓库并 `go mod tidy` 安装依赖，`go run` 能启动即说明框架就绪。

## Handler 结构与默认接口

`SvcApi` 持有一个后端 `svc.SvcService` 客户端，所有方法都通过它调用 `go.micro.service.svc`：

```go
type SvcApi struct {
	SvcService svc.SvcService
}
```

网关把 `/svcApi/findSvcById`、`/svcApi/AddSvc` 等 HTTP 路径映射到对应方法；未显式实现的请求会落到 `Call`（默认查所有）。

## 查询单个服务 FindSvcById

从 `req.Get["svc_id"]` 取参数，校验非空后转为 int64，调用后端 `FindSvcByID`，结果 JSON 化返回：

```go
func (e *SvcApi) FindSvcById(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("接受 svcApi.FindSvcById 的请求")
	if _, ok := req.Get["svc_id"]; !ok {
		rsp.StatusCode = 500
		return errors.New("参数异常")
	}
	svcIdString := req.Get["svc_id"].Values[0]
	svcId, err := strconv.ParseInt(svcIdString, 10, 64)
	if err != nil {
		common.Error(err)
		return err
	}
	svcInfo, err := e.SvcService.FindSvcByID(ctx, &svc.SvcId{Id: svcId})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(svcInfo)
	rsp.Body = string(b)
	return nil
}
```

## 添加服务 AddSvc（端口与类型处理）

添加时端口比较特殊：不同 Service 类型需要设置不同的端口字段。课程按 `ClusterIP` 模式开发，因此用 `switch` 判断类型，匹配到 `ClusterIP` 才设置 `SvcPort` / `SvcTargetPort` / `SvcPortProtocol`；未匹配到直接返回"类型不支持"。

```go
func (e *SvcApi) AddSvc(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("添加svc服务")
	addSvcInfo := &svc.SvcInfo{}
	svcType, ok := req.Post["svc_type"]
	if ok && len(svcType.Values) > 0 {
		svcPort := &svc.SvcPort{}
		switch svcType.Values[0] {
		case "ClusterIP":
			port, err := strconv.ParseInt(req.Post["svc_port"].Values[0], 10, 32)
			if err != nil {
				common.Error(err)
				return err
			}
			svcPort.SvcPort = int32(port)
			targetPort, err := strconv.ParseInt(req.Post["svc_target_port"].Values[0], 10, 32)
			if err != nil {
				common.Error(err)
				return err
			}
			svcPort.SvcTargetPort = int32(targetPort)
			svcPort.SvcPortProtocol = req.Post["svc_port_protocol"].Values[0]
			addSvcInfo.SvcPort = append(addSvcInfo.SvcPort, svcPort)
		default:
			return errors.New("类型不支持")
		}
	}
	// 其余字段通过 form 插件批量反射映射
	from.FormToSvcStruct(req.Post, addSvcInfo)
	response, err := e.SvcService.AddSvc(ctx, addSvcInfo)
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

端口数组被提前单独处理，是因为 `SvcInfo.SvcPort` 是数组、映射关系特殊；其余平铺字段交给 `FormToSvcStruct` 用 `json` 标签反射赋值（端口 / targetPort 在插件内被 `continue` 跳过）：

```go
func FormToSvcStruct(data map[string]*svcApi.Pair, obj interface{}) {
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
		if dataTag == "svc_port" || dataTag == "svc_target_port" {
			continue
		}
		// ... 按字段类型做类型转换并 Set
	}
}
```

## 删除与默认查询

删除 `DeleteSvcById` 同样取 `svc_id` → 调后端 `DeleteSvc`。`Call` 作为默认接口，调用 `FindAllSvc` 返回服务列表：

```go
func (e *SvcApi) Call(ctx context.Context, req *svcApi.Request, rsp *svcApi.Response) error {
	log.Info("查询所有svc服务")
	allSvc, err := e.SvcService.FindAllSvc(ctx, &svc.FindAll{})
	if err != nil {
		common.Error(err)
		return err
	}
	rsp.StatusCode = 200
	b, _ := json.Marshal(allSvc)
	rsp.Body = string(b)
	return nil
}
```

> `UpdateSvc` 接口课程留给学员实现：逻辑与 `AddSvc` 类似，但要带上查询出来的 `id` / `svc_id`，否则因主键对应不上而更新失败。

## 服务治理装配（main.go）

`svcApi` 在 `main.go` 中通过 go-micro 选项一次性装配注册中心、链路追踪、熔断、限流与负载均衡：

```go
service := micro.NewService(
	micro.Name("go.micro.api.svcApi"),
	micro.Address(":"+servicePort),
	micro.Registry(consul),
	// 链路追踪
	micro.WrapHandler(opentracing2.NewHandlerWrapper(opentracing.GlobalTracer())),
	micro.WrapClient(opentracing2.NewClientWrapper(opentracing.GlobalTracer())),
	// 熔断（仅作为客户端时生效）
	micro.WrapClient(hystrix2.NewClientHystrixWrapper()),
	// 限流
	micro.WrapHandler(ratelimit.NewHandlerWrapper(1000)),
	// 负载均衡（轮询）
	micro.WrapClient(roundrobin.NewClientWrapper()),
)
// 把后端 svc 服务注入 handler
svcService := go_micro_service_svc.NewSvcService("go.micro.service.svc", service.Client())
svcApi.RegisterSvcApiHandler(service.Server(), &handler.SvcApi{SvcService: svcService})
```

熔断以 go-micro `client.Wrapper` 实现：每个 RPC 调用包进 `hystrix.Do`，正常路径执行、异常路径走熔断兜底。

```go
func (c *clientWrapper) Call(ctx context.Context, req client.Request, rsp interface{}, opts ...client.CallOption) error {
	return hystrix.Do(req.Service()+"."+req.Endpoint(), func() error {
		return c.Client.Call(ctx, req, rsp, opts...)
	}, func(e error) error {
		return e
	})
}
```

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/svcapi/filebeat.yml`
- `code/课件/svcapi/go.mod`
- `code/课件/svcapi/proto/svcApi/svcApi.proto`
- `code/课件/svcapi/plugin/hystrix/hystrix.go`
- `code/课件/svcapi/plugin/form/form.go`
- `code/课件/svcapi/README.md`
- `code/课件/svcapi/main.go`
- `code/课件/svcapi/handler/svcApiHandler.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
