# 822 调度延迟抽样与 /sched/latencies

> 分类：并发模型 / runtime | 难度：L3 | 题型：八股题 | 频率：低 | 关键词：**trackingSeq 采样**/**runnableTime**/**1/8 抽样**/**sched latencies**
> 原文锚点：第 145~155 段「trackingSeq 字段用于决定是否跟踪这个 goroutine 序列号」，第 157~165 段「runnableTime 记录可运行状态的时间」

## 一句话总述
Go 用 **g 上的四个字段（tracking / trackingSeq / trackingStamp / runnableTime）在状态机转换里做 1/8 抽样**，把「goroutine 从可运行到真正跑起来等了多久」统计成 **`/sched/latencies:seconds`** 直方图（163 桶 HDR）——**默认就有，但只有 1/8 样本**，且**只统计 Mutex 锁等待**，不能当端到端延迟看。

## 面试官视角
- 考察意图：专治「以为 runtime 没有内置调度延迟指标」。答不出 `/sched/latencies` 说明只用过 pprof。
- 分档：P5 知道 pprof/runtime/metrics 能看调度延迟；P6 说清 `trackingSeq % gTrackingPeriod == 0` 的**抽样条件**、`runnableTime` 进 `_Grunning` 即清零；P7 指出这是**抽样不是全量**，单次读数不能当精确值，知道 `casgstatusAlwaysTrack` 能强制全量。
- 红旗答案：「`runnableTime` 记录 g 总共运行了多久」——错，它记录**处于 runnable（可运行但没被调度）**的时间，进 `_Grunning` 立刻清零；「tracking 是全局开关」——错，它是**每 g 各自**的标志，由 `trackingSeq` 抽样决定；「这些字段给 pprof 用」——不准确，它们喂的是 `runtime/metrics`。
- 惊艳点：`/sched/latencies:seconds` 是**精确 HDR 直方图**——每桶 4 子桶，桶宽从 64 ns 起按 2 的幂递增，共 **163 桶**（含 -Inf），**桶边界是 API 契约、计数不是** [实测]。

## 主问答
**Q（面试官原话）：** Go 有内置的调度延迟指标吗？数据从哪来？
**A：**
1. **先给结论**：内置，指标是 **`/sched/latencies:seconds`**（直方图，`runtime/metrics` 读取）。数据来自 g 上四字段的**抽样统计** [源码]。
2. **再给机制**：每次 g 状态**离开** `_Grunning`/`_Gsyscall` 时，`casgstatus` 尾部执行 `if casgstatusAlwaysTrack || gp.trackingSeq%gTrackingPeriod == 0 { gp.tracking = true }` 并 `trackingSeq++`。被抽中的 g 在进出 `_Grunnable` 时用 `trackingStamp` 累加到 `runnableTime`，进 `_Grunning` 时 `sched.timeToRun.record(...)` 并清零（`proc.go:1321-1382`）[源码]。
3. **最后给边界**：`gTrackingPeriod = 8`，即**只统计 1/8 的转换**；且**只统计锁等待**（`isMutexWait()` 仅认 3 种 Mutex `waitReason`：`SyncMutexLock`/`SyncRWMutexRLock`/`SyncRWMutexLock`），channel 等待**不算**——**不能当端到端延迟**看 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | Go 有调度延迟指标吗 | 有没读过 `runtime/metrics` | `/sched/latencies:seconds` | 换题 → 不及格 |
| L2 | 数据从哪来 | 是否读过 `proc.go` 统计段 | g 四字段 + `casgstatus` 尾部 | P5 停 |
| L3 | 为什么不都记 | 有无抽样统计意识 | `gTrackingPeriod=8`，热路径不能加重 | P6 停 |
| L4 | 统计范围含什么 | 能否读 `isMutexWait` | 只含 3 种 Mutex waitReason，不含 channel | P6 停 |
| L5 | 线上怎么用 | 真实作战 | 配 pprof 看尾部延迟；端到端要业务埋点或 trace | 答得上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| `/sched/latencies:seconds` | **Go 1.16 随 `runtime/metrics` 引入** | 早于此只能靠 pprof |
| `gTrackingPeriod = 8` | Go 1.x 长期 | 背 8；明说这是抽样系数非契约 |
| 锁等待只认 3 种 `waitReason` | Go 1.x 长期 | `runtime2.go` 明列，**不含 channel** |
| `casgstatusAlwaysTrack` | 调试开关，非生产用 | 打开后 `casgstatus` 变慢 |

## 关键代码
```go
package main

import (
	"fmt"
	"runtime/metrics"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 3000; i++ {
		wg.Add(1)
		go func() { defer wg.Done(); _ = make([]byte, 8) }()
	}
	wg.Wait()
	time.Sleep(50 * time.Millisecond)

	s := []metrics.Sample{{Name: "/sched/latencies:seconds"}}
	metrics.Read(s)
	h := s[0].Value.Float64Histogram()
	fmt.Println("桶数 =", len(h.Buckets), " 计数数 =", len(h.Counts))

	var tot uint64
	for _, c := range h.Counts {
		tot += c
	}
	fmt.Println("样本总数 =", tot, "（约 3000/8 ≈ 375，实测偏大因为含 runtime 自身的 g）")

	fmt.Printf("前 8 个桶边界: ")
	for i := 0; i < 8; i++ {
		fmt.Printf("%.3e ", h.Buckets[i])
	}
	fmt.Println("\n（桶宽 6.4e-8 = 64 ns 等比）")
}
```

实测输出（go1.26.5 darwin/amd64，数值会波动）[实测]：

```text
桶数 = 163  计数数 = 162
样本总数 = 699
前 8 个桶边界: -Inf 0.000e+00 6.400e-08 1.280e-07 1.920e-07 2.560e-07 3.200e-07
```

分布峰值落在 `3.072e-06`~`8.192e-06`（约 3~8 µs），长尾到 `2.048e-05` 后消失；三次实测形状一致 [实测]。**桶边界确定、计数随机**。另：`/sync/mutex/wait/total:seconds` 是 `KindUint64` **标量**，别按直方图读。

## 总结与追问预判
一句话记忆：**「抽样 1/8、只记 runnable 段、只认 Mutex 等待——三句话缺一句，数字就没法解读」**。追问预判：g 状态字段全貌见 814-g结构体的身份与状态字段，GC 安全字段见 813-g的系统调用与GC安全字段；桶公式与两种失败口径见本卡深挖 [边界]。

## ⚠️ 原文纠错
1. 「tracking 是**是否正在跟踪**该 g（一个开关）」→ 是**每 g 各自**的 `bool`，由 `trackingSeq % 8` 抽样置位；`newproc1` 用 `cheaprand()` 随机初始化 `trackingSeq`（`proc.go:5376`）。
2. 「runnableTime 记录 g 处于可运行状态的时间」→ 对，但**漏了进入 `_Grunning` 时就被清零**（`proc.go:1380`），故它**只含「还没被调度」那段**。
3. 「通过 tracking 字段决定是否跟踪，零值表示不跟踪」→ 方向对，但**判据是 `trackingSeq % gTrackingPeriod == 0`**，不是 `tracking` 本身。
