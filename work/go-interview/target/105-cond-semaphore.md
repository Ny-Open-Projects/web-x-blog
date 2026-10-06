# 105 条件变量 sync.Cond 与信号量 semaphore 的用法与坑

> 分类：并发模型 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**sync.Cond** / **Wait 需持锁** / **semaphore.Acquire**
> 原文锚点：第 16~148 段「sync.Cond 等待通知…signal/broadcast…信号量 Acquire/Release/TryAcquire」

## 一句话总述
sync.Cond 用于"等待-通知"协作，Wait 必须先持锁；信号量（golang.org/x/sync/semaphore）用 Acquire/Release 控制并发数，二者都解决锁覆盖不到的同步场景。

## 面试官视角
- **考察意图**：是否掌握 Wait/Signal 的正确姿势与 noCopy 约束。
- **P5** 知 Cond 有 Wait/Signal/Broadcast / **P6** 能说 Wait 须持锁、Cond 不可复制 / **P7** 知信号量限流、Wait 与 Signal 不能同处一 goroutine 否则死锁。
- **红旗**：Wait 前不加锁；把 Cond 当普通变量复制传递；以为 signal 是"解锁"。
- **惊艳点**：Cond.Wait 内部先 `c.L.Unlock()` 再挂起、唤醒后重加锁，并非"加锁" —— 验证：`go doc sync.Cond.Wait`，go1.26.5 `[源码]`。

## 主问答
**Q（面试官原话）：** sync.Cond 怎么用？Wait 为什么要先加锁？
**A：**
1. **结论**：Wait 调用前必须持有 c.L；Signal 唤醒一个、Broadcast 唤醒全部；Cond 只能传指针、不可复制。
2. **机制**：Wait 内部先解锁再挂起，唤醒后重新加锁，避免"等待途中锁被长期占用"；noCopy 字段在复制时被检测报错。
3. **边界**：Wait 与 Signal 不能同在一个 goroutine（无人唤醒即死锁）；信号量用 Acquire(n)/Release(n)/TryAcquire(n) 控制并发额度。
**加分层：** 信号量是计数/二进制互斥的通用原语，二进制信号量即等价于互斥锁。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | Cond 有啥方法 | 概念 | Wait/Signal/Broadcast | 换题 |
| L2 | Wait 为何持锁 | 机制 | 内部先解锁 | 判 P5 |
| L3 | 不能复制 | 边界 | noCopy 字段 | 判 P6 |
| L4 | 同协程死锁 | 权衡 | Wait+Signal 互等 | 判 P6+ |
| L5 | 信号量限流 | 实战 | Acquire/Release | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| sync.Cond 全版本；semaphore 在 golang.org/x/sync | 无 | Cond 语义稳定；信号量用 x/sync `[源码]` |

## 关键代码
```go
// 示意，未验证：Cond 标准用法
cond := sync.NewCond(&sync.Mutex{})
go func() { cond.L.Lock(); cond.Wait(); cond.L.Unlock() }() // 必须先持锁
cond.L.Lock(); cond.Signal(); cond.L.Unlock()

// 信号量限流（golang.org/x/sync/semaphore）
sem := semaphore.NewWeighted(3)
sem.Acquire(ctx, 1); /* 工作 */; sem.Release(1)
```

## 总结与追问预判
- Cond 等待-通知需持锁、不可复制；信号量控制并发额度；二进制信号量等价于锁。
- 预判：原子 vs 锁选型 → 见 105-atomic-vs-lock-when；原理 → 见 105-atomic-implementation。

## ⚠️ 原文纠错
发现 2 处技术错误。
- 其一，原文将 `Wait` 类比为"加锁"、`Signal`/`Broadcast` 类比为"解锁"（第 37 段）。实际 `Wait` 内部先 `c.L.Unlock()` 再挂起、唤醒后重新 `c.L.Lock()`，并非"加锁"；`Signal` 只唤醒一个等待者（该等待者随后自行重新获取锁），并非"解锁"。此类比会误导对 Cond 的理解。
- 其二，原文称 `runtime` 的 `notifyListWait` "应该是由底层的 C 语言库提供的支持"（第 59 段）。Go 运行时主要由 Go 代码加少量汇编实现，并非 C 库；`sync.Cond.Wait` 内部调用的是 `runtime_notifyListWait`（位于 runtime/sema.go），属于 Go 运行时。
