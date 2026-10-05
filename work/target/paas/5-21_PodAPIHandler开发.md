# Go PaaS 平台开发: PodAPI Handler 开发

## 纲要

- `PodApi` 结构体持有 `PodService` 客户端字段，用以调用后端 Pod 服务。
- 由 `podApi.proto` 生成的接口必须全部实现，否则 Handler 无法注册到微服务。
- `FindPodById`：从 `req.Get` 提取 `pod_id` 参数，校验缺失后调用后端，返回 JSON。
- 其余接口（AddPod/DeletePodById/UpdatePod/Call）先以打印占位，业务逻辑后续章节补全。
- 路由规则：网关按 `/podApi/方法名` 精确转发到对应方法；`/podApi/` 或 `/podApi/call` 命中默认 `Call`。

## Handler 结构体

API Handler 通过持有后端 Service 的客户端来编排调用。其它 Service 也按同样方式注入：

```go
package handler

import (
    "context"
    "git.imooc.com/coding-535/pod/proto/pod"
    "git.imooc.com/coding-535/podApi/proto/podApi"
)

type PodApi struct {
    PodService pod.PodService
}
```

`pod.PodService` 是后端 pod 服务经 proto 生成并注册到 Consul 后，由 `go.micro.service.pod` 名称拿到的客户端。若还要调用别的 Service，同样在此追加字段，经由服务名调用对应接口。

## 实现 FindPodById

以查询单个 Pod 为例，演示"提取参数 → 校验 → 调用后端 → 组装响应"的完整套路：

```go
// podApi.FindPodById 通过 API 向外暴露为 /podApi/findPodById
func (e *PodApi) FindPodById(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.FindPodById 的请求")
    // 1. 从 GET 参数取 pod_id，缺失则报错
    if _, ok := req.Get["pod_id"]; !ok {
        rsp.StatusCode = 500
        return errors.New("参数异常")
    }
    // 2. 取参数值并转为 int64
    podIdString := req.Get["pod_id"].Values[0]
    podId, err := strconv.ParseInt(podIdString, 10, 64)
    if err != nil {
        return err
    }
    // 3. 调用后端 Pod 服务
    podInfo, err := e.PodService.FindPodByID(ctx, &pod.PodId{Id: podId})
    if err != nil {
        return err
    }
    // 4. 以 JSON 返回
    rsp.StatusCode = 200
    b, _ := json.Marshal(podInfo)
    rsp.Body = string(b)
    return nil
}
```

说明：

- 参数来自 `req.Get`（网关把 URL 查询参数映射成 `map<string, Pair>`）。
- 校验缺失返回 500 与错误，避免下游空指针。
- 拿到 `podInfo` 后直接 `json.Marshal` 写入 `rsp.Body`，由网关回给前端。

## 其余接口先占位

本阶段先把另外四个接口实现出来（不实现会导致编译期接口未满足），逻辑暂时只打印请求到达，业务后续补全：

```go
func (e *PodApi) AddPod(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.AddPod 的请求")
    rsp.StatusCode = 200
    return nil
}

func (e *PodApi) DeletePodById(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.DeletePodById 的请求")
    rsp.StatusCode = 200
    return nil
}

func (e *PodApi) UpdatePod(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.UpdatePod 的请求")
    rsp.StatusCode = 200
    return nil
}

// 默认接口：/podApi/ 或 /podApi/call 命中
func (e *PodApi) Call(ctx context.Context, req *podApi.Request, rsp *podApi.Response) error {
    fmt.Println("接受到 podApi.Call 的请求")
    rsp.StatusCode = 200
    return nil
}
```

## 路由映射

网关依据访问路径把请求精确转发到方法：

| 访问路径 | 命中方法 |
| --- | --- |
| `/podApi/findPodById?pod_id=1` | `FindPodById` |
| `/podApi/addPod` | `AddPod` |
| `/podApi/deletePodById?pod_id=1` | `DeletePodById` |
| `/podApi/updatePod` | `UpdatePod` |
| `/podApi/` 或 `/podApi/call` | `Call`（默认） |

## 衔接

本篇完成 Handler 骨架，至少保证五个接口都能被网关路由到。下一篇编写 `main.go`，把注册中心、链路追踪、熔断、日志、监控、限流、负载均衡全部接入，并注册该 Handler。

总结：

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/go-paas-html/pages-404.html`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/go-paas-html/pages-login.html`
- `code/课件/go-paas-html/pages-login2.html`
- `code/课件/podapi/handler/podApiHandler.go`
- `code/课件/go-paas-html/pages-sign-up.html`
- `code/课件/go-paas-html/layouts-nosidebars.html`
- `code/课件/go-paas-front/volume-create.html`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：94%。是否需要继续：是。代码是否可运行：是。
