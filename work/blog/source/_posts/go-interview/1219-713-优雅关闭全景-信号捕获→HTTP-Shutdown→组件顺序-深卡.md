---
disableNunjucks: true
title: "713 优雅关闭全景：信号捕获→HTTP Shutdown→组件顺序（深卡）"
date: 2026-10-10 09:07:02
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 工程 | 难度：L4 | 题型：体系题 | 频率：高 | 关键词：**优雅关闭体系**/**信号**/**Shutdown**/**组件反向**/**与 1420/187 边界**

> 原文锚点：第 1~62 段「如何优雅关闭服务全节」

## 思路与架构
优雅关闭这条线按「**信号捕获 → HTTP Shutdown → 组件顺序**」三层串：
- 信号层：signal.Notify 转发可捕获信号到 channel、主 goroutine 阻塞等待；SIGKILL 不可监听（对应 `713-signal-capture.md`）。
- 服务层：收到信号后 http.Server.Shutdown(ctx) 先拒新流量、等老请求、带超时；通用五步收尾（对应 `713-http-graceful-shutdown.md`）。
- 架构层：多组件关闭 = 启动反向；先停入口再关依赖；异步生产者 flush（对应 `713-component-close-order.md`）。

## 方案取舍
- **信号基础给 signal-capture 卡**：讲清各信号值与 SIGKILL 不可捕获。
- **Web 服务给 http-graceful-shutdown 卡**：落到 Shutdown 机制 + 五步法 + 超时。
- **架构原则给 component-close-order 卡**：依赖反向总原则 + 反例。
- **不重产 Kafka flush**：异步生产者丢消息已由 `1420-graceful-shutdown.md` 覆盖，本深卡只引用不重述。
- **不重产 Docker PID1**：exec 作 PID1 收 SIGTERM 见 187.md`，本卡只点「容器里 SIGTERM 由 PID1 接收」一句。

## 答题技巧
1. 开场定调：优雅关闭 = 拦截信号 + 拒新流量 + 等老请求 + 释放资源。
2. 第一步信号：signal.Notify 转发、SIGKILL 不监听。
3. 第二步 Shutdown：先拒新请求、等在途、带超时（3s 常见）。
4. 第三步组件：启动反向关，先 HTTP 后依赖；异步生产者 flush。
5. 收尾：所有 Close/defer 释放资源，最后退出。被追问 Kafka 丢消息直接引 1420。

## 细节与核心 API

```go
ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGINT, syscall.SIGTERM)
defer stop()
srv := &http.Server{Addr: ":8080", Handler: mux}
go func() { if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed { log.Fatal(err) } }()
<-ctx.Done()                 // 收到信号
shutdownCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
defer cancel()
if err := srv.Shutdown(shutdownCtx); err != nil { log.Println("shutdown:", err) }
// Shutdown 停止接收新请求、等待活跃请求完成（或超时强切）
// 注意：ListenAndServe 在 Shutdown 后返回 ErrServerClosed，属正常，忽略即可
```
