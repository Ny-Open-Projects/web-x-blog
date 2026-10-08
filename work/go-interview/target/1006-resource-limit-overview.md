# 1006 Go 运行时如何限制操作系统线程等资源（SetMaxThreads/GOMAXPROCS/SetMaxStack/SetMemoryLimit 总览）

> 分类：Go 运行时 / GMP | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**SetMaxThreads** / **GOMAXPROCS** / **SetMaxStack** / **SetMemoryLimit** / **资源限制**
> 原文锚点：第 1~50 段「限制 M/P 数量控制 OS 资源；四个设置：SetMaxThreads(M数,默认1万)、GOMAXPROCS(P数)、SetMaxStack(单协程栈内存)、SetMemoryLimit(Go1.19 软内存限制)；非必要不调整」

## 一句话总述
Go 运行时暴露了四类"资源限制"旋钮：限制 **OS 线程 M 数量**（`debug.SetMaxThreads`）、限制 **逻辑处理器 P 数量**（`runtime.GOMAXPROCS`）、限制 **单个 goroutine 栈内存**（`debug.SetMaxStack`）、限制 **Go 堆内存上限**（`debug.SetMemoryLimit`，Go 1.19 软限制）。前两者直接约束 GMP 调度器的物理并发规模，后两者约束内存。

## 面试官视角
- 意图：考察是否真懂 GMP 里 M/P 的"数量"意味着什么，以及这些旋钮该不该动、动了会怎样。
- P5 知四者各自限制对象；P6 知默认值（M=1万、P=NumCPU、栈 1GB/250MB、内存 MaxInt64）；P7 知"超限即 crash""软限制""cgo 不计入"等陷阱。
- 红旗：把 SetMaxThreads 当成限制 goroutine 数；或以为 SetMemoryLimit 能卡住 cgo/C 申请的内存。
- 惊艳点：点出"限制的是 M 不是 G"、软限制与 GC 联动、与 Linux 内核参数（threads-max/PID_MAX/max_map_count）的对应关系 `[边界]` 见 813-gmp-model-overview、815-p-overview-status、816-gmp-tradeoff（GMP 调度与 P/M 含义）。

## 主问答
**Q（面试官原话）：** Go 能限制运行时操作系统线程的数量吗？都有哪些限制手段？
**A：**
1. **限制 OS 线程 M 数**：`debug.SetMaxThreads(n)` 设 M 上限，默认 10000；一旦超过，运行时直接抛 fatal 让程序崩溃，目的是防止耗尽内核线程资源。
2. **限制逻辑处理器 P 数**：`runtime.GOMAXPROCS(n)` 设 P 个数，等价于环境变量 `GOMAXPROCS`；Go 1.5 起默认等于 CPU 核数，IO 密集型可设大于核数。
3. **限制单协程栈内存**：`debug.SetMaxStack(n)` 设单个 goroutine 栈上限，64 位默认 1GB、32 位 250MB；仅约束"单协程"，不影响协程总数。
4. **限制 Go 堆内存（软）**：`debug.SetMemoryLimit(n)`（Go 1.19）等价于 `GOMEMLIMIT`，设 Go 运行时管理内存的软上限，触发更激进 GC；不含二进制与 cgo 内存。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 四个旋钮各限什么 | 基础 | M/P/单栈/堆 | 判 P5 |
| L2 | 默认值多少 | 记忆 | 1万/NumCPU/1GB/MaxInt64 | 判 P6 |
| L3 | 超 SetMaxThreads 会怎样 | 陷阱 | 直接 crash | 判 P6+ |
| L4 | 内存限制含 cgo 吗 | 边界 | 不含，仅 Go 运行时映射内存 | 判 P7 |
| L5 | 与内核参数关系 | 进阶 | threads-max/PID_MAX/max_map_count | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| GOMAXPROCS | Go 1.5 起默认 NumCPU（此前=1） | 讲"1.5 是分水岭" |
| SetMemoryLimit | Go 1.19 新增 | 旧版本答"用 GOGC/cgroup 兜底" |
| 其余 | 长期稳定 | 四者并列讲 |

## 关键代码
```go
package main

import (
	"runtime"
	"runtime/debug"
)

func main() {
	oldThreads := debug.SetMaxThreads(10000) // 返回旧值；超过即 crash
	_ = oldThreads

	oldP := runtime.GOMAXPROCS(0) // 传 0 仅读当前 P 数，不修改
	_ = oldP

	oldStack := debug.SetMaxStack(1 << 30) // 单协程栈上限（字节）
	_ = oldStack

	oldMem := debug.SetMemoryLimit(-1) // -1 = 不限制（等同 math.MaxInt64）
	_ = oldMem
}
```

## 总结与追问预判
- 四个旋钮分两层：M/P 是 GMP 并发规模，栈/堆是内存边界；SetMaxThreads 超限即崩，SetMemoryLimit 是软限制。
- 预判：GMP 模型与 P/M 含义 → 见 813-gmp-model-overview、816-gmp-tradeoff；栈扩容与 SetMaxStack 旁支 → 见 420-stack-grow-address-shift、1118-stack-heap-diff。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：SetMaxThreads 默认 1 万、超限崩溃、GOMAXPROCS 1.5 起默认 NumCPU、SetMaxStack 64 位 1GB/32 位 250MB、SetMemoryLimit 为 Go 1.19 软限制且不含 cgo 内存——均正确，未做更正。
