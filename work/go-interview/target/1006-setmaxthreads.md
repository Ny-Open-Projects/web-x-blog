# 1006 debug.SetMaxThreads：限制 OS 线程（M）数量与超限崩溃

> 分类：Go 运行时 / GMP | 难度：L3 | 题型：机制题 | 频率：中 | 关键词：**SetMaxThreads** / **M 数量** / **线程上限** / **kernel.threads-max** / **崩溃**
> 原文锚点：第 5~20 段「SetMaxThreads 限制 M 数量默认 1 万；超限制程序崩溃；限制的是 OS 线程不是协程；受 Linux 内核参数 threads-max/PID_MAX/max_map_count 约束」

## 一句话总述
`debug.SetMaxThreads(n)` 限制 Go 程序能创建的 **操作系统线程（GMP 中的 M）总数**，默认 10000；一旦运行时试图创建超过该数的 M，进程直接 fatal 崩溃。它限制的是 **M（内核线程）**，不是 G（goroutine）数量。

## 面试官视角
- 意图：确认候选人不混淆 M 与 G，并理解"为什么要有这个上限"以及"超限即崩"的严厉语义。
- P5 知 SetMaxThreads 限 M、默认 1 万；P6 知超限崩溃、返回旧值、与内核参数挂钩；P7 知 PID_MAX / max_map_count 如何间接卡住线程创建。
- 红旗：以为 SetMaxThreads 能限制 goroutine 数；或以为调大它就"安全"（其实受内核 threads-max 与 PID 空间约束）。
- 惊艳点：点出"M 受 cgo/ syscall 阻塞放大，防的是疯狂起线程拖垮 OS" `[边界]` 见 813-gmp-model-overview、816-gm-problems（M 的创建与阻塞）。

## 主问答
**Q（面试官原话）：** SetMaxThreads 是做什么的？限制的是线程还是协程？
**A：**
1. **限 M 不限 G**：它约束 GMP 中 M（操作系统工作线程）的数量，goroutine（G）数量由栈与调度决定，不受此限。
2. **默认 10000，超限即崩**：超过上限时运行时抛 `runtime: program exceeds N-thread limit` 并终止进程，用于防止程序不合理地耗尽内核线程资源。
3. **返回旧值**：函数返回调用前的设置值，便于保存/还原；内核调度本身也消耗线程资源，故设限是为保护 OS。
4. **受内核参数约束**：Linux 上 `kernel.threads-max`（系统最大线程数）、`PID_MAX`（全局 PID 上限）、`vm.max_map_count`（每进程虚拟内存区上限）都会间接钳制可创建的 M 数。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 限 M 还是限 G | 基础 | 限 M | 判 P5 |
| L2 | 默认值/超限后果 | 记忆 | 1万/崩溃 | 判 P6 |
| L3 | 返回什么 | 细节 | 旧值 | 判 P6+ |
| L4 | 内核参数关联 | 进阶 | threads-max/PID_MAX/max_map_count | 判 P7 |
| L5 | 为何要限 M | 设计 | 防拖垮 OS、cgo 放大 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有受支持版本 | 无 | 限 M、默认 1 万、超限崩溃；与内核参数联动 |

## 关键代码
```go
package main

import "runtime/debug"

func main() {
	prev := debug.SetMaxThreads(10000)
	_ = prev // 返回旧上限；运行时线程数超过此值即 fatal 退出

	// 注意：goroutine 数量不受此函数限制，以下不会触发 SetMaxThreads
	// go func() { for {} }()  // 大量 G 受栈/调度约束，而非 M 上限
}
```

## 总结与追问预判
- SetMaxThreads = 限 M 数、默认 1 万、超限崩溃；M 受内核 threads-max/PID_MAX/max_map_count 间接约束。
- 预判：M 的阻塞与 cgo 放大 → 见 816-gm-problems；GMP 总览 → 见 813-gmp-model-overview；P 数量 → 见 815-p-overview-status。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：SetMaxThreads 限 M 数、默认 10000、超限崩溃、返回旧值、三个 Linux 内核参数——均正确，未做更正。
