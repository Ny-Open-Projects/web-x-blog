# 612 channel 与 goroutine 的垃圾回收：谁被谁引用、为什么会泄漏

> 分类：Go 并发 | 难度：L4 | 题型：事故题 | 频率：中 | 关键词：**GC、发送队列、接收队列、互相引用、goroutine 泄漏、永久阻塞**

> 原文锚点：第 63~66 段「我们需要注意的是呢，一个channel会被它的发送队列的协程和接受数据的所有协程所引用。那如果一个channel的发送队列或者是接受队列有一个不为空的情况下，那这个channel是肯定不会被垃圾回收的。那对于协程而言呢，如果一个协程处在某个channel的某个协程队列当中，那即使这个channel只被这个协程所引用，那这个协程也不会被垃圾回收，只有当这个协程退出之后呢，才能被垃圾回收」

## 一句话总述
channel 与 goroutine 之间是**双向引用**：channel 被其**发送队列和接收队列里的所有 goroutine 引用**，只要任一个队列**不为空**，该 channel **肯定不会被 GC**；反过来，一个 goroutine 只要**处在某个 channel 的等待队列中**，即使这个 channel 只被它自己引用，这个 goroutine 也**不会被 GC**，**只有它退出之后才可能被回收**——这就是 goroutine 泄漏的根因。

## 面试官视角
- 考察意图：能否解释"channel 不用了也不关，为什么会泄漏"，而不是只背"要 close"。
- 分档：P5 知道 goroutine 泄漏存在；P6 能说清 channel 与 goroutine 互相引用；P7 能推出"**阻塞在收发上的 goroutine 永远不退出 → 连同 channel 一起无法回收**"，并给出排查/规避手段。
- 红旗答案：以为"channel 没人引用就会被回收"——**只要还有 goroutine 卡在它的等待队列里，就永远不会被回收**。
- 惊艳点：**引用是双向的**：channel 引用着等待它的 goroutine，goroutine 也引用着它等待的 channel，形成**环**；但 Go 的 GC 能处理环引用，真正卡住回收的是** goroutine 处于阻塞态、永远不退出** `[源码]`。

## 主问答
**Q（面试官原话）：** channel 不用了但 goroutine 还卡着，会被回收吗？

1. **结论**：不会。channel 与 goroutine **互相引用**：只要还有 goroutine 卡在它的发送/接收队列里，双方都无法被回收，**必须等 goroutine 退出** `[源码]`。
2. **channel 侧**：一个 channel **会被它发送队列的协程和接收数据的所有协程所引用**；若**发送队列或接收队列有一个不为空**，这个 channel **肯定不会被垃圾回收** `[源码]`。
3. **goroutine 侧**：如果一个协程**处在某个 channel 的某个协程队列当中**，那么**即使这个 channel 只被这个协程所引用**，这个协程**也不会被垃圾回收**；**只有当这个协程退出之后**，才能被回收 `[源码]`。
4. **泄漏链条**：协程阻塞在收发上 → 协程不退出 → 它持有的 channel 与栈上对象都不可回收；若这类协程随时间累积，就是典型的 **goroutine 泄漏**（内存与调度开销双涨）`[经验]`。
5. **boundary · nil channel**：向 `nil` channel 发送或从其接收，会使**当前协程永久阻塞**；在**同一个协程中**读写 `nil` channel 会导致**死锁** `[源码]`。
6. **工程解法**：用 `context` 取消、`select` + 超时/`default`、明确的关闭责任（发送方关闭），保证每个阻塞点都有**退出路径**；用 `runtime.NumGoroutine()` 或 pprof goroutine profile 做回归观测 `[经验]`。

**加分层：** 判断"channel 该不该关"的标准不是"用完就关"，而是"**还有没有接收方需要被通知**"。若没有接收方要通知，靠 `context` 让发送方退出即可，不必强行 close（多发送方场景下强行 close 反而会 panic）。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | channel 会被谁引用？ | 答不出收发队列的 goroutine |
| L2 | 队列非空时能回收吗？ | 答出不能 |
| L3 | 卡住的 goroutine 能回收吗？ | 答出退出才行 |
| L4 | nil channel 收发会怎样？ | 答出永久阻塞/死锁 |
| L5 | 怎么排查与规避？ | 答出 context/超时/pprof |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0+ | 无 | 双向引用与"退出才回收"语义稳定 |
| Go 1.7+ | 引入 context | 取消通知首选 context |
| Go 1.11+ | pprof 标签 | 可用 goroutine profile 定位泄漏 |
| Go 全版本 | nil channel | 收发永久阻塞，同协程读写死锁 |

## 关键代码
```go
// 1) 泄漏样本：goroutine 卡在接收上，channel 与 goroutine 互相引用，谁都不回收
func leak() {
	ch := make(chan int)
	go func() {
		<-ch // 永远阻塞，goroutine 不退出
	}()
	// ch 已无外部引用，但因接收队列非空，不会被 GC
}

// 2) 用 context 给出退出路径
func noLeak(ctx context.Context) {
	ch := make(chan int)
	go func() {
		select {
		case v := <-ch:
			_ = v
		case <-ctx.Done(): // 有退出路径，goroutine 能结束
			return
		}
	}()
}

// 3) nil channel：收发永久阻塞；同一个 goroutine 内读写会死锁
var nc chan int
// nc <- 1  // 永久阻塞
// <-nc     // 永久阻塞

// 4) 回归观测：goroutine 数是否随时间单调上涨
fmt.Println("goroutines:", runtime.NumGoroutine())
```

## 总结与追问预判
**这一节最容易和"要不要 close channel"混在一起问**。标准答法是分层回答：**关闭是为了通知接收方"没有更多数据了"**；**回收则取决于 goroutine 能否退出**。所以"不 close 一定泄漏"是错的——只要所有 goroutine 都有退出路径（context / 超时 / 正常结束），不 close 也会被回收；反过来，**close 了但仍有 goroutine 卡在别的 channel 上，照样泄漏**。

## ⚠️ 原文纠错
1. 事实核校：channel 被收发队列中的 goroutine 引用、队列非空则不回收、goroutine 位于 channel 等待队列时即使只被该 channel 引用也不回收、协程退出后才可回收、nil channel 收发永久阻塞且同协程读写死锁——均与 Go 运行时语义一致 `[经验]`。
2. 补充：原文"只有协程退出之后才能被垃圾回收"的表述应补一句前提——**协程退出后，若它引用的对象已无其他强引用才被回收**；另外泄漏的对象不止 channel，还包括该协程栈上可达的全部对象 `[经验]`。
3. 崩坏词归一：源码将 channel、goroutine、垃圾回收、发送队列、接收队列等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
