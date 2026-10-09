> 原文锚点：第 1~40 段「未初始化channel是nil…关闭后的channel不是nil…向nil channel收发会阻塞导致死锁…关闭nil channel会panic(close of nil channel)」

## 一句话总述
**nil channel（未初始化的 channel 零值）**的操作有明确后果：向其**发送或接收都会永久阻塞**（在当前 goroutine 中则死锁），而**关闭 nil channel 会直接 panic**（`close of nil channel`）。关键区分——阻塞/死锁来自"收发"，panic 来自"关闭"，二者机制不同。

## 面试官视角
channel 八股高频题。面试官要看你是否分清"nil channel 的收发行为"与"关闭 nil channel 的 panic"，以及是否知道"关闭后的 channel 不是 nil"（常被混淆）。

## 主问答
**Q（面试官原话）：** 向一个 nil 的 channel 发送或接收数据会怎样？关闭呢？

**A：**

1. **收发 → 阻塞（当前 goroutine 则死锁）**：nil channel 没有底层 `hchan`，对其发送或接收会**永久阻塞**；若收发都在同一 goroutine 中（无他人取走），就演变成**死锁 panic**（`all goroutines are asleep - deadlock`）。
2. **关闭 → panic**：对 nil channel 调用 `close` 会直接抛 `panic: close of nil channel`，与"收发阻塞"是不同机制。
3. **关闭后的 channel 不是 nil**：`close(ch)` 之后 `ch == nil` 仍为 `false`——"nil"指未初始化，"closed"是已初始化后的终态，两者不要混为一谈。

## 追问链（L1~L5）
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | nil channel 收发 | 是否懂阻塞 | 永久阻塞/同goroutine死锁 | 答不出停档 |
| L2 | 关闭 nil 会怎样 | 是否懂 panic | close of nil channel panic | 答不出停档 |
| L3 | 关闭后还是nil吗 | 是否懂 closed≠nil | close后!=nil | 答不出停档 |
| L4 | 为什么收发不panic | 是否懂机制 | 无hchan阻塞非异常 | 答不出停档 |
| L5 | 和closed区别 | 是否懂对比 | 见下卡对比 | 答不出停档 |

## 版本与兼容性
- nil channel 行为自 Go 1.0 稳定；`close(nil)` panic、`nil` 收发阻塞均为语言规定，无版本翻转。
- 注意：nil channel 在 `select` 中对应 case **永不选中**（见 610）。

## 关键代码
```go
var ch chan int // 零值 nil
// ch <- 1        // 阻塞；若同 goroutine 则 deadlock
// <-ch           // 同上
// close(ch)      // panic: close of nil channel

// 结论验证
var a, b chan int
fmt.Println(a == nil) // true：未初始化
b = make(chan int, 1)
close(b)
fmt.Println(b == nil) // false：关闭后并非 nil
```

## 总结与追问预判
- 口诀：**nil 收发阻塞(同goroutine死锁)，nil 关闭 panic；closed 不是 nil**。
- 预判追问："nil channel 在 select 里呢？"→ 永不选中，可用来动态禁用分支（见 610）。

## ⚠️ 原文纠错
源码将 channel 相关术语音译为崩坏词，本卡已统一为规范术语（如 channel/nil/goroutine/死锁/panic/close/make）。纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：channel 需 make、零值 nil、select 中不选中见 610；关闭后的行为见 612/`612-closed-channel-ops`；本卡只讲 nil channel 自身操作后果。
