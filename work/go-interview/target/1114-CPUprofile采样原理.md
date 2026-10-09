# 1114 CPU profile 采样原理

> 分类：性能与排障 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**SIGPROF** / **100Hz** / **StartCPUProfile**
> 原文锚点：第 13~14 段「CPU 采样开启后每十毫秒中断一次，由 SIGPROF 触发取函数栈」

## 一句话总述
CPU profile 默认以 100Hz（每 10ms）由 SIGPROF 中断，记录所有运行中的 goroutine 调用栈，导出后用 `go tool pprof` 看热点；`runtime/pprof.StartCPUProfile` 控制开关。

## 面试官视角
- 意图：是否真懂 CPU 采样的"统计抽样"本质与频率来源，而非只看 top。
- P5 知 100Hz/10ms / P6 说清 SIGPROF 与栈采样机制 / P7 知采样本身有开销、频率可调的代价。
- 红旗：以为 CPU profile 是"逐行计时"；以为采样频率无限高更准。
- 惊艳点：CPU profile 是统计抽样不是精确计时，100Hz 下短于约 10ms 的热点会被低估 —— 验证 `runtime/pprof` `[源码]`。

## 主问答
**Q（面试官原话）：** CPU profile 是怎么采样的？频率是多少？
**A：**
1. **结论**：开启后运行时每 10ms（默认 100Hz）收到 SIGPROF，记录当前所有运行 goroutine 的调用栈，累积成 profile `[源码]`。
2. **机制**：`runtime/pprof.StartCPUProfile` 启动、`StopCPUProfile` 停止；底层靠 SIGPROF 周期中断，对"正在 CPU 上跑"的栈采样，因此只反映 on-CPU 时间 `[源码]`。
3. **边界**：默认 100Hz 是统计抽样，小于 10ms 的瞬时热点会漏采；提高频率更准但侵入性/开销更大；它采不到阻塞等待（那属于 block profile）。
**加分层：** CPU profile 只看 on-CPU，IO 阻塞型慢要用 `block`/`mutex` 或 `trace`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 频率多少 | 概念 | 100Hz/10ms | 换题 |
| L2 | 谁触发 | 机制 | SIGPROF | 判 P5 |
| L3 | 采什么 | 边界 | on-CPU栈 | 判 P6 |
| L4 | 为何抽样 | 权衡 | 开销/精度 | 判 P6+ |
| L5 | 漏采咋办 | 实战 | 调频/trace | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 `[源码]` | 100Hz 默认长期不变 | 讲"SIGPROF 100Hz 采 on-CPU 栈" |

## 关键代码
```go
// 示意，未验证：手动采集 CPU profile
// f, _ := os.Create("cpu.prof")
// pprof.StartCPUProfile(f)
// defer pprof.StopCPUProfile()
// ... 业务代码 ...
```

## 总结与追问预判
- 100Hz SIGPROF 采 on-CPU 栈；短热点会漏；只看运行不采阻塞。
- 预判：heap/mutex → 见 1114；分析命令 → 见 1114。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 CPU 采样频率(100Hz/10ms)、SIGPROF 触发与 runtime/pprof 接口；仅做了机翻解码（如 勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
