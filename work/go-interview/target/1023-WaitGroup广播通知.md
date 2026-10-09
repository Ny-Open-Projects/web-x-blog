# 1023 WaitGroup 广播通知：用第二个 WG 等数据就绪再继续

> 分类：Go 并发 / 同步 | 难度：L3 | 题型：技巧题 | 频率：中 | 关键词：**WaitGroup 广播** / **ready 信号** / **Add(-1)** / **数据就绪** / **阻塞等待**
> 原文锚点：第 6~23 段「双 WaitGroup:WG2.Add(1)后协程内 WG2.Wait 阻塞;主调 WG2.Done 广播通知数据就绪协程才继续;Done=Add(-1)等价;用于协程间数据依赖」

## 一句话总述
当协程**依赖其他协程准备好的数据**才能继续时，可用**第二个 WaitGroup 当广播信号**：主协程 `ready.Add(1)`，子协程在 `ready.Wait()` 上阻塞，等数据准备完主协程调 `ready.Done()`（等价 `Add(-1)`）广播通知，子协程才往下执行。这是 WaitGroup 的"通知/同步"妙用。

## 面试官视角
- 意图：考察能否把 WaitGroup 从"计数等待"升华到"条件通知"，理解 Done 即 Add(-1)。
- P5 知双 WG 广播思路；P6 知 `ready.Wait()` 阻塞、`Done()` 唤醒、Done=Add(-1)；P7 知它实现的是"数据就绪通知"，与 channel 通知的区别与取舍。
- 红旗：用单个 WG 既等退出又等数据导致语义混乱；或不知 Done 等价于 Add(-1)。
- 惊艳点：点出"WG2 在此是一次性广播原语，数据准备好才放行依赖协程" `[边界]` 见 1023（等待方式选型）、913-waitgroup-usage（WaitGroup 语义）、1024-signal-notify-daemon（信号通知对照）。

## 主问答
**Q（面试官原话）：** 怎么用 WaitGroup 实现"数据准备好再通知协程继续"？
**A：**
1. **双 WG 分工**：`wg` 负责等所有协程退出，`ready` 充当广播信号——`ready.Add(1)` 后，子协程在 `ready.Wait()` 阻塞。
2. **广播通知**：主协程准备好数据后调 `ready.Done()`（等价于 `ready.Add(-1)`），阻塞的协程被唤醒、才真正使用数据；实现"数据就绪才继续"。
3. **语义本质**：这里 WaitGroup 被当成一次性"条件变量"用——不是计数 N 个任务，而是等一个"就绪"事件。
4. **与 channel 对照**：同样可用 close(channel) 或发信号实现通知；WaitGroup 广播胜在语义直观、无需额外 channel 变量。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 怎么广播 | 基础 | 双 WG + Done | 判 P5 |
| L2 | Done 等价 | 细节 | Add(-1) | 判 P6 |
| L3 | 阻塞在哪 | 机制 | ready.Wait() | 判 P6+ |
| L4 | 与 channel 通知 | 区分 | 语义直观 vs 需变量 | 判 P7 |
| L5 | 何时用广播 | 边界 | 协程间数据依赖 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | 双 WG 广播；Done=Add(-1) |

## 关键代码
```go
package main

import "sync"

// WaitGroup 广播：用第二个 WG 通知"数据就绪"
func main() {
	var wg, ready sync.WaitGroup
	ready.Add(1) // ready 充当广播信号
	wg.Add(1)
	go func() {
		defer wg.Done()
		ready.Wait() // 阻塞直到主协程广播数据就绪
		// 这里才真正使用已准备好的数据
	}()
	// 准备数据 ...
	ready.Done() // 广播：通知协程继续（等价 ready.Add(-1)）
	wg.Wait()
}
```

## 总结与追问预判
- 双 WG 广播 = 把 WaitGroup 当一次性"就绪通知"；Done=Add(-1)；适合协程间数据依赖。
- 预判：等待方式选型 → 见 1023；WaitGroup 语义 → 见 913；信号通知对照 → 见 1024。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：双 WaitGroup 广播、ready.Wait 阻塞、Done 广播等价 Add(-1)、用于协程间数据依赖——均正确，未做更正。
