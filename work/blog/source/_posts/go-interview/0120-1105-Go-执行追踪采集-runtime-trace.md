---
disableNunjucks: true
title: "1105 Go 执行追踪采集（runtime/trace）"
date: 2026-10-10 07:28:14
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go/性能 | 难度：L3 | 题型：工具题 | 频率：中 | 关键词：**runtime/trace** / **go tool trace** / **执行追踪** / **采集**
> 原文锚点：第 4~11 段、52~58 段「runtime/trace Start/Stop 写文件+go tool trace 打开UI；net/http/pprof 的 /debug/pprof/trace?seconds=N 下载 trace 文件」

## 一句话总述
当 pprof 看不清 goroutine "执行了啥、阻塞多久、在哪被阻"时，用 **执行追踪（execution tracer）**：方式一是标准库 `runtime/trace` 的 `trace.Start(f)` / `trace.Stop()` 写文件，再用 `go tool trace <file>` 打开浏览器 UI；方式二是 `net/http/pprof` 的 `/debug/pprof/trace?seconds=N` 直接下载 trace 文件。

## 面试官视角
- 意图：考察"trace 怎么采"的工具熟练度，常接"trace 和 pprof 啥区别"。
- P5 知道 go tool trace；P6 能说清两种采集方式；P7 能讲清 trace 有运行时开销、采完即停。
- 红旗：以为 trace 和 pprof 是同一个东西；采完不关导致线上常驻开销。
- 惊艳点：点出 pprof 是采样剖析、看不清 goroutine 时序/阻塞，才需要 trace；trace 有性能开销。

## 主问答
**Q（面试官原话）：** 怎么采集 Go 的执行 trace？
**A：**
1. **结论**：两种方式——① **runtime/trace**：`import "runtime/trace"` 后 `f, _ := os.Create("t.trace"); trace.Start(f); defer trace.Stop()`，程序退出后 `go tool trace t.trace` 自动开浏览器 UI；② **net/http/pprof**：起 HTTP server 后访问 `/debug/pprof/trace?seconds=N` 下载一段时长的 trace 文件（pprof 端点机制见 1114）。
2. **机制（为何用 trace）**：pprof 是**采样**剖析，看不清"某个 goroutine 阻塞了多久、在哪被调度打断"这类**时序/阻塞**信息；执行追踪记录每个 goroutine 的完整生命周期事件，正好补这块盲区。
3. **边界（开销）**：trace 会对程序产生**可观测的性能开销**，所以分析完性能问题后应避免无意义的常驻采集 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | trace 怎么采 | 基础 | runtime/trace + go tool trace | 判 P5 |
| L2 | 两种方式 | 工具 | 库 / pprof 端点 | 判 P6 |
| L3 | 为何不用 pprof | 区别 | pprof 采样看不清时序 | 判 P6+ |
| L4 | 开销 | 边界 | trace 有运行时开销 | 判 P7 |
| L5 | trace vs pprof | 综合 | 见 1105 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0+（runtime/trace） | 无 | runtime/trace 与 go tool trace 长期稳定；net/http/pprof 的 trace 端点自 pprof 包提供，语义一致 `[经验]` |

## 关键代码
```go
// 方式一：runtime/trace 采集
import (
    "os"
    "runtime/trace"
)
func main() {
    f, _ := os.Create("t.trace")
    trace.Start(f)       // 开始采集
    defer trace.Stop()   // 程序退出时写入
    // ... 业务 ...
}

// 方式二：net/http/pprof 已挂载时
// 访问 http://host:port/debug/pprof/trace?seconds=5 下载 5s 的 trace 文件
// 端点机制见 1114
```

## 总结与追问预判
- 采 trace：runtime/trace(Start/Stop) 或 pprof /debug/pprof/trace?seconds=N；go tool trace 看。
- 预判：trace UI 解读 → 见 1105；trace vs pprof → 见 1105；pprof 用法见 1114。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"pprof 看不清 goroutine 时序/阻塞、runtime/trace 的 Start/Stop 采集 + go tool trace 打开 UI、net/http/pprof 的 /debug/pprof/trace?seconds=N 下载"的描述，与 Go 工具链一致。源码将术语音译为崩坏词（勾入进→goroutine、PPROF→pprof、runtimetrace→runtime/trace、gototrice→go tool trace、trss→trace 文件 等），本卡统一为规范术语，技术结论未做更正。runtime G 的 trace 字段见 814（本卡聚焦执行追踪工具，不重复）`[经验]`。
