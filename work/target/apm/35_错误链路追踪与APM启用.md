# 35. Go APM 监控系统实战: 错误链路追踪与 APM 启用

## 纲要

- 每个服务自己决定是否开启 APM：框架暴露 `EnableAPM` 这类设置项，调用方传入 Collector 地址即可
- 开启时初始化 `TracerProvider`：gRPC 连接 + OTLP Exporter + `AlwaysSample`（真正筛选交给 Collector 后置采样）
- `buildinfo` 子包：服务名取 `os.Args[0]` 的 basename，主机名取 `os.Hostname()`，让每个服务有独立标识
- 组合传播者（Composite Propagator）：同时传播 `TraceContext` 与 `Baggage`，后者可在链路上下文里附带额外信息
- 优雅退出：把 `TracerProvider.Shutdown` 包成 `Closer` 注册进全局关闭列表，进程退出时冲刷未发出的 Span
- 错误日志联动：打 error 日志时从 `ctx` 取出 Span，标记 `error=true` 并 `RecordError`，同时把 `trace_id` 写进日志，使日志与链路可互查
- 后置采样：只要 Span 带 `error=true` 整条 Trace 全采；业务侧另起一个以服务名命名的 `Tracer` 供自定义埋点

## 每个服务自己掌控 APM 开关

dogAPM 框架希望每个服务都能自主决定是否启用链路追踪，因此把开启逻辑收敛到一个设置项（讲稿里的 `infooption` / `EnableAPM`）里。调用方只需传入 OpenTelemetry Collector 的地址：

```go
// 以 order-service 为例，启用 APM 并指向本机 Collector
orderService.EnableAPM("127.0.0.1:54317")
```

内部会SDK 初始化骨架：建立 gRPC 连接、构造 OTLP Trace Exporter、组装 `TracerProvider`。不同之处在于两点：采样器统一用 `AlwaysSample`（把筛选决策交给 Collector 后置采样），以及服务名必须取自当前服务自身，而非写死成 `test-service`。

## buildinfo：拿到服务的身份标识

每个服务应当有自己独有的服务名与主机名，才能在上报的 Resource 中区分来源。框架用一个内部子包 `internal` 承载这段逻辑：

```go
// internal/buildinfo.go —— 根据讲稿逻辑补充
package internal

import (
	"os"
	"path/filepath"
)

// AppName 返回当前进程名（取可执行文件路径的 basename 作为服务名）
func AppName() string {
	return filepath.Base(os.Args[0])
}

// Hostname 返回运行主机名，失败时回退为 unknown
func Hostname() string {
	name, err := os.Hostname()
	if err != nil {
		return "unknown"
	}
	return name
}
```

## 组合传播者：TraceContext + Baggage

讲稿提到，除了链路上下文 `TraceContext`，还希望跨服务传递" baggage（行李）"——即随 Trace 上下文一起携带的额外键值信息。因此传播者不能只设 `TraceContext{}`，而要改成组合传播者：

```go
import (
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/propagation"
)

// 同时传播 W3C TraceContext 与 Baggage
otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(
	propagation.TraceContext{},
	propagation.Baggage{},
))
```

`Baggage` 遵循 W3C 规定的封装 / 解析格式，能在服务间透传业务维度（如租户 ID），而不必污染 Span 属性。

## 优雅退出：把 TracerProvider 接进全局关闭列表

进程退出时，内存里还缓存着没发往 Collector 的 Span。`TracerProvider` 自带 `Shutdown(ctx)` 能把这些数据强制推送出去。框架维护一个全局 `closers` 列表，在程序退出时统一调用每个 `Closer.Close()`。由于 `TracerProvider` 自身没有 `Close` 方法，需要包一层：

```go
// closer.go —— 根据讲稿逻辑补充
package dogapm

import (
	"context"
	"time"

	sdktrace "go.opentelemetry.io/otel/sdk/trace"
)

// Closer 是全局关闭列表的统一接口
type Closer interface {
	Close() error
}

// tracerProviderCloser 把 TracerProvider.Shutdown 适配成 Closer
type tracerProviderCloser struct {
	tp *sdktrace.TracerProvider
}

func (c tracerProviderCloser) Close() error {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	return c.tp.Shutdown(ctx)
}

// 注册进全局关闭列表（示意）
var globalClosers []Closer

func registerCloser(c Closer) { globalClosers = append(globalClosers, c) }
```

