# 713 HTTP 服务优雅关闭机制

> 分类：Go 工程 / Web | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**http.Server.Shutdown**/**关闭 listener**/**等待在途请求**/**超时 ctx**/**5 步通用法**

> 原文锚点：第 23~37 段「Shutdown 方法 / 关闭监听 / 等待已有请求」

## 一句话总述
HTTP 服务优雅关闭靠 `http.Server.Shutdown(ctx)`：它先**关闭 listener** 拒绝新请求，再（定时器）关闭空闲连接，并**等待在途请求处理完成**后才返回。通用五步：① 捕获终止信号 ② 停止接收新请求/连接 ③ 等待已有请求/连接处理完（sync.WaitGroup / context）④ 释放占用资源（db/文件句柄 Close、defer）⑤ 退出程序。务必带超时 ctx，避免收尾无限拖。

## 面试官视角
这是 Web 后端面试高频实战题。能讲清「Shutdown 不是立即杀进程、而是先拒新流量再等老请求」的机制，并落到「超时控制 + 资源释放顺序」，就是高分；只说「监听信号」不算完。

## 主问答
**Q（面试官原话）：** HTTP 服务怎么优雅关闭？

1. **Shutdown 做了什么**：调用 `srv.Shutdown(ctx)` 后，server 关闭 listener（新请求进不来），并等待**已建立的连接处理完**才返回；内部用定时器关闭空闲连接。
2. **带超时 ctx**：`ctx, cancel := context.WithTimeout(ctx, 3*time.Second)` 包住 Shutdown，超时强制返回，防止某些长请求拖死退出。
3. **与 signal 联动**：在 `<-sig` 之后调用 Shutdown，实现「收到 SIGTERM → 拒新流量 → 等老请求 → 退」。
4. **等待在途用 WaitGroup/context**：业务里的 worker / 长任务用 `sync.WaitGroup` 或 `context` 感知取消，Shutdown 前/中优雅收尾，而非硬杀。
5. **释放资源**：最后关 db、Redis、Kafka 等连接（见 713.md`），用 `Close()` 或 `defer` 释放文件句柄，再 `os.Exit` 或自然返回。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 怎么关 HTTP server？ | 说不清 Shutdown |
| L2 | Shutdown 立即杀进程？ | 说不清先拒新流量等老请求 |
| L3 | 为何要超时？ | 说不清长请求拖死 |
| L4 | 在途任务怎么等？ | 说不清 WaitGroup/context |
| L5 | 资源释放顺序？ | 说不清组件反向关 |

## 版本与兼容性
| 动作 | 实现 | 注意 |
|------|------|------|
| 拒新请求 | 关 listener | Shutdown 自动做 |
| 等老请求 | 等活跃连接完成 | 受 ctx 超时约束 |
| 释放资源 | Close/defer | 组件按依赖反向 |

## 关键代码
```go
srv := &http.Server{Addr: ":8080", Handler: mux}
go srv.ListenAndServe()

sig := make(chan os.Signal, 1)
signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
<-sig // 收到退出信号

ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
defer cancel()
if err := srv.Shutdown(ctx); err != nil { // 关 listener + 等老请求，最多等 3s
    log.Printf("shutdown err: %v", err)
}
// 此后关闭 db/redis 等资源，最后退出
```

## 总结与追问预判
核心：**Shutdown 先拒新流量、等老请求完成、带超时；通用五步收尾**。追问拐向「多组件怎么排关闭顺序」——备好「启动最后依赖最先 init、关闭相反」（见 713.md`）；Kafka 异步生产者 flush 见 1420.md`。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文称 Shutdown「先关监听拒新请求、定时关空闲连接、等已有任务完成不再收新任务」——与 `http.Server.Shutdown` 语义一致；本卡补入「Shutdown 是 goroutine-safe、可多次调用、受 ctx 超时约束」与「WaitGroup/context 等待在途任务」的工程要点（原文只提超时 3s）。
2. 崩坏词归一：源码将 server / 关闭 / 请求 / 连接 / 携程 等音译为多组崩坏词，本卡统一为规范术语。
