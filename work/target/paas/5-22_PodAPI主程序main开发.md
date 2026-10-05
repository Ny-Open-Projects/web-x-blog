# Go PaaS 平台开发: PodAPI 的 main 主程序开发

## 纲要

- API 层 `main.go` 与服务层结构相似，但命名以 `go.micro.api.xxx` 约定，便于网关寻址。
- 全局变量集中管理：服务地址、Consul、链路追踪、熔断端口、监控端口，各服务端口须互不冲突。
- 依次接入：注册中心、链路追踪、熔断看板、日志、监控采集、限流、负载均衡。
- 用 `Advertise` 上报可达地址，`micro.Address` 固定端口，避免随机端口无法暴露。
- 注册 Handler 并把后端 `PodService` 客户端注入，最后 `service.Run()` 启动。
- API 网关通过 `go.micro.api.podApi` 找到 `podApi` 子服务，约定前缀 `go.micro.api`。

## 全局变量

API 与后端服务同机开发时端口必须不同，否则冲突；容器或 K8s 内则可相同。统一在文件顶部声明：

```go
var (
    hostIp        = "192.168.0.105"
    serviceHost   = hostIp      // 服务上报地址
    servicePort   = "8082"      // 服务端口，需固定
    consulHost    = hostIp
    consulPort int64 = 8500
    tracerHost    = hostIp
    tracerPort    = 6831        // OpenTracing / Jaeger Agent
    hystrixPort   = 9092        // 熔断看板端口，不能重复
    prometheusPort = 9192       // 监控端口，不能重复
)
```

## main 主流程

```go
func main() {
    // 1. 注册中心 Consul
    consul := consul.NewRegistry(func(options *registry.Options) {
        options.Addrs = []string{consulHost + ":" + strconv.FormatInt(consulPort, 10)}
    })

    // 2. 链路追踪
    t, io, err := common.NewTracer("go.micro.api.podApi", tracerHost+":"+strconv.Itoa(tracerPort))
    if err != nil {
        common.Error(err)
    }
    defer io.Close()
    opentracing.SetGlobalTracer(t)

    // 3. 熔断看板数据流
    hystrixStreamHandler := hystrix.NewStreamHandler()
    hystrixStreamHandler.Start()

    // 4. 日志统一写入根目录 micro.log，配合 filebeat.yml 采集上报

    // 6. 启动熔断监听程序（独立端口）
    go func() {
        err = http.ListenAndServe(net.JoinHostPort("0.0.0.0", strconv.Itoa(hystrixPort)), hystrixStreamHandler)
        if err != nil {
            common.Error(err)
        }
    }()

    // 7. 监控采集地址
    common.PrometheusBoot(prometheusPort)

    // 8. 创建服务
    service := micro.NewService(
        // 自定义服务地址，必须写在其它参数前面
        micro.Server(server.NewServer(func(options *server.Options) {
            options.Advertise = serviceHost + ":" + servicePort
        })),
        micro.Name("go.micro.api.podApi"),
        micro.Version("latest"),
        micro.Address(":" + servicePort),
        micro.Registry(consul),
        micro.WrapHandler(opentracing2.NewHandlerWrapper(opentracing.GlobalTracer())),
        micro.WrapClient(opentracing2.NewClientWrapper(opentracing.GlobalTracer())),
        micro.WrapClient(hystrix2.NewClientHystrixWrapper()),
        micro.WrapHandler(ratelimit.NewHandlerWrapper(1000)),
        micro.WrapClient(roundrobin.NewClientWrapper()),
    )

    service.Init()

    // 注册后端 PodService 客户端
    podService := go_micro_service_pod.NewPodService("go.micro.service.pod", service.Client())
    // 注册 Handler
    if err := podApi.RegisterPodApiHandler(service.Server(), &handler.PodApi{PodService: podService}); err != nil {
        common.Error(err)
    }
    // 启动服务
    if err := service.Run(); err != nil {
        common.Fatal(err)
    }
}
```

## 关键点

### 服务命名与网关约定

API 服务名为 `go.micro.api.podApi`。网关默认以 `go.micro.api` 为前缀，再据子服务名 `podApi` 查找并转发，因此命名必须遵循该约定，否则网关找不到路由。

### Advertise 必须靠前

`options.Advertise` 写在 `micro.Server(...)` 的最前面，告知注册中心"用哪个地址访问我"。若写在后面会被其它参数覆盖，导致注册成容器内网地址，宿主机无法访问。

### 熔断、监控端口各服务唯一

`hystrixPort`、`prometheusPort` 在多个服务间不能重复，否则同机启动会端口冲突、数据无法收集。

### 日志与 Filebeat

程序把日志写入本地 `micro.log`，项目内 `filebeat.yml` 负责采集并上报 Logstash。Filebeat 二进制需下载对应版本并在启动时执行 `./filebeat -e -c filebeat.yml`。

## 启动验证

启动后在 Consul 控制台会多出 `go.micro.api.podApi` 一条记录，说明 API 服务已正常注册。随后启动统一网关（下一篇），即可经网关访问该 API。

## 衔接

API 主程序已完成注册与启动。下一篇讲解统一网关 `cap-api-gateway` 的作用与启动方式，把 API 暴露出去。

总结：

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/go-paas-html/pages-404.html`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/go-paas-html/pages-login.html`
- `code/课件/go-paas-html/pages-login2.html`
- `code/课件/go-paas-html/pages-sign-up.html`
- `code/课件/go-paas-html/layouts-nosidebars.html`
- `code/课件/go-paas-front/volume-create.html`
- `code/课件/go-paas-front/route-create.html`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：96%。是否需要继续：是。代码是否可运行：是。