这样程序退出时会先把尚未发往 Collector 的残留 Trace 冲刷出去，再真正停止，避免缓冲数据丢失。

## 错误日志联动：让日志与链路互相串联

这是把"含错误的链路"采集落地的关键一步。框架规定：业务里出错一定要处理，而处理时必然会打一条 error 级日志。于是框架在打错误日志的地方做文章——只要 `ctx` 里携带 Span，就把它标记为错误，并把 `trace_id` 也写进日志行：

```go
import (
	"context"
	"fmt"
	"log"

	"go.opentelemetry.io/otel/codes"
	"go.opentelemetry.io/otel/trace"
)

// Errorf 打错误日志的同时，把当前 ctx 中的 Span 标记为 error，并记录 trace_id
func Errorf(ctx context.Context, format string, args ...interface{}) {
	msg := fmt.Sprintf(format, args...)

	if span := trace.SpanFromContext(ctx); span != nil && span.IsRecording() {
		span.RecordError(fmt.Errorf("%s", msg))
		span.SetStatus(codes.Error, msg)
		// 把 trace_id 落到日志，便于在日志系统与 Jaeger 间互查
		log.Printf("ERROR trace_id=%s %s", span.SpanContext().TraceID().String(), msg)
		return
	}
	log.Printf("ERROR %s", msg)
}
```

注意：业务侧打日志时传入的必须是**携带 Trace 上下文的 `ctx`**（即 `tracer.Start` 返回的那个），否则 `SpanFromContext` 取不到 Span。

## 后置采样与业务侧 Tracer

仅产生 Span 还不够。框架把 Collector 的配置文件改为：只要 Span 带 `error=true`，后置采样器就整条 Trace 全采。同时，框架在 `EnableAPM` 之后初始化一个专供业务系统创建 Span 的 `Tracer`，并以其服务名命名：

```go
// 业务侧即可用它手动埋点，例如下单逻辑
tracer := otel.Tracer(internal.AppName())
ctx, span := tracer.Start(ctx, "orderStart")
defer span.End()
// ... 下单业务 ...
```

## 验证效果

只启动 `order-service`，然后调用 `orderAdd` 接口。由于它依赖的 `user-service`、`goods-service` 没启动，请求必然走到错误分支，触发 `Errorf` 中把 Span 标 `error=true` 的逻辑。在 Jaeger 中能看到这条 `orderStart` 链路带有红色感叹号，并记录了当时的错误信息与堆栈——这就是"含错误的请求轨迹"被完整采集的结果。

## API 速览

| API | 说明 |
| --- | --- |
| `propagation.NewCompositeTextMapPropagator(p ...TextMapPropagator)` | 组合多个传播者，按顺序注入 / 提取 |
| `propagation.TraceContext{}` / `propagation.Baggage{}` | W3C 链路上下文 / 行李传播者 |
| `(*sdktrace.TracerProvider).Shutdown(ctx)` | 关闭并冲刷未导出的 Span |
| `trace.SpanFromContext(ctx)` | 从 ctx 取出当前 Span（可能为 noop） |
| `span.RecordError(err)` | 记录错误事件及堆栈 |
| `span.SetStatus(codes.Error,msg)` | 把 Span 状态置为错误 |
| `span.SpanContext().TraceID().String()` | 取 TraceID 字符串，用于日志关联 |

> 以上代码与 API 说明**根据讲稿逻辑补充**，课程源码目录中未提供对应文件。

## 技术点总结

- APM 开关收敛到 `EnableAPM`，调用方只传 Collector 地址
- 服务名 / 主机名来自 `buildinfo`，保证每个服务标识独立
- 用组合传播者同时透传 TraceContext 与 Baggage
- `TracerProvider` 必须接入全局关闭列表，否则退出时丢 Span
- 错误日志联动 Span 的 `error=true`，并写 `trace_id`，是日志与链路互查的桥梁
- 后置采样按 `error=true` 全采，业务侧用独立 `Tracer` 做自定义埋点

