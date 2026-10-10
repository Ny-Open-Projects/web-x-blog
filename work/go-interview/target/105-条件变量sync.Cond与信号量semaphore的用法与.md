# 105 条件变量 sync.Cond 与信号量 semaphore 的用法与坑

> 分类：并发模型 | 难度：中 | 题型：工程题 | 频率：中 | 关键词：**sync.Cond、Wait 需持锁、noCopy、semaphore.Acquire**

> 原文锚点：第 16~148 段「sync.Cond 等待通知…signal/broadcast…信号量 Acquire/Release/TryAcquire」

## 一句话总述
sync.Cond 用于"等待-通知"协作，**Wait 必须先持锁**；信号量（`golang.org/x/sync/semaphore`）用 Acquire/Release 控制并发数，二者都解决锁覆盖不到的同步场景。一句话背法：**「Cond 等通知须先持锁、不可复制；信号量 Acquire/Release 控并发额度」**。

## 面试官视角
考官考察是否掌握 Wait/Signal 的正确姿势与 noCopy 约束。能讲清 Wait 内部"先解锁再挂起、唤醒后重加锁"、Cond 不可复制、信号量限流，说明熟练；Wait 前不加锁、把 Cond 当普通变量复制、以为 signal 是"解锁"，是红旗。
- **P5**：知道 Cond 有 Wait/Signal/Broadcast。
- **P6**：能说 Wait 须持锁、Cond 不可复制。
- **P7**：知道信号量限流、Wait 与 Signal 不能同处一 goroutine 否则死锁。

## 主问答
**Q（面试官原话）：** sync.Cond 怎么用？Wait 为什么要先加锁？

**先铺垫（由浅入深第 1 层）**：锁解决"别同时改"，但有些场景是"某个条件满足前我先等、满足了你通知我"。这种"等-通知"锁表达不了，要用 Cond。它和锁强绑定——因为"检查条件+决定等待"本身也得互斥。

1. **结论（第 2 层）**：Wait 调用前必须持有 `c.L`；Signal 唤醒一个、Broadcast 唤醒全部；Cond 只能传指针、不可复制（noCopy 字段）。
2. **机制（第 3 层·关键）**：Wait 内部先 `c.L.Unlock()` 再挂起、唤醒后重新 `c.L.Lock()`——**并非"加锁"**，而是"挂起期间释放锁、醒来再拿回"，避免等待时长期占锁。
3. **边界（第 4 层）**：Wait 与 Signal 不能同在一个 goroutine（无人唤醒即死锁）；信号量用 `Acquire(n)/Release(n)/TryAcquire(n)` 控制并发额度。
4. **加分层（第 5 层）**：信号量是计数/二进制互斥的通用原语，二进制信号量即等价于互斥锁；它管"并发额度"，Cond 管"条件满足再继续"，各司其职。
5. **误用风险（第 6 层）**：别把 Cond 当"解锁"用、别复制 Cond 值（触发 noCopy panic）、别在持锁 goroutine 里既 Wait 又 Signal。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | Cond 有啥方法？ | Wait/Signal/Broadcast | — |
| L2 | Wait 为何持锁？ | 内部先解锁再挂起 | 停 L2：以为加锁 |
| L3 | 不能复制？ | noCopy 字段检测 | 停 L3：当普通变量 |
| L4 | 同协程死锁？ | Wait+Signal 互等 | 停 L4：不防死锁 |
| L5 | 信号量限流？ | Acquire/Release | 停 L5：不会限流 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| sync.Cond | 标准库，语义全版本稳定；`go doc sync.Cond.Wait` 可验证内部先 Unlock |
| noCopy | Cond 含 noCopy 字段，复制传递编译期/运行期报错 |
| 信号量 | `golang.org/x/sync/semaphore`，`NewWeighted`+`Acquire/Release/TryAcquire` |
| 二进制信号量 | 额度=1 等价于互斥锁 |
| Go 版本 | 与 Go 版本无关，本项目实测 Go 1.26.5 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
	"time"
)

// sync.Cond 标准用法：等待方先持锁再 Wait，通知方持锁再 Signal
func main() {
	cond := sync.NewCond(&sync.Mutex{})
	ready := false

	// 等待方：条件不满足就等
	go func() {
		cond.L.Lock()
		for !ready { // 用 for 防虚假唤醒
			cond.Wait() // 内部先 Unlock 再挂起，唤醒后重 Lock
		}
		fmt.Println("收到通知，开始工作")
		cond.L.Unlock()
	}()

	time.Sleep(10 * time.Millisecond)
	// 通知方：条件满足，持锁后 Signal
	cond.L.Lock()
	ready = true
	cond.Signal()
	cond.L.Unlock()

	time.Sleep(10 * time.Millisecond)
}
```

## 总结与追问预判
**背这三句就够**：① **Cond 等通知：Wait 前必须持锁，内部先解锁再挂起、唤醒重加锁**；② **Cond 只能传指针、不可复制（noCopy）**；③ **信号量 Acquire/Release 控并发额度，二进制信号量等价于锁**。
**预判追问**：
- 「Wait 和 Signal 能在一个 goroutine 吗？」→ 不能，无人唤醒即死锁（见本卡第 4 层）。
- 「Cond 和 channel 怎么选？」→ 简单通知用 channel 更直观，复杂条件+共享状态用 Cond（见 102 选型大方向）。
- 「信号量限流怎么写？」→ 见 1015 channel 信号量 / 1023 无缓冲 vs 信号量。

## ⚠️ 原文纠错
发现并修正 2 处技术错误：
- **其一（Wait/Signal 类比错误）**：原文将 `Wait` 类比为"加锁"、`Signal`/`Broadcast` 类比为"解锁"。实际 `Wait` 内部先 `c.L.Unlock()` 再挂起、唤醒后重新 `c.L.Lock()`，**并非"加锁"**；`Signal` 只唤醒一个等待者（该等待者随后自行重新获取锁），**并非"解锁"**。此类比会误导对 Cond 的理解。
- **其二（运行时实现误解）**：原文称 `runtime` 的 `notifyListWait` "应由底层 C 语言库提供"。Go 运行时主要由 Go 代码加少量汇编实现，并非 C 库；`sync.Cond.Wait` 内部调用 `runtime_notifyListWait`（位于 runtime/sema.go），属于 Go 运行时。
- 崩坏词归一：源码将 goroutine/Cond/信号量等音译为崩坏词；本卡统一为规范术语。
