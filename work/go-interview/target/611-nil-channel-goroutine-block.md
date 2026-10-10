# 611 nil channel 收发的死锁判定（同/异 goroutine）

> 分类：Go 并发/channel | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**nil channel**/**死锁**/**goroutine**/**阻塞**

> 原文锚点：第 11~33 段「同goroutine向nil/满channel收发→死锁…异goroutine向nil channel收发→一直阻塞直到主goroutine退出…是否死锁看是否在同goroutine」

## 一句话总述
向 **nil channel** 收发的"死锁与否"取决于**是否在同一个 goroutine**：在**当前 goroutine** 中收发（无其他 goroutine 取走）→ 永久阻塞 → 死锁；在**另一个新 goroutine** 中收发 → 也会永久阻塞，但**主 goroutine 退出后整个程序就结束**，**不会报死锁错误**（只是静默卡住直到进程结束）。

## 面试官视角
这是 nil channel 题里最易被忽略的细分层。面试官想看你区分"死锁（deadlock 报错）"与"单纯阻塞（不报错，等进程退出）"——二者表象都是卡住，根因不同。

## 主问答
**Q（面试官原话）：** 如果在另一个 goroutine 里向 nil channel 收发，还会死锁吗？

**A：**

1. **同 goroutine → 死锁**：当前 goroutine 既发又收同一个 nil channel，没有任何其他 goroutine 能取走数据，调度器判定"所有 goroutine  asleep"→ `panic: deadlock`。
2. **异 goroutine → 仅阻塞**：把收发放到 `go func()` 里，该 goroutine 永久阻塞在发送/接收点；但**主 goroutine 仍在跑**（如 `time.Sleep(1s)`），所以调度器不认为死锁，不会报错——直到主 goroutine 退出、进程结束，那个子 goroutine 才随之终止。
3. **本质**：死锁要求"所有 goroutine 都阻塞且无出路"；异 goroutine 情形下主 goroutine 还活着，不满足该条件，故只是阻塞而非 deadlock。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | 同goroutine收发给果 | 是否懂死锁 | 永久阻塞→deadlock | 答不出停档 |
| L2 | 异goroutine呢 | 是否懂仅阻塞 | 主活则不限死锁 | 答不出停档 |
| L3 | 为什么异goroutine不报错 | 是否懂死锁条件 | 主goroutine还活着 | 答不出停档 |
| L4 | 子goroutine卡到何时 | 是否懂进程退出 | 主退则进程结束 | 答不出停档 |
| L5 | 这和无缓冲死锁异 | 是否懂对比 | 见610死锁场景 | 答不出停档 |

## 版本与兼容性
- 行为自 Go 1.0 稳定，由运行时死锁检测器判定（仅当所有 goroutine 均阻塞才报 deadlock）。
- 无缓冲 channel 同 goroutine 收发也会死锁，机制相同，见 610。

## 关键代码
```go
func main() {
    var ch chan int // nil
    go func() {
        ch <- 1           // 子 goroutine 永久阻塞在发送点
        fmt.Println("sent") // 不会执行
    }()
    time.Sleep(time.Second)
    fmt.Println("main exit") // 主 goroutine 活着→不报 deadlock，1s 后进程结束
}
```

## 总结与追问预判
- 口诀：**同 goroutine 卡=死锁报错；异 goroutine 卡=等主退，不报错**。
- 预判追问："那无缓冲 channel 同 goroutine 收发呢？"→ 同样死锁，机制一致（见 610）。

## ⚠️ 原文纠错
源码将 goroutine/channel 术语音译为崩坏词，本卡已统一为规范术语（如 goroutine/channel/nil/死锁/阻塞/主协程）。纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：一般 channel 死锁场景见 610；nil channel 操作总览见 611；本卡只纵深"同/异 goroutine 的死锁 vs 阻塞差异"。
