# Go PaaS 平台开发: 路由 Handler 开发

## 纲要

- `RouteHandler` 依赖 `IRouteDataService` 接口
- 五个方法：添加 / 删除 / 更新 / 按 ID 查 / 查全部
- 用 `common.SwapTo` 在 proto 结构与 model 结构间互转
- 添加路由：先建 Ingress，成功后再写数据库
- 启动注意事项：`hostIp` 写本机 IP、各服务端口不重叠

本节在 `route` 微服务的 handler 层把上一节的 service 封装成对外的 gRPC 方法。handler 不直接碰 Kubernetes 和数据库，只调用 `RouteDataService`。

## Handler 结构与依赖注入

```go
type RouteHandler struct {
	// 注意这里的类型是 IRouteDataService 接口类型
	RouteDataService service.IRouteDataService
}
```

## 添加路由

先用 `common.SwapTo` 把 proto 的 `RouteInfo` 转成 model 的 `Route`，再调用 service 创建 Ingress，成功后把记录写入数据库：

```go
func (e *RouteHandler) AddRoute(ctx context.Context, info *route.RouteInfo, rsp *route.Response) error {
	log.Info("Received *route.AddRoute request")
	route := &model.Route{}
	if err := common.SwapTo(info, route); err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	// 创建 route 到 k8s
	if err := e.RouteDataService.CreateRouteToK8s(info); err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	// 写入数据库
	routeID, err := e.RouteDataService.AddRoute(route)
	if err != nil {
		common.Error(err)
		rsp.Msg = err.Error()
		return err
	}
	common.Info("Route 添加成功 ID 号为：" + strconv.FormatInt(routeID, 10))
	rsp.Msg = "Route 添加成功 ID 号为：" + strconv.FormatInt(routeID, 10)
	return nil
}
```

## 删除路由

先按 ID 查出模型（包含命名空间、路由名），再调用 `DeleteRouteFromK8s` 完成「删 Ingress + 删库」：

```go
func (e *RouteHandler) DeleteRoute(ctx context.Context, req *route.RouteId, rsp *route.Response) error {
	log.Info("Received *route.DeleteRoute request")
	routeModel, err := e.RouteDataService.FindRouteByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err := e.RouteDataService.DeleteRouteFromK8s(routeModel); err != nil {
		common.Error(err)
		return err
	}
	return nil
}
```

## 更新路由

先更新 Kubernetes 里的 Ingress，再把数据库记录查出来、用新数据覆盖后写回：

```go
func (e *RouteHandler) UpdateRoute(ctx context.Context, req *route.RouteInfo, rsp *route.Response) error {
	log.Info("Received *route.UpdateRoute request")
	if err := e.RouteDataService.UpdateRouteToK8s(req); err != nil {
		common.Error(err)
		return err
	}
	routeModel, err := e.RouteDataService.FindRouteByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	if err := common.SwapTo(req, routeModel); err != nil {
		common.Error(err)
		return err
	}
	return e.RouteDataService.UpdateRoute(routeModel)
}
```

也可以不先查询，直接覆盖对应字段再更新，按业务需要选择。

## 查询：按 ID 与查全部

```go
func (e *RouteHandler) FindRouteByID(ctx context.Context, req *route.RouteId, rsp *route.RouteInfo) error {
	routeModel, err := e.RouteDataService.FindRouteByID(req.Id)
	if err != nil {
		common.Error(err)
		return err
	}
	// 数据转化（model -> proto），供前端展示
	if err := common.SwapTo(routeModel, rsp); err != nil {
		common.Error(err)
		return err
	}
	return nil
}

func (e *RouteHandler) FindAllRoute(ctx context.Context, req *route.FindAll, rsp *route.AllRoute) error {
	allRoute, err := e.RouteDataService.FindAllRoute()
	if err != nil {
		common.Error(err)
		return err
	}
	for _, v := range allRoute {
		routeInfo := &route.RouteInfo{}
		if err := common.SwapTo(v, routeInfo); err != nil {
			common.Error(err)
			return err
		}
		rsp.RouteInfo = append(rsp.RouteInfo, routeInfo)
	}
	return nil
}
```

查询给前端做展示时，要注意做一次**数据结构转换**（model ↔ proto），把关联的路径数据一并带上。

## 启动注意事项

`main.go` 里这些变量必须按本机环境调整：

- `hostIp`：**必须写成你本机的 IP**（本机运行）；若跑在容器里则写 `127.0.0.1`。
- `servicePort`：每个微服务端口不能重叠。前面已经开发了 service、port-service、port 的 API 等，路由服务这里写 `8087`，不要与它们冲突。
- 熔断端口、Prometheus 监控端口每个服务也要各不相同。

首次运行会连接 MySQL，自动建好对应的测试表；启动成功后，在 Consul 注册中心里会多出一个 `go.micro.service.route` 服务。

## 技术点总结

- handler 只编排 service，不直接操作 K8s/DB，保持分层清晰。
- `common.SwapTo` 基于 JSON tag 在 proto 与 model 间互转，是贯穿全课程的转换工具。
- 添加/更新顺序：先 K8s 后 DB；删除在 service 内部已是「先 K8s 后 DB」。
- 端口、IP 是本地联调最常见的坑，务必按本机环境修改。

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

相关度：100%。是否需要继续：是。代码是否可运行：是。
